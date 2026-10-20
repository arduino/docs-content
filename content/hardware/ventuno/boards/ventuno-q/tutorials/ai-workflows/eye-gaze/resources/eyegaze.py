#!/usr/bin/env python3
"""Real-time eye gaze estimation on the Arduino VENTUNO Q (Qualcomm AI Hub EyeGaze).

Per frame:

    camera frame
      -> MediaPipe face detector
      -> MediaPipe face landmarks        -> the four eye corners
      -> one level 160x96 crop per eye   -> EyeGaze (EyeNet), once per eye
      -> 34 eye landmarks per eye + one gaze direction from both, smoothed and drawn

Usage:
    python eyegaze.py                       # first USB webcam, models on the NPU
    python eyegaze.py --cpu                 # same, on the CPU (slow)
    python eyegaze.py --source 2            # /dev/video2
    python eyegaze.py --source clip.mp4 --save out.mp4 --headless

Keys: q/Esc quit, c calibrate (look into the camera first), x clear calibration,
      m mirror, p eye previews, s smoothing.
"""
import argparse
import math
import os
import threading
import time
from pathlib import Path

import cv2
import numpy as np
import onnxruntime as ort
from ai_edge_litert.interpreter import Interpreter, load_delegate

HERE = Path(__file__).resolve().parent
MODELS = HERE / "models"
GAZE_SOURCE_MODEL = MODELS / "eyegaze-onnx-w8a16" / "eyegaze.onnx"   # as downloaded from AI Hub
GAZE_MODEL = MODELS / "eyegaze_npu.onnx"                             # made by prepare_model.py
FACE_DETECTOR = MODELS / "mediapipe_face-tflite-float" / "face_detector.tflite"
FACE_LANDMARKS = MODELS / "mediapipe_face-tflite-float" / "face_landmark_detector.tflite"
FACE_ANCHORS = MODELS / "anchors_face_back.npy"

# --- EyeGaze model I/O (models/eyegaze-onnx-w8a16/metadata.json) ---
EYE_W, EYE_H = 160, 96
INPUT_MAX = 65535.0                      # uint16 input, scale 1/65535: 0..65535 <-> 0..1
HEATMAP_SCALE, HEATMAP_ZERO = 0.000017086889783968218, 11910
GAZE_SCALE, GAZE_ZERO = 0.000015449146303581074, 38104
HEATMAP_TO_CROP = 2.0                    # heatmaps are 80x48, half the crop resolution
SOFTARGMAX_BETA = 100.0                  # same sharpness the model uses internally
# The 34 landmarks: eyelid outline, iris outline, iris centre, eyeball centre.
EYELID, IRIS, IRIS_CENTRE = slice(0, 16), slice(16, 32), 32

# --- Eye crops ---
# MediaPipe face-mesh indices. "right"/"left" are the subject's own right and left;
# corner pairs are ordered left-to-right in the (unmirrored) image.
RIGHT_EYE_CORNERS = (33, 133)
LEFT_EYE_CORNERS = (362, 263)
RIGHT_EYE_CONTOUR = (33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246)
LEFT_EYE_CONTOUR = (362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398)
EYE_CROP_WIDTH = 1.5                     # crop width, in corner-to-corner distances
# Mean iris heatmap peak: ~0.5 for an open eye, <0.1 when closed or not an eye.
# An eye appears above the first value and stays until it drops below the second.
EYE_CONFIDENCE_ON, EYE_CONFIDENCE_OFF = 0.2, 0.12

# --- Face tracking ---
DETECT_THRESHOLD = 0.6
DETECT_ROI_SCALE = 1.5                   # detector box -> landmark crop
TRACK_ROI_SCALE = 1.5                    # previous landmarks' bounding box -> landmark crop
LANDMARK_THRESHOLD = 0.5
MESH_PASSES = 2

# --- Smoothing (One Euro filter: cutoff = min_cutoff + beta * speed) ---
CORNER_FILTER = dict(min_cutoff=0.3, beta=10.0)      # eye corners, in face sizes
LANDMARK_FILTER = dict(min_cutoff=0.5, beta=0.1)     # eye landmarks, in pixels
GAZE_FILTER = dict(min_cutoff=0.3, beta=3.0)         # pitch/yaw, in radians
IMBALANCE_RATE = 0.05                    # per frame, for the left/right difference estimate

