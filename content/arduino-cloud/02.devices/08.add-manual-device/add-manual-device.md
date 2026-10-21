---
title: Add a Manual Device
description: Create a generic (manual) device in Arduino Cloud and connect it from Python, MicroPython, or Node.js.
tags: [Arduino Cloud, Manual Device, Generic Device, Devices]
author: Karl Söderby & Arduino Team
---

A **manual** (or **generic**) device is a virtual device with no firmware
requirement — anything that can authenticate with its **Device ID** and
**Secret Key** can act as it. This is what **Manual Setup → Any device**
creates in the Setup Device dialog. A Thing linked to a manual device has **no
generated sketch**.

## Why Use a Manual Device

- Prototyping without flashing real hardware.
- Bridging a non-Arduino system — a Raspberry Pi running plain Linux, a server,
  or a Node.js backend — into Arduino Cloud.
- Reproducible demo and test setups, scriptable via
  `arduino-cloud-cli device create-generic`.

## Create the Device

1. Go to **Devices → + Device → Manual Setup → Any device**.
2. Name the device and continue.
3. Save the generated **Device ID** and **Secret Key** — the key is shown only
   once.

From the terminal, the equivalent is:

```bash
arduino-cloud-cli device create-generic --name <deviceName>
```

See [Managing Devices from the CLI](/arduino-cloud/apis-cli/cli-devices).

## Connect From Python, MicroPython, or Node.js

Use the client library that matches your language, then authenticate with the
device credentials and register each Cloud Variable by name:

| Language | Library | Guide |
|---|---|---|
| Python / MicroPython | arduino-iot-cloud-py | [Python](/arduino-cloud/device-libraries/python), [MicroPython](/arduino-cloud/device-libraries/micropython) |
| JavaScript / Node.js | arduino-iot-js | [JavaScript](/arduino-cloud/device-libraries/javascript-nodejs) |

```python
client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY)

client.register("temperature")
client["temperature"] = 20

client.register("ledSwitch", value=None, on_write=on_switch_changed)

client.start()
```

Each name passed to `register()` must exactly match a Cloud Variable already
created on the linked [Thing](/arduino-cloud/things-data/things).

## How It Differs From an Arduino Board

- **No generated sketch** — you provide the connection logic in your own code.
- **No OTA** — over-the-air firmware updates are specific to Arduino firmware.
- Everything else (Variables, Dashboards, Triggers) works the same.

## Next Steps

- [Python Library](/arduino-cloud/device-libraries/python)
- [JavaScript Library](/arduino-cloud/device-libraries/javascript-nodejs)
- [Managing Devices from the CLI](/arduino-cloud/apis-cli/cli-devices)
