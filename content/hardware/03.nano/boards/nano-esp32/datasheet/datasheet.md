---
identifier: ABX00083
title: Arduino® Nano ESP32
type: maker
---
![](assets/featured.jpg)

# Description 
The Arduino® Nano ESP32 (with and without headers) is a Nano form factor board based on the ESP32-S3 microcontroller unit (MCU). This is the first Arduino board to be based fully on an ESP32 MCU, and features Wi-Fi, Bluetooth® LE, debugging via native USB in the Arduino IDE as well as low power.

The Nano ESP32 is compatible with the Arduino IoT Cloud, and has support for MicroPython. It is an ideal board for getting started with IoT development.

# Target areas:
Maker, Debugging, IoT, MicroPython

# Features
* **Espressif ESP32-S3** 
    * **Xtensa® Dual-core 32-bit LX7 Microprocessor**
      * Up to 240 MHz
      * 384 KB ROM
      * 512 KB SRAM
      * 16 KB SRAM in RTC (low power mode)
      * Built-in temperature sensor (not ambient)
      * DMA Controller
    * **Power**
      * Operating voltage 3.3V
      * VUSB supplies 5V via USB-C connector
      * VIN range is 6-18V
    * **Connectivity**
      * Wi-Fi
      * Bluetooth® LE
      * Built-in antenna
      * 2.4 GHz transmitter/receiver
      * Up to 150 Mbps
    * **Pins**
      * 14x digital (21x including analog)
      * 8x analog (available in RTC mode)
      * SPI(D11,D12,D13), I2C (A4/A5), UART(D0/D1)
    * **Communication Ports**
      * SPI
      * I2C
      * I2S
      * UART
      * CAN (TWAI®)
    * **Low Power**
      * 7 μA consumption in deep sleep mode
      * 240 μA consumption in light sleep mode
      * RTC Memory
      * Ultra Low Power (ULP) Coprocessor
      * Power Management Unit (PMU)
      * ADC in RTC mode

# Contents

## The Board

Nano ESP32 is a 3.3V development board based on the NORA-W106-10B from uBlox, a module that includes a ESP32-S3 system on a chip (SoC). This module has support for Wi-Fi and Bluetooth® Low Energy (LE), with amplified communication through a a built-in antenna. The CPU (32-bit Xtensa® LX7) support clock frequencies up to 240 MHz and has native support for debugging via the USB-C connector. 

### Application Examples

**Home automation:** an ideal board for building home automations for your home, such as smart switches, automatic lighting and motor control for e.g. motor controlled blinds. 

**IoT sensors:** with several dedicated ADC channels, accessible I2C/SPI buses and a robust ESP32 based radio module, this board can easily be deployed to monitor sensor values. 

**Low power design:** create battery powered applications with low power consumption, utilising the built in low power modes of the ESP32-S3 SoC. 

## ESP32 Core

The Nano ESP32 is based on the [Arduino Core for ESP32 boards](), a derivation of Espressif's [arduino-esp32](https://github.com/espressif/arduino-esp32) core.

# Rating

## Recommended Operating Conditions

| Symbol          | Description                      | Min                | Typ | Max                | Unit |
| --------------- | -------------------------------- | ------------------ | --- | ------------------ | ---- |
| V<sub>IN</sub>  | Input voltage from VIN pad       | 6                  | 7.0 | 24                 | V    |
| V<sub>USB</sub> | Input voltage from USB connector | 4.8                | 5.0 | 5.5                | V    |
| V<sub>DD</sub>  | Input high-level voltage         | 0.7*V<sub>DD</sub> |     | V<sub>DD</sub>     | V    |
| V<sub>IL</sub>  | Input low-level voltage          | 0                  |     | 0.3*V<sub>DD</sub> | V    |
| T<sub>OP</sub>  | Operating Temperature            | -40                | 25  | 85                 | °C   |

**Note:** V<sub>DD</sub> controls the logic level and is connected to the 5V power rail. V<sub>AREF</sub> is for the analog logic.

# Functional Overview

## Block Diagram

![Arduino Nano ESP32 Block Diagram](assets/UNO_R4_WiFi_Block_Diagram.png)

## Board Topology

### Front View

![Top View of Arduino Nano ESP32]()

| **Ref.** | **Description**                                  |
| -------- | ------------------------------------------------ |
| M1       | NORA-W106-10B (ESP32-S3 SoC)                     |
| J1       | CX90B-16P USB-C connector                        |
| JP1      | 1x15 analog header                               |
| JP2      | 1x15 digital header                              |
| U2       | MP2322GQH step down converter                    |
| U3       | GD25B128EWIGR 128 Mbit (16 MB) ext. flash memory |
| DL1      | RGB LED                                          |
| DL2      | LED SCK (serial clock)                           |
| DL3      | LED Power (green)                                |
| D2       | PMEG6020AELRX Schottky Diode                     |
| D3       | PRTR5V0U2X,215 ESD Protection                    |


### Back View

![Back View of Arduino Nano ESP32]()

## Microcontroller (NORA-W106-10B)

The Nano ESP32 is based on the 

The ESP32-S3 features:
* 

For more technical details on this microcontroller, visit [ESP32-S3 series]().


## USB Connector

The Nano ESP32 has one USB-C® port, used to power and program your board as well as sending & receiving serial communication.

Note that you should not power the board with more than 5V via the USB-C® port.

## LED Matrix

