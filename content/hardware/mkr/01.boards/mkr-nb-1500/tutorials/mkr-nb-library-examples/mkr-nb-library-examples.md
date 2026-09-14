---
title: 'MKR NB Library Examples'
description: 'A series of examples related to the MKRNB Library, which can be used to send data over the LTE Cat M1/NB1 bands, make voice calls, and sending SMS, using a enabled SIM card.'
tags: [NB-IoT, LTE]
author: 'Arduino'
---

The [Arduino MKR NB 1500](https://store.arduino.cc/products/arduino-mkr-nb-1500) is a powerful IoT board that can communicate over LTE-M, NB-IoT and EGPRS networks. In this article, you will find a lot of useful examples, such as sending SMS, making voice calls and making http requests. All examples are available in the [MKRNB library](https://www.arduino.cc/reference/en/libraries/mkrnb/), which is available for download through the [Arduino IDE](https://www.arduino.cc/en/main/software) library manager.

You can also visit the [MKRGSM GitHub repository](https://github.com/arduino-libraries/MKRNB) to learn more about this library.

## Hardware Required

- [Arduino MKR NB 1500](https://store.arduino.cc/products/arduino-mkr-nb-1500)
- Antenna
- SIM card enable for Data

## Circuit

![Connect the antenna to the board.](assets/mkr-nb-circuit.png)

## Examples

### MKR NB GPRS Udp Ntp Client

In this example, you will use your MKR NB 1500, to query a Network Time Protocol (NTP) server. In this way, your board can get the time from the Internet.

```arduino
/*

  Udp NTP Client

  Get the time from a Network Time Protocol (NTP) time server

  Demonstrates use of UDP sendPacket and ReceivePacket

  For more on NTP time servers and the messages needed to communicate with them,

  see http://en.wikipedia.org/wiki/Network_Time_Protocol

  created 4 Sep 2010

  by Michael Margolis

  modified 9 Apr 2012

  by Tom Igoe

  modified 6 Dec 2017 ported from WiFi101 to MKRGSM

  by Arturo Guadalupi



  This code is in the public domain.

*/

#include <MKRNB.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;

unsigned int localPort = 2390;      // local port to listen for UDP packets

IPAddress timeServer(129, 6, 15, 28); // time.nist.gov NTP server

const int NTP_PACKET_SIZE = 48; // NTP time stamp is in the first 48 bytes of the message

byte packetBuffer[ NTP_PACKET_SIZE]; //buffer to hold incoming and outgoing packets

// initialize the library instance

NBClient client;

GPRS gprs;

NB nbAccess;

// A UDP instance to let us send and receive packets over UDP

NBUDP Udp;

void setup()
{

  // Open serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("Starting Arduino GPRS NTP client.");

  // connection state

  boolean connected = false;

  // After starting the modem with NB.begin()

  // attach the shield to the GPRS network with the APN, login and password

  while (!connected) {

    if ((nbAccess.begin(PINNUMBER) == NB_READY) &&

        (gprs.attachGPRS() == GPRS_READY)) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  Serial.println("\nStarting connection to server...");

  Udp.begin(localPort);
}

void loop()
{

  sendNTPpacket(timeServer); // send an NTP packet to a time server

  // wait to see if a reply is available

  delay(1000);

  if ( Udp.parsePacket() ) {

    Serial.println("packet received");

    // We've received a packet, read the data from it

    Udp.read(packetBuffer, NTP_PACKET_SIZE); // read the packet into the buffer

    //the timestamp starts at byte 40 of the received packet and is four bytes,

    // or two words, long. First, esxtract the two words:

    unsigned long highWord = word(packetBuffer[40], packetBuffer[41]);

    unsigned long lowWord = word(packetBuffer[42], packetBuffer[43]);

    // combine the four bytes (two words) into a long integer

    // this is NTP time (seconds since Jan 1 1900):

    unsigned long secsSince1900 = highWord << 16 | lowWord;

    Serial.print("Seconds since Jan 1 1900 = " );

    Serial.println(secsSince1900);

    // now convert NTP time into everyday time:

    Serial.print("Unix time = ");

    // Unix time starts on Jan 1 1970. In seconds, that's 2208988800:

    const unsigned long seventyYears = 2208988800UL;

    // subtract seventy years:

    unsigned long epoch = secsSince1900 - seventyYears;

    // print Unix time:

    Serial.println(epoch);

    // print the hour, minute and second:

    Serial.print("The UTC time is ");       // UTC is the time at Greenwich Meridian (GMT)

    Serial.print((epoch  % 86400L) / 3600); // print the hour (86400 equals secs per day)

    Serial.print(':');

    if ( ((epoch % 3600) / 60) < 10 ) {

      // In the first 10 minutes of each hour, we'll want a leading '0'

      Serial.print('0');

    }

    Serial.print((epoch  % 3600) / 60); // print the minute (3600 equals secs per minute)

    Serial.print(':');

    if ( (epoch % 60) < 10 ) {

      // In the first 10 seconds of each minute, we'll want a leading '0'

      Serial.print('0');

    }

    Serial.println(epoch % 60); // print the second

  }

  // wait ten seconds before asking for the time again

  delay(10000);
}

// send an NTP request to the time server at the given address
unsigned long sendNTPpacket(IPAddress& address)
{

  //Serial.println("1");

  // set all bytes in the buffer to 0

  memset(packetBuffer, 0, NTP_PACKET_SIZE);

  // Initialize values needed to form NTP request

  // (see URL above for details on the packets)

  //Serial.println("2");

  packetBuffer[0] = 0b11100011;   // LI, Version, Mode

  packetBuffer[1] = 0;     // Stratum, or type of clock

  packetBuffer[2] = 6;     // Polling Interval

  packetBuffer[3] = 0xEC;  // Peer Clock Precision

  // 8 bytes of zero for Root Delay & Root Dispersion

  packetBuffer[12]  = 49;

  packetBuffer[13]  = 0x4E;

  packetBuffer[14]  = 49;

  packetBuffer[15]  = 52;

  //Serial.println("3");

  // all NTP fields have been given values, now

  // you can send a packet requesting a timestamp:

  Udp.beginPacket(address, 123); //NTP requests are to port 123

  //Serial.println("4");

  Udp.write(packetBuffer, NTP_PACKET_SIZE);

  //Serial.println("5");

  Udp.endPacket();

  //Serial.println("6");
}
```

### MKR NB NBSSL Web Client

This sketch connects an Arduino MKR NB 1500 board to [https://example.org](https://example.org), through the NB network. It then prints the content of the page through the serial monitor of the Arduino Software (IDE).

Before you start, please double check with your cellular company if they allow connections to the "Open Internet" (means that you can connect to every website).

NB and CATM1 connectivity access can be restricted to some endpoints for security reasons.

```arduino
/*

  SSL Web client

 This sketch connects to a website using SSL through a MKR NB 1500 board. Specifically,

 this example downloads the URL "http://arduino.tips/asciilogo.txt" and

 prints it to the Serial monitor.

 Circuit:

 * MKR NB 1500 board

 * Antenna

 * SIM card with a data plan

 created 8 Mar 2012

 by Tom Igoe

*/

// libraries
#include <MKRNB.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;

// initialize the library instance

NBSSLClient client;

GPRS gprs;

NB nbAccess;

// URL, path and port (for example: arduino.cc)
char server[] = "arduino.tips";
char path[] = "/asciilogo.txt";
int port = 443; // port 443 is the default for HTTPS

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("Starting Arduino web client.");

  // connection state

  boolean connected = false;

  // After starting the modem with NB.begin()

  // attach to the GPRS network with the APN, login and password

  while (!connected) {

    if ((nbAccess.begin(PINNUMBER) == NB_READY) &&

        (gprs.attachGPRS() == GPRS_READY)) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  Serial.println("connecting...");

  // if you get a connection, report back via serial:

  if (client.connect(server, port)) {

    Serial.println("connected");

    // Make a HTTP request:

    client.print("GET ");

    client.print(path);

    client.println(" HTTP/1.1");

    client.print("Host: ");

    client.println(server);

    client.println("Connection: close");

    client.println();

  } else {

    // if you didn't get a connection to the server:

    Serial.println("connection failed");

  }
}

void loop() {

  // if there are incoming bytes available

  // from the server, read them and print them:

  if (client.available()) {

    char c = client.read();

    Serial.print(c);

  }

  // if the server's disconnected, stop the client:

  if (!client.available() && !client.connected()) {

    Serial.println();

    Serial.println("disconnecting.");

    client.stop();

    // do nothing forevermore:

    for (;;)

      ;

  }
}
```

### MKR NB NB Web Client

This sketch connects an Arduino MKR NB 1500 board to the Arduino homepage, through the NB network. It then prints the content of the page through the serial monitor of the Arduino Software (IDE).

```arduino

/*

  Web client

  This sketch connects to a website through a MKR NB 1500 board. Specifically,

  this example downloads the URL "http://example.org/" and

  prints it to the Serial monitor.

  Circuit:

   - MKR NB 1500 board

   - Antenna

   - SIM card with a data plan

  created 8 Mar 2012

  by Tom Igoe

*/

// libraries
#include <MKRNB.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;

// initialize the library instance

NBClient client;

GPRS gprs;

NB nbAccess;

// URL, path and port (for example: example.org)
char server[] = "example.org";
char path[] = "/";
int port = 80; // port 80 is the default for HTTP

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("Starting Arduino web client.");

  // connection state

  boolean connected = false;

  // After starting the modem with NB.begin()

  // attach to the GPRS network with the APN, login and password

  while (!connected) {

    if ((nbAccess.begin(PINNUMBER) == NB_READY) &&

        (gprs.attachGPRS() == GPRS_READY)) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  Serial.println("connecting...");

  // if you get a connection, report back via serial:

  if (client.connect(server, port)) {

    Serial.println("connected");

    // Make a HTTP request:

    client.print("GET ");

    client.print(path);

    client.println(" HTTP/1.1");

    client.print("Host: ");

    client.println(server);

    client.println("Connection: close");

    client.println();

  } else {

    // if you didn't get a connection to the server:

    Serial.println("connection failed");

  }
}

void loop() {

  // if there are incoming bytes available

  // from the server, read them and print them:

  if (client.available()) {

    Serial.print((char)client.read());

  }

  // if the server's disconnected, stop the client:

  if (!client.available() && !client.connected()) {

    Serial.println();

    Serial.println("disconnecting.");

    client.stop();

    // do nothing forevermore:

    for (;;)

      ;

  }
}
```

### MKR NB Scan Networks

This example prints out the IMEI number of the modem, then checks to see if it's connected to a carrier and prints out its signal strength. It also scans for all nearby networks.

```arduino

/*

 NB Scan Networks

 This example prints out the IMEI number of the modem,

 then checks to see if it's connected to a carrier.

 Then it scans for nearby networks and prints out their signal strengths.

 Circuit:

 * MKR NB 1500 board

 * Antenna

 * SIM card

 Created 8 Mar 2012

 by Tom Igoe, implemented by Javier Carazo

 Modified 4 Feb 2013

 by Scott Fitzgerald

*/

// libraries
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

### MKR NB Pin Management

This example is part of the tools supplied for the Arduino MKR NB 1500 and helps you change or remove the PIN of a SIM card.

```arduino

/*

 This example enables you to change or remove the PIN number of

 a SIM card inserted into a MKR NB 1500 board.

 Circuit:

 * MKR NB 1500 board

 * Antenna

 * SIM card

 Created 12 Jun 2012

 by David del Peral

*/

// libraries
#include <MKRNB.h>

// pin manager object

NBPIN PINManager;

// save input in serial by user

String user_input = "";

// authenticated with PIN code
boolean auth = false;

// serial monitor result messages

String oktext = "OK";

String errortext = "ERROR";

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for Leonardo only

  }

  Serial.println("Change PIN example\n");

  PINManager.begin();

  // check if the SIM have pin lock

  while (!auth) {

    int pin_query = PINManager.isPIN();

    if (pin_query == 1) {

      // if SIM is locked, enter PIN code

      Serial.print("Enter PIN code: ");

      user_input = readSerial();

      // check PIN code

      if (PINManager.checkPIN(user_input) == 0) {

        auth = true;

        PINManager.setPINUsed(true);

        Serial.println(oktext);

      } else {

        // if PIN code was incorrected

        Serial.println("Incorrect PIN. Remember that you have 3 opportunities.");

      }

    } else if (pin_query == -1) {

      // PIN code is locked, user must enter PUK code

      Serial.println("PIN locked. Enter PUK code: ");

      String puk = readSerial();

      Serial.print("Now, enter a new PIN code: ");

      user_input = readSerial();

      // check PUK code

      if (PINManager.checkPUK(puk, user_input) == 0) {

        auth = true;

        PINManager.setPINUsed(true);

        Serial.println(oktext);

      } else {

        // if PUK o the new PIN are incorrect

        Serial.println("Incorrect PUK or invalid new PIN. Try again!.");

      }

    } else if (pin_query == -2) {

      // the worst case, PIN and PUK are locked

      Serial.println("PIN and PUK locked. Use PIN2/PUK2 in a mobile phone.");

      while (true);

    } else {

      // SIM does not requires authentication

      Serial.println("No pin necessary.");

      auth = true;

    }

  }

  // start module

  Serial.print("Checking register in NB IoT / LTE Cat M1 network...");

  if (PINManager.checkReg() == 0) {

    Serial.println(oktext);

  }

  // if you are connect by roaming

  else if (PINManager.checkReg() == 1) {

    Serial.println("ROAMING " + oktext);

  } else {

    // error connection

    Serial.println(errortext);

    while (true);

  }
}

void loop() {

  // Function loop implements pin management user menu

  // Only if you SIM use pin lock, you can change PIN code

  // user_op variables save user option

  Serial.println("Choose an option:\n1 - On/Off PIN.");

  if (PINManager.getPINUsed()) {

    Serial.println("2 - Change PIN.");

  }

  String user_op = readSerial();

  if (user_op == "1") {

    Serial.println("Enter your PIN code:");

    user_input = readSerial();

    // activate/deactivate PIN lock

    PINManager.switchPIN(user_input);

  } else if (user_op == "2" && PINManager.getPINUsed()) {

    Serial.println("Enter your actual PIN code:");

    String oldPIN = readSerial();

    Serial.println("Now, enter your new PIN code:");

    String newPIN = readSerial();

    // change PIN

    PINManager.changePIN(oldPIN, newPIN);

  } else {

    Serial.println("Incorrect option. Try again!.");

  }

  delay(1000);
}

/*

  Read input serial

 */

String readSerial() {

  String text = "";

  while (1) {

    while (Serial.available() > 0) {

      char inChar = Serial.read();

      if (inChar == '\n') {

        return text;

      }

      if (inChar != '\r') {

        text += inChar;

      }

    }

  }
}
```


### MKR NB Test GPRS

This sketch tests the GPRS data connection on the Arduino MKR NB 1500. It  tries to connect to arduino.cc.

To use a data connection with the MKR NB 1500, you'll need your provider's Access Point Name (APN), login, and password. To obtain this information, contact the network provider for the most up to date information. [This page](http://wiki.apnchanger.org/) has some information about various carrier settings, but it may not be current.

```arduino

/*

 This sketch test the MKR NB 1500 board's ability to connect to a

 GPRS network. It asks for APN information through the

 serial monitor and tries to connect to example.org.

 Circuit:

 * MKR NB 1500 board

 * Antenna

 * SIM card with data plan

 Created 18 Jun 2012

 by David del Peral

*/

// libraries
#include <MKRNB.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instance

NB nbAccess;        // NB access: include a 'true' parameter for debug enabled

GPRS gprsAccess;  // GPRS access

NBClient client;  // Client service for TCP connection

// messages for serial monitor response

String oktext = "OK";

String errortext = "ERROR";

// URL and path (for example: example.org)
char url[] = "example.org";
char urlproxy[] = "http://example.org";
char path[] = "/";

// variable for save response obtained

String response = "";

// use a proxy
boolean use_proxy = false;

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for Leonardo only

  }
}

