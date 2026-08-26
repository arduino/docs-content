---
title: 'Installing OpenClaw on VENTUNO Q'
overwriteSidebar: OpenClaw
description: 'A comprehensive guide to installing OpenClaw, setting up Telegram bot integration, and configuring AI models on your Arduino® VENTUNO™ Q board.'
difficulty: intermediate
tags:
  - OpenClaw
  - AI
  - Ubuntu
  - VENTUNO Q
  - Telegram
  - API Key
author: 'Karl Söderby, Ernesto Voltaggio'
compatible-products: [ventuno-q]
hardware:
  - hardware/14.ventuno/boards/ventuno-q
software:
  - app-lab
---

## Overview

This tutorial provides a step-by-step guide to installing OpenClaw on your Arduino® VENTUNO™ Q board, integrating it with a Telegram bot, and configuring an AI model for intelligent interactions. By the end of this tutorial, you will have a functional OpenClaw setup ready for your AI projects.

## Hardware & Software Needed

### Hardware

* [Arduino® VENTUNO™ Q](https://docs.arduino.cc/hardware/ventuno-q)
* [Arduino® USB-C Power Supply (65W)](https://store.arduino.cc/products/usb-c-power-supply-65w)
* USB-C® cable
* Computer with `adb` and `ssh` client installed

### Software

* Telegram account
* Google AI Studio account (or similar AI model provider) to obtain an API key

## Accessing the Board Shell

To access the shell (terminal) on your VENTUNO Q, you can use `adb` or `ssh`.

<Alert type="note">

**Important:** The VENTUNO Q board must be powered with a power supply connected to the power jack before connecting a USB-C® cable to your computer, otherwise the board may crash. The recommended power supply is a minimum of 65 W in the range of 7-24 V.

</Alert>

To connect via `adb`, connect a USB-C® cable between your VENTUNO Q and your computer, then run:

```bash
# Using adb (Android Debug Bridge)
adb shell
```

To connect via `ssh`, ensure your VENTUNO Q is connected to the same Wi-Fi® network as your computer, then run:

```bash
# Using ssh (Secure Shell)
ssh arduino@<ip-address>
```

<Alert type="info">

For more alternatives to remotely access your board, please see the [Remote Access](https://docs.arduino.cc/tutorials/uno-q/remote-access/) tutorial.

</Alert>

## Installing OpenClaw

This section will guide you through installing OpenClaw on your VENTUNO Q, which is powered by the Qualcomm® Dragonwing™ QCS8275 processor and runs Ubuntu.

OpenClaw is distributed as an `npm` package, so the installer needs a recent Node.js. The VENTUNO Q image does not ship Node.js, and the version in the Ubuntu® repositories is older than OpenClaw supports, so the installer offers to install a supported release for you. That step needs administrator rights, which is why the script asks for your password.

1. **Install OpenClaw:**
    Execute the following command to install OpenClaw:

    ```bash
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
    ```

    <Alert type="info">

    **Note:** Run this from an interactive terminal on the board. The installer prompts for your password to install Node.js, and it cannot read that prompt if you pipe the command through a non-interactive session.

    </Alert>

    The installer places OpenClaw in `~/.npm-global/bin` and adds that directory to your `PATH` in `~/.bashrc`.

2. **Reset Your Shell:**
    Reload your shell so that the new `PATH` takes effect:

    ```bash
    source ~/.bashrc
    hash -r
    ```

3. **Verify Installation:**
    You can verify that OpenClaw has been installed correctly by checking its version:

    ```bash
    openclaw --version
    ```

    This prints the installed release, for example `OpenClaw 2026.7.1-2`.

4. **Complete Onboarding:**
    Run the guided setup, which walks through authentication, model selection, the Gateway and your workspace:

    ```bash
    openclaw onboard
    ```

    You can re-run it at any time, and `openclaw doctor` checks the resulting setup and suggests fixes.

## Setting up Telegram Bot

Here, you'll create a new Telegram bot and obtain the necessary credentials to integrate it with OpenClaw.

1. **Start a Chat with BotFather:**

    Open Telegram and search for `BotFather`. Start a chat with it.

2. **Create a New Bot:**

    Send the command `/newbot` to BotFather and follow the instructions to choose a name and username for your bot. BotFather will provide you with an **HTTP API Token**. Save this token, as it will be used to configure OpenClaw.

3. **Get Your Chat ID:**

    To enable your bot to send messages to you, you need your Telegram Chat ID. Start a conversation with your newly created bot by sending it any message. Then, you can use a service like `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` in your web browser (replace `<YOUR_BOT_TOKEN>` with your bot's API token) to find your chat ID in the JSON response. Look for the `id` field within the `chat` object.

## Configuring AI Model and API Key

OpenClaw supports various AI models. For this tutorial, we will focus on configuring a model like Google Gemini.

1. **Obtain an API Key:**

    If you are using Google Gemini, you can obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey). Follow the instructions to create a new API key.

2. **Configure OpenClaw with your API Key:**

    Credentials and model selection are handled by the interactive configuration command:

    ```bash
    openclaw configure
    ```

    This walks through credentials, channels, the Gateway and agent defaults, and writes the result to OpenClaw's configuration file.

    To see which models OpenClaw can reach with the credentials you supplied:

    ```bash
    openclaw models list
    ```

3. **Inspect the Configuration File (Optional):**
    OpenClaw stores its configuration as JSON at `~/.openclaw/openclaw.json`. You rarely need to edit it by hand — the `config` subcommands read and write it safely:

    ```bash
    openclaw config file      # print the configuration file path
    openclaw config get       # read the current configuration
    openclaw config validate  # check the file is well formed
    ```

## Running OpenClaw Gateway and Chat Functions

With OpenClaw installed and configured, you can now run its gateway and chat functions.

1. **Connect the Telegram Channel:**

    Register the bot token you obtained from BotFather. Telegram is one of OpenClaw's supported channels:

    ```bash
    openclaw channels add --channel telegram --bot-token <YOUR_BOT_TOKEN>
    ```

    Check that the channel came up:

    ```bash
    openclaw channels status
    openclaw status
    ```

2. **Run the OpenClaw Gateway:**

    The Gateway is the WebSocket service that connects your channels to the AI model. On a board you normally want it running in the background and surviving reboots, which the built-in installer sets up as a `systemd` service:

    ```bash
    openclaw gateway install
    ```

    To check that it is healthy:

    ```bash
    openclaw gateway health
    openclaw doctor
    ```

3. **Chat With Your Agent:**

    Send your Telegram bot a message and OpenClaw processes it with the model you configured. You can also talk to the same agent from the board's terminal:

    ```bash
    openclaw chat
    ```

    `openclaw channels logs` shows recent channel activity if a message does not arrive as expected.

## Conclusion

You have successfully installed OpenClaw on your VENTUNO Q, set up Telegram bot integration, and configured an AI model. You can now explore the capabilities of OpenClaw and develop your own AI-powered applications on your board.
