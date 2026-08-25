---
title: 'Running Ollama on the Arduino VENTUNO Q'
overwriteSidebar: Ollama
difficulty: beginner
description: 'Install and run Ollama large language models (LLMs) locally on the Arduino® VENTUNO™ Q.'
tags:
  - Linux
  - Ollama
  - AI
  - Debian
author: 'Karl Söderby, Ernesto Voltaggio'
compatible-products: [ventuno-q]
hardware:
  - hardware/14.ventuno/boards/ventuno-q
software:
  - app-lab
---

## Overview

This tutorial walks through installing [Ollama](https://ollama.com) — a framework for running large language models locally — and running lightweight models on the Arduino® VENTUNO™ Q's Qualcomm® Dragonwing™ QCS8275 processor.

<Alert type="note">
Note: Please be advised that the Ollama installation + a model will take up a large amount of disk space, and requires a stable Internet connection.
</Alert>

## Hardware & Software Needed

- [Arduino® VENTUNO™ Q](https://docs.arduino.cc/hardware/ventuno-q)
- USB-C® cable
- [Arduino® USB-C Power Supply (65W)](https://store.arduino.cc/products/usb-c-power-supply-65w)

## Accessing the Board Shell

This tutorial requires you to access the shell on the VENTUNO Q. To access the shell (terminal), you can use `adb` or `ssh`.

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

<Alert type="info">For more alternatives to remotely access your board, please see the [Remote Access](https://docs.arduino.cc/tutorials/uno-q/remote-access/) tutorial.</Alert>

## Installing Ollama

Ollama can be installed using `curl`:

```bash
# Download and run the official Ollama installer
curl -fsSL https://ollama.com/install.sh | sh
```

<Alert type="info">**Note:** The installer writes to `/usr/local` and registers a `systemd` service, so it asks for your password. Run it from an interactive terminal on the board — through a non-interactive session the prompt cannot be answered and the install stops at `sudo: a password is required`.</Alert>

When it finishes, Ollama runs as a background service. Check it with:

```bash
ollama --version
systemctl is-active ollama
```

## Running LLMs on the VENTUNO Q

```bash
# Recommended for minimal memory usage (~500 MB RAM)
ollama run qwen2.5:0.5b

# Balanced option with better output quality (~1.5 GB RAM required)
ollama run llama3.2:1b
```

Once the model weights are downloaded, internet access is no longer required. You can run inferences completely offline.

## Ollama Runs on the CPU

Ollama is the quickest way to get a local model running, but on the VENTUNO Q it uses **only the CPU** — it does not reach the Hexagon™ NPU or the Adreno™ GPU. You can confirm this while a model is loaded:

```bash
ollama ps
```

The `PROCESSOR` column reports `100% CPU`. The Ollama server log says the same at startup, listing `cpu` as the only inference device it discovered.

This is a property of the build rather than of the board. The official Linux arm64 release ships CPU backends (`libggml-cpu-armv8.0` through `armv9.2`) and CUDA, with no Vulkan, OpenCL or QNN backend, so there is nothing for it to offload to. The board itself is capable: the Adreno™ 623 exposes both OpenCL 3.0 and Vulkan 1.3 (the latter through the Mesa `turnip` driver), and llama.cpp uses OpenCL on it successfully.

Ollama's Vulkan backend does exist upstream, but it is experimental and is not included in any released binary. Building Ollama from source with `-DGGML_VULKAN=ON` does produce a working `libggml-vulkan.so`, and the runtime then finds the GPU — it reports `library=Vulkan description=Adreno623` once integrated GPUs are enabled with `OLLAMA_IGPU_ENABLE=1`, and it offloads every layer of the model into Vulkan buffers. Inference itself, however, terminates with a segmentation fault. The GPU path on this hardware is therefore not usable yet, and the packaged installer above remains the sensible way to run Ollama.

There is no Ollama path to the Hexagon™ NPU at all: no build option adds one.

This matters when choosing a runtime. Measured on a VENTUNO Q running Ubuntu 24.04:

| Runtime | Model | Runs on | Generation speed |
| ------- | ----- | ------- | ---------------- |
| Ollama | Qwen2.5 0.5B | CPU | 5.3 tok/s |
| llama.cpp (OpenCL build) | Qwen2.5 1.5B | Adreno™ GPU | 7.4 tok/s |
| GenieX | Qwen2.5 1.5B | Hexagon™ NPU | ~25 tok/s |

The accelerated runtimes are faster on a model three times larger. Use Ollama when convenience matters most — it manages downloads, model files and an API server for you. When you want the accelerators, see [Running LLMs and VLMs on the NPU with GenieX](/tutorials/ventuno-q/geniex), which is both the fastest option and about as simple to install, or [Running Local LLMs on Ventuno Q](/tutorials/ventuno-q/llama-cpp) if you want to build the stack yourself.

## Conclusion

You have successfully installed Ollama and run lightweight LLMs locally on the Dragonwing™ QCS8275. This setup is well suited for edge AI inference during development without relying on cloud services.
