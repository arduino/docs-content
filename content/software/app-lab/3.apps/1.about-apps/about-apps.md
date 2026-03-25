---
title: About Apps in Arduino App Lab
nav_label: About Apps
description: Understand the structure of an App, including the roles of sketch.ino, main.py, and app.yaml.
tags:
  - Architecture
  - Apps
  - Python
  - Arduino
---

**Apps** are hybrid applications that combine the power of a Linux microprocessor (MPU) with the real-time reliability of an microcontroller (MCU) running Arduino sketches. Every app follows a specific structure to ensure compatibility with the Arduino App Lab environment.

## Overview

An App is a container for two separate programs that can communicate with each other:

*   **Python (`python/main.py`):** This script runs in the Linux environment on the board's microprocessor's. It handles high-level logic, AI models, networking, and web interfaces. It runs standard Python 3.
*   **Sketch (`sketch/sketch.ino`):** The Sketch runs on the board's microcontroller. It manages low-level hardware interactions, such as reading sensors and controlling motors, with real-time precision. The Sketch is written in the Arduino/C++ language.

## Core Files

Every app contains three primary configuration and source files:

| File | Status | Role |
| :--- | :--- | :--- |
| `app.yaml` | Mandatory | The App Descriptor manifest file that defines the App metadata, network ports, and active Bricks. |
| `python/main.py` | Mandatory | The entry point for the Python application. |
| `python/requirements.txt` | Optional | The standard Python dependency list. |
| `sketch/sketch.ino` | Mandatory if `sketch/` exists | The entry point for the Arduino microcontroller. |
| `sketch/sketch.yaml` | Mandatory if `sketch/` exists | The configuration file for the sketch. |
| `README.md` | Optional | A Markdown document that provides instructions to the user. |

<Alert type="info">**Note:** The `app.yaml` and `sketch.yaml` files are managed automatically by Arduino App Lab.</Alert>

## Storage Location

Your Apps are stored on your board, in the `/home/arduino/ArduinoApps/` directory.

Each App resides in its own subdirectory named after your App title.

## Next Steps

* [Manage Apps in Arduino App Lab](../../3.apps/2.manage-apps/manage-apps.md)
