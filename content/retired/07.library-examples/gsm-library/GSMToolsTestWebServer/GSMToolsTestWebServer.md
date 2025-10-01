---
slug: '/en/Tutorial/LibraryExamples/GSMToolsTestWebServer'
date: 'February 05, 2018, at 08:43 PM'
title: 'GSM Test Web Server'
description: 'Create a webserver with your GSM shield.'
---

This sketch creates a web server to accept incoming connections on the GSM shield.  Some network providers only allow requests from inside their own network. You will need to check with your network provider to make sure your SIM card will accept incoming HTTP requests.

## Hardware Required

- Arduino Board

- [Arduino + Telefonica GSM/GPRS Shield](/retired/shields/arduino-gsm-shield)
- SIM card enable for Data

## Circuit

![image of the Arduino GSM Shield on top of an Arduino board](assets/GSMShield_ArduinoUno.jpg)



## Code

## Complete Sketch

The complete sketch is below.

```arduino

/*

  Basic Web Server

 A simple web server that replies with nothing, but prints the client's request

 and the server IP address.

 Circuit:

 * GSM shield attached

 created

 by David Cuartielles

 modified 21 Nov 2012

 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/GSMToolsTestWebServer

 This example code is part of the public domain

 */
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// APN data
#define GPRS_APN       "GPRS_APN" // replace your GPRS APN
#define GPRS_LOGIN     "login"    // replace with your GPRS login
#define GPRS_PASSWORD  "password" // replace with your GPRS password

// initialize the library instance

GPRS gprs;

GSM gsmAccess;     // include a 'true' parameter for debug enabled

GSMServer server(80); // port 80 (http default)

// timeout

const unsigned long __TIMEOUT__ = 10 * 1000;

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for Leonardo only

  }

  Serial.println("starting,..");

  // connection state

  bool connected = true;

  // Start GSM shield

  // If your SIM has PIN, pass it as a parameter of begin() in quotes

  while (!connected) {

    if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &

        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD) == GPRS_READY)) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  Serial.println("Connected to GPRS network");

  // start server

  server.begin();

  //Get IP.

  IPAddress LocalIP = gprs.getIPAddress();

  Serial.println("Server IP address=");

  Serial.println(LocalIP);
}

void loop() {

  GSMClient client = server.available();

  if (client) {

    if (client.available()) {

      Serial.write(client.read());

    }

  }

}
```


*Last revision 2018/08/23 by SM*