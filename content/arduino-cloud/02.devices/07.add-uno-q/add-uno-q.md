---
title: Add an UNO Q
description: Provision an Arduino UNO Q — a Linux-based board — in Arduino Cloud through Arduino App Lab.
tags: [Arduino Cloud, UNO Q, App Lab, Devices]
author: Karl Söderby & Arduino Team
---

The Arduino **UNO Q** (and VENTUNO Q) run a full Linux OS and connect to Arduino Cloud through the [arduino-cloud-connector](https://github.com/arduino/arduino-cloud-connector) service rather than an Arduino sketch. You connect the board to Arduino Cloud directly from **Arduino App Lab**. Once connected to your Cloud space, the board is provisioned automatically and is ready to exchange data with your apps. You don't need to copy a Device ID or Secret Key.

The communication with Arduino Cloud runs on the board's microprocessor (MPU) and is programmed in Python. Data to and from the microcontroller (MCU) is handled by the [Bridge](/software/app-lab/getting-started/quickstart/#bridge-tool) tool.

## What You Need

- An [Arduino UNO Q](https://store.arduino.cc/products/uno-q) or VENTUNO Q.
- An [Arduino account](https://login.arduino.cc/login).
- [Arduino App Lab](https://www.arduino.cc/en/software) installed on your computer.

## Connect the Device

You can start from Arduino Cloud or directly from App Lab:

1. *Optional:* In [Arduino Cloud](https://app.arduino.cc/), go to **Devices**, select **+ Device**, and choose **Arduino UNO Q** (or the matching Q device). Arduino Cloud asks you to open App Lab, or to download it if it is not installed.
2. Open Arduino App Lab, go to the device settings, and select **Connect** in the **Cloud** section.
3. If you are not logged in to App Lab with your Arduino account, a web login page opens. Log in, and App Lab reopens automatically.
4. Select the Cloud space to add the device to. You can choose your personal space or an organization space.
5. A confirmation message appears, and the device is listed in **Devices** in the selected space.

## Set Up the Thing and Dashboard

1. Create a [Thing](/arduino-cloud/things-data/things) and associate the UNO Q device with it.
2. Add a **Boolean** Cloud Variable named `led`.
3. Create a [Dashboard](/arduino-cloud/dashboards/dashboards), select **Edit**, and select the Thing. A switch widget is assigned to the `led` variable automatically.

## Run the Cloud Example in App Lab

In App Lab, an app is built from **Bricks**. The built-in example **Blinking LED from Arduino Cloud** shows the pattern:

1. Open the **Examples** tab and select **Blinking LED from Arduino Cloud**.
2. Select **Copy and edit app** to duplicate the example.
3. The **Arduino Cloud** Brick is already added to the app. No configuration is needed: the board is already connected to your Cloud space and connects automatically.
4. Select **Run** and wait until the app has launched.

When you toggle the dashboard switch, Arduino Cloud updates the `led` variable. The app's `main.py`, running on the MPU, receives the change through the Arduino Cloud Brick and uses Bridge to tell the MCU to turn the LED on or off.

For the full walkthrough with screenshots, see [Connect UNO Q to the Arduino Cloud](/tutorials/uno-q/arduino-cloud/).

## Next Steps

- [Devices Overview](/arduino-cloud/devices/devices-overview)
- [Things & Data](/arduino-cloud/things-data/things)
- [Dashboards](/arduino-cloud/dashboards/dashboards)
