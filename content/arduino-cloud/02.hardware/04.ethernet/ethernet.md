---
title: Ethernet
description: Learn how to configure an Ethernet device in the Arduino Cloud.
tags: [Ethernet, Arduino Cloud, IoT]
author: Karl Söderby
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/shields/portenta-vision-shield
  - hardware/05.pro-solutions/solutions-and-kits/portenta-machine-control
  - hardware/07.opta/opta-family/opta
---

The Arduino Cloud supports connection via Ethernet on a number of devices. 

## Supported Boards

The options to connect via Ethernet are the following:
- Connect with the [Portenta H7](https://store.arduino.cc/products/portenta-h7) in combination with an Ethernet-compatible carrier/shield (see below).
- Connect with the [Opta](https://store.arduino.cc/products/opta-wifi).

To connect with the **Portenta H7** board, you will need one of the following shields/carriers:
- [Portenta Vision Shield Ethernet](https://store.arduino.cc/products/arduino-portenta-vision-shield-ethernet)
- [Portenta Machine Control](https://store.arduino.cc/portenta-machine-control)

***Please note that older hardware such as the [Ethernet Shield Rev2](https://store.arduino.cc/products/arduino-ethernet-shield-2) and [MKR ETH Shield](https://store.arduino.cc/products/arduino-mkr-eth-shield) are currently not supported by the Arduino Cloud.***

## Setup

To configure Ethernet board, follow the steps below:

**1.** Connect your board to your computer.

**2.** Go to [Arduino Cloud](https://app.arduino.cc), and navigate to the **"Devices"** section. Click on the **"Add Device"** button and then select the **"Arduino Board"**. After a while, your board will be visible, and you can click on the **"Configure"** button.

![Board show up.](assets/eth.png)

**3.** If you selected an Ethernet compatible board, you will receive an option to choose from **Wi-Fi® / Ethernet**. Choose Ethernet.

![Choose the Ethernet option.](assets/ethernet-option.png)

**4.** Allow some time for the configuration, as a sketch is being uploaded to your board and your crypto chip is configured.

Your board is now configured and ready to be used in the Arduino Cloud. 

To get started, check out the official [Getting Started (Arduino / C++)](/arduino-cloud/guides/arduino-c) guide. This will guide you to successfully send data between your board and Arduino Cloud.