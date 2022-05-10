---
title: 'Powering Alternatives for Arduino Boards'

description: 'Learn more about the power pins and connectors of Arduino® boards in this article, their main characteristics, and how to use them correctly.'
tags: 
  - Power
  - 5V
  - 3V3
  - Vin
  - USB
  - Barrel jack
author: 'José Bagur, Taddy Chung, Karl Söderby'
---

Arduino boards can be powered in several ways; we can use dedicated **connectors** (USB ports and barrel jacks) or dedicated **pins**. One fundamental question that usually arises when using an Arduino board in real-life applications is what dedicated power connector or pin we should use. This article will describe the main characteristics and correct use of power pins and connectors of Arduino boards.

## Powering Alternatives


Arduino boards have **four** ways in which they can be powered:

1. Powering via USB connector

2. Powering via a barrel jack connector / JST connector if available on the board

3. Powering via the VIN (Voltage In) pin

4. Powering via the 3V3/5V pin*

***\*Powering your board via the 3V3/5V pins is not recommended, as it can damage your board's voltage regulator. Read more [here](#3v35v-pin).***


In this article, we will examine the alternatives to power your Arduino more in-depth.


## USB Connector


The most common and easiest way we can power an Arduino board is by using its **onboard USB connector**. The USB connector provides a regulated 5V line to power the board's electronics. However, it can also power external components via the 5V pin that can be found in Arduino boards, as shown in the image below:


Something important about the USB connection is the current rating of the USB host device. For example, a USB host device can be a computer; this means that the computer's USB port is the 5V power source of the Arduino board connected to it. Besides USB ports of computers, we can also use power banks, for example, as power sources for Arduino boards. Power banks usually have one or more USB outputs that provide regulated 5V lines at different current ratings. Arduino boards that run at 5V use the USB-regulated 5V line directly, boards that run at 3V3 regulate the 5V line from the USB connector to 3V3 using their onboard voltage regulator. Output current rating from the 5V pin will vary, depending on the 5V power source.   


***Current from USB ports of computers is usually limited to 500mA.***


## Barrel Jack Connector


Some Arduino boards have an **onboard barrel jack connector** that is used to connect external power supplies. The Arduino boards with an onboard barrel jack connector are the following:


