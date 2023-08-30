---
title: UNO R4 WiFi Network Examples
description: Discover examples compatible with the WiFi library included in the UNO R4 core.
author: Jacob Hylén
hardware:
  - hardware/02.hero/boards/uno-r4-wifi
tags: [Wi-Fi, Web Server, AP Mode, SSL, UDP]
---

The [Arduino UNO R4 WiFi](/hardware/uno-r4-wifi) has a built in ESP32-S3 module that enables you to connect to Wi-Fi® networks, and perform network operations. Protocols including HTTPS, MQTT, UDP are tested and supported, and in this article, you will find a number of examples that will get you started.

Wi-Fi® support is enabled via the built-in `WiFiS3` library that is shipped with the [Arduino UNO R4 Core](https://github.com/arduino/ArduinoCore-renesas). Installing the core automatically installs the `WiFiS3` library.

***The easiest way to connect your board to the Internet is via the [Arduino IoT Cloud](https://create.arduino.cc/iot/) platform. Here you can configure, program, monitor and synchronize your devices without having to write any networking code.*** 


## Hardware & Software Needed

- [Arduino UNO R4 WiFi](/hardware/uno-r4-wifi)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Examples

Examples listed in this section have been tested and verified to work. Most examples require you to input the `SSID` and `PASSWORD` for your local Wi-Fi® network. As a standard practice, in all of our examples, we store this in a separate header file (called `arduino_secrets.h`).

You will need to create this file, or remove the `#include "arduino_secrets.h"` file at the top of each example. The file should contain:

```arduino
//arduino_secrets.h header file
#define SECRET_SSID "yournetwork"
#define SECRET_PASS "yourpassword"
```

***Storing your network & password in a separate file minimizes the risk of you accidentally sharing your Wi-Fi® credentials.***

### Access Point
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/AP_SimpleWebServer/AP_SimpleWebServer.ino" className="arduino"/>

### Connect With WPA
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/ConnectWithWPA/ConnectWithWPA.ino" className="arduino"/>

### Scan Networks
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/ScanNetworks/ScanNetworks.ino" className="arduino"/>

### Scan Networks (Advanced)
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/ScanNetworksAdvanced/ScanNetworksAdvanced.ino" className="arduino"/>

### Simple Webserver
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/SimpleWebServerWiFi/SimpleWebServerWiFi.ino" className="arduino"/>

### Wi-Fi® Chat Server
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/WiFiChatServer/WiFiChatServer.ino" className="arduino"/>

### Wi-Fi® UDP NTP Client
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/WiFiUdpNtpClient/WiFiUdpNtpClient.ino" className="arduino"/>

### Wi-Fi® UDP Send Receive String
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino" className="arduino"/>

### Wi-Fi® Web Client
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/WiFiWebClient/WiFiWebClient.ino" className="arduino"/>

### Wi-Fi® Web Client Repeating
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/WiFiWebClientRepeating/WiFiWebClientRepeating.ino" className="arduino"/>

### Wi-Fi® Web Client SSL
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/WiFiWebClientSSL/WiFiWebClientSSL.ino" className="arduino"/>

### Wi-Fi® Web Server
<CodeBlock url="https://github.com/arduino/ArduinoCore-renesas/blob/main/libraries/WiFiS3/examples/WiFiWebServer/WiFiWebServer.ino" className="arduino"/>