# --- Drawing (BGR) ---
EYELID_COLOR = (255, 220, 120)
IRIS_COLOR = (120, 255, 120)
GAZE_COLOR = (60, 60, 255)
ARROW_LENGTH = 3.0                       # in eye widths, for a gaze at 90 degrees
SHIFT = 4                                # draw with 1/16 px precision so overlays glide


class OneEuroFilter:
    """Low-pass filter whose cutoff rises with speed: steady at rest, quick to follow motion."""

    def __init__(self, min_cutoff, beta, d_cutoff=1.0):
        self.min_cutoff, self.beta, self.d_cutoff = min_cutoff, beta, d_cutoff
        self.x = self.dx = None

    @staticmethod
    def _alpha(cutoff, dt):
        return 1.0 / (1.0 + 1.0 / (2.0 * math.pi * cutoff * dt))

    def __call__(self, x, dt):
        x = np.asarray(x, dtype=np.float64)
        if self.x is None or dt <= 0:
            self.x, self.dx = x, np.zeros_like(x)
            return x
        self.dx += self._alpha(self.d_cutoff, dt) * ((x - self.x) / dt - self.dx)
        speed = np.linalg.norm(self.dx, axis=-1, keepdims=True)
        self.x = self.x + self._alpha(self.min_cutoff + self.beta * speed, dt) * (x - self.x)
        return self.x


def crop_transform(centre, angle, scale, out_w, out_h):
    """Affine (2x3) taking frame pixels to an upright out_w x out_h crop centred on
    `centre`, plus its inverse. `angle` is the tilt, in the frame, of the crop's x axis."""
    c, s = math.cos(angle) * scale, math.sin(angle) * scale
    forward = np.array([[c, s, 0.0], [-s, c, 0.0]])
    forward[:, 2] = np.array([out_w / 2.0, out_h / 2.0]) - forward[:, :2] @ centre
    return forward, cv2.invertAffineTransform(forward)


def transform_points(affine, points):
    return points @ affine[:, :2].T + affine[:, 2]


def litert_model(path, use_npu):
    if use_npu:
        # htp_performance_mode 2 = "burst", the fastest Hexagon clock profile.
        delegates = [load_delegate("libQnnTFLiteDelegate.so",
                                   options={"backend_type": "htp", "htp_performance_mode": "2"})]
        interpreter = Interpreter(model_path=str(path), experimental_delegates=delegates)
    else:
        interpreter = Interpreter(model_path=str(path), num_threads=4)
    interpreter.allocate_tensors()
    return interpreter


