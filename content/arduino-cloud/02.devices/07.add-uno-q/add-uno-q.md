---
title: Add an UNO Q
description: Provision an Arduino UNO Q — a Linux-based board — in Arduino Cloud through Arduino App Lab.
tags: [Arduino Cloud, UNO Q, App Lab, Devices]
author: Karl Söderby & Arduino Team
---

The Arduino **UNO Q** (and Ventuno Q) run a full Linux OS and connect to Arduino Cloud through the [arduino-cloud-connector](https://github.com/arduino/arduino-cloud-connector) daemon rather than an Arduino sketch. Provisioning and Cloud Variable exchange are handled by **Arduino App Lab**, not by code written directly against `ArduinoCloud`.

<Alert type="info">

The UNO Q board also documents this flow in its own hardware tutorial at `hardware/uno-q/tutorials/06.arduino-cloud`. Use that page for board-specific setup details.

</Alert>

## Provision the Device

1. In Arduino Cloud, go to **Devices → + Device → Automatic Setup → Arduino UNO Q & VENTUNO Q**. This generates a `device_id` / `secret_key` pair.
2. Create a [Thing](/arduino-cloud/things-data/things) with a Cloud Variable and associate this device with it, then build a [Dashboard](/arduino-cloud/dashboards/dashboards) — exactly as with any other device type.

## Connect From App Lab

In App Lab, an app is built from **Bricks**. The built-in example **"Blinking LED from Arduino Cloud"** (duplicate it via **Copy and edit app**) shows the pattern:

- Its **Arduino Cloud** Brick is configured (**Brick Configuration**) with the `device_id` / `secret_key` from provisioning and handles the MPU-side connection to Arduino Cloud.
- The app's `main.py` (running on the Linux/MPU side) reacts to Cloud Variable changes delivered through the Arduino Cloud Brick, and uses the **Bridge** tool to relay values to the microcontroller (MCU) side of the board — e.g. toggling a dashboard switch updates a variable, which `main.py` forwards over Bridge to turn an LED on or off.

<Alert type="warning">

Needs verification: the exact App Lab UI labels, Brick configuration steps, and whether the UNO Q path appears under Automatic or Manual Setup were not re-walked against real hardware in this pass. Confirm against a physical UNO Q and the current App Lab release before publishing.

</Alert>

## Next Steps

- [Devices Overview](/arduino-cloud/devices/devices-overview)
- [Things & Data](/arduino-cloud/things-data/things)
- [Dashboards](/arduino-cloud/dashboards/dashboards)
