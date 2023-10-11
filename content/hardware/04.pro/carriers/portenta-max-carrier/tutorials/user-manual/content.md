---
title: 'Portenta Max Carrier User Manual'
description: 'Get a general overview of Portenta Max Carrier and its features.'
difficulty: intermediate
tags:
  - CAN
  - RS-232
  - RS-422
  - RS-485
  - Audio
  - WiFi
  - LoRa
  - CAT-M1 / NB-IoT
  - Connectivity
author: 'Christopher Méndez'
hardware:
  - hardware/04.pro/carriers/portenta-max-carrier
  - hardware/04.pro/boards/portenta-x8
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/boards/portenta-h7-lite
  - hardware/04.pro/boards/portenta-h7-lite-connected
  - hardware/04.pro/boards/portenta-c33
software:
  - ide-v1
  - ide-v2
  - iot-cloud
---

## Overview

This user manual offers a detailed guide on the Portenta Max Carrier, consolidating all its features for easy reference. It will show how to set up, adjust, and assess its main functionalities. This manual will guide as a key to proficiently operate the Portenta Max Carrier, making it suitable for project developments related to industrial automation, manufacturing automation, robotics, and prototyping.

![Portenta Max Carrier Overview](assets/overview.png)

## Hardware and Software Requirements

### Hardware Requirements

