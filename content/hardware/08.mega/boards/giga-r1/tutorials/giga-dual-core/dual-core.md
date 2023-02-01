---
title: Dual Core Processing with GIGA R1
description: 'Learn how to setup and control the M7 and M4 cores, and how to communicate between them using RPC.'
author: Karl Söderby
tags: [Dual Core, RPC, MicroPython]
---

The GIGA R1's microcontroller, the **STM32H747XI** has two processor cores, the **M7** and **M4**, clocking in at 480MHz and 240Mhz respectively. 

Having two cores in a microcontroller brings a significant advantage, to run two main applications simultaneuously, and communicate with them through something called **Remote Procedure Call (RPC)**.


## Goals

In this tutorial, we will take a closer look at how to make use of the dual core, by:
- Running MicroPython on the M7 core.
- Running Arduino code on the M4 core.
- Set up a communication line between the two cores through RPC.

## Hardware & Software Needed

Hardware needed:

- [GIGA R1]() / [GIGA R1 WiFi]()

For programming the M4 core (C++):

- [Arduino IDE](https://www.arduino.cc/en/software)

For programming the M7 core (MicroPython):

- [dfu-util](https://dfu-util.sourceforge.net/)
- [firmware.dfu](linktofw)

***The installation for `dfu-util` varies between operation systems. For installation using [brew.sh](https://formulae.brew.sh/formula/dfu-util) simply use `brew install dfu-util`.***

## Remote Procedure Call (RPC)

RPC is a communication protocol that allows programs to make requests to programs located elsewhere. It is based on the client-server model, where the client makes a request to the server. 




## Conclusion

Add a conclusion to what this tutorial has gone through. Connect back to what you wrote in the "Goals" section. 

