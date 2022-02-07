---
title: 'Proximity Detection with Arduino Nicla Vision'
difficulty: easy
description: 'Learn how to use the proximity sensor to vary the speed of the LED's blink'
tags:
  - Proximity
  - Sensor
author: 'Pablo Marquínez'
libraries: 
  - name: VL53L1X
    url: https://github.com/pololu/vl53l1x-arduino
hardware:
  - hardware/05.nicla/boards/nicla-vision
software:
  - ide-v1
  - ide-v2
  - web-editor
  - cli
---

## Overview

In this tutorial you will use the Nicla Vision to detect proximity, made by the Time of Flight (ToF) sensor **VL53L1X**.

This tutorial contains the sketch to blink the built-in RGB LED and control the speed of its blink by the proximity values.
This could help for future projects and control the Camera only when something is crossing in front of the board, like a proximity detector.

## Goals
The goals of this project are:
 - Set up the needed libraries
 - Learn how to interact with the proximity readings
 - Change the RGB values of the LED


### Required Hardware and Software

* Arduino Nicla Vision
* VL53L1X library (Available on the Library Manager)

## Instructions

Make sure you have installed the latest version of **Arduino mbed Core** and the **VL53L1X library**.

### Include the needed libraries

```cpp
    #include <Wire.h>
    #include "VL53L1X.h"
```
### Initialize the proximity sensor and the LED

```cpp
  VL53L1X proximity;
  bool blinkState = false;
  int reading = 0;
  int timeStart = 0;
  int blinkTime = 2000;

  void setup(){
    Serial.begin(115200);
    Wire.begin();
    Wire.setClock(400000); // use 400 kHz I2C
    pinMode(LEDB,OUTPUT);
    digitalWrite(LEDB, blinkState);
    proximity.setTimeout(500);
    if (!proximity.init()){
        Serial.println("Failed to detect and initialize sensor!");
        while (1)
            ;
    }

    proximity.setDistanceMode(VL53L1X::Long);
    proximity.setMeasurementTimingBudget(50000);

    proximity.startContinuous(50);
  }
```

### Control the speed of the blink

```cpp
  void loop(){
    reading = proximity.read();
    Serial.println(reading);

    if (millis() - timeStart >= reading){
        digitalWrite(LEDB, blinkState);
        !blinkState;
        timeStart = millis();
    }
  }
```

## Conclusion


