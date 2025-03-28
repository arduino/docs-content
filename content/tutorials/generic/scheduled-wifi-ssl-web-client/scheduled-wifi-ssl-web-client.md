---
title: 'Scheduled WiFi SSL Web Client'
description: 'Print an Arduino ASCII logo by using RTC.'
difficulty: intermediate
tags: 
  - RTC
  - Serial Monitor
libraries:
  - name: SPI Library
    url: https://www.arduino.cc/en/reference/SPI
  - name: WiFi101 Library
    url: https://www.arduino.cc/en/Reference/WiFi101
  - name: WiFiNINA Library
    url: https://www.arduino.cc/en/Reference/WiFiNINA
  - name: RTCZero Library
    url: https://www.arduino.cc/reference/en/libraries/rtczero/
hardware:
  - hardware/01.mkr/01.boards/mkr-1000-wifi
  - hardware/01.mkr/01.boards/mkr-wifi-1010
  - hardware/01.mkr/01.boards/mkr-vidor-4000
software:
  - ide-v1
  - ide-v2
  - web-editor
author: "Arduino"
contributeURL: content/tutorials/generic
---

## Introduction

With this tutorial you will use the Real Time Clock (RTC) alarm function and interrupt to make an https GET request to the Arduino.cc website every minute. The request downloads the Arduino ASCII logo and the data is streamed to the Serial Monitor.

## Goals


- To use the Real Time Clock (RTC)
- To make a GET request that downloads an Arduino ASCII logo and print it to the Serial Monitor.



## Hardware & Software Needed

