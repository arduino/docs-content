---
title: 'Getting Started with Nano Connector Carrier'
difficulty: beginner
description: 'This short guide takes you through the features of the Nano Connector Carrier, along with some important considerations when using this product.'
tags: [Prototyping]
author: 'Pedro Sousa Lima'
hardware:
  - hardware/03.nano/carriers/nano-connector-carrier
---

The Arduino Connector Carrier is a versatile expansion board designed for the Arduino Nano form factor. It provides an easy way to interface your Arduino Nano with various sensors, modules, and storage options through industry-standard connectors. This carrier board eliminates the need for complex wiring and breadboarding, allowing you to focus on your project's functionality rather than connectivity challenges.

![The Nano Connector Carrier](assets/cover.gif)

## Compatibility

The carrier is designed to work with all Arduino Nano form factor boards. Its standardized layout ensures compatibility with current and future Arduino Nano boards, giving you flexibility in your project development.

![Carrier With a Nano Board](assets/nano-formfactor.png)

## Features

The Arduino Connector Carrier comes packed with useful features to enhance your Arduino Nano projects:

#### Voltage Level Switch

To ensure compatibility and as some Arduino Nano boards can be configured to change its voltage level the carrier includes a switch to select 3.3V or 5V voltage levels. The voltage selector switch allows you to choose the appropriate voltage for your specific Nano board and connected peripherals.

![Onboard Voltage Switch](assets/power-switch-01.gif)

This flexibility ensures compatibility with a wide range of sensors and modules that operate at different voltage levels, eliminating the need for additional level shifters in most cases.

## Pinout

The Arduino Connector Carrier features a comprehensive pinout that makes it easy to connect various peripherals to your Arduino Nano. The board is divided into two main sections:

![Nano Carrier Pinout](assets/ASX00061-pinout-v2.png)

The pinout includes clearly labeled connections for all interfaces:
- Arduino Nano pins (Digital and Analog)
- SPI interface pins
- I²C interface pins
- Power lines (5V, 3.3V, GND)
- UART/Serial pins

All connectors on the board are mapped to specific Arduino Nano pins, making it straightforward to program your projects. The voltage level switch affects all VCC pins on the Grove and Qwiic connectors, allowing you to match your peripherals voltage requirements.

### Connectors

The Carrier includes a both QWIIC and Grove connectors for expanding the board capability with external sensors aswell a MicroSD:
![Available Connectors](assets/connector-list.png)

#### Qwiic Connector

The carrier features a single Qwiic connector, allowing you to easily interface with Arduino Modulinos and other I²C-based sensors and modules.

![QWIIC Connector](assets/qwiic-01.gif)

The Qwiic connector uses a 4-pin JST SH connector with standardized pinout:

| Pin | Connection |
|-----|------------|
| GND | Ground     |
| VCC | 3.3V/5V (selected by the voltage switch) |
| SDA | I²C Data (connected to A4 on the Nano) |
| SCL | I²C Clock (connected to A5 on the Nano) |

A single Qwiic connector is all you need since it's designed to be daisy-chainable, allowing you to connect multiple Modulinos or other Qwiic-compatible devices in series. This connector makes it plug-and-play simple to add sensors, displays, and other I²C devices to your project.

#### Grove Connectors

The board includes 4 Grove connectors, compatible with the extensive ecosystem of Grove modules.

![Grove Connector](assets/grove-01.gif)

Each Grove connector has a specific pin configuration:

**Grove (J5) - Analog**

| Pin | Connection |
|-----|------------|
| GND | Ground     |
| VCC | 5V or 3.3V (based on voltage switch) |
| A3  | Analog pin A3 |
| A2  | Analog pin A2 |

**Grove (J7) - Analog**

| Pin | Connection |
|-----|------------|
| GND | Ground     |
| VCC | 5V or 3.3V (based on voltage switch) |
| A1  | Analog pin A1 |
| A0  | Analog pin A0 |

**Grove (J4) - SPI**

| Pin | Connection |
|-----|------------|
| GND | Ground     |
| VCC | 5V or 3.3V (based on voltage switch) |
| MOSI | SPI MOSI (D11) |
| MISO | SPI MISO (D12) |

**Grove (J6) - I²C**

| Pin | Connection |
|-----|------------|
| GND | Ground     |
| VCC | 5V or 3.3V (based on voltage switch) |
| SDA | I²C Data (A4, shared with Qwiic) |
| SCL | I²C Clock (A5, shared with Qwiic) |

These standardized connectors eliminate the need for soldering or breadboarding and simplify connecting various sensors, actuators, and displays to your Arduino Nano.

#### Micro SD Card Slot

For projects requiring data logging or file storage, the carrier includes a Micro SD card slot.

![MicroSD Card Slot](assets/sd-card-01.gif)

The Micro SD card connects to the Arduino Nano through the SPI interface:

| SPI Signal | Arduino Pin |
|------------|-------------|
| MISO       | D12         |
| MOSI       | D11         |
| SCK        | D13         |
| CS         | D4 (default, configurable to D2 or D3) |

By default, pin D4 is used as the SPI SS (Chip Select) for the Micro SD card, but you can configure solder jumpers to use D2 or D3 instead if needed.

![SS Pin Selector Jumpers](assets/solder-jumper-01.gif)

With this feature, your Arduino Nano can read and write files on a Micro SD card, perfect for data logging applications, playing audio files, or storing configuration data.

## What to Do Next?

Now that you understand the features of the Arduino Connector Carrier, here are some exciting project ideas to get you started:

- **Weather Station**: Connect temperature, humidity, and pressure sensors via Grove connectors to create a simple weather monitoring system
- **Plant Monitor**: Use soil moisture and light sensors to monitor your houseplants and alert you when they need attention
- **Data Logger**: Use the Micro SD card slot to record sensor readings over time - perfect for environmental monitoring or tracking experiments
- **Smart Home Interface**: Create a hub that interfaces with multiple sensors around your home and logs data or sends alerts

For additional project inspiration, check out the Arduino Project Hub or join the Arduino community forums to share your creations and learn from others.

## Conclusion

The Arduino Connector Carrier transforms your Arduino Nano into a versatile platform capable of interfacing with numerous sensors, displays, and storage options. By eliminating complex wiring and providing standardized connectors, the carrier allows you to focus on developing your application rather than dealing with connection issues.