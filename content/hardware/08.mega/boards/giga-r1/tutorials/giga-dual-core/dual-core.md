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

RPC is a method that allows programs to make requests to programs located elsewhere. It is based on the client-server model (also referred to as caller/callee), where the client (caller) makes a request to the server (callee). 

An RPC is a synchronous operation, and while a request is being made (client/caller) to another system, the operation is suspended. On return of the results, the operation is resumed. On the other side, (server/callee) performs the subroutine on request, and suspends any other operation as well. After it sends the result to the client, it resumes its operation, while waiting for another request.

![Request routine.]()

### RPCs in the Arduino Environment

As some microcontrollers, including the STM32H747XI, has two processors, it is possible to program them both to perform individual tasks, and enable communication between them via an RPC.

The advantage of this is great, as you essentially have "two" Arduino boards running (on the some board). For example, you can run a machine learning module on one of the core, while another core is connected to a network system such as the [Arduino IoT Cloud](). Running these applications in parallel increases performance, as you split the work load and allow them to run with less blocking code for example.

![Communication between cores]()

### RPC vs Multi-Threading

This is a similar, but not identical to [multi-threading on Arduino boards](https://github.com/arduino-libraries/Arduino_Threads). Multi-threading essentially allows you to run code asynchronously on a single processor, and create communication lines between the threads. While RPC is similar, it differs as communication can be set up between two remote systems (such as two different processors, in this case).

Both methods are great to apply in more sophisticated and performance-craving projects, as you can combine the two methods to create several threads, running on separate cores.

### Use Cases

RPC and Multi-Threading can be used for several different setups. Here are some good combinations that can be considered:

- Use **Core A** for networking (e.g. publishing to a MQTT channel) and **Core B** for data recording & analysis.
- Use **Core A** for image capturing, and **Core B** for image processing.
- Use **Core A** for storing sensor data locally (USB/SD) and **Core B** for streaming it to a cloud service.

## GIGA R1 RPC Example

The GIGA R1's STM32H747XI microcontroller includes the M7 and M4 core. In this example, we will:
- Install MicroPython on the M7 core (this is the main core).
- Load a script that sets up the **M7 as a server/callee**.
- Upload a sketch to the **M4 that sets it up as a client/caller**.  
- Make a request from the M4 to the M7.

### Installing MicroPython

To install MicroPython on the GIGA R1, you will need to flash a specific MicroPython firmware to the **M7 processor.** This requires the [dfu-util]() tool.

1. Download the [MicroPython firmware for GIGA R1]().
2. Download [dfu-util]() (also available via [brew.sh](https://formulae.brew.sh/formula/dfu-util)). Make sure the tool is added to your PATH on your machine.
3. Open a terminal, and navigate to the directory where you saved the downloaded MicroPython firmware.
4. Double tap the reset button on the GIGA R1 (while it is powered). This will enter bootloader mode.
5. Finally, load the MicroPython firmware, by using the following command:

```sh
dfu-util -w -a 0 -d 2341:0366 -D <firmware>.dfu
```

This will start an uploading process that can be tracked in the terminal. Once it is done, the green LED will be pulsing. Success!

Make sure to reset the board before continuing (tap the reset button).

### Flash M4

### Load MicroPython Script


### 


## Conclusion

Add a conclusion to what this tutorial has gone through. Connect back to what you wrote in the "Goals" section. 

