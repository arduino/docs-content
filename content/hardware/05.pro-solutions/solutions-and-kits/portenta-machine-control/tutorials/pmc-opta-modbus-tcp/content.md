---
title: 'Modbus TCP with Portenta Machine Control & Opta™'
difficulty: intermediate
description: "Modbus TCP communication on a real industrial application using a Portenta Machine Control, Opta™, a temperature sensor, and the Arduino® PLC IDE."
tags:
  - Thermocouple
  - IEC-61131-3
  - PLC-IDE
  - Opta™
author: 'Christopher Mendez'

hardware:
  - hardware/05.pro-solutions/solutions-and-kits/portenta-machine-control
  - hardware/07.opta/opta-family/opta
  
software:
  - plc-ide
---

## Overview

In this tutorial, a Portenta Machine Control and an Opta micro PLC will be used as a **server** and a **client** respectively to share temperature information through a Modbus TCP using the PLC IDE. The server will do the measurements using a type K thermocouple and the client will activate its relay outputs when a certain threshold is reached.

## Goals

- Learn how to measure temperature with the Portenta Machine Control using a thermocouple and the PLC IDE
- Learn how to use the Modbus protocol over TCP/IP using the PLC IDE
- Leverage Arduino Pro products for real industrial applications 

## Hardware and Software Requirements

### Hardware
- [Portenta Machine Control](https://store.arduino.cc/products/arduino-portenta-machine-control) (x1)
- [Opta™](https://store-usa.arduino.cc/collections/opta-family) (x1)
- Type K thermocouple (x1)
- Ethernet cables (x2)
- Wired internet access
- 24 VDC Power Supply (x2)
### Software
- The [Arduino PLC IDE](https://www.arduino.cc/pro/software-plc-ide) (including Arduino PLC IDE Tools)
- [Portenta Machine Control - PLC IDE Activation](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license)

## Instructions 

### Solution Wiring

![Real Application Wiring Setup](assets/Wiring-white-small.png)

- In the __Portenta Machine Control__, connect the thermocouple terminals to TP0 and TN0 respectively. The 24 VDC power supply to the 24-volt input and GND. 

- In the __Opta micro PLC__, connect the power supply to the respective inputs on the screw terminals.

- Connect both the PMC and the Opta to your router using ethernet cables.

### Portenta Machine Control Setup

After downloading the [PLC IDE](https://www.arduino.cc/pro/software-plc-ide), open it and create a __new project__ for the Portenta Machine Control.

![New project for the PMC](assets/new-project.png)

We need a license for this product to be used with the PLC IDE that we can buy directly from the [Arduino store](https://store-usa.arduino.cc/products/plc-key-portenta-machine-control), it will include a **product key** needed to activate the device. 

Connect the PMC to the computer using a micro USB cable, the board needs to run a specific program (runtime) in order to interact with the **PLC IDE**. To flash it, select the device serial port and click on download.

![Runtime program download](assets/runtime.png)

Once the runtime is flashed, navigate to **On-line > Set up communication**, open the **Modbus** properties and select the **secondary** serial port, then click "OK". 

![Modbus properties](assets/modbus-prop.png)
![Modbus secondary serial port selection](assets/first-connect.png)

Now, in the upper left corner, click on the **Connect** button and wait for the base program to be uploaded. A green **Connected** flag should appear in the lower right corner if everything goes well.

![Connecting the board](assets/connect.png)

The device will show its activation status, in this case, **No License** as is the first time we are using it with the PLC IDE. To activate it, paste the **product key** you bought in the highlighted box and click on **Activate**. 

![Activation process](assets/activate.png)

After that, the status should say **OK**, and now you are ready to start programming the Portenta Machine Control with the PLC IDE.

If want to learn more about the PLC IDE first setup, continue reading this [detailed guide](https://docs.arduino.cc/software/plc-ide/tutorials/plc-ide-setup-license/#6-license-activation-with-product-key-portenta-machine-control).

#### Modbus TCP - Server
For the Modbus TCP configuration, on the **resources tab** go to the **Ethernet** section. As noticed, the Modbus TCP Slave mode is always enabled, so you don't have to make any changes.

![Modbus set to slave mode](assets/slave-mode.png)


### Opta Micro PLC Setup

#### Modbus TCP - Client

