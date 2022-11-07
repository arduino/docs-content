---
author: 'Arduino'
description: 'This example connects to a named server using an Ethernet shield.'
title: 'Ethernet Shield DnsWebClient'
tags: [Ethernet]

---


## DNS Web Client

This example connects to a named server using an Ethernet shield.  The sketch illustrates how to connect using DHCP and DNS. When calling Ethernet.begin(mac), the Etehrnet library attempts to obtain an IP address using DHCP. Using DHCP significantly adds to the sketch size; be sure there is enough space to run the program.

DNS lookup happens when client.connect(**servername**,port) is called. **servername** is a URL string, like `"www.arduino.cc"`.

## Hardware Required

- Arduino Ethernet Shield

- Shield-compatible Arduino board

## Circuit

The Ethernet shield allows you to connect a WizNet Ethernet controller to the Arduino via the SPI bus. It uses pins 10, 11, 12, and 13 for the SPI connection to the WizNet.  Later models of the Ethernet shield also have an SD Card on board. Digital pin 4 is used to control the slave select pin on the SD card.

The shield should be connected to a network with an ethernet cable. You will need to change the network settings in the program to correspond to your network.

![The circuit for this example.](assets/ArduinoPlusEthernetShield.png)



***In the above  image, your Arduino would be stacked below the Ethernet shield.***

## Code

```arduino
/*

  DNS and DHCP-based Web client

 This sketch connects to a website (http://www.google.com)

 using an Arduino Wiznet Ethernet shield.

 Circuit:

 * Ethernet shield attached to pins 10, 11, 12, 13

 created 18 Dec 2009

 by David A. Mellis

 modified 9 Apr 2012

 by Tom Igoe, based on work by Adrian McEwen

 */

#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield
byte mac[] = {  0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x02 };
char serverName[] = "www.google.com";

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):

EthernetClient client;

void setup() {

 // Open serial communications and wait for port to open:

  Serial.begin(9600);

   while (!Serial) {

    ; // wait for serial port to connect. Needed for Leonardo only

  }

  // start the Ethernet connection:

  if (Ethernet.begin(mac) == 0) {

    Serial.println("Failed to configure Ethernet using DHCP");

    // no point in carrying on, so do nothing forevermore:

    while(true);

  }

  // give the Ethernet shield a second to initialize:

  delay(1000);

  Serial.println("connecting...");

  // if you get a connection, report back via serial:

  if (client.connect(serverName, 80)) {

    Serial.println("connected");

    // Make a HTTP request:

    client.println("GET /search?q=arduino HTTP/1.0");

    client.println();

  }

  else {

    // kf you didn't get a connection to the server:

    Serial.println("connection failed");

  }
}

void loop()
{

  // if there are incoming bytes available

  // from the server, read them and print them:

  if (client.available()) {

    char c = client.read();

    Serial.print(c);

  }

  // if the server's disconnected, stop the client:

  if (!client.connected()) {

    Serial.println();

    Serial.println("disconnecting.");

    client.stop();

    // do nothing forevermore:

    while(true);

  }
}
```

