---
title: 'Arduino UNO R4 WiFi Qwiic Connector'
description: 'Learn how use the Qwiic connector on the Arduino UNO R4 WiFi.'
tags:
  - Qwiic
  - STEMMA QT
  - I2C
author: 'Jacob Hylén'
---

In this tutorial you will learn how to use the Qwiic connector on the Arduino UNO R4 WiFi.

## Goals

We will walk through the concept of I2C, and how it relates to the Qwiic ecosystem.

You'll learn what Qwiic is, as well as how to set it up and get started making your own Qwiic system with the Arduino UNO R4 WiFi.

![The Qwiic connector of the Arduino UNO R4 WiFi](./assets/Qwiic-connector.png)

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software))
- [Arduino UNO R4 WiFi](https://store.arduino.cc/uno-r4-wifi)
- Qwiic module
- Qwiic cable

## I2C

I2C is the communication protocol that is used in Qwiic, it is a protocol that allows you to connect many peripheral devices to a single controller board, using only two pins. 

To learn more about I2C and how it functions, check out our [I2C guide](/learn/communication/wire#tutorials).

## Qwiic
Qwiic is an ecosystem of breakout-modules and development boards with a so called Qwiic connector. The Arduino UNO R4 WiFi has one, for example. The Qwiic ecosystem combines the flexibility of I2C with the ease of use of pre-bundled cables making it incredibly easy to create lines of I2C devices, by collecting all the pins to get up and running with a large network of I2C devices in a single cable. 

Effectively this means that the wiring of your Qwiic devices is as simple as plugging them in in a series, and you're done.

![3 Qwiic Modules in a Line](./assets/Qwiic-modules.jpg)

## Arduino UNO R4 WiFi Implementation

The Arduino UNO R4 WiFi has two I2C buses, and the Qwiic connector is connected to the secondary one. 

Practically, this means that if you intend to use the Qwiic connector, when you're writing the code for your sketches, you cannot use the primary `Wire` object for I2C that you normally would, but you instead need to use the secondary one, `Wire1`. 

This *can* get problematic in some instances depending on the library developed for the breakout module you are using, as if there is no adequate solution for selecting the `Wire1` object when initialising the library you may need to alter the library code slightly, or write your own. 

In most cases, however, you will be able to select the `Wire1` object when initialising the library in a fashion similar to this:

```arduino
Wire1.begin();
libraryName.begin( Wire1 );
```

For example, when using SparkFuns AHT20 library, a sketch that read the temperature and prints it to the serial monitor could look like this:
```arduino
#include <Wire.h>
#include <SparkFun_Qwiic_Humidity_AHT20.h>

AHT20 humiditySensor;

void setup() {
  Serial.begin(9600);
  Wire1.begin();  //Join I2C bus
  //Check if the AHT20 will acknowledge
  if (humiditySensor.begin(Wire1) == false) {
    Serial.println("AHT20 not detected. Please check wiring. Freezing.");
    while (1)
      ;
  }
  Serial.println("AHT20 acknowledged.");
}

void loop() { 


  float temperature = humiditySensor.getTemperature();
  Serial.print("Temperature: ");
  Serial.print(temperature, 2);
  Serial.println(" C");
}
```

## Summary
In this tutorial, we have gone over the Qwiic connector on the Arduino UNO R4 WiFi. We've learned about how I2C works, and how that relates to Qwiic. We've also learned how the Arduino UNO R4 WiFis Qwiic connector is configured and how to make use of it to conveniently build large I2C networks of nodes for your interactive projects with minimal wiring. 