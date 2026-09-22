import sys
import time

import cv2
import numpy as np
from ai_edge_litert.interpreter import Interpreter, load_delegate

# --- SETUP ---
# NOTE: the detector runs on float (CPU) rather than the w8a8 NPU asset on purpose.
# AI Hub's published mediapipe_face w8a8 TFLite detector is poorly calibrated --
# verified by A/B against this float model over identical frames at the same score
# threshold: float returns one stable box per frame at 0.93-0.96, while w8a8 returns
# 2-9 boxes per frame at 0.81-0.97 whose best box sits a median 294px (225-345px)
# off the real face, often partly outside the frame. The landmark model's w8a8 asset
# does not have this problem and runs on the NPU normally.
DETECTOR_MODEL_PATH = 'face_detector-float.tflite'
LANDMARK_MODEL_PATH = 'face_landmark_detector-w8a8.tflite'
ANCHORS_PATH = 'anchors_face_back.npy'

DETECT_SCORE_THRESHOLD = 0.8   # min_detector_face_box_score (MediaPipeFaceApp default)
DETECT_NMS_IOU = 0.3           # nms_iou_threshold
DETECT_SCORE_CLIP = 100.0      # DETECT_SCORE_CLIPPING_THRESHOLD
DETECT_BOX_SCALE = 1.1         # DETECT_DSCALE -- enlarge detector box before landmark crop
LEFT_EYE_KEYPOINT_INDEX = 0
RIGHT_EYE_KEYPOINT_INDEX = 1
LANDMARK_SCORE_THRESHOLD = 0.5  # min_landmark_score

use_npu = True if len(sys.argv) >= 2 and sys.argv[1] == '--use-npu' else False


def make_interpreter(model_path, use_delegate):
    experimental_delegates = []
    if use_delegate:
        experimental_delegates = [load_delegate("libQnnTFLiteDelegate.so", options={"backend_type": "htp"})]
    interp = Interpreter(model_path=model_path, experimental_delegates=experimental_delegates)
    interp.allocate_tensors()
    return interp


# Detector always runs on CPU (see NOTE above); only the landmark model uses --use-npu.
detector = make_interpreter(DETECTOR_MODEL_PATH, use_delegate=False)
landmark_net = make_interpreter(LANDMARK_MODEL_PATH, use_delegate=use_npu)

det_in = detector.get_input_details()
det_out = detector.get_output_details()
lm_in = landmark_net.get_input_details()
lm_out = landmark_net.get_output_details()

_, DET_H, DET_W, _ = det_in[0]['shape']
_, LM_H, LM_W, _ = lm_in[0]['shape']

# det_out/lm_out are indexed positionally below (verified against the exported
# model's output order): det_out = [box_coords_1, box_coords_2, box_scores_1,
# box_scores_2]; lm_out = [scores, landmarks].

# Anchor table: (896, 4) = [x_center, y_center, w, h], normalized [0, 1].
anchors = np.load(ANCHORS_PATH).astype(np.float32).reshape(-1, 2, 2)
NUM_ANCHORS = anchors.shape[0]

# --- NPU WARMUP (landmark model only -- detector runs on CPU) ---
if use_npu:
    print("Warming up NPU...")
    dummy_lm = np.zeros(lm_in[0]['shape'], dtype=lm_in[0]['dtype'])
    for _ in range(3):
        landmark_net.set_tensor(lm_in[0]['index'], dummy_lm)
        landmark_net.invoke()
    print("Warmup done.")


def quantize(values01, detail):
    """values01: float array in the model's natural [0,1]-ish range -> quantized input tensor."""
    scale, zero_point = detail['quantization']
    dtype = detail['dtype']
    if scale:
        q = np.rint(values01 / scale) + zero_point
        info = np.iinfo(dtype)
        return np.clip(q, info.min, info.max).astype(dtype)
    return values01.astype(dtype)


def dequantize(tensor, detail):
    scale, zero_point = detail['quantization']
    if scale:
        return (tensor.astype(np.float32) - float(zero_point)) * float(scale)
    return tensor.astype(np.float32)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))


def letterbox(frame_rgb, dst_h, dst_w):
    """Resize (preserving aspect ratio) + center-pad. Mirrors qai_hub_models.utils.image_processing.resize_pad."""
    h, w = frame_rgb.shape[:2]
    scale = min(dst_h / h, dst_w / w)
    new_h, new_w = int(h * scale), int(w * scale)

    resized = cv2.resize(frame_rgb, (new_w, new_h))
    canvas = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)

    pad_top = (dst_h - new_h) // 2
    pad_left = (dst_w - new_w) // 2
    canvas[pad_top:pad_top + new_h, pad_left:pad_left + new_w] = resized

    return canvas, scale, (pad_left, pad_top)


