---
title: 'Using BLE, WiFi and Ethernet on the Arduino Opta'
description: 'Learn how to make use of the Arduino Opta's connectivity features'
tags:
  - Wi-Fi
  - Ethernet
  - BLE
author: 'Benjamin Dannegård'
software:
  - Arduino IDE
hardware:
  - hardware/
---

## Overview

The Arduino® Opta is a powerful PLC device that has many features, allowing you to customize its use for your solution. Among these features are the standard connectivity features Wi-Fi®, Ethernet and Bluetooth®. In this tutorial we will go through how to use these features with the Arduino IDE and the Arduino Opta.

## Goals

- Learn how to use Bluetooth® Low Energy on the Opta
- Learn how to use Wi-Fi® on the Opta
- Learn how to use Ethernet on the Opta

### Required Hardware and Software

- USB-C cable (either USB-C to USB-A or USB-C to USB-C)
- Wi-Fi Access Point with Internet Access
- Arduino Opta
- Ethernet cable

## Instructions

Using the Arduino IDE we can easily work with these peripherals. Some features have their own library that we can make use of. First we need to install the appropriate core for the Arduino Opta, go into the **Board manager** and search for **Opta Mbed core**. When the latests version of the core is installed we can move on to trying out the connectivity options.

### Wi-Fi®

The files necessary for using the Wi-Fi® on the Opta are included in the core. To try it out we can go to **Flie > Examples**, under **Examples for Opta** we can find the **WiFi** section, inside there is an example sketch **WiFiWebClient**. Open this example sketch and fill out the WiFi details in the **arduino_secrets.h** tab. The sketch will make the Opta connect to whatever website is entered into the ``char server[] = "example.com";`` variable. If the connection is successful it will then print the websites HTML content to the serial monitor. If the sketch ran successfully the output should look like the image below.

![Running WiFi sketch on the Opta in the Arduino IDE](assets/opta-wifi.png)

If you want to take a deeper look at what features the **WiFi** library has to offer, please go [here](https://www.arduino.cc/reference/en/libraries/wifi/).

### Ethernet

The files necessary for using Ethernet on the Opta are included in the core. To try it out we can go to **Flie > Examples**, under **Examples for Opta** we can find the **Ethernet** section, inside there is an example sketch **WebClient**. Connect the Ethernet cable to the Arduino Opta then try and upload the example. This example will function the same way as the one mentioned in the Wi-Fi® section. The device will connect to the website stated in the sketch and print the websites HTML content in the serial monitor.

If you want to take a deeper look at what features the **Ethernet** library has to offer, please go [here](https://www.arduino.cc/reference/en/libraries/ethernet/).

### Bluetooth® Low Energy

To use the Bluetooth® feature, download the **ArduinoBLE** library in the Arduino IDE. Go into the **library manager** and search for **ArduinoBLE**, if you cant find it try to sort by official libraries published by Arduino. Let's now try and run a simple example sketch from the ArduinoBLE library, a sketch that will scan for other Bluetooth® devices within range. The sketch will then print the found devices address, local name and the advertised service UUIDs, if present. You can find the example under **File > Examples > ArduinoBLE > Central**, the sketch is called **Scan**. When the sketch is running on the Opta the output on the serial monitor should look something like the image below.

![Bluetooth® sketch running on the Opta](assets/opta-ble.png)

If you want to take a deeper look at what features the **ArduinoBLE** library has to offer, please go [here](https://www.arduino.cc/reference/en/libraries/arduinoble/).

## Conclusion

Now you have a better overview of the connectivity features on the Arduino Opta and how to use them. We went through how to use the different connectivity features and what libraries are required for them. By running all the example sketches on our device we have made sure that the modules are all working and everything is up to date. 

### Next Steps

Now that you know how to use the connectivity features of the device, have a look at our other tutorials and try to combine the different features. The Opta uses the same architecture as the Portanta H7, it could therefor be a good idea to take a look at the Portenta H7 tutorials. Such as the using your [device as a Wi-Fi® access point tutorial](https://docs.arduino.cc/tutorials/portenta-h7/wifi-access-point) or the (Bluetooth® Low Energy connectivity with a phone tutorial)[https://docs.arduino.cc/tutorials/portenta-h7/ble-connectivity].
