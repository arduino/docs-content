---
title: "Modbus communication serial protocoll"
description: "Learn about the Modbus "
author: "Hannes Siebeneicher"
---

***Controller/peripheral is formerly known as master/slave. Arduino no longer supports the use of this terminology. Devices formerly known as master are referred to as controller and devices formerly known as slaves are referred to as peripheral.***

## What is Modbus?
Modbus is an open serial communication protocol used for transmitting information over serial lines between electronic devices. It was originally published by Modicon (now Schneider Electric) in 1979. The Modbus protocol is the oldest and by far the most popular automation protocol in the field of process automation. It enables devices, such as energy meters or humidity sensors connected to the same network to communicate the results to a supervisory computer or a Programmable Logic Computer (PLC). Several versions of the Modbus protocol exist for the serial port and Ethernet and the most common are Modbus RTU, Modbus ASCII, Modbus TPU and Modbus Plus. It is based on a controller peripheral architecture and communication between nodes is achieved with send request and read response type messages. Modbus communicates over several types of physical media such as RS-232 and over Ethernet. The original Modbus interface ran on RS-232 serial communication but most the later Modbus implementations us RS-485 because it allows for longer distancer, higher speeds and the possibility of multiple devices on a single multi-drop network. The communication over serial RS-485 physical media works with two-wire transmit and receive connections. (SEE TWO WIRE TUTORIAL)

On simple interfaces like RS-485 and RS-232 the Modbus messages are sent in plain form over the network and the network will be dedicated to only Modbus communication. However, if your network requires multiple heterogeneous devices using a more versatile system like TCP/IP over ethernet, the Modbus messages are embedded in Ethernet packets with the format prescribed for this physical interface. In this case Modbus and other types of mixed protocols can co-exist in the same physical interface at the same time. The main Modbus message structure is peer-to-peer, but it can also function on point to point and multidrop networks. As mentioned, the Modbus protocol communicates using a controller / peripheral technique in which only one device can initiate transactions, called queries. 
The next part will go into more detail how the communications is done between controller and peripheral device.

## How does Modbus work?
Each Modbus message has the same structure. Four basic elements are present in each message and the sequence and order of these elements are the same for all messages. This allows for easy parsing of the content. The conversation is always started by the controller and when a message is sent by the controller, depending on the message the peripheral interprets the message and responds to it. Physical peripheral addressing in the message header is used to define which peripheral device should respond to a message, while all other nodes ignore the message if the address field does	not match their own address. 
Modbus functions perform read and write instructions to the peripheral’s internal memory registers to configure, monitor and control the peripheral’s inputs and outputs. Modbus devices will typically include a register map outlining where the configuration input and output data can be written and read from. You should always refer to the peripheral’s register map of your device to gain a better understanding of its overall operation. The Modbus data model has a simple structure described in four basic data types:
-	Discrete Inputs 
-	Coils Output
-	Input Registers (Input Data)
-	 Holding Registers (Output Data)
The service request area of the message or Modbus Protocol Data Unit or PDU is comprised of a function code and a number of data bytes requested by the controller. The Modbus memory registers of a device are organized around the four basic data reference types and this data type is further identified by the leading number used in the devices memory address, such as, a 0 based register referencing a message to Read or Write discrete outputs or coils, or a 1 based register referencing Reading discrete inputs, or a 3 based register referencing Reading input registers, and a 4 based register referencing Reading or Writing to output or holding registers. The function code field specifies which register data group it reads or writes to and from the peripheral.
SHOW IMAGE OF FUNCTION CODE