- Arduino MKR1000 WiFi or Arduino MKR WiFi 1010, MKR Vidor 4000 [Link to store](https://store.arduino.cc/)
- Wi-Fi access to the Internet
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [SPI Library](https://www.arduino.cc/en/reference/SPI)
- [WiFi101 Library](https://www.arduino.cc/en/Reference/WiFi101)
- [WiFiNINA Library](https://www.arduino.cc/en/Reference/WiFiNINA) (For MKR WiFi 1010 or MKR VIDOR 4000)
- [RTCZero Library](https://www.arduino.cc/reference/en/libraries/rtczero/)


### The Circuit

No circuit is required for this tutorial. Simply connect your Arduino board to your computer and upload the sketch found in this tutorial to you IDE.

### Real Time Clock (RTC)

Isn't Real Time Clock just another word for actual time? The answer is yes, it is actually just the tracking of actual time. But what is interesting is the component that does this. Most electronic devices that need to track current time use an RTC component, often in the form of an Integrated Circuit (IC). They typically consist of a crystal oscillator, which is used to create electronic signals with a constant frequency. The frequency is typically set to 32.768 kHz, which is the same frequency used for most watches.

The frequency is equal to 2^15 cycles per second, which means it is a convenient rate to use for binary counter circuits. This operation also does not require a lot of power, and can still run while the board is in a sleep mode. This can be a quite powerful feature, to for example tell the board to wake up at a certain time, or go to sleep at a certain time, automatically.


## Programming the Board

**1.** First, let's make sure we have correct the drivers installed. If we are using the Cloud Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAMD boards (32-bits ARM Cortex-M0+)** and install it. 

**2.** Now, we need to install the libraries needed. Simply go to **Tools > Manage libraries...** and search for the libraries listed below and install them.



### Code
Before we begin, let's take a look at the libraries used and some of the core functions of the program:

### The Libraries


- `<SPI.h>` - This library allows you to communicate with SPI devices, with the Arduino as the controller device. In this tutorial the WiFi101 library uses it to control the WiFi radio. It is included for compatibillity with IDE versions before  1.6.5.



- `<WiFi101.h>` - This is the library shared across the old WiFi enabled boards to manage the connections to the Internet through WiFi.
  

**or**

- `<WiFiNINA.h>` - This is the library shared across the new WiFi enabled boards to manage the connections to the Internet through WiFi. **Please change `<WiFi101.h>` into `<WiFiNINA.h>` if you are using an Arduino MKR WiFi 1010 or MKR VIDOR 4000.**


- `<RTCZero.h>` - This library allows an Arduino Zero, MKR1000 or  MKR WiFi 1010 board to control and use the internal Real Time Clock. When an alarm is set, the board can be put in sleep mode, with very low power consumption, waiting to be woken up by the alarm. The RTC supports just one active alarm at a time.




### Functions Defined in the Sketch

- `printWifiStatus()` - Prints to Serial console a full set of information including the SSID of the network you're connected to, the local IP address and the signal strength.


- `alarmMatch()` - This is the function that is triggered by the interrupt set in the setup part. It is activated at every 00 seconds occurrence.


- `connectToAP()` - It uses the WiFi library functions to connect to the Access Point (AP) with Access point ID (SSID) and password embedded in the code. It also works with a WiFi shield.


- `httpRequest()` - This function prints the time on Serial console, then it sends out an HTTP GET request to Arduino.cc website.


- `listenToClient()` -Using millis() this function waits for 5 seconds the response from the Arduino.cc website and it prints out on Serial console any character received, then the client is closed.


- `print2digits(int number)` -An handy function that puts a leading zero to any single digit number to be printed on Serial console, offering a better formatting on screen.

***Note: Arduino.cc uses SHA 256 certificate. Be sure to connect to sites that use SHA 256, because SHA 348 is still not yet supported. Comodo for example has certificate SHA-348 with RSA encryption.***


Upload the sketch below to your board:


```arduino

/*

  Scheduled WiFi SSL Web Client for MKR1000

  This sketch connects to the Arduino website every minute and downloads the ASCII logo to display it on the serial monitor

  created 19 Jan 2016

  by Arturo Guadalupi <a.guadalupi@arduino.cc>

  https://docs.arduino.cc/tutorials/generic/scheduled-wifi-ssl-web-client

  This code is in the public domain.

*/

#include <SPI.h>
#include <WiFi101.h>
#include <RTCZero.h>

char ssid[] = "yourPassword";      //  your network SSID (name)
char pass[] = "yourNetwork";       // your network password
int keyIndex = 0;                  // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;

// Initialize the Wifi client library

WiFiSSLClient client;

// server address:
char server[] = "www.arduino.tips";

bool sendRequest = true; // used to understand if the http request must be sent

/* Create an rtc object */

RTCZero rtc;

/* Change these values to set the current initial time */

const byte seconds = 50;

const byte minutes = 00;

const byte hours = 17;

/* Change these values to set the current initial date */

const byte day = 17;

const byte month = 11;

const byte year = 15;

void setup() {

  //Initialize Serial and wait for port to open:

  Serial.begin(115200);

  connectToAP();    // connect the board to the access point

  printWifiStatus();

  httpRequest();

  listenToClient();

  rtc.begin();

  rtc.setTime(hours, minutes, seconds);

  rtc.setDate(day, month, year);

  rtc.setAlarmTime(0, 0, 0);    //in this way the request is sent every minute at 0 seconds

  rtc.enableAlarm(rtc.MATCH_SS);

  rtc.attachInterrupt(alarmMatch);
}

void loop() {

  if (sendRequest) {

    sendRequest = false;

    httpRequest();

    listenToClient();

  }
}

void printWifiStatus() {

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

void alarmMatch() {

  sendRequest = true;
}

void connectToAP() {

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to Wifi network:

  while ( status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);


    // wait 1 second for connection:

    delay(1000);

  }
}

// this method makes a HTTP connection to the server:
void httpRequest() {

  sendRequest = false;

  // Print request time

  Serial.println();

  Serial.print("Request sent @ ");

  print2digits(rtc.getHours());

  Serial.print(":");

  print2digits(rtc.getMinutes());

  Serial.print(":");

  print2digits(rtc.getSeconds());

  Serial.println();

  Serial.println();

  if (client.connect(server, 443)) {

    // Make a HTTP request:

    client.println("GET /asciilogo.txt HTTP/1.1");

    client.println("Host: www.arduino.tips");

    client.println("Connection: close");

    client.println();

  }

  else {

    Serial.println("connection failed");

  }
}

void listenToClient()
{

  unsigned long startTime = millis();

  bool received = false;

  while ((millis() - startTime < 5000) && !received) { //try to listen for 5 seconds

    while (client.available()) {

      received = true;

      char c = client.read();

      Serial.write(c);

    }

  }

  client.stop();

  Serial.println();
}

void print2digits(int number) {

  if (number < 10) {

    Serial.print("0");

  }

  Serial.print(number);
}
```

## Testing It Out

We want to get an alarm every minute with the RTC functions. We use `rtc.setAlarmSeconds( 0);` and then `rtc.enableAlarm(rtc.MATCH_SS);`. The first functions sets at "00" the value of seconds to compare; the second function enables the alarm and sets its trigger on the match of the actual time and the set value for seconds. The condition is met every time the seconds digits go to "00", that is every minute. When the condition is met, the RTC generates an interrupt request. 

The request is serviced by the function `alarmMatch` that sets to **true** the flag `sendRequest` used by the main loop. There, If this flag is true, the request to the Arduino.cc site is made, otherwise nothing is done. This solution allows you to do something else between the interrupts because the code execution flows without being blocked by any big `delay()` function. Please remember that RTC resets every time the board is powered up. After having uploaded the code, you should see an ASCII Arduino logo being printed on the Serial Monitor.

![Arduino ASCII logo](assets/arduinoASCII.png)

### Troubleshoot
If the code is not working, there are some common issues we can troubleshoot:

- You have not installed the correct drivers for the board.
- You have not installed the correct libraries.
- Your `ssid` or `pass` is incorrect.
- You are using an incorrect configuration for your network type. 

## Conclusion

In this tutorial we have used RTC and interrupt to make a GET request to the arduino.cc website. This request downloads an Arduino ASCII logo which is printed to the Serial Monitor in the IDE. 