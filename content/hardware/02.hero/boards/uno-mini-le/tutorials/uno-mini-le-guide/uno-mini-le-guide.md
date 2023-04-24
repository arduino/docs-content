---
title: 'A Guide to the Arduino UNO Mini Limited Edition'
description: 'Learn how to set up the UNO Mini Limited Edition (LE), a miniature version of the classic UNO board. This guide includes instructions and technical information to get started with your board.'
tags: 
  - UNO Mini LE
  - Limited Edition
author: 'Karl Söderby'
hardware:
  - hardware/01.hero/boards/uno-mini-le
software:
  - arduino-ide
---

![The Arduino UNO Mini LE](assets/Uno_Mini_LE_Top.jpg)

The [Arduino UNO Mini LE](https://store.arduino.cc/uno-mini-le) is a great little board that is very much like its dad: the good ol' UNO. It uses the same microcontroller, **ATmega328P** and the same USB-Serial Processor **ATmega16U2**, but differs in size and some other areas. Some notable differences are:

- The UNO Mini LE has a USB-C® connector
- The female header pins are half the pitch of the original UNO (due to its small size). 
- It does not feature a barrel plug connector for external power supply. Instead, there are two pins available for connecting external power supplies: **VIN** and **GND**. The limit for these pins are 6-21V and should not be exceeded.

In this guide, we will go through some requirements, installation instructions, ideas for projects and some technical specifications. If you want to visit the official documentation for this board, you click on the link below:

- [Official documentation for Arduino UNO Mini LE.](/hardware/uno-mini-le).

## Goals

The goal with this guide is to:
- Set up and test out your UNO Mini LE board.
- Provide you with a technical overview of the board.

## Hardware & Software Needed

- [Arduino UNO Mini LE](https://store.arduino.cc/uno-mini-le)
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software) versions).
- USB-C® cable.

## Setup & Installation

If you need help installing your UNO Mini LE board, you can follow any of the guides below. The board is based on the classic **AVR core**, which means the installation is identical to the [Arduino UNO](https://store.arduino.cc/products/arduino-uno-rev3/) and other classic boards.

### Arduino IDE 1.8.X

The UNO Mini LE can be programmed through the **Classic Arduino IDE 1.8.X**. To install your board, you can check out the guide below:

- [Installing classic AVR boards.](/software/ide-v1/tutorials/getting-started/cores/arduino-avr)

### Arduino IDE 2 

The UNO Mini LE can be programmed through the **Arduino IDE 2**. To install your board, you can check out the guide below:

- [How to use the board manager with the Arduino IDE 2](/software/ide-v2/tutorials/ide-v2-board-manager)

### Web Editor

The UNO Mini LE can be programmed through the **Web Editor**. To get started with your board, you will only need to install a plugin, which is explained in the guide below:

- [Getting started with the Web Editor](/arduino-cloud/getting-started/getting-started-web-editor)

## The Blink Example

To test out your UNO Mini LE board, you can upload & run the **Blink** example. Inside any editor, navigate to:

**File > Examples > 01.Basics > Blink**

The code is also available from the snippet below. Upload the code to your board.

```arduino
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

When the upload is finished, the **built-in LED** will turn on and off every one second. 

<video width="100%" loop autoplay>
<source src="assets/MINI_UNO_LE_Blink.mp4" type="video/mp4" />
</video>

## Technical Specifications

In this section, we will explore some of the technical aspects of the UNO Mini LE, such as pinout, datasheet, schematics and external power sources.

These are also available from the [official documentation for the UNO Mini LE board](/hardware/uno-mini-le).

### Pitch

The pitch (distance between pin holes) is 0.05", or 1.27 mm. This is half the distance compared to the classic, regular sized UNO (0.1", 2.54 mm).

### Dimension

- Width: **26.70 mm**
- Length: **34.20 mm**

### Pinout

![Arduino UNO Mini LE Pinout](assets/ABX00062-pinout.png)

***If you want a more detailed pinout, please refer to the [UNO Mini LE Resources](/hardware/uno-mini-le#resources) section in the documentation.***

### Datasheet

The UNO Mini LE has an in-depth datasheet that covers all of the technical aspects of the board. You can download from the resources section in the [UNO Mini LE's documentation page](/hardware/uno-mini-le#resources).

### Schematics

The schematics for this board is available through an interactive viewer in the [resources section](/hardware/uno-mini-le#resources) of the UNO Mini LE's documentation page.

### External Power

Unlike the classic UNO, the UNO Mini LE does not have a barrel jack plug. Although there are two pins dedicated for external power sources, such as batteries. Look for the **VIN** and **GND** pins at the corner of the board, and connect your power source (+ to VIN, - to GND).

![Connecting a battery to the UNO Mini LE](assets/UNO-Mini-LE-external-power.png)

***Please not that the recommended range is 6-21 volts. Anything outside that range can damage your board.***

