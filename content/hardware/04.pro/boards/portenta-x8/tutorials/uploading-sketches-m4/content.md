---
title: 'Upload sketches to Portenta X8'
description: 'This tutorial will show how to upload Arduino sketches on the M4 processor'
difficulty: medium
beta: true
tags:
  - Bootloader
  - Firmware
  - Core
author: 'Pablo Marquínez'
hardware:
  - hardware/04.pro/boards/portenta-x8
software:
  - ide-v1
  - ide-v2
  - cli
---

## Overview
This tutorial will explain how to upload a standard Arduino sketch to your portenta X8's M4.

## Goals
- Use the Arduino IDE to compile and upload.
- Compile the sketch binaries with the Arduino IDE and upload it through ADB.

### Required Hardware and Software
- Portenta X8
- USB C cable (either USB A to USB C or USB C to USB C)
- Arduino IDE 1.8.10+ or Arduino-cli
- arduino-mbed portenta Core up to date (greater than 3.0.1)

## Instructions

### Standard Arduino IDE upload
Open the Arduino IDE, make sure you have selected the Portenta X8 on the boards selector.

![IDE board selector](assets/x8-board-manager.png)

Create your sketch, for example the blink sketch:
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

Once your sketch it's completed, select the port of your device.

Press the Compile and Upload button.

To finalize, when you see that the sketch has bee uploaded successfully, check that every second you are getting the LED changing from OFF to ON.

### Upload using ADB

To use ADB, it gets installed at `Arduino15\packages\arduino\tools\adb\32.0.0`.

From that directory you can use the `adb` tool. To upload your compiled sketch you just need to type:
```
adb push <sketchBinaryPath> /tmp/arduino/m4-user-sketch.elf
```

![ADB upload with a terminal](assets/x8-terminal-ADB-push.png)

## Conclusion
You now have access to the M4 processor, so for example you are able to connect an I<sup>2</sup>C sensor and interact with it and the Arduino X8 Linux side.

## Troubleshooting

### ADB folder empty

If you cannot use the `ADB` tool and the folder `Arduino15\packages\arduino\tools\adb\32.0.0` is empty Remove the Mbed Portenta Core and install it again.