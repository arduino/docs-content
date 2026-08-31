import numpy as np
import cv2
from ai_edge_litert.interpreter import Interpreter, load_delegate
import time
import sys

# --- SETUP ---
MODEL_PATH = 'face_det_lite-lightweight-face-detection-w8a8.tflite'
use_npu = True if len(sys.argv) >= 2 and sys.argv[1] == '--use-npu' else False

experimental_delegates = []
if use_npu:
    experimental_delegates = [load_delegate("libQnnTFLiteDelegate.so", options={"backend_type": "htp"})]

interpreter = Interpreter(model_path=MODEL_PATH, experimental_delegates=experimental_delegates)
interpreter.allocate_tensors()

input_details  = interpreter.get_input_details()
output_details = interpreter.get_output_details()

_, M_H, M_W, M_C = input_details[0]['shape']
input_dtype = input_details[0]['dtype']
in_scale = float(input_details[0]['quantization'][0])
in_zp    = int(input_details[0]['quantization'][1])   # int() cast matches official code

# Confirm how many outputs the delegate sees
print(f"Number of outputs: {len(output_details)}")

# Pre-allocate reusable buffers
_canvas       = np.zeros((M_H, M_W, 3), dtype=np.uint8)
_input_tensor = np.zeros((1, M_H, M_W, 1), dtype=input_dtype)

# --- NPU WARMUP ---
if use_npu:
    print("Warming up NPU...")
    for _ in range(3):
        interpreter.set_tensor(input_details[0]['index'], _input_tensor)
        interpreter.invoke()
    print("Warmup done.")


class BBox:
    def __init__(self, xyrb, score, landmark=None):
        self.score    = score
        self.landmark = landmark
        x, y, r, b   = xyrb
        self.x = min(x, r)
        self.y = min(y, b)
        self.r = max(x, r)
        self.b = max(y, b)

    @property
    def width(self):  return self.r - self.x + 1
    @property
    def height(self): return self.b - self.y + 1
    @property
    def box(self):    return [self.x, self.y, self.r, self.b]
    @property
    def xywh(self):   return [self.x, self.y, self.width, self.height]


def get_iou(boxA, boxB):
    xA = max(boxA[0], boxB[0]);  yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2]);  yB = min(boxA[3], boxB[3])
    inter = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    aA = (boxA[2]-boxA[0]+1) * (boxA[3]-boxA[1]+1)
    aB = (boxB[2]-boxB[0]+1) * (boxB[3]-boxB[1]+1)
    return inter / float(aA + aB - inter + 1e-6)


def nms(objs, iou_thresh=0.5):
    if not objs:
        return []
    objs  = sorted(objs, key=lambda o: o.score, reverse=True)
    flags = [0] * len(objs)
    keep  = []
    for i, obj in enumerate(objs):
        if flags[i]:
            continue
        keep.append(obj)
        for j in range(i + 1, len(objs)):
            if flags[j] == 0 and get_iou(np.array(obj.box), np.array(objs[j].box)) > iou_thresh:
                flags[j] = 1
    return keep


