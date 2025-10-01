---
title: Guide to WiFi101
description: 'Find examples & utilities for using the WiFi101 library, designed for the MKR 1000 WiFi and WiFi Shield 101 (retired).'
tags: [Wi-Fi]
author: Arduino
---

>This article was revised on 2021/11/29 by Karl Söderby & Benjamin Dannegård.

The [WiFi101 library](https://www.arduino.cc/reference/en/libraries/wifi101/) is designed for Arduino products using a [WINC 1500 module](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42618-SmartConnect-ATSAMW25-MR210PB_Datasheet.pdf). In this article you will find a series of examples that can be uploaded to your board.

You can also visit the [WiFi101 GitHub repository](https://github.com/arduino-libraries/WiFi101) to learn more about this library.

## Hardware Required

- [Arduino MKR 1000 WiFi](https://store.arduino.cc/products/arduino-mkr1000-wifi)

***This library is also compatible with the [Arduino WiFi Shield 101](/retired/shields/arduino-wifi-shield-101)(retired). This shield can be mounted on top of a board, such as the Arduino UNO.***

## Circuit

- If you have a Wi-Fi Shield 101, mount it on top of your Arduino UNO.
- If you have a MKR 1000 WiFi, no additional circuit is needed!

***Digital pin 7 is used as a handshake pin between the WiFi Shield 101 and the board, and should not be used.***

You should have access to a 802.11b/g wireless network that connects to the internet for this example. You will need to change the network settings in the sketch to correspond to your particular networks SSID.

For networks using WPA/WPA2 Personal encryption, you need the SSID and password. The shield will not connect to networks using WPA2 Enterprise encryption.

WEP network passwords are hexadecimal strings known as keys. A WEP network can have 4 different keys; each key is assigned a "Key Index" value. For WEP encrypted networks, you need the SSID, the key, and key number.

## WiFi101 Firmware

### Check Firmware Version

You can check the firmware of your board/shield by using the sketch below.

When you load the sketch on the board, it will wait for a serial monitor console to be opened on your computer, then it prints out the result of the check between the expected firmware and the one available.

```arduino

/*

 * This example check if the firmware loaded on the WiFi101

 * shield is updated.

 *

 * Circuit:

 * - WiFi Shield 101 attached

 *

 * Created 29 July 2015 by Cristian Maglie

 * This code is in the public domain.

 */
#include <SPI.h>
#include <WiFi101.h>
#include <driver/source/nmasic.h>

void setup() {

  // Initialize serial

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // Print a welcome message

  Serial.println("WiFi101 firmware check.");

  Serial.println();

  // Check for the presence of the shield

  Serial.print("WiFi Shield 101: ");

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("NOT PRESENT");

    return; // don't continue

  }

  Serial.println("DETECTED");

  // Print firmware version on the shield

  String fv = WiFi.firmwareVersion();

  String latestFv;

  Serial.print("Firmware version installed: ");

  Serial.println(fv);

  if (REV(GET_CHIPID()) >= REV_3A0) {

    // model B

    latestFv = WIFI_FIRMWARE_LATEST_MODEL_B;

  } else {

    // model A

    latestFv = WIFI_FIRMWARE_LATEST_MODEL_A;

  }

  // Print required firmware version

  Serial.print("Latest firmware version available : ");

  Serial.println(latestFv);

  // Check if the latest version is installed

  Serial.println();

  if (fv >= latestFv) {

    Serial.println("Check result: PASSED");

  } else {

    Serial.println("Check result: NOT PASSED");

    Serial.println(" - The firmware version on the shield do not match the");

    Serial.println("   version required by the library, you may experience");

    Serial.println("   issues or failures.");

  }
}

void loop() {

  // do nothing
}
```

### Update Firmware / Load Certificates

The 19.6.1 firmware is only available for model B of the WINC1500, this is used in the MKR1000 board. Unfortunately, the WiFi shield 101 uses model A, which Atmel has stopped supporting, so there is no 19.6.1 firmware release for it, 19.4.4 will be the latest firmware version that is compatible.

To simplify the process, we have prepared a specific sketch - this **FirmwareUpdater** - that you must load on the host board (either the one with the shield plugged in, or the MKR1000 itself) and an easy to use plug-in available in Arduino Software (IDE) 1.6.10 onwards.

The `FirmwareUpdater.ino` sketch is available in **Examples > WiFi101**


![Select the "FirmwareUpdater" example.](assets/firmware_updater_sketch_101.png)

***When you load the sketch on the board, it prepares the communication between the plug-in and the Wi-Fi chip. It opens up the communication through the serial port to the Wi-Fi module hosted on the board. It is necessary to perform all the procedures managed by the Firmware Upgrader Plugin. Everything will be managed by the plug-in, but it is important to upload this sketch first.***

Upload the sketch and keep the board (either the one with the shield plugged in, or the MKR1000 itself) connected to the computer.

Once done, open the plug-in that is available in the tools menu.

![Navigate to the firmware updater tool.](assets/wifi101_wifinina_firmware_updater.png)

![Select your board and firmware.](assets/firmware_updater_tool_101.png)

Your board should be in the list of the available serial ports.
If not, please check that it is properly configured in the Tools menu.

To update the firmware you should choose the right typer of board. You can find your model looking at the Wi-Fi module: the first line in the sticker or the last line of the silk print on the right side of the PCB shows the microcontroller model. It can be either MR210PA or MR510PB and the last letter shows yor model accordingly.

![Find the model.](assets/MKR1000_RevA_B_20copy.png)

Choose in the dropdown list the model corresponding to your unit and proceed clicking on the **Update Firmware button**. A bar at the bottom will show you the progress of the procedure that includes erasing, writing and verifying of the firmware. At the end you get a clear notice of the successful operation.

![Firmware has been updated.](assets/firmware_uploaded_101.png)

#### Certificate Uploading

With the same procedure, you may load root certificates on the Wi-Fi module to access securely specific websites. Your board must be running the **FirmwareUpdater** sketch to work .The root certificates are issued by a limited number of certification authorities, but it is difficult to know which site is using which authority. To ease your life, we allow you to specify directly the URL to which you need to connect securely, leaving to us the task to download the root certificate.
The list you are building is not saved from one session to the next one. It might happen that a few websites share the same root certificate. You don't have to worry about this as we take care of it. The space available on your Wi-Fi module to store the certificates is limited to around 10 certificates that, being issued by a limited number of authorities, should be more than enough for the average projects.

The procedure starts connecting your board (either the one with the shield plugged in, or the MKR1000 itself) to your computer and selecting it from the Tools menu of the Arduino Software (IDE). Load the FirmwareUpdater on the board and launch the **WiFi101 Firmware Updater** from Tools and go to the third section of the interface.

![Adding SSL root certificates.](assets/certificates_upload_101.png)

There you find on the left an empty list and on the right the buttons to add or remove the URL from which you want to download the root certificates. The URL should be exactly the one to which you need to connect. Add all the websites' URLs needed and then proceed with the uploading process. Please remember that you erase all the existing certificates when you load a new set.
Press the ''Upload Certificates to WiFi module" and wait for the confirmation message.

![Certificates loaded successfully.](assets/certificates_uploaded_101.png)

## Examples

Below are a set of examples to test out the WiFi101 Library.

### Wifi101 Connect No Encryption

This example shows you how to connect to an open (not encrypted) 802.11b/g network with the Arduino WiFi shield 101 or a MKR1000.  Your Arduino Software (IDE) serial monitor will provide information about the connection once it has connected.

```arduino
/*
 This example connects to an unencrypted WiFi network.

 Then it prints the  MAC address of the WiFi shield,

 the IP address obtained, and other network details.

 Circuit:

 * WiFi shield attached

 created 13 July 2010

 by dlf (Metodo2 srl)

 modified 31 May 2012

 by Tom Igoe

 */
#include <SPI.h>
#include <WiFi101.h>
#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
int status = WL_IDLE_STATUS;     // the WiFi radio's status

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to WiFi network:

  while ( status != WL_CONNECTED) {

    Serial.print("Attempting to connect to open SSID: ");

    Serial.println(ssid);

    status = WiFi.begin(ssid);

    // wait 10 seconds for connection:

    delay(10000);

  }

  // you're connected now, so print out the data:

  Serial.print("You're connected to the network");

  printCurrentNet();

  printWiFiData();
}

void loop() {

  // check the network connection once every 10 seconds:

  delay(10000);

  printCurrentNet();
}

void printWiFiData() {

  // print your WiFi shield's IP address:

  IPAddress ip = WiFi.localIP();

  Serial.print("IP Address: ");

  Serial.println(ip);

  Serial.println(ip);

  // print your MAC address:

  byte mac[6];

  WiFi.macAddress(mac);

  Serial.print("MAC address: ");

  printMacAddress(mac);

  // print your subnet mask:

  IPAddress subnet = WiFi.subnetMask();

  Serial.print("NetMask: ");

  Serial.println(subnet);

  // print your gateway address:

  IPAddress gateway = WiFi.gatewayIP();

  Serial.print("Gateway: ");

  Serial.println(gateway);
}

void printCurrentNet() {

  // print the SSID of the network you're attached to:

  Serial.print("SSID: ");

  Serial.println(WiFi.SSID());

  // print the MAC address of the router you're attached to:

  byte bssid[6];

  WiFi.BSSID(bssid);

  Serial.print("BSSID: ");

  printMacAddress(bssid);

  // print the received signal strength:

  long rssi = WiFi.RSSI();

  Serial.print("signal strength (RSSI):");

  Serial.println(rssi);

  // print the encryption type:

  byte encryption = WiFi.encryptionType();

  Serial.print("Encryption Type:");

  Serial.println(encryption, HEX);
}

void printMacAddress(byte mac[]) {

  for (int i = 5; i >= 0; i--) {

    if (mac[i] < 16) {

      Serial.print("0");

    }

    Serial.print(mac[i], HEX);

    if (i > 0) {

      Serial.print(":");

    }

  }

  Serial.println();
}
```

### Wifi101 Connect With WEP

This example shows you how to connect to a WEP encrypted 802.11b/g network with the Arduino WiFi shield 101 or a MKR1000 board.  Your Arduino Software (IDE) serial monitor will provide information about the connection once it has connected.

```arduino
/*

 This example connects to a WEP-encrypted WiFi network.

 Then it prints the  MAC address of the WiFi shield,

 the IP address obtained, and other network details.

 If you use 40-bit WEP, you need a key that is 10 characters long,

 and the characters must be hexadecimal (0-9 or A-F).

 e.g.  for 40-bit, ABBADEAF01 will work, but ABBADEAF won't work

 (too short) and ABBAISDEAF won't work (I and S are not

 hexadecimal characters).

 For 128-bit, you need a string that is 26 characters long.

 D0D0DEADF00DABBADEAFBEADED will work because it's 26 characters,

 all in the 0-9, A-F range.

 Circuit:

 * WiFi shield attached

 created 13 July 2010

 by dlf (Metodo2 srl)

 modified 31 May 2012

 by Tom Igoe

 */
#include <SPI.h>
#include <WiFi101.h>

#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char key[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                                // your network key Index number
int status = WL_IDLE_STATUS;                     // the WiFi radio's status

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to WiFi network:

  while ( status != WL_CONNECTED) {

    Serial.print("Attempting to connect to WEP network, SSID: ");

    Serial.println(ssid);

    status = WiFi.begin(ssid, keyIndex, key);

    // wait 10 seconds for connection:

    delay(10000);

  }

  // once you are connected :

  Serial.print("You're connected to the network");

  printCurrentNet();

  printWiFiData();
}

void loop() {

  // check the network connection once every 10 seconds:

  delay(10000);

  printCurrentNet();
}

void printWiFiData() {

  // print your WiFi shield's IP address:

  IPAddress ip = WiFi.localIP();

  Serial.print("IP Address: ");

  Serial.println(ip);

  Serial.println(ip);

  // print your MAC address:

  byte mac[6];

  WiFi.macAddress(mac);

  Serial.print("MAC address: ");

  printMacAddress(mac);
}

void printCurrentNet() {

  // print the SSID of the network you're attached to:

  Serial.print("SSID: ");

  Serial.println(WiFi.SSID());

  // print the MAC address of the router you're attached to:

  byte bssid[6];

  WiFi.BSSID(bssid);

  Serial.print("BSSID: ");

  printMacAddress(bssid);

  // print the received signal strength:

  long rssi = WiFi.RSSI();

  Serial.print("signal strength (RSSI):");

  Serial.println(rssi);

  // print the encryption type:

  byte encryption = WiFi.encryptionType();

  Serial.print("Encryption Type:");

  Serial.println(encryption, HEX);

  Serial.println();
}

void printMacAddress(byte mac[]) {

  for (int i = 5; i >= 0; i--) {

    if (mac[i] < 16) {

      Serial.print("0");

    }

    Serial.print(mac[i], HEX);

    if (i > 0) {

      Serial.print(":");

    }

  }

  Serial.println();
}
```

### Wifi101 Connect With WPA

This example shows you how to connect to a WPA2 Personal encrypted 802.11b/g network with the Arduino WiFi Shield 101 or a MKR1000 board.   Your Arduino Software (IDE) serial monitor will provide information about the connection once it has connected.

```arduino

/*

 This example connects to an unencrypted WiFi network.

 Then it prints the  MAC address of the WiFi shield,

 the IP address obtained, and other network details.

 Circuit:

 * WiFi shield attached

 created 13 July 2010

 by dlf (Metodo2 srl)

 modified 31 May 2012

 by Tom Igoe

 */
#include <SPI.h>
#include <WiFi101.h>

#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int status = WL_IDLE_STATUS;     // the WiFi radio's status

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to WiFi network:

  while ( status != WL_CONNECTED) {

    Serial.print("Attempting to connect to WPA SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  // you're connected now, so print out the data:

  Serial.print("You're connected to the network");

  printCurrentNet();

  printWiFiData();

}

void loop() {

  // check the network connection once every 10 seconds:

  delay(10000);

  printCurrentNet();
}

void printWiFiData() {

  // print your WiFi shield's IP address:

  IPAddress ip = WiFi.localIP();

  Serial.print("IP Address: ");

  Serial.println(ip);

  Serial.println(ip);

  // print your MAC address:

  byte mac[6];

  WiFi.macAddress(mac);

  Serial.print("MAC address: ");

  printMacAddress(mac);

}

void printCurrentNet() {

  // print the SSID of the network you're attached to:

  Serial.print("SSID: ");

  Serial.println(WiFi.SSID());

  // print the MAC address of the router you're attached to:

  byte bssid[6];

  WiFi.BSSID(bssid);

  Serial.print("BSSID: ");

  printMacAddress(bssid);

  // print the received signal strength:

  long rssi = WiFi.RSSI();

  Serial.print("signal strength (RSSI):");

  Serial.println(rssi);

  // print the encryption type:

  byte encryption = WiFi.encryptionType();

  Serial.print("Encryption Type:");

  Serial.println(encryption, HEX);

  Serial.println();
}

void printMacAddress(byte mac[]) {

  for (int i = 5; i >= 0; i--) {

    if (mac[i] < 16) {

      Serial.print("0");

    }

    Serial.print(mac[i], HEX);

    if (i > 0) {

      Serial.print(":");

    }

  }

  Serial.println();
}
```

### Wifi101 Scan Networks

This example scans for 802.11b/g networks with the Arduino WiFi Shield 101 or a MKR1000 board. Your Arduino Software (IDE) serial monitor will print out information about the board and the networks it can see. It will not connect to a network.

```arduino

/*

 This example  prints the WiFi shield's MAC address, and

 scans for available WiFi networks using the WiFi shield.

 Every ten seconds, it scans again. It doesn't actually

 connect to any network, so no encryption scheme is specified.

 Circuit:

 * WiFi shield attached

 created 13 July 2010

 by dlf (Metodo2 srl)

 modified 21 Junn 2012

 by Tom Igoe and Jaymes Dec

 */

#include <SPI.h>
#include <WiFi101.h>

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // Print WiFi MAC address:

  printMacAddress();

  // scan for existing networks:

  Serial.println("Scanning available networks...");

  listNetworks();
}

void loop() {

  delay(10000);

  // scan for existing networks:

  Serial.println("Scanning available networks...");

  listNetworks();
}

void printMacAddress() {

  // the MAC address of your WiFi shield

  byte mac[6];

  // print your MAC address:

  WiFi.macAddress(mac);

  Serial.print("MAC: ");

  printMacAddress(mac);
}

void listNetworks() {

  // scan for nearby networks:

  Serial.println("** Scan Networks **");

  int numSsid = WiFi.scanNetworks();

  if (numSsid == -1)

  {

    Serial.println("Couldn't get a wifi connection");

    while (true);

  }

  // print the list of networks seen:

  Serial.print("number of available networks:");

  Serial.println(numSsid);

  // print the network number and name for each network found:

  for (int thisNet = 0; thisNet < numSsid; thisNet++) {

    Serial.print(thisNet);

    Serial.print(") ");

    Serial.print(WiFi.SSID(thisNet));

    Serial.print("\tSignal: ");

    Serial.print(WiFi.RSSI(thisNet));

    Serial.print(" dBm");

    Serial.print("\tEncryption: ");

    printEncryptionType(WiFi.encryptionType(thisNet));

    Serial.flush();

  }
}

void printEncryptionType(int thisType) {

  // read the encryption type and print out the name:

  switch (thisType) {

    case ENC_TYPE_WEP:

      Serial.println("WEP");

      break;

    case ENC_TYPE_TKIP:

      Serial.println("WPA");

      break;

    case ENC_TYPE_CCMP:

      Serial.println("WPA2");

      break;

    case ENC_TYPE_NONE:

      Serial.println("None");

      break;

    case ENC_TYPE_AUTO:

      Serial.println("Auto");

      break;

  }
}

void printMacAddress(byte mac[]) {

  for (int i = 5; i >= 0; i--) {

    if (mac[i] < 16) {

      Serial.print("0");

    }

    Serial.print(mac[i], HEX);

    if (i > 0) {

      Serial.print(":");

    }

  }

  Serial.println();
}
```

### Wifi101 Simple Web Server Wi-Fi

In this example,  a simple web server lets you blink an LED via the web. This example will print the IP address of your WiFi Shield 101 or MKR1000 board (once connected) to the Arduino Software (IDE) Serial Monitor. Once you know the IP address of our board, you can open that address in a web browser to turn on and off the LED on pin 9.

If the IP address of your shield/board is yourAddress:
[http://yourAddress/H](http://yourAddress/H) turns the LED on
[http://yourAddress/L](http://yourAddress/L) turns it off

This example is written for a network using WPA encryption. For  WEP or WPA, change the Wifi.begin() call accordingly.

```arduino
Access Point Web Server

Creating access point named: MKR1000-network

SSID: MKR1000-network

IP Address: 192.168.1.1

signal strength (RSSI):-100 dBm

To see this page in action, open a browser to http://192.168.1.1
```

Every connection is reported on the Serial Monitor as well and contains information that is related to the connecting client. In the following example, the client is Chrome on OSX:

```arduino
new client

GET / HTTP/1.1

Host: 192.168.1.1

Connection: keep-alive

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36

Accept-Encoding: gzip, deflate, sdch

Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2

client disconnected

new client

GET /favicon.ico HTTP/1.1

Host: 192.168.1.1

Connection: keep-alive

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36

Accept: */*

Referer: http://192.168.1.1/

Accept-Encoding: gzip, deflate, sdch

Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2

client disconnected
```

The complete sketch of this tutorial is below.

```arduino

/*

  WiFi Web Server LED Blink

 A simple web server that lets you blink an LED via the web.

 This sketch will print the IP address of your WiFi Shield (once connected)

 to the Serial monitor. From there, you can open that address in a web browser

 to turn on and off the LED on pin 9.

 If the IP address of your shield is yourAddress:

 http://yourAddress/H turns the LED on

 http://yourAddress/L turns it off

 This example is written for a network using WPA encryption. For

 WEP or WPA, change the WiFi.begin() call accordingly.

 Circuit:

 * WiFi shield attached

 * LED attached to pin 9

 created 25 Nov 2012

 by Tom Igoe

 */
#include <SPI.h>
#include <WiFi101.h>

#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                 // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;

WiFiServer server(80);

void setup() {

  Serial.begin(9600);      // initialize serial communication

  pinMode(9, OUTPUT);      // set the LED pin mode

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    while (true);       // don't continue

  }

  // attempt to connect to WiFi network:

  while ( status != WL_CONNECTED) {

    Serial.print("Attempting to connect to Network named: ");

    Serial.println(ssid);                   // print the network name (SSID);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  server.begin();                           // start the web server on port 80

  printWiFiStatus();                        // you're connected now, so print out the status
}

void loop() {

  WiFiClient client = server.available();   // listen for incoming clients

  if (client) {                             // if you get a client,

    Serial.println("new client");           // print a message out the serial port

    String currentLine = "";                // make a String to hold incoming data from the client

    while (client.connected()) {            // loop while the client's connected

      if (client.available()) {             // if there's bytes to read from the client,

        char c = client.read();             // read a byte, then

        Serial.write(c);                    // print it out the serial monitor

        if (c == '\n') {                    // if the byte is a newline character

          // if the current line is blank, you got two newline characters in a row.

          // that's the end of the client HTTP request, so send a response:

          if (currentLine.length() == 0) {

            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)

            // and a content-type so the client knows what's coming, then a blank line:

            client.println("HTTP/1.1 200 OK");

            client.println("Content-type:text/html");

            client.println();

            // the content of the HTTP response follows the header:

            client.print("Click <a href=\"/H\">here</a> turn the LED on pin 9 on<br>");

            client.print("Click <a href=\"/L\">here</a> turn the LED on pin 9 off<br>");

            // The HTTP response ends with another blank line:

            client.println();

            // break out of the while loop:

            break;

          }

          else {      // if you got a newline, then clear currentLine:

            currentLine = "";

          }

        }

        else if (c != '\r') {    // if you got anything else but a carriage return character,

          currentLine += c;      // add it to the end of the currentLine

        }

        // Check to see if the client request was "GET /H" or "GET /L":

        if (currentLine.endsWith("GET /H")) {

          digitalWrite(9, HIGH);               // GET /H turns the LED on

        }

        if (currentLine.endsWith("GET /L")) {

          digitalWrite(9, LOW);                // GET /L turns the LED off

        }

      }

    }

    // close the connection:

    client.stop();

    Serial.println("client disconnected");

  }
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

  // print where to go in a browser:

  Serial.print("To see this page in action, open a browser to http://");

  Serial.println(ip);
}
```


### Wifi101 Udp NTP Client

In this example, you will use your WiFi Shield 101 with your Arduino Zero board, or a MKR1000 board, to query a Network Time Protocol (NTP) server. In this way, your board can get the time from the Internet.

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

 This code is in the public domain.

 */

#include <SPI.h>
#include <WiFi101.h>
#include <WiFiUdp.h>

int status = WL_IDLE_STATUS;
#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

unsigned int localPort = 2390;      // local port to listen for UDP packets

IPAddress timeServer(129, 6, 15, 28); // time.nist.gov NTP server

const int NTP_PACKET_SIZE = 48; // NTP time stamp is in the first 48 bytes of the message

byte packetBuffer[ NTP_PACKET_SIZE]; //buffer to hold incoming and outgoing packets

// A UDP instance to let us send and receive packets over UDP

WiFiUDP Udp;

void setup()
{

  // Open serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

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

  Serial.println("Connected to wifi");

  printWiFiStatus();

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
```

### Wifi101 Wi-Fi Chat Server

A simple server that distributes any incoming messages to all connected clients.  To use, open a terminal window, telnet to your WiFi shield's or MKR1000's IP address, and type away.  Any incoming text will be sent to all connected clients (including the one typing). Additionally, you will be able to see the client's input in your Arduino Software (IDE) serial monitor as well.

```arduino

/*

 Chat  Server

 A simple server that distributes any incoming messages to all

 connected clients.  To use telnet to  your device's IP address and type.

 You can see the client's input in the serial monitor as well.

 This example is written for a network using WPA encryption. For

 WEP or WPA, change the WiFi.begin() call accordingly.

 Circuit:

 * WiFi shield attached

 created 18 Dec 2009

 by David A. Mellis

 modified 31 May 2012

 by Tom Igoe

 */

#include <SPI.h>
#include <WiFi101.h>

#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)

int keyIndex = 0;            // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;

WiFiServer server(23);

bool alreadyConnected = false; // whether or not the client was connected previously

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

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

  // start the server:

  server.begin();

  // you're connected now, so print out the status:

  printWiFiStatus();
}

void loop() {

  // wait for a new client:

  WiFiClient client = server.available();

  // when the client sends the first byte, say hello:

  if (client) {

    if (!alreadyConnected) {

      // clead out the input buffer:

      client.flush();

      Serial.println("We have a new client");

      client.println("Hello, client!");

      alreadyConnected = true;

    }

    if (client.available() > 0) {

      // read the bytes incoming from the client:

      char thisChar = client.read();

      // echo the bytes back to the client:

      server.write(thisChar);

      // echo the bytes to the server as well:

      Serial.write(thisChar);

    }

  }
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
```


### Wifi101 Wi-Fi Udp Send Receive String

This tutorial waits for a UDP packet on a local port. When a valid packet is received, an acknowledge packet is sent back to the client on a specified outgoing port. It relies on a WiFi connection made to your LAN using an Arduino Wifi 101 Shield and Zero Board or the MKR1000 board.

```arduino

/*

  WiFi UDP Send and Receive String

 This sketch wait an UDP packet on localPort using a WiFi shield.

 When a packet is received an Acknowledge packet is sent to the client on port remotePort

 Circuit:

 * WiFi shield attached

 created 30 December 2012

 by dlf (Metodo2 srl)

 */

#include <SPI.h>
#include <WiFi101.h>
#include <WiFiUdp.h>

int status = WL_IDLE_STATUS;
#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

unsigned int localPort = 2390;      // local port to listen on

char packetBuffer[255]; //buffer to hold incoming packet
char  ReplyBuffer[] = "acknowledged";       // a string to send back

WiFiUDP Udp;

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

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

  Serial.println("Connected to wifi");

  printWiFiStatus();

  Serial.println("\nStarting connection to server...");

  // if you get a connection, report back via serial:

  Udp.begin(localPort);
}

void loop() {

  // if there's data available, read a packet

  int packetSize = Udp.parsePacket();

  if (packetSize)

  {

    Serial.print("Received packet of size ");

    Serial.println(packetSize);

    Serial.print("From ");

    IPAddress remoteIp = Udp.remoteIP();

    Serial.print(remoteIp);

    Serial.print(", port ");

    Serial.println(Udp.remotePort());

    // read the packet into packetBufffer

    int len = Udp.read(packetBuffer, 255);

    if (len > 0) packetBuffer[len] = 0;

    Serial.println("Contents:");

    Serial.println(packetBuffer);

    // send a reply, to the IP address and port that sent us the packet we received

    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());

    Udp.write(ReplyBuffer);

    Udp.endPacket();

  }
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
```

### Wifi101 Wi-Fi Web Client

This example shows you how to make a HTTP request using a WiFi Shield 101 or a MKR1000 board. It returns a [Google search for the term "Arduino"](http://www.google.com/search?q=arduino). The results of this search are viewable as HTML through your Arduino Software (IDE) serial window.

This example is written for a network using WPA encryption. For  WEP or WPA, change the Wifi.begin() call accordingly.

```arduino

/*

  Web client

 This sketch connects to a website (http://www.google.com)

 using a WiFi shield.

 This example is written for a network using WPA encryption. For

 WEP or WPA, change the WiFi.begin() call accordingly.

 This example is written for a network using WPA encryption. For

 WEP or WPA, change the WiFi.begin() call accordingly.

 Circuit:

 * WiFi shield attached

 created 13 July 2010

 by dlf (Metodo2 srl)

 modified 31 May 2012

 by Tom Igoe

 */

#include <SPI.h>
#include <WiFi101.h>
#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
//IPAddress server(74,125,232,128);  // numeric IP for Google (no DNS)
char server[] = "www.google.com";    // name address for Google (using DNS)

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):

WiFiClient client;

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to WiFi network:

  while (status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  Serial.println("Connected to wifi");

  printWiFiStatus();

  Serial.println("\nStarting connection to server...");

  // if you get a connection, report back via serial:

  if (client.connect(server, 80)) {

    Serial.println("connected to server");

    // Make a HTTP request:

    client.println("GET /search?q=arduino HTTP/1.1");

    client.println("Host: www.google.com");

    client.println("Connection: close");

    client.println();

  }
}

void loop() {

  // if there are incoming bytes available

  // from the server, read them and print them:

  while (client.available()) {

    char c = client.read();

    Serial.write(c);

  }

  // if the server's disconnected, stop the client:

  if (!client.connected()) {

    Serial.println();

    Serial.println("disconnecting from server.");

    client.stop();

    // do nothing forevermore:

    while (true);

  }
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
```


### Wifi101 Wi-Fi Web Client Repeating

This example shows you how to make repeated HTTP requests using a WiFi Shield 101 or a MKR1000 board.  It connects to  [http://example.org](http://example.org). The content of the page is viewable through your Arduino Software (IDE) Serial Monitor window.

This example is written for a network using WPA encryption. For  WEP or WPA, change the Wifi.begin() call accordingly.

```arduino

/*

  Repeating WiFi Web Client

 This sketch connects to a a web server and makes a request

 using an Arduino WiFi shield.

 Circuit:

 * WiFi shield attached to pins SPI pins and pin 7

 created 23 April 2012

 modified 31 May 2012

 by Tom Igoe

 modified 13 Jan 2014

 by Federico Vanzati

 http://arduino.cc/en/Tutorial/WiFiWebClientRepeating

 This code is in the public domain.

 */

#include <SPI.h>
#include <WiFi101.h>

#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;

// Initialize the WiFi client library

WiFiClient client;

// server address:
char server[] = "example.org";
//IPAddress server(64,131,82,241);

unsigned long lastConnectionTime = 0;            // last time you connected to the server, in milliseconds

const unsigned long postingInterval = 10L * 1000L; // delay between updates, in milliseconds

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

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
}

void loop() {

  // if there's incoming data from the net connection.

  // send it out the serial port.  This is for debugging

  // purposes only:

  while (client.available()) {

    char c = client.read();

    Serial.write(c);

  }

  // if ten seconds have passed since your last connection,

  // then connect again and send data:

  if (millis() - lastConnectionTime > postingInterval) {

    httpRequest();

  }

}

// this method makes a HTTP connection to the server:
void httpRequest() {

  // close any connection before send a new request.

  // This will free the socket on the WiFi shield

  client.stop();

  // if there's a successful connection:

  if (client.connect(server, 80)) {

    Serial.println("connecting...");

    // send the HTTP PUT request:

    client.println("GET / HTTP/1.1");

    client.println("Host: example.org");

    client.println("User-Agent: ArduinoWiFi/1.1");

    client.println("Connection: close");

    client.println();

    // note the time that the connection was made:

    lastConnectionTime = millis();

  }

  else {

    // if you couldn't make a connection:

    Serial.println("connection failed");

  }
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
```


### Wifi101 Simple Web Server Wi-Fi

In this example, you will use your WiFi Shield 101 and your Arduino Zero, or a MKR1000 board, to create a simple Web server. Using the Wi-Fi library, your device will be able to answer a HTTP request received from the Wi-FI connection. After opening a browser and navigating to your WiFi shield's or MKR1000's IP address, your board will respond with just enough HTML for a browser to display the input values from all six analog pins.

This example is written for a network using WPA encryption. For  WEP or WPA, change the Wifi.begin() call accordingly.

```arduino

/*

  WiFi Web Server

 A simple web server that shows the value of the analog input pins.

 using a WiFi shield.

 This example is written for a network using WPA encryption. For

 WEP or WPA, change the WiFi.begin() call accordingly.

 Circuit:

 * WiFi shield attached

 * Analog inputs attached to pins A0 through A5 (optional)

 created 13 July 2010

 by dlf (Metodo2 srl)

 modified 31 May 2012

 by Tom Igoe

 */

#include <SPI.h>
#include <WiFi101.h>

#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                 // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;

WiFiServer server(80);

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to WiFi network:

  while (status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  server.begin();

  // you're connected now, so print out the status:

  printWiFiStatus();
}

void loop() {

  // listen for incoming clients

  WiFiClient client = server.available();

  if (client) {

    Serial.println("new client");

    // an http request ends with a blank line

    bool currentLineIsBlank = true;

    while (client.connected()) {

      if (client.available()) {

        char c = client.read();

        Serial.write(c);

        // if you've gotten to the end of the line (received a newline

        // character) and the line is blank, the http request has ended,

        // so you can send a reply

        if (c == '\n' && currentLineIsBlank) {

          // send a standard http response header

          client.println("HTTP/1.1 200 OK");

          client.println("Content-Type: text/html");

          client.println("Connection: close");  // the connection will be closed after completion of the response

          client.println("Refresh: 5");  // refresh the page automatically every 5 sec

          client.println();

          client.println("<!DOCTYPE HTML>");

          client.println("<html>");

          // output the value of each analog input pin

          for (int analogChannel = 0; analogChannel < 6; analogChannel++) {

            int sensorReading = analogRead(analogChannel);

            client.print("analog input ");

            client.print(analogChannel);

            client.print(" is ");

            client.print(sensorReading);

            client.println("<br />");

          }

          client.println("</html>");

          break;

        }

        if (c == '\n') {

          // you're starting a new line

          currentLineIsBlank = true;

        }

        else if (c != '\r') {

          // you've gotten a character on the current line

          currentLineIsBlank = false;

        }

      }

    }

    // give the web browser time to receive the data

    delay(1);

    // close the connection:

    client.stop();

    Serial.println("client disconnected");

  }
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
```