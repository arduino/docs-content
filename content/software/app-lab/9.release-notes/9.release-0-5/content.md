---
title: 'App Lab Release Notes 0.5.0'
overwriteSidebar: Release 0.5.0
tags: [app-lab, releases]
description: 'This article contains release notes of App Lab.'
author: Arduino Team
---

## Overview

This page contains all release notes for Arduino App Lab. To access the software, go [here](https://www.arduino.cc/en/software/#app-lab-section).

<Alert type="info">Note: You need to have an UNO Q ([2GB](https://store.arduino.cc/products/uno-q) or [4GB](https://store.arduino.cc/products/uno-q-4gb)) to use Arduino App Lab.</Alert>

## Release 0.5.0 [2026.02.27]

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

<Alert type="info">You can always find the latest release [here](https://github.com/arduino/arduino-app-lab/releases). </Alert>

If you have already downloaded App Lab once, you should get your updates automatically next time you open the software. You can also [download the latest release here](https://www.arduino.cc/en/software/#app-lab-section).