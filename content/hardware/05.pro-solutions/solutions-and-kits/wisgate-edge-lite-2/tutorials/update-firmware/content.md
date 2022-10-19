---
title: 'Update WisGate Edge Gateway Firmware'
description: 'Tutorial to update the firmware version of the WisGate Edge Gateway'
difficulty: beginner
tags: [Maintenance, Firmware, WisGate]
author: 'Pablo Marquínez'
hardware:
  - hardware/05.pro-solutions/wisgate-edge-lite-2
  - hardware/05.pro-solutions/wisgate-edge-pro
---

## Introduction 

This tutorial will show you how to update the firmware of your **WisGate Edge** gateway.

## Goals

The goals of this article are:

- Download the latest Firmware version.
- Connect to the Gateway
- Open the dashboard panel
- Upload the new version

## Hardware & Software Needed

- [WisGate Edge Pro or WisGate Edge Lite 2](https://store.arduino.cc/pages/wisgate-lora-gateways)

## Requirements

We assume that you already connected the gateway to your local network, and you can connect to it using your favourite method.   

You can check out the needed steps on the [Getting Started tutorial](/getting-started).

## Instructions

### Download the Latest Firmware Version

Go to your gateway's [Arduino Docs Product Page](../../product) go to the Essentials section and click the button with the Latest Firmware Version.

![Product Page Essentials section](assets/wisgate-essentials.png)

You will get a zip file called `WisGateOS_<version>_ARDUINO_RAK.zip`

Unzip it and you will have the firmware files.

### Connect to the WisGate Dashboard

There are different ways to access the WisGate (default values):
* Connecting to its Wi-Fi Access Point (dashboard IP: `192.168.230.1`)
* Ethernet cable from your Computer to the Gateway (dashboard IP: `192.168.230.1`)
* Connecting your Gateway to your LAN, getting its DHCP IP (You will need to discover the device's IP)

![WisGate dashboard](assets/wisgate-dashboard-overview.png)

### Upload the Firmware

Open the Settings page and click on the "Firmware" tab.

![WisGate dashboard Settings page](assets/wisgate-firmware-settings.png)

Now drag and drop or open the browse file option to select the firmware file downloaded previously with the format end `.bin.rwi` as you can see on the screenshot we uploaded the file called `WisGateOS_2.0.1_ARDUINO_b30_RAK636.bin.rwi`

![WisGate firmware zip uploaded](assets/wisgate-firmware-update.png)

### Flash the Firmware

Click update and you will flash the gateway with the new version.

***To not erase the settings remember to check the box "Keep settings after updating"***

![WisGate firmware flashing](assets/wisgate-firmware-flashing.png)

After flashing the gateway will reboot itself, it may be for some minutes unavailable.

## Next Step

Make sure to check periodically if your device is up-to-date to avoid bugs and security issues.