---
title: "Running LLMs and VLMs on the NPU with GenieX"
overwriteSidebar: LLMs with GenieX
difficulty: intermediate
compatible-products: [ventuno-q]
description: "Run local language and vision-language models on the Hexagon NPU of the Arduino® VENTUNO™ Q using Qualcomm® GenieX."
tags:
  - AI
  - LLM
  - VLM
  - NPU
  - GenieX
  - Edge AI
  - Linux
author: 'Ernesto Voltaggio'
hardware:
  - hardware/14.ventuno/boards/ventuno-q
software:
  - app-lab
---

## Overview

[GenieX](https://github.com/qualcomm/GenieX) is Qualcomm®'s on-device generative AI runtime, and the community edition of Qualcomm GENIE. It takes a GGUF model from Hugging Face or a pre-compiled bundle from Qualcomm® AI Hub and runs it locally on the **Hexagon™ NPU**, the Adreno™ GPU or the CPU of the Arduino® VENTUNO™ Q.

There are several ways of running language and vision-language models on the VENTUNO Q, where GenieX is both the fastest and easiest to set up: it installs with a single command, needs no administrator rights, and requires nothing to be compiled.

In this tutorial you will learn how to:

1. Install GenieX on the VENTUNO Q.
2. Download a model.
3. Run inference on the NPU, and compare it against the GPU and the CPU.
4. Run a Vision Language Model (VLM) with an image.
5. Serve the model through an OpenAI-compatible API.

<Alert type="info">

**Note:** GenieX is published as a Developer Preview. The commands below were verified on a VENTUNO Q running Ubuntu® 24.04 with GenieX v0.4.0, but expect the interface to keep changing between releases.

</Alert>

## Hardware & Software Requirements

### Hardware

- [Arduino® VENTUNO™ Q](https://store.arduino.cc/products/ventuno-q)
- [Arduino® USB-C Power Supply (65W)](https://store.arduino.cc/products/usb-c-power-supply-65w), or a 7–24 V DC supply on the power jack

### Software

- `adb` or `ssh` available on your host machine
- At least 5 GB of free disk space for the model used in this tutorial

<Alert type="note">

**Important:** The VENTUNO Q must be powered from its power supply before you connect a USB-C® cable to a host computer, otherwise the board may crash.

</Alert>

## Accessing the Board Shell

All commands in this guide run **on the VENTUNO Q**. Connect using either method:

```bash
# Using adb (Android Debug Bridge)
adb shell
```

```bash
# Using ssh (Secure Shell)
ssh arduino@<ip-address>
```

<Alert type="info">

For more alternatives to remotely access your board, please see the [Remote Access](https://docs.arduino.cc/tutorials/uno-q/remote-access/) tutorial.

</Alert>

## Installing GenieX

GenieX installs into your home directory, so no `sudo` is required:

```bash
curl -fsSL https://qaihub-public-assets.s3.us-west-2.amazonaws.com/qai-hub-geniex/install.sh | sh
```

The installer places the binary in `~/.local/share/geniex`, adds a launcher at `~/.local/bin/geniex`, and links the board's DSP libraries so the runtime can reach the NPU. Add the launcher directory to your `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Add that line to your `~/.bashrc` to make it permanent, then check the install:

```bash
geniex --version
```

This reports the CLI version along with the runtimes behind it:

```text
GenieX CLI Version:     v0.4.0
QAIRT Runtime Version:  v2.45.0.260326
LlamaCPP Runtime Hash:  6ba5ef2
```

Those two runtimes are how GenieX reaches the hardware: **llama.cpp** for GGUF models, and **Qualcomm® AI Runtime (QAIRT)** for pre-compiled AI Hub bundles.

## Downloading a Model

GenieX caches models locally with `geniex pull`. It can take them from Hugging Face, from Qualcomm® AI Hub, from Docker Hub, or from a directory on the board.

Pull the Q4_0 [Gemma 4 E2B model](https://huggingface.co/google/gemma-4-E2B-it-qat-q4_0-gguf) used throughout this tutorial. It is published by Google and used in Qualcomm's GenieX examples:

```bash
geniex pull google/gemma-4-E2B-it-qat-q4_0-gguf --model-hub hf
```

This repository provides a Q4_0 language model and its vision projector. GenieX downloads both and records the cached precision as `Q4_0`.

<Alert type="info">

**Note:** Repositories with multiple precisions open an interactive prompt. When scripting one of those pulls over `ssh` or `adb`, append the precision to the model name, for example `:Q4_0`.

</Alert>

<Alert type="info">

**Note:** For NPU execution, prefer a Q4_0 quantization. It is the format the Hexagon™ kernels are optimized for.

</Alert>

If you already have a `.gguf` file on the board — for example one you produced with `llama-quantize` while following the [llama.cpp tutorial](/tutorials/ventuno-q/llama-cpp) — register it from a local directory instead:

```bash
mkdir -p ~/models/my-model
cp ~/path/to/model.gguf ~/models/my-model/

geniex pull my-model --model-hub localfs --local-path ~/models/my-model
```

<Alert type="info">

**Note:** `--local-path` expects a directory or an AI Hub `.zip` archive, not a bare `.gguf` file. Pointing it straight at the file fails with `local path ... is a file but not a .zip`.

</Alert>

List what is cached at any time:

```bash
geniex list
```

| NAME                                      | SIZE    | PRECISIONS |
| ----------------------------------------- | ------- | ---------- |
| `google/gemma-4-E2B-it-qat-q4_0-gguf`     | 4.0 GiB | Q4_0       |

## Running Inference on the NPU

Run a model with `geniex infer`. The `--compute` flag selects the processor, and `npu` is the default:

```bash
geniex infer google/gemma-4-E2B-it-qat-q4_0-gguf:Q4_0 \
  --compute npu --max-tokens 32 --think=false \
  --prompt "Reply with exactly: NPU OK"
```

GenieX prints the reply followed by a summary line with the generation speed, the token count and the time to first token:

```text
NPU OK

— 12.8 tok/s • 3 tok • 0.2 s first token —
```

### Comparing the Processors

The GPU path requires Qualcomm's OpenCL driver. Install it before running the comparison:

```bash
sudo apt update
sudo apt install -y qcom-adreno-cl1
```

The same command with a different `--compute` value runs the identical model elsewhere on the chip, which makes the trade-off easy to see. The following results were measured on a VENTUNO Q running Ubuntu® 24.04 with the Gemma 4 E2B model, using the same 128-token prompt for every run:

| `--compute` | Runs on              | Generation speed |
| ----------- | -------------------- | ---------------- |
| `cpu`       | Kryo™ CPU            | 4.7 tok/s        |
| `gpu`       | Adreno™ 623          | 4.6 tok/s        |
| `hybrid`    | CPU and NPU together | 6.5 tok/s        |
| **`npu`**   | **Hexagon™ NPU**     | **12.7 tok/s**   |

The NPU is more than **twice as fast as the CPU** on this model, and it also reaches the first token in about 0.2 s, which is what makes a chat interface feel responsive.

For a comparison with setting up llama.cpp and Ollama directly, see [Running Local LLMs on Ventuno Q](/tutorials/ventuno-q/llama-cpp).

### Useful Flags

- `--max-tokens <n>` — cap the length of the reply.
- `--system-prompt "<text>"` — set the system prompt.
- `--think=false` — disable thinking mode for models that support it.
- `--nctx <n>` — context window size, for the llama.cpp runtime.
- `--temperature`, `--top-p`, `--top-k` — the usual sampling controls.

## Running a Vision Language Model

A VLM accepts images as well as text. The Gemma 4 E2B model already downloaded in this tutorial includes vision support, so no second model is required.

Pass an image by placing its absolute path inside angle brackets in the prompt:

```bash
geniex infer google/gemma-4-E2B-it-qat-q4_0-gguf:Q4_0 \
  --compute npu \
  --prompt "Describe this image </home/arduino/photos/example.png>"
```

The image must be available on the VENTUNO Q. GenieX encodes it on-device and returns the model's description in the terminal. Resize large photos before using them interactively: a 256 × 384 image takes about 32 seconds to reach the first token, while a 1200 × 1800 image takes about 194 seconds.

## Serving an OpenAI-Compatible API

To use the model from another device or from your own code, start the built-in server:

```bash
geniex serve
```

It listens on `127.0.0.1:18181` by default and exposes an OpenAI-compatible API. To reach it from elsewhere on your network, bind it to all interfaces:

```bash
geniex serve --host 0.0.0.0:18181 --compute npu
```

<Alert type="warning">

**Warning:** The server does not require authentication. Keep the default loopback binding unless remote access is necessary, and only expose it on a trusted network.

</Alert>

Find the board's network address with `hostname -I`. From a trusted device on the same network, open `http://<board-ip>:18181`. If both devices use Tailscale, run `tailscale ip -4` on the board and use that address instead. This opens the interactive Swagger API explorer, not a chat interface.

List the models the server can see:

```bash
curl http://127.0.0.1:18181/v1/models
```

```json
{"data":[{"id":"google/gemma-4-E2B-it-qat-q4_0-gguf:Q4_0","created":0,"object":"model","owned_by":"google"}],"object":"list"}
```

And send it a chat completion:

```bash
curl http://127.0.0.1:18181/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemma-4-E2B-it-qat-q4_0-gguf:Q4_0",
    "messages": [{"role": "user", "content": "Say hi in 3 words."}]
  }'
```

Add `"stream": true` to the request body to receive Server-Sent Events as tokens are generated.

VLMs use the same endpoint. Supply text and an absolute image path using OpenAI's multimodal message format:

```bash
curl http://127.0.0.1:18181/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemma-4-E2B-it-qat-q4_0-gguf:Q4_0",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "Describe this image in one sentence."},
        {"type": "image_url", "image_url": {"url": "/home/arduino/photos/example.png"}}
      ]
    }]
  }'
```

Because the API follows the OpenAI schema, clients that accept a custom base URL can talk to the board. Create a virtual environment and install the OpenAI Python package:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install openai
```

Then run:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:18181/v1",
    api_key="geniex",
)

response = client.chat.completions.create(
    model="google/gemma-4-E2B-it-qat-q4_0-gguf:Q4_0",
    messages=[{"role": "user", "content": "Say hi in 3 words."}],
)
print(response.choices[0].message.content)
```

The local server ignores the API key, but the client requires a non-empty value. See the [GenieX local server documentation](https://geniex.aihub.qualcomm.com/en/run/cli/local-server) for the complete API reference.

## Conclusion

In this tutorial you installed GenieX on the VENTUNO Q, downloaded one model for language and vision tasks, ran it on the Hexagon™ NPU, compared the NPU against the GPU and the CPU, and used the model through an OpenAI-compatible API.

The NPU path is the fastest way to run these models on this board and the least involved to set up. From here you can point an existing OpenAI-compatible application at the board or build multimodal applications that run entirely offline on the Dragonwing™ QCS8275 processor.
