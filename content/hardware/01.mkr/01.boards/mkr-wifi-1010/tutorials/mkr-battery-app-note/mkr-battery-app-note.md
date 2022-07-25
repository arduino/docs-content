---
title: 'Understanding Battery Selection for the MKR boards'
difficulty: intermediate
description: 'Choose the correct battery for you MKR application.'
tags:
  - Battery
  - MKR
  - 
author: 'Ali Jahangiri'
hardware:
  - hardware/01.mkr/01.boards/mkr-wifi-1010
software:
  - Arduino IDE 2.x
---

## Introduction

While you can run your MKR board from USB, you can make best use of it when your MKR board is able to operate independantly of your computer and a USB cable. This is particulary useful for many IoT applications, use of relays with high current draw and remote sensing. Batteries can help us in this regard and a special connector is included in the MKR products for this end. In this application note, we will take a closer look at the battery capabilities of the MKR boards. 

### Goals
The goals of this project are:
- Understand what the terms `charging capacity` and `charging current`
- Distinguish between LiPo and Li-Ion batteries
- Learn how to identify connector polarity
- Understand how the SAMD chip reads battery voltage via a voltage divider
- Export data to the Arduino IoT CLoud to read values in real time

### Hardware & Software Needed
- [Arduino MKR WiFi 1010](https://store.arduino.cc/products/arduino-mkr-wifi-1010)
- Multimeter
- IDE 2.0
- LiPo battery with JST-PH connector
- Arduino IoT Cloud

### LiPo vs Fe vs Li-ion batteries
Several different chemistries of rechargeable batteries are commerically avalible. The two main types are Li-Po and Li-Ion. Lithium Ion batteries have been around for a longer time and are generally cheaper. Lithium Polymer batteries have a higher energy density, allowing you to run your board for longer with a similar sized battery. 
You can see a comparison between these three in the table below.

| Battery Chemistry | Cost   | Energy Density (mass) | Energy density (size) | Stability | Nominal voltage (single cell) |
|-------------------|--------|-----------------------|-----------------------|-----------|-------------------------------|
| LiPo              | Higher | higher                | lower                 | Higher    | 3.7V                          |
| Li-ion            | Lower  | Lower                 | Higher                | Lower     | 3.7V                          |

***While other battery rechargeable types exist, these two chemistries (Li-Ion and LiPo) are the most commonly relavent.***

Apart from being a single cell (3.7V), a key factor to selecting the correct battery is that the connector is compatible.

### Connector
You can connect a battery to the MKR WIFI 1010 via a 2-pin JST-PH female connector. The PH varient of JST connectors are identified by a pin-to-pin distance of 2 mm. Here are several examples of LiPo batteries with a 2-pin JST-PH connector:
- LiPo 3.7V 750mAh https://www.electrokit.com/produkt/batteri-lipo-3-7v-750mah

You can either buy one commercially connected to the battery, or alternatively, connect it yourself.
- JST-PH Female Connector Housing https://se.rs-online.com/web/p/wire-housings-plugs/8201466
- JST-PH Female Crimp Terminal

Each individual connector is made of one plastic housing and two metal crimp terminals. A crimping device may be required.

[Add graphic]

### Electrical Properties

**Voltage**
The nominal voltage of both LiPo and Li-Ion batteries is around 3.7V and is commonly refered to as the voltage of single cell batteries. However, this is an ideal scenario since as a battery is used the voltage changes. We can see this represented in the image below. The voltage can be considered similar to a waterfall. The higher the waterfall, the higher the voltage.

![Battery Discharge Curve](assets/batteryDischargeCurve.jpg)

In the MKR boards, the battery terminal is connected to the SAMD21 via a reserved pin (PB09) known as `ADC_BATTERY` within the Arduino Core. Since the voltage of a Li-ion battery exceeds 3.3V (the AREF value), a voltage divider must be used to extend the range while also ensure that only safe voltages are applied to the microcontroller. We can calculate the output voltage using the following formula

$$ V_{out} = \frac{V_{source} \ times R2} {R_1 + R_2} $$

In the MKR WIFI 1010, $R_1$ and $R_2$ are 330k ohm and 1M ohm respectively. Therefore, for a resolution of 12 bits, the board is subject to 3.3V that corresponds to about 4.39V on the battery side. Therefore, we can cover the operating value of a whole battery. The high values reduce the leakage current that may pass throught, increasing the life of the battery. 

[Add graphic]

**Capacity**
Continuing with the waterfall analogy, the volume of water passing through a waterfall represents the current. Therefore, the amount of water stored behind the waterfall is considered the capacity. It is common to discuss the capacity in terms of milliamp hours (mAh), which is the current that can be potentially extracted in an hour to discharge it. Note that changes in temperature and elevated current demands can change the effective capacity of your battery.

While the MKR boards do not provide a mechanism for identifying capacity, we can get a general idea of the current status by mapping the voltage to the capacity. A more precise value can be obtained with the help of a fuel gauge IC, avaliable in the Portenta X8 and H7.

**Discharge rating**
When the battery is fully charged, or when it is near to discharge the discharge rate changes considerably. Yet, there is a region where the discharge rate constant (change in voltage over change in discharge capacity does not flunctuate). Within this region, the maximum current draw is defined as:

$$\text{maximum current draw } = \text{ battery capacity } \times \text{ discharge rating} $$

The discharge rating (C) is often provided in the datasheet of the battery. If the C rating of a battery is 1, then it can discharge the maximum current for one hour before running out. As a rule of thumb, higher discharge rates lead reduce the effective capacity and lifetime of the battery. 

## Measure battery locally

**0.** Test the battery voltage with a multimeter. It should be between 3.3V and 4.2V. Also, try to connect it then see what the 5V, VCC and AREF are. 

**1.** Connect a battery to the MKR Motor Carrier. We have used a 1200 mAh LiPo battery with a JST connector. Most commerical batteries have a JST connector, although the MKR board is not limited to LiPo batteries and Li-ion is also acceptable. You can also test to see the 

**2.** We will create a sketch to read the ADC voltage that is sensed by the SAMD controller. . 

**3.** Now we will change the sketch to account for the voltage divider.

**4.** We will try to approximate the capacity of the battery with the help of a simple mapping function. However, since the internal arduino function is limited to int, we will do it ourselves. 

## Measure battery voltage via the Arduino IoT Cloud

**1.** In order to evaluate the performance of the device in a real world setting, we need to be able to test it remotely. To do so, we will use the Arduino Cloud to transfer data. The Arduino cloud makes it easy ton create IoT solutions. In the free plan, you have to connect the board to the cable, but in the money money tier, you can program the board wirelessley.

**2.** First, we will create a simple digital output to display the value of the ADC.

**3.** Next we will use a graph to plot the voltage calues, when the voltage divider is accounted for.

**4.** Finally, we will display the end result with the help of a percent output thing

## Extract plots

**1.** Extract historical data from the online dashboard

**2.** Plot with Google Sheets

after i the usb port, the battery is disconnected as well? I have to reconnect battery for it to work? How are you supposed to charge it in a practical setting 

### Troubleshoot
- You cannot upload OTA with 

## Conclusion

## Further Ideas

- An averaging function is used to increase the stability of the values obtained
- Evaluate the performance of a sketch and compare how the voltage falls for various loads and frequencies
- Use the BatterySense library to get a better approximation of the battery capacity
- Use the Arduino Portenta series to have access to a onboard fuel guage.
- Try calculating the discharge rating in the linear region

## References
battery charge level is tied to the voltage. don't need a table, but have explanation. depending on a battery used. from 4.2 to 4.0 and from 3.5 to 3.3 very little energy is released.