---
title: 'ModBus Setup with Arduino PLC IDE'
description: 'This tutorial will show you how to set up the ModBus communication with the Arduino PLC IDE.'
tags:
  - PLC
  - ModBus
author: 'Pablo Marquínez'
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/portenta-machine-control
software:
  - plc-ide
---

## Overview

The Arduino Portenta Machine Control (PMC) is a fully-centralized, low-power, industrial control unit. For equipment and machinery control, industrial communication protocols, such as Modbus RTU over RS485 and Modbus TCP/IP over Ethernet, can be implemented in the PMC. In this tutorial, we will learn about how to get started on how to configure the ModBus communication with the Arduino PLC IDE.

## Goals

- Configure the ModBus communication (RTU and TCP)

## Required Hardware and Software

- [Arduino Portenta Machine Control](https://store.arduino.cc/products/arduino-portenta-machine-control) board
- [Arduino PLC IDE](../../../../software/plc-ide) license

## Set Up

In order to configure the Portenta Machine Control you will need to connect to the device through the Arduino PLC IDE.

1. Connect the device to the computer through USB
2. Click "Connects to the target" button on the PLC IDE

***The device needs to be activated with a license, check the steps on the [PLC IDE Set-up tutorial](./plc-ide-setup-license)***

***Both ModBus RTU and ModBus TCP can run at the same time in parallel***

## Configure The ModBus RTU Communication

***Important: Once you use the ModBus Mode to Master/Slave the RS485 ports will be only dedicated to ModBus, so the RS485 protocol is not accessible while using ModBus***

### ModBus RTU Configuration

Inside the Arduino PLC IDE navigate to the left side panel and click on the "Resources" tab.

![Arduino PLC IDE Resources panel, -> RS485 settings](assets/PLC-IDE-ModBus.png)

To configure the ModBus communication click on the "RS485 Serialport" label, it will open a new window on the middle to customize:

![ModBus configuration window](assets/ModBus-setup.png)

Then you can attach some functions to the Generic Modbus item, they will appear also in the **Catalog Tile Window**, you need to select first the **Generic Modbus_01**

![Modbus catalog add new item](assets/modBusCatalog-add.png)

![Modbus catalog select new item](assets/modbusCatalog-add-prompt.png)

#### Mode

* Not used
* ModBus RTU Master
* ModBus RTU Slave

#### Baud Rate

Bauds per second of the clock, options:
  * 600
  * 1200
  * 2400
  * 4800
  * 9600
  * 19200
  * 38400
  * 57600
  * 115200

#### Serial Mode

| Name    | Parity      | data bits | stop bits |
| ------- | ----------- | --------- | ----------|
| N, 8, 1 | No parity   | 8         | 1         |
| E, 8, 1 | Even parity | 8         | 1         |
| O, 8, 1 | Odd parity  | 8         | 2         |
| N, 8, 2 | No parity   | 8         | 2         |
| O, 8, 2 | Odd parity  | 8         | 2         |

#### Slave Settings

(Only available on slave mode)

* ModBus address
  Address of the device, from 1 to 247, it can not be repeated within the same ModBus net.

#### ModBus Node Configuration

Once you have configured your device as a **ModBus Master** you can attach some blocks to configure it, you can see them while you have the **RS485 SerialPort** on the **Catalog Tile Window**
![Modbus catalog](assets/modBusCatalog.png)

* Generic Modbus
  Configure the device name, Modbus address and the minimum polling time.

### ModBus TCP Configuration

***Important: Once you use the ModBus Mode, the ethernet port will be only dedicated to ModBus, so the ethernet protocol is not accessible while using ModBus***

Inside the Arduino PLC IDE navigate to the left side panel and click on the "Resources" tab.

To configure the ModBus communication click on the "Ethernet" label, it will open a new window on the middle to customize:

![Arduino PLC IDE Resources panel, -> Ethernet configuration](assets/modbusTCP-configuration.png)

* ModBus TCP Master: Enables the Master mode on the TCP bus (ModBus)
* ModBus TCP Slave: Always enabled, address 255

Then you can attach some functions to the Generic Modbus item, they will appear also in the **Catalog Tile Window**, you need to select first the **Generic Modbus device**

![ModBus catalog add new item](assets/modbusTCP-configurationAdd.png)

![ModBus catalog select new item](assets/modbusTCP-configurationCatalogAdd.png)

![ModBus TCP general configuration tab](assets/modbusTCP-configuration-general.png)

Settings:
* Name
* IP address
* Minimum polling time

## ModBus Parametrization

On the Generic
![Generic ModBus Parametrization Tab](assets/modbusParametrization.png)

## ModBus Devices Functions (Modbus FC)

* Modbus FC-01: This will read the status of the coils (digital outputs)
* Modbus FC-02: Reads the discrete inputs
* Modbus FC-03: Reads the holding registers
* Modbus FC-04: Read the input registers
* Modbus FC-05: Writes single coil state
* Modbus FC-06: Write single register
* Modbus FC-15: Write multiple coils
* Modbus FC-16: Write multiple registers

To configure the block you can click on it and it will show the configuration panel on the main window.
![ModBus item catalog](assets/genericModbus-catalog.png)

Inside each of the "devices" (functions) you can set its:
**General**
* Start address
* Polling time
* Time Out

![ModBus item general configuration](assets/genericModbus-catalog-setting-general.png)

**Coil/Register/Table**
This is a table to link all the coils, registers or variables that the function is going to poll/write.

![ModBus item specific configuration](assets/genericModbus-catalog-setting-specific.png)

### Next Steps

- Configure it as a ModBus Master device and connect a ModBus sensor to get data from.
- Interconnect two Portenta Machine Control boards and create a sketch to communicate between them.