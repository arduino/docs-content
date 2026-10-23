---
title: Devices Overview
description: Device types in Arduino Cloud, the Device ID and Secret Key, and how to add a device from the Devices page.
tags: [Arduino Cloud, Devices]
author: Karl Söderby & Arduino Team
---

A **device** is the physical (or virtual) hardware that runs your code and talks to Arduino Cloud. You manage every device from **Devices** in the left navigation (`/devices`), where each one is listed with its name, status, and linked Things.

## Device Identity: ID and Secret Key

When a device is registered, Arduino Cloud generates two credentials that uniquely identify it:

- **Device ID** — the device's unique identifier, safe to reference in code and dashboards.
- **Secret Key** — a private key shown only once at creation. Store it somewhere safe; it can't be retrieved later, only regenerated.

![The Device ID and Secret Key generated for a device.](assets/device-key.png)

Boards with a secure element (such as the MKR family, Nano 33 IoT, or Portenta) instead store a hardware-backed certificate and private key, so no secret key is exposed in the sketch. Boards without a secure element (UNO R4 Wi-Fi®, Nano ESP32, ESP32/ESP8266) and manual clients use the login + secret key method.

## Device Types

| Type | Connectivity | Setup path |
|---|---|---|
| Official Arduino (Wi-Fi®) | Wi-Fi® | [Add a Wi-Fi Board](/arduino-cloud/devices/add-wifi-board) |
| Official Arduino (Ethernet) | Wired | [Add an Ethernet Board](/arduino-cloud/devices/add-ethernet-board) |
| Official Arduino (Cellular) | GSM / NB-IoT | [Add a Cellular Board](/arduino-cloud/devices/add-cellular-board) |
| Official Arduino (LoRaWAN®) | LoRaWAN® | [Add a LoRaWAN Device](/arduino-cloud/devices/add-lorawan-device) |
| Third-party (ESP32 / ESP8266) | Wi-Fi® | [Add an ESP32/ESP8266](/arduino-cloud/devices/add-esp32-esp8266) |
| UNO Q / Ventuno Q (Linux) | Wi-Fi® (via App Lab) | [Add an UNO Q](/arduino-cloud/devices/add-uno-q) |
| Manual / generic | Software client | [Add a Manual Device](/arduino-cloud/devices/add-manual-device) |

## Adding a Device

Select **+ Device** (or **ADD DEVICE**) to open the **Setup Device** dialog, split into two paths:

![Choosing a device type in the Setup Device dialog.](assets/device-type.png)

| Path | For |
|---|---|
| **Automatic Setup** | Arduino boards and compatible ESP32/ESP8266/LoRaWAN® boards, provisioned through a guided wizard |
| **Manual Setup** | Any device — generates credentials for a [generic/virtual device](/arduino-cloud/devices/add-manual-device) with no sketch |

For scriptable, repeatable provisioning, [arduino-cloud-cli](/arduino-cloud/apis-cli/cli-devices) is a fully equivalent alternative to the web wizard.

## The Device Page

Selecting a device opens its detail page, where you can rename it, view its ID, type, FQBN, and firmware version, see its connection history, attach it to a [Thing](/arduino-cloud/things-data/things), and revisit its [network configuration](/arduino-cloud/devices/network-configuration).

<Alert type="info">

A device must be associated with a Thing before it can exchange Cloud Variables. See [Things & Data](/arduino-cloud/things-data/things).

</Alert>

## Next Steps

- [Add a Wi-Fi Board](/arduino-cloud/devices/add-wifi-board)
- [Network Configuration](/arduino-cloud/devices/network-configuration)
- [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle)
