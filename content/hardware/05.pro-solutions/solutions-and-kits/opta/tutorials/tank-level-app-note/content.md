---
title: 'Tank Level Monitoring with Opta (Application Note)'
description: "This application note describes how to monitor the level in tanks using the Arduino® Opta."
difficulty: beginner
tags:
  - Tank level
  - Opta
  - RS-485
  - Modbus
  - Level sensor
author: 'José Bagur and Taddy Chung'
libraries:
  - name: ArduinoModbus
    url: https://www.arduino.cc/reference/en/libraries/arduinomodbus/
  - name: ArduinoRS485
    url: https://www.arduino.cc/reference/en/libraries/arduinors485/
  - name: Scheduler
    url: https://www.arduino.cc/reference/en/libraries/scheduler/
software:
  - ide-v1
  - ide-v2
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/opta
---

## Introduction

Monitoring and adjusting tank levels, in-situ and remotely, are everyday tasks that are done in many industries, even in your house. Some industrial applications include transport and storage tanks (for example, think of a tank in a water treatment plant). In household applications, tank level monitoring is essential for applications like water dispensers, water evaporators, streamers, monitoring systems of boilers, heating systems, washing machines, steam irons, automated coffee machines, etc. With its industrial IoT capabilities, the Opta micro PLC can be used for this application. 

## Goals

This application note aims to show a system based on the Opta, capable of monitoring and adjusting two tank levels; we will refer to those tanks as Big Tank (BT) and Small Tank (ST). The goals to be met by the application are the following:

- BT and ST levels must stay within a minimum and a maximum user-defined level; maximum and minimum levels will be measured using float switches. A vertical-type float switch will be used for measuring the maximum level, while a horizontal-type float switch will be used for measuring the minimum level in the tanks.
- If the ST level goes below its minimum level, a relay opens a gate valve from the BT, letting the BT liquid fill the ST. When the level in the ST goes over its maximum, the relay closes the gate valve.
- If the BT level goes over its maximum level, a pump is activated to bring its level back below its maximum level.
- If the BT level goes below its minimum level, the system gets blocked, and the levels of the ST don't activate the relay that opens or closes the gate valve of the BT.

A graphical representation of the intended application is shown below:

![Graphical representation of the tank level monitoring application.](assets/application_represetation.png)

BT is at least 2.5 times bigger than ST in the experimental setup shown before.

## Hardware and Software Requirements

### Hardware Requirements

- [Arduino Opta](https://store.arduino.cc/products/nicla-sense-me)
- USB-C® cable (x2)
- [Vertical float switch](https://export.rsdelivers.com/product/rs-pro/rs-pro-vertical-pp-float-switch-float-300mm-cable/0519242) (x2)
- [Horizontal float switch](https://export.rsdelivers.com/product/rs-pro/rs-pro-horizontal-external-nylon-float-switch-1m/1748421) (x2)
- [12VDC solenoid valve](https://www.sparkfun.com/products/10456) (x1) 
- [12VDC liquid pump](https://www.sparkfun.com/products/10455) (x1)
- [12VDC DIN rail power supply](https://uk.rs-online.com/web/p/din-rail-power-supplies/2411620) (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- If you choose the offline Arduino IDE, you must install the following libraries: `ArduinoModbus`, `ArduinoRS485`, and `Scheduler`.
- For the Wi-Fi connectivity feature of the Opta, we will use [Arduino IoT Cloud](https://create.arduino.cc/iot/things); you will need to create an account if you still need to create one.

## Demonstration Setup

The electrical connections of the intended application are shown in the diagram below:

![Electrical connections of the application.](assets/electrical_connections.png)

Notice that the Optas communicate with each other using Modbus RTU over RS-485. The level sensors (vertical and horizontal float switches) are monitored via the digital input pins of the Optas; the pump and the gate valve are controlled using the built-in relay outputs of the Optas.

## Demonstration Description

ST and BT each have a specific monitoring routine to monitor and control their minimum and maximum level. Both Optas will exchange important states and parameters of each tank to understand and execute appropriate actions to maintain both tank levels as expected in the application. As stated before, the Optas in charge of ST and BT will communicate with each other using Modbus RTU over RS-485.

The Opta in the BT performs the following actions:

- It activates the pump if its maximum level alarm is triggered; this will cause liquid migration from BT to ST. 
- It shuts off the system completely, halting any activity on it.
- It sends the current minimum level state to ST while also seeking for ST maximum level state. 

The Opta in the ST performs the following actions:

- It manages the gate valve given the ST level and BT minimum level state. 
- It sends ST's current maximum level state to BT while seeking BT's minimum level state. 

## Conclusion

## References 