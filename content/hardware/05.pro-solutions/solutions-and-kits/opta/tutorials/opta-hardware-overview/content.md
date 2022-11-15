---
title: 'Arduino Opta Hardware Overview'
description: 'Get an overview of the Arduino Opta's hardware and software features'
difficulty: beginner
tags:
  - Hardware
author: 
libraries:
  - name: 
    url: 
hardware:
  - hardware/04.pro/
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Overview

The Arduino Opta is a powerful tool to incorporate into your industrial or production environment. This PLC can also be used with an Arduino device, like the Portenta Machine Control, to further expand its capabilities and features. This article will highlight the Opta's features so you can easily identify how this device can best work for you.

## Goals

- Learn about the features that the Arduino Opta provides

### Required Hardware and Software

- USB C cable (either USB A to USB C or USB C to USB C)
- Arduino IDE 1.8.13+  or Arduino Pro IDE 0.0.4+ 
- Arduino Opta
- Arduino Portenta Machine Control (optional for some features)

## Hardware Features

### CAN bus

![CAN bus connectors on the Opta]()

CAN, which is short for Controller Area Network, is a bus designed for devices to communicate with each other without involving a host computer, such as a server. CAN provides an inexpensive, durable network that helps multiple CAN devices communicate with one another. An advantage to this is that electronic control units can have a single CAN interface rather than analog and digital inputs to every device in the system. 

![Example of a CAN network and one without]()

The CAN bus can be applied to control a wide variety of applications such as lights, tables, cameras, lifts, escalators, controllers, doors, laboratory equipment, sports cameras, telescopes, automatic doors, and even coffee machines. This has made it so that CAN is used in many different fields, from the automotive and aerospace field to the medical equipment industry.

### Ethernet (RJ45)

The Opta has a RJ45 ethernet port with a LED that will indicate the status of the connected cable. The 10/100 Ethernet physical interface is directly connected to the internal Ethernet MAC and provides half-duplex communication with automatic MDIX support. With an internet connection, the ethernet communication can be used to connect the device to the Arduino IoT Cloud. This Ethernet port supports Modbus TCP connection.

![Ethernet port on the Opta]()

### Modbus TCP via Ethernet port

Modbus TCP is a variant of the Modbus family of simple, vendor-neutral communication protocols intended for supervision and control of automation equipment. Specifically, it covers the use of Modbus messaging in an intranet or internet environment using the TCP/IP protocols. The most common use of the protocols at this time is for Ethernet attachment of PLCs, I/O modules and gateways to other simple field buses or I/O networks.

### Modbus(RS485)

![Modbus connectors on the Opta]()

The Arduino Opta uses the RS485 protocol for Modbus communication. Enabling Modbus TCP and Modbus RTU communication.

### Modbus RTU

Modbus RTU is an open serial protocol derived from the client/server architecture. It is a widely accepted serial level protocol due to its ease of use and reliability. Modbus RTU is widely used within Building Management Systems and Industrial Automation Systems.

Modbus RTU messages are a simple 16-bit structure with a Cyclic-Redundant Checksum. The simplicity of these messages ensures reliability. Due to this simplicity, the basic 16-bit Modbus RTU register structure can be used to pack in floating point, tables, ASCII text, queues, and other unrelated data.

This protocol primarily uses the RS-485 serial interfaces for communications and is supported by every commercial SCADA, HMI, OPC server and data acquisition software program in the marketplace. This makes it very easy to integrate Modbus-compatible equipment into new or existing monitoring and control applications.

### Wi-Fi® and Bluetooth® Low Energy

The onboard wireless module allows simultaneous management of WiFi and Bluetooth connectivity. The WiFi interfacecan be operated as an Access Point, as a Station or as a dual mode simultaneous AP/STA and can handle up to 65Mbps transfer rate. Bluetooth interface supports Bluetooth Low Energy (BLE 4.2). With an internet connection, the Wi-Fican be used for connecting to the Arduino IoT Cloud.

For more information on how to use these features, take a look at our [Getting started with connectivity features on the Arduino Opta]().

## Software Features

### NTP library

NTP stands for Network Time Protocol, and it is an Internet protocol used to synchronize the clocks of devices to some time reference. NTP is an Internet standard protocol.

If you have communicating programs running on different computers, time should stay synchronized if you switch from one computer to another. Obviously if one system is ahead of the others, the others are behind that particular one. From the perspective of an external observer, switching between these systems would cause time to jump forward and back, a non-desirable effect. As a consequence, isolated networks may run their own wrong time, but as soon as you connect to the Internet, effects will be visible. Even on a single computer some applications have trouble when the time jumps backwards. For example, database systems using transactions and crash recovery like to know the time of the last good state. NTP needs some reference clock that defines the true time to operate. All clocks are set towards that true time. (It will not just make all systems agree on some time, but will make them agree upon the true time as defined by some standard.)

NTP is highly scalable: A synchronization network may consist of several reference clocks. Each node of such a network can exchange time information either bidirectional or unidirectional. Propagating time from one node to another forms a hierarchical graph with reference clocks at the top.

### Supported Programming Languages

Using Arduino IDE and Logic Lab with the Arduino Opta it is possible to utilize a range of different programming languages. To use the Opta with Logic Lab we need to use a Arduino Portenta Machine Control with it. Let's take a look at the different ones available to us with this set up.

### Ladder Diagram

Ladder Diagram is a graphics-oriented programming language that resembles that of an electric circuit structure. This language is suitable for constructing logical switches and creating networks as in Function Block Diagram. The LD language is useful for controlling the call of other Program Organisation Units (POU).

The Ladder Diagram consists of a series of networks, each being limited by a vertical current line. A network contains a circuit diagram made up of contacts, coils, optionally additional POUs, and connecting lines.

### Sequential Function Chart

Sequential function chart (SFC) is a graphical programming language used for programmable logic controllers, such as PLCs. It can be used to program processes that can be split into steps. Steps in an SFC diagram can be active or inactive. Actions are only executed for active steps. ////

### Function Block Diagram

A Functional Block Diagram (FBD) is a graphical representation of a functional process via blocks and diagrams that is easier for a reader to understand and interpret. An FBD can help us determine the function between output variables and input variables via a set of rudimentary blocks and diagrams that are connected with arrows known as connections. A Functional Block Diagram can help us create relationships between one or more than one variable (both input and output) to establish our understanding of functional processes aligned in a system.

### Structured Text

Structured Text or just ST is based on and resembles traditional programming languages like Python or Java.

### Instruction List

Instruction lists (IL) are not a graphical programming language. Instead, they most resemble assembly language programming. As the name implies, a program is a series of instructions, listed in much the same way as an assembly program. So for instance, some common operations are mathematical like adding, subtracting, multiplying and dividing values. Other operations can include jumping to a program label as well as calling or returning from separate functions.

## Conclusion

Now you should have a good overview of the Arduino Opta and its software and hardware features. 

### Next Steps

Now that you are familiar with some of the features of the Arduino Opta, you can take a look at some of our tutorials to start using the Opta.

- Getting started
- IDE tutorial