- [Arduino UNO Rev3](https://store.arduino.cc/collections/boards/products/arduino-uno-rev3)
- [Arduino UNO WiFi Rev2](https://store.arduino.cc/collections/boards/products/arduino-uno-wifi-rev2)
- [Arduino Leonardo](https://store.arduino.cc/collections/boards/products/arduino-leonardo-with-headers) 
- [Arduino Mega 2560 Rev3](https://store.arduino.cc/collections/boards/products/arduino-mega-2560-rev3)
- [Arduino Due](https://store.arduino.cc/collections/boards/products/arduino-due)
- [Arduino Zero](https://store.arduino.cc/collections/boards/products/arduino-zero)


***Arduino boards with onboard barrel jacks are configured with positive polarity; this means a negative sleeve and a positive pin. They use a a negative 5.5mm sleeve and a 2.1mm positive pin***


The voltage line from the barrel jack connector is regulated in Arduino boards using their onboard voltage regulator; usually, it is first regulated to 5V and then regulated again to 3V3 in most Arduino boards. The recommended voltage and current ratings for external regulated power supplies connected to the barrel jack connector are summarized in the table below:


|          Board         | External Power Supply Voltage (V) | External Power Supply Current (A) |
|:----------------------:|:---------------------------------:|:---------------------------------:|
|    Arduino UNO Rev3    |                7-12               |                 1                 |
|  Arduino UNO WiFi Rev2 |               4.5-21              |                1.5                |
|    Arduino Leonardo    |                7-12               |                 1                 |
| Arduino Mega 2560 Rev3 |                7-12               |                 1                 |
|       Arduino Due      |               4.5-21              |                1.5                |
|      Arduino Zero      |                3-20               |                 1                 |


 ## VIN Pin


The VIN pin in Arduino boards is a power pin with a dual function. This pin can work as a **voltage input for regulated external power supplies** that do not use a barrel jack connector. This pin can also work as a **voltage output when an external power supply is connected to the barrel jack connector** present in some Arduino boards. An important consideration is that the Vin pin is connected directly to the input pin of the onboard voltage regulator on Arduino boards. Since the VIN pin is directly connected to the voltage regulator, the **VIN pin does not have reverse polarity protection**. 


***Use the VIN pin carefully to avoid damaging your Arduino board since it does not have reverse polarity protection.***


The **minimum and maximum voltages** that can be applied to the VIN pin are determined by the onboard voltage regulator on Arduino boards, varying from board to board. Those voltages are summarized in the table below:


|      **Board**      | **VIN Minimum Voltage (V)** | **VIN Maximum Voltage (V)** |
|:-------------------:|:---------------------------:|:---------------------------:|
|       UNO Mini      |             4.5             |              21             |
|       UNO Rev3      |              7              |              12             |
|    UNO WiFi Rev2    |              7              |              12             |
|     UNO Rev3 SMD    |              7              |              12             |
|       Leonardo      |              7              |              12             |
|    Mega 2560 Rev3   |              7              |              12             |
|        Micro        |              7              |              12             |
|         Zero        |              3              |              20             |
|     Portenta H7     |             4.1             |              6              |
|   Nicla Sense ME    |             3.4             |             5.5             |
| Nano RP2040 Connect |              3              |              22             |
|     MKR NB 1500     |             3.9             |              17             |
|    MKR Vidor 4000   |             3.9             |              17             |
|    MKR WiFi 1010    |             3.9             |              17             |
|       MKR Zero      |             3.3             |             5.5             |
|     MKR1000 WIFI    |             4.5             |              21             |
|     MKR WAN 1300    |             3.3             |             5.5             |
|     MKR WAN 1310    |             3.3             |             5.5             |
|         Nano        |              7              |              12             |
|      Nano Every     |             4.5             |              21             |
|     Nano 33 IoT     |             4.5             |              21             |
|     Nano 33 BLE     |             4.5             |              21             |
|  Nano 33 BLE Sense  |             4.5             |              21             |


## 3V3/5V Pin 


3V3 and 5V pins are also power pins with a dual function. They can work as **power outputs** since these pins are directly connected to the onboard 3V3 and 5V voltage regulators outputs (depending on the board). Moreover, 3V3 and 5V pins can also be used as **power inputs if no regulated power supply is connected through the other power inputs (USB port, barrel jack connector or VIN pin)**.


***Since 3V3 and 5V pins are directly connected to the onboard's 3V3 and 5V voltage regulators outputs, these pins have no reverse polarity protection. Use them carefully when working as power inputs to avoid damaging your board's voltage regulator.***


Although 3V3 and 5V pins can be used as power inputs, **it is not recommended** if no power supply is connected through the USB port, the barrel jack connector, or the VIN pin. 3V3 and 5V pins are connected directly to the onboard voltage regulator's output pin. Suppose the voltage in the voltage regulator output pin becomes higher than the input voltage of the voltage regulator. In that case, a large current may flow into the voltage regulator from its output pin to its input pin. That large current can permanently damage your board's voltage regulator.


***It is safe but not recommended to apply a voltage to the 3V3 or 5V pins that are not higher than the input voltage of the voltage regulators.*** 


The **maximum current** drawn from the 3V3 and 5V pins are summarized below. Notice that this current can be provided by the 3V3 and 5V onboard voltage regulators or from the power source connected to the board:


|      **Board**      | **Vin Minimum Voltage (V)** | **Vin Maximum Voltage (V)** |
|:-------------------:|:---------------------------:|:---------------------------:|
|       UNO Mini      |             4.5             |              21             |
|       UNO Rev3      |              7              |              12             |
|    UNO WiFi Rev2    |              7              |              12             |
|     UNO Rev3 SMD    |              7              |              12             |
|       Leonardo      |              7              |              12             |
|    Mega 2560 Rev3   |              7              |              12             |
|        Micro        |              7              |              12             |
|         Zero        |              3              |              20             |
|     Portenta H7     |             4.1             |              6              |
|   Nicla Sense ME*   |             3.4             |             5.5             |
| Nano RP2040 Connect |              3              |              22             |
|     MKR NB 1500     |             3.9             |              17             |
|    MKR Vidor 4000   |             3.9             |              17             |
|    MKR WiFi 1010    |             3.9             |              17             |
|       MKR Zero      |             3.3             |             5.5             |
|     MKR1000 WIFI    |             4.5             |              21             |
|     MKR WAN 1300    |             3.3             |             5.5             |
|     MKR WAN 1310    |             3.3             |             5.5             |
|         Nano        |              7              |              12             |
|      Nano Every     |             4.5             |              21             |
|     Nano 33 IoT     |             4.5             |              21             |
|     Nano 33 BLE     |             4.5             |              21             |
|  Nano 33 BLE Sense  |             4.5             |              21             |