---
identifier: ABXXXXX
title: Arduino® Nano R4
type: maker
author: 
---

![](assets/featured.png)

# Description

The Arduino® Nano R4 is  a Nano form factor board based on the RA4M1 series microcontroller from Renesas (R7FA4M1AB3CFM#AA0), which embeds a 48 MHz Arm® Cortex®-M4 microprocessor. The Nano R4's memory is larger than its predecessors, with 256 kB flash, 32 kB SRAM and 8 kB data memory (EEPROM).

The Nano R4 board's operating voltage is 5 V, making it hardware compatible with Nano form factor accessories with the same operating voltage. Shields designed for previous Nano revisions are therefore safe to use with this board but are not guaranteed to be software compatible due to the change of microcontroller.

# Target areas:

Maker, Beginner, Education

# Features
- **R7FA4M1AB3CFM#HA0**
  - 48 MHz Arm® Cortex®-M4 microprocessor with a floating point unit (FPU)
  - 5 V operating voltage
  - Real-time Clock (RTC)
  - Memory Protection Unit (MPU)
  - Digital Analog Converter (DAC)
- **Memory**
  - 256 kB Flash Memory
  - 32 kB SRAM
  - 8 kB Data Memory (EEPROM)
- **Pins**
  - 14x digital pins (GPIO), D0-D13
  - 8x analog input pins (ADC), A0-A7
  - <!--- PWM pins--> 
  - SPI(D11,D12,D13), I2C (A4/A5), UART(D0/D1)
- **Peripherals**
  - USB 2.0 Full-Speed Module (USBFS)
  - up to 14-bit ADC
  - up to 12-bit DAC
  - Operational Amplifier (OPAMP)
- **Power**
  - Recommended input voltage (VIN) is 6-24 V
  - 5 V operating voltage
  - Power via USB-C® at 5 V
  - Schottky diodes for overvoltage and reverse polarity protection
- **Communication**
  - 1x UART (pin D0, D1)
  - 1x SPI (pin D10-D13)
  - 1x I2C (pin A4, A5)
  - 1x CAN (pin D4, D5, external transceiver is required)

# Contents

## The Board

The Nano R4 is a evolution of its predecessors the Nano Classic, being previously based on 8-bit AVR
microcontrollers. There are thousands of guides, tutorials and books written about the Nano board, where Nano R4 continues its legacy.
The board features the standard 14 digital I/O ports, 6 analog channels, dedicated pins for I2C, SPI and UART
connections. Compared to its predecessors the board has a much larger memory: 8 times more flash memory (256
kB) and 16 times more SRAM (32 kB).

### Application Examples

**Entry level projects:** If this is your first project within coding and electronics, the Nano R4 is a good fit. It is easy to get started with and has a lot of online documentation (both official + third party).

**Easy power management:** the Nano R4 supports input voltages from 6-24 V. Removes the need for additional circuitry required to step down the voltage.

**Cross compatibility:** the Nano form factor automatically makes it compatible with hundreds of existing third-party shields and other accessories.

### Related Products

- Arduino Nano Classic

<div style="page-break-after: always;"> </div>

# Rating

## Recommended Operating Conditions

| Symbol          | Description                          | Min | Typ | Max | Unit |
| --------------- | ------------------------------------ | --- | --- | --- | ---- |
| V<sub>IN</sub>  | Input voltage from VIN pad / DC Jack | 6   | 7.0 | 24  | V    |
| V<sub>USB</sub> | Input voltage from USB connector     | 4.8 | 5.0 | 5.5 | V    |
| T<sub>OP</sub>  | Operating Temperature                | -40 | 25  | 85  | °C   |

<!--- Temp to be confirmed-->

<div style="page-break-after: always;"> </div>

# Functional Overview

## Block Diagram

![Arduino Nano R4 Block Diagram](assets/Nano_R4_Block_Diagram.png)

## Board Topology

### Front View

![Top View of Arduino Nano R4](assets/topViewNanoR4.svg)

| **Ref.** | **Description**                      | **Ref.** | **Description**          |
| -------- | ------------------------------------ | -------- | ------------------------ |
| U1       | R7FA4M1AB3CFM#AA0 Microcontroller IC | J4       | <!--- to be confirmed--> |
| U2       | MP2322GQH Step-Down                  | DL1      | RGB LED                  |
| PB1      | RESET Button                         | DL2      | LED L                    |
| JP1      | Analog input/output headers          | DL3      | LED Power                |
| JP2      | Digital input/output headers         |
| J1       | CX90B-16P USB-C® connector           |
| J2       | QWIIC CONNECTOR                      |
| J3       | <!--- to be confirmed-->             |

### Back View

![Back View of Arduino Nano R4](assets/backViewNanoR4.svg)

## Microcontroller (R7FA4M1AB3CFM#HA0)

The Nano R4 is based on the 32-bit RA4M1 series microcontroller, **R7FA4M1AB3CFM#HA0**, from Renesas, which uses a 48 MHz Arm® Cortex®-M4 microprocessor with a floating point unit (FPU).

On the Nano R4, the operating voltage is fixed at 5 V to be fully retro compatible with shields, accessories & circuits originally designed for older Nano revisions.

The R7FA4M1AB3CFM#HA0 features:

- 256 kB flash / 32 kB SRAM / 8 kB data flash (EEPROM)
- Real-time Clock (RTC)
- 4x Direct Memory Access Controller (DMAC)
- up to 14-bit ADC
- up to 12-bit DAC
- OPAMP
- 1x CAN bus

For more technical details on this microcontroller, visit [Renesas - RA4M1 series](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra4m1-32-bit-microcontrollers-48mhz-arm-cortex-m4-and-lcd-controller-and-cap-touch-hmi).

## USB Connector

The Nano R4 has one USB-C® port, used to power and program your board as well as send & receive serial communication.

**_Note: You should not power the board with more than 5 V via the USB-C® port._**

## Digital Analog Converter (DAC)

The Nano R4 has a DAC with up to 12-bit resolution attached to the A0 analog pin. A DAC is used to convert a digital signal to an analog signal.

## I2C Connector

The I2C connector SM04B-SRSS-TB(LF)(SN) is connected to a secondary I2C bus on the board. Note that this connector is powered via 3.3 V.

<!---Posible connector pic-->

This connector also shares the following pin connections:

**JANALOG header**
- A4
- A5

<!---Is not this a separated I2C bus? I get this from the UNO R4 WiFi-->

## System

### Resets

### Timers

### Interrupts

## Serial Communication Protocols

### Inter-Integrated Circuit (I2C)

### Inter-IC Sound (I2S)

### Serial Peripheral Interface (SPI)

### Universal Asynchronous Receiver/Transmitter (UART)

## Power Options

### Power Tree

### Pin Voltage

### VIN Rating

### VBUS

### Using the 3.3 V Pin

### Pin Current

# Mechanical Information

## Pinout

### Analog

### Digital

### OFF

### ICSP

## Mounting Holes And Board Outline

## Board Operation

### Getting Started - IDE

### Getting Started - Arduino Cloud Editor

### Getting Started - Arduino Cloud

### Online Resources

### Board Recovery

# Certifications

## Declaration of Conformity CE DoC (EU)

## Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

## Conflict Minerals Declaration

## FCC Caution

## SRRC

## Company Information

## Reference Documentation

## Change Log