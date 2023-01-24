---
tags: [Ethernet]
author: Arduino
title: 'Ethernet Shield Sending and Receiving String via UDP'
description: 'Send and receive text strings via UDP.'
---

[Tutorials](https://arduino.cc/en/Tutorial/HomePage) > [Examples](https://arduino.cc/en/Tutorial/LibraryExamples) > Ethernet > UDPSendReceiveString

In this example, you will use your Ethernet Shield and your Arduino to send and receive text strings via the UDP protocol (Universal Datagram Packet). You'll need another device to send to and from.  The [Processing](http://www.processing.org) sketch included at the end of the code will send to and receive from your Arduino running this example.

## Hardware Required

- Arduino Board

- [Arduino Ethernet Shield](/hardware/ethernet-shield-rev2)

## Circuit

The Ethernet shield allows you to connect a WIZNet Ethernet controller to the Arduino boards via the SPI bus. It uses the ICSP header pins and pin 10 as chip select for the SPI connection to the Ethernet controller chip. Later models of the Ethernet shield also have an SD Card on board. Digital pin 4 is used to control the chip select pin on the SD card.

The shield should be connected to a network with an Ethernet cable.  You will need to change the network settings in the program to correspond to your network.

![The circuit for this tutorial.](assets/EthernetShieldF_bb.png)

Image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

***In the above  image, the Arduino board would be stacked below the Ethernet shield.***

## Schematic

![The schematic for this tutorial.](assets/EthernetShield_sch.png)

## Code

<iframe src='https://create.arduino.cc/example/library/ethernet_2_0_0/ethernet_2_0_0%5Cexamples%5CUDPSendReceiveString/UDPSendReceiveString/preview?embed' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

## Processing Code

Copy the Processing sketch from the code sample above. When you type any letter in the Processing sketch window, it will send a string to the Arduino via UDP.


**Last revision 2018/09/07 by SM**
