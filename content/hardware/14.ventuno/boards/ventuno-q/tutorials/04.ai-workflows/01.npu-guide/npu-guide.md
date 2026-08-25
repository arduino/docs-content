---
title: "Understanding and Using the NPU on the VENTUNO Q"
overwriteSidebar: Using the NPU
difficulty: intermediate
compatible-products: [ventuno-q]
description: "Learn what an NPU is, how it compares to the CPU, and the three ways to run AI models on the Hexagon NPU of the Arduino® VENTUNO™ Q."
tags:
  - AI
  - NPU
  - Edge AI
  - TFLite
  - ONNX
  - PyTorch
  - Linux
  - Qualcomm AI Hub
author: "Karl Söderby, Ernesto Voltaggio"
hardware:
  - hardware/14.ventuno/boards/ventuno-q
software:
  - app-lab
---

## Overview

The **Arduino® VENTUNO™ Q** is built around the Qualcomm® Dragonwing™ IQ8 (QCS8275), a processor that pairs a general purpose CPU with a dedicated **Neural Processing Unit (NPU)** for running AI models. This guide explains what an NPU actually is, how it differs from the CPU and GPU on the same chip, and the three practical paths for getting a model — whether pre-trained, TensorFlow™, or PyTorch — running on it.

In this guide we will cover:

1. What an NPU is and how it differs from a CPU and GPU.
2. The Hexagon™ Tensor Processor's specifications on the QCS8275.
3. The three supported paths for running a model on the NPU (Qualcomm® AI Hub, TensorFlow™/LiteRT, PyTorch/ONNX Runtime).
4. Setting up the NPU toolchain on the VENTUNO Q.
5. Constraints every NPU workload runs into, and how to work around them.
6. Benchmark figures comparing NPU and CPU inference.

