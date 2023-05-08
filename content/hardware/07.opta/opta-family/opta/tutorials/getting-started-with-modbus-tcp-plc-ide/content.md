---
title: 'Getting Started With Modbus TCP On Opta™ Using PLC IDE'
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

**IT IS CURRENTLY IN TBD PHASE**

## Overview

## Goals

- Learn how to configure Modus TCP on Opta™ using PLC IDE
- Learn how to configure workspace environment to work with Modbus TCP using PLC IDE
- Learn how to verify that Opta™ has been correctly set up and Modbus TCP is enabled using PLC IDE

## Required Hardware and Software

### Hardware Requirements

- Opta™ PLC (x1)
- USB-C® cable (x1)

### Software Requirements

- Arduino PLC IDE ([Official Website](https://www.arduino.cc/pro/software-plc-ide))

***If you have an Opta, you do not need any license key to activate your product.***

## Modbus TCP

To briefly explain the Modbus TCP protocol:
- what is it
- why is it useful
- How it is intended to be used

## Instructions

### Setting Up the Arduino PLC IDE

To explain PLC IDE environment setup requirement

To use the Arduino PLC IDE software, go to the [Arduino PLC IDE official website](https://www.arduino.cc/pro/software-plc-ide) and click on the download button. Download the following two executables:

  * The Arduino PLC IDE Tools
  * The Arduino PLC IDE

The first one will install all the required drivers, libraries and cores that you are going to need, while the second one will install the IDE software.

***For more details regarding Arduino PLC IDE setup, please have a look into [Arduino PLC IDE Setup and Board's License Activation](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license) tutorial.***

### Ethernet Connection on Opta™

To explain how the hardware configuration is set up

IMAGE SHAREHOLDER - ETHERNET CONNECTION

### Workspace Pre-Configuration

Following bulletpoints are **sub-sections of the workspace pre-configuration**.

- TCP server and client simultaneous operation (Configuration details) - To briefly explain how the PLC IDE handles the configuration and clarify such confusions that may arise
- IP address configuration related details (DHCP address or manual configuration) - This is to explaing how to setup for both approaches when configurating to use Modbus TCP on PLC IDE. This is to help clarify the user the difference found between two approaches and why is it important.

Following are additional sub-sections to explain how set up for Modbus TCP communication with Opta and other devices when using PLC IDE.
- Node configurations (TENTATIVE)
- Modbus Custom editor (TENTATIVE)
  
### Project Overview

***EXAMPLE/PROJECT SECTION IS INTENDED TO SHOWCASE A SIMPLE METHOD TO VERIFY THE MODBUS TCP IS CORRECTLY IMPLEMENTED BETWEEN 2 OPTAS USING PLC IDE. (TENTATIVE)***
- Use `cnt` variable to pass this active variable over Modbus TCP triggered by a simple Modbus Function request. (CURRENT EXAMPLE IDEA)
- Maybe use STATUS LEDs as part of the example for visual indication..?

#### Modbus TCP Client (Master)

WILL EXPLAIN HOW TO SET AND USE MODBUS TCP MASTER (CLLIENT) OPTION FOR OPTA

#### Modbus TCP Server (Slave)

WILL EXPLAIN HOW TO SET AND USE MODBUS TCP SLAVE (SERVER) OPTION FOR OPTA

### Testing the Modbus TCP on Opta (PLC IDE)

IMAGE SHAREHOLDER - MODBUS TCP TEST

## Conclusion

### Next Steps