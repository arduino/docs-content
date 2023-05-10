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

IN PROGRESS

The Opta™ features industrial grade hardware with rich connectivity options providing scalability, and the Arduino PLC IDE software enriches the experience by bringing most out of the Opta™ for solid field deployments. The Opta™ offers Modbus protocols and it can be implemented effortlessly using the Arduino PLC IDE.

The Modbus TCP is one of the protocols available within Opta™. In this tutorial, you will learn how to implement Modbus TCP based communication between two Opta™ devices using Arduino PLC IDE.

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

The **Modbus TCP/IP**, also briefly referred to as **Modbus TCP**, is a Modbus RTU protocol on Transmission Control Protocol and Internet Protocol (TCP/IP) interface over Ethernet to exchange data between compatible devices.

***For more information regarding the Modbus RTU protocol implementation on an Opta™, it may interest you to check out ["Getting Started with Modbus RTU on Opta™"](https://docs.arduino.cc/tutorials/opta/getting-started-with-modbus-rtu) tutorial.***

The Modbus protocol is a messaging service structure using Client/Server or Master/Slave communication. This is an *application protocol* to manage the data independent of the transmission method.

For the transmission, the *Transmission Control Protocol and Internet Protocol (TCP/IP)* is the transmission protocol integrating the TCP to handle the exchanging packets and IP to define the addresses for routing message destinations.

One characteristic to have in consideration using Modbus TCP is regarding how the data integrity is maintained. Due to Modbus TCP enclosing the basic data frame into the TCP frame, the usual checksum field of the Modbus is not used. Instead, the checksum method from Ethernet TCP/IP layer is used to ensure data integrity.

Thus, the Modbus TCP/IP is an integration of TCP/IP networking standards on the Ethernet using the Modbus messaging service as the data handler. The connected devices are usually Modbus TCP/IP Client and Server devices, but also interconnections established via routers, gateways, or bridges constructing a TCP/IP network.

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

***It is recommendable to check out [this tutorial](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license#3-project-setup) to familiarize with Arduino PLC IDE environment.***

#### Opta™ Basic Configuration

To use Modbus TCP, the device address used to identify for this protocol is by using IP address. Basically, if you attach the Opta™ and leave the ethernet configuration as default, the external DHCP server will provide IP address by assigning automatically for the Opta™. You will later need to scan for the address and use that IP address as the device address of the Opta™.

The Opta™ can also be configured with a specific IP address via a manual approach. This method is viable to assign the devices with specific addresses to operate under certain policy for example. To do this, you will have to define the IP setting by enabling the sketch found within `Resources` tab of the PLC IDE. The following image shows how the configuration could look like.

![Opta™ Manual IP Configuration](assets/opta_plcide_ipconfig.svg)

If the IP address for the Opta™ will be set manually, it is necessary to configure Ethernet interface on your computer by introducing manual IP address setting under IPv4.

The communication setting used to connect to Opta™ from Arduino PLC IDE requires an IP address. This IP address should be configured as same as your computer's subnet.

#### Modbus TCP Master (Client) and Server (Slave) Mode

The following image will show how the PLC IDE will welcome you when accessing the Modbus TCP configuration panel.

![Arduino PLC IDE - Modbus Role Configuration](assets/opta_plcide_ethernet_config.svg)

There are two options on the Modbus TCP configuration panel:

- Modbus TCP Master
- Modbus TCP Slave always enabled. Unit Identifier: 255

If the Modbus TCP Master remains unchecked, the Opta™ will behave as a Modbus TCP Slave with its assigned Unit Identifier. In this instance, you don't have to worry about the Unit Identifier because the configured IP address for the Opta™ will be the routing address to understand which Opta™ device it is talking to even though it has same Unit Identifier as the other.

On the other hand, if the Modbus TCP Master is checked, then the Opta™ will behave as a Master (Client) and also as a Slave (Server) device, prioritizing as a Master (Client). This will enable an option to add *General Modbus Node* under `Ethernet` configuration tab.

#### General Modbus Node Configuration

IN PROGRESS

The General Modbus Node allows to add information regarding the devices that will be communicating using Modbus messaging service.

![Arduino PLC IDE - General Modbus Node Configuration](assets/opta_plcide_generalNode.svg)

It will require you to fill basic information under `General` tab and expected parameters to intercept under `Parametrization` tab.

If you have added a General Modbus Node defining the Opta™ as a Modbus TCP Master (Client) initially and unchecked the Master (Client) role later, the Node option will stay. However, the Node's configuration field will change and request for Modbus address with `1 ... 247` range.

#### PLC IDE Modbus Custom Editor

IN PROGRESS

This is an alternative way of adding a Modbus node under `Ethernet` configuration tab. To open the Modbus Custom Editor window, go to `Tools -> Run Modbus Custom Editor` on PLC IDE.

![Arduino PLC IDE - Modbus Custom Editor Configuration](assets/opta_plcide_customModbus.svg)

It will allow to define device version and information with Modbus functions. This can later be deployed by adding it under `Ethernet` configuration tab.
  
### Project Overview

IN PROGRESS

Now that the pre-requisites are ready and you were able to understand how to set up Modbus TCP configuration for Opta™ using PLC IDE, an example project will be used to briefly test Modbus TCP communication between two Opta™ devices.

The example project will make a slight change to default example code using counter (`cnt`) variable and transmit the counter data to achieve a live handshake verification operation.

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