The Nano ESP32 features a 12x8=96 LED matrix (U_LEDMATRIX), connected using the charlieplexing technique. The LEDs are red.

The following pins on the RA4M1 MCU is used for the matrix:
- P003
- P004
- P011
- P012
- P013
- P015
- P204
- P205
- P206
- P212
- P213

![LED matrix schematics.](assets/matrix.png)

These LEDs can be accessed as an array, using a specific library. See the mapping below:

![LED matrix number mapping.](assets/matrix-2.png)

This matrix can be used for a number of projects and prototyping purposes, and supports animation, simple game designs and scrolling text among other things.

## Digital Analog Converter (DAC)

The Nano ESP32 has one 8-bit & one 12-bit DAC attached to the A0 analog pin. A DAC is used to convert a digital signal to an analog signal. 

The DAC is connected to 

<div style="page-break-after: always;"> </div>

## I²C Connector

The I²C connector SM04B-SRSS-TB(LF)(SN) is connected to the main I²C bus on the board. Note that this connector is powered via 3.3V.

![I²C connector.](assets/i2c-connector.png)

This connector also shares the following pin connections:

**JANALOG header**
- A4
- A5

**JDIGITAL header**
- SDA
- SCL

**Please note:** as A4/A5 is connected to the main I²C bus, these should not be used as ADC inputs whenever the bus is in use. You can however connect I²C devices to each of these pins and connector simultaneously.

## Power Options

Power can either be supplied via the VIN pin, or via USB-C® connector. If power is supplied via VIN, the ISL854102FRZ buck converter steps the voltage down to 5V.

Both VUSB and VIN pins are connected to the ISL854102FRZ buck converter, with Schottky diodes in place for reverse polarity & overvoltage protection respectively. 

Power via USB supplies about ~4.7V (due to Schottky drop) to the RA4M1 MCU.

The linear regulator (SGM2205-3.3XKC3G/TR) converts 5V from either the buck converter or USB, and provides 3.3V to a number of components, including the ESP32-S3 module.

### Power Tree

![Arduino Nano ESP32 power tree.](assets/UNO_R4_WiFi_Power_Tree.png)

### Pin Voltage

The general operating voltage for Nano ESP32 is 5V, however the ESP32-S3 module's operating voltage is 3.3V. 

### Pin Current

The GPIOs on the R7FA4M1AB3CFM#AA0 microcontroller can handle up to 20 mA. Never connect devices that draw higher current directly to a GPIO.

For powering e.g. servo motors, use an external power supply.

# Mechanical Information

## Pinout

![Pinout for Nano ESP32.](assets/ABX00080-pinout.png)

### Analog

| Pin | Function | Type   | Description                                     |
| --- | -------- | ------ | ----------------------------------------------- |
| 1   | BOOT     | NC     | Not Connected                                   |
| 2   | IOREF    | IOREF  | Reference for digital logic V - connected to 5V |
| 3   | Reset    | Reset  | Reset                                           |
| 4   | +3V3     | Power  | +3V3 Power Rail                                 |
| 5   | +5V      | Power  | +5V Power Rail                                  |
| 6   | GND      | Power  | Ground                                          |
| 7   | GND      | Power  | Ground                                          |
| 8   | VIN      | Power  | Voltage Input                                   |
| 9   | A0       | Analog | Analog input 0 / DAC                            |
| 10  | A1       | Analog | Analog input 1 / OPAMP+                         |
| 11  | A2       | Analog | Analog input 2 / OPAMP-                         |
| 12  | A3       | Analog | Analog input 3 / OPAMPOut                       |
| 13  | A4       | Analog | Analog input 4 / I²C Serial Datal (SDA)         |
| 14  | A5       | Analog | Analog input 5 / I²C Serial Clock (SCL)         |

### Digital

| Pin | Function  | Type    | Description                                      |
| --- | --------- | ------- | ------------------------------------------------ |
| 1   | SCL       | Digital | I²C Serial Clock (SCL)                           |
| 2   | SDA       | Digital | I²C Serial Datal (SDA)                           |
| 3   | AREF      | Digital | Analog Reference Voltage                         |
| 4   | GND       | Power   | Ground                                           |
| 5   | D13/SCK   | Digital | GPIO 13 / SPI Clock                              |
| 6   | D12/CIPO  | Digital | GPIO 12 / SPI Controller In Peripheral Out       |
| 7   | D11/COPI  | Digital | GPIO 11 (PWM) / SPI Controller Out Peripheral In |
| 8   | D10/CS    | Digital | GPIO 10 (PWM) / SPI Chip Select                  |
| 9   | D9        | Digital | GPIO 9 (PWM~)                                    |
| 10  | D8        | Digital | GPIO 8                                           |
| 11  | D7        | Digital | GPIO 7                                           |
| 12  | D6        | Digital | GPIO 6 (PWM~)                                    |
| 13  | D5/CANRX0 | Digital | GPIO 5 (PWM~) / CAN Transmitter (TX)             |
| 14  | D4/CANTX0 | Digital | GPIO 4 / CAN Receiver (RX)                       |
| 15  | D3        | Digital | GPIO 3 (PWM~)                                    |
| 16  | D2        | Digital | GPIO 2                                           |
| 17  | D1/TX0    | Digital | GPIO 1 / Serial 0 Transmitter (TX)               |
| 18  | D0/TX0    | Digital | GPIO 0 / Serial 0 Receiver    (RX)               |

## Mounting Holes And Board Outline

![Mechanical View of Arduino Nano ESP32]()
