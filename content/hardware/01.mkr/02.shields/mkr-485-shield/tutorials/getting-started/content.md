---
slug: '/en/Guide/MKR485Shield'
date: 'February 05, 2018, at 08:43 PM'
title: 'Getting Started with the MKR 485 Shield'
tags:
    - RS485
author: 'Arduino'
---

The [MKR 485 shield](https://store.arduino.cc/arduino-mkr-485-shield) allows a MKR board to connect to other 485 devices.

This board may be used with the [Arduino RS485](/en/Reference/ArduinoRS485) and the [Arduino Modbus](/en/ArduinoModbus/ArduinoModbus) libraries, available from the Library Manager.

### Usage Notes

The Arduino MKR 485 Shield allows the Arduino MKR family of boards to communicate with industrial automation systems or to extend the serial wired communication over much longer range. This shield supports half and full duplex with or without biasing and termination, master slave configuration.

Most of these configurations are physical and the 3 ways dip switch allows you to set up the connection properly.

| Switch No. | ON                   | OFf            |
| ---------- | -------------------- | -------------- |
| 1          | Termination on A-B\* | NO termination |
| 2          | FULL Duplex\*        | HALF Duplex    |
| 3          | Termination on Y-Z\* | NO termination |

(* Factory configuration)

![The MKR 485 Shield](assets/MKR485_featured.jpg)

### Tutorials

Now that you have a basic knowledge of the shield, you may find inspiration in our [Project Hub](https://projecthub.arduino.cc/) tutorial platform.

<iframe frameborder='0' height='410' scrolling='no' src='https://create.arduino.cc/projecthub/123325/monitor-your-energy-bill-via-modbus-mkr-wifi-1010-and-rs485-814e5e/embed?use_route=project' width='354' style='margin-top:30px'></iframe>

This shield may be used with the libraries already available for 485 communication.

### PIN Usage

This shield is compatible with the MKR family of Arduino boards.

| Pin number | Usage | Notes    |
| ---------- | ----- | -------- |
| A4         | RE    |          |
| A5         | DE    |          |
| 13         | RX    | Reserved |
| 14         | TX    | Reserved |

