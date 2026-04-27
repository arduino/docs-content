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

An **Arduino App** is a modular software architecture that orchestrates multiple components into a single functional unit. Unlike a traditional Arduino sketch, the core of an App is high-level **Python** logic running on the board's Linux subsystem. 

While an App is fundamentally a Python application, it is highly extensible. You can enhance it by adding **Bricks** (pre-built modular components like AI models or databases) and, on supported dual-processor boards, an optional **C++ sketch** for real-time hardware control.

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

<Alert type="info">**Note:** The `app.yaml` and `sketch.yaml` files are managed automatically by Arduino App Lab. You should not edit them manually unless you are an advanced user.</Alert>

## Storage Location

Your Apps are stored on your board, in the `/home/arduino/ArduinoApps/` directory.

Each App resides in its own subdirectory named after your App title.

## Next Steps

- [Manage Apps in Arduino App Lab](../../apps/manage-apps/)
