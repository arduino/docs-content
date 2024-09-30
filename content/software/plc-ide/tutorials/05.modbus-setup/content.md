---
title: 'Modbus Setup with Arduino PLC IDE'
description: 'This tutorial will show you how to set up the Modbus communication with the Arduino PLC IDE.'
tags:
  - PLC
  - Modbus
author: 'Pablo Marquínez'
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/portenta-machine-control
software:
  - plc-ide
---

## Overview

The Arduino Portenta Machine Control (PMC) is a fully-centralized, low-power, industrial control unit. For equipment and machinery control, industrial communication protocols, such as Modbus RTU over RS-485 and Modbus TCP/IP over Ethernet, can be implemented in the PMC. In this tutorial, we will learn about how to get started on how to configure the Modbus communication with the Arduino PLC IDE.

## Goals

- Configure the Modbus communication (RTU and TCP)

## Required Hardware and Software

- [Arduino Portenta Machine Control](https://store.arduino.cc/products/arduino-portenta-machine-control) board
- [Arduino PLC IDE](../../../../software/plc-ide) license

## Set Up

In order to configure the Portenta Machine Control you will need to connect to the device through the Arduino PLC IDE.

1. Connect the device to the computer through USB
2. Click "Connect to the target" button on the PLC IDE

***The device needs to be activated with a license, check the steps on the [PLC IDE Set-up tutorial](./plc-ide-setup-license)***

***Both Modbus RTU and Modbus TCP can run at the same time in parallel***

## Configure The Modbus RTU Communication

***Important: Once you use the Modbus Mode to Master/Slave the RS-485 ports will be only dedicated to Modbus, so the RS-485 protocol is not accessible while using Modbus***

### Modbus RTU Configuration

Inside the Arduino PLC IDE navigate to the left side panel and click on the "Resources" tab.

To configure the Modbus communication click on the "RS485 Serialport" label, it will open a new window in the middle to customize:

![Arduino PLC IDE Resources panel, -> RS-485 settings](assets/PLC-IDE-ModBus.png)

Then you can attach some functions to the Generic Modbus item, they will appear also in the **Catalog Tile Window**, you need to select first the **Generic Modbus_01**

![Modbus catalog add new item](assets/modBusCatalog-add.png)

![Modbus catalog select new item](assets/modbusCatalog-add-prompt.png)

#### Mode
<br></br>

* Not used
* Modbus RTU Master
* Modbus RTU Slave

#### Baud Rate
<br></br>


Baud rate, options:
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
<br></br>

| Name    | Parity      | data bits | stop bits |
| ------- | ----------- | --------- | ----------|
| N, 8, 1 | No parity   | 8         | 1         |
| E, 8, 1 | Even parity | 8         | 1         |
| O, 8, 1 | Odd parity  | 8         | 2         |
| N, 8, 2 | No parity   | 8         | 2         |
| O, 8, 2 | Odd parity  | 8         | 2         |

#### Slave Settings
<br></br>

(Only available on slave mode)

* Modbus address
  Address of the device: from 1 to 247. It can not be repeated within the same Modbus net.

#### Modbus Node Configuration
<br></br>

Once you have configured your device as a **Modbus Master** you can attach some blocks to configure it, you can see them while you have the **RS485 SerialPort** on the **Catalog Tile Window**
![Modbus catalog](assets/modBusCatalog.png)

* Generic Modbus
  Configure the device name, Modbus address and the minimum polling time.

### Modbus TCP Configuration

***Important: Once you use the Modbus Mode, the Ethernet port will be only dedicated to Modbus, so the Ethernet protocol is not accessible while using Modbus***

Inside the Arduino PLC IDE navigate to the left side panel and click on the "Resources" tab.

To configure the Modbus communication click on the "Ethernet" label, it will open a new window in the middle to customize:

![Arduino PLC IDE Resources panel, -> Ethernet configuration](assets/modbusTCP-configuration.png)

* Modbus TCP Master: Enables the Master mode on the TCP bus (Modbus)
* Modbus TCP Slave: Always enabled, address 255

Then you can attach some functions to the Generic Modbus item, they will appear also in the **Catalog Tile Window**, you need to select first the **Generic Modbus device**

![Modbus catalog add new item](assets/modbusTCP-configurationAdd.png)

![Modbus catalog select new item](assets/modbusTCP-configurationCatalogAdd.png)

![Modbus TCP general configuration tab](assets/modbusTCP-configuration-general.png)

Settings:
* Name
* IP address
* Minimum polling time

## Modbus Parametrization

On the Generic
![Generic Modbus Parametrization Tab](assets/modbusParametrization.png)

## Modbus Devices Functions (Modbus FC)

* Modbus FC-01: This will read the status of the coils (digital outputs)
* Modbus FC-02: Reads the discrete inputs
* Modbus FC-03: Reads the holding registers
* Modbus FC-04: Read the input registers
* Modbus FC-05: Writes single coil state
* Modbus FC-06: Write single register
* Modbus FC-15: Write multiple coils
* Modbus FC-16: Write multiple registers

To configure the block you can click on it and it will show the configuration panel on the main window.
![Modbus item catalog](assets/genericModbus-catalog.png)

Inside each of the "devices" (functions) you can set its:
**General**
* Start address
* Polling time
* Time Out

![Modbus item general configuration](assets/genericModbus-catalog-setting-general.png)

**Coil/Register/Table**
This is a table to link all the coils, registers or variables that the function is going to poll/write.

![Modbus item specific configuration](assets/genericModbus-catalog-setting-specific.png)

### Next Steps

- Configure it as a Modbus Master device and connect a Modbus sensor to get data from it.
- Interconnect two Portenta Machine Control boards and create a sketch to communicate between them.