void loop() {

  use_proxy = false;

  // start module

  // if your SIM has PIN, pass it as a parameter of begin() in quotes

  Serial.print("Connecting NB IoT / LTE Cat M1 network...");

  if (nbAccess.begin(PINNUMBER) != NB_READY) {

    Serial.println(errortext);

    while (true);

  }

  Serial.println(oktext);

  // attach GPRS

  Serial.println("Attaching to GPRS...");

  if (gprsAccess.attachGPRS() != GPRS_READY) {

    Serial.println(errortext);

  } else {

    Serial.println(oktext);

    // read proxy introduced by user

    char proxy[100];

    Serial.print("If your carrier uses a proxy, enter it, if not press enter: ");

    readSerial(proxy);

    Serial.println(proxy);

    // if user introduced a proxy, asks him for proxy port

    int pport;

    if (proxy[0] != '\0') {

      // read proxy port introduced by user

      char proxyport[10];

      Serial.print("Enter the proxy port: ");

      readSerial(proxyport);

      // cast proxy port introduced to integer

      pport = (int) proxyport;

      use_proxy = true;

      Serial.println(proxyport);

    }

    // connection with example.org and realize HTTP request

    Serial.print("Connecting and sending GET request to example.org...");

    int res_connect;

    // if use a proxy, connect with it

    if (use_proxy) {

      res_connect = client.connect(proxy, pport);

    } else {

      res_connect = client.connect(url, 80);

    }

    if (res_connect) {

      // make a HTTP 1.0 GET request (client sends the request)

      client.print("GET ");

      // if use a proxy, the path is example.org URL

      if (use_proxy) {

        client.print(urlproxy);

      } else {

        client.print(path);

      }

      client.println(" HTTP/1.1");

      client.print("Host: ");

      client.println(url);

      client.println("Connection: close");

      client.println();

      Serial.println(oktext);

    } else {

      // if you didn't get a connection to the server

      Serial.println(errortext);

    }

    Serial.print("Receiving response...");

    boolean test = true;

    while (test) {

      // if there are incoming bytes available

      // from the server, read and check them

      if (client.available()) {

        char c = client.read();

        response += c;

        // cast response obtained from string to char array

        char responsechar[response.length() + 1];

        response.toCharArray(responsechar, response.length() + 1);

        // if response includes a "200 OK" substring

        if (strstr(responsechar, "200 OK") != NULL) {

          Serial.println(oktext);

          Serial.println("TEST COMPLETE!");

          test = false;

        }

      }

      // if the server's disconnected, stop the client:

      if (!client.connected()) {

        Serial.println();

        Serial.println("disconnecting.");

        client.stop();

        test = false;

      }

    }

  }
}

/*

  Read input serial

 */
int readSerial(char result[]) {

  int i = 0;

  while (1) {

    while (Serial.available() > 0) {

      char inChar = Serial.read();

      if (inChar == '\n') {

        result[i] = '\0';

        return 0;

      }

      if (inChar != '\r') {

        result[i] = inChar;

        i++;

      }

    }

  }
}
```


### MKR NB Test Modem

This sketch tests the modem on the MKR NB 1500 to see if it is working correctly. You do not need a SIM card for this example.

```arduino

/*

 This example tests to see if the modem of the

 MKR NB 1500 board is working correctly. You do not need

 a SIM card for this example.

 Circuit:

 * MKR NB 1500 board

 * Antenna

 Created 12 Jun 2012

 by David del Peral

 modified 21 Nov 2012

 by Tom Igoe

*/

// libraries
#include <MKRNB.h>

// modem verification object

NBModem modem;

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