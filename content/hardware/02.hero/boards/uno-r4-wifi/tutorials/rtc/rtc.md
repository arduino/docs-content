---
title: 'Arduino UNO R4 WiFi Real-Time Clock'
description: 'Learn how to access the real-time clock (RTC) on the UNO R4 WiFi.'
tags:
  - RTC
  - Alarm
author: 'Karl Söderby'
hardware:
  - hardware/02.hero/boards/uno-r4-wifi
---

In this tutorial you will learn how to access the real-time clock (RTC) on an **Arduino UNO R4 WiFi** board. The RTC is embedded in the UNO R4 WiFi's microcontroller (RA4M1).

## Goals

The goals of this project are:

- Set a start date of the RTC
- Access the date / time from the RTC in calendar format.
- Access the time in Unix format.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software))
- [Arduino UNO R4 WiFi](https://store.arduino.cc/uno-r4-wifi)
- [Arduino Renesas Core](https://github.com/arduino/ArduinoCore-renesas)

## Real-Time Clock (RTC)

The RTC on the UNO R4 WiFi can be accessed using the [RTC](https://github.com/arduino/ArduinoCore-renesas/tree/main/libraries/RTC) library that is included in the [Renesas](https://github.com/arduino/ArduinoCore-renesas) core. This library allows you to set/get the time as well as using alarms to trigger interrupts. 

***The UNO R4 WiFi features a VRTC pin, that is used to keep the onboard RTC running, even when the boards power supply is is cut off. In order to use this, apply a voltage in the range of 1.6 - 3.6 V to the VRTC pin.***

There are many practical examples using an RTC, and the examples provided in this page will help you get started with it.

### Set Time

- `RTCTime startTime(30, Month::JUNE, 2023, 13, 37, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE)`
- `RTC.setTime(startTime)`

To set the starting time for the RTC, you can create an `RTCTime` object. Here you can specify the day, month, year, hour, minute, second, and specify day of week as well as daylight saving mode.

Then to set the time, use the `setTime()` method.

Example:

```arduino
#include "RTC.h"

void setup() {
  Serial.begin(9600);

  RTC.begin();
  
  RTCTime startTime(30, Month::JUNE, 2023, 13, 37, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE);

  RTC.setTime(startTime);
}

void loop(){
}
```

### Get Time

- `RTC.getTime(currentTime)`

To retrieve the time, we need to create a `RTCTime` object, and use the `getTime()` method to retrieve the current time.

This example sets & gets the time and stores it in an `RTCTime` object called `currentTime`.

```arduino
#include "RTC.h"

void setup() {
  Serial.begin(9600);

  RTC.begin();
  
  RTCTime startTime(30, Month::JUNE, 2023, 13, 37, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE);

  RTC.setTime(startTime);
}

void loop(){
RTCTime currentTime;

// Get current time from RTC
RTC.getTime(currentTime);
}
```


### Print Date & Time

The above examples show how to set & get the time and store it in an object. This data can be retrieved by a series of methods:
- `getDayOfMonth()`
- `getMonth()`
- `getYear()`
- `getHour()`
- `getMinutes()`
- `getSeconds()`

The example below prints out the date and time from the `currentTime` object.

```arduino
#include "RTC.h"

void setup() {
  Serial.begin(9600);

  RTC.begin();
  
  RTCTime startTime(30, Month::JUNE, 2023, 13, 37, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE);

  RTC.setTime(startTime);
}

void loop() {
  RTCTime currentTime;

  // Get current time from RTC
  RTC.getTime(currentTime);

  // Print out date (DD/MM//YYYY)
  Serial.print(currentTime.getDayOfMonth());
  Serial.print("/");
  Serial.print(Month2int(currentTime.getMonth()));
  Serial.print("/");
  Serial.print(currentTime.getYear());
  Serial.print(" - ");

  // Print time (HH/MM/SS)
  Serial.print(currentTime.getHour());
  Serial.print(":");
  Serial.print(currentTime.getMinutes());
  Serial.print(":");
  Serial.println(currentTime.getSeconds());

  delay(1000);
}
```

### Unix

- `currentTime.getUnixTime()`

To retrieve the Unix timestamp, use the `getUnixTime()` method.

```arduino
#include "RTC.h"

void setup() {
  Serial.begin(9600);

  RTC.begin();
  
  RTCTime startTime(30, Month::JUNE, 2023, 13, 37, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE);

  RTC.setTime(startTime);
}

void loop() {
  RTCTime currentTime;

  // Get current time from RTC
  RTC.getTime(currentTime);
  
  //Unix timestamp
  Serial.print("Unix timestamp: ");
  Serial.println(currentTime.getUnixTime());

  delay(1000);
}
```

### Periodic Interrupt

A periodic interrupt allows you to set a recurring callback. 

To use this, you will need to initialize the periodic callback, using the `setPeriodicCallback()` method:
- `RTC.setPeriodicCallback(periodic_cbk, Period::ONCE_EVERY_2_SEC)`

You will also need to create a function that will be called:
- `void periodic_cbk() { code to be executed }`

The example below blinks a light every 2 seconds:

```arduino
#include "RTC.h"

const int LED_ON_INTERRUPT  = 22;

void setup(){
  RTC.begin();
  if (!RTC.setPeriodicCallback(periodic_cbk, Period::ONCE_EVERY_2_SEC)) {
    Serial.println("ERROR: periodic callback not set");
  }
}

void loop() {
}

void periodic_cbk() {
  static bool clb_st = false;
  if(clb_st) {
    digitalWrite(LED_ON_INTERRUPT,HIGH);
  }
  else {
    digitalWrite(LED_ON_INTERRUPT,LOW);
  }
  clb_st = !clb_st;
 
  Serial.println("PERIODIC INTERRUPT");
}
```

The period can be specified using the following enumerations:
- `ONCE_EVERY_2_SEC`
- `ONCE_EVERY_1_SEC`
- `N2_TIMES_EVERY_SEC`
- `N4_TIMES_EVERY_SEC`
- `N8_TIMES_EVERY_SEC`
- `N16_TIMES_EVERY_SEC`
- `N32_TIMES_EVERY_SEC`
- `N64_TIMES_EVERY_SEC`
- `N128_TIMES_EVERY_SEC`
- `N256_TIMES_EVERY_SEC`


### Alarm Callback

- `RTC.setAlarmCallback(alarm_cbk, alarmtime, am)`

```arduino
#include "RTC.h"

void setup() {
  Serial.begin(9600);

  RTC.begin();

  RTCTime alarmtime;
  alarmtime.setSecond(35);

  AlarmMatch am;
  am.addMatchSecond();

  if (!RTC.setAlarmCallback(alarm_cbk, alarmtime, am)) {
    Serial.println("ERROR: alarm callback not set");
  }
}

void alarm_cbk() {
  Serial.println("ALARM INTERRUPT");
}
```

## Summary

This tutorial shows how to use the RTC on the UNO R4 WiFi, such as setting a start time, setting an alarm, or obtaining time in calendar or unix format.

Read more about this board in the [Arduino UNO R4 WiFi documentation](/hardware/uno-r4-wifi).
