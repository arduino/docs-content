---
title: Getting Started with Nano ESP32
description: A step-by-step guide to install the board package needed for the Nano ESP32.
author: Karl Söderby
hardware:
  - hardware/03.nano/boards/nano-esp32
tags: [ESP32, Installation, IDE]
---

To use the [Arduino Nano ESP32](/hardware/nano-esp32) board, you will need to install the Nano ESP32 board package, which is part of the [Arduino ESP32 Core](https://github.com/arduino/arduino-esp32/tree/master).

To install it, you will need the Arduino IDE, which you can download from the [Arduino Software page](https://www.arduino.cc/en/software). In this guide, we will use the latest version of the IDE 2.

## Software & Hardware Needed

- [Arduino Nano ESP32](https://store.arduino.cc/nano-esp32)
- [Arduino IDE](/software/ide-v2)

***You can also use the [Arduino Web Editor](https://create.arduino.cc/editor) which comes with all Arduino boards pre-installed.***

## Download & Install IDE

1. First, we need to download the Arduino IDE, which can be done from the [Arduino Software page](https://www.arduino.cc/en/software/).
2. Install the Arduino IDE on your local machine.
3. Open the Arduino IDE.

![The Arduino IDE.](./assets/open-ide.png)

## Install Board Package

To install the board package, open the "Board Manager" from the menu to the left. Search for Nano ESP32 and install the latest version (or the version you want to use).

![Install Nano ESP32 boards package.](./assets/esp32boards.png)

You should now be able to select your board in the board selector. You will need to have your board connected to your computer via the USB-C® connector at this point.

![Arduino Nano ESP32 board found.](./assets/nanoboarddetected.png)

Congratulations, you have now successfully installed the Nano ESP32 board package via the Arduino IDE.

## Compile & Upload Sketches

To compile and upload sketches, you can use the:
- **Checkmark** for compiling code.
- **Right arrow** to upload code.

There are several examples available for the Nano ESP32 board, which can be accessed directly in the IDE, through **File > Examples**. These examples can be used directly without external libraries.

![Nano ESP32 examples.](./assets/nano-examples.png)

## Summary

In this tutorial, we have installed the Nano ESP32 board package, using the Arduino IDE.

For any issues regarding the Arduino ESP32 board package, please refer to the [arduino-esp32 Core](https://github.com/arduino/arduino-esp32).