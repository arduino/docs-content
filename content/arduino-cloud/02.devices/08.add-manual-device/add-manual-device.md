---
title: Add a Manual Device
description: Create a generic (manual) device in Arduino Cloud and connect it from Python, MicroPython, or Node.js.
tags: [Arduino Cloud, Manual Device, Generic Device, Devices]
author: Karl Söderby & Arduino Team
---

A **manual** (or **generic**) device is a virtual device with no firmware requirement — anything that can authenticate with its **Device ID** and **Secret Key** can act as it. This is what **Manual Setup → Any device** creates in the Setup Device dialog. A Thing linked to a manual device has **no generated sketch**.

## Why Use a Manual Device

- Prototyping without flashing real hardware.
- Bridging a non-Arduino system — a Raspberry Pi running plain Linux, a server, or a Node.js backend — into Arduino Cloud.
- Reproducible demo and test setups, scriptable via `arduino-cloud-cli device create-generic`.

## Before You Start

What you need depends on the client you connect with:

- **Python**: [Python](https://www.python.org/) installed on your computer (check with `python --version`). The client is tested with Python 3.11.
- **MicroPython**: a supported board, such as GIGA R1 WiFi, Portenta H7 or Nano RP2040 Connect, running MicroPython 1.2 or later. See [MicroPython](/arduino-cloud/device-libraries/micropython) for setup.
- **JavaScript / Node.js**: [Node.js](https://nodejs.org/en) installed on your computer.

## Create the Device

1. Go to **Devices → + Device → Manual Setup → Any device**.
2. Name the device and continue.
3. Save the generated **Device ID** and **Secret Key**. You can download them as a PDF or copy them. The Secret Key is shown only once and cannot be retrieved after you close the window.

<Alert type="warning">

If you lose the Secret Key, delete the device and add it again to generate a new Device ID and Secret Key, then update your client code.

</Alert>

From the terminal, the equivalent is:

```bash
arduino-cloud-cli device create-generic --name <deviceName>
```

See [Managing Devices from the CLI](/arduino-cloud/apis-cli/cli-devices). To create and manage devices from your own code, use the [Devices section of the Arduino Cloud API reference](https://docs.arduino.cc/cloud-api/devices-api) and the [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks).

## Connect From Python, MicroPython, or Node.js

Use the client library that matches your language, then authenticate with the device credentials and register each Cloud Variable by name:

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

Each name passed to `register()` must exactly match a Cloud Variable already created on the linked [Thing](/arduino-cloud/things-data/things).

## How It Differs From an Arduino Board

- **No generated sketch** — you provide the connection logic in your own code.
- **No OTA** — over-the-air firmware updates are specific to Arduino firmware.
- Everything else (Variables, Dashboards, Triggers) works the same.

## Next Steps

- [Python Library](/arduino-cloud/device-libraries/python)
- [JavaScript Library](/arduino-cloud/device-libraries/javascript-nodejs)
- [Managing Devices from the CLI](/arduino-cloud/apis-cli/cli-devices)
- [Devices API reference](https://docs.arduino.cc/cloud-api/devices-api)
