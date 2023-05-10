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

## Overview

## Goals

- Learn how to configure Modus TCP on Opta™ using PLC IDE
- Learn how to configure workspace environment to work with Modbus TCP using PLC IDE
- Learn how to verify that Opta™ has been correctly set up and Modbus TCP is enabled using PLC IDE

## Required Hardware and Software

### Hardware Requirements

- Opta™ PLC (x2)
- USB-C® cable (x2)
- Ethernet LAN cable (x1)

### Software Requirements

- Arduino PLC IDE ([Official Website](https://www.arduino.cc/pro/software-plc-ide))

***If you have an Opta™, you do not need any license key to activate your product.***

## Modbus TCP

The **Modbus TCP/IP**, also briefly referred as **Modbus TCP**, is a Modbus RTU procol on Transmission Control Protocol and Internet Protocol (TCP/IP) interface over Ethernet to exchange data between compatible devices.

***For more information regarding the Modbus RTU protocol implementation on an Opta™, it may interest you to check out ["Getting Started with Modbus RTU on Opta™"](https://docs.arduino.cc/tutorials/opta/getting-started-with-modbus-rtu) tutorial.***

The Modbus protocol is a messaging service structure using the Client/Server or Master/Slave communication. This is an *application protocol* to manage the data independent from the transmission method.

For the transmission, the *Transmission Control Protocol and Internet Protocol (TCP/IP)* is the transmission protocol integrating the TCP to handle the exchanging packets and IP to define the addresses for routing message destinations.

Thus, the Modbus TCP/IP is an integration of TCP/IP networking standard on the Ethernet using Modbus messaging service as the data handler. The connected devices are usually Modbus TCP/IP Client and Server devices, but also interconnections established via routers, gateways, or bridges constructing a TCP/IP network.

## Instructions

### Setting Up the Arduino PLC IDE

You will be able to access the Arduino PLC IDE software by following [Arduino PLC IDE official website](https://www.arduino.cc/pro/software-plc-ide). You will have to download two executable files for proper installation of the software:

- Arduino PLC IDE
- Arduino PLC IDE Tools

The `Arduino PLC IDE` will install the IDE software, while the `Arduino PLC IDE Tools` will provide all the required drivers, libraries, and cores for development.

***For more details regarding Arduino PLC IDE setup, please have a look into [Arduino PLC IDE Setup and Board's License Activation](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license) tutorial.***

### Ethernet Connection on Opta™

The two Opta™ devices will communicate using Modbus TCP. It will need to use the Ethernet LAN cable attached on both devices on `ETH RJ45` port. The following image shows a simple connection diagram for two Opta™ devices.

![RJ45 Connection for two Opta™ devices](assets/opta_plcide_hardware_connection.svg)

### Workspace Pre-Configuration

There are some considerations that you will need to take it into account beforehand to properly enable and use Modbus TCP on Opta™ using PLC IDE. Following subsections will help briefly explain such aspects.

#### Opta™ Basic Configuration

To use Modbus TCP, the device address used to identify for this protocol is by using IP address. Basically, if you attach the Opta™ and leave the ethernet configuration as default, the external DHCP server will provide IP address by assigning automatically for the Opta™. You will later need to scan for the address and use that IP address as the device address of the Opta™.

The Opta™ can also be configured with a specific IP address via a manual approach. This method is viable to assign the devices with specific addresses to operate under certain policy for example. To do this, you will have to define the IP setting by enabling the sketch found within `Resources` tab of the PLC IDE. The following image shows how the configuration could look like.

![Opta™ Manual IP Configuration](assets/opta_plcide_ipconfig.svg)

#### Modbus TCP Master (Client) and Server (Slave) Mode

The following image will show how the PLC IDE will welcome you when accessing the Modbus TCP configuration panel.

IMAGE SHAREHOLDER - MODBUS TCP CONFIG PANEL PLC IDE

#### General Node Configuration

![Modbus General Node Configuration](assets/opta_plcide_generalNode.svg)

Following bulletpoints are **sub-sections of the workspace pre-configuration**.

#### PLC IDE Modbus Custom Editor

![Arduino PLC IDE Modbus Custom Editor Configuration](assets/opta_plcide_customModbus.svg)

- TCP server and client simultaneous operation (Configuration details) - To briefly explain how the PLC IDE handles the configuration and clarify such confusions that may arise
- IP address configuration related details (DHCP address or manual configuration) - This is to explain how to setup for both approaches when configuring to use Modbus TCP on PLC IDE. This is to help clarify the user the difference found between two approaches and why is it important.

Following are additional sub-sections to explain how set up (role based) for Modbus TCP communication with Opta and other devices when using PLC IDE.
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

To show the expected result when testing the example project

IMAGE SHAREHOLDER - MODBUS TCP TEST

## Conclusion

### Next Steps