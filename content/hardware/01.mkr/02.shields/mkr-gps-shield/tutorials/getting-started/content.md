---
title: 'Getting Started with the MKR GPS Shield'
description: 'Learn how to access GPS data from the module on board the MKR GPS Shield.'
tags:
    - GPS
author: Arduino
---

## Introduction

The MKR GPS Shield is based on the u-blox® [SAM-M8Q](https://www.u-blox.com/sites/default/files/SAM-M8Q_DataSheet_%28UBX-16012619%29.pdf) GNSS (Global Navigation Satellite System) module. This module is designed to operate with different positioning services concurrently. It receives and processes the signals from [GPS](https://en.wikipedia.org/wiki/Global_Positioning_System), [GLONASS](https://en.wikipedia.org/wiki/GLONASS) and [Galileo](https://en.wikipedia.org/wiki/Galileo_satellite_navigation).

The reception of different services at the same time makes this shield suitable for outdoor applications around the world with an accurate calculation of the position down to a few meters. Multiple constellations means also more satellites in sight in environments like cities with tall buildings or areas with deep valleys and limited sky view.

### Hardware

The MKR GPS Shield has a small footprint and it is just slightly bigger than the space occupied by the headers. On it we have placed the [SAM-M8Q](https://www.u-blox.com/sites/default/files/SAM-M8Q_DataSheet_%28UBX-16012619%29.pdf) module, a backup battery holder, a power regulator and a 5 pin connector that is based on our 5pin standard scheme.

| connector pin | Signal |
| ------------- | ------ |
| 1             | +5V    |
| 2             | EXTINT |
| 3             | SCL    |
| 4             | SDA    |
| 5             | GND    |

Six solder pads allow the configuration of the connection between the module and the host. Some are already bridged, others are disconnected by default.

| M8Q        | HOST | CONNECTED |
| ---------- | ---- | --------- |
| RESET_N    | 10   | N         |
| RXD        | 9    | Y         |
| TXD        | 8    | Y         |
| SAFEBOOT_N | 3    | N         |
| EXTINT     | 2    | Y         |
| TP         | 1    | N         |

The shield has been designed to be used with a MKR board as host through the headers or in a detached way, with the I2C connector that supports the power supply through pin 1.

The module runs at a maximum voltage of 3.3 V and it is not 5 V tolerant, so if you plan to use it in a design where the signal levels for communication are managed by a board that has a 5 V microcontroller, you need to add a logic level converter 5V<->3.3V to safeguard the module input ports.

The patch antenna is omnidirectional and should be kept with a clear sky view. Please remember that some car windshields are laminated with filters for IR and UV light that also shield electromagnetic signals. Usually the front windshield has a dedicated uncoated zone, useful for GNSS signal reception, near the rear mirror.

### Software

The MKR GPS Shield is connected through Serial1 to the MKR board or through I2C / DCC protocol on the 5pin connector. You can specify the type of connection you are using in the creator API `begin()` of our [Arduino_MKRGPS](/en/Reference/ArduinoMKRGPS) library that supports both in a transparent way for all the other APIs.

### Examples

The following sketch print continuously on the serial console the position.

```c
/*

  GPS Location
  This sketch uses the GPS to determine the location of the board
  and prints it to the Serial monitor.

  Circuit:
   - MKR board
   - MKR GPS Shield attached via I2C cable

  This example code is in the public domain.

*/

#include <Arduino_MKRGPS.h>

void setup() {
  // initialize serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // If you are using the MKR GPS as shield, change the next line to pass
  // the GPS_MODE_SHIELD parameter to the GPS.begin(...)

  if (!GPS.begin()) {
    Serial.println("Failed to initialize GPS!");
    while (1);
  }
}

void loop() {

  // check if there is new GPS data available

  if (GPS.available()) {
    // read GPS values
    float latitude   = GPS.latitude();
    float longitude  = GPS.longitude();
    float altitude   = GPS.altitude();
    float speed      = GPS.speed();
    int   satellites = GPS.satellites();

    // print GPS values

    Serial.print("Location: ");
    Serial.print(latitude, 7);
    Serial.print(", ");
    Serial.println(longitude, 7);
    Serial.print("Altitude: ");
    Serial.print(altitude);
    Serial.println("m");
    Serial.print("Ground speed: ");
    Serial.print(speed);
    Serial.println(" km/h");
    Serial.print("Number of satellites: ");
    Serial.println(satellites);
    Serial.println();
  }
}
```

This second example keeps the power consumption under control waking up the module every 10 seconds to get the position of the shield; when the position is acquired, it gets printed on the serial console together with the time taken to acquire it.

```c
/*

  GPS Location Standby
  This sketch uses the GPS to determine the location of the board
  and prints it to the Serial Monitor.

  It puts the GPS to in standby mode every 10 seconds, then wakes it up.

  Circuit:
   - MKR board
   - MKR GPS attached via I2C cable

  This example code is in the public domain.

*/

#include <Arduino_MKRGPS.h>

void setup() {
  // initialize serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // If you are using the MKR GPS as shield, change the next line to pass
  // the GPS_MODE_SHIELD parameter to the GPS.begin(...)

  if (!GPS.begin()) {
    Serial.println("Failed to initialize GPS!");
    while (1);
  }
}

void loop() {
  // put the GPS in standby mode
  Serial.println("standby");
  GPS.standby();
  // wait for 10 seconds
  Serial.print("delay ");
  for (int i = 0; i < 10; i++) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println();
  // wake up the GPS
  Serial.println("wakeup");
  GPS.wakeup();
  Serial.print("wait location ... ");
  // wait for new GPS data to become available
  unsigned long startMillis = millis();
  while (!GPS.available());
  unsigned long endMillis = millis();
  Serial.print(endMillis - startMillis);
  Serial.println(" ms");

  // read GPS values

  float latitude   = GPS.latitude();
  float longitude  = GPS.longitude();
  float altitude   = GPS.altitude();
  int   satellites = GPS.satellites();

  // print GPS values

  Serial.println();
  Serial.print("Location: ");
  Serial.print(latitude, 7);
  Serial.print(", ");
  Serial.println(longitude, 7);
  Serial.print("Altitude: ");
  Serial.print(altitude);
  Serial.println("m");
  Serial.print("Number of satellites: ");
  Serial.println(satellites);
  Serial.println();
}
```
