---
beta: true
title: '09. How To Flash Your Portenta X8'
description: 'This tutorial teaches you how to flash your Portenta X8 through USB.'
difficulty: intermediate
tags:
  - Embedded Linux
  - Flashing
author: 'Pablo Marquínez'
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

In this tutorial, you will learn how to manually flash your Portenta X8 with the image provided by Arduino. You will flash your board through USB using the Terminal. The instructions below are meant to be used with a **Windows Operating System**.

***We encourage you to check now and then if the device image version is up-to-date to have the latest bootloader. Please check the release section of the [lmp-manifest repository](https://github.com/arduino/lmp-manifest/releases) and compare the target version number***

## Goals

- Learn how to get the required files
- Learn how to set up the correct structure of the files
- Learn how to set up the board
- Learn how to flash the device

### Required Hardware and Software

- [Arduino Portenta X8](https://store.arduino.cc/products/portenta-x8)
- [Portenta Breakout Board](https://store.arduino.cc/products/arduino-portenta-breakout) or [Arduino Portenta Max Carrier](https://store.arduino.cc/products/portenta-max-carrier)
- USB-C® cable (either USB-C® to USB-A or USB-C® to USB-C®)
    
## Instructions

### Getting Latest Portenta X8 Image

The `lmp-manifest` [GitHub repository](https://github.com/arduino/lmp-manifest) contains releases of the official Arduino Linux microPlatform Manifests. We will head to the [releases](https://github.com/arduino/lmp-manifest/releases) section to acquire the required files. The files are compressed in tarball format (`.tar.gz`).

At the time of this tutorial writing, the available version was `456`. If you encounter newer versions, please use the latest version to have the Portenta X8 up to date. We will proceed to download `456.tar.gz` which is the current latest version.

![lpm-manifest repository overview](assets/lpm-manifest-overview.png)

Please extract the files after you have downloaded the compressed file. The extracted contents have the following structure.

```
Unzipped folder
├── imx-boot-portenta-x8
├── lmp-partner-arduino-image-portenta-x8.wic.gz **(Compressed)**
├── mfgtool-files-portenta-x8.tar.gz **(Compressed)**
├── sit-portenta-x8.bin
└── u-boot-portenta-x8.itb
```

After verifying these files are available, you will need to decompress `mfgtool-files-portenta-x8.tar.gz` and `lmp-partner-arduino-image-portenta-x8.wic.gz`. Please make sure the `.wic` is in the unzipped folder in the main directory. The folder structure should share a similar following layout.

```
Unzipped folder
├── mfgtool-files-portenta-x8/
├── imx-boot-portenta-x8
├── lmp-partner-arduino-image-portenta-x8.wic
├── lmp-partner-arduino-image-portenta-x8.wic.gz **(Compressed)**
├── mfgtool-files-portenta-x8.tar.gz **(Compressed)**
├── sit-portenta-x8.bin
└── u-boot-portenta-x8.itb
```

### Setting the Portenta X8 to Flashing Mode

Connect your Portenta X8 into your carrier of choice, either *Portenta Breakout* or *Portenta Max Carrier*, via High-Density connectors. After connecting the Portenta X8, you will need to set the `BOOT` DIP switches to the ON position. The `BOOT` switch configuration is important as it will put the board into Flashing mode.

On the Portenta Max Carrier, the DIP switches are identified by the label `BOOT SEL` and `BOOT` as shown in the figure:

![Max Carrier DIP switches](assets/max-carrier-dip-switches.png)

On the Portenta Breakout, the DIP switches are identified by the label `BT_SEL` and `BOOT` as shown in the figure:

![Breakout DIP switches](assets/breakout-dip-switches.png)

You will need to connect one USB-C® end to the Portenta X8 and the other end (USB-C® or USB-A) to your computer. If the connection is established correctly, you will be able to see a newly connected device called `SE Blank M845S`.

### Flashing the Portenta X8

To flash the Portenta X8, you need to begin by opening a terminal. Within the terminal, you need to change the directory to where `mfgtool-files-portenta-x8` file is located using the `cd` command. Once it is inside the directory where the previous file is included, the following command is used:

```
uuu full_image.uuu
```

When the flashing operation is finished, you should see a similar result as the following figure:

![uuu tool flashing success output](assets/uuu-flashing-success.png)

Once you have verified it has successfully flashed the Portenta X8, the `BOOT` DIP switches that have been configured to the ON position, now need to be set to the OFF position. Otherwise, you will always have the Portenta X8 in Flashing mode whenever it is attached to a carrier. Recycle the power for Portenta X8 by reconnecting the board to your computer and start using with the latest updates.

***After booting, you will need to wait 10 seconds until the Portenta X8 starts blinking Blue LED. The Blue LED indicates it was able to boot successfully.***

## Conclusion

In this tutorial, you have learned to flash the Portenta X8 by getting the latest image, setting up the adequate file structure and the board, and finally flashing the board with these files.

## Troubleshooting

- If you get an error while it is flashing, make sure your USB is correctly plugged in. Reconnect your board and try to flash it again. You may need to go through a few trials before successful flashing.
- If you get an error related to permissions, try to launch the `uuu` command as Super User (`sudo`).