class FaceTracker:
    """Finds one face and returns its 468 MediaPipe mesh landmarks in frame pixels."""

    def __init__(self, use_npu):
        self.detector = litert_model(FACE_DETECTOR, use_npu)
        self.mesh = litert_model(FACE_LANDMARKS, use_npu)
        self.det_in = self.detector.get_input_details()[0]
        self.mesh_in = self.mesh.get_input_details()[0]
        self.det_size = int(self.det_in["shape"][1])
        self.mesh_size = int(self.mesh_in["shape"][1])
        # Detector outputs: box coordinates (.., 16) and scores (.., 1) for two anchor
        # grids; the larger grid comes first in the anchor table.
        outs = sorted(self.detector.get_output_details(), key=lambda d: -int(d["shape"][1]))
        self.det_coords = [d["index"] for d in outs if d["shape"][-1] == 16]
        self.det_scores = [d["index"] for d in outs if d["shape"][-1] == 1]
        outs = self.mesh.get_output_details()
        self.mesh_score = next(d["index"] for d in outs if np.prod(d["shape"]) == 1)
        self.mesh_points = next(d["index"] for d in outs if np.prod(d["shape"]) > 1)
        # (896, 2, 2): [[x_centre, y_centre], [w, h]] per anchor, normalised to 0..1.
        self.anchors = np.load(FACE_ANCHORS).astype(np.float32).reshape(-1, 2, 2)
        self.roi = None  # (centre xy, size, angle) of the landmark crop

    def _detect(self, rgb):
        h, w = rgb.shape[:2]
        scale = self.det_size / max(h, w)
        new_w, new_h = round(w * scale), round(h * scale)
        pad_x, pad_y = (self.det_size - new_w) // 2, (self.det_size - new_h) // 2
        canvas = np.zeros((self.det_size, self.det_size, 3), np.float32)
        canvas[pad_y:pad_y + new_h, pad_x:pad_x + new_w] = cv2.resize(rgb, (new_w, new_h)) / 255.0
        self.detector.set_tensor(self.det_in["index"], canvas[None])
        self.detector.invoke()
        scores = np.concatenate([self.detector.get_tensor(i).reshape(-1) for i in self.det_scores])
        best = int(np.argmax(scores))
        if scores[best] < math.log(DETECT_THRESHOLD / (1.0 - DETECT_THRESHOLD)):  # logit
            return None
        coords = np.concatenate([self.detector.get_tensor(i).reshape(-1, 16) for i in self.det_coords])
        # Anchor-relative [box centre, box size, right eye, left eye, nose, mouth, ears].
        offset, size = self.anchors[best]
        points = coords[best].reshape(8, 2) * size
        points[[0, 2, 3]] += offset * self.det_size
        points[[0, 2, 3]] = (points[[0, 2, 3]] - (pad_x, pad_y)) / scale
        box_size = points[1].max() / scale
        eye_a, eye_b = points[2], points[3]
        angle = math.atan2(eye_b[1] - eye_a[1], eye_b[0] - eye_a[0])
        return points[0].astype(np.float64), box_size * DETECT_ROI_SCALE, angle

    def _landmarks(self, rgb):
        """Runs the landmark model on the current ROI and moves the ROI onto the result."""
        centre, size, angle = self.roi
        forward, inverse = crop_transform(centre, angle, self.mesh_size / size,
                                          self.mesh_size, self.mesh_size)
        crop = cv2.warpAffine(rgb, forward, (self.mesh_size, self.mesh_size),
                              borderMode=cv2.BORDER_REPLICATE)
        self.mesh.set_tensor(self.mesh_in["index"], (crop.astype(np.float32) / 255.0)[None])
        self.mesh.invoke()
        if float(self.mesh.get_tensor(self.mesh_score).reshape(-1)[0]) < LANDMARK_THRESHOLD:
            self.roi = None
            return None
        points = self.mesh.get_tensor(self.mesh_points).reshape(-1, 3)[:, :2] * self.mesh_size
        points = transform_points(inverse, points.astype(np.float64))

        lo, hi = points.min(axis=0), points.max(axis=0)
        eye_a, eye_b = points[RIGHT_EYE_CORNERS[0]], points[LEFT_EYE_CORNERS[1]]
        self.roi = ((lo + hi) / 2.0, float((hi - lo).max()) * TRACK_ROI_SCALE,
                    math.atan2(eye_b[1] - eye_a[1], eye_b[0] - eye_a[0]))
        return points

    def __call__(self, rgb):
        # Detect on every frame (about 1 ms on the NPU). Following the previous frame's
        # landmarks alone can slide onto a hand or a beard and stay there; that is only
        # the fallback for frames where the detector misses, e.g. a turned head.
        self.roi = self._detect(rgb) or self.roi
        if self.roi is None:
            return None
        # Twice: the first pass centres the ROI on the face, the second measures on
        # that well-centred crop. The landmarks shift slightly with the face's
        # position in the crop otherwise.
        for _ in range(MESH_PASSES):
            points = self._landmarks(rgb)
            if points is None:
                return None
        return points


