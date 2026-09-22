---
title: 'MKRGSM Library Examples'
description: 'A list of examples related to the MKRGSM Library, which can be used to make voice calls, send SMS and connect to website with a data enabled SIM card.'
tags: [GSM, SMS, Voice Calls]
author: Arduino
---

The [Arduino MKR GSM 1400](https://store.arduino.cc/mkr-gsm-1400) is a powerful IoT board that communicates over the mobile network. In this article, you will find a lot of useful examples, such as sending SMS, making voice calls and making http requests. All examples are available in the [MKRGSM library](https://www.arduino.cc/reference/en/libraries/mkrgsm/), which is available for download through the [Arduino IDE](https://www.arduino.cc/en/main/software) library manager.

You can also visit the [MKRGSM GitHub repository](https://github.com/arduino-libraries/MKRGSM) to learn more about this library.

## Hardware & Software Required

- [Arduino MKR GSM 1400](https://store.arduino.cc/mkr-gsm-1400)
- Antenna
- SIM card enable for Data
- (optional) 6 potentiometers or other analog inputs attached to A0-A5  

## Circuit

![Connect the antenna to the board.](assets/mkr-gsm-circuit.png)

## Examples

### MKR GSM GPRS Ping

This sketch connects an host and continuously ping it.

```arduino
/*

 This uses an MKR GSM 1400 to continuously pings given host specified by IP Address or name.

Circuit:

* MKR GSM 1400 board

* Antenna

* SIM card with a data plan

 created 06 Dec 2017

 by Arturo Guadalupi

*/
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;
// APN data

const char GPRS_APN[]      = SECRET_GPRS_APN;

const char GPRS_LOGIN[]    = SECRET_GPRS_LOGIN;

const char GPRS_PASSWORD[] = SECRET_GPRS_PASSWORD;

// initialize the library instance

GSMSSLClient client;

GPRS gprs;

GSM gsmAccess;

// Specify IP address or hostname

String hostName = "www.google.com";
int pingResult;

void setup() {

 // Initialize serial and wait for port to open:

 Serial.begin(9600);

 while (!Serial) {

   ; // wait for serial port to connect. Needed for native USB port only

 }

 Serial.println("Starting Arduino GPRS ping.");

 // connection state

 bool connected = false;

 // After starting the modem with GSM.begin()

 // attach the shield to the GPRS network with the APN, login and password

 while (!connected) {

   if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &&

       (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD) == GPRS_READY)) {

     connected = true;

   } else {

     Serial.println("Not connected");

     delay(1000);

   }

 }
}

void loop() {

 Serial.print("Pinging ");

 Serial.print(hostName);

 Serial.print(": ");

 pingResult = gprs.ping(hostName);

 if (pingResult >= 0) {

   Serial.print("SUCCESS! RTT = ");

   Serial.print(pingResult);

   Serial.println(" ms");

 } else {

   Serial.print("FAILED! Error code: ");

   Serial.println(pingResult);

 }

 delay(5000);
}
```

### MKR GSM GPRS Udp Ntp

In this example, you will use your MKR GSM 1400, to query a Network Time Protocol (NTP) server. In this way, your board can get the time from the Internet.

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

#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;
// APN data

const char GPRS_APN[]      = SECRET_GPRS_APN;

const char GPRS_LOGIN[]    = SECRET_GPRS_LOGIN;

const char GPRS_PASSWORD[] = SECRET_GPRS_PASSWORD;

unsigned int localPort = 2390;      // local port to listen for UDP packets

IPAddress timeServer(129, 6, 15, 28); // time.nist.gov NTP server

const int NTP_PACKET_SIZE = 48; // NTP time stamp is in the first 48 bytes of the message

byte packetBuffer[ NTP_PACKET_SIZE]; //buffer to hold incoming and outgoing packets

// initialize the library instance

GSMClient client;

GPRS gprs;

GSM gsmAccess;

// A UDP instance to let us send and receive packets over UDP

GSMUDP Udp;

void setup()
{

  // Open serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("Starting Arduino GPRS NTP client.");

  // connection state

  bool connected = false;

  // After starting the modem with GSM.begin()

  // attach the shield to the GPRS network with the APN, login and password

  while (!connected) {

    if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &&

        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD) == GPRS_READY)) {

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

### MKR GSM Make Voice Call

Get your board to make phone calls from the Serial Monitor.

```arduino

/*

 Make Voice Call

 This sketch, for the MKR GSM 1400 board, puts a voice call to

 a remote phone number that you enter through the serial monitor.

 To make it work, open the serial monitor, and when you see the

 READY message, type a phone number. Make sure the serial monitor

 is set to send a just newline when you press return.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

* SIM card that can send voice calls

 created Mar 2012

 by Javier Zorzano

*/

// libraries
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instance

GSM gsmAccess; // include a 'true' parameter for debug enabled

GSMVoiceCall vcs;

String remoteNumber = "";  // the number you will call
char charbuffer[20];

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("Make Voice Call");

  // connection state

  bool connected = false;

  // Start GSM shield

  // If your SIM has PIN, pass it as a parameter of begin() in quotes

  while (!connected) {

    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  Serial.println("GSM initialized.");

  Serial.println("Enter phone number to call.");

}

void loop() {

  // add any incoming characters to the String:

  while (Serial.available() > 0) {

    char inChar = Serial.read();

    // if it's a newline, that means you should make the call:

    if (inChar == '\n') {

      // make sure the phone number is not too long:

      if (remoteNumber.length() < 20) {

        // let the user know you're calling:

        Serial.print("Calling to : ");

        Serial.println(remoteNumber);

        Serial.println();

        // Call the remote number

        remoteNumber.toCharArray(charbuffer, 20);

        // Check if the receiving end has picked up the call

        if (vcs.voiceCall(charbuffer)) {

          Serial.println("Call Established. Enter line to end");

          // Wait for some input from the line

          while (Serial.read() != '\n' && (vcs.getvoiceCallStatus() == TALKING));

          // And hang up

          vcs.hangCall();

        }

        Serial.println("Call Finished");

        remoteNumber = "";

        Serial.println("Enter phone number to call.");

      } else {

        Serial.println("That's too long for a phone number. I'm forgetting it");

        remoteNumber = "";

      }

    } else {

      // add the latest character to the message to send:

      if (inChar != '\r') {

        remoteNumber += inChar;

      }

    }

  }
}
```

### MKR GSM Receive SMS

This sketch waits for an SMS message and prints it to the serial monitor. It uses the GSM library of the Arduino GSM Shield and an active SIM card. To operate, the SIM card doesn't need a data plan.

```arduino
/*

 SMS receiver

 This sketch, for the MKR GSM 1400 board, waits for a SMS message

 and displays it through the Serial port.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card that can receive SMS messages

 created 25 Feb 2012

 by Javier Zorzano / TD

*/

// include the GSM library
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instances

GSM gsmAccess;

GSM_SMS sms;

// Array to hold the number a SMS is retrieved from
char senderNumber[20];

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("SMS Messages Receiver");

  // connection state

  bool connected = false;

  // Start GSM connection

  while (!connected) {

    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  Serial.println("GSM initialized");

  Serial.println("Waiting for messages");
}

void loop() {

  int c;

  // If there are any SMSs available()

  if (sms.available()) {

    Serial.println("Message received from:");

    // Get remote number

    sms.remoteNumber(senderNumber, 20);

    Serial.println(senderNumber);

    // An example of message disposal

    // Any messages starting with # should be discarded

    if (sms.peek() == '#') {

      Serial.println("Discarded SMS");

      sms.flush();

    }

    // Read message bytes and print them

    while ((c = sms.read()) != -1) {

      Serial.print((char)c);

    }

    Serial.println("\nEND OF MESSAGE");

    // Delete message from modem memory

    sms.flush();

    Serial.println("MESSAGE DELETED");

  }

  delay(1000);

}
```

### MKR GSM Receive Voice Call

This sketch receives a voice call from an Arduino MKR GSM 1400. Once the call is received and connected, it shows the number that is calling, and hangs up.

```arduino
/*

 Receive Voice Call

 This sketch, for the MKR GSM 1400 board, receives voice calls,

 displays the calling number, waits a few seconds then hangs up.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card that can accept voice calls

 created Mar 2012

 by Javier Zorzano

*/

// Include the GSM library
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instance

GSM gsmAccess;

GSMVoiceCall vcs;

// Array to hold the number for the incoming call
char numtel[20];

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("Receive Voice Call");

  // connection state

  bool connected = false;

  // Start GSM shield

  // If your SIM has PIN, pass it as a parameter of begin() in quotes

  while (!connected) {

    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  // This makes sure the modem correctly reports incoming events

  vcs.hangCall();

  Serial.println("Waiting for a call");
}

void loop() {

  // Check the status of the voice call

  switch (vcs.getvoiceCallStatus()) {

    case IDLE_CALL: // Nothing is happening

      break;

    case RECEIVINGCALL: // Yes! Someone is calling us

      Serial.println("RECEIVING CALL");

      // Retrieve the calling number

      vcs.retrieveCallingNumber(numtel, 20);

      // Print the calling number

      Serial.print("Number:");

      Serial.println(numtel);

      // Answer the call, establish the call

      vcs.answerCall();

      break;

    case TALKING:  // In this case the call would be established

      Serial.println("TALKING. Press enter to hang up.");

      while (Serial.read() != '\n') {

        delay(100);

      }

      vcs.hangCall();

      Serial.println("Hanging up and waiting for the next call.");

      break;

  }

  delay(1000);
}
```


### MKR GSM Send SMS

This sketch send a SMS message from an Arduino MKR GSM 1400. Using the serial monitor of the Arduino Software (IDE), you'll enter the number to connect with, and the text message to send.

```arduino
/*

 SMS sender

 This sketch, for the MKR GSM 1400 board,sends an SMS message

 you enter in the serial monitor. Connect your Arduino with the

 GSM shield and SIM card, open the serial monitor, and wait for

 the "READY" message to appear in the monitor. Next, type a

 message to send and press "return". Make sure the serial

 monitor is set to send a newline when you press return.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card that can send SMS

 created 25 Feb 2012

 by Tom Igoe

*/

// Include the GSM library
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instance

GSM gsmAccess;

GSM_SMS sms;

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  Serial.println("SMS Messages Sender");

  // connection state

  bool connected = false;

  // Start GSM shield

  // If your SIM has PIN, pass it as a parameter of begin() in quotes

  while (!connected) {

    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {

      connected = true;

    } else {

      Serial.println("Not connected");

      delay(1000);

    }

  }

  Serial.println("GSM initialized");
}

void loop() {

  Serial.print("Enter a mobile number: ");

  char remoteNum[20];  // telephone number to send sms

  readSerial(remoteNum);

  Serial.println(remoteNum);

  // sms text

  Serial.print("Now, enter SMS content: ");

  char txtMsg[200];

  readSerial(txtMsg);

  Serial.println("SENDING");

  Serial.println();

  Serial.println("Message:");

  Serial.println(txtMsg);

  // send the message

  sms.beginSMS(remoteNum);

  sms.print(txtMsg);

  sms.endSMS();

  Serial.println("\nCOMPLETE!\n");
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

        Serial.flush();

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

### MKR GSM SSL Web Client

This sketch connects an Arduino MKR GSM 1400 board to the Arduino homepage, through the GSM network. It then prints the content of the page through the serial monitor of the Arduino Software (IDE).

```arduino
/*
  Web client

 This sketch connects to a website using SSL through a MKR GSM 1400 board. Specifically,

 this example downloads the URL "http://arduino.tips/asciilogo.txt" and

 prints it to the Serial monitor.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card with a data plan

 created 8 Mar 2012

 by Tom Igoe

*/

// libraries
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;
// APN data

const char GPRS_APN[]      = SECRET_GPRS_APN;

const char GPRS_LOGIN[]    = SECRET_GPRS_LOGIN;

const char GPRS_PASSWORD[] = SECRET_GPRS_PASSWORD;

// initialize the library instance

GSMSSLClient client;

GPRS gprs;

GSM gsmAccess;

// URL, path and port (for example: arduino.tips)
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

  bool connected = false;

  // After starting the modem with GSM.begin()

  // attach the shield to the GPRS network with the APN, login and password

  while (!connected) {

    if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &&

        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD) == GPRS_READY)) {

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

### MKR GSM Web Client

This sketch connects an Arduino MKR GSM 1400 board to the Arduino homepage, through the GSM network. It then prints the content of the page through the serial monitor of the Arduino Software (IDE).

```arduino
/*

  Web client

 This sketch connects to a website through a MKR GSM 1400 board. Specifically,

 this example downloads the URL "http://www.example.org/" and

 prints it to the Serial monitor.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card with a data plan

 created 8 Mar 2012

 by Tom Igoe

*/

// libraries
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;
// APN data

const char GPRS_APN[]      = SECRET_GPRS_APN;

const char GPRS_LOGIN[]    = SECRET_GPRS_LOGIN;

const char GPRS_PASSWORD[] = SECRET_GPRS_PASSWORD;

// initialize the library instance

GSMClient client;

GPRS gprs;

GSM gsmAccess;

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

  bool connected = false;

  // After starting the modem with GSM.begin()

  // attach the shield to the GPRS network with the APN, login and password

  while (!connected) {

    if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &&

        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD) == GPRS_READY)) {

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

### MKR GSM Web Server

This sketch turns the Arduino MKR GSM 1400 into a web server. When the board receives a request from a connected client, it sends back the value of analog inputs 0-5.

Not all network operators allow incoming data requests from outside their network. This means you can create a web server with the GSM shield, but you may not be able to connect to it from the public internet; only from another data enabled device from the same provider on the same network. You should check with your provider to see what specific policies they have in place regarding incoming data connections.

```arduino
/*

 GSM Web Server

 A simple web server that shows the value of the analog input pins.

 using a MKR GSM 1400 board.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * Analog inputs attached to pins A0 through A5 (optional)

 created 8 Mar 2012

 by Tom Igoe

*/

// libraries
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;
// APN data

const char GPRS_APN[]      = SECRET_GPRS_APN;

const char GPRS_LOGIN[]    = SECRET_GPRS_LOGIN;

const char GPRS_PASSWORD[] = SECRET_GPRS_PASSWORD;

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

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // connection state

  bool connected = false;

  // Start GSM shield

  // If your SIM has PIN, pass it as a parameter of begin() in quotes

  while (!connected) {

    if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &&

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

  // listen for incoming clients

  GSMClient client = server.available();

  if (client) {

    while (client.connected()) {

      if (client.available()) {

        Serial.println("Receiving request!");

        bool sendResponse = false;

        while (int c = client.read()) {

          if (c == -1) {

            break;

          } else if (c == '\n') {

            sendResponse = true;

          }

        }

        // if you've gotten to the end of the line (received a newline

        // character)

        if (sendResponse) {

          // send a standard http response header

          client.println("HTTP/1.1 200 OK");

          client.println("Content-Type: text/html");

          client.println();

          client.println("<html>");

          // output the value of each analog input pin

          for (int analogChannel = 0; analogChannel < 6; analogChannel++) {

            client.print("analog input ");

            client.print(analogChannel);

            client.print(" is ");

            client.print(analogRead(analogChannel));

            client.println("<br />");

          }

          client.println("</html>");

          //necessary delay

          delay(1000);

          client.stop();

        }

      }

    }

  }
}
```

### MKR GSM Tools Band Management

This example is part of the tools supplied to manage the Arduino MKR GSM 1400 and shows how to use the GSM Library to manage the GSM band the modem connects to.

Check [http://www.worldtimezone.com/gsm.html](http://www.worldtimezone.com/gsm.html) for general GSM band information. Typical regional configurations are:

- Europe, Africa, Middle East: E-GSM(900)+DCS(1800)

- USA, Canada, South America: GSM(850)+PCS(1900)

- Mexico: PCS(1900)

- Brazil: GSM(850)+E-GSM(900)+DCS(1800)+PCS(1900)

```arduino

/*

  Band Management

  This sketch, for the MKR GSM 1400 board, checks the band

  currently configured in the modem and allows you to change

  it.

  Please check http://www.worldtimezone.com/gsm.html

  Usual configurations:

  Europe, Africa, Middle East: E-GSM(900)+DCS(1800)

  USA, Canada, South America: GSM(850)+PCS(1900)

  Mexico: PCS(1900)

  Brazil: GSM(850)+E-GSM(900)+DCS(1800)+PCS(1900)

  Circuit:

   MKR GSM 1400 board

   Antenna

  created 12 June 2012

  by Javier Zorzano, Scott Fitzgerald

*/

// libraries
#include <MKRGSM.h>

// initialize the library instance

GSMBand band;

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for Leonardo only

  }

  // Beginning the band manager restarts the modem

  Serial.println("Restarting modem...");

  band.begin();

  Serial.println("Modem restarted.");

};

