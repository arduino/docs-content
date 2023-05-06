---
title: 'Getting Started with Modbus TCP on Opta™ using PLC IDE'
description: "Learn how to set and enable Modbus TCP on Opta™ using Arduino PLC IDE."
author: 'Taddy Chung and José Bagur'
libraries:
  - name: 'ArduinoModbus'
    url: https://www.arduino.cc/reference/en/libraries/arduinomodbus
difficulty: intermediate
tags:
  - Getting-started
  - ModbusTCP
software:
  - plc-ide
hardware:
  - hardware/07.opta/opta-family/opta
---

## Overview

## Goals

TBD

- Learn how to configure Modus TCP on Opta™ using PLC IDE
- Learn how to configure workspace environment to work with Modbus TCP using PLC IDE
- Learn how to verify that Opta™ has been correctly set up and Modbus TCP is enabled using PLC IDE

## Required Hardware and Software

### Hardware Requirements

TBD

- Opta™ PLC (x1)
- USB-C® cable (x1)

### Software Requirements

TBD

- Arduino PLC IDE ([Official Website](https://www.arduino.cc/pro/software-plc-ide))

***If you have an Opta, you do not need any license key to activate your product.***

## Modbus TCP

## Instructions

### Setting Up the Arduino PLC IDE

TBD

To use the Arduino PLC IDE software, go to the [Arduino PLC IDE official website](https://www.arduino.cc/pro/software-plc-ide) and click on the download button. Download the following two executables:

  * The Arduino PLC IDE Tools
  * The Arduino PLC IDE

The first one will install all the required drivers, libraries and cores that you are going to need, while the second one will install the IDE software.

***For more details regarding Arduino PLC IDE setup, please have a look into [Arduino PLC IDE Setup and Board's License Activation](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license) tutorial.***

### Ethernet Connection on Opta™

IMAGE SHAREHOLDER - ETHERNET CONNECTION

### Workspace Pre-Configuration

TBD

- TCP server and client simultaneous operation (Configuration details)
- IP address configuration related details (DHCP address or manual configuration)
- Node configurations
- Modbus Custom editor (As a reference)

### Project Overview

#### Modbus TCP Client (Master)

TBD

WILL EXPLAIN HOW TO SET AND USE MODBUS TCP MASTER (CLLIENT) OPTION FOR OPTA

#### Modbus TCP Server (Slave)

TBD

WILL EXPLAIN HOW TO SET AND USE MODBUS TCP SLAVE (SERVER) OPTION FOR OPTA

### Testing the Modbus TCP

IMAGE SHAREHOLDER - MODBUS TCP TEST

## Conclusion

### Next Steps