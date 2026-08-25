---
title: 'App Lab Release Notes 0.9.0'
overwriteSidebar: Release 0.9.0
tags: [app-lab, releases]
description: 'This article contains release notes for App Lab version 0.9.0.'
author: Arduino Team
---

## Overview

This page contains all release notes for Arduino App Lab. To access the software, go [here](https://www.arduino.cc/en/software/#app-lab-section).

<Alert type="info">Note: You need to have an UNO Q ([2GB](https://store.arduino.cc/products/uno-q) or [4GB](https://store.arduino.cc/products/uno-q-4gb)) to use Arduino App Lab.</Alert>

## Release 0.9.0 [2026.07.09]

### TL;DR

#### What's New

*   Editor split-panel view
*   Expanded icon set for more file types
*   Drag-and-drop file interactions
*   Preview files on single click
*   Copy text from console panel
*   Support for model download
*   New Brick: LLM (UNO Q)

#### What's Fixed

*   Broken Brick add after using custom models
*   Prevent sketch.ino deletion resulting in broken Apps
*   Misc code editor and file explorer fixes
*   Workspace persistence stability in SBC mode

### Full Version

#### What's New

*   App Lab has a new split panel mode to simultaneously view two items at once, be them code or documentation files
*   The expanded icon set supports more file types
*   You can drag-and-drop files to move them to a folder or open them for viewing, works with multiple files at once
*   You can now preview files with a single click (double-click to open)
*   You can copy text from the console
*   There is included support for model download on both UNO Q and the upcoming VENTUNO Q
*   You can now visualize NPU usage on VENTUNO Q in the app's footer

**Bricks**

*   We updated the WebUI brick - better scaffolding of required web files
*   We added an LLM brick for UNO Q
*   We added Bricks and models for VENTUNO Q: ASR, TTS, LLM, VLM, Gesture Recognition

#### What's Fixed

*   Broken brick add after using custom models
*   Prevent sketch.ino deletion resulting in broken apps
*   Misc code editor and file explorer glitches
*   Improved workspace persistence stability in SBC mode
*   Misc cosmetic and functional enhancements

### GitHub Release

<Alert type="info">

You can always find the latest release [here](https://github.com/arduino/arduino-app-lab/releases).

</Alert>

If you have already downloaded App Lab once, you should get your updates automatically next time you open the software. You can also [download the latest release here](https://www.arduino.cc/en/software/#app-lab-section).