void loop() {

  // Get current band

  String bandName = band.getBand(); // Get and print band name

  Serial.print("Current band:");

  Serial.println(bandName);

  Serial.println("Want to change the band you're on?");

  String newBandName;

  newBandName = askUser();

  // Tell the user what we are about to do...

  Serial.print("\nConfiguring band ");

  Serial.println(newBandName);

  // Change the band

  bool operationSuccess;

  operationSuccess = band.setBand(newBandName);

  // Tell the user if the operation was OK

  if (operationSuccess) {

    Serial.println("Success");

  } else {

    Serial.println("Error while changing band");

  }

  if (operationSuccess) {

    while (true);

  }
}

// This function offers the user different options
// through the Serial interface
// The user selects one

String askUser() {

  String newBand;

  Serial.println("Select band:");

  // Print the different options

  Serial.println("1 : E-GSM(900)");

  Serial.println("2 : DCS(1800)");

  Serial.println("3 : PCS(1900)");

  Serial.println("4 : E-GSM(900)+DCS(1800) ex: Europe");

  Serial.println("5 : GSM(850)+PCS(1900) Ex: USA, South Am.");

  Serial.println("6 : GSM800(800)+GSM(850)+E-GSM(900)+PCS(1900)");

  Serial.println("7 : UMTS(2100)");

  Serial.println("8 : GSM(850)+E-GSM(900)+PCS(1900)+UMTS(2100)");

  // Empty the incoming buffer

  while (Serial.available()) {

    Serial.read();

  }

  // Wait for an answer, just look at the first character

  while (!Serial.available());

  char c = Serial.read();

  if (c == '1') {

    newBand = GSM_MODE_EGSM;

  } else if (c == '2') {

    newBand = GSM_MODE_DCS;

  } else if (c == '3') {

    newBand = GSM_MODE_PCS;

  } else if (c == '4') {

    newBand = GSM_MODE_EGSM_DCS;

  } else if (c == '5') {

    newBand = GSM_MODE_GSM850_PCS;

  } else if (c == '6') {

    newBand = GSM_MODE_GSM850_EGSM_DCS_PCS;

  } else if (c == '7') {

    newBand = GSM_MODE_UMTS;

  } else if (c == '8') {
    newBand = GSM_MODE_GSM850_EGSM_PCS_UMTS;

  } else {

    newBand = "GSM_MODE_UNDEFINED";

  }
  return newBand;
}
```

### MKR GSM Tools Gsm Scan Networks

This example prints out the IMEI number of the modem, then checks to see if it's connected to a carrier and prints out its signal strength. It also scans for all nearby networks.

```arduino

