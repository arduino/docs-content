---
title: 'Arduino UNO R4 Minima Real-Time Clock'
description: 'Learn how to access the real-time clock (RTC) on the UNO R4 Minima.'
tags:
  - RTC
  - Alarm
author: 'Karl Söderby'
---

In this tutorial you will learn how to access the real-time clock (RTC) on an **Arduino UNO R4 Minima** board. The RTC is embedded in the UNO R4 Minima's microcontroller (RA4M1).

## Goals

The goals of this project are:

- Set a start date of the RTC
- Access the date / time from the RTC in calendar format.
- Access the time in Unix format.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software))
- [Arduino R4 Minima](https://store.arduino.cc/uno-r4-minima)
- [Arduino Renesas Core](https://github.com/arduino/ArduinoCore-renesas)

## Real-Time Clock (RTC)

The RTC on the UNO R4 Minima can be accessed using the [RTC](https://github.com/arduino/ArduinoCore-renesas/tree/main/libraries/RTC) library that is included in the [Renesas](https://github.com/arduino/ArduinoCore-renesas) core. This library allows you to set/get the time as well as using alarms to trigger interrupts. 

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
- `void periodicCallback() { code to be executed }`

***Note the IRQ has a very fast execution time. Placing a lot of code is not a good practice, so in the example below we are only switching  a single flag, `irqFlag`.***

The example below blinks a light every 2 seconds:

```arduino
#include "RTC.h"

volatile bool irqFlag = false;
volatile bool ledState = false;

const int led = LED_BUILTIN;

void setup() {
  pinMode(led, OUTPUT);

  Serial.begin(9600);

  // Initialize the RTC
  RTC.begin();

  // RTC.setTime() must be called for RTC.setPeriodicCallback to work, but it doesn't matter
  // what date and time it's set to
  RTCTime mytime(30, Month::JUNE, 2023, 13, 37, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE);
  RTC.setTime(mytime);

  if (!RTC.setPeriodicCallback(periodicCallback, Period::ONCE_EVERY_2_SEC)) {
    Serial.println("ERROR: periodic callback not set");
  }
}

void loop(){
  if(irqFlag){
    Serial.println("Timed CallBack");
    ledState = !ledState;
    digitalWrite(LED_BUILTIN, ledState);
    irqFlag = false;
  }
}

void periodicCallback()
{
  irqFlag = true;
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
unsigned long previousMillis = 0;
const long interval = 1000;
bool ledState = false;

// Include the RTC library
#include "RTC.h"

void setup() {
  //initialize Serial Communication
  Serial.begin(9600);

  //define LED as output
  pinMode(LED_BUILTIN, OUTPUT);

  // Initialize the RTC
  RTC.begin();

  // RTC.setTime() must be called for RTC.setAlarmCallback to work, but it doesn't matter
  // what date and time it's set to in this example
  RTCTime initialTime(7, Month::JUNE, 2023, 13, 03, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE);
  RTC.setTime(initialTime);

  // Trigger the alarm every time the seconds are zero
  RTCTime alarmTime;
  alarmTime.setSecond(0);

  // Make sure to only match on the seconds in this example - not on any other parts of the date/time
  AlarmMatch matchTime;
  matchTime.addMatchSecond();

  //sets the alarm callback
  RTC.setAlarmCallback(alarmCallback, alarmTime, matchTime);
}

void loop() {

  // in the loop, we continuously print the alarm's current state
  // this is for debugging only and has no effect on the alarm whatsoever
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;
    Serial.print("Alarm state: ");
    Serial.println(ledState);
  }
}

// this function activates every minute
// and changes the ledState boolean
void alarmCallback() {
  if (!ledState) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
  ledState = !ledState;
}
```

## Summary

This tutorial shows how to use the RTC on the UNO R4 Minima, such as setting a start time, setting an alarm, or obtaining time in calendar or unix format.

Read more about this board in the [Arduino UNO R4 Minima documentation](/hardware/uno-r4-minima).
