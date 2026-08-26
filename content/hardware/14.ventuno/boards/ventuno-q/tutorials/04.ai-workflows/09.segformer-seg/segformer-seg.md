---
title: "Real-Time Semantic Segmentation on the VENTUNO Q"
overwriteSidebar: Semantic Segmentation
difficulty: intermediate
compatible-products: [ventuno-q]
description: "Learn how to run live semantic segmentation on the NPU of the Arduino® VENTUNO™ Q using the SegFormer model from Qualcomm AI Hub."
tags:
  - AI
  - NPU
  - TFLite
  - Segmentation
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

In this tutorial you will run a live semantic segmentation demo on the Arduino® VENTUNO™ Q, using the [`segformer_base`](https://aihub.qualcomm.com/models/segformer_base?chipsets=qualcomm-qcs8275) model from [Qualcomm® AI Hub](https://aihub.qualcomm.com/). SegFormer is a transformer-based segmentation model (`nvidia/segformer-b0-finetuned-ade-512-512`) that classifies every pixel into one of 150 ADE20K scene categories (wall, floor, person, chair, sky, and so on). The model runs entirely on the Qualcomm® Hexagon™ NPU of the board's Qualcomm® Dragonwing™ QCS8275 processor.

The demo is a single, self-contained Python script (`segformer_camera.py`) that reads from a USB camera and overlays a color-tinted segmentation mask on the live feed in real time, with a small legend of the most common classes in view.

In this guide we will cover:

1. Powering and accessing the VENTUNO Q.
2. Setting up a Python virtual environment.
3. Downloading the model file directly on the board.
4. Running the segmentation demo on the CPU and on the NPU.

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

<Alert type="warning">

__Note:__ Because this demo opens a live camera window on-screen, run it from the board's actual desktop session (a physical monitor and keyboard, or a VNC/X11 session into the board). `adb` and `ssh` are still the easiest way to install dependencies and confirm the script runs before switching to the desktop session to watch the camera feed.

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

## Downloading the Model File

The demo requires a single model file in addition to the Python script. You can download and prepare it **directly on the board** — no host-side transfer needed:

| File | Description | Source |
| ------------------------------ | -------------------------------------------------- | --------------- |
| `segformer_base-w8a8.tflite` | Quantized segmentation model, runs on the NPU | Qualcomm AI Hub |

First, create and move into a working directory on the board:

```bash
mkdir -p /home/arduino/segformer-seg
cd /home/arduino/segformer-seg
```

The model comes from the [`segformer_base`](https://aihub.qualcomm.com/models/segformer_base?chipsets=qualcomm-qcs8275) model on Qualcomm AI Hub, fetched with the `qai-hub-models` CLI. Install it (a large package, so this may take a while), then fetch the quantized precision:

```bash
pip install qai-hub-models

# Quantized precision -> extracts segformer_base-tflite-w8a8/
qai-hub-models fetch segformer_base -r tflite -p w8a8 -o .
```

This extracts a `segformer_base-tflite-w8a8/` folder containing a single `segformer_base.tflite`. Unlike a multi-stage model, this is a single-stage model, so there are no extra files to discard. Rename it to match what the script expects:

```bash
cp segformer_base-tflite-w8a8/segformer_base.tflite ./segformer_base-w8a8.tflite
```

After this step, your `/home/arduino/segformer-seg` directory should contain `segformer_base-w8a8.tflite`.

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

## Creating the Script

On the VENTUNO Q, move into the working directory and create the script file:

```bash
cd /home/arduino/segformer-seg
nano segformer_camera.py
```

Paste the full script from the [Code Example](#code-example) section below into the editor. In `nano`, save and exit with `Ctrl+X`, then `Y`, then `Enter`.

## Running the Demo

With the virtual environment active and all files in `/home/arduino/segformer-seg`, run the demo from the board's desktop session:

```bash
cd /home/arduino/segformer-seg
source ~/.venv/bin/activate            # if not already active

python3 segformer_camera.py            # model on the CPU (noticeably laggy)
python3 segformer_camera.py --use-npu  # model on the Hexagon NPU (real time)
```

A window titled **"Segformer Segmentation"** opens showing the live camera feed with a color-tinted overlay: each pixel is colored by its predicted class, plus a small legend (the top 5 classes by pixel count, with color swatches) in the corner. The on-screen overlay reports the model invoke time and the total per-frame latency. Press **`q`** in the window to quit.

Running on the NPU is dramatically faster than on the CPU — the difference between a laggy preview and a smooth real-time feed. On a VENTUNO Q running Ubuntu 24.04, averaged over 45 frames:

| Model on | Model invoke | Total per frame       |
| -------- | ------------ | --------------------- |
| CPU      | 271.7 ms     | 287.2 ms (~3 fps)     |
| **NPU**  | **20.9 ms**  | **37.9 ms (~26 fps)** |

That is roughly a **13x** speedup on the model itself. This is the largest NPU gain of any model in this collection, because SegFormer is a comparatively large, compute-dense network — exactly the kind of workload the Hexagon™ Tensor Processor is built for.

If you launch the script from a remote host (`adb` or `ssh`), you will first need to allow it to render on the display.

On the board itself (not using `adb` or `ssh`), open a terminal and run the following:

```bash
xhost +
export DISPLAY=:0   # replace 0 with your display number
```

This will enable a remote host to run applications on the display. If you do not do this, when running the script from a remote host, you will see `xcb` related error.

## Code Example

The full, self-contained demo is shown below. Save it as `segformer_camera.py` in the working directory alongside the model file.

```python
import colorsys
import sys
import time

import cv2
import numpy as np
from ai_edge_litert.interpreter import Interpreter, load_delegate

# --- SETUP ---
MODEL_PATH = 'segformer_base-w8a8.tflite'
TOP_K = 5  # how many classes to list in the on-screen legend, ranked by pixel count

# The 150 ADE20K scene-parsing classes this model was finetuned on (from
# nvidia/segformer-b0-finetuned-ade-512-512's config.json id2label, index == class id).
CLASS_NAMES = [
    "wall", "building", "sky", "floor", "tree", "ceiling", "road", "bed", "windowpane",
    "grass", "cabinet", "sidewalk", "person", "earth", "door", "table", "mountain",
    "plant", "curtain", "chair", "car", "water", "painting", "sofa", "shelf", "house",
    "sea", "mirror", "rug", "field", "armchair", "seat", "fence", "desk", "rock",
    "wardrobe", "lamp", "bathtub", "railing", "cushion", "base", "box", "column",
    "signboard", "chest of drawers", "counter", "sand", "sink", "skyscraper",
    "fireplace", "refrigerator", "grandstand", "path", "stairs", "runway", "case",
    "pool table", "pillow", "screen door", "stairway", "river", "bridge", "bookcase",
    "blind", "coffee table", "toilet", "flower", "book", "hill", "bench", "countertop",
    "stove", "palm", "kitchen island", "computer", "swivel chair", "boat", "bar",
    "arcade machine", "hovel", "bus", "towel", "light", "truck", "tower", "chandelier",
    "awning", "streetlight", "booth", "television receiver", "airplane", "dirt track",
    "apparel", "pole", "land", "bannister", "escalator", "ottoman", "bottle", "buffet",
    "poster", "stage", "van", "ship", "fountain", "conveyer belt", "canopy", "washer",
    "plaything", "swimming pool", "stool", "barrel", "basket", "waterfall", "tent",
    "bag", "minibike", "cradle", "oven", "ball", "food", "step", "tank", "trade name",
    "microwave", "pot", "animal", "bicycle", "lake", "dishwasher", "screen", "blanket",
    "sculpture", "hood", "sconce", "vase", "traffic light", "tray", "ashcan", "fan",
    "pier", "crt screen", "plate", "monitor", "bulletin board", "shower", "radiator",
    "glass", "clock", "flag",
]
NUM_CLASSES = len(CLASS_NAMES)

use_npu = True if len(sys.argv) >= 2 and sys.argv[1] == '--use-npu' else False

experimental_delegates = []
if use_npu:
    experimental_delegates = [load_delegate("libQnnTFLiteDelegate.so", options={"backend_type": "htp"})]

interpreter = Interpreter(model_path=MODEL_PATH, experimental_delegates=experimental_delegates)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

_, M_H, M_W, _ = input_details[0]['shape']
in_scale, in_zp = input_details[0]['quantization']
out_scale, out_zp = output_details[0]['quantization']

# Deterministic BGR color per class, spread evenly around the hue wheel.
PALETTE = np.array(
    [tuple(int(c * 255) for c in reversed(colorsys.hsv_to_rgb(i / NUM_CLASSES, 0.85, 1.0)))
     for i in range(NUM_CLASSES)],
    dtype=np.uint8,
)

# --- NPU WARMUP ---
if use_npu:
    print("Warming up NPU...")
    dummy = np.zeros(input_details[0]['shape'], dtype=input_details[0]['dtype'])
    for _ in range(3):
        interpreter.set_tensor(input_details[0]['index'], dummy)
        interpreter.invoke()
    print("Warmup done.")

def letterbox(frame_rgb, dst_h, dst_w):
    h, w = frame_rgb.shape[:2]
    scale = min(dst_h / h, dst_w / w)
    new_h, new_w = int(h * scale), int(w * scale)

    resized = cv2.resize(frame_rgb, (new_w, new_h))
    canvas = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)

    pad_top = (dst_h - new_h) // 2
    pad_left = (dst_w - new_w) // 2
    canvas[pad_top:pad_top + new_h, pad_left:pad_left + new_w] = resized

    return canvas, (pad_left, pad_top, new_w, new_h)

def process_frame(frame_bgr):
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    h, w = frame_rgb.shape[:2]
    canvas, (pad_left, pad_top, new_w, new_h) = letterbox(frame_rgb, M_H, M_W)

    if in_scale:
        q = np.rint((canvas.astype(np.float32) / 255.0) / in_scale) + in_zp
        model_input = np.clip(q, 0, 255).astype(input_details[0]['dtype'])
    else:
        model_input = (canvas.astype(np.float32) / 255.0)

    interpreter.set_tensor(input_details[0]['index'], model_input[np.newaxis, ...])
    t0 = time.perf_counter()
    interpreter.invoke()
    invoke_ms = (time.perf_counter() - t0) * 1000

    logits = interpreter.get_tensor(output_details[0]['index'])[0]  # (128, 128, 150)
    if out_scale:
        logits = (logits.astype(np.float32) - out_zp) * out_scale
    class_map = logits.argmax(axis=-1).astype(np.uint8)  # (128, 128)

    # Upsample to the letterboxed canvas size, then crop out the real (non-pad) area
    # and resize that back to the original frame size -- nearest-neighbor throughout
    # so we never invent a class at a boundary between two real ones.
    class_map = cv2.resize(class_map, (M_W, M_H), interpolation=cv2.INTER_NEAREST)
    class_map = class_map[pad_top:pad_top + new_h, pad_left:pad_left + new_w]
    class_map = cv2.resize(class_map, (w, h), interpolation=cv2.INTER_NEAREST)

    return class_map, invoke_ms

# --- MAIN LOOP ---
mode = "NPU" if use_npu else "CPU"
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    t_start = time.perf_counter()
    class_map, invoke_ms = process_frame(frame)
    total_ms = (time.perf_counter() - t_start) * 1000

    mask_color = PALETTE[class_map]
    overlay = cv2.addWeighted(frame, 0.55, mask_color, 0.45, 0)

    ids, counts = np.unique(class_map, return_counts=True)
    top = ids[np.argsort(-counts)][:TOP_K]
    for i, class_id in enumerate(top):
        swatch = tuple(int(c) for c in PALETTE[class_id])
        y = 70 + i * 26
        cv2.rectangle(overlay, (20, y - 14), (40, y + 4), swatch, -1)
        cv2.putText(overlay, CLASS_NAMES[class_id], (48, y), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

    label = f"{mode}  invoke={invoke_ms:.1f}ms  total={total_ms:.1f}ms"
    cv2.putText(overlay, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow('Segformer Segmentation', overlay)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## How It Works

- **Preprocessing.** The frame is letterboxed (aspect-ratio-preserving resize plus padding) to the model's 512×512 input.
- **Inference.** The model outputs a 128×128×150 class-logit map (it downsamples 4× internally). The script takes an `argmax` over the 150 classes at each position to get a class map, upsamples that 128×128 map back to 512×512 with **nearest-neighbor** interpolation (so no new class is invented at a boundary between two real ones), crops out the letterbox padding, then resizes back to the original frame size.
- **Class names.** The 150 categories are the standard ADE20K label set, taken from the exact checkpoint's (`nvidia/segformer-b0-finetuned-ade-512-512`) `id2label` mapping.
- **Colors.** Each class is assigned a deterministic color by spacing 150 hues evenly around the HSV wheel, so the same class always gets the same color across runs.

## Conclusion

In this tutorial you set up the VENTUNO Q, downloaded the `segformer_base` model file, and ran a self-contained Python script that performs live semantic segmentation, accelerated on the Qualcomm® Hexagon™ NPU. From here you can build on the per-pixel class map — for example to isolate people from the background, mask specific object categories, or drive scene-aware interactions — directly on the Dragonwing™ QCS8275 processor.
