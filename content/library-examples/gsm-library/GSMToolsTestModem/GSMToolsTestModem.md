---
slug: '/en/Tutorial/LibraryExamples/GSMToolsTestModem'
date: 'February 05, 2018, at 08:43 PM'
title: 'GSMToolsTestModem'
description: 'Read the IMEI of your modem and print it in the Serial Monitor.'
---

## GSM Test Modem

This sketch tests the modem on the GSM shield to see if it is working correctly. You do not need a SIM card for this example.

## Hardware Required

- Arduino Board

- [Arduino + Telefonica GSM/GPRS Shield](/retired/shields/arduino-gsm-shield)

## Circuit

![image of the Arduino GSM Shield on top of an Arduino board](assets/GSMShield_ArduinoUno.jpg)



## Code

First, import the GSM library

`#include <GSM.h>`

Create an instance of the GSMModem class:

`GSMModem modem;`

Create a variable to hold the IMEI number of the modem

```arduino
String IMEI = "";
```

In `setup`, open a serial connection to the computer. After opening the connection, send a message indicating the sketch has started.

```arduino
void setup(){

  Serial.begin(9600);

  Serial.print("Starting modem test...");
```

Call `modem.begin()` to start the modem. Send a status message depending on the outcome, and end `setup()`.

```arduino
if(modem.begin())

    Serial.println("modem.begin() succeeded");

  else

    Serial.println("ERROR, no modem answer.");
}
```

Inside `loop`, use `modem.getIMEI()` to return the IMEI number of the modem. This number is unique to your GSM shield.

```arduino
void loop()
{

  // get modem IMEI

  Serial.print("Checking IMEI...");

  IMEI = modem.getIMEI();
```

If there is a valid response from `getIMEI()`, print it to the serial monitor and reset the modem with `modem.begin()`.

```arduino
if(IMEI != NULL)

  {

    // show IMEI in serial monitor

    Serial.println("Modem's IMEI: " + IMEI);

    // reset modem to check booting:

    Serial.print("Resetting modem...");

    modem.begin();
```

Once reset, check the IMEI again. If it is a valid return again, the modem is functioning as expected.

```arduino
if(modem.getIMEI() != NULL)

    {

      Serial.println("Modem is functioning properly");

    }
```

If, after resetting the modem, there is not a valid return from `getIMEI()`, report an error

```arduino
else

    {

      Serial.println("Error: getIMEI() failed after modem.begin()");

    }
```

If you never received an IMEI after starting the sketch, report it, and end the program.

```arduino
}

  else

  {

    Serial.println("Error: Could not get IMEI");

  }

  // do nothing:

  while(true);
}
```

Once your code is uploaded, open the serial monitor.  You should see the HTML of [http://arduino.cc](http://arduino.cc) print out on screen when it is received.

## Complete Sketch

The complete sketch is below.

```arduino

/*

 This example tests to see if the modem of the

 GSM shield is working correctly. You do not need

 a SIM card for this example.

 Circuit:

 * GSM shield attached

 Created 12 Jun 2012

 by David del Peral

 modified 21 Nov 2012

 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/GSMToolsTestModem

 This sample code is part of the public domain

 */

// libraries
#include <GSM.h>

// modem verification object

GSMModem modem;

// IMEI variable

String IMEI = "";

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for Leonardo only

  }

  // start modem test (reset and check response)

  Serial.print("Starting modem test...");

  if (modem.begin()) {

    Serial.println("modem.begin() succeeded");

  } else {

    Serial.println("ERROR, no modem answer.");

  }
}

void loop() {

  // get modem IMEI

  Serial.print("Checking IMEI...");

  IMEI = modem.getIMEI();

  // check IMEI response

  if (IMEI != NULL) {

    // show IMEI in serial monitor

    Serial.println("Modem's IMEI: " + IMEI);

    // reset modem to check booting:

    Serial.print("Resetting modem...");

    modem.begin();

    // get and check IMEI one more time

    if (modem.getIMEI() != NULL) {

      Serial.println("Modem is functioning properly");

    } else {

      Serial.println("Error: getIMEI() failed after modem.begin()");

    }

  } else {

    Serial.println("Error: Could not get IMEI");

  }

  // do nothing:

  while (true);
}
```


*Last revision 2018/08/23 by SM*