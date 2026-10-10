#!/usr/bin/env python3
"""Rewrite AI Hub's EyeGaze w8a16 ONNX so that it runs entirely on the NPU.

onnxruntime-qnn 1.23 rejects two patterns in the published graph. Each rejected
node runs on the CPU instead, which cuts the model into 36 NPU pieces with a CPU
round trip between them: ~20 ms per inference instead of ~1.5 ms.

  * BatchNormalization with per-channel quantized parameters
    ("QNN BatchNorm doesn't support dynamic scale"), 48 of them. Each becomes the
    equivalent 1x1 Conv, quantized like the graph's other Convs (per-channel int8
    weight, int32 bias). The weight is a diagonal matrix: a depthwise Conv would
    be the obvious choice, but the HTP backend runs those ~100x slower here.
  * Reshape with allowzero=1 ("QNN Reshape doesn't support dynamic shape"). No
    target shape contains a zero, so the attribute is simply cleared.

The result matches the original to within 0.06 heatmap pixels / 0.04 degrees.
eyegaze.py runs this automatically when models/eyegaze_npu.onnx is missing.

Usage: python prepare_model.py [SOURCE.onnx] [OUTPUT.onnx]
"""
import sys
from pathlib import Path

import numpy as np
import onnx
from onnx import helper, numpy_helper

MODELS = Path(__file__).resolve().parent / "models"
SOURCE = MODELS / "eyegaze-onnx-w8a16" / "eyegaze.onnx"
OUTPUT = MODELS / "eyegaze_npu.onnx"


def convert(source=SOURCE, output=OUTPUT):
    model = onnx.load(str(source))
    graph = model.graph
    initializers = {t.name: t for t in graph.initializer}
    producer = {name: node for node in graph.node for name in node.output}

    def constant(name):
        return numpy_helper.to_array(initializers[name])

    def dequantized(name):
        """Float value of a BN parameter: what its (Quantize ->) Dequantize chain yields."""
        dq = producer[name]
        assert dq.op_type == "DequantizeLinear", dq.op_type
        if dq.input[0] in initializers:
            q = constant(dq.input[0]).astype(np.float64)
        else:
            quantize = producer[dq.input[0]]
            assert quantize.op_type == "QuantizeLinear", quantize.op_type
            zero_point = constant(quantize.input[2])
            limits = np.iinfo(zero_point.dtype)
            q = np.rint(constant(quantize.input[0]).astype(np.float64) / constant(quantize.input[1]))
            q = np.clip(q + zero_point, limits.min, limits.max)
        return (q - constant(dq.input[2]).astype(np.float64)) * constant(dq.input[1]).astype(np.float64)

    nodes, new_initializers = [], []
    batch_norms = reshapes = 0
    for node in graph.node:
        if node.op_type == "Reshape":
            for attribute in node.attribute:
                if attribute.name == "allowzero" and attribute.i:
                    assert 0 not in constant(node.input[1])
                    attribute.i = 0
                    reshapes += 1
        if node.op_type != "BatchNormalization":
            nodes.append(node)
            continue

        x, *parameters = node.input
        gamma, beta, mean, variance = (dequantized(p) for p in parameters)
        epsilon = next(a.f for a in node.attribute if a.name == "epsilon")
        # gamma * (x - mean) / sqrt(variance + epsilon) + beta  ==  w * x + b
        w = gamma / np.sqrt(variance + epsilon)
        b = beta - mean * w

        # Each output channel has a single non-zero weight, so per-channel int8
        # represents it exactly (as +-127).
        x_scale = float(constant(producer[x].input[1]))
        w_scale = np.maximum(np.abs(w), 1e-12) / 127.0
        b_scale = x_scale * w_scale
        b_q = np.rint(b / b_scale)
        assert np.abs(b_q).max() < 2**31 - 1, f"{node.name}: bias does not fit int32"

        name, channels = node.name, len(w)
        new_initializers += [
            numpy_helper.from_array(np.diag(w).astype(np.float32).reshape(channels, channels, 1, 1),
                                    f"{name}_w"),
            numpy_helper.from_array(w_scale.astype(np.float32), f"{name}_w_scale"),
            numpy_helper.from_array(np.zeros(channels, np.int8), f"{name}_w_zero"),
            numpy_helper.from_array(b_q.astype(np.int32), f"{name}_b_q"),
            numpy_helper.from_array(b_scale.astype(np.float32), f"{name}_b_scale"),
            numpy_helper.from_array(np.zeros(channels, np.int32), f"{name}_b_zero"),
        ]
        nodes += [
            helper.make_node("QuantizeLinear", [f"{name}_w", f"{name}_w_scale", f"{name}_w_zero"],
                             [f"{name}_w_q"], name=f"{name}_w_quantize", axis=0),
            helper.make_node("DequantizeLinear", [f"{name}_w_q", f"{name}_w_scale", f"{name}_w_zero"],
                             [f"{name}_w_dq"], name=f"{name}_w_dequantize", axis=0),
            helper.make_node("DequantizeLinear", [f"{name}_b_q", f"{name}_b_scale", f"{name}_b_zero"],
                             [f"{name}_b_dq"], name=f"{name}_b_dequantize", axis=0),
            helper.make_node("Conv", [x, f"{name}_w_dq", f"{name}_b_dq"], list(node.output),
                             name=f"{name}_as_conv", kernel_shape=[1, 1]),
        ]
        batch_norms += 1

    # Drop the BN parameters' now-unused Quantize/Dequantize chains.
    outputs = {o.name for o in graph.output}
    while True:
        used = {name for node in nodes for name in node.input} | outputs
        kept = [node for node in nodes if any(name in used for name in node.output)]
        if len(kept) == len(nodes):
            break
        nodes = kept

    kept_initializers = [t for t in graph.initializer if t.name in used] + new_initializers
    del graph.node[:], graph.initializer[:], graph.value_info[:]
    graph.node.extend(nodes)
    graph.initializer.extend(kept_initializers)

    onnx.checker.check_model(model)
    onnx.save(model, str(output))  # one file, weights embedded
    print(f"{source} -> {output}: {batch_norms} BatchNormalization -> Conv, "
          f"{reshapes} Reshape fixed")


if __name__ == "__main__":
    convert(*sys.argv[1:3])
