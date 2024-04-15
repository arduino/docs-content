---
title: 'Opta™ Expansions with the PLC IDE'
difficulty: beginner
description: "Learn how to use the Opta™ expansions to extend your solution capabilities with the Arduino® PLC IDE."
tags:
  - Expansions
  - IEC-61131-3
  - PLC-IDE
  - Opta™
author: 'Christopher Mendez'

hardware:
  - hardware/07.opta/opta-family/opta
  - hardware/07.opta/opta-family/opta-digital-ext
software:
  - plc-ide
---

## Overview

## Goals

## Hardware and Software Requirements

### Hardware
- [Opta™](https://store-usa.arduino.cc/collections/opta-family) (x1)
- [Opta Ext D1608E](https://store.arduino.cc/products/Opta-Ext-D1608E) (x1)
- [Opta Ext D1608S](https://store.arduino.cc/products/Opta-Ext-D1608S) (x1)
- 24 VDC/0.5 A power supply (x2)
### Software
- The [Arduino PLC IDE](https://www.arduino.cc/pro/software-plc-ide) (including Arduino PLC IDE Tools)

## Instructions 

### Solution Wiring

### Opta™ Micro PLC Setup

Now the server is configured, create a new project, this time for the Opta™ micro PLC that will be the Client or Master.

![New project for the Opta™](assets/new-project-opta.png)

Upload the runtime for Opta™ by selecting its serial port and clicking on the **Download** button as before.

![Uploading the runtime to the Opta™](assets/runtime-opta.png)

Once the runtime is flashed, with your Opta™ connected to your router, search for its IP address on the router configurations.

On the PLC IDE, navigate to **On-line > Set up communication**, activate and then open the **ModbusTCP** properties. Add the Opta™ IP address, then click "OK". 

![Modbus TCP connection](assets/modbus-prog-opta.png)
![Modbus TCP IP setup](assets/modbus-ip-opta.png)

Now, in the upper left corner, click on the **Connect** button and wait for the base program to be uploaded. A green **Connected** flag should appear in the lower right corner if everything goes well.

![Connecting the board](assets/connected-opta.png)

***The Opta™ is Pre-Licensed so you don't have to buy any license to use it with the PLC IDE***

If the Opta status says **No License**, click on the **Activate PLC runtime** button to activate it. Learn more about this case in this [guide](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license/#7-license-activation-with-pre-licensed-products-opta).

### Final Test

You can leave each device connected separately to the internet router or connect them together directly with one ethernet cable. The first option will let you update the preferred device remotely as you can access it through the local network.

Now you can expose the temperature sensor to some heat and monitor it from the PLC IDE. The Opta™ relay outputs and LEDs will close and turn on when the temperature surpasses the programmed thresholds respectively.

![Testing the project](assets/final.gif)

### Conclusion 

In this tutorial you learned how to communicate two Arduino PRO products using the Modbus TCP protocol, demonstrating a simple application of sharing temperature data to control the outputs of the devices.

As you can notice, the configuration process is very straightforward and the results were as expected, being a good starting point to adapt the work done here to create your own professional solution.

#### Next Steps

Extend your knowledge about the Portenta Machine Control, PLC IDE and the variety of industrial protocols it supports by following these tutorials:

- [Programming Introduction with Arduino PLC IDE](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-programming-introduction/)
- [Tank Thermoregulation with Portenta Machine Control & Opta™](https://docs.arduino.cc/tutorials/portenta-machine-control/pmc-opta-temp-ctrl/)
- [Connect an RTD/Thermocouple to the Portenta Machine Control](https://docs.arduino.cc/tutorials/portenta-machine-control/rtd-thermocouple-pmc/)
- [Arduino PLC IDE Setup & Device License Activation](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license/)