---
title: Arduino / C++ Library
description: The ArduinoIoTCloud library allows you to connect to the Arduino Cloud using Arduino/C++. 
author: Karl Söderby
tags: [C++, Arduino]
---

The default Arduino / C++ library for the Arduino Cloud is the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) library. This library depends on the [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) library which provides connection via various wireless protocols (Wi-Fi®, LoRaWAN®, NB-IoT, GSM, Ethernet). 

The library is integrated into the Arduino Cloud platform, where [Automatic Sketch Generation](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/cloud-interface/sketches#iot-sketches) converts your Thing configurations into a set files that relies on aforementioned libraries.

The **ArduinoIoTCloud** library supports either connection via **TCP/IP** or **LoRaWAN®**. Depending on the device you compile for, the library automatically chooses the right configuration.

## GitHub

To view the source code and report issues, follow the links below to the GitHub repository:
- [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud/tree/master)

## Connection Methods

The ArduinoIoTCloud library supports both connection via TCP/IP and via LoRaWAN®, which is enabled via the `ArduinoIoTCloudTCP` and `ArduinoIoTCloudLPWAN` classes. Depending on what [device you configure](/arduino-cloud/hardware/devices), the library will automatically choose the right class, which will externally be available in your sketch file as `ArduinoCloud` class.

### TCP / MQTT

When connecting via [TCP/IP](https://en.wikipedia.org/wiki/Internet_protocol_suite) stack, the library communicates with the Arduino Cloud via [MQTT](https://en.wikipedia.org/wiki/MQTT), a lightweight network protocol using a publish/subscribe method to send data. This support is enabled in the following files:
- [ArduinoIoTCloudTCP.cpp](https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/src/ArduinoIoTCloudTCP.cpp)
- [ArduinoIoTCloudTCP.h](https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/src/ArduinoIoTCloudTCP.h)

### LoRaWAN®

When connecting via LoRaWAN®, data is sent via [The Things Network](https://www.thethingsnetwork.org/), which is integrated with the Arduino Cloud. This support is enabled in the following files:
- [ArduinoIoTCloudLPWAN.cpp](https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/src/ArduinoIoTCloudLPWAN.cpp)
- [ArduinoIoTCloudLPWAN.h](https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/src/ArduinoIoTCloudLPWAN.h)

## Library API Docs

The documentation lives in the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) library documentation page. Here you will find all public methods that are available. 

Most of its functions are already pre-configured in your sketch files, so for most use cases you will not need to explore the API. Functions for connecting to, and syncing data with the Arduino Cloud is handled automatically, and will be generated into your sketch files in the web environment. 

## Arduino IDE

This library can be used with the offline version of the Arduino IDE (download through the [Arduino Downloads Page](https://www.arduino.cc/en/software/)). You can program your devices offline and monitor them via the cloud, but your Thing configuration is not synchronized if you do so.