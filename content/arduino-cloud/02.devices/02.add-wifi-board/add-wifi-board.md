---
title: Add a Wi-Fi Board
description: Provision an official Arduino Wi-Fi board in Arduino Cloud, including the two authentication methods and the sketch pattern.
tags: [Arduino Cloud, Wi-Fi, Devices]
author: TODO
---

Wi-Fi® is the most common way to connect an official Arduino board to Arduino
Cloud. Provisioning registers the board, stores its credentials securely, and
generates a sketch that connects it to the platform.

## Supported Boards

Per [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud):
MKR 1000, MKR Wi-Fi® 1010, Nano 33 IoT, Portenta H7, Nano RP2040 Connect,
Nicla Vision, Opta Wi-Fi®, GIGA R1 Wi-Fi®, Portenta C33, UNO R4 Wi-Fi®, and
Nano ESP32.

## Authentication Methods

The method depends on whether the board has a secure element:

| Method | Boards | Where credentials live |
|---|---|---|
| **Certificate + private key** | MKR 1000, MKR Wi-Fi® 1010, Nano 33 IoT, Portenta H7, Nano RP2040 Connect, Nicla Vision, Opta Wi-Fi®, GIGA R1 Wi-Fi®, Portenta C33 | Hardware secure element (provisioned once) |
| **Login + secret key** | UNO R4 Wi-Fi®, Nano ESP32 | In the sketch / on-board storage |

## Provisioning the Board

1. Connect the board over USB. The first time, install the
   [Cloud Agent](/arduino-cloud/devices/cloud-agent) so the browser can reach
   the board.
2. Go to **Devices → + Device → Automatic Setup** and pick your Arduino board.
3. When the Cloud Agent detects the board, select **Configure**, name it, and
   choose the Wi-Fi® connection type.
4. The wizard securely provisions the device and generates its **Device ID**
   and, where applicable, a **Secret Key**.

![Selecting a connected board over USB.](assets/connect-with-usb.png)

The equivalent from the terminal is
`arduino-cloud-cli device create --fqbn <board-fqbn> --connection wifi` — see
[Managing Devices from the CLI](/arduino-cloud/apis-cli/cli-devices).

## Sketch Pattern

Once the device is associated with a [Thing](/arduino-cloud/things-data/things)
and network credentials are set, a sketch is generated automatically:

```arduino
#include "thingProperties.h"

void setup() {
  Serial.begin(9600);
  initProperties();
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
}

void loop() {
  ArduinoCloud.update();
}
```

`ArduinoIoTPreferredConnection` is a `WiFiConnectionHandler` configured with
your network SSID and password, generated into `thingProperties.h`.

## Next Steps

- [Network Configuration](/arduino-cloud/devices/network-configuration)
- [Arduino C++ Library](/arduino-cloud/device-libraries/arduino-cpp)
- [Quickstart: Your First IoT Project](/arduino-cloud/get-started/quickstart-first-project)
