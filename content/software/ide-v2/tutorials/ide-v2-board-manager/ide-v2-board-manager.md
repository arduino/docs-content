---
title: 'Getting Started - Core Installation'
difficulty: beginner
description: 'Learn how the new board manager tool works, and how to easily install the boards you want to use in the Arduino IDE 2.'
tags:
 - Installation
 - Tools
author: 'Karl Söderby & Jacob Hylén'
---

The board manager is a great tool for installing the necessary cores to use your Arduino boards. In this quick tutorial, we will take a look at how to install one, and choosing the right core for your board! 

You can easily download the editor from the [Arduino Software page](https://www.arduino.cc/en/software). 

You can also follow the [downloading and installing the Arduino IDE 2](/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing) tutorial for more detailed guide on how to install the editor.

## Requirements

- Arduino IDE 2 installed. 

## Why Use the Board Manager?

The board manager is a tool that is used to install different cores on your local computer. So what is a **core**, and why is it necessary that I install one?

Simply explained, a core is written and designed for specific microcontrollers. Arduino offers several different types of boards, and these boards may also have different types of microcontrollers. While different microcontrollers accomplish tasks in similar ways, the way code is compiled, pins are mapped, and what features are available is tailor-made to the silicon itself, meaning that this will also be microcontroller-specific. 

What a core does is to act as a layer between all of this microcontroller-specific jargon, and you - the maker. The core translates it into the Arduino API you are already familiar with so that you can program any of the microcontrollers in the Arduino ecosystem in the same way.

For example, an Arduino UNO has an **ATmega328P**, which uses the **AVR core**, while an Arduino Nano 33 IoT has a **SAMD21** microcontroller, where we need to use the **SAMD core**. However, regardless of what microcontroller is on the board we are using, `digitalWrite(LED_BUILTIN, HIGH)` will turn on the built-in LED, and `analogRead(A0)` will read the analog pin 0 and check for a voltage.

In conclusion, to use a specific board, we need to install a specific core. 


## What Core Should I Install?

Do you have an Arduino board in your hands, but are not sure what core you need to install? When you plug a board in to your computer, and you don't have the appropriate core installed, the IDE should automatically prompt you to install it. But, in case you need it anyways, you can find a list of boards and the core packages they belong to below:

### AVR
- [UNO R3](/hardware/uno-rev3)
- [UNO R3 SMD](/hardware/uno-rev3-smd)
- [UNO Mini Limited Edition](/hardware/uno-mini-le)
- [Leonardo](/hardware/leonardo)
- [Micro](/hardware/micro)
- [Nano](/hardware/nano)
- [Mega 2560](/hardware/mega-2560)

The AVR core comes pre-installed when you download the Arduino IDE, so if you have one of these boards - Great! You're already done and won't need to install it yourself. You can, however, still find it in the board manager if you want to change what version of the core you have installed. 

### MegaAVR
- [UNO WiFi Rev2](/hardware/uno-wifi-rev2)
- [Nano Every](/hardware/nano-every)

To install the **MegaAVR** core, follow the [steps detailed below](#installing-a-core), but search for "**MegaAVR**".

### UNO R4 
- [UNO R4 Minima](/hardware/uno-r4-minima)
- [UNO R4 WiFi](/hardware/uno-r4-wifi)

To install the **UNO R4** core, follow the [steps detailed below](#installing-a-core), but search for "**UNO R4**".

### SAM
- [Due](/hardware/due)

To install the **SAM** core, follow the [steps detailed below](#installing-a-core), but search for "**SAM**".

### SAMD
- [Zero](/hardware/zero)
- [Nano 33 IoT](/hardware/nano-33-iot)
- [MKR 1000 WiFi](/hardware/mkr-1000-wifi)
- [MKR Zero](/hardware/mkr-zero)
- [MKR WiFi 1010](/hardware/mkr-wifi-1010)
- [MKR FOX 1200](/hardware/mkr-fox-1200)
- [MKR WAN 1300](/hardware/mkr-wan1300)
- [MKR WAN 1310](/hardware/mkr-wan1310)
- [MKR GSM 1400](/hardware/mkr-gsm-1400)
- [MKR NB 1500](/hardware/mkr-nb-1500)
- [MKR Vidor 4000](/hardware/mkr-vidor-4000)

To install the **SAMD** core, follow the [steps detailed below](#installing-a-core), but search for "**SAMD**".

### Mbed OS GIGA 
- [GIGA R1 WiFi](/hardware/giga-r1-wifi)

To install the **Mbed OS GIGA** core, follow the [steps detailed below](#installing-a-core), but search for "**Mbed OS GIGA**".

### Mbed OS Nano
- [Nano RP2040 Connect](/hardware/nano-rp2040-connect)
- [Nano 33 BLE](/hardware/nano-33-ble)
- [Nano 33 BLE Sense](/hardware/nano-33-ble-sense)
- [Nano 33 BLE Sense Rev2](/hardware/nano-33-ble-sense-rev2)

To install the **Mbed OS Nano** core, follow the [steps detailed below](#installing-a-core), but search for "**Mbed OS Nano**".

### Mbed OS Portenta
- [Portenta H7](/hardware/portenta-h7)
- [Portenta H7-lite](/hardware/portenta-h7-lite)
- [Portenta H7-lite-connected](/hardware/portenta-h7-lite-connected)
- [Portenta X8](/hardware/portenta-x8)

To install the **Mbed OS Portenta** core, follow the [steps detailed below](#installing-a-core), but search for "**Mbed OS Portenta**".

### Mbed OS Nicla
- [Nicla Sense ME](/hardware/nicla-sense-me)
- [Nicla Vision](/hardware/nicla-vision)
- [Nicla Voice](/hardware/nicla-voice)

To install the **Mbed OS Nicla** core, follow the [steps detailed below](#installing-a-core), but search for "**Mbed OS Nicla**".

### Mbed OS Edge boards
- [Edge Control](/hardware/edge-control)

To install the **Mbed OS Edge** core, follow the [steps detailed below](#installing-a-core), but search for "**Mbed OS Edge**".

### Renesas Portenta
- [Portenta C33](/hardware/portenta-c33)

To install the **Renesas Portenta** core, follow the [steps detailed below](#installing-a-core), but search for "**Renesas Portenta**".

### ESP32
- [Nano ESP32](/hardware/nano-esp32)

To install the **ESP32** core, follow the [steps detailed below](#installing-a-core), but search for "**ESP32**".

## Installing a Core

Installing a core is quick and easy, but let's take a look at what we need to do. 

**1.** Open the Arduino IDE 2. 

**2.** With the editor open, let's take a look at the left column. Here, we can see a couple of icons. Let's click the on the **Arduino board** icon.

![The board manager.](assets/installing-a-core-img01.png)

**3.** A list will now appear of all available cores. Now let's say we are using an **Nano 33 BLE** board, and we want to install the core. Simply enter the name in the search field, and the right core (Mbed OS Nano) will appear, where the Nano 33 BLE features in the description. Click on the **"INSTALL"** button.

![Navigating the board manager.](assets/installing-a-core-img02.png)

**4.** This will begin an installation process, which usually only take a few moments. 

![Installation may take a few minutes.](assets/installing-a-core-img03.png)

**5.** When it is finished, we can take a look at the core in the boards manager column, where it should say **"INSTALLED"**, as well as noting which version you have installed on your machine.

![Board is installed.](assets/installing-a-core-img04.png)

Congratulations! You have now successfully downloaded and installed a core on your machine, and you can start using your Arduino board! 

### More Tutorials

You can find more tutorials in the [Arduino IDE 2 documentation page](/software/ide-v2/).