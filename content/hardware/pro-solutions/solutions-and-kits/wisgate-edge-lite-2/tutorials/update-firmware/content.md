---
title: 'Update WisGate Edge Gateway Device Firmware'
description: 'Tutorial to update the firmware version of the WisGate Edge gateway device variants'
difficulty: beginner
tags: [Maintenance, Firmware, WisGate]
author: 'Pablo Marquínez'
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/wisgate-edge-lite-2
  - hardware/05.pro-solutions/solutions-and-kits/wisgate-edge-pro
---

## Introduction

This tutorial will show you how to update the firmware of your **WisGate Edge** gateway.

## Goals

The goals of this tutorial are the following:

- Download the latest firmware version for the Wisgate Edge gateway
- Install the latest firmware version on the Wisgate Edge gateway

## Hardware and Software Needed

- [WisGate Edge Pro or WisGate Edge Lite 2](https://store.arduino.cc/pages/wisgate-lora-gateways)

## Requirements

In this tutorial, we assume that you have already connected the gateway to your local network and that you can access it using your preferred method. Please refer to the [Getting Started with WisGate Edge Gateway Devices tutorial](../getting-started/) for detailed guidance.

## Instructions

### Download the Latest Firmware Version

To update your product's firmware, click here to download the [**latest firmware version**](assets/WisGateOS_2.2.2_ARDUINO_RAK.zip). You will receive a ZIP file named `WisGateOS_<version>_ARDUINO_RAK.zip`. Unzip this file to extract the required firmware files.

***The latest version of the WisGate Edge Gateway devices is 2.2.2. Once the device is updated to version 2.2.2 __it is not possible to downgrade the version of the firmware to an older version anymore__, download the release notes [here](assets/Release_Notes_WisGateOS_2.2.2_ARDUINO_RAK.txt) to know more.***

### Connect to the WisGate Dashboard

There are several methods to access the WisGate dashboard (using default values):

* Connecting via the Wi-Fi® Access Point of the device (Dashboard IP: `192.168.230.1`)
* Use an Ethernet cable to connect your computer directly to the gateway (Dashboard IP: `192.168.230.1`)
* Connect the Gateway to your LAN and obtain its DHCP IP address (You will need to discover the device's IP)

![WisGate dashboard](assets/wisgate-dashboard-overview.png)

### Upload the Firmware

On the WisGate Dashboard, open the Settings page and click on the "Firmware" tab.

![WisGate gateway dashboard settings page](assets/wisgate-firmware-settings.png)

Now, drag and drop or open the browse file option to select the firmware file downloaded in the previous step. As you can see in the image below, it is in `.bin.rwi` format.

![WisGate firmware file uploaded to the gateway](assets/wisgate-firmware-update.png)

### Flash the Firmware

With the latest firmware uploaded, now click on the "Update" button. This will flash the new firmware to your gateway.

***Remember to check the box "Keep settings after updating" not to erase your gateway's settings***

![WisGate new firmware flashing process](assets/wisgate-firmware-flashing.png)  

After flashing the new firmware, your gateway will reboot itself, and it may be unavailable for a few minutes.

## Next Steps

Make sure to check periodically to see if your gateway has the latest firmware to avoid bugs and security issues.