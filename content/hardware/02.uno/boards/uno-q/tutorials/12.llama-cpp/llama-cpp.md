---
title: 'Running Llama.cpp with Qwen3.5-0.8B on the Arduino® UNO Q'
overwriteSidebar: Llama.cpp
description: 'Install llama.cpp on the Linux side of an Arduino® UNO Q and run local Qwen3.5-0.8B inference'
difficulty: intermediate
tags:
  - Linux
  - AI
  - llama.cpp
  - UNO Q
author: 'Arduino'
---

## Overview

This tutorial installs [llama.cpp](https://github.com/ggml-org/llama.cpp) directly on the Arduino® UNO Q's Linux system and runs inference on a local Large Language Model (LLM). The model used in this tutorial is [Qwen3.5-0.8B](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF). The UNO Q uses the Qualcomm® Dragonwing™ QRB2210 processor and ships with a small Debian-based root filesystem and limited disk space, so this guide uses a prebuilt binary release and a small GGUF model instead of compiling from source.

This workflow is independent of the Arduino App. If you want an LLM inside an Arduino App instead, the board already includes the `arduino:llm` Brick, which wraps local inference for you. This guide is for running llama.cpp as a standalone tool directly on the board.

## Hardware & Software Needed

- [Arduino® UNO Q](https://docs.arduino.cc/hardware/uno-q/)
- [USB-C® cable](https://store.arduino.cc/collections/cables-wires/products/usb-c-cable-24-pin) (or a separate power source + access via SSH)

You will also need to have:
- [ADB](https://docs.arduino.cc/tutorials/uno-q/adb/) or [SSH](https://docs.arduino.cc/tutorials/uno-q/ssh/) installed on your machine. This allows you to access your board's shell (terminal).
- [Qwen3.5-0.8B](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) (this will be downloaded when running the installation scripts)


<Alert type="note">
Make sure you have around 1GB of free space on your UNO Q for this tutorial.
</Alert>

## Accessing the Board Shell

To access the shell (terminal) on the Arduino® UNO Q, use `adb` or `ssh`.

To connect by `adb`, connect a USB-C® cable between the board and your computer, then run:

```bash
# Using adb (Android Debug Bridge)
adb shell
```

To connect by `ssh`, ensure the board is connected to the same network as your computer, then run:

```bash
# Using ssh (Secure Shell)
ssh arduino@<ip-address>
```

For more alternatives to access the board remotely, see the [Remote Access](https://docs.arduino.cc/tutorials/uno-q/remote-access/) tutorial.

## Connect to Internet

This tutorial requires a stable Internet connection to download dependencies & the model. Connecting to Internet is easiest done via the [Arduino App Lab](https://www.arduino.cc/en/software/#app-lab-section), where upon launching and connecting your board, you will be asked to provide network credentials.

You can also connect via `nmtui` on the board's shell, via `nmcli`.

## Instructions

### 1. Check the board resources

Before installing anything, confirm that the board is recognized and that there is enough space available for the model and binaries.

```bash
cat /sys/firmware/devicetree/base/compatible | tr '\0' '\n'   # arduino,imola = UNO Q
free -h                                                        # RAM
df -h /                                                        # free disk space
```

An UNO Q 4GB version generally has about 3.6 GB of free RAM and a small root filesystem. That is enough for a compact 0.8B model in 4-bit quantization, but not for large F16 models or a source build. Keep the installation lean by choosing one prebuilt release and one smaller GGUF model.

### 2. Download a prebuilt llama.cpp release

The UNO Q runs Debian on the Linux side, and it does not come with a compiler toolchain or passwordless `sudo`. Compiling from source would require extra packages and is not the most practical approach. Instead, download the official prebuilt `ubuntu-arm64` release for the board.

Find the latest release tag and download the matching archive:

```bash
curl -s https://api.github.com/repos/ggml-org/llama.cpp/releases?per_page=1 \
  | grep -E '"tag_name"|browser_download_url.*ubuntu-arm64'
```

Then download and extract the release into a local folder:

```bash
mkdir -p ~/llama.cpp && cd ~/llama.cpp
TAG=b10644   # replace this with the tag you found above
wget -O llama-bin.tar.gz \
  "https://github.com/ggml-org/llama.cpp/releases/download/${TAG}/llama-${TAG}-bin-ubuntu-arm64.tar.gz"
tar -xzf llama-bin.tar.gz
rm llama-bin.tar.gz   # save disk space; the archive is no longer needed
```

This creates a folder similar to `~/llama.cpp/llama-b10644/` containing `llama-cli`, `llama-server`, and the required shared libraries.

Test the binary before continuing:

```bash
cd ~/llama.cpp/llama-b10644
LD_LIBRARY_PATH=. ./llama-cli --version
```

> `LD_LIBRARY_PATH=.` is required because the release ships its shared libraries next to the binaries instead of installing them system-wide.

### 3. Download the Qwen3.5-0.8B GGUF model

llama.cpp expects the model in GGUF format. A good default for the UNO Q is the Qwen3.5-0.8B model in Q4_K_M quantization, because it is relatively small and still practical for local inference.

Download the model to a dedicated folder:

```bash
mkdir -p ~/llama.cpp/models && cd ~/llama.cpp/models
wget -O Qwen3.5-0.8B-Q4_K_M.gguf \
  "https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-Q4_K_M.gguf"
```

This model is roughly 500 MB. If space is tight, check `df -h /` before and after the download and delete unused files with `rm` if needed.

### 4. Run inference locally

Now start the model with a single prompt and stop after the response. This is a good way to confirm that the install works before moving to longer or interactive sessions.

```bash
cd ~/llama.cpp/llama-b10644
LD_LIBRARY_PATH=. ./llama-cli \
  -m ~/llama.cpp/models/Qwen3.5-0.8B-Q4_K_M.gguf \
  -p "Tell me a short fact about the t-rex" \
  -n 120 --single-turn -rea off
```

The key flags are:

*   `-m`: path to the GGUF model file
*   `-p`: prompt text
*   `-n`: maximum tokens to generate
*   `--single-turn`: answer once and exit instead of opening an interactive chat
*   `-rea off`: disable the model's built-in reasoning output for shorter, more direct responses

The expected output on the board is similar to:

```text
> Tell me a short fact about the t-rex.
T-rex has short arms and have been extinct for...

[ Prompt: 8.4 t/s | Generation: 3.6 t/s ]
```

Generation at roughly 3.6 tokens per second is typical for CPU-only inference on the UNO Q. This is fine for short experiments and small demos, but not for long interactive sessions.

### 5. Use the model in interactive or server mode

For a chat-style REPL, omit `--single-turn` and `-p` and let the model run interactively:

```bash
cd ~/llama.cpp/llama-b10644
LD_LIBRARY_PATH=. ./llama-cli \
  -m ~/llama.cpp/models/Qwen3.5-0.8B-Q4_K_M.gguf
```

If you want to expose an OpenAI-compatible API from the board, start `llama-server` on port 8080:

```bash
cd ~/llama.cpp/llama-b10644
LD_LIBRARY_PATH=. ./llama-server \
  -m ~/llama.cpp/models/Qwen3.5-0.8B-Q4_K_M.gguf \
  --port 8080
```

This exposes `/v1/chat/completions` on the local network so other code running on the board or elsewhere can call the model.

### 6. Make the binaries easier to run

Add an alias so you do not have to type the `LD_LIBRARY_PATH` prefix and full path each time:

```bash
echo 'alias llama-cli="LD_LIBRARY_PATH=$HOME/llama.cpp/llama-b10644 $HOME/llama.cpp/llama-b10644/llama-cli"' >> ~/.bashrc
source ~/.bashrc
```

After that, you can run `llama-cli` directly in a new shell.

## Code Example

```bash
# Check the hardware and disk usage
cat /sys/firmware/devicetree/base/compatible | tr '\0' '\n'
free -h
df -h /
```

```bash
# Download a prebuilt llama.cpp release and extract it
mkdir -p ~/llama.cpp && cd ~/llama.cpp
TAG=b10644
wget -O llama-bin.tar.gz \
  "https://github.com/ggml-org/llama.cpp/releases/download/${TAG}/llama-${TAG}-bin-ubuntu-arm64.tar.gz"
tar -xzf llama-bin.tar.gz
rm llama-bin.tar.gz
```

```bash
# Download and run the compact GGUF model
mkdir -p ~/llama.cpp/models && cd ~/llama.cpp/models
wget -O Qwen3.5-0.8B-Q4_K_M.gguf \
  "https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-Q4_K_M.gguf"

cd ~/llama.cpp/llama-b10644
LD_LIBRARY_PATH=. ./llama-cli \
  -m ~/llama.cpp/models/Qwen3.5-0.8B-Q4_K_M.gguf \
  -p "Give a short, fun fact about octopuses." \
  -n 120 --single-turn -rea off
```

## Conclusion

This workflow provides a straightforward way to run a small local LLM directly on the Arduino® UNO Q without installing a full compiler toolchain or requiring passwordless `sudo`. The prebuilt llama.cpp release and the compact Qwen3.5-0.8B GGUF model are a practical combination for the limited storage and memory available on the board.

For tight storage situations, remove unused model files or cached downloads, and keep only the binary and GGUF model you are actively using. The result is a working local inference pipeline that is easy to test, demo, and expand.