---
title: 'App Lab Release Notes'
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
  * Fix "Detect objects on smartphone camera" example in usb mode
  * Fix "Detect objects on smartphone camera" example in case of multiple detection
  * Updated libraries used in sketches

<Alert type="info">You can always find the latest release [here](https://github.com/arduino/arduino-app-lab/releases). </Alert>

## Previous Releases

Below is a list of release notes for previous versions.

### Release 0.5.0 [2026.02.27]

<details>
  <summary><strong>Details</strong></summary>

You can now connect App Lab with Arduino Cloud and your Edge Impulse account! This means that you can now use the IoT Remote App as a camera input to your examples, as well as create your own custom models using Edge Impulse.

New Examples: 

* Color Your LEDs
* Video Object Detection on Mobile

See a full list of what's new and which bugs have been fixed below.

#### What's new

* Connect App Lab with Edge Impulse Account
* Edge Impulse Custom Model integration
* Switch boards from the footer
* Use Command Line to import/export Arduino Apps
* UI updated
  * What’s new pop up during update
  * Notifications update
  * Persistent Editor Panel sizing on tab change or restart
  * Other UI improvements
* Bricks
  * New: Web Socket Camera integration with Arduino IoT Remote App
  * Improvement: Camera peripheral, brick documentation
* Examples
  * New: Color your LEDs
  * New: Video Object Detection on Mobile
  * Improvements: LED Matrix Painter

#### What's fixed

* HTML syntax highlighting lost on scroll
* Board discovery: duplicates and network mode shown when USB connection available
* Allow Skip/Change network when “check for updates“ fails
* Misc cosmetic/behavioral defects
* Updates will download only the minimum required data, instead of re-downloading all the container images each time
* app-cli commands now also autocomplete app names as “folder names”
* Fixed an error when checking for updates and there are no platform updates
* Bricks
  * Minor fixes on Camera peripheral discovery and Speaker peripheral discovery
* Examples
  * Fixes on Object Detection in case of multiple detection

#### GitHub Release

https://github.com/arduino/arduino-app-lab/releases/tag/al-0.5.0

</details>

### Release 0.4.0 [2026.02.06]

<details>
  <summary><strong>Details</strong></summary>

#### What's New

* Flasher tool integrated in App Lab (for outdated boards)
* Skip WiFi step with warning (WiFi dependent features not managed yet)
* Syntax highlighting for Web dev code (js/ts, css/scss, html, json)
* Analytics enhancement to distinguish SBC/PC users
* Persist app logs when Arduino Apps crash unexpectedly
* Editor QOL updates
* UI rework

#### What's Fixed

* Disappearing App.yaml/README.md on app/brick configuration
* Arduino App UI occasionally not opening
* Unmanaged “wrong password” when connecting network mode
* SBC/network mode corrupt README.md loading in UI
* Security fixes for open source repo
* Miscellaneous behavioural and cosmetic corrections

#### GitHub Release

https://github.com/arduino/arduino-app-lab/releases/tag/al-0.4.0

</details>

<br></br>

If you have already downloaded App Lab once, you should get your updates automatically next time you open the software. You can also [download the latest release here](https://www.arduino.cc/en/software/#app-lab-section). 
