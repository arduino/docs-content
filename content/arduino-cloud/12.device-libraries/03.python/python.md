---
title: Python
description: Connect a Python (CPython) client — on a Raspberry Pi or PC — to Arduino Cloud with arduino-iot-cloud-py.
tags: [Arduino Cloud, Python, Device Libraries]
author: TODO
---

Python (CPython) devices — a Raspberry Pi, a PC, a server — connect to Arduino
Cloud as a [manual (generic) device](/arduino-cloud/devices/add-manual-device),
using the same [arduino-iot-cloud-py](https://github.com/arduino/arduino-iot-cloud-py)
library that also supports [MicroPython](/arduino-cloud/device-libraries/micropython).
It syncs Cloud Variables over MQTT; it does not manage account resources — for
that, see the [REST API SDKs](/arduino-cloud/apis-cli/rest-api-sdks).

## Create a Generic Device

From the web UI, go to **Devices → + Device → Manual Setup → Any device**, or
from the terminal:

```bash
arduino-cloud-cli device create-generic --name <deviceName>
```

Save the generated **Device ID** and **Secret Key** — the key is shown only
once. Then create a [Thing](/arduino-cloud/things-data/things), bind it to the
generic device, and add [Cloud Variables](/arduino-cloud/things-data/cloud-variables).

## Install

```bash
pip install arduino-iot-cloud
```

<Alert type="note">

On some platforms the install also needs the
[`swig`](https://pypi.org/project/swig/) package (`pip install swig`) to build
successfully. Verify it worked by running `from arduino_iot_cloud import
ArduinoCloudClient` in an interpreter — no error means you're ready to connect.

</Alert>

## Minimal Example

```python
from secrets import DEVICE_ID, SECRET_KEY
from arduino_iot_cloud import ArduinoCloudClient

def on_switch_changed(client, value):
    client["led"] = value

client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY)
client.register("sw1", value=None, on_write=on_switch_changed)
client.register("led", value=None)
client.start()
```

`DEVICE_ID` and `SECRET_KEY` come from the generic device's credentials.
`register()` binds a Cloud Variable by name; `on_write` fires whenever the value
changes from the cloud side.

## Full Example

This script pushes a static value (`test_value`) to the Cloud and reacts to a
Boolean (`test_switch`) changed from a dashboard. Create matching variables of
type `int` and `boolean` on the Thing, and replace the credentials:

```python
import time
import logging

import sys
sys.path.append("lib")

from arduino_iot_cloud import ArduinoCloudClient

DEVICE_ID = b"YOUR_DEVICE_ID"
SECRET_KEY = b"YOUR_SECRET_KEY"

def logging_func():
    logging.basicConfig(
        datefmt="%H:%M:%S",
        format="%(asctime)s.%(msecs)03d %(message)s",
        level=logging.INFO,
    )

# Runs each time the "test_switch" variable changes
def on_switch_changed(client, value):
    print("Switch Pressed! Status is: ", value)

if __name__ == "__main__":
    logging_func()
    client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY)

    client.register("test_value")
    client["test_value"] = 20
    client.register("test_switch", value=None, on_write=on_switch_changed)

    client.start()
```

Run it with `python cloud_first_test.py`. Once connected, `test_value` updates
in the Thing, and toggling a switch widget linked to `test_switch` prints its
state in the terminal.

## Sync vs. Async Mode

- **Async (default)** — runs its own asyncio loop; just call `client.start()`.
- **Sync** (`sync_mode=True`) — you drive it: call `client.update()`
  periodically after `client.start()`. `update()` never blocks — it retries
  transient connection/discovery errors internally and only raises on a fatal
  `CloudConfigError` (e.g. the device isn't linked to a Thing).

## Advanced Authentication

Beyond Device ID + Secret Key, the client supports certificate/key pairs from
the filesystem or a PKCS#11 crypto element. See the repository's README for the
SoftHSM-based testing setup on CPython/Linux if you don't have real secure
hardware to test against.

<Alert type="info">

Common issues: `command not found: python` usually means the interpreter is
`python3` instead; a `Connection failed 5, retrying...` loop usually means the
Device ID or Secret Key is wrong; a `ModuleNotFoundError: No module named
'_m2crypto'` means the installed library version is out of date — update it.

</Alert>

## Managing the Cloud Side From Python

This library is for **device connection** only. To create, list, or delete
Things/Devices/Dashboards from Python instead, use the separate REST client
(`arduino-iot-client`) — see
[REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks).

## Next Steps

- [MicroPython](/arduino-cloud/device-libraries/micropython)
- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
- [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks)
