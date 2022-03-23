---
title: 'Curie Time Library'
description: 'This library allows an Arduino/Genuino 101 control and use the internal RTC (Real Time Clock).'
author: Arduino
---

## Overview

***This library is included in the [Arc32 core](https://github.com/arduino/ArduinoCore-arc32/tree/master/libraries). This core can be installed through the Arduino IDEs , where the package is named "Intel Curie Boards".*** 

This library allows an Arduino/Genuino 101 control and use the internal RTC (Real Time Clock). A real-time clock is a clock that keeps track of the current time and that can be used in order to program actions at a certain time. Most RTCs use a crystal oscillator whose frequency is 32.768 kHz (same frequency used in quartz clocks and watches). Namely this the frequency equal to 2^15 cycles per second and so is a convenient rate to use with simple binary counter circuits. Furthermore the RTC can continue to operate in any sleep mode, so it can be used to wake up the device from sleep modes in a programmed way. Every time the board is powered, the RTC is reset and starts from a standard date. To keep the time and the RTC running it is necessary to keep the board powered.

To use this library
```
#include <CurieTime.h>
```
## Examples
- [Read Test](https://www.arduino.cc/en/Tutorial/ReadTest)
- [Set Time](https://www.arduino.cc/en/Tutorial/SetTime)

## Functions

---

### `now()`
#### Description
Returns the number of seconds since Jan 1 1970.

#### Syntax
```
unsigned long now = now()
```
#### Returns
The number of seconds since Jan 1 1970.

---

### `year()`
#### Description
Set or read the RTC year value.

#### Syntax
```
year(unsigned long year)

unsigned long year = year();
```
#### Parameters
year: the year value to be set.

#### Returns
The current year value.

---

### `month()`
#### Description
Set or read the RTC month value.

#### Syntax
```
month(unsigned long month)

unsigned long month = month();
```
#### Parameters
month: the month value to be set.

#### Returns
The current month value.

---

### `day()`
#### Description
Set or read the RTC day value.

#### Syntax
```
day(unsigned long day)

unsigned long day = day();
```
#### Parameters
day: the day value to be set.

#### Returns
The current day value.

---

### `hour()`
#### Description
Set or read the RTC hour value.

#### Syntax
```
hour(unsigned long hour)

unsigned long hour = hour();
```
#### Parameters
hour: the hour value to be set.

#### Returns
The current hour value.

---

### `minute()`
#### Description
Set or read the RTC minute value.

#### Syntax
```
minute(unsigned long minute)

unsigned long minute = minute();
```
#### Parameters
minute: the minute value to be set.

#### Returns
The current minute value.

---

### `second()`
#### Description
Set or read the RTC second value.

#### Syntax
```
second(unsigned long second)

unsigned long second = second();
```
#### Parameters
second: the second value to be set.

#### Returns
The current second value.

---

### `setTime()`
#### Description
Set hour, minute, second, day, month and year of the RTC

#### Syntax
```
void setTime(int hour, int minute, int second, int day, int month, int year)

void setTime(unsigned long t)
```
#### Parameters
hour: the hour value to be set.

minute: the minute value to be set.

second: the second value to be set.

day: the day value to be set.

month: the month value to be set.

year: the year value to be set.

t: the current number of seconds since Jan 1 1970
