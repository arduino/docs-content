---
title: 'Uploading Sketches to the M4 Core on Arduino Portenta X8'
description: 'This tutorial explains how to upload Arduino sketches to the M4 core.'
difficulty: intermediate
tags:
  - firmware
  - M4
author: 'Pablo Marquínez'
hardware:
  - hardware/04.pro/boards/portenta-x8
software:
  - ide-v1
  - ide-v2
  - cli
---

## Overview
In this tutorial we will go through the process of uploading sketches to the M4 core on the STM32H747XI MCU. For the user the process is the same as usual but it differs quite a bit in regards to what happens behind the scenes compared to other Arduino boards.

## Goals
- Learn how to use the Arduino IDE to compile and upload a sketch.
- Learn how to compile the sketch binaries with the Arduino IDE and upload it manually via ADB.

### Required Hardware and Software
- [Portenta X8](https://store.arduino.cc/products/portenta-x8)
- USB C cable (either USB A to USB C or USB C to USB C)
- Arduino IDE 1.8.10+ or Arduino-cli
- Latest "Arduino Mbed OS Portenta Boards" Core > 3.0.1

## Instructions

### Standard Arduino IDE Upload
Open the Arduino IDE, make sure you have selected the Portenta X8 in the boards selector.

![IDE board selector](assets/x8-board-manager.png)

Create a custom sketch or open one of the example sketches e.g. the blink sketch:
```arduino
void setup(){
  pinMode(LED_BUILTIN ,OUTPUT);
}

void loop(){
  digitalWrite(LED_BUILTIN , HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN , LOW);
  delay(1000);
}
```

- Select the port of your device in the port selector menu.
- Press the Compile and Upload button.

Behind the curtains, the sketch gets compiled into a binary. That binary file is then uploaded to the Linux side of the Portenta X8 via an `adb` SSH connection. The flashing itself is done on the board itself by a service running on Linux. When the sketch has bee uploaded successfully, check if the onboard LED is blinking at an interval of one second.

### Upload Manually Using ADB

To upload a firmware manually, you first need to compile the sketch. In the Arduino IDE select "Export compiled binary" from the Sketch menu. It will compile the sketch and save the binary file in the sketch folder. Alternatively you can use the [Arduino CLI](https://arduino.github.io/arduino-cli/) to create an elf file.

To upload the firmware you can use the ADB tool that has been installed as part of the Portenta X8 core. It can be found at `Arduino15\packages\arduino\tools\adb\32.0.0`.

From that directory you can use the `adb` tool. To upload your compiled sketch you just need to type:
```
adb push <sketchBinaryPath> /tmp/arduino/m4-user-sketch.elf
```

![ADB upload with a terminal](assets/x8-terminal-ADB-push.png)

## How It Works?
The Portenta X8 has a service that waits for a sketch to be uploaded to a folder. If it detects changes the device will flash the M4 with the uploaded firmware.

This work thanks to the following services:
* **monitor-m4-elf-file.service**: this service monitors the directory `/tmp/arduino/m4-user-sketch.elf` and each time it detects a new file it will proceed to flash the M4 using  `openOCD` with the sketch that has been pushed.

## Conclusion
In this tutorial you have learned how to upload a sketch to the M4 core. Now for example you are able to connect an I<sup>2</sup>C sensor and interact with it. 

## Troubleshooting

- If you cannot use the `ADB` tool and the folder `Arduino15\packages\arduino\tools\adb\32.0.0` is empty Remove the Mbed Portenta Core and install it again.