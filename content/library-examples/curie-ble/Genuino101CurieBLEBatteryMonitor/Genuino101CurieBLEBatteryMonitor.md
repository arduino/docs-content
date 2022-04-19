---
author: 'Arduino'
description: 'This tutorial shows one of the simplest things you can do with an Arduino 101 Bluetooth® Low Energy capabilities.'
tags: [Arduino 101]
title: 'Arduino 101 CurieBLE Battery Monitor'

---

This tutorial shows one of the simplest things you can do with an Arduino 101's onboard Bluetooth® Low Energy capabilities. The sketch implements the [standard Bluetooth® Low Energy "Battery Monitor" service](https://developer.bluetooth.org/gatt/services/Pages/ServiceViewer.aspx?u=org.bluetooth.service.battery_service.xml). The Battery Monitor service reads battery level values over Bluetooth® Low Energy from your smartphone or tablet and displays them on the Serial Monitor of the Arduino Software (IDE). This is achieved with the Curie's Bluetooth® Low Energy library and a proper application on the smartphone or tablet.

## Hardware Required

- [Arduino 101](https://www.arduino.cc/en/Main/ArduinoBoard101)
- 10k linear potentiometer

- Smartphone or Tablet Android or iOS

## Software Required

- nRF Master Control Panel(Bluetooth® Low Energy) for [Android](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&amp;hl=en) and [iOS](https://itunes.apple.com/us/app/nrf-master-control-panel-ble/id1054362403?mt=8)

## The Circuit

![](./Arduino101_PotentiometerA0.png)

image developed using [Fritzing](http://www.fritzing.org).

The board has an embedded Bluetooth® Low Energy module, therefore it is enough to connect the board to the computer and use the Serial Monitor to read the messages sent by the sketch. A potentiometer is connected to 3.3V, GND and A0 to simulate the charge of a battery.

## Software Essentials

### Libraries

*CurieBLE.h* is the library that gives access to all the parameters, features and functions of the Bluetooth® Low Energy module of the 101 board. With Bluetooth® Low Energy it is possible to connect to and communicate with smartphones, tablets and peripherals that support this standard. In this tutorial it is used to read the battery level of the device to which we connect as a peripheral.

*updateBatteryLevel()* - This function is called every 200 millliseconds from the main loop. It simulates the readiong of a battery with a potentiometer connected to A0. The value is first checked against the former value read. If it is changed, the code activates the printing on the Serial Monitor of the new value and updates the Battery characteristic with `batteryLevelChar.setValue(batteryLevel);`. This is read on the Bluetooth® Low Energy Control Panel on the smartphone under the "Battery Service"

![](./BatteryMonitorBLE.png)

## Code

This sketch example partially implements the standard Bluetooth® Low-Energy Battery Service.

In the setup(), you initialize pin 13 as an output to drive the LED with `pinMode(13, OUTPUT);`
blePeripheral is used to initialize the board as a Bluetooth® Low Energy peripheral with `BLEPeripheral blePeripheral;`
If multiple boards will be running this sketch example in close proximity, you need to modify the local name so each can be uniquely identified.

For example,

`blePeripheral.setLocalName("BatteryMonitorSketch");`
becomes

`blePeripheral.setLocalName("BatteryMonitorSketch1");`
In the main loop, you turn the LED on when the connection to the central device is detected with the line:

`digitalWrite(13, HIGH);`
Every 200ms the connection is tested and if still active, updateBatteryLevel is called. When the connection is lost, you turn off the LED with the line: `digitalWrite(13, LOW);` that takes pin 13 from 3.3V back to 0V, and turns the LED off.

```arduino
/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

#include <CurieBLE.h>

/*

   This sketch example partially implements the standard Bluetooth® Low-Energy Battery service.

   For more information: https://developer.bluetooth.org/gatt/services/Pages/ServicesHome.aspx

*/

/*  */

BLEPeripheral blePeripheral;       // BLE Peripheral Device (the board you're programming)

BLEService batteryService("180F"); // BLE Battery Service

// BLE Battery Level Characteristic"

BLEUnsignedCharCharacteristic batteryLevelChar("2A19",  // standard 16-bit characteristic UUID

    BLERead | BLENotify);     // remote clients will be able to
// get notifications if this characteristic changes

int oldBatteryLevel = 0;  // last battery level reading from analog input
long previousMillis = 0;  // last time the battery level was checked, in ms

void setup() {

  Serial.begin(9600);    // initialize serial communication

  pinMode(13, OUTPUT);   // initialize the LED on pin 13 to indicate when a central is connected

  /* Set a local name for the BLE device

     This name will appear in advertising packets

     and can be used by remote devices to identify this BLE device

     The name can be changed but maybe be truncated based on space left in advertisement packet */

  blePeripheral.setLocalName("BatteryMonitorSketch");

  blePeripheral.setAdvertisedServiceUuid(batteryService.uuid());  // add the service UUID

  blePeripheral.addAttribute(batteryService);   // Add the BLE Battery service

  blePeripheral.addAttribute(batteryLevelChar); // add the battery level characteristic

  batteryLevelChar.setValue(oldBatteryLevel);   // initial value for this characteristic

  /* Now activate the BLE device.  It will start continuously transmitting BLE

     advertising packets and will be visible to remote BLE central devices

     until it receives a new connection */

  blePeripheral.begin();

  Serial.println(" Bluetooth® device active, waiting for connections...");
}

void loop() {

  // listen for BLE peripherals to connect:

  BLECentral central = blePeripheral.central();

  // if a central is connected to peripheral:

  if (central) {

    Serial.print("Connected to central: ");

    // print the central's MAC address:

    Serial.println(central.address());

    // turn on the LED to indicate the connection:

    digitalWrite(13, HIGH);

    // check the battery level every 200ms

    // as long as the central is still connected:

    while (central.connected()) {

      long currentMillis = millis();

      // if 200ms have passed, check the battery level:

      if (currentMillis - previousMillis >= 200) {

        previousMillis = currentMillis;

        updateBatteryLevel();

      }

    }

    // when the central disconnects, turn off the LED:

    digitalWrite(13, LOW);

    Serial.print("Disconnected from central: ");

    Serial.println(central.address());

  }
}

void updateBatteryLevel() {

  /* Read the current voltage level on the A0 analog input pin.

     This is used here to simulate the charge level of a battery.

  */

  int battery = analogRead(A0);

  int batteryLevel = map(battery, 0, 1023, 0, 100);

  if (batteryLevel != oldBatteryLevel) {      // if the battery level has changed

    Serial.print("Battery Level % is now: "); // print it

    Serial.println(batteryLevel);

    batteryLevelChar.setValue(batteryLevel);  // and update the battery level characteristic

    oldBatteryLevel = batteryLevel;           // save the level for next comparison

  }
}

/*

   Copyright (c) 2016 Intel Corporation.  All rights reserved.

   This library is free software; you can redistribute it and/or

   modify it under the terms of the GNU Lesser General Public

   License as published by the Free Software Foundation; either

   version 2.1 of the License, or (at your option) any later version.

   This library is distributed in the hope that it will be useful,

   but WITHOUT ANY WARRANTY; without even the implied warranty of

   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU

   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public

   License along with this library; if not, write to the Free Software

   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

*/
```


*Last revision 2016/04/05 by SM* \\