---
title: 'Arduino UNO R4 Minima Cheat Sheet'
description: 'Learn how to set up the UNO R4 Minima, get a quick overview of the components, information regarding pins and how to use different Serial (SPI, I2C, CAN) protocols.'
tags:
  - Installation
  - I2C
  - SPI
  - UART
  - JTAG
  - CAN
  - DAC
author: 'Hannes Siebeneicher'
hardware:
  - hardware/08.mega/boards/giga-r1-wifi
software:
  - ide-v1
  - ide-v2
  - web-editor
---

The Arduino® UNO R4 Minima is a development board with the classic UNO formfactor, based on the renesas microcontroller. Compared to the UNO R3 it now comes with 32 KB of RAM memory, a clock speed of 48 MHz and a USB-C® port.

This article is a collection of guides, API calls, libraries and tutorials that help you getting started with the UNO R4 Minima.

## Datasheet

The full datasheet is available as a downloadable PDF from the link below:

- [Download the UNO R4 Minima datasheet](https://www.google.com/)

## Power Supply

To power the UNO R4 Minima you may either use a USB-C® cable, or the VIN pin.

If you’re using the USB-C® connector you must power it with 5V.

Powering the board with the VIN pin gives you more options, as you can safely power the board with any voltage between 6-24V.


## Installation

***For detailed instructions on how to install the UNO R4 Minima core, please refer to the [Getting Started with the UNO R4 Minima [LINK MISSING]]() guide.***

The **UNO R4 Minima** can be programmed through:

- The **Classic Arduino IDE 1.8.X**, 
- the **Arduino IDE 2.0.X**, 
- and the **Web Editor**. 

## Core

The UNO R4 Minima is based on the [Arduino Core for renesas devices](https://github.com/bcmi-labs/ArduinoCore-renesas), which also provides a set of examples that work out of the box.

### Bootloader

In case you need to flash the bootloaderyou can follow these steps:

- Install the rensesas core.
- Navigate to: 

"C:\Users\YourWindowsUserName\AppData\Local\Arduino15\packages\arduino\hardware\
renesas\0.5.0\bootloaders\SANTIAGO"

- Identify the **dfu.exe***
- Instal the Renesas flash programmer ([download page](https://www.renesas.com/us/en/software-tool/renesas-flash-programmer-programming-gui))
- To flash the bootloader:
    - Select dfu.exe.
    - Connet your board.
    - Short the BOOT and GND pin found on the UNO R4 Minima
    - Go to the Connect Settings tab.
    - Select COM port in teh Tool > select the port shown in the IDE.
    - Press start. 

## Renesas R7FA4M1AB3CFM

The UNO R4 Minima features the powerful and very robust renesas microcontroller also found on the UNO R4. Renesas microcontrollers are known for their high performance and robustness, including their built in peripheral set. 

These peripherals include analog-to-digital converters, timers, pulse width modulation (PWM) units, communication interfaces (such as UART, SPI, and I2C) and more.

## Memory

### RAM

The **UNO R4 Minima** comes equipped with 32 KB of RAM memory.

### Flash

The flash memory comes in 256 KB code and 8 KB data.

## Pins

### SWD Connector

On the R4 Minima there is a a debugging option available using the SWD connector pins (2x5 header pitch, 1.27mm) mounted on the board.

### PWM

There are a total of 6 PWM pins located on the R4 Minima. They are marked with ~ on the headers. Otherwise take a look at the pinout [here]().

### I2C

SCL and SDA pins of JDIGITAL are shared with A4 (SDA) and A5 (SCL) owners of previous UNO's are familiar with. The Pullups are not mounted on the PCB but ithere are footprints to do so if needed.

### 1 SPI

The UNO R4 Minima has one Serial Peripheral Interface (SPI) which is located... 

### CAN Bus

### Analog ADC

### Analog DAC

### Analog Operational Amplifier

### Digital

### Serial Ports

### Boot Pin