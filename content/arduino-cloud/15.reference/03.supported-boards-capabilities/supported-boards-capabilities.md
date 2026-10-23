---
title: Supported Boards & Capabilities
description: Board families supported by Arduino Cloud and which capabilities each supports — connectivity, OTA, and hardware-backed security.
tags: [Arduino Cloud, Devices, Boards, Reference]
author: Karl Söderby & Arduino Team
---

Arduino Cloud supports official Arduino boards across several connectivity types, third-party ESP32/ESP8266 boards, Linux-based boards, and purely software clients. This page summarizes the families and the capabilities each supports. For the step-by-step setup of each type, see [Devices Overview](/arduino-cloud/devices/devices-overview).

## Capability Summary

| Family | Connectivity | Auth Method | OTA | Secure Element |
|---|---|---|---|---|
| MKR WiFi 1010, MKR 1000 | Wi-Fi® | Certificate + private key | Yes | Yes |
| Nano 33 IoT, Nano RP2040 Connect | Wi-Fi® | Certificate + private key | Yes | Yes |
| Portenta H7, Portenta C33, Nicla Vision | Wi-Fi® | Certificate + private key | Yes | Yes |
| GIGA R1 Wi-Fi®, OPTA Wi-Fi® | Wi-Fi® | Certificate + private key | Yes | Yes |
| UNO R4 Wi-Fi® | Wi-Fi® | Login + secret key | Yes | No |
| Nano ESP32 | Wi-Fi® | Login + secret key | Yes | No |
| Third-party ESP32 | Wi-Fi® | Login + secret key | Yes | No |
| Third-party ESP8266 | Wi-Fi® | Login + secret key | See note | No |
| Ethernet-capable boards (e.g. OPTA, Portenta + shield) | Ethernet | Depends on board | Depends | Depends |
| Cellular boards (e.g. MKR GSM/NB 1500) | GSM / NB-IoT | Certificate + private key | Depends | Yes |
| LoRaWAN® devices | LoRaWAN® (via The Things Stack) | Device EUI / keys | No | N/A |
| UNO Q / Ventuno Q (Linux) | Wi-Fi® (via App Lab) | Managed by App Lab | N/A | N/A |
| Manual / generic clients | Software (Python, MicroPython, JS) | Login + secret key | No | No |

<Alert type="info">

Boards **with a secure element** store a hardware-backed certificate and private key, so no secret key is ever exposed in the sketch. Boards **without one** use the login + secret key method, where the key is stored in `arduino_secrets.h`. See [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).

</Alert>

<Alert type="warning">

Needs verification: the exact OTA support, secure-element presence, and auth method for Ethernet, cellular, and some third-party boards vary by specific model and firmware/core version. Confirm against the current [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) board list and each board's product page before publishing.

</Alert>

## Connectivity Types

| Type | Notes |
|---|---|
| Wi-Fi® | The most common type; official boards support the 2.4 GHz band only (see [Supported Wi-Fi Frequencies](/arduino-cloud/reference/supported-wifi-frequencies)). |
| Ethernet | Wired connectivity for boards/shields that support it. |
| Cellular | GSM / NB-IoT for boards with a modem. |
| LoRaWAN® | Low-power long-range via The Things Stack integration. |

## Next Steps

- [Devices Overview](/arduino-cloud/devices/devices-overview)
- [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets)
- [Supported Wi-Fi Frequencies](/arduino-cloud/reference/supported-wifi-frequencies)

## Trademark Acknowledgments

- **LoRa®** and **LoRaWAN®** are registered trademarks of Semtech Corporation.
- **Wi-Fi®** is a registered trademark of Wi-Fi Alliance.
