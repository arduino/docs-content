---
title: Getting Started with the Portenta Max Carrier
description: This tutorial give you an overview of the core features of the Portenta Max Carrier. 
difficulty: Beginner 
tags:
  - Portenta Max Carrier
  - Getting Started
author: José Bagur, Taddy Chung
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/carriers/portenta-max-carrier
software:
  - ide-v1
  - ide-v2
---

## Overview

The Arduino® Portenta Max Carrier provides developers an unlimited range of applications, from robotics and medical devices to industrial or automotive applications; the Portenta Max Carrier possibilities are endless. The Portenta Max Carrier can be used as a single-board computer (SBC) or reference design. It couples the Arduino® Portenta H7 board as a central high-performance unit, granting Edge AI and cutting edge connectivity features into an industry-standard embedded Next Unit of Computing (eNUC) form factor ready. In this tutorial, you will know the core features of the Portenta Max Carrier and how to get started with it.

## Goals 

- Describe the core features of the Portenta Max Carrier.	
- Describe the power sources of the Portenta Max Carrier. 
- Describe the relevant peripherals, headers, and connectors of the Portenta Max Carrier.

## Required Hardware and Software

- [Arduino® Portenta H7](https://store.arduino.cc/products/portenta-h7).
- Arduino® Portenta Max Carrier.
- USB-C cable (either USB-A to USB-C or USB-C to USB-C).
- LoRa® antenna (868-915MHz) with SMA connector.
- LTE antenna (698-960/1710-2690MHz) with SMA connector. 
- 3.7V 2600mAh 18650 Li-Ion battery.
- DC 4.5-20V power supply with barrel jack. 
- [Arduino IDE 2.0](https://www.arduino.cc/en/software). 

## Instructions 

### 1. Get to Know the Portenta Max Carrier

The Portenta Max Carrier was designed to augment the capabilities of the Arduino® Portenta H7 board and provide easy access to its onboard peripherals. It is designed to enable research and develop industrial grade advanced applications, from fast prototyping to deployable robust single board computer. The Portenta Max Carrier establishes connection with Portenta H7 via High Density connectors. This interface grants access to extensive modules and peripherals on-board Portenta Max Carrier.

In the image below, you can see Portenta's Max Carrier main features highlighted: 

In this tutorial, we will describe the following features of the Portenta Max Carrier:

- Power distribution.
- Connectors.
- Onboard memory units.
- Wireless connectivity. 
- Audio interfaces.
- Onboard debugger.

Let us talk more about those features.

#### 1.1. Power Distribution

The Arduino® Portenta Max Carrier provides several peripherals and modules to cover wide spectrum of applications. For this peripherals and modules to be powered up and running, Arduino® Portenta Max Carrier bases on a sophisticated electric power distribution architecture. To power the Portenta Max Carrier, you can use the **barrel jack** connector (X1) or a **3.7V 18650 Li-Ion battery** connected to the Portenta's Max Carrier battery clips (J16 and J18). You can also power the Portenta Max Carrier directly from the USB-C connector of the Portenta H7 board.

You can see the detailed Portenta's Max Carrier power tree in the image below:

These power feed line options powers up different peripherals and modules depending on the line configuration. The Portenta H7 powered by USB-C cable while attached to Portenta Max Carrier enables Audio, LoRa, USB Hub, SD ports, Camera, and Fieldbus including the Debugger; while it is possible to upload the Code. This power line use case will be useful to develop and debug the code.

**If the Arduino IDE throws an error failing to upload the Code, please check the Portenta H7 is in Bootloader Mode**

The external power supply goes through [**MPM3550EGLE**](https://www.mouser.com/datasheet/2/277/MPS_05172019_MPM3550E_r1.0-1595120.pdf), which is a DC/DC power module, to provide +5V to power up the peripherals and the modules. The module provides the power to [**BQ24195RGET**](https://www.ti.com/lit/ds/symlink/bq24195.pdf?HQS=dis-mous-null-mousermode-dsf-pf-null-wwe&ts=1647034752895&ref_url=https%253A%252F%252Fwww.mouser.com%252F), which is a battery charge and power path management, and it is used in Portenta Max Carrier for the Li-Ion battery source and to boost the voltage to +5V. The battery charger IC feeds the power to Modem above all the peripherals and modules mentioned previously. The external power supply has the highest priority in power line. 

A Micro USB port is available for the use on the Arduino® Portenta Max Carrier for debugging capability. The debugging module is a separate segment, and it is powered by Micro USB port using its own power supply [**AP2112K**](https://www.diodes.com/assets/Datasheets/AP2112.pdf), which is a low-dropout linear regulator. The debugger is available for use without the Portenta H7 paired to the Portenta Max Carrier. 

#### 1.2. Connectors

#### 1.3. Onboard Memory Units

The Portenta Max Carrier equips two different memory units on-board: Flash Memory and Mini SD Card slot.

- Flash Memory on-board the Portenta Max Carrier has 2MB of storage via QSPI (Quad Serial Peripheral Interface).
- Mini SD Card slot grants the possibility to extend the storage size. It can be used to process hefty amount of log data, which can be from sensors or programmed on-board computer registry. 

IP

#### 1.4. Wireless Connectivity

#### LoRaWAN® Module - Murata CMWX1ZZABZ-078
One of the notable features of Portenta Max Carrier is the Murata [CMWX1ZZABZ-078](https://www.murata.com/products/connectivitymodule/lpwa/overview/lineup/type-abz-078) that enables LoRaWAN® connectivity. LoRaWAN® is a Low Power Wide Area Network (LPWAN) designed to connect low power devices to the Internet. It was developed to meet and fulfill Internet of Things (IoT) devices' requirements, such as low-power consumption and low data throughput. 

![Murata CMWX1ZZABZ-078 LoRaWAN® Module](assets/)

Depending on the region, it will require to use the appropriate antenna for the respective frequencies. The common frequencies are 915 MHz for North America and Australia, and 863 MHz for European region. Frequencies are on a range, so for example Australia region it is possible to use 928 MHz compatible antenna and configuration. 

***For more in-depth information about LoRa® and LoRaWAN®, please read [The Arduino Guide to LoRa® and LoRaWAN®](https://docs.arduino.cc/learn/communication/lorawan-101).***

The LoRa® Connection tutorial with in-depth details on how to power up the module and establish connection to The Things Network (TTN), please go [here]() for more information. 

##### Cell Modem Initialization on Portenta Max Carrier
##### 1. Cat-M1

##### 2. NB-IoT

#### 1.5. Audio Interfaces

The Portenta Max Carrier features a stereo CODEC, the [CS42L52](https://www.mouser.com/datasheet/2/76/CS42L52_F2-1141287.pdf) from Cirrus Logic®. The CS42L52 is a 24-bit, low-power stereo CODEC that can provide up to 1W per channel of Class D stereo/mono amplification to external speakers (8-ohm stereo speakers and 4-ohm mono speakers) or enough power to drive 44mW per channel into stereo headphones. There are four analog audio interfaces in the Portenta Max Carrier, as shown in the image below:

- J13 - Audio line-in (right).
- J14 - Audio line-in (left).
- J12 - Audio line-out (right).
- J20 - Speaker line-out via Groove connector. 

You can use [this](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/5244/16056943) cable assembly and make your mono speaker. The CS42L52 stereo CODEC operates using an I2C interface, with the CODEC acting as a secondary device. 

Arduino Portenta H7 establishes I2C interface using the `Wire` library included in `ArduinoCore-mbed` package. The Arduino Portenta Max Carrier, while having paired the Portenta H7 via High-Density Connectors, is expanded via Header Connector J5. External modules requiring I2C interface can be established via header Connector J5 with up to 2 available I2C bridges. 

IP

#### 1.6. Onboard Debugger

Part of the development process, debugging process is crucial and it is required step if we are aiming now to work with industrial grade devices. The Portenta Max Carrier provides discrete debugging capability on-board. The feature can be accessed via micro USB to J-Link debugger. It is driven by STM32F405RGT6 controller and compatible with Segger® J-Link OB and Blackmagic probes. The module itself does not require Portenta H7 to be attached on the Portenta Max Carrier, meaning it does not require VBUS. 

***For more in-depth information about Debugging, please read [Debugging Fundamentals](https://docs.arduino.cc/learn/microcontrollers/debugging).***

### 2. Basic Setup of the Portenta Max Carrier
To take advantage of Portenta Max Carrier's Power Architecture, an important physical configuration requires to be verified. A DIP Switch for Boot mode selection is present on the Portena Max Carrier board. It requires to set **BOOT_SEL** to select between 2 boot addresses, which will enable Portenta H7 and Max Carrier to run the firmware. **BOOT** parameter will switch the Portenta H7 state into Boot mode.

Every time it initiates at Boot mode, the Portenta H7 will fade the Green LED to indicate its state. This will help to understand the board is in Boot mode and not turned off due to unavailable electric supply as it shutted off. As the power lines are alive even if the board shows no indication of operating instance. 

![Portenta Max Carrier Power DIP Switch](assets/)

### 3. Portenta Max Carrier Quick Peripheral Table
The following peripheral table will help you guide through quickly about the available connectors on Portenta Max Carrier. 

| PERIPHERAL             | PIN     | FUNCTION      | TYPE    | DESCRIPTION             |
| ---------------------- | ------- | ------------- | ------- | ----------------------- |
| **LoRa® Header (CN2)** |         |               |         |                         | 
|                        | 1       | +3V3          | Power   | +3V3 Power Rail         | 
|                        | 2       | LoRa_SWDIO    | Digital | LoRa® SWD Data Line     | 
|                        | 3, 5, 9 | GND           | Power   | Ground                  | 
|                        | 6 ~ 8   | NC            | NC      | Not Connected           | 
|                        | 4       | LoRa_SWCLK    | Digital | LoRa® SWD Clock Line    | 
|                        | 10      | LORA_RST      | Digital | LoRa® module reset pin  | 
| **Debug Header (CN3)** |         |               |         |                         | 
|                        | 1       | 3V3_DBG       | Power   | +3V3 Power Rail         |
|                        | 2       | DBG_SWDIO     | Digital | SWD Data Line           |
|                        | 3, 5, 9 | GND           | Power   | Ground                  | 

## Conclusion

### Next Steps

## Troubleshooting




