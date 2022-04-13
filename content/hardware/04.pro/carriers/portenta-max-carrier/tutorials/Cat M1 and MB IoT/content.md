---
title: 'Using NB-IoT or Cat-M1 with the Portenta Max Carrier'
difficulty: easy
description: "Learn how to connect the Portenta Max Carrier to the internet with NB-IoT or Cat-M1 technology"
tags:
  - Installation
  - CATM1
  - NBIOT
author: 'Benjamin Dannegård'
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04pro/carriers/portenta-max-carrier
  - _snippets/hardware/sim-card
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Introduction 

The Portenta Max carrier adds a lot of functionality to the Portenta H7. With the Portenta Max Carrier it is possible to use NB-IoT and Cat-M1 technology. In this tutorial we will show to connect to GSM with the Portenta Max carrier and the Portenta H7.

***Note: This tutorial was created in Sweden, and as a result, the available networks are only Swedish network operators. The results will vary depending on what location you are in.***

## Goals

The goals of this project are:

- Learn how to connect the board and the carrier.
- Connect to the GSM network with Cat-M1 or NB-IoT.
- Print HTML content in the Serial Monitor.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [Portenta H7](https://store.arduino.cc/products/portenta-h7)
- Antenna with GSM 850 / 900 / 1800 / 1900 MHz range and the ability to connect via SMA
- DC 4.5-20V power supply with barrel jack.
- [Portenta Max carrier](https://store.arduino.cc/products/portenta-max-carrier)

## Instructions

### Circuit

For this tutorial we need to plug the Portenta H7 into the Max Carrier, like shown in the image below.

![Connecting the Portenta H7 and Max Carrier](assets/Connect-H7-to-Max-carrier.svg)

And we also need to insert a SIM card and connect an antenna to the Max Carrier, like shown in the image below.

![SIM card slot and antenna connector](assets/Sim-card-and-antenna-on-Max-carrier.png)

After everything else is connected, connect a power cable to the barrel jack. The one right next to the antenna connector.

### Arduino IDE

Make sure you have the latest **Portenta mbed os Core** installed. Found in **Tools > Board: > boards manager...**.

We will also need to libraries to be installed, **MKRNB** and **arduino_bq24195**. You can find these in the **Library manager** in the Arduino IDE. We will be using example sketches from the **MKRNB** library.

### NB-IoT or Cat-M1

NB-IoT is a radio technology deployed over mobile networks which is especially suited for indoor coverage, low cost, long battery life, and large number of devices. While Cat-M1 supports downlink and uplink speeds up to 1 Mbps with a latency of 50 to 100 ms and can be used for realtime-communication. Cat-M1 is ideal if you are interested in tracking things such as logistics and transportation. Make sure the technology that you choose is supported by your service provider.

### Switching between NB-IoT and Cat-M1

If you prefer to use one communication technology over the other, then this can be changed with the simple use of one sketch. Open the **ChoseRadioAccessTechnology** sketch located in the libraries examples. When this sketch is uploaded open the serial monitor. You will now get options for what technology you prefer to use in the serial monitor. Follow the steps and wait for the sketch to say that it is finished. The board will now use the preferred technology and we can move on to upload other sketches.

[Serial monitor for sketch]()

### Programming the Board

Now open the sketch from examples **NBWebClient**. This sketch will connect the Portenta Max carrier to a website and print its content in the serial monitor.

First go to the **arduino_secrets.h** tab and enter your PIN code into the **Secret_pinnumber** variable.

The **char server[]** variable will decide what website the board will connect to and print in the serial monitor. Feel free to try different sites and see the difference in the result. In this tutorial we will use the default **example.org**.

The sketch will also set the port it uses for connecting with **int port = 80;**. This is the default connection port, but if the connection is not being established. Or if you know the specific port you want to connect to, then change this variable to a more appropriate value.

### Result of Sketch

When the sketch is uploaded open the serial monitor to see the result. You will also get error messages in the serial monitor if there is some issue along the way. When it works you should see something similar to what is shown below.

[Result in the serial monitor]()

### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- We have entered the wrong pin number.
- We are out of coverage (no signal). You can run the example sketch **Scan available networks** to see if there is coverage.
- SIM card may not be activated.

## Next Step

- The Portenta Max Carrier offers a lot of features when used with the Portenta H7. If you want to learn more about the Portenta Max Carriers peripherals and features, check out our [Getting Started guide for Max Carrier and Portenta H7]().

- If you are interested in trying out more of the Max Carriers connectivity options. Be sure to check out our tutorial on how to use [LoRa with the Max Carrier and Portenta H7]().

## Conclusion

In this tutorial we went through how to connect all the necessary parts to the Portenta Max Carrier. How to change whether to use NB-IoT or Cat-M1. To then connect to a website and print it's content in the serial monitor.