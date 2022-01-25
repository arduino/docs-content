---
slug: '/en/Tutorial/LibraryExamples/WiFiChatServer'
date: 'February 05, 2018, at 08:43 PM'
title: 'WiFi Chat Server'
description: 'Set up a simple chat server with the WiFi Shield.'
---

A simple server that distributes any incoming messages to all connected clients.  To use, open a terminal window, telnet to your WiFi shield's IP address, and type away.  Any incoming text will be sent to all connected clients (including the one typing). Additionally, you will be able to see the client's input in your Arduino Software (IDE) serial monitor as well.

## Hardware Required

- Arduino WiFi Shield

- Shield-compatible Arduino board

## Circuit

The WiFi shield uses pins 10, 11, 12, and 13 for the SPI connection to the HDG104 module. Digital pin 4 is used to control the chip select pin on the SD card.

You should have access to a 802.11b/g wireless network that connects to the internet for this example. You will need to change the network settings in the sketch to correspond to your particular networks SSID.

For networks using WPA/WPA2 Personal encryption, you need the SSID and password. The shield will not connect to networks using WPA2 Enterprise encryption.

WEP network passwords are hexadecimal strings known as keys. A WEP network can have 4 different keys; each key is assigned a "Key Index" value. For WEP encrypted networks, you need the SSID, the key, and key number.

![](assets/WiFiShield_bb.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

***In the above image, the Arduino board would be stacked below the WiFi shield.***

## Code

<iframe src='https://create.arduino.cc/example/library/wifi_1_2_7/wifi_1_2_7%5Cexamples%5CWiFiChatServer/WiFiChatServer/preview?embed' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>


*Last revision 2018/08/23 by SM*
