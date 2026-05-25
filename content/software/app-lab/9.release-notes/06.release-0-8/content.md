---
title: 'App Lab Release Notes 0.8.0'
overwriteSidebar: Release 0.8.0
tags: [app-lab, releases]
description: 'This article contains release notes for App Lab version 0.8.0.'
author: Arduino Team
---

## Overview

This page contains all release notes for Arduino App Lab. To access the software, go [here](https://www.arduino.cc/en/software/#app-lab-section).

<Alert type="info">Note: You need to have an UNO Q ([2GB](https://store.arduino.cc/products/uno-q) or [4GB](https://store.arduino.cc/products/uno-q-4gb)) to use Arduino App Lab.</Alert>

## Release 0.8.0 [2026.05.21]

### TL;DR

#### What's New

*   Enhanced Media Carrier Support (CSI cameras, LED control)
*   Improved security for web socket camera and microphone
*   Updated Cloud LLM models (Claude Sonnet 4.6 and GPT 5.4 mini)
*   Improved Music Composer Example UI

#### What's Fixed

*   Resolved camera availability issues
*   Corrected Python logging for Cloud LLM Brick
*   Fixed threshold handling for Vibration Anomaly Detection brick
*   Addressed volume selection for Theremin Example
*   Improved error banner position for Cloud AI Assistant
*   Updated documentation for various examples
*   Fixed threshold slider for Vibration Anomaly Detection

### Full Version

**Bricks**

Significant advancements in our Bricks ecosystem:

#### What's New (Bricks)

*   **Media Carrier Camera Support**: Now supports CSI cameras via the media carrier, enabling advanced vision applications.
*   **Media Carrier LED Control**: Gain control over LEDs using the media carrier, expanding interaction possibilities.
*   **Enhanced Web Socket Security**: Improved security measures for web socket camera and web socket microphone functionalities.
*   **Cloud LLM Model Updates**: We've updated our Cloud LLM models to the latest versions: Claude Sonnet 4.6 and GPT 5.4 mini, bringing more powerful AI capabilities to your projects.

#### What's Fixed (Bricks)

*   **Camera Availability**: Resolved an issue where the system would encounter a bug when no camera was available.
*   **Cloud LLM Logging**: Fixed Python logging for the Cloud LLM brick, ensuring more accurate debugging.
*   **Vibration Anomaly Detection Thresholds**: Corrected the threshold handling for the Vibration Anomaly Detection brick.

**Examples**

Improvements and fixes to our example applications:

#### What's New (Examples)

*   **Music Composer UI**: The Music Composer Example UI has been enhanced, now featuring an extended note range for more creative possibilities.

#### What's Fixed (Examples)

*   **Theremin Example Volume**: Fixed the volume selection issue in the Theremin Example.
*   **Cloud AI Assistant Error Banner**: Corrected the positioning of the error banner for the Cloud AI Assistant.
*   **Documentation Updates**: Comprehensive documentation updates for many examples, providing clearer guidance.
*   **Vibration Anomaly Detection Slider**: The threshold slider for the Vibration Anomaly Detection example has been fixed.

**Low-Level Changes**

A summary of underlying platform enhancements:

*   **Media Carrier Support**: Full support for the Media Carrier has been integrated through automatic updates, including a kernel update and the introduction of a new CLI tool: `arduino-linux-config`.
*   **TCP Port Forwarding**: Improved the forwarding of TCP ports when launching an app, resolving issues with applications utilizing services from Bricks.

### GitHub Release

<Alert type="info">You can always find the latest release [here](https://github.com/arduino/arduino-app-lab/releases). </Alert>

If you have already downloaded App Lab once, you should get your updates automatically next time you open the software. You can also [download the latest release here](https://www.arduino.cc/en/software/#app-lab-section).