/*

 GSM Scan Networks

 This example prints out the IMEI number of the modem,

 then checks to see if it's connected to a carrier. If so,

 it prints the phone number associated with the card.

 Then it scans for nearby networks and prints out their signal strengths.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card

 Created 8 Mar 2012

 by Tom Igoe, implemented by Javier Carazo

 Modified 4 Feb 2013

 by Scott Fitzgerald

*/

// libraries
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instance

GSM gsmAccess;     // include a 'true' parameter to enable debugging

GSMScanner scannerNetworks;

GSMModem modemTest;

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

  Serial.println("GSM networks scanner");

  scannerNetworks.begin();

  // connection state

  bool connected = false;

  // Start GSM shield

  // If your SIM has PIN, pass it as a parameter of begin() in quotes

  while (!connected) {

    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {

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

  // scan for existing networks, displays a list of networks

  Serial.println("Scanning available networks. May take some seconds.");

  Serial.println(scannerNetworks.readNetworks());

  // currently connected carrier

  Serial.print("Current carrier: ");

  Serial.println(scannerNetworks.getCurrentCarrier());

  // returns strength and ber

  // signal strength in 0-31 scale. 31 means power > 51dBm

  // BER is the Bit Error Rate. 0-7 scale. 99=not detectable

  Serial.print("Signal Strength: ");

  Serial.print(scannerNetworks.getSignalStrength());

  Serial.println(" [0-31]");

}
```

### MKR GSM Tools Pin Management

This example is part of the tools supplied for the Arduino MKR GSM 1400 and helps you change or remove the PIN of a SIM card .

```arduino
/*

 This example enables you to change or remove the PIN number of

 a SIM card inserted into a GSM shield.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card

 Created 12 Jun 2012

 by David del Peral

*/

// libraries
#include <MKRGSM.h>

// pin manager object

GSMPIN PINManager;

// save input in serial by user

String user_input = "";

// authenticated with PIN code

bool auth = false;

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

  // start GSM shield

  Serial.print("Checking register in GSM network...");

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

### MKR GSM Tools Test GPRS

This sketch tests the GPRS data connection on the Arduino MKR GSM 1400. It  tries to connect to arduino.cc.

To use a data connection with the GSM shield, you'll need your provider's Access Point Name (APN), login, and password. To obtain this information, contact the network provider for the most up to date information. [This page](http://wiki.apnchanger.org/) has some information about various carrier settings, but it may not be current.

```arduino
/*

 This sketch test the MKR GSM 1400 board's ability to connect to a

 GPRS network. It asks for APN information through the

 serial monitor and tries to connect to example.org.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 * SIM card with data plan

 Created 18 Jun 2012

 by David del Peral

*/

// libraries
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instance

GSM gsmAccess;        // GSM access: include a 'true' parameter for debug enabled

GPRS gprsAccess;  // GPRS access

GSMClient client;  // Client service for TCP connection

// messages for serial monitor response

String oktext = "OK";

String errortext = "ERROR";

// URL and path (for example: example.org)
char url[] = "example.org";
char urlproxy[] = "http://www.example.org";
char path[] = "/";

// variable for save response obtained

String response = "";

// use a proxy

bool use_proxy = false;

void setup() {

  // initialize serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for Leonardo only

  }
}

void loop() {

  use_proxy = false;

  // start GSM shield

  // if your SIM has PIN, pass it as a parameter of begin() in quotes

  Serial.print("Connecting GSM network...");

  if (gsmAccess.begin(PINNUMBER) != GSM_READY) {

    Serial.println(errortext);

    while (true);

  }

  Serial.println(oktext);

  // read APN introduced by user

  char apn[50];

  Serial.print("Enter your APN: ");

  readSerial(apn);

  Serial.println(apn);

  // Read APN login introduced by user

  char login[50];

  Serial.print("Now, enter your login: ");

  readSerial(login);

  Serial.println(login);

  // read APN password introduced by user

  char password[20];

  Serial.print("Finally, enter your password: ");

  readSerial(password);

  // attach GPRS

  Serial.println("Attaching to GPRS with your APN...");

  if (gprsAccess.attachGPRS(apn, login, password) != GPRS_READY) {

    Serial.println(errortext);

  } else {

    Serial.println(oktext);

    // read proxy introduced by user

    char proxy[100];

    Serial.print("If your carrier uses a proxy, enter it, if not press enter: ");

    readSerial(proxy);

    Serial.println(proxy);

    // if user introduced a proxy, asks them for proxy port

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

      client.println(" HTTP/1.0");

      client.println();

      Serial.println(oktext);

    } else {

      // if you didn't get a connection to the server

      Serial.println(errortext);

    }

    Serial.print("Receiving response...");

    bool test = true;

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

### MKR GSM Tools Test Modem

This sketch tests the modem on the GSM shield to see if it is working correctly. You do not need a SIM card for this example.

```arduino
/*

 This example tests to see if the modem of the

 MKR GSM 1400 board is working correctly. You do not need

 a SIM card for this example.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 Created 12 Jun 2012

 by David del Peral

 modified 21 Nov 2012

 by Tom Igoe

*/

// libraries
#include <MKRGSM.h>

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

### MKR GSM Tools Test Web Server

This sketch creates a web server to accept incoming connections on the Arduino MKR GSM 1400.  Some network providers only allow requests from inside their own network. You will need to check with your network provider to make sure your SIM card will accept incoming HTTP requests.

```arduino
/*

  Basic Web Server

 A simple web server that replies with nothing, but prints the client's request

 and the server IP address.

 Circuit:

 * MKR GSM 1400 board

 * Antenna

 created

 by David Cuartielles

 modified 21 Nov 2012

 by Tom Igoe

*/
#include <MKRGSM.h>

#include "arduino_secrets.h"
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number

const char PINNUMBER[]     = SECRET_PINNUMBER;
// APN data

const char GPRS_APN[]      = SECRET_GPRS_APN;

const char GPRS_LOGIN[]    = SECRET_GPRS_LOGIN;

const char GPRS_PASSWORD[] = SECRET_GPRS_PASSWORD;

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

  bool connected = false;

  // Start GSM shield

  // If your SIM has PIN, pass it as a parameter of begin() in quotes

  while (!connected) {

    if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &&

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