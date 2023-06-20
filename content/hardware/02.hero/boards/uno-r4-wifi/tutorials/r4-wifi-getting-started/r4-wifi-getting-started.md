---
title: Getting Started with UNO R4 WiFi
description: A step-by-step guide to install the board package needed for the UNO R4 WiFi board.
author: Hannes Siebeneicher
tags: [UNO R4 WiFi, Installation, IDE]
---

To use the [Arduino UNO R4 WiFi](/hardware/uno-r4-wifi) board, you will need to install the UNO R4 WiFi board package, which is part of the [Arduino Core for renesas devices](https://github.com/arduino/ArduinoCore-renesas).

To install it, you will need the Arduino IDE, which you can download from the [Arduino Software page](https://www.arduino.cc/en/software). In this guide, we will use the latest version of the IDE 2.

## Software & Hardware Needed

- [Arduino UNO R4 WiFi](https://store.arduino.cc/products/arduino-uno-r4-wifi)
- [Arduino IDE](/software/ide-v2)

***You can also use the [Web Editor](https://create.arduino.cc/editor) which comes with all Arduino boards pre-installed.*** 

## Download & Install IDE

1. First, we need to download the Arduino IDE, which can be done from the [Arduino Software page](https://www.arduino.cc/en/software/).
2. Install the Arduino IDE on your local machine.
3. Open the Arduino IDE.

![The Arduino IDE.](assets/open-ide.png)

## Install Board Package

To install the board package, open the "Board Manager" from the menu to the left. Search for UNO R4 WiFi and install the latest version (or the version you want to use).

![Install UNO R4 WiFi boards package.](assets/install-wifi-core.png)

You should now be able to select your board in the board selector. You will need to have your board connected to your computer via the USB-C® connector at this point.

![Arduino UNO R4 WiFi board found.](assets/wifi-connected.png)

Congratulations, you have now successfully installed the UNO R4 WiFi board package via the Arduino IDE.

## Compile & Upload Sketches

To compile and upload sketches, you can use the:
- **Checkmark** for compiling code.
- **Right arrow** to upload code.

There are several examples available for the UNO R4 WiFi board, which can be accessed directly in the IDE, through **File > Examples**. These examples can be used directly without external libraries.

![UNO R4 WiFi examples.](assets/wifi-examples.png)

## Summary

In this tutorial, we have installed the UNO R4 WiFi board package, using the Arduino IDE.

For any issues regarding the UNO R4 WiFi board package, please refer to the [Arduino Core for Renesas devices](https://github.com/arduino/ArduinoCore-renesas).