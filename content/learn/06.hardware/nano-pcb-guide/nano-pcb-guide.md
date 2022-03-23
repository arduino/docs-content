---
title: 'Designing Arduino Nano Hardware'
description: 'Learn how to create your own custom hardware that is compatible with the Arduino Nano Family.'
author: Karl Söderby
tags: [Nano Family, PCB Design]
---

![The Nano Family](assets/hero.png)

The Arduino Nano Family is a series of boards with a tiny footprint. This guide is dedicated to you who wants to design your own customized hardware for the Nano Family. 

This article aims to provide you with technical information that will aid the design of your own customized Nano hardware.

## Documentation

Each Nano Family board has a dedicated documentation page, see the list below:

- [Nano (classic)](/hardware/nano)
- [Nano Every](/hardware/nano-every)
- [Nano 33 BLE](/hardware/nano-33-ble)
- [Nano 33 BLE Sense](/nano-33-ble-sense)
- [Nano 33 IoT](/nano-33-iot)
- [Nano RP2040 Connect](/hardware/nano-rp2040-connect)

Inside the documentation page, you will find design files such as full pinout, CAD and Fritzing files. You will also find any tutorials and compatible libraries with the respective boards in this page.

## Technical Overview

### Dimensions

![Nano Dimensions]()

| Format | Measurement |
| ------ | ----------- |
| Width  | 18 mm       |
| Length | 45 mm       |
| Pitch  | 1.27 mm     |


### Feature Comparisons

Below is a comparison between the different Nano Family boards. 

| Board        | Nano          | Nano Every     | Nano 33 BLE  | Nano 33 BLE Sense | Nano 33 IoT       | Nano RP2040 Connect |
| ------------ | ------------- | -------------- | ------------ | ----------------- | ----------------- | ------------------- |
| Processor    | **ATmega328** | **ATmega4809** | **nRF42840** | **nRF42840**      | **SAMD21G18A**    | **RP2040**          |
| Radio Module | x             | x              | NINA-B306    | NINA-B306         | NINA-W102         | NINA-W102           |
| Connectivity | x             | x              | Bluetooth®   | Bluetooth®        | Wi-Fi, Bluetooth® | Wi-Fi, Bluetooth®   |
| Clock Speed  | 16 Mhz        | 16 Mhz         | 64 Mhz       | 64 Mhz            | 48 Mhz            | 133 MHz             |
| Flash Memory | 32 KB         | 48 KB          | 256 KB       | 256 KB            | 264 KB            | 16 MB               |
| SRAM         | 2 KB          | 6 KB           | 1 MB         | 1 MB              | 256 KB            | 16 MB               |
| EEPROM       | 1 KB          | 256 byte       | x            | x                 | x                 | x                   |
| I/O Voltage  | 5V            | 5V             | 3.3V         | 3.3V              | 3.3V              | 3.3V                |

There are several embedded sensors on the Nano boards, which can be seen below:

| Board       | Nano | Nano Every | Nano 33 BLE | Nano 33 BLE Sense | Nano 33 IoT | Nano RP2040 Connect |
| ----------- | ---- | ---------- | ----------- | ----------------- | ----------- | ------------------- |
| IMU         | x    | x          | **LSM9DS1** | **LSM9DS1**       | **LSM6DS3** | **LSM6DSOX**        |
| Microphone  | x    | x          | x           | **MP34DT05**      | x           | **MP34DT05**        |
| Gesture     | x    | x          | x           | **APDS-9960**     | x           | x                   |
| Light       | x    | x          | x           | **APDS-9960**     | x           | x                   |
| Color       | x    | x          | x           | **APDS-9960**     | x           | x                   |
| Pressure    | x    | x          | x           | **LPS22HB**       | x           | x                   |
| Temperature | x    | x          | x           | **HTS221**        | x           | x                   |
| Humidity    | x    | x          | x           | **HTS221**        | x           | x                   |

## Power Considerations

### Voltage (3.3V / 5V)

It is important to understand that the Nano family boards operates on different voltage. Any board with a radio module (Nano 33 BLE, Nano 33 BLE Sense, Nano 33 IoT, Nano RP2040 Connect) operates on **3.3V**. The Nano (classic), and Nano Every operates on **5V**.

The boards with radio modules are shipped with the 5V pin disconnected. This is a safety precaution, as connecting higher voltage signals to the board can damage the hardware. 

To enable the 5V pin, you will need to solder together the VUSB pads on the bottom of the board, as shown in the image below:

![Solder the VUSB pads.](assets/5V-PIN-VUSB.png)

### VIN Min/Max

The min/max voltage supply varies between boards. This is important to consider when choosing the battery source, that you do not exceed the limits to damage the board. 

| Nano  | Nano Every | Nano 33 BLE | Nano 33 BLE Sense | Nano 33 IoT | Nano RP2040 Connect |
| ----- | ---------- | ----------- | ----------------- | ----------- | ------------------- |
| xx-xx | xx-xx      | xx-xx       | xx-xx             | xx-xx       | xx-xx               |

### Battery Connection

None of the Nano Family boards have a battery connector due to its small form factor. This means it also has no battery charging circuit, such as the one onboard the [MKR WiFi 1010](https://store.arduino.cc/arduino-mkr-wifi-1010).

To power the Nano board using a battery, you will need to use the VIN pin (refer to the table in the section above).

![Nano battery connection.](assets/nano-external-power.png)

## Pinout

Nano boards largely share the placement of many pins, to make it easy for accessories to be designed for different Nano boards.

### Serial Buses

The Nano Family boards have serial buses attached to the following pins:

| Protocol | Pins                        |
| -------- | --------------------------- |
| UART     | RX,TX                       |
| SPI      | COPI(11), CIPO(12), SCK(13) |
| I²C      | SDA(A4), SCL(A5)            |

The location of these pins are located in the pinout for each board. These are found in the **Resources Section** product page of each board.

## Nano Form Factor Design Files

### PCB

Below are template files for creating your custom **Printable Circuit Board (PCB)**.

- [Nano Board PCB]()
- [Nano Shield PCB]()
- [Nano Carrier PCB]()

The files can be used together with various PCB design programs, such as [Altium](https://www.altium.com/) and [Eagle](https://www.autodesk.com/products/eagle/free-download) to create your own Nano accessories.

### 3D Files

The design file(s) below can be used for 3D printing, e.g. enclosures, mounts.

- [Nano Board Enclosure (STL)]()

## Soldering Directly To PCB

All Nano boards can be purchased **without headers**. This makes it possible to solder them directly to a custom PCB. If you need a template for PCBs, please refer to the [PCB Section](#pcb) at the start of this section.

Watch the short video below on how a Nano board can easily be soldered onto a circuit board.

<iframe></iframe>