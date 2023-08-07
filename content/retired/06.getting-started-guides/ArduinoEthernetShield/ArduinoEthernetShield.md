---
title: 'Getting Started with the Arduino Ethernet Shield.'
description: 'The first steps to setting up the Arduino Ethernet Shield'
---

**The Ethernet Shield is a retired product. The Arduino Ethernet Shield Rev2 is available to buy. See [documentation for Ethernet Shield Rev2](/hardware/ethernet-shield-rev2).**

The **Arduino Ethernet Shield** allows an Arduino board to connect to the internet using the [Ethernet library](https://www.arduino.cc/reference/en/libraries/ethernet/) and to read and write an SD card using the [SD library](https://www.arduino.cc/reference/en/libraries/sd/). This shield is fully compatible with the former version but relies on the newer W5500 chip.

### Connecting the Shield

![](./assets/A000024-Arduino-Eth-Shield-2-3tri.jpg)

To use the shield, mount it on top of an Arduino board (e.g. the Uno). To upload sketches to the board, connect it to your computer with a USB cable as you normally would. Once the sketch has been uploaded, you can disconnect the board from your computer and power it with an external power supply.

Connect the shield to your computer or a network hub or router using a standard ethernet cable (CAT5 or CAT6 with RJ45 connectors). Connecting to a computer may require the use of a cross-over cable (although many computers, including [all recent Macs](https://web.archive.org/web/20191015221518/https://support.apple.com/en-us/HT2274) can do the cross-over internally).

### Tutorials

***All tutorials for the Ethernet Shield can be found in the [Ethernet Shield Rev2 Tutorials](https://docs.arduino.cc/hardware/ethernet-shield-rev2#tutorials) section.***

You may also find inspiration in our [Project Hub](https://create.arduino.cc/projecthub/products/arduino-ethernet-shield-2) tutorial platform with some projects developed by our users

<iframe frameborder='0' height='410' scrolling='no' src='https://create.arduino.cc/projecthub/ThereIsNoTry/water-leakage-detector-and-valve-control-f45048/embed?use_route=project' width='354' style='margin-top:30px'></iframe>

### Network Settings

The shield must be assigned a MAC address and a fixed IP address using the [Ethernet.begin()](https://www.arduino.cc/reference/en/libraries/ethernet/ethernet.begin/) function. A MAC address is a globally unique identifier for a particular device. Current Ethernet shields come with a sticker indicating the MAC address you should use with them. For older shields without a dedicated MAC address, inventing a random one should work, but don't use the same one for multiple boards. Valid IP addresses depend on the configuration of your network. It is possible to use DHCP to dynamically assign an IP to the shield. Optionally, you can also specify a network gateway and subnet.

### SD Card

The latest revision of the Ethernet Shield includes a micro-SD card slot, which can be interfaced with using the [SD library](https://www.arduino.cc/reference/en/libraries/sd/).

The text of the Arduino getting started guide is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). Code samples in the guide are released into the public domain.
