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

The Portenta Max Carrier was designed to augment the capabilities of the Arduino® Portenta H7 board and provide easy access to its onboard peripherals. In the image below, you can see Portenta's Max Carrier main features highlighted: 

In this tutorial, we will describe the following features of the Portenta Max Carrier:

- Power distribution.
- Connectors.
- Onboard memory units.
- Wireless connectivity. 
- Audio interfaces.
- Onboard debugger.

Let us talk more about those features.

#### 1.1. Power Distribution

To power the Portenta Max Carrier, you can use the **barrel jack** connector (X1) or a **3.7V 18650 Li-Ion battery** connected to the Portenta's Max Carrier battery clips (J16 and J18). You can also power the Portenta Max Carrier directly from the USB-C connector of the Portenta H7 board.

You can see the detailed Portenta's Max Carrier power tree in the image below:

#### 1.2. Connectors

#### 1.3. Onboard Memory Units

#### 1.4. Wireless Connectivity

#### 1.5. Audio Interfaces

The Portenta Max Carrier features a stereo CODEC, the [CS42L52](https://statics.cirrus.com/pubs/proDatasheet/CS42L52_F2.pdf) from Cirrus Logic®. The CS42L52 is a 24-bit, low-power stereo CODEC that can provide up to 1W per channel of Class D stereo/mono amplification to external speakers (8-ohm stereo speakers and 4-ohm mono speakers) or enough power to drive 44mW per channel into stereo headphones. There are four analog audio interfaces in the Portenta Max Carrier, as shown in the image below:

- J13 - Audio line-in (right).
- J14 - Audio line-in (left).
- J12 - Audio line-out (right).
- J20 - Speaker line-out via Groove connector. 

You can use [this](https://www.digikey.ca/en/products/detail/adafruit-industries-llc/5244/16056943) cable assembly and make your mono speaker. The CS42L52 stereo CODEC operates using an I2C interface, with the CODEC acting as a secondary device. 

#### 1.6. Onboard Debugger

### 2. Basic Setup of the Portenta Max Carrier

## Conclusion

### Next Steps

## Troubleshooting




