---
title: UNO R4 WiFi Network Examples
description: Discover examples compatible with the WiFi library included in the UNO R4 core.
author: Jacob Hylén
tags: [Wi-Fi, Web Server, AP Mode, SSL, UDP]
---

The [Arduino UNO R4 WiFi](/hardware/uno-r4-wifi) has a built in ESP32-S3 module that enables you to connect to Wi-Fi® networks, and perform network operations. Protocols including HTTPS, MQTT, UDP are tested and supported, and in this article, you will find a number of examples that will get you started.

Wi-Fi support is enabled via the built-in `WiFi` library that is shipped with the [Arduino UNO R4 Core](https://github.com/arduino/ArduinoCore-renesas). Installing the core automatically installs the `WiFi` library.

***The easiest way to connect your board to the Internet is via the [Arduino IoT Cloud](https://create.arduino.cc/iot/) platform. Here you can configure, program, monitor and synchronize your devices without having to write any networking code.*** 


## Hardware & Software Needed

- [Arduino UNO R4 WiFi](/hardware/uno-r4-wifi)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Examples

Examples listed in this section have been tested and verified to work. Most examples requires you to input the `SSID` and `PASSWORD` for your local Wi-Fi network. As a standard practice, in all of our examples, we store this in a separate header file (called `arduino_secrets.h`).

You will need to create this file, or remove the `#include "arduino_secrets.h"` file at the top of each example. The file should contain:

```arduino
//arduino_secrets.h header file
#define SECRET_SSID "yournetwork"
#define SECRET_PASS "yourpassword"
```

***Storing network & password in a separate file minimizes the risk of you accidentally sharing your Wi-Fi credentials.***

### WPA Connection

