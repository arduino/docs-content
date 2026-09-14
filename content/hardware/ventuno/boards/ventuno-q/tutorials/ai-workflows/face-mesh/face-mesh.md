---
title: "Real-Time Face Mesh on the VENTUNO Q"
overwriteSidebar: Real-Time Face Mesh
difficulty: advanced
compatible-products: [ventuno-q]
description: "Run live face detection and a 468-point face mesh on the NPU of the Arduino® VENTUNO™ Q with the mediapipe_face model."
tags:
  - AI
  - NPU
  - TFLite
  - Face Mesh
  - Edge AI
  - Linux
  - Qualcomm AI Hub
author: "Karl Söderby, Ernesto Voltaggio"
hardware:
  - hardware/14.ventuno/boards/ventuno-q
software:
  - app-lab
---

## Overview

In this tutorial you will run a live face detection and 468-point face mesh demo on the Arduino® VENTUNO™ Q, using the [`mediapipe_face`](https://aihub.qualcomm.com/models/mediapipe_face?chipsets=qualcomm-qcs8275) model from [Qualcomm® AI Hub](https://aihub.qualcomm.com/). The landmark stage runs on the Qualcomm® Hexagon™ NPU of the board's Qualcomm® Dragonwing™ QCS8275 processor, while the detector stage runs on the CPU.

The demo is a single, self-contained Python script (`face_mesh_camera.py`) that reads from a USB camera, detects each face, and overlays a bounding box, a rotated region-of-interest outline, and the full 468-point mesh in real time.

In this guide we will cover:

1. Powering and accessing the VENTUNO Q.
2. Setting up a Python virtual environment.
3. Downloading the model files directly on the board.
4. Running the face mesh demo on the CPU and on the NPU.

## Hardware & Software Requirements

### Hardware

- [Arduino® VENTUNO™ Q](https://store.arduino.cc/products/ventuno-q)
- [Arduino® USB-C Power Supply (65W)](https://store.arduino.cc/products/usb-c-power-supply-65w), or a 7–24 V DC supply on the power jack
- USB camera connected to the USB-A port, reachable as `/dev/video0`
- A display, keyboard, and mouse\* connected to the board (the script opens a live window on-screen)

<Alert type="info">

**Note:** To use the VENTUNO Q as an SBC, a mouse is not required (but makes it easier).

</Alert>

### Software

- `adb` (Android® Platform Tools) or `ssh` available on your host machine
- Python 3.12 (pre-installed on the VENTUNO Q)

<Alert type="warning">

The VENTUNO Q must be powered with its power supply **before** connecting a USB-C® cable to a host computer, otherwise the board may crash. The recommended power supply is a minimum of 65 W in the range of 7–24 V.

</Alert>

## Accessing the Board Shell

With the board powered from its power jack, you can access the shell (terminal) on the VENTUNO Q using either `adb` or `ssh`.

To connect via `adb`, connect a USB-C® cable between the VENTUNO Q and your computer, then run:

```bash
# Using adb (Android Debug Bridge)
adb shell
```

To connect via `ssh`, ensure the VENTUNO Q is connected to the same network as your computer, then run:

```bash
# Using ssh (Secure Shell)
ssh arduino@<ip-address>
```

If you don't know the board's IP address, connect a keyboard and monitor and run `hostname -I` on the board, or configure Wi-Fi® on the board first with `sudo nmtui`.

<Alert type="info">

For more alternatives to remotely access your board, please see the [Remote Access](https://docs.arduino.cc/tutorials/uno-q/remote-access/) tutorial.

</Alert>

<Alert type="info">

**Note:** Because this demo opens a live camera window on-screen, run it from the board's actual desktop session (a physical monitor and keyboard, or a VNC/X11 session into the board). `adb` and `ssh` are still the easiest way to install dependencies and confirm the script runs before switching to the desktop session to watch the camera feed.

</Alert>

## Setting Up the Python Environment

All commands in this section are run **on the VENTUNO Q**.

### 1. Create a Virtual Environment

Create and activate a Python virtual environment to keep dependencies isolated:

```bash
python3 -m venv ~/.venv
source ~/.venv/bin/activate
```

The `(.venv)` prefix in your prompt confirms the environment is active. Run the `source` command again at the start of each new session.

### 2. Install the Dependencies

This demo needs `opencv-python`, `numpy`, and `ai-edge-litert` (which bundles the TFLite interpreter and the QNN HTP delegate loader used for NPU execution):

```bash
pip install ai-edge-litert==1.3.0 opencv-python numpy
```

NPU execution additionally needs the QNN HTP delegate (`libQnnTFLiteDelegate.so`), which is provided by the **Qualcomm® AI Runtime (QAIRT)**. It is not installed by default and is not pulled in by any `pip` package, so install it from the board's apt repositories:

```bash
sudo apt update
sudo apt install qairt-libs qairt-dsp-binaries
```

Confirm the delegate is present before continuing:

```bash
ls /usr/lib/libQnnTFLiteDelegate.so
```

## Downloading the Model Files

The demo requires three files in addition to the Python script. You can download and prepare all of them **directly on the board** — no host-side transfer needed:

| File | Description | Source |
| ------------------------------------ | ----------------------------------------------- | --------------------------- |
| `face_detector-float.tflite` | Float face detector, runs on the CPU | Qualcomm AI Hub |
| `face_landmark_detector-w8a8.tflite` | Quantized landmark model, runs on the NPU | Qualcomm AI Hub |
| `anchors_face_back.npy` | Anchor table used to decode the detector output | MediaPipePyTorch reference |

First, create and move into a working directory on the board:

```bash
mkdir -p /home/arduino/face-mesh
cd /home/arduino/face-mesh
```

### 1. Fetch the Model Files From AI Hub

The two `.tflite` files come from the [`mediapipe_face`](https://aihub.qualcomm.com/models/mediapipe_face?chipsets=qualcomm-qcs8275) model on Qualcomm AI Hub, fetched with the `qai-hub-models` CLI. Install it (a large package, so this may take a while), then fetch both precisions:

```bash
pip install qai-hub-models

# Float precision -> extracts mediapipe_face-tflite-float/
qai-hub-models fetch mediapipe_face -r tflite -p float -o .

# Quantized precision -> extracts mediapipe_face-tflite-w8a8/
qai-hub-models fetch mediapipe_face -r tflite -p w8a8 -o .
```

Each command extracts a folder containing a `face_detector.tflite` and a `face_landmark_detector.tflite`. We keep the **float** detector and the **w8a8** landmark model (see [Known Limitations](#known-limitations) for why they are mixed), renaming them to match what the script expects:

```bash
cp mediapipe_face-tflite-float/face_detector.tflite ./face_detector-float.tflite
cp mediapipe_face-tflite-w8a8/face_landmark_detector.tflite ./face_landmark_detector-w8a8.tflite
```

<Alert type="warning">

**Important:** `qai-hub-models` depends on `ai-edge-litert>=2.0.2`, so installing it **upgrades** the `ai-edge-litert==1.3.0` you installed earlier. Version 2.x does not work with the QNN HTP delegate: the delegate rejects every convolution with `Failed to validate op ... Conv2d`, silently falls back to the CPU, and ends up *slower* than plain CPU execution because of the added delegation overhead. After fetching the model files, put version 1.3.0 back:

</Alert>

```bash
pip install ai-edge-litert==1.3.0
```

Confirm you are on the working version before running the demo:

```bash
pip show ai-edge-litert | grep Version   # must report 1.3.0
```

<Alert type="info">

**Note:** `pip` prints a line beginning with `ERROR:` reporting that `qai-hub-models` requires a newer `ai-edge-litert`. The downgrade still succeeds, and `qai-hub-models fetch` keeps working afterwards, so this message can be ignored.

</Alert>

Alternatively, keep `qai-hub-models` in a separate virtual environment used only for downloading models, and leave the demo environment pinned to `ai-edge-litert==1.3.0`.

### 2. Download the Anchor Table

The `anchors_face_back.npy` anchor table is not published on AI Hub. It is the static BlazeFace anchor table from the Apache-2.0 [`zmurez/MediaPipePyTorch`](https://github.com/zmurez/MediaPipePyTorch/) reference repository — the same repo `qai-hub-models` uses for its own `mediapipe_face` postprocessing:

```bash
git clone --depth 1 https://github.com/zmurez/MediaPipePyTorch.git /tmp/mediapipepytorch
cp /tmp/mediapipepytorch/anchors_face_back.npy ./anchors_face_back.npy
```

After these steps, your `/home/arduino/face-mesh` directory should contain `face_detector-float.tflite`, `face_landmark_detector-w8a8.tflite`, and `anchors_face_back.npy`.

## Creating the Script

On the VENTUNO Q, move into the working directory and create the script file:

```bash
cd /home/arduino/face-mesh
nano face_mesh_camera.py
```

Paste the full script from the [Code Example](#code-example) section below into the editor. In `nano`, save and exit with `Ctrl+X`, then `Y`, then `Enter`.

## Running the Demo

With the virtual environment active and all files in `/home/arduino/face-mesh`, run the demo from the board's desktop session:

```bash
cd /home/arduino/face-mesh
source ~/.venv/bin/activate            # if not already active

python3 face_mesh_camera.py            # landmark model on the CPU
python3 face_mesh_camera.py --use-npu  # landmark model on the Hexagon NPU
```

A window titled **"Face Mesh"** opens showing the live camera feed with, per detected face:

- a **green** bounding box,
- a **blue** rotated ROI outline, and
- the **468-point** mesh (orange dots).

The on-screen overlay reports the per-model invoke time (`detector=CPU(...)`, `landmark=NPU(...)` or `CPU(...)`) and the total per-frame latency. Press **`q`** in the window to quit.

On a VENTUNO Q running Ubuntu 24.04, averaged over frames where a face was detected:

| Landmark model on | Detector (always CPU) | Landmark model | Total per frame |
| ----------------- | --------------------- | -------------- | --------------- |
| CPU               | 19.3 ms               | 11.13 ms       | ~30 ms          |
| **NPU**           | 18.2 ms               | **0.98 ms**    | **~19 ms**      |

The landmark model is roughly **11x faster** on the NPU. Because the detector stage always runs on the CPU (see [Known Limitations](#known-limitations)), it dominates the frame time in both cases — so the end-to-end improvement is smaller than the landmark speedup on its own, and the detector is where any further optimization would have to happen.

If you launch the script from a remote host (`adb` or `ssh`), you will first need to allow it to render on the display.

On the board itself (not using `adb` or `ssh`), open a terminal and run the following:

```bash
xhost +
export DISPLAY=:0   # replace 0 with your display number
```

This will enable a remote host to run applications on the display. If you do not do this, when running the script from a remote host, you will see `xcb` related error.

## Code Example

The full, self-contained demo is shown below. Save it as `face_mesh_camera.py` in the working directory alongside the three model files.

```python
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
```

## How It Works

Each frame goes through two model stages:

1. **Detection (CPU).** The frame is letterboxed to the detector's input size and passed through the float face detector. The raw output is decoded against the anchor table, filtered by a score threshold, and reduced with non-maximum suppression (NMS) to produce one box and a set of keypoints per face.
2. **Landmark mesh (NPU).** For each detected face, the eye keypoints are used to compute a rotated region of interest. That region is cropped and warped to the landmark model's input size and passed through the quantized landmark model on the Hexagon™ NPU, producing 468 landmarks that are mapped back onto the original frame.

## Known Limitations

- **The detector always runs on the CPU.** The w8a8 (NPU-quantized) asset that AI Hub publishes for the detector sub-model is miscalibrated. Running both detectors over the same 20 camera frames, with the same `DETECT_SCORE_THRESHOLD` of 0.8, the float model returned exactly one box per frame at a stable position and a score of 0.93–0.96, while the w8a8 model returned between two and nine boxes per frame, scored 0.81–0.97, with the highest-scoring box sitting a median of **294 px** away from the float model's (225–345 px across the set) and often partly outside the frame. The failure is therefore not low confidence that could be filtered with a higher threshold — the wrong boxes are confidently wrong. Since there is no NPU-native alternative published for this sub-model, the detector uses the float weights on the CPU while the landmark model (whose w8a8 asset is fine) runs on the NPU.
- **Mouth landmark placement can look slightly off** for some faces. In initial testing, clean-shaven faces showed pixel-accurate mouth landmarks, but a few faces showed lip landmarks that sat slightly under visible facial hair. This has not been fully root-caused and does not appear to be a systematic issue in the ROI or affine math.

## Conclusion

In this tutorial you set up the VENTUNO Q, transferred the `mediapipe_face` model files, and ran a self-contained Python script that performs live face detection and 468-point face mesh estimation, with the landmark stage accelerated on the Qualcomm® Hexagon™ NPU. From here you can build on the mesh output — for example to drive expression tracking, face filters, or gaze-aware interfaces — directly on the Dragonwing™ QCS8275 processor.