def undo_letterbox(points_xy, scale, pad):
    """Inverse of letterbox(): maps (x, y) points in the padded canvas back to original-frame coordinates."""
    pad_left, pad_top = pad
    out = points_xy.copy()
    out[..., 0] = (points_xy[..., 0] - pad_left) / scale
    out[..., 1] = (points_xy[..., 1] - pad_top) / scale
    return out


def decode_detections(box_coords, box_scores, img_size):
    """
    Hand-ported from qai_hub_models._shared.mediapipe.utils.mediapipe_detector_postprocess
    + decode_preds_from_anchors.

    box_coords: (NUM_ANCHORS, 16) raw dequantized model output.
        Layout: [box_cx, box_cy, box_w, box_h, kp0_x, kp0_y, ..., kp5_x, kp5_y]
    box_scores: (NUM_ANCHORS,) raw dequantized logits.

    Returns boxes_xyxy (N,4), keypoints (N,6,2), scores (N,) for boxes passing
    the score threshold (NMS is applied separately).
    """
    scores = sigmoid(np.clip(box_scores, -DETECT_SCORE_CLIP, DETECT_SCORE_CLIP))

    coords = box_coords.reshape(NUM_ANCHORS, 8, 2)
    h_size, w_size = img_size
    offset = anchors[:, 0:1, :] * np.array([w_size, h_size], dtype=np.float32)
    scale = anchors[:, 1:2, :]
    mask = (np.arange(8) != 1).reshape(8, 1).astype(np.float32)
    decoded = coords * scale + offset * mask

    flat = decoded.reshape(NUM_ANCHORS, 16)
    cx, cy, bw, bh = flat[:, 0], flat[:, 1], flat[:, 2], flat[:, 3]
    boxes_xyxy = np.stack([cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], axis=-1)
    keypoints = flat[:, 4:].reshape(NUM_ANCHORS, 6, 2)

    keep = scores >= DETECT_SCORE_THRESHOLD
    return boxes_xyxy[keep], keypoints[keep], scores[keep]


def iou(box, boxes):
    xA = np.maximum(box[0], boxes[:, 0])
    yA = np.maximum(box[1], boxes[:, 1])
    xB = np.minimum(box[2], boxes[:, 2])
    yB = np.minimum(box[3], boxes[:, 3])
    inter = np.maximum(0, xB - xA) * np.maximum(0, yB - yA)
    area_a = np.maximum(0, box[2] - box[0]) * np.maximum(0, box[3] - box[1])
    area_b = np.maximum(0, boxes[:, 2] - boxes[:, 0]) * np.maximum(0, boxes[:, 3] - boxes[:, 1])
    return inter / (area_a + area_b - inter + 1e-6)


def nms(boxes, scores, iou_threshold):
    order = np.argsort(-scores)
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        if order.size == 1:
            break
        ious = iou(boxes[i], boxes[order[1:]])
        order = order[1:][ious <= iou_threshold]
    return keep


def compute_roi_corners(box_xyxy, keypoints):
    """
    From a detector box + its keypoints, compute the rotated ROI (4 corners) fed to
    the landmark model. Hand-ported from compute_vector_rotation, box_xyxy_to_xywh,
    and compute_box_corners_with_rotation (DETECT_DXY == 0 for this model, so the
    apply_directional_box_offset step is a no-op and is skipped).
    """
    left_eye = keypoints[LEFT_EYE_KEYPOINT_INDEX]
    right_eye = keypoints[RIGHT_EYE_KEYPOINT_INDEX]
    theta = np.arctan2(right_eye[1] - left_eye[1], right_eye[0] - left_eye[0])

    x0, y0, x1, y1 = box_xyxy
    xc, yc = (x0 + x1) / 2, (y0 + y1) / 2
    w, h = (x1 - x0) * DETECT_BOX_SCALE, (y1 - y0) * DETECT_BOX_SCALE

    unit_square = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]], dtype=np.float32)
    pts = unit_square * np.array([w / 2, h / 2], dtype=np.float32)
    c, s = np.cos(theta), np.sin(theta)
    rot = np.array([[c, -s], [s, c]], dtype=np.float32)
    corners = (rot @ pts.T).T + np.array([xc, yc], dtype=np.float32)
    return corners  # order: top-left, bottom-left, top-right, bottom-right


