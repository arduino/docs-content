---
author: 'Arduino'
description: 'With this tutorial you will learn to use the RTC (Real Time Clock) and the WiFi capabilities.'
title: 'WiFi RTC'
---

With this tutorial you will learn to use the RTC (Real Time Clock) and the WiFi capabilities of the boards Arduino MKR1000, Arduino MKR WiFi 1010 and Arduino MKR VIDOR 4000. The network connection is used to access one Time Server on the Internet and to get from it the correct Time, using the Network Time Protocol builtin in the used WiFi module. The time is then used to configure the internal RTC (UTC format) of the board using the linux epoch format.

## Hardware Required

- Arduino MKR1000, Arduino MKR WiFi 1010 and Arduino MKR VIDOR 4000

- WiFi access to the Internet

## The Circuit

No circuit is required for this tutorial.

## Software Essentials

### Includes:

`<SPI.h>`
This library allows you to communicate with SPI devices, with the Arduino as the master device. In this sketch it is used to communicate with the WiFi Radio. Included for compatibillity with IDE versions before  1.6.5.

`<WiFi101.h>`
This is the library shared across the old WiFi enabled boards to manage the connections to the Internet through WiFi.

**or**

`<WiFiNINA.h>`
This is the library shared across the new WiFi enabled boards to manage the connections to the Internet through WiFi. Please change `<WiFi101.h>` into `<WiFiNINA.h>` if you are using an Arduino MKR WiFi 1010 or Arduino MKR VIDOR 4000.

`<RTCZero.h>`
This library allows an Arduino Zero or MKR1000 board to control and use the internal RTC (Real Time Clock).

### Functions defined in the sketch:

*printTime()*
Reads the time from the RTC object and prints hour, minutes and seconds to the Serial console.

*printDate()*
Reads the date from the RTC object and prints day, month and year to the Serial console with zero padding.

*printWiFiStatus()*
Prints to Serial console a full set of information including the SSID of the network you're connected to, the local IP address and the signal strength.

## Code

The code is based on [Epoch](https://raw.githubusercontent.com/arduino-libraries/RTCZero/master/examples/Epoch/Epoch.ino) example in RTCZero.

```arduino

/*

  MKR1000 - MKR WiFi 1010 - MKR VIDOR 4000 WiFi RTC

  This sketch asks NTP for the Linux epoch and sets the internal Arduino MKR1000's RTC accordingly.

  created 08 Jan 2016

  by Arturo Guadalupi <a.guadalupi@arduino.cc>

  modified 26 Sept 2018

  https://www.arduino.cc/en/Tutorial/WiFiRTC

  This code is in the public domain.

*/

#include <SPI.h>
#include <WiFi101.h>
//#include <WiFiNINA.h> //Include this instead of WiFi101.h as needed
#include <WiFiUdp.h>
#include <RTCZero.h>

RTCZero rtc;

#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                           // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;

const int GMT = 2; //change this to adapt it to your time zone

void setup() {

  Serial.begin(115200);

  // check if the WiFi module works

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to WiFi network:

  while ( status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  // you're connected now, so print out the status:

  printWiFiStatus();

  rtc.begin();

  unsigned long epoch;

  int numberOfTries = 0, maxTries = 6;

  do {

    epoch = WiFi.getTime();

    numberOfTries++;

  }

  while ((epoch == 0) && (numberOfTries < maxTries));

  if (numberOfTries == maxTries) {

    Serial.print("NTP unreachable!!");

    while (1);

  }

  else {

    Serial.print("Epoch received: ");

    Serial.println(epoch);

    rtc.setEpoch(epoch+ GMT*3600); //Add the time zone to the epoch

    Serial.println();

  }
}

void loop() {

  printDate();

  printTime();

  Serial.println();

  delay(1000);
}

void printTime()
{

  print2digits(rtc.getHours());

  Serial.print(":");

  print2digits(rtc.getMinutes());

  Serial.print(":");

  print2digits(rtc.getSeconds());

  Serial.println();
}

void printDate()
{

  Serial.print(rtc.getDay());

  Serial.print("/");

  Serial.print(rtc.getMonth());

  Serial.print("/");

  Serial.print(rtc.getYear());

  Serial.print(" ");
}

void printWiFiStatus() {

  // print the SSID of the network you're attached to:

  Serial.print("SSID: ");

  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:

  IPAddress ip = WiFi.localIP();

  Serial.print("IP Address: ");

  Serial.println(ip);

  // print the received signal strength:

  long rssi = WiFi.RSSI();

  Serial.print("signal strength (RSSI):");

  Serial.print(rssi);

  Serial.println(" dBm");
}

void print2digits(int number) {

  if (number < 10) {

    Serial.print("0");

  }

  Serial.print(number);
}
```

