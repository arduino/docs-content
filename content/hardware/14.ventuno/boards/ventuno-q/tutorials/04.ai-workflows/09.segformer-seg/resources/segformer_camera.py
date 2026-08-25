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