class EyeGaze:
    """Qualcomm AI Hub EyeGaze (EyeNet): one eye crop in, eye landmarks and gaze out."""

    def __init__(self, use_npu):
        if not GAZE_MODEL.exists():
            from prepare_model import convert
            convert(GAZE_SOURCE_MODEL, GAZE_MODEL)
        if use_npu:
            providers = [("QNNExecutionProvider",
                          {"backend_type": "htp", "htp_performance_mode": "burst"})]
        else:
            providers = ["CPUExecutionProvider"]
        self.session = ort.InferenceSession(str(GAZE_MODEL), providers=providers)
        self.on_npu = self.session.get_providers()[0] == "QNNExecutionProvider"
        self._xs = np.arange(EYE_W // 2, dtype=np.float32)
        self._ys = np.arange(EYE_H // 2, dtype=np.float32)

    def __call__(self, gray, centre, width, roll, flip):
        """gray: full frame. centre/width/roll: where the eye is, how wide (corner to
        corner, pixels) and how tilted. flip: True for the subject's right eye. EyeNet
        only knows left eyes, so right eyes are mirrored on the way in and back on
        the way out.

        Returns (landmarks (34, 2) in frame pixels, [pitch, yaw] in radians relative
        to the level crop, confidence, the crop).
        """
        forward, inverse = crop_transform(centre, roll, EYE_W / (EYE_CROP_WIDTH * width), EYE_W, EYE_H)
        # Replicated border: black beyond the frame edge would wreck the equalisation.
        crop = cv2.equalizeHist(cv2.warpAffine(gray, forward, (EYE_W, EYE_H),
                                               borderMode=cv2.BORDER_REPLICATE))
        image = crop[:, ::-1] if flip else crop
        tensor = (image.astype(np.float32) * (INPUT_MAX / 255.0)).astype(np.uint16)[None]
        heatmaps, gaze = self.session.run(["heatmaps", "gaze_pitchyaw"], {"image": tensor})

        # Landmarks: soft-argmax over the last hourglass stack's heatmaps. Doing it here
        # in float is ~3x closer to the reference than the NPU's own 16-bit softmax.
        maps = (heatmaps[0, -1].astype(np.float32) - HEATMAP_ZERO) * HEATMAP_SCALE
        peaks = maps.max(axis=(1, 2))
        weights = np.exp(SOFTARGMAX_BETA * (maps - peaks[:, None, None]))
        weights /= weights.sum(axis=(1, 2), keepdims=True)
        points = np.stack([weights.sum(axis=1) @ self._xs, weights.sum(axis=2) @ self._ys],
                          axis=1).astype(np.float64) * HEATMAP_TO_CROP
        pitch_yaw = (gaze[0].astype(np.float64) - GAZE_ZERO) * GAZE_SCALE
        if flip:
            points[:, 0] = EYE_W - points[:, 0]
            pitch_yaw[1] = -pitch_yaw[1]
        return transform_points(inverse, points), pitch_yaw, float(peaks[IRIS].mean()), crop


def gaze_vector(pitch, yaw, roll):
    """Unit vector in camera space (x right, y down, z away from the camera) for a
    gaze measured in an eye crop that is tilted by `roll` in the frame."""
    x, y = -math.cos(pitch) * math.sin(yaw), math.sin(pitch)
    c, s = math.cos(roll), math.sin(roll)
    return np.array([c * x - s * y, s * x + c * y, -math.cos(pitch) * math.cos(yaw)])


class Eye:
    """One eye's filters and latest result."""

    def __init__(self, corners, flip):
        self.corners, self.flip = list(corners), flip
        self.reset()

    def reset(self):
        self.landmark_filter = OneEuroFilter(**LANDMARK_FILTER)
        self.gaze_filter = OneEuroFilter(**GAZE_FILTER)
        self.landmarks = self.pitch_yaw = self.crop = None
        self.width = self.roll = 0.0
        self.visible = False


class GazePipeline:
    def __init__(self, use_npu=True, smoothing=True):
        self.tracker = FaceTracker(use_npu)
        self.eyegaze = EyeGaze(use_npu)
        self.smoothing = smoothing
        self.eyes = [Eye(RIGHT_EYE_CORNERS, flip=True), Eye(LEFT_EYE_CORNERS, flip=False)]
        self.corner_filter = OneEuroFilter(**CORNER_FILTER)
        self.imbalance = np.zeros(2)   # running (left - right) / 2 of [pitch, yaw]
        self.offset = np.zeros(2)      # calibration: [pitch, yaw] read when looking at the camera
        self.pitch_yaw = self.gaze = None
        self.face_ms = self.gaze_ms = 0.0

    def _eye_corners(self, mesh, dt):
        """The four eye corners, steadied. The model reads gaze from where the iris
        sits in the crop (about 2.5 degrees per pixel at this scale), so the corners
        that place the crop must not jitter, nor lag behind a moving head. Hence they
        are filtered relative to the face (its centroid, size and tilt, which average
        over many landmarks) rather than in frame coordinates."""
        corners = mesh[[c for eye in self.eyes for c in eye.corners]]
        if not self.smoothing:
            return corners
        origin = mesh.mean(axis=0)
        size = math.sqrt(((mesh - origin) ** 2).sum(axis=1).mean())
        across = mesh[list(LEFT_EYE_CONTOUR)].mean(axis=0) - mesh[list(RIGHT_EYE_CONTOUR)].mean(axis=0)
        c, s = across / np.linalg.norm(across)
        to_face = np.array([[c, s], [-s, c]])
        in_face = self.corner_filter((corners - origin) @ to_face.T / size, dt)
        return in_face * size @ to_face + origin

    def process(self, frame, dt):
        """Updates self.eyes and self.gaze from a BGR frame taken `dt` seconds after
        the previous one."""
        t0 = time.perf_counter()
        mesh = self.tracker(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        t1 = time.perf_counter()
        self.face_ms = (t1 - t0) * 1000.0
        if mesh is None:
            for eye in self.eyes:
                eye.reset()
            self.corner_filter = OneEuroFilter(**CORNER_FILTER)
            self.pitch_yaw = self.gaze = None
            self.gaze_ms = 0.0
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = self._eye_corners(mesh, dt).reshape(2, 2, 2)
        for eye, (a, b) in zip(self.eyes, corners):
            eye.width = float(np.linalg.norm(b - a))
            eye.roll = math.atan2(b[1] - a[1], b[0] - a[0])
            landmarks, pitch_yaw, confidence, eye.crop = self.eyegaze(gray, (a + b) / 2.0, eye.width,
                                                                      eye.roll, eye.flip)
            was_visible = eye.visible
            eye.visible = confidence >= (EYE_CONFIDENCE_OFF if was_visible else EYE_CONFIDENCE_ON)
            if not eye.visible:
                continue
            if self.smoothing:
                if not was_visible:  # don't glide in from wherever the eye was before a blink
                    eye.landmark_filter = OneEuroFilter(**LANDMARK_FILTER)
                    eye.gaze_filter = OneEuroFilter(**GAZE_FILTER)
                landmarks = eye.landmark_filter(landmarks, dt)
                pitch_yaw = eye.gaze_filter(pitch_yaw, dt)
            eye.landmarks, eye.pitch_yaw = landmarks, pitch_yaw
        self._fuse()
        self.gaze_ms = (time.perf_counter() - t1) * 1000.0

    def _fuse(self):
        """One gaze direction from both eyes.

        The right eye goes through the model mirrored, so any constant bias in the
        model's yaw (or in where the face mesh puts the eye corners) comes out with
        opposite signs in the two eyes: on its own each eye is several degrees off
        and the two arrows splay apart. Their mean cancels that. The running half
        difference is kept so that one eye alone can be corrected the same way while
        the other is hidden."""
        right, left = self.eyes
        if right.visible and left.visible:
            self.imbalance += IMBALANCE_RATE * ((left.pitch_yaw - right.pitch_yaw) / 2.0 - self.imbalance)
            self.pitch_yaw, roll = (left.pitch_yaw + right.pitch_yaw) / 2.0, (left.roll + right.roll) / 2.0
        elif left.visible:
            self.pitch_yaw, roll = left.pitch_yaw - self.imbalance, left.roll
        elif right.visible:
            self.pitch_yaw, roll = right.pitch_yaw + self.imbalance, right.roll
        else:
            self.pitch_yaw = self.gaze = None
            return
        self.gaze = gaze_vector(*(self.pitch_yaw - self.offset), roll)

    def calibrate(self):
        """Call while the user looks into the camera: the current reading becomes zero."""
        if self.pitch_yaw is not None:
            self.offset = self.pitch_yaw.copy()

    def clear_calibration(self):
        self.offset = np.zeros(2)

    def gaze_angles(self):
        """(pitch, yaw) in degrees, or None. Seen from the camera: positive pitch
        looks down, positive yaw looks to the image's left."""
        if self.gaze is None:
            return None
        x, y, z = self.gaze
        return math.degrees(math.atan2(y, math.hypot(x, z))), math.degrees(math.atan2(-x, -z))


def fixed(points):
    return np.round(np.asarray(points) * (1 << SHIFT)).astype(np.int32)


def draw_eye(frame, eye, gaze):
    if not eye.visible:
        return
    thickness = max(1, round(frame.shape[0] / 400))
    cv2.polylines(frame, [fixed(eye.landmarks[EYELID])], True, EYELID_COLOR, thickness, cv2.LINE_AA, SHIFT)
    cv2.polylines(frame, [fixed(eye.landmarks[IRIS])], True, IRIS_COLOR, thickness, cv2.LINE_AA, SHIFT)
    start = eye.landmarks[IRIS_CENTRE]
    end = start + gaze[:2] * ARROW_LENGTH * eye.width
    cv2.arrowedLine(frame, tuple(fixed(start).tolist()), tuple(fixed(end).tolist()), GAZE_COLOR,
                    thickness + 1, cv2.LINE_AA, SHIFT, tipLength=0.25)
    cv2.circle(frame, tuple(fixed(start).tolist()), (thickness + 1) << SHIFT, GAZE_COLOR, -1,
               cv2.LINE_AA, SHIFT)


def draw_text(frame, text, origin, scale=0.6):
    cv2.putText(frame, text, origin, cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 4, cv2.LINE_AA)
    cv2.putText(frame, text, origin, cv2.FONT_HERSHEY_SIMPLEX, scale, (255, 255, 255), 1, cv2.LINE_AA)


def render(frame, pipeline, fps, mirror, previews):
    for eye in pipeline.eyes:
        draw_eye(frame, eye, pipeline.gaze)
    if mirror:
        frame = cv2.flip(frame, 1)

    device = "NPU" if pipeline.eyegaze.on_npu else "CPU"
    draw_text(frame, f"{fps:4.1f} fps   face {pipeline.face_ms:4.1f} ms   gaze {pipeline.gaze_ms:4.1f} ms   {device}",
              (12, 26))
    angles = pipeline.gaze_angles()
    if angles is not None:
        draw_text(frame, f"pitch {angles[0]:+5.1f}   yaw {angles[1]:+5.1f}  deg", (12, 52))
    elif all(eye.crop is None for eye in pipeline.eyes):
        draw_text(frame, "no face", (12, 52))
    draw_text(frame, "q quit   c calibrate (look into the camera)   x clear   m mirror   p previews   s smoothing",
              (12, frame.shape[0] - 12), 0.45)

    if previews:
        # What the model sees. Ordered as on screen: the eye drawn on the left goes left.
        eyes = pipeline.eyes[::-1] if mirror else pipeline.eyes
        for i, eye in enumerate(eyes):
            if eye.crop is None:
                continue
            x = frame.shape[1] - (len(eyes) - i) * (EYE_W + 8)
            crop = eye.crop[:, ::-1] if mirror else eye.crop
            frame[8:8 + EYE_H, x:x + EYE_W] = cv2.cvtColor(crop, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(frame, (x, 8), (x + EYE_W - 1, 8 + EYE_H - 1), (255, 255, 255), 1)
    return frame


def find_usb_camera():
    """Index of the first USB (UVC) capture node. On the VENTUNO Q /dev/video0 and
    /dev/video1 belong to the onboard camera pipeline and never deliver frames."""
    nodes = sorted(Path("/sys/class/video4linux").glob("video*"), key=lambda p: int(p.name[5:]))
    for node in nodes:
        driver = os.path.basename(os.path.realpath(node / "device" / "driver"))
        # A UVC camera exposes two nodes; index 0 is video, index 1 is metadata.
        if driver == "uvcvideo" and (node / "index").read_text().strip() == "0":
            return int(node.name[5:])
    return None


class Camera:
    """Webcam read on a background thread, so the main loop always gets the newest
    frame instead of one that has been waiting in the driver's queue."""

    def __init__(self, index, width, height):
        self.cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
        # MJPG: uncompressed YUYV is limited to a few fps above 640x480 over USB 2.
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        if not self.cap.isOpened():
            raise SystemExit(f"Could not open /dev/video{index}.")
        self.fps = 30.0
        self._frame = self._time = None
        self._count = self._taken = 0
        self._running = True
        self._new = threading.Condition()
        self._thread = threading.Thread(target=self._reader, daemon=True)
        self._thread.start()

    def _reader(self):
        while self._running:
            ok, frame = self.cap.read()
            with self._new:
                self._frame, self._time = (frame if ok else None), time.monotonic()
                self._count += 1
                self._new.notify()
            if not ok:
                return

    def read(self):
        """Blocks until there is a frame newer than the last one returned.
        Returns (frame, capture time in seconds), or (None, None) if the camera stops."""
        with self._new:
            if not self._new.wait_for(lambda: self._count != self._taken, timeout=5.0):
                return None, None
            self._taken = self._count
            return self._frame, self._time

    def release(self):
        self._running = False
        self._thread.join(timeout=2.0)
        self.cap.release()


class VideoFile:
    """Image or video file, played frame by frame (never dropping any)."""

    def __init__(self, path):
        self.cap = cv2.VideoCapture(path)
        if not self.cap.isOpened():
            raise SystemExit(f"Could not open {path}.")
        self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 30.0
        self.is_image = self.cap.get(cv2.CAP_PROP_FRAME_COUNT) <= 1
        self._count = 0

    def read(self):
        ok, frame = self.cap.read()
        self._count += 1
        return (frame, self._count / self.fps) if ok else (None, None)

    def release(self):
        self.cap.release()


def open_source(args):
    if args.source is not None and not args.source.isdigit():
        return VideoFile(args.source)
    index = int(args.source) if args.source is not None else find_usb_camera()
    if index is None:
        raise SystemExit("No USB webcam found. Plug one in, or pass --source N (see `ls /dev/video*`) "
                         "or --source FILE.")
    print(f"Camera: /dev/video{index}")
    return Camera(index, args.width, args.height)


def parse_args():
    parser = argparse.ArgumentParser(description="Real-time eye gaze estimation (Qualcomm AI Hub EyeGaze).")
    parser.add_argument("--source", help="camera index, or an image/video file (default: first USB webcam)")
    parser.add_argument("--cpu", action="store_true", help="run the models on the CPU instead of the NPU")
    parser.add_argument("--use-npu", action="store_true", help=argparse.SUPPRESS)  # now the default
    parser.add_argument("--width", type=int, default=1280, help="camera capture width (default 1280)")
    parser.add_argument("--height", type=int, default=720, help="camera capture height (default 720)")
    parser.add_argument("--no-mirror", action="store_true", help="don't mirror the view")
    parser.add_argument("--no-smoothing", action="store_true", help="show raw model output")
    parser.add_argument("--save", metavar="PATH", help="write the annotated output to an image/video file")
    parser.add_argument("--headless", action="store_true", help="don't open a window")
    return parser.parse_args()


def main():
    args = parse_args()
    ort.set_default_logger_severity(3)
    source = open_source(args)
    is_image = getattr(source, "is_image", False)
    pipeline = GazePipeline(use_npu=not args.cpu, smoothing=not args.no_smoothing)
    print(f"Models on the {'NPU' if pipeline.eyegaze.on_npu else 'CPU'}. Press q to quit.")

    # Mirrored like a mirror for a live camera; files are shown as they are.
    mirror = isinstance(source, Camera) and not args.no_mirror
    previews = True
    writer = None
    fps = 0.0
    last_time = last_loop = None
    try:
        while True:
            frame, now = source.read()
            if frame is None:
                break
            pipeline.process(frame, 0.0 if last_time is None else now - last_time)
            last_time = now

            loop = time.perf_counter()
            if last_loop is not None:
                rate = 1.0 / max(loop - last_loop, 1e-6)
                fps = rate if fps == 0.0 else 0.9 * fps + 0.1 * rate
            last_loop = loop
            output = render(frame, pipeline, fps, mirror, previews)

            if args.save:
                if is_image:
                    cv2.imwrite(args.save, output)
                else:
                    if writer is None:
                        writer = cv2.VideoWriter(args.save, cv2.VideoWriter_fourcc(*"mp4v"), source.fps,
                                                 (output.shape[1], output.shape[0]))
                    writer.write(output)
            if not args.headless:
                cv2.imshow("EyeGaze", output)
                key = cv2.waitKey(0 if is_image else 1) & 0xFF
                if key in (ord("q"), 27):
                    break
                if key == ord("c"):
                    pipeline.calibrate()
                elif key == ord("x"):
                    pipeline.clear_calibration()
                elif key == ord("m"):
                    mirror = not mirror
                elif key == ord("p"):
                    previews = not previews
                elif key == ord("s"):
                    pipeline.smoothing = not pipeline.smoothing
    except KeyboardInterrupt:
        pass
    finally:
        source.release()
        if writer is not None:
            writer.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