* [Portenta Max Carrier](https://store.arduino.cc/products/portenta-max-carrier) (x1)
* [Portenta X8](https://store.arduino.cc/products/portenta-x8) (x1)
* [Portenta C33](https://store.arduino.cc/products/portenta-c33) (x1)
* [Portenta H7](https://store.arduino.cc/products/portenta-h7) (x1)
* USB-C® cable (either USB-C® to USB-A or USB-C® to USB-C®) (x1)
* Wi-Fi® Access Point or Ethernet with Internet access (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)

## Product Overview

Max Carrier transforms Portenta modules into single-board computers that enable edge AI for high-performance industrial, building automation and robotics applications.
Thanks to dedicated high-density connectors, it can be paired with Portenta X8, H7 or C33, allowing you to easily prototype and deploy your industrial projects.

This Arduino Pro carrier further augments Portenta connectivity options with Fieldbus, LoRa®, Cat-M1 and NB-IoT.
Among the many available plug-and-play connectors there are Gigabit Ethernet, USB-A, audio jacks, microSD, mini-PCIe, MIPI camera, FD-CAN and Serial RS-232/422/485.
Max Carrier can be powered via external supply (6-36V) or battery via the onboard 18650 Li-ion battery connector.

![Portenta X8 Coupling](assets/portenta-x8.gif)

### Carrier Architecture Overview

![Portenta Max Carrier board overview](assets/architecture-v3.png)

Here is an overview of the board's architecture's main components shown in the image above:

- **Compatible core**: The board is compatible with Portenta X8 (ABX00049), Portenta H7 (ABX00042/ABX00045/ABX00046), and Portenta C33 (ABX00074). The Portenta H7 and C33 are limited in camera support and the Ethernet speed to 100 Mbit.
  
- **Power management**: The Portenta Max Carrier can either be powered through the power jack (6 ~ 36V DC) or a 18650 Li-ion/LiPo battery (3.7V) that can be used as backup power source if the external power supply fails.

The battery is charged while the minimum input voltage to the power jack is met.

- **USB connectivity**: The Portenta Max Carrier also includes a USB 2.0 Hi-Speed Hub controller based on the USB2514B/M2 that manages the 2 USB devices from the USB type A connector plus the LoRa® and PCIe modules. J15 is protected by a NCP383LMUAJAATXG (U7) power switch and current limiter.

  A USB-A female connector is used for data logging and the connection of external peripherals like keyboards, mice, hubs, and similar devices.
  
- **Ethernet connectivity**: The Gigabit Ethernet physical interface (J17) is directly connected to the high density connector to the Portenta board. The connector includes an activity LED indication (orange) and speed indication (green). __Note:__ Gigabit Ethernet functionality is only supported on the Portenta X8.

- **Serial Transceiver**: The Portenta Max Carrier includes a multi-protocol transceiver supporting RS-232, RS-485, and RS-422 serial standards (configurable) based on the SP335 IC. It is connected to a 6P6C Connector (RJ11, RJ12, RJ14, RJ25).

- **CAN Transceiver**: The Portenta Max Carrier includes a high speed CAN transceiver based on the TJA1049T/3J IC. It is connected to a 4P4C connector (RJ9, RJ10, RJ22).

- **Mini PCIe**: The Portenta Max Carrier includes one female mini PCI Express card slot. The connector is right angled and the board includes 2 removable standoffs for external module support. The Max Carrier supports two different Mini PCIe sizes. Pins 8, 10, 12 and 14 are reserved for UIM (in this case SIM).
__Note:__ USB, I2C and SIM functionality over PCIe is available only for the X8. Full PCIe functionality not provided at this time.

- **Cell Modem**: The SARA-R412M-02B is a multi-region modem capable of connecting to 2G/Cat-M1/NB-IoT networks worldwide. A dedicated SMA connector allows for an external antenna. The chip operates over the 1V8 power line. A microSIM slot is available, the corresponding SIM card slot for the cell modem is on the top side of the board, directly adjacent to the module.

- **Audio**: The Portenta Max Carrier enables connections to analog audio channels. This is done through the low power CS42L52 stereo CODEC providing ADC/DAC between analog signals and the I2S protocol. An internal Class D amplifier eliminates the need for external audio amplification circuitry. 

- **LoRa® Module**: The Portenta Max Carrier provides long range wireless connectivity for low bandwidth applications with the onboard Murata CMWX1ZZABZ-078 LoRa® transceiver module. This module operates on 3V3. A dedicated SMA connector allows for an external antenna. 

- **Storage**: The board has a MicroSD card slot for data logging operation and bootloading operation from external memory.

- **Debug interface**: Debugging capabilities are integrated directly into the Portenta Max Carrier and are accessible via microUSB. The J-link debugger is compatible with the Segger® J-Link OB and Blackmagic probes, driven by the STM32F405RGT6 controller. In addition to providing access to the Portenta board JTAG ports, different sniffer channels for I2C, CAN and UART lines. The debugger firmware can be updated via SWD on CN3. Additionally, headers for debugging the LoRa® are accessible via CN2 with SWD
   
- **DIP switch**: The carrier has a DIP switch with two position and allows different profiles depending on the paired Portenta board. The DIP switch has ETH CENTER TAP and BTSEL switches.
  
  when paired with **Portenta X8**, the ETH CENTER TAP will control 1 Gbit Ethernet capacity, while the BTSEL will make the system boot from SD Card memory if turned on or from MMC memory if selected in off position.
  
  The **Portenta H7/C33** will have the 100 Mbit Ethenet capacity controlled by ETH CENTER TAP, but BTSEL does not modify any settings.

### Carrier Topology
### Pinout
### Datasheet
### Schematics
### STEP Files
### Mechanical Information
## First Use Of Your Portenta Hat Carrier
### Stack The Carrier
### Power The Board
### Carrier Characteristics Highlight
### Using Portenta X8 with Linux
### Using Portenta X8 with Arduino
### Using Portenta H7 with Arduino
### Using Portenta C33 with Arduino
### Hello World Using Linux
### Hello World Using Arduino
## High-Density Connectors
## Network Connectivity
### Ethernet
### Wi-Fi® & Bluetooth®
### LTE CAT.M1 NB-IoT
### LoRa®
## mini PCIe
## MIPI Camera
## Audio Interface
## DIP Switch Configuration
## USB Interface
## MicroSD Storage
## CAN Bus (Onboard Transceiver)
### JTAG Pins
## Communication
### SPI
### I2C
### CAN Bus
### Serial RS-232 / RS-422 / RS-485
### UART

## Support

If you encounter any issues or have questions while working with the Portenta Max Carrier, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for the Portenta Max Carrier. The Arduino Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Portenta Max Carrier help center page](https://support.arduino.cc/hc)

### Forum

Join our community forum to connect with other Portenta Max Carrier users, share your experiences, and ask questions. The forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Portenta Max Carrier.

- [Portenta Max Carrier category in the Arduino Forum](https://forum.arduino.cc/c/hardware/portenta/portenta-max-carrier/175)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Portenta Max Carrier.

- [Contact us page](https://www.arduino.cc/pro/contact-us)