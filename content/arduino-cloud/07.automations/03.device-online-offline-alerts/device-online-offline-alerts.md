---
title: Device Online/Offline Alerts
description: Get alerted when an Arduino Cloud device connects or disconnects, using its connection status as an automation condition.
tags: [Arduino Cloud, Device Status, Alerts, Automation]
author: TODO
---

Every [device](/arduino-cloud/devices/devices-overview) in Arduino Cloud
reports a **status** — whether it currently has an active connection. Alerting
on that status lets you know the moment a device goes **offline** (lost power,
out of range, crashed sketch) or comes back **online**, which is often more
important than any single variable reading.

## What Drives Device Status

The device's underlying connection reports connect/disconnect events that
update its status in near-real-time:

- **MQTT** for Arduino/C++ boards, ESP32/ESP8266, and manual (Python,
  MicroPython, Node.js) devices.
- **The connector daemon** for UNO Q / Ventuno Q Linux boards.

The status is shown in the Devices list' **Status** column and on the device
page. For the full picture, see
[Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle).

## Alerting on Connectivity

Arduino Cloud provides a dedicated **Device Status** trigger — you don't need a
value-based variable condition. To set one up:

1. Go to [Triggers](https://app.arduino.cc/triggers) and click **+ Trigger**.
2. Select **Device Status** as the trigger type.
3. Choose the device to track.
4. Select whether to be notified when it goes **online**, **offline**, or both.
5. Choose the timing — **immediately** on status change, or after a set delay
   (e.g. 1 hour after it changes).
6. Choose the action: **email** or **push notification** to the IoT Remote app.

See [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts) for the
general trigger UI and [Push Notifications](/arduino-cloud/iot-remote-app/push-notifications)
for the mobile side.

## Reading Status Programmatically

If you track connectivity from code rather than the Devices list, the REST
API models it through the device-status resources in
[iot-client-go](https://github.com/arduino/iot-client-go). See the
[APIs & CLI](/arduino-cloud/apis-cli/cli-devices) section.

## Next Steps

- [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts)
- [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle)
- [Choose an Automation](/arduino-cloud/automations/choose-an-automation)
