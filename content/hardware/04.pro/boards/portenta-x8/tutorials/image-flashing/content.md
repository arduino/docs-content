---
beta: true
title: 'How to flash your Portenta X8'
description: 'This tutorial teaches you how to flash your Portenta X8 through USB'
difficulty: intermediate
tags:
  - Embedded Linux
  - Flashing
  - Foundries
author: 'Pablo Marquínez'
hardware:
  - hardware/04.pro/boards/portenta-x8
software:
  - Terminal
---

## Overview

In this tutorial you will see how to manually flash your Portenta X8 with the image that is provided by foundries through USB using the Terminal.

## Goals

- Get the needed files
- Set up the correct structure of the files
- Set up the board
- Flash the device

### Required Hardware and Software

- USB-C to USB-A or USB-C to USB-C
- Portenta X8
- Portenta Breakout Board <!-- or Portenta Max Carrier-->
- Arduino Create account
- Arduino Create Pro subscription
- Foundries account (linked with the Pro plan)
- Foundries factory (Check the Getting Started tutorial)
- 1 Device already attatched to your factory (Check the Getting Started tutorial)
    
## Instructions

### Get the needed files

Needed files following this structure:

- Root folder
  - imx-boot
  - imx-boot-portenta-x8
  - sit-portenta-x8.bin
  - u-boot-portenta-x8.itb
  - mfgtool-files-portenta-x8.tar (Unzipped)
  - lmp-partner-arduino-image-portenta-x8.wic.gz (Unzipped)

To get those files open your Foundries factory.

Switch to the targets tab.

Click on the platform-master version.

On the "Runs" section open those collapsed labels, and download the files listed above.

After downloading them, make sure you put them in a folder following the structure shown.

### Set up the Portenta X8 into flashing mode

Plug you Porenta X8 in your carrier (Portenta Breakout carrier <!-- or Portenta Max Carrier-->).

Switch both DIP switches into the ON position.

Plug the USB-C on the Portenta X8 and the other end (USB-C or USB-A) to your computer.

You will see a new device connected called `SE Blank M845S`.

### Flash the device

Open a terminal and change the directory (`cd`) to your root folder as shown on the beginning.

Introduce ´uuu full_image.uuu´

Wait until it gets flashed.

Switch back the DIP switches to OFF position.

Unplug and plug again the Portenta X8 to your computer.

***After flashing you will need to wait 10 secs, until the Portenta X8 blue LED start blinking, that means the boot was successful***

## Troubleshooting

- If you get an error while its flashing, make sure your USB is correctly plugged. Re-plug your board and try to flash again, you may need few tries before it gets a success flashing.
