---
title: 'Nicla Voice User Manual'
difficulty: beginner
compatible-products: [nicla-voice]
description: 'Learn about the hardware and software features of the Arduino® Nicla Voice.'
tags: 
  - IMU
  - Cheat sheet
  - RGB
  - Communication
author: 'Benjamin Dannegård and José Bagur'
hardware:
  - hardware/06.nicla/boards/nicla-voice
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

This user manual will provide you with a comprehensive overview of the Arduino Nicla Voice board, covering its main hardware and software features. With this user manual, you will also learn how to set up, configure and use these features. 

## Hardware and Software Requirements

### Hardware Requirements

- [Nicla Voice](https://store.arduino.cc/products/nicla-voice) (x1)
- Micro USB cable (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- To create custom Machine Learning models, we will use the integrated Machine Learning Tools of the [Arduino Cloud](https://create.arduino.cc/iot/) (you will need to create an account if you don't have one yet)

## Product Overview

The Nicla Voice is an innovative and versatile development board designed by the Arduino team for voice-enabled projects and applications. This board has an onboard always-on speech recognition processor, advanced motion sensors, and wireless connectivity via Bluetooth® Low Energy. The Nicla Voice is an ideal solution for various applications, from ultra-low power predictive maintenance and gesture or voice recognition systems to contactless wireless applications.

### Board Architecture Overview

The Nicla Voice features a robust and efficient architecture that integrates various components to enable voice-enabled projects and applications. Here is an overview of the board's architecture main components shown in the image below:

- **Microcontroller**: at the heart of the Nicla Voice is the nRF52832, a powerful and versatile System-on-Chip (SoC) from Nordic® Semiconductor. The nRF52832 is built around a 32-bit Arm® Cortex®-M4 processor running at 64 MHz.
- **Speech recognition processor**: the board features the NDP120 Neural Decision Processor™, an ultra-low power always-on speech processor from Syntiant®, which enables several applications including echo-cancellation, beamforming, noise suppression, speech enhancement, speaker identification, and keyword spotting. 
- **Onboard advanced motion sensors**: the board features the BMI270, a high-precision IMU by Bosch® Sensortec, which combines a 3-axis accelerometer and a 3-axis gyroscope for precise motion tracking and orientation detection. The board also features the BMM150, a compact geomagnetic sensor from Bosch® Sensortec with a 3-axis magnetometer.
- **Onboard high-performance microphone**:  The Nicla Voice is equipped with the IM69D130, a high-quality MEMS microphone by Infineon® Technologies. The IM69D130 offers excellent audio quality and low noise performance, ensuring accurate and distortion-free audio capturing.
- **Wireless connectivity**: the board supports Bluetooth® Low Energy (BLE) connectivity, provided by the ANNA-B112 module developed by u-blox®. This compact, high-performance BLE module allows the Nicla Voice to communicate wirelessly with other devices and systems.
- **Power management**: The Nicla Voice is designed for ultra-low power operation, with efficient power management features that ensure minimal energy consumption even when using always-on speech recognition and multiple sensors.

### Board Core and Libraries

The **Arduino Mbed OS Nicla Boards** core contains the libraries you need to work with the board's components, such as its IMU, magnetometer and onboard. To install the core for Nicla boards, navigate to **Tools > Board > Boards Manager** or clicking the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `nicla` and install the latest `Arduino Mbed OS Nicla Boards` version.

![Installing the Arduino Mbed OS Nicla Boards core in the Arduino IDE bootloader.](assets/user-manual-1.png)

### Board Pinout

The Nicla Voice pinout is shown in the image below:

![Installing the Arduino Mbed OS Nicla Boards core in the Arduino IDE bootloader.](assets/nicla-voice-pinout.png)

### Board Datasheet

The Nicla Voice datasheet can be downloaded [here](assets/ABX00061-datasheet.pdf).

### Board Schematics

The Nicla Voice schematics can be downloaded [here](assets/ABX00061-schematics.pdf).

### Board STEP Files

The Nicla Voice STEP files can be downloaded [here](assets/ABX00061-step.zip).

## Board First Use

### Powering the Board

The Nicla voice can be powered in four ways:

1. Using a Micro USB cable. 
2. Using an external 5 V power supply connected to `VIN_BQ25120` pin. The recommended voltage is 5 V; the minimum voltage is 3.4 V and the maximum is 5.5 V.
3. Using a 3.7 V Lithium Polymer battery connected to the board through the onboard battery connector; the manufacturer part number of the battery connector is BM03B-ACHSS and the recommended battery capacity for the Nicla Voice is 200 mAh. A battery with an integrated NTC thermistor monitor is also recommended for thermal protection. 
4. Using the onboard ESLOV connector, which has a dedicated 5 V line; the manufacturer part number of the ESLOV connector is SM05B-SRSS. 