def detect(hm, box, landmark=None, threshold=0.4, nms_iou=0.3, stride=8):
    """
    Postprocessing matching the official AI Hub implementation:
      - sigmoid heatmap
      - 3x3 max-pool local-maxima suppression
      - top-2000 candidates
      - NMS
    """
    hm_hw = 1.0 / (1.0 + np.exp(-np.clip(hm[..., 0].astype(np.float32), -15, 15)))

    # 3x3 max-pool, same padding — mirrors torch F.max_pool2d(kernel=3, stride=1, padding=1)
    H, W = hm_hw.shape
    xpad = np.pad(hm_hw, 1, mode='constant', constant_values=-np.inf)
    s0, s1 = xpad.strides
    windows  = np.lib.stride_tricks.as_strided(
        xpad, shape=(H, W, 3, 3), strides=(s0, s1, s0, s1), writeable=False
    )
    hm_pool  = windows.max(axis=(2, 3))

    candidate_scores = np.where(hm_hw >= hm_pool, hm_hw, 0.0).ravel()

    k = min(int((hm_hw >= hm_pool).sum()), 2000)
    if k == 0:
        return []
    idx_part = np.argpartition(-candidate_scores, k - 1)[:k]
    order    = np.argsort(-candidate_scores[idx_part])
    flat_idx = idx_part[order]
    scores_k = candidate_scores[flat_idx]

    ys = (flat_idx // W).astype(np.int32)
    xs = (flat_idx %  W).astype(np.int32)

    objs = []
    for cx, cy, score in zip(xs, ys, scores_k):
        if score < threshold:
            break  # sorted desc — safe to break early

        x, y, r, b = box[cy, cx].astype(np.float32)
        xyrb = [
            int((cx - x) * stride),
            int((cy - y) * stride),
            int((cx + r) * stride),
            int((cy + b) * stride),
        ]

        lm = None
        if landmark is not None:
            x5y5  = landmark[cy, cx].astype(np.float32)
            x5y5 += np.array([cx]*5 + [cy]*5, dtype=np.float32)
            x5y5 *= float(stride)
            lm = list(zip(x5y5[:5].tolist(), x5y5[5:].tolist()))

        objs.append(BBox(xyrb, float(score), lm))

    return nms(objs, nms_iou)


def preprocess_frame(frame):
    """
    Letterbox + blue-channel extraction + quantization.
    Matches official AI Hub preprocessing exactly.
    """
    h, w = frame.shape[:2]
    f_scale = min(M_W / w, M_H / h) * 0.75
    nw, nh  = int(w * f_scale), int(h * f_scale)

    scaled = cv2.resize(frame, (nw, nh))
    _canvas[:] = 0
    dx, dy = (M_W - nw) // 2, (M_H - nh) // 2
    _canvas[dy:dy+nh, dx:dx+nw] = scaled

    # Blue channel 0..1  (official code: img_array / 255.0, then take index [:,:,:,-1])
    blue = _canvas[:, :, 0].astype(np.float32) / 255.0

    # Quantize using int(zp) — matches official load_image_litert exactly
    if in_scale != 0.0:
        q = np.rint(blue / in_scale) + in_zp
        if input_dtype == np.uint8:
            _input_tensor[0, :, :, 0] = np.clip(q, 0, 255).astype(np.uint8)
        else:
            _input_tensor[0, :, :, 0] = np.clip(q, -128, 127).astype(np.int8)
    else:
        _input_tensor[0, :, :, 0] = blue

    return _canvas.copy()


def process_frame(frame):
    debug_canvas = preprocess_frame(frame)

    t_set = time.perf_counter()
    interpreter.set_tensor(input_details[0]['index'], _input_tensor)
    set_ms = (time.perf_counter() - t_set) * 1000

    t_invoke = time.perf_counter()
    interpreter.invoke()
    invoke_ms = (time.perf_counter() - t_invoke) * 1000

    t_get = time.perf_counter()

    def dequant(idx):
        s, z = output_details[idx]['quantization']
        return (interpreter.get_tensor(output_details[idx]['index']).astype(np.float32) - float(z)) * float(s)

    hm  = dequant(0)[0]
    box = dequant(1)[0]
    lm  = dequant(2)[0] if len(output_details) >= 3 else None
    get_ms = (time.perf_counter() - t_get) * 1000

    infer_ms   = set_ms + invoke_ms + get_ms
    detections = detect(hm, box, lm, threshold=0.4, nms_iou=0.3, stride=8)
    return detections, debug_canvas, infer_ms, invoke_ms


# --- MAIN LOOP ---
mode = "NPU" if use_npu else "CPU"
cap  = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    t_start = time.perf_counter()
    detections, debug_canvas, infer_ms, invoke_ms = process_frame(frame)
    total_ms = (time.perf_counter() - t_start) * 1000

    for det in detections:
        x, y, w, h = det.xywh
        cv2.rectangle(debug_canvas, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if det.landmark:
            for (lx, ly) in det.landmark:
                cv2.circle(debug_canvas, (int(lx), int(ly)), 2, (0, 128, 255), -1)

    label = (f"{mode}  invoke={invoke_ms:.1f}ms  "
             f"round-trip={infer_ms:.1f}ms  total={total_ms:.1f}ms")
    cv2.putText(debug_canvas, label, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow('Face Detect', debug_canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
