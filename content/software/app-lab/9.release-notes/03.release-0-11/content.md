---
title: 'App Lab Release Notes 0.11.0'
overwriteSidebar: Release 0.11.0
tags: [app-lab, releases]
description: 'This article contains release notes for App Lab version 0.11.0.'
author: Arduino Team
---

## Overview

This page contains release notes for Arduino App Lab. To access the software, go [here](https://www.arduino.cc/en/software/#app-lab-section).

## Release 0.11.0 [2026.10.22]

This release introduces App releases, new integrations with Project Hub and Hugging Face, an Agent panel inside the editor, and board extensions.

### What's New

* **App Releases:** Package an App into a read-only release (`.ard` file) that runs exactly as it did when you created it, to deploy it to other boards or share a run-only copy. Create a release from the App menu, and install one from the **Import or install App** dialog on the **Apps** page. Installed releases are read-only and can be copied for editing. See [Create an App Release](../../apps/manage-apps/#create-an-app-release).
* **Project Hub Integration:** Upload your App to Arduino Project Hub as a project draft, directly from the App menu. See [Publish on Project Hub](../../apps/manage-apps/#publish-on-project-hub).
* **Hugging Face Integration:** Add language models for the **Large Language Model (LLM)** Brick from Hugging Face, using a model ID or URL. App Lab checks that the model is compatible and selects a suitable quantization automatically. See [Add Models from Hugging Face](../../integrations/models/#add-models-from-hugging-face).
* **Agent Panel:** Open the AI agent in a panel next to the editor (`⌘L` / `Ctrl+L`). The agent receives the open file and your selected code as context. Sessions are now organized per App, and you can browse an App's previous sessions from the panel. See [Agent Mode](../../integrations/agent-mode/).
* **Board Extensions:** Declare carriers and JHat add-ons attached to your board from the **Settings** page. See [Board extensions](../../configure/settings/#board-extensions).
* **VENTUNO Q Flashing:** Flash the VENTUNO Q from the built-in flasher in the **Settings** page.
* **Editor Improvements:** A **References** panel that lists the results of **Find All References**, YAML syntax checking, support for any file and folder name, a separate console tab for each Brick container, and UI zoom (`⌘+`/`⌘-`/`⌘0` on macOS, `Ctrl++`/`Ctrl+-`/`Ctrl+0` on Linux, and `Ctrl` + scroll wheel on Windows). The **Python** console tab is now selected automatically when you run an App.

### Arduino App CLI 0.14

* **Release Commands:** Build and install App releases from the board's terminal with `app build` and `app install`.
* **App Status:** `app list` now shows the Apps catalog only. Use the new `app ps` command to see the live status of Apps on the board.
* **New Commands:** `app details` shows an App's metadata, Bricks, and variables, `app ports` lists the ports an App exposes, and `app brick config` sets Brick variables and models from the terminal.
* **Hugging Face Models:** `model install` accepts Hugging Face IDs (`llamacpp:owner/repo:quant`, or `owner/repo`) and model file URLs.

See the [Arduino App CLI command reference](../../cli/commands/).

### Bridge and Python API

* **Python Bridge:** The Python `Bridge` now uses the standalone `arduino-router-bridge` library. It connects to the Arduino Router the first time you use it and raises an `AppError` if the router can't be reached within 5 seconds. Functions registered with `Bridge.provide()` run one at a time on a dedicated thread, are registered again automatically after a reconnection, and raise a `RuntimeError` if they try to use `Bridge.call()`. `Bridge.call()` also raises a `ConnectionError` if the connection drops while it waits. The `@call`, `@notify`, and `@provide` decorators no longer accept an `address` argument. See the [Bridge API Reference](../../bridge/bridge-api/).

### New Bricks, Examples & Models

* **Pose Estimation Brick (VENTUNO Q):** A new Brick and the **Pose Detection** example for detecting up to 10 body poses in a camera stream.
* **TPS Brick:** A new Brick that estimates the board's location from nearby Wi-Fi access points, using the Qualcomm TPS Location API cloud service. Requires TPS credentials and an internet connection.
* **MCP Client Brick:** New examples demonstrating how to use the MCP Client Brick, including with a custom Brick and the LLM Brick.
* **Visualize Smartphone Sensors:** Use the Arduino IoT Remote App to stream smartphone sensor data to a web dashboard.
* **New AI models:** Desk Items Detector and Qwen 3-VL-8B VLM.

### Fixes

* **Editor Performance:** Files now load lazily, and typing in the editor no longer lags on the UNO Q.
* **Network Mode Folders:** Fixed a bug that caused folders to disappear while working in Network Mode.
* **Zephyr Auto-Update Loop:** Resolved an issue where the board incorrectly prompted for a Zephyr update immediately after a system update.
* **Brick Configurations:** Saving a Brick configuration from **Run** now starts the App instead of asking for the configuration again.
* **Single-Board Computer Mode:** App Lab now starts on the UNO Q when its local storage cannot be opened, and the **Remote access (SSH)** toggle works again.
* **Operating System Update:** The **Update now** button in the **Operating system** section of **Settings** now opens the flasher.
* **Console:** Cleared Python logs no longer reappear when you run the App again.
* **Run at Startup:** The **Run at startup** toggle now shows the correct state after the board restarts.
* **Temporary Files:** App Lab no longer leaves a copy of the flasher in the temporary folder each time it runs. On the UNO Q, this could fill the memory and make App Lab crash in Single-Board Computer Mode.

### Release Information

App Lab updates automatically the next time you open it. All releases are available on [GitHub](https://github.com/arduino/arduino-app-lab/releases).
