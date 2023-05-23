---
title: 'Arduino UNO R4 Minima Real Time Clock'
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

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [Arduino R4 Minima]().
- [Arduino Renesas Core](https://github.com/bcmi-labs/ArduinoCore-renesas)

## Real-time Clock (RTC)

The RTC on the UNO R4 Minima can be accessed using the [RTC]() library that is included in the [Renesas]() core. This library allows you to set/get the time as well as using alarms to trigger interrupts. 

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

  RTC.setTime(startTime)
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

  RTC.setTime(startTime)
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

  RTC.setTime(startTime)
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
```arduino
#include "RTC.h"

void setup() {
  Serial.begin(9600);

  RTC.begin();
  
  RTCTime startTime(30, Month::JUNE, 2023, 13, 37, 00, DayOfWeek::WEDNESDAY, SaveLight::SAVING_TIME_ACTIVE);

  RTC.setTime(startTime)
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

This tutorial shows how to use the RTC on the UNO R4 Minima, such as setting a start time, setting an alarm, or obtaining time in calendar or unix format.

Read more about this board in the [Arduino UNO R4 Minima documentation]().

---

## API

The API is listed below:

## RTClock Class
The `RTClock` class is responsible for managing the real-time clock. It provides methods for initializing the clock, retrieving the current time, setting periodic callbacks, setting alarm callbacks, checking if the clock is running, and setting the time.

### Constructor
- `RTClock()`
  - Initializes a new `RTClock` object.

### Destructor
- `~RTClock()`
  - Destroys the `RTClock` object.

### Member Functions
- `bool begin()`
  - Initializes the real-time clock. Returns `true` if successful, `false` otherwise.
- `bool getTime(RTCTime &t)`
  - Retrieves the current time and stores it in the provided `RTCTime` object. Returns `true` if successful, `false` otherwise.
- `bool setPeriodicCallback(rtc_cbk_t fnc, Period p)`
  - Sets a periodic callback function to be called at the specified interval. The callback function should have the signature `void callback()`. Returns `true` if successful, `false` otherwise.
- `bool setAlarmCallback(rtc_cbk_t fnc, RTCTime &t, AlarmMatch &m)`
  - Sets an alarm callback function to be called when the specified time and match conditions are met. The callback function should have the signature `void callback()`. Returns `true` if successful, `false` otherwise.
- `bool isRunning()`
  - Checks if the real-time clock is running. Returns `true` if running, `false` otherwise.
- `bool setTime(RTCTime &t)`
  - Sets the current time to the specified `RTCTime` object. Returns `true` if successful, `false` otherwise.
- `bool setTimeIfNotRunning(RTCTime &t)`
  - Sets the current time to the specified `RTCTime` object only if the clock is not already running. Returns `true` if successful, `false` otherwise.

### External Object
- `RTClock RTC`
  - An external instance of the `RTClock` class that can be used to access the real-time clock functionality.

## RTCTime Class
The `RTCTime` class represents a specific time and date. It provides methods for setting and retrieving different components of the time and date.

### Constructors
- `RTCTime()`
  - Initializes a new `RTCTime` object with default values.
- `RTCTime(struct tm &t)`
  - Initializes a new `RTCTime` object from a `struct tm` object.
- `RTCTime(int _day, Month _m, int _year, int _hours, int _minutes, int _seconds, DayOfWeek _dow, SaveLight _sl)`
  - Initializes a new `RTCTime` object with the specified day, month, year, hours, minutes, seconds, day of the week, and daylight saving status.

### Destructor
- `~RTCTime()`
  - Destroys the `RTCTime` object.

### Setters
- `bool setDayOfMonth(int day)`
  - Sets the day of the month. Accepts a value from 1 to 31. Returns `true` if successful, `false` otherwise.
- `bool setMonthOfYear(Month m)`
  - Sets the month of the year. Accepts a value from 1 (January) to 12 (December). Returns `true` if successful, `false` otherwise.
- `bool setYear(int year)`
  - Sets the year. Accepts the year as a four-digit value (e.g., 1989 or 2022). Returns `true` if successful, `false` otherwise.
- `bool setHour(int hour)`
  - Sets the hour. Accepts a value from 0 (midnight) to 23. Returns `true` if successful, `false` otherwise.
- `bool setMinute(int minute)`
  - Sets the minute. Accepts a value from 0 to 59. Returns `true` if successful, `false` otherwise.
- `bool setSecond(int second)`
  - Sets the second. Accepts a value from 0 to 59. Returns `true` if successful, `false` otherwise.
- `bool setDayOfWeek(DayOfWeek d)`
  - Sets the day of the week. Accepts a value from 0 (Sunday) to 6 (Saturday). Returns `true` if successful, `false` otherwise.
- `bool setSaveLight(SaveLight sl)`
  - Sets the daylight saving status. Accepts a `SaveLight` value (`SAVING_TIME_INACTIVE` or `SAVING_TIME_ACTIVE`). Returns `true` if successful, `false` otherwise.
- `void setTM(struct tm &t)`
  - Sets the time and date using a `struct tm` object.

### Getters
- `int getDayOfMonth()`
  - Returns the day of the month.
- `Month getMonth()`
  - Returns the month of the year as a `Month` enum value.
- `int getYear()`
  - Returns the year.
- `int getHour()`
  - Returns the hour.
- `int getMinutes()`
  - Returns the minutes.
- `int getSeconds()`
  - Returns the seconds.
- `DayOfWeek getDayOfWeek()`
  - Returns the day of the week as a `DayOfWeek` enum value.
- `time_t getUnixTime()`
  - Returns the time in Unix timestamp format.
- `struct tm getTmTime()`
  - Returns the time and date as a `struct tm` object.

## Enumerations

### Month
- `JANUARY`
- `FEBRUARY`
- `MARCH`
- `APRIL`
- `MAY`
- `JUNE`
- `JULY`
- `AUGUST`
- `SEPTEMBER`
- `OCTOBER`
- `NOVEMBER`
- `DECEMBER`

### DayOfWeek
- `MONDAY`
- `TUESDAY`
- `WEDNESDAY`
- `THURSDAY`
- `FRIDAY`
- `SATURDAY`
- `SUNDAY`

### SaveLight
- `SAVING_TIME_INACTIVE`
- `SAVING_TIME_ACTIVE`

## Structures

### timeval
- `time_t tv_sec`
- `useconds_t tv_usec`

## Functions
The following functions are declared and defined in the library:

### External C Functions
- `void set_time(time_t t)`
- `void attach_rtc(time_t (*read_rtc)(void), void (*write_rtc)(time_t), void (*init_rtc)(void), int (*isenabled_rtc)(void))`
- `int gettimeofday(struct timeval *tv, void *tz)`
- `int settimeofday(const struct timeval *tv, const struct timezone *tz)`

### Helper Functions
- `int Month2int(Month m)`
- `int DayOfWeek2int(D

ayOfWeek dow, bool sunday_first)`
- `bool SaveLigth2bool(SaveLight sl)`

### AlarmMatch Class
The `AlarmMatch` class represents a set of match conditions for alarm triggers.

#### Constructor
- `AlarmMatch()`
  - Initializes a new `AlarmMatch` object.

#### Destructor
- `~AlarmMatch()`
  - Destroys the `AlarmMatch` object.

#### Member Functions
- `void addMatchSecond()`
  - Adds a match condition for seconds.
- `void addMatchMinute()`
  - Adds a match condition for minutes.
- `void addMatchHour()`
  - Adds a match condition for hours.
- `void addMatchDay()`
  - Adds a match condition for days.
- `void addMatchMonth()`
  - Adds a match condition for months.
- `void addMatchYear()`
  - Adds a match condition for years.
- `void addMatchDayOfWeek()`
  - Adds a match condition for days of the week.
- `void removeMatchSecond()`
  - Removes the match condition for seconds.
- `void removeMatchMinute()`
  - Removes the match condition for minutes.
- `void removeMatchHour()`
  - Removes the match condition for hours.
- `void removeMatchDay()`
  - Removes the match condition for days.
- `void removeMatchMonth()`
  - Removes the match condition for months.
- `void removeMatchYear()`
  - Removes the match condition for years.
- `void removeMatchDayOfWeek()`
  - Removes the match condition for days of the week.
- `bool isMatchingSecond()`
  - Checks if the match condition for seconds is set.
- `bool isMatchingMinute()`
  - Checks if the match condition for minutes is set.
- `bool isMatchingHour()`
  - Checks if the match condition for hours is set.
- `bool isMatchingDay()`
  - Checks if the match condition for days is set.
- `bool isMatchingMonth()`
  - Checks if the match condition for months is set.
- `bool isMatchingYear()`
  - Checks if the match condition for years is set.
- `bool isMatchingDayOfWeek()`
  - Checks if the match condition for days of the week is set.

## Additional Definitions
- `using stime_t = struct tm`
- `using rtc_cbk_t = void (*)()`