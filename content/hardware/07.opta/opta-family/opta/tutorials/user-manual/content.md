---
title: 'Opta™ C33 User Manual'
difficulty: beginner
compatible-products: [portenta-c33]
description: 'Learn about the hardware and software features of the Arduino® Portenta C33.'
tags:
  - Cheat sheet
  - User manual
  - Portenta C33
author: 'José Bagur and Julián Caro Linares'
hardware:
  - hardware/04.pro/boards/portenta-c33
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

This user manual will provide a comprehensive overview of the Opta™, covering its major hardware and software elements. With this user manual, you will learn how to set up, configure and use all the main features of an Opta™ device.

## Hardware and Software Requirements

### Hardware Requirements

- [Opta™ WiFi](https://store.arduino.cc/products/opta-wifi) (x1)
- USB-C® cable (x1)
- 24 VDC/0.5A power supply (x1)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Web Editor](https://create.arduino.cc/editor)
- [Arduino PLC IDE 1.0.3+](https://www.arduino.cc/en/software)

## Opta™ Overview

The Opta™ is a secure micro Programmable Logic Controller (PLC) with Industrial Internet of Things (IoT) capabilities. Developed in partnership with Finder®, this device supports both the Arduino programming language and standard IEC-61131-3 PLC programming languages such as Ladder Diagram (LD), Sequential Function Chart (SFC), Function Block Diagram (FBD), Structured Text (ST) and Instruction List (IL), making it an ideal device for automation engineers. Based on the STM32H747XI from STMicroelectronics®, a high-performance Arm® Cortex®-M7 + Cortex®-M4 microcontroller, the Opta™  is a perfect option for a wide range of applications, from real-time control to predictive maintenance applications.

### Opta™ Main Components

The Opta™ features a secure and durable design that enables it for automation applications. 

Here's an overview of the device's main components shown in the images above:

- **Microcontroller**: At the heart of the Opta™ is the STM32H747XI, a powerful and high-performance microcontroller from STMicroelectronics®. The STM32H747XI is built around an Arm® Cortex®-M7 and Cortex®-M4 32-bit RISC cores. The Cortex®-M7 core operates at up to 480 MHz, and the Cortex®-M4 core at up to 240 MHz.
- **Wireless connectivity**: The Opta™ (WiFi variant only) supports 2.4 GHz Wi-Fi® (802.11 b/g/n) and Bluetooth® Low Energy (4.2 supported by firmware and 5.1 supported by hardware), allowing the device to communicate wirelessly with other devices and systems. 
- **Ethernet connectivity**: The Opta™ (all variants) features an onboard, high-performance 10/100 Mbps Ethernet transceiver accessible through its onboard RJ45 connector.
- **Security**: The Opta™ features an onboard ready-to-use secure element, the ATECC608B from Microchip®, specifically designed for IoT devices and provides advanced security features.
- **USB connectivity**: The Opta™ features an onboard USB-C port that can be used for programming purposes.
- **Analog and digital peripherals**: The Opta™ features analog and digital peripherals such as eight analog/digital input ports and four digital outputs ports (relay outputs). 
- **RS-485 connectivity**: The Opta™ (all variants) features a physical RS-485 communication interface available through an onboard connector. 