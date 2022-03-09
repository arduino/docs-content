---
title: ''
difficulty: easy
description: ""
tags:
  - Installation
  - CATM1
  - NBIOT
author: 'Benjamin Dannegård'
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04pro/carriers/portenta-max-carrier
  - _snippets/hardware/dipole-antenna
  - _snippets/hardware/sim-card
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Introduction 

With the Portenta Max Carrier it is possible to use NB IoT and Cat M1 technology. 

***Note: This tutorial was created in Sweden, and as a result, the available networks are only Swedish network operators. The results will vary depending on what location you are in.***

## Goals

The goals of this project are:

- Learn how to connect the board and the carrier.
- Connect to the GSM network with Cat-M1 or NBIoT.
- Print HTML content in the Serial Monitor.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [Portenta H7](https://store.arduino.cc/products/portenta-h7)
- [Dipole Antenna](https://store.arduino.cc/antenna) (or equivalent product with the same frequency range).
- [Portenta Max carrier]()

## Instructions

### Circuit

For this tutorial we need to plug the Portenta H7 into the Max Carrier, like shown in the image below.

[Connecting the Portenta H7 and Max Carrier]()

And we also need to insert a SIM card and connect an antenna to the Max Carrier, like shown in the image below.

[SIM card slot and antenna connector]()

### Arduino IDE

Make sure you have the latest Portenta mbed os Core installed. Found in **boards manager...**.

We will also be using an example sketch from the MKRNB library, make sure this library is installed. It can be found inside the Library manager in the Arduino IDE.

### Programming the Board

Now open the sketch from examples **NBConnection** 


### Result of Sketch

When the sketch is uploaded open the serial monitor to see the result. 

### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- We have entered the wrong pin number.
- We are out of coverage (no signal). You can run the example sketch **Scan available networks** to see if there is coverage.
- SIM card may not be activated.

## Next Step


## Conclusion

In this tutorial we went through how to connect everything with the Portenta Max Carrier to be able to utilize NB IoT / Cat M1. 