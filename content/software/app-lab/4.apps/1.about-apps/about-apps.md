---
title: About Apps in Arduino App Lab
overwriteSidebar: About Apps
description: Understand the structure of an App, including the roles of sketch.ino, main.py, and app.yaml.
tags:
  - Architecture
  - Apps
  - Python
  - Arduino
---

An **Arduino App** is a project built around **Python** code that runs on the board's Linux system. Unlike a traditional Arduino sketch, the Python code is the core of the App. You can add **Bricks** (pre-built components such as AI models or databases) and, on dual-processor boards, an optional Arduino sketch for real-time hardware control.

## Anatomy of an App

Every App is a folder that can contain the following components:

- **The Logic Layer (Python):** Mandatory. The "brains" of your application running on Linux. This is where you write code for AI processing, networking, or web interfaces.
- **Bricks:** Optional. Pre-packaged services running alongside your logic in isolated Docker containers to provide specific features without implementing them from scratch.
- **The Real-Time Layer (Sketch):** Optional. The "muscles" of your application. This is standard Arduino C++ code running on an onboard microcontroller to interact directly with hardware pins and sensors.

When both a Python script and an Arduino sketch are present, they communicate through a system called the **Bridge**, allowing them to share data and trigger functions across processors.

## Project Structure

To ensure compatibility with the Arduino App Lab environment, every App follows a strict file organization.

| File | Status | Role |
| :--- | :--- | :--- |
| `app.yaml` | Mandatory | The manifest file that defines App metadata (name, icon) and active Bricks. |
| `python/main.py` | Mandatory | The entry point for the Python application logic. |
| `python/requirements.txt` | Optional | A list of external Python libraries (pip packages) needed by the App. |
| `sketch/sketch.ino` | Optional | The C++ code for the microcontroller. |
| `sketch/sketch.yaml` | Mandatory if sketch exists | Configuration for the sketch, including required libraries. |
| `README.md` | Optional | Documentation that is displayed in the App Lab UI. |
| `bricks/` | Optional | [Custom Bricks](../../bricks/custom-bricks/) created for this App. |
| `python-libraries/` | Optional | Python wheel files (`.whl`) installed when the App starts. |
| `data/` | Optional | Data stored by your App. Included in exports and releases only if you choose **Include data associated with the App**. |
| `.cache/` | Generated | The App's Python virtual environment and build cache. Excluded from exports. |

You can add any other files and folders your App needs, such as web assets for a WebUI Brick.

<Alert type="note">

**Important:** When you export an App or create a release without **Include data associated with the App**, every folder named `data` is left out, at any level of the App. A release built with this option only adds the `data/` folder at the top level of the App, so `data` folders inside other folders are always left out of releases. Don't use `data` as the name of a folder that contains code or assets your App needs.

</Alert>

<Alert type="info">

**Note:** The `app.yaml` and `sketch.yaml` files are managed automatically by Arduino App Lab. You should not edit them manually unless you are an advanced user.

</Alert>

## Storage Location

Your Apps are stored on your board, in the `/home/arduino/ArduinoApps/` directory. Each App resides in its own subdirectory named after your App title.

Built-in examples and installed [App releases](../manage-apps/#create-an-app-release) are stored separately, in `/var/lib/arduino-app-cli/examples/` and `/var/lib/arduino-app-cli/releases/`, and are read-only.

## Next Steps

- [Manage Apps in Arduino App Lab](../../apps/manage-apps/)
- [Develop Apps in Arduino App Lab](../../apps/develop-apps/)
- [Run and Monitor Apps](../../apps/run/)
