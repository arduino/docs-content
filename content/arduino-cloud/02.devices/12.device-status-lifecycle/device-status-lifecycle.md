---
title: Device Status & Lifecycle
description: How Arduino Cloud reports whether a device is online or offline, and what drives its connection status.
tags: [Arduino Cloud, Device Status, Devices]
author: Karl Söderby & Arduino Team
---

Every device shows a **status** indicator — visible in the Status column of the Devices list and on the device page — reflecting whether it currently has an active connection to Arduino Cloud.

## Online and Offline

The two states you'll see most are:

- **Online** — the device has an active connection and its variables are syncing.
- **Offline** — the device has no active connection (powered down, out of network range, or not running a Cloud-connected sketch).

The device page also keeps a **connection history**, and the device's information panel shows a **Last Activity** timestamp — the time of its last synchronization with Arduino Cloud — so you can see when it last connected and how long it has been in its current state.

## What Drives the Status

Status is driven by the device's underlying connection:

- **MQTT** for Arduino/C++ boards, ESP32/ESP8266, and manual (Python, MicroPython, Node.js) devices.
- **The connector daemon** for UNO Q / Ventuno Q Linux boards.

On Arduino hardware, the connection itself is managed by the [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) library (handling Wi-Fi®, LoRa®-based network, Ethernet, NB-IoT, and GSM) on top of [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud). Each reports connect and disconnect events, which update the status in near-real-time.

## Reading Status Programmatically

If you track status from code rather than the Devices list, the REST API models it through the device-status resources in [iot-client-go](https://github.com/arduino/iot-client-go). See the [APIs & CLI](/arduino-cloud/apis-cli/cli-devices) section.

## Next Steps

- [Troubleshoot Device Connections](/arduino-cloud/devices/troubleshoot-device-connections)
- [Devices Overview](/arduino-cloud/devices/devices-overview)
- [Manage Devices at Scale](/arduino-cloud/devices/manage-devices-at-scale)