This is a conceptual and reference guide. For hands-on, step-by-step walkthroughs, see the [linked tutorials](#tutorials-in-this-collection) at the end.

## What Is an NPU?

An NPU (Neural Processing Unit) is a processor core built specifically to execute the arithmetic that neural networks are made of: large numbers of multiply-accumulate (MAC) operations, arranged as matrix and tensor multiplications. Rather than executing a general instruction stream one branch at a time like a CPU, an NPU is wired as an array of thousands of small multiply-accumulate units that all execute the same kind of operation on different pieces of data at once.

- **CPU** (Central Processing Unit) is built for flexibility. It executes arbitrary instructions, handles branching logic, and supports any numeric format (32-bit floats, 64-bit doubles, arbitrary-precision integers). This flexibility costs power and throughput when the workload is simple, repetitive math at a massive scale, like a neural network's matrix multiplications.
- **GPU** (Graphics Processing Unit) sits in between: thousands of simpler cores executing the same instruction on different data (SIMD), originally designed for pixel/vertex math but well-suited to general matrix compute (GPGPU) via APIs like OpenCL. The Adreno™ 623 GPU on the QCS8275 is used this way for graphics and some compute workloads.
- **NPU** goes further than a GPU by giving up support for anything other than tensor math, and by restricting itself to **low-precision arithmetic** — 8-bit or 16-bit integers, or 16-bit floating point — rather than the 32-bit floating point a CPU uses. In exchange, it delivers far higher throughput per watt for that one workload than either a CPU or a GPU can.

The practical consequence for you as a developer: an NPU cannot run "a program" the way a CPU does. It runs a fixed computation graph (a neural network) at reduced precision. The NPU cannot execute FP32, so every graph is either quantized to 8-bit or 16-bit integers ahead of time, or converted to 16-bit floating point (FP16) by the runtime when the model is loaded. Quantization takes more preparation but delivers the highest throughput; FP16 requires no preparation at all.

### CPU vs. GPU vs. NPU on the QCS8275

| Processor | Component on QCS8275                 | Executes                                   | Data Types                                  | Best For                                                                        |
| --------- | ------------------------------------ | ------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------- |
| CPU       | Kryo™ Gen 6 (Octa-core Arm® Cortex®) | Arbitrary instructions, branching logic    | FP32/64, any integer width                  | General-purpose code, orchestration, pre/postprocessing                         |
| GPU       | Adreno™ 623                          | SIMD graphics and general compute (OpenCL) | FP16/FP32 (and INT8 for some compute paths) | 3D graphics, video processing, some parallel compute                            |
| NPU       | Hexagon™ Tensor Processor            | Fixed neural network graphs only           | INT8 / INT16 (quantized), FP16 (no FP32)    | Neural network inference (vision, audio, LLMs) at high throughput and low power |

## The Hexagon Tensor Processor on the QCS8275

The NPU on the VENTUNO Q's Qualcomm® Dragonwing™ QCS8275 is called **Hexagon™ Tensor Processor**. It integrates three distinct compute blocks under one unit:

- A **Hexagon™ DSP** (Digital Signal Processor) core, which handles scalar and control-flow work within the NPU pipeline.
- **Quad Hexagon Vector eXtensions (HVX)** — four vector co-processors for wide SIMD math (used heavily in image pre/postprocessing steps like resizing and color conversion).
- **Dual Hexagon Matrix eXtensions (HMX)** — one integer and one floating-point matrix co-processor, purpose-built for the dense matrix multiplications that make up convolution and fully connected layers.

| Specification                                                   | Value                                                                                                |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Peak AI performance                                             | Up to **40 dense TOPS** (Tera Operations Per Second) on the QCS8275-AA variant used in the VENTUNO Q |
| Peak AI performance (QCS8275-AC variant, not used in VENTUNO Q) | Up to 20 dense TOPS                                                                                  |
| On-chip memory for the NPU                                      | 1 MB L2 cache + 8 MB Vector-TCM (vTCM) per Hexagon Tensor Processor                                  |
| Supported precisions                                            | INT8 (`w8a8`), INT16 activations (`w8a16`), FP16. FP32 is not executed on the NPU                    |
| Supported frameworks                                            | TensorFlow™ Lite (LiteRT), ONNX Runtime, PyTorch (via conversion)                                    |

For comparison, the QCS8275's other compute blocks on the VENTUNO Q run at:

| Component         | Detail                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------ |
| CPU (Kryo™ Gen 6) | 2× Prime cores up to 2.35 GHz, 2× Gold cores up to 2.1 GHz, 4× Silver cores up to 1.95 GHz |
| GPU (Adreno™ 623) | Up to 877 MHz                                                                              |

<Alert type="info" text="Note">
TOPS is a peak theoretical figure for 8-bit integer multiply-accumulate throughput. Real-world inference speed also depends on model architecture, memory bandwidth, and how much of the graph can actually run on the NPU (see [Common Constraints](#common-constraints-when-targeting-the-npu) below).
</Alert>

## Three Ways to Run a Model on the NPU

Every AI workload on the VENTUNO Q's NPU follows the same underlying requirement — a reduced-precision, fixed-shape computation graph — but there are three practical starting points depending on where your model comes from.

### 1. Start From a Pre-Optimized Model (Qualcomm AI Hub)

The fastest path. [Qualcomm® AI Hub](https://aihub.qualcomm.com) hosts a large library of models that are already trained, already quantized, and already validated to run on Dragonwing™ hardware (more specifically, the QCS8275). Note that not all models are compatible with this chipset.

- Browse the [AI Hub model list](https://aihub.qualcomm.com/models), filter by chipset (`Qualcomm QCS8275 (Proxy)`) and precision (`Quantized`).
- Download the model in either **TFLite** format (to run with LiteRT) or **ONNX** format (to run with ONNX Runtime).
- The `qai-hub-models` Python package (`pip install qai-hub-models`) also provides ready-made reference implementations with correct preprocessing/postprocessing for many models, and a `fetch` command to download model files directly on the board:

```bash
qai-hub-models fetch <model-id> --runtime onnx --precision w8a16 --output-dir models/
```

Pre-compiled TFLite and ONNX assets are device agnostic, so `fetch` needs no chipset or device argument. Add `--url-only` to print the download URL instead of fetching the file.

Tutorials for using this Qualcomm® AI Hub are described in the following tutorials:

- [Getting Started with Qualcomm AI Hub](/tutorials/ventuno-q/getting-started-qc-ai-hub)
- [Face Mesh](/tutorials/ventuno-q/face-mesh)
- [Face Detection](/tutorials/ventuno-q/face-detection)
- [Semantic Segmentation](/tutorials/ventuno-q/segformer-seg) tutorials in this collection.

### 2. Convert a TensorFlow™ / Keras Model (LiteRT)

**TensorFlow™ itself only runs on the CPU** — it trains and evaluates models using 32-bit floating-point math, which the NPU cannot execute directly. To reach the NPU, a TensorFlow™/Keras model has to be converted to a `.tflite` file — quantized to INT8 for the best throughput, or left in floating point and converted to FP16 by the runtime — then executed with **LiteRT** (the current name for the TensorFlow™ Lite runtime — the technology and file format are unchanged, only the name has been rebranded).

To do so, we can use the instructions below:

1. Train or load a TensorFlow™/Keras model (FP32).
2. Convert it to `.tflite` using the TensorFlow™ Lite Converter, applying **post-training quantization** (or quantization-aware training for better accuracy) so weights and activations become INT8.
3. Run the resulting `.tflite` file with `ai-edge-litert`, pointing it at the QNN HTP delegate (`libQnnTFLiteDelegate.so`) so the graph executes on the NPU instead of the CPU.

When running models, it can be a good idea to have both a CPU and NPU version for comparison. Examples listed in the [tutorials section](#tutorials-in-this-collection) have a flag that enables the NPU (e.g. `python3 script.py --use-npu`), whereas leaving it blank will run on the CPU. This is also a good way to confirm whether the model is running on the NPU or the CPU. Performance should be significantly better on the NPU.

### 3. Convert a PyTorch Model (ONNX Runtime)

PyTorch models also cannot run directly on the NPU, for the same reason: PyTorch computation is FP32 by default, and the NPU does not execute FP32. The path here goes through **ONNX** instead of TFLite:

1. Export the trained PyTorch model to ONNX (FP32) with `torch.onnx.export()`, using **static (fixed) input shapes** — the NPU cannot target dynamic shapes.
2. Quantize the ONNX model from FP32 to INT8. This means writing a `CalibrationDataReader` that feeds a handful of representative input samples through the model, then calling ONNX Runtime's `quantize_static()` with `QUInt8` activations and `QInt8` weights in QDQ (quantize-dequantize) format.
3. Run the quantized model with ONNX Runtime, selecting the `QNNExecutionProvider` with `"backend_type": "htp"` to target the NPU (or `CPUExecutionProvider` to compare against the CPU).

Qualcomm's reference example for this workflow (a SqueezeNet-1.1 classifier) showed **comparable per-image latency (~7.5 ms) on both CPU and NPU** — a useful reminder that very small models don't always benefit from the NPU, since fixed overhead (data marshaling, session setup) can dominate at that scale. The benefit grows with model size and compute density, as the LiteRT and TFLite/TensorFlow™ examples above show.

This is the path used by the [ONNX Runtime](/tutorials/ventuno-q/onnx-runtime) tutorial in this collection, which uses a pre-quantized AI Hub model rather than a custom-quantized one, but targets the NPU through the identical `QNNExecutionProvider` mechanism.

### A Fourth Option: No-Code Training with Edge Impulse

For building and training a **custom** model without hand-rolling a quantization pipeline, the VENTUNO Q also integrates with [Edge Impulse Studio](https://edgeimpulse.com/), which handles data collection, training, and export of an NPU-ready quantized model in one workflow. This is outside the scope of this guide but is worth knowing about if your goal is a custom classifier rather than an existing published model.

## Setting Up the NPU Toolchain on the VENTUNO Q

Regardless of which of the three paths above you take, getting to the point of "run this on the NPU" always involves the same board-side setup: access the shell, create an isolated Python environment, and install the runtime that matches your model format.

### Accessing the Board Shell

All commands are run **on the VENTUNO Q**, using one of:

- **SSH:** `ssh arduino@<device-ip>`
- **ADB:** `adb shell`
- **Directly:** keyboard, mouse, and monitor connected to the board (it runs a full Ubuntu Linux desktop, Debian is also supported).

### Installing the Qualcomm AI Runtime

The NPU is driven by the **Qualcomm® AI Runtime (QAIRT)**, which provides the QNN HTP backend that both LiteRT and ONNX Runtime load at inference time. It is **not** installed by default on the VENTUNO Q image, and it is not pulled in by any of the `pip` packages below — without it, every NPU call fails with a library load error.

Install it from the board's apt repositories:

```bash
sudo apt update
sudo apt install qairt-libs qairt-dsp-binaries
```

This installs the QNN backend libraries into `/usr/lib/`, including the two the examples in this collection reference:

- `/usr/lib/libQnnHtp.so` — the HTP (Hexagon Tensor Processor) backend, used by ONNX Runtime.
- `/usr/lib/libQnnTFLiteDelegate.so` — the LiteRT delegate, used by the TFLite examples.

Verify the install before continuing:

```bash
ls /usr/lib/libQnnHtp.so /usr/lib/libQnnTFLiteDelegate.so
```

<Alert type="info" text="Note">
Because `/usr/lib` is on the default library search path, the delegate can be loaded by name (`libQnnTFLiteDelegate.so`) without specifying a full path.
</Alert>

### Creating a Python Virtual Environment

Ubuntu 24.04 does not allow `pip install` into the system Python, so create a virtual environment first:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Re-run the `source` command at the start of every new session.

### Choosing a Runtime: LiteRT vs. ONNX Runtime

Both runtimes ultimately hand the quantized graph to the same underlying **QNN HTP backend** (Qualcomm's Hexagon Tensor Processor driver) — the choice mostly comes down to which format your model is in.

|                       | LiteRT (`.tflite` models)                               | ONNX Runtime (`.onnx` models)                                             |
| --------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| Install               | `pip install ai-edge-litert==1.3.0 opencv-python numpy` | `pip install qai-hub-models` then swap in a special QNN wheel (see below) |
| NPU delegate/provider | `libQnnTFLiteDelegate.so`, backend `"htp"`              | `QNNExecutionProvider`, `"backend_type": "htp"`                           |
| Typical source models | TensorFlow™/Keras, AI Hub TFLite exports                | PyTorch, AI Hub ONNX exports                                              |

**LiteRT setup:**

```bash
pip install ai-edge-litert==1.3.0 opencv-python numpy
```

```python
from ai_edge_litert.interpreter import Interpreter, load_delegate

qnn_delegate = load_delegate("libQnnTFLiteDelegate.so", options={"backend_type": "htp"})
interpreter = Interpreter(model_path="model.tflite", experimental_delegates=[qnn_delegate])
```

**ONNX Runtime setup** (the QNN-enabled build isn't a plain `pip install onnxruntime` — see the [ONNX Runtime tutorial](/tutorials/ventuno-q/onnx-runtime) for the full three-step install):

```bash
pip install qai-hub-models
pip uninstall -y onnxruntime
pip install onnx==1.18.0
wget https://cdn.edgeimpulse.com/qc-ai-docs/wheels/onnxruntime_qnn-1.23.0-cp312-cp312-linux_aarch64.whl
pip install onnxruntime_qnn-*-linux_aarch64.whl
```

```python
import onnxruntime as ort

providers = [("QNNExecutionProvider", {"backend_type": "htp", "library_path": "/usr/lib/libQnnHtp.so"})]
sess = ort.InferenceSession("model.onnx", providers=providers)
```

## Common Constraints When Targeting the NPU

These limitations apply across all three paths, and explain why the tutorials in this collection are structured the way they are:

- **FP32 never runs on the NPU, but quantization is not the only way off it.** The NPU executes INT8, INT16, and FP16 tensors — not FP32. An unquantized model is therefore not automatically a CPU model: the QNN HTP backend converts the FP32 graph to FP16 when it loads it, and runs it on the NPU's floating-point matrix co-processor. Quantizing to INT8 buys the highest throughput and the smallest model, but an FP32 model straight from AI Hub will still reach the NPU, at roughly FP16 accuracy. Ops the backend genuinely cannot map are offloaded to the CPU rather than failing outright — which can silently hide performance problems if you assume the whole graph is running on the NPU. Both LiteRT and ONNX Runtime allow disabling this automatic CPU fallback (for example, `session.disable_cpu_ep_fallback` in ONNX Runtime) so unsupported ops raise an error instead of quietly falling back.
- **Fixed input shapes only.** Models exported with dynamic dimensions (a common default) must be converted to static shapes before the NPU can target them — see the `make_dynamic_shape_fixed` step in the [ONNX Runtime tutorial](/tutorials/ventuno-q/onnx-runtime).
- **Not every sub-graph benefits equally.** In mixed pipelines (a detector feeding a landmark model, for instance), one stage's NPU-quantized weights may be poorly calibrated for a given input distribution while its CPU/float counterpart is not — the [Face Mesh tutorial](/tutorials/ventuno-q/face-mesh) documents exactly this case, where the face detector deliberately runs on the CPU using float weights, while only the landmark model runs on the NPU.
- **Small models may not show a speedup.** As the SqueezeNet PyTorch example above shows, fixed per-inference overhead can outweigh the NPU's raw throughput advantage on very small graphs.

## Benchmarks: How Much Faster Is the NPU?

The figures below were measured on a VENTUNO Q running Ubuntu 24.04, averaged over repeated inferences after one warm-up pass. The first model is quantized to INT8; the second is an unquantized FP32 export, which the runtime converts to FP16 to run on the NPU:

| Model                                        | Model precision | CPU       | NPU (QNN HTP delegate) | Speedup |
| -------------------------------------------- | --------------- | --------- | ---------------------- | ------- |
| Face landmark detector (192×192)             | INT8 (`w8a8`)   | 9.10 ms   | 0.46 ms                | ~20x    |
| YOLOv7 (640×640)                             | FP32 → FP16     | 440.42 ms | 12.60 ms               | ~35x    |

The YOLOv7 figure is a useful illustration of the FP16 path: the model was exported from Qualcomm® AI Hub without quantization, and AI Hub's own profiler placed all 201 operations on the NPU. Comparing its NPU output against the same graph run on the CPU shows a median relative deviation of about 5.2 × 10⁻⁴, which matches FP16's precision rather than FP32's — confirming the runtime converted the graph to half precision to execute it.

The following additional figures come from Qualcomm's own reference examples on Dragonwing™ hardware and illustrate typical relative speedups rather than VENTUNO Q-specific measurements — treat them as a guide to the shape of the trade-off (latency vs. accuracy vs. model size), not as a guarantee for any particular model.

| Model                                        | CPU (FP32)                | NPU (Quantized)            | Speedup | Notes                                              |
| -------------------------------------------- | ------------------------- | -------------------------- | ------- | -------------------------------------------------- |
| Vision Transformer (LiteRT)                  | ~300 ms                   | ~14 ms                     | ~21x    | Large, compute-dense model — biggest NPU advantage |
| Cats classifier (TensorFlow™/Keras → TFLite) | 12.9 ms (94.37% accuracy) | 3.809 ms (88.51% accuracy) | ~4x     | Small accuracy trade-off from quantization         |
| SqueezeNet-1.1 (PyTorch → ONNX)              | ~7.5 ms                   | ~7.5 ms                    | ~1x     | Small model — fixed overhead dominates             |

The general pattern: the larger and more matrix-multiplication-heavy the model, the bigger the NPU's advantage. Small or lightweight models may see little to no benefit once overhead is accounted for.

## Tutorials in This Collection

This guide is the conceptual entry point to the following hands-on tutorials, all of which run inference on the VENTUNO Q's NPU:

- **[Getting Started with Qualcomm AI Hub on the VENTUNO Q](/tutorials/ventuno-q/getting-started-qc-ai-hub)** — the full AI Hub workflow: finding a compatible model, exporting/compiling it, and running a static-image example on the NPU.
- **[ONNX Runtime on the VENTUNO Q](/tutorials/ventuno-q/onnx-runtime)** — installing the QNN-enabled ONNX Runtime build, fixing dynamic shapes, and running a live eye gaze tracking example.
- **[Real-Time Face Detection on the VENTUNO Q](/tutorials/ventuno-q/face-detection)** — live face detection using the `face_det_lite` model via LiteRT.
- **[Real-Time Face Mesh on the VENTUNO Q](/tutorials/ventuno-q/face-mesh)** — a mixed CPU/NPU pipeline: face detection on the CPU, 468-point landmark mesh on the NPU.
- **[Real-Time Semantic Segmentation on the VENTUNO Q](/tutorials/ventuno-q/segformer-seg)** — live per-pixel scene segmentation using the SegFormer model, entirely on the NPU.

## Conclusion

The Hexagon™ Tensor Processor on the VENTUNO Q's QCS8275 trades the CPU's flexibility for up to 40 dense TOPS of reduced-precision neural network throughput. Whichever of the three paths you take — a pre-optimized AI Hub model, a converted TensorFlow™/Keras model, or a converted PyTorch model — the destination is the same fixed, reduced-precision graph running through the QNN HTP backend, accessed via either LiteRT or ONNX Runtime. From here, the linked tutorials walk through each path end to end on real models.
