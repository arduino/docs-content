---
title: 'Scanning Available Networks with MKR NB 1500'
difficulty: intermediate
compatible-products: [mkr-nb-1500]
description: 'Learn how to scan nearby NB-IoT / CAT-M1 networks in your area, and print them out in the Serial Monitor.'
tags:
 - NB-IoT
 - CAT-M1
author: 'Benjamin Dannegård'
libraries: 
  - name: MKRNB
    url: https://www.arduino.cc/reference/en/libraries/mkrnb/
hardware:
  - hardware/01.mkr/01.boards/mkr-nb-1500
  - _snippets/hardware/dipole-antenna
  - _snippets/hardware/sim-card
software:
  - ide-v1
  - ide-v2
  - web-editor
---


## Introduction 

In this tutorial, we will perform a scan of available networks for your NB board in the area. The networks available will then be printed in the Serial Monitor along with the signal strength. 

>**Note:** This tutorial was created in Sweden, and as a result, the available networks are only Swedish network operators. The results will vary depending on what location we are in. 

## Goals

The goals of this project are:

- Scan nearby networks
- Print detected networks in the Serial Monitor.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [MKRNB](https://www.arduino.cc/en/Reference/MKRNB) library installed.
- Arduino MKR NB 1500 ([link to store](https://store.arduino.cc/arduino-mkr-nb-1500-1413)).
- Antenna ([link to store](https://store.arduino.cc/antenna)).

## The uBlox SARA-R4 Module

As every other MKR family board, the MKR NB 1500 board has a specific module for connectivity. It is called uBlox SARA-R4, and is designed to communicate over LTE Cat M1 or NB IoT networks with a speed of up to 375 Kbps.

It is designed to operate in temperature conditions between –40 °C to +85 °C, making it quite durable. It also offers low power consumption and coverage enhancement for deeper range into buildings and basements (and underground with NB1).

The module also provides an interface for SIM cards, and supports both 1.8V and 3V SIM cards, which can be automatically detected. 

You can find out much more information about this component in the <a href="https://content.arduino.cc/assets/Arduino_SARA-R4_DataSheet_%28UBX-16024152%29.pdf" target="_blank">uBlox SARA-R4 datasheet</a>.

## Circuit

![Simple circuit of the board with antenna.](assets/MKRNB_T2_IMG01.png)

## Programming the Board

We will now get to the programming part of this tutorial. 

**1.** First, let's make sure we have the drivers installed. If we are using the Web Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it. 

**2.** Now, we need to install the libraries needed. If we are using the Web Editor, there is no need to install anything. If we are using an offline editor, simply go to **Tools > Manage libraries..**, and search for **MKRNB** and install it.

**3.** After the library is installed, we can now navigate to **File > Examples > MKRNB > Tools > NBScanNetworks**. This will open a new sketch window (or direct you to the sketch if you are using the Web Editor). There will also be a separate tab called `arduino_secrets.h`. Here we will simply fill in the pin number of our SIM card. 

>**Note:** A standard pre-paid SIM card typically have 0000 or 1234 as a pin code. This varies from operator to operator,and it is important to find out this before uploading the code. Otherwise, too many unsuccessful attempts may block the SIM card.

**4.** We can now take a look at some of the core functions of this sketch:

- `NB nbAccess` - base class for all NB functions.
- `NBScanner scannerNetworks` - base class relating to scanning of available networks.
- `NBModem modemTest` - base class for calls that have specific diagnostic functionality with the modem.
- `nbAccess.begin(pin)` - connects to the selected network with the pin number as a parameter, e.g. 0123.
- `getIMEI()` - retrieves the International Mobile Equipment Identity (IMEI) from the modem.

**5.** We can now upload the sketch to the board. The code is also available in the snippet below:

```cpp
#include <MKRNB.h>

#include "arduino_secrets.h" 
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number
const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instance
NB nbAccess;     // include a 'true' parameter to enable debugging
NBScanner scannerNetworks;
NBModem modemTest;

// Save data variables
String IMEI = "";

// serial monitor result messages
String errortext = "ERROR";

void setup() {
  // initialize serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  Serial.println("NB IoT/LTE Cat M1 networks scanner");
  scannerNetworks.begin();

  // connection state
  boolean connected = false;

  // Start module
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while (!connected) {
    if (nbAccess.begin(PINNUMBER) == NB_READY) {
      connected = true;
    } else {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  // get modem parameters
  // IMEI, modem unique identifier
  Serial.print("Modem IMEI: ");
  IMEI = modemTest.getIMEI();
  IMEI.replace("\n", "");
  if (IMEI != NULL) {
    Serial.println(IMEI);
  }
}

void loop() {
  // currently connected carrier
  Serial.print("Current carrier: ");
  Serial.println(scannerNetworks.getCurrentCarrier());

  // returns strength and ber
  // signal strength in 0-31 scale. 31 means power > 51dBm
  // BER is the Bit Error Rate. 0-7 scale. 99=not detectable
  Serial.print("Signal Strength: ");
  Serial.print(scannerNetworks.getSignalStrength());
  Serial.println(" [0-31]");

  // scan for existing networks, displays a list of networks
  Serial.println("Scanning available networks. May take some seconds.");
  Serial.println(scannerNetworks.readNetworks());
  // wait ten seconds before scanning again
  delay(10000);
}
```

## Testing It Out

Once we have uploaded the code to the board, we can proceed by opening the Serial Monitor. This will initialize the program, and a scanning of the network will shortly begin. 

If the board fails to connect to the NB network, it will print `"Not connected"` in the Serial Monitor. This could be a problem with the SIM card, or that we are simply not within range of a network.

If it succeeds, it will start listing the available networks in your area.

## Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- We have not installed the **MKRNB** library.
- We have entered the wrong pin number.
- We are out of coverage (no signal).
- SIM card may not be activated.

## Conclusion

In this tutorial, we took a brief look at the uBlox SARA-R4 module that provides network connectivity to the MKR NB 1500 board. We then configured the sketch (entered the pin number for our SIM card), got our currently connected network and signal strength printed in the serial monitor, and performed a scan of available networks. The list of available networks were then printed in the Serial Monitor.

This is a very basic tutorial for testing the connectivity of the MKR NB 1500 board, and there's much much more we can do. Feel free to explore the [MKRNB](https://www.arduino.cc/en/Reference/MKRNB) library further, and try out some of the many cool functions in this library.
