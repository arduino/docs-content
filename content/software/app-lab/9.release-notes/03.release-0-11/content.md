---
title: 'App Lab Release Notes 0.11.0'
overwriteSidebar: Release 0.11.0
tags: [app-lab, releases]
description: 'This article contains release notes for App Lab version 0.11.0.'
author: Arduino Team
---

## Overview

This page contains release notes for Arduino App Lab. To access the software, go [here](https://www.arduino.cc/en/software/#app-lab-section).

## Release 0.11.0 [YYYY.MM.DD]

This release introduces App releases, new integrations with Project Hub and Hugging Face, and an Agent panel inside the editor.

### What's new

* **App Releases:** Package an App into a ready-to-run release (`.ard` file) to deploy it to other boards or share a run-only copy. Install releases from the **Import or install App** dialog on the **Apps** page.
* **Project Hub Integration:** Publish your Apps on Arduino Project Hub as a project draft, directly from the App menu.
* **Hugging Face Integration:** Add language models for the **Large Language Model (LLM)** Brick from Hugging Face, using a model ID or URL.
* **Agent Panel:** Open the AI agent in a panel next to the editor (`⌘L` / `Ctrl+L`). The agent receives the open file and your selected code as context, and you can browse previous sessions from the panel.
* **Board Extensions:** Configure carriers attached to your board from the **Settings** page.
* **VENTUNO Q Flashing:** Flash the VENTUNO Q from the built-in flasher in the **Settings** page.
* **Editor Improvements:** **Find All References** for Python and C++, YAML linting, support for any file and folder name, and a separate console tab for each Brick container.

### New Bricks, Examples & Models

* **TPS Brick:** A new Brick that estimates the board's location by scanning nearby Wi-Fi access points, with accompanying examples.
* **Pose Estimation Brick:** A new Brick and the **Pose Detection** example for detecting body poses in video streams.
* **MCP Client Brick:** New examples demonstrating how to use the MCP Client Brick.
* **Visualize Smartphone Sensors:** A new example that streams sensor data from a smartphone to a web dashboard.
* **New AI models:** Desk Items Detector and Qwen 3-VL-8B VLM.

### Fixes

* **Editor Performance:** Files now load lazily, and typing in the editor no longer lags on the UNO Q.
* **Network Mode Folders:** Fixed a bug that caused folders to disappear while working in Network Mode.
* **Zephyr Auto-Update Loop:** Resolved an issue where the board incorrectly prompted for a Zephyr update immediately after a system update.
* **Brick Configurations:** Saving a Brick configuration from **Run** now starts the App instead of asking for the configuration again.
* **Single-Board Computer Mode:** App Lab now starts on the UNO Q when its local storage cannot be opened, and the **Remote access (SSH)** toggle works again.

### Release Information

App Lab updates automatically the next time you open it. All releases are available on [GitHub](https://github.com/arduino/arduino-app-lab/releases).
