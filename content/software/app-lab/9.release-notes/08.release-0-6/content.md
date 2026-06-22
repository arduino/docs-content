---
title: 'App Lab Release Notes 0.6.0'
overwriteSidebar: Release 0.6.0
tags: [app-lab, releases]
description: 'This article contains release notes of App Lab.'
author: Arduino Team
---

## Overview

This page contains all release notes for Arduino App Lab. To access the software, go [here](https://www.arduino.cc/en/software/#app-lab-section).

<Alert type="info">Note: You need to have an UNO Q ([2GB](https://store.arduino.cc/products/uno-q) or [4GB](https://store.arduino.cc/products/uno-q-4gb)) to use Arduino App Lab.</Alert>

## Releases

### Release 0.6.0 [2026.03.18]

Flashing and updating your board will now become easier, with the new board settings page! Set up your board, and explore the new Bricks and Examples in this newest release.

New Examples:

* Telegram Bot
* Music Composer
* Cloud AI Assistant

See a full list of what’s new and which bugs have been fixed below.

#### What’s new

* A new board settings page, with update and flash features
* Edge Impulse model update action when model has been retrained
* UI Updated
  * Device Discovery Page
  * Edge Impulse Integration
* Bricks
  * New: Sound Generator
  * New: Telegram Bot
  * New: Automatic Speech Recognition (Cloud)
  * Improvement: Wave Generator
  * All bricks now have a basic use example
* Examples
  * New: Telegram Bot
  * New: Music Composer
  * New: Cloud AI Assistant
  * Improvement: Thread safety on "Led Matrix Painter" sketch

#### What’s fixed

* Editor file tree and app edit actions issues
* Accessibility improvements (better keyboard support coverage)
* Sketch libraries needed by the examples are now downloaded as a part of the software update
* Arduino Apps description is now taken from the readme.md file (if not present in the app.yaml file)
* The arduino-router package now provides a CLI (arduino-router-client) to manually send messages, for test and debugging purposes
* Improved compilation speed when the sketch was not changed
* Bricks
  * Fix audio peripheral enumeration
  * Logging LLM provider logs in case of error
* Examples
  * Fix "Detect objects on smartphone camera" example in USB Mode
  * Fix "Detect objects on smartphone camera" example in case of multiple detection
  * Updated libraries used in sketches

<Alert type="info">You can always find the latest release [here](https://github.com/arduino/arduino-app-lab/releases). </Alert>

If you have already downloaded App Lab once, you should get your updates automatically next time you open the software. You can also [download the latest release here](https://www.arduino.cc/en/software/#app-lab-section).
