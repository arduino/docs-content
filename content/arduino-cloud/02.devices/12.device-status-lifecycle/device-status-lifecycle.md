---
title: Device Status & Lifecycle
description: How Arduino Cloud reports whether a device is online or offline, and what drives its connection status.
tags: [Arduino Cloud, Device Status, Devices]
author: Karl Söderby & Arduino Team
---

Each device shows a **status** indicator, visible in the Status column of the Devices list and on the device page. The status describes the connection between the device and Arduino Cloud.

<Alert type="note">

Device status is not supported by the LoRa® communication protocol. LoRaWAN® devices, such as the MKR WAN 1300 and MKR WAN 1310, never report as online. To check that a LoRaWAN® device is sending data, look at the **Last Value / Last Update** of its Thing's variables instead (see [Add a LoRaWAN Device](/arduino-cloud/devices/add-lorawan-device#verifying-data)).

</Alert>

## Status Values

| Status | Meaning |
|---|---|
| **Online** | The device is connected and communicating with Arduino Cloud. Its variables are syncing. |
| **Offline** | The device has initialized a connection but is not connected to Arduino Cloud, for example because it is powered down, out of network range, or not running a Cloud-connected sketch. |
| **Unknown** | Device status is not supported for this device, for example a LoRaWAN® device. |

After you upload a sketch, it may take a few minutes before the status changes to **Online**.

The device's information panel also shows a **Last Activity** timestamp, the time of its last synchronization with Arduino Cloud.

## Device Status History

The **Device Status History** shows how the status of a device has changed over time, so you can see when it connected or disconnected and how long it has been in its current state. To open it:

1. Go to **Devices**.
2. Select the device name to open the device page.
3. The Device Status History is at the top right of the page.

## Get Notified When the Status Changes

You can create a [Trigger](/arduino-cloud/automations/device-online-offline-alerts) that sends an email or a push notification when a device goes online or offline, either immediately or after it has been in the new state for a set time.

## What Drives the Status

Status is driven by the device's underlying connection:

- **MQTT** for Arduino/C++ boards, ESP32/ESP8266, and manual (Python, MicroPython, Node.js) devices.
- **The connector daemon** for UNO Q / Ventuno Q Linux boards.

On Arduino hardware, the connection itself is managed by the [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) library (handling Wi-Fi®, LoRa®-based network, Ethernet, NB-IoT, and GSM) on top of [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud). Each reports connect and disconnect events, which update the status in near-real-time.

## Reading Status Programmatically

To track status from your own code or scripts, use the Arduino Cloud APIs instead of the Devices list:

- The [Devices section of the Arduino Cloud API reference](https://docs.arduino.cc/cloud-api/devices-api) documents the device resource, including its connection status and the connection status events of a device.
- The official API clients for [Python, JavaScript and Go](/arduino-cloud/apis-cli/rest-api-sdks) wrap the same endpoints.
- [arduino-cloud-cli](/arduino-cloud/apis-cli/cli-devices) lists and manages devices from the terminal, for scripted checks.

See [APIs & CLI](/arduino-cloud/apis-cli/developer-overview) for an overview of all the options and how to authenticate.

## Next Steps

- [Troubleshoot Device Connections](/arduino-cloud/devices/troubleshoot-device-connections)
- [Devices Overview](/arduino-cloud/devices/devices-overview)
- [Manage Devices at Scale](/arduino-cloud/devices/manage-devices-at-scale)
