---
title: Supported Boards & Capabilities
description: Board families supported by Arduino Cloud and which capabilities each supports — connectivity, OTA, and hardware-backed security.
tags: [Arduino Cloud, Devices, Boards, Reference]
author: Karl Söderby & Arduino Team
---

Arduino Cloud supports official Arduino boards across several connectivity types, third-party ESP32/ESP8266 boards, Linux-based boards, and purely software clients. This page summarizes the families and the capabilities each supports. For the step-by-step setup of each type, see [Devices Overview](/arduino-cloud/devices/devices-overview).

## Capability Summary

### Official Arduino Boards

| Board | Connectivity | Auth Method | OTA | Bluetooth® Provisioning |
|---|---|---|---|---|
| MKR WiFi 1010 | Wi-Fi® | Certificate + private key | Yes | Yes¹ |
| MKR 1000 WiFi | Wi-Fi® | Certificate + private key | No | No |
| Nano 33 IoT | Wi-Fi® | Certificate + private key | Yes | Yes¹ |
| Nano RP2040 Connect | Wi-Fi® | Certificate + private key | Yes | Yes¹ |
| Nano ESP32 | Wi-Fi® | Device ID + secret key | Yes | No |
| UNO R4 WiFi | Wi-Fi® | Device ID + secret key | Yes | Yes (Wi-Fi® firmware 0.6.0 or later) |
| GIGA R1 WiFi | Wi-Fi® | Certificate + private key | Yes | Yes |
| Nicla Vision | Wi-Fi® | Certificate + private key | Yes | Yes¹ |
| Portenta H7, Portenta H7 Lite Connected | Wi-Fi®; Ethernet with Portenta Vision Shield Ethernet, Max Carrier or Breakout | Certificate + private key | Yes | Yes¹ (Portenta H7) |
| Portenta Machine Control | Wi-Fi®, Ethernet | Certificate + private key | Yes | No |
| Portenta C33 | Wi-Fi®; Ethernet with Portenta Vision Shield Ethernet | Certificate + private key | No | No |
| Opta WiFi | Wi-Fi®, Ethernet | Certificate + private key | Yes | Yes |
| Opta RS485, Opta Lite | Ethernet | Certificate + private key | No | No |
| MKR GSM 1400 | Cellular (GSM) | Certificate + private key | No | No |
| MKR NB 1500 | Cellular (LTE-M, NB-IoT) | Certificate + private key | No | No |
| MKR WAN 1300, MKR WAN 1310 | LoRaWAN® (via The Things Stack) | AppEUI + AppKey | No | No |
| UNO Q, VENTUNO Q (Linux) | Wi-Fi® (via App Lab) | Managed by the board's Cloud connector | N/A | N/A |

¹ The board may first need to be [made compatible with BLE provisioning](/arduino-cloud/devices/network-configuration#make-a-board-compatible-with-ble-provisioning).

### Third-Party Boards and Software Clients

| Device | Connectivity | Auth Method | OTA | Bluetooth® Provisioning |
|---|---|---|---|---|
| ESP32 boards | Wi-Fi® | Device ID + secret key | Verified boards only (see below) | No |
| ESP8266 boards | Wi-Fi® | Device ID + secret key | Not verified | No |
| Manual / generic clients | Software (Python, MicroPython, JavaScript) | Device ID + secret key | No | No |

The following ESP32 boards have been tested and verified to support OTA: ESP32-S2-DevKitC, NODEMCU-32-S2, WEMOS LOLIN D32, ESP32-S3-DevKitC, ESP32-CAM, NodeMCU-32S, Freenove ESP32 WROVER, ESP32-DevKitC32E and DOIT ESP32 DevKit v1.

Older Ethernet hardware, such as the Ethernet Shield Rev2 and the MKR ETH Shield, is not supported. For the latest list of boards supported by the C++ library, see the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud?tab=readme-ov-file#what) repository.

<Alert type="info">

Boards **with a secure element** store a hardware-backed certificate and private key, so no secret key is ever exposed in the sketch. Official boards **without one**, such as UNO R4 WiFi and Nano ESP32, get their credentials configured automatically during setup. Third-party ESP32/ESP8266 boards and manual clients use a Device ID and Secret Key that you enter yourself. See [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).

</Alert>

## Connectivity Types

| Type | Notes |
|---|---|
| Wi-Fi® | The most common type; official boards support the 2.4 GHz band only (see [Supported Wi-Fi Frequencies](/arduino-cloud/reference/supported-wifi-frequencies)). |
| Ethernet | Wired connectivity for boards/shields that support it. |
| Cellular | GSM, LTE-M or NB-IoT for boards with a modem. |
| LoRaWAN® | Low-power long-range via The Things Stack integration. |

## Next Steps

- [Devices Overview](/arduino-cloud/devices/devices-overview)
- [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets)
- [Supported Wi-Fi Frequencies](/arduino-cloud/reference/supported-wifi-frequencies)

## Trademark Acknowledgments

- **LoRa®** and **LoRaWAN®** are registered trademarks of Semtech Corporation.
- **Wi-Fi®** is a registered trademark of Wi-Fi Alliance.