def run_landmarks(frame_rgb, roi_corners):
    """Crop+rotate the ROI to the landmark model's input size, run it, and map the
    predicted landmarks back to frame_rgb's coordinate space."""
    src = roi_corners[:3]
    dst = np.array([[0, 0], [0, LM_H - 1], [LM_W - 1, 0]], dtype=np.float32)
    affine = cv2.getAffineTransform(src, dst)
    crop = cv2.warpAffine(frame_rgb, affine, (LM_W, LM_H))

    lm_input = quantize(crop.astype(np.float32) / 255.0, lm_in[0])[np.newaxis, ...]
    landmark_net.set_tensor(lm_in[0]['index'], lm_input)
    t0 = time.perf_counter()
    landmark_net.invoke()
    lm_invoke_ms = (time.perf_counter() - t0) * 1000

    score = dequantize(landmark_net.get_tensor(lm_out[0]['index']), lm_out[0]).reshape(-1)[0]
    landmarks = dequantize(landmark_net.get_tensor(lm_out[1]['index']), lm_out[1]).reshape(-1, 3)

    if score < LANDMARK_SCORE_THRESHOLD:
        return None, lm_invoke_ms

    landmarks[:, 0] *= LM_W
    landmarks[:, 1] *= LM_H

    inv_affine = cv2.invertAffineTransform(affine)
    xy = landmarks[:, :2]
    mapped = (inv_affine[:, :2] @ xy.T + inv_affine[:, 2:]).T
    landmarks[:, :2] = mapped
    return landmarks, lm_invoke_ms


def process_frame(frame_bgr):
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    canvas, scale, pad = letterbox(frame_rgb, DET_H, DET_W)

    det_input = quantize(canvas.astype(np.float32) / 255.0, det_in[0])[np.newaxis, ...]
    detector.set_tensor(det_in[0]['index'], det_input)
    t0 = time.perf_counter()
    detector.invoke()
    det_invoke_ms = (time.perf_counter() - t0) * 1000

    c1 = dequantize(detector.get_tensor(det_out[0]['index']), det_out[0]).reshape(-1, 16)
    c2 = dequantize(detector.get_tensor(det_out[1]['index']), det_out[1]).reshape(-1, 16)
    s1 = dequantize(detector.get_tensor(det_out[2]['index']), det_out[2]).reshape(-1)
    s2 = dequantize(detector.get_tensor(det_out[3]['index']), det_out[3]).reshape(-1)
    box_coords = np.concatenate([c1, c2], axis=0)
    box_scores = np.concatenate([s1, s2], axis=0)

    boxes, keypoints, scores = decode_detections(box_coords, box_scores, (DET_H, DET_W))
    keep = nms(boxes, scores, DETECT_NMS_IOU)
    boxes, keypoints = boxes[keep], keypoints[keep]

    # Map detector-space (letterboxed canvas) coordinates back to the original frame.
    boxes = undo_letterbox(boxes.reshape(-1, 2, 2), scale, pad).reshape(-1, 4)
    keypoints = undo_letterbox(keypoints, scale, pad)

    faces = []
    lm_invoke_ms_total = 0.0
    for box, kp in zip(boxes, keypoints):
        roi_corners = compute_roi_corners(box, kp)
        landmarks, lm_ms = run_landmarks(frame_rgb, roi_corners)
        lm_invoke_ms_total += lm_ms
        faces.append((box, roi_corners, landmarks))

    return faces, det_invoke_ms, lm_invoke_ms_total


# --- MAIN LOOP ---
landmark_mode = "NPU" if use_npu else "CPU"
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    t_start = time.perf_counter()
    faces, det_invoke_ms, lm_invoke_ms = process_frame(frame)
    total_ms = (time.perf_counter() - t_start) * 1000

    for box, roi_corners, landmarks in faces:
        x0, y0, x1, y1 = box.astype(int)
        cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)

        quad = roi_corners[[0, 2, 3, 1]].astype(int)  # TL, TR, BR, BL -> valid polygon order
        cv2.polylines(frame, [quad], isClosed=True, color=(255, 0, 0), thickness=1)

        if landmarks is not None:
            for (lx, ly, _lz) in landmarks:
                cv2.circle(frame, (int(lx), int(ly)), 1, (0, 128, 255), -1)

    label = (f"detector=CPU({det_invoke_ms:.1f}ms)  landmark={landmark_mode}({lm_invoke_ms:.1f}ms)  "
             f"total={total_ms:.1f}ms  faces={len(faces)}")
    cv2.putText(frame, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow('Face Mesh', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
