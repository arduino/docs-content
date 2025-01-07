---
title: 'Arduino® Portenta Cat. M1/NB IoT GNSS Shield Cheat Sheet'
description: 'Learn how to set up the Portenta Cat. M1/NB IoT GNSS Shield and get a quick overview of its functionality. Obtain information regarding pins and how to use the different communication technologies.'
difficulty: beginner
tags:
  - Installation
  - Cat. M1
  - NB IoT
  - GNSS
  - NMEA
author: 'Pablo Marquínez'
hardware:
  - hardware/04pro/shields/portenta-cat-m1-nb-iot-gnss-shield
software:
  - ide-v1
  - ide-v2
  - web-editor
  - cli
libraries:
  - name: 107-Arduino-NMEA-Parser
    url: https://github.com/107-systems/107-Arduino-NMEA-Parser
---

![The Arduino Portenta Cat. M1/NB IoT GNSS Shield](assets/featured.png)

The **Arduino Portenta Cat. M1/NB IoT GNSS Shield** is a board that enables cellular connectivity with both Cat. M1 and NB-IoT networks. Easily track your valuable assets across the city or worldwide by choosing among GPS, GLONASS, Galileo or BeiDou Satellite navigation system.

This article is a collection of guides, API calls and tutorials that can help you get started with the Portenta Cat. M1/NB IoT GNSS Shield board. You can also visit the [documentation product page for the Portenta Cat. M1/NB IoT GNSS Shield](/hardware/portenta-cat-m1-nb-iot-gnss-shield) for more in-depth tutorials about the different features.

## Core

The Portenta Cat. M1/NB IoT GNSS Shield uses the libraries from the [Arduino Mbed OS Portenta core](https://github.com/arduino/ArduinoCore-mbed).

***The libraries are included in the mbed Core version greater than 2.6.1***

## Installation

### Arduino IDE

The Portenta Cat. M1/NB IoT GNSS Shield can be programmed through the **Classic Arduino IDE 1.8.X** and **Arduino IDE 2**.

To install your board, you can check out the guides below:

- [Installing the Arduino Mbed OS Portenta Boards core](/software/ide-v1/tutorials/getting-started/cores/arduino-mbed_portenta)
- [How to use the board manager with the Arduino IDE 2](https://www.arduino.cc/en/Tutorial/getting-started-with-ide-v2/ide-v2-board-manager)

### Cloud Editor

The board can be programmed through the **Cloud Editor**. To get started with your board, you will only need to install a plug-in, which is explained in the guide below:

- [Getting started with the Cloud Editor](/cloud/web-editor/tutorials/getting-started/getting-started-web-editor)

## Pins

As a Portenta family shield, it uses High Density Connectors to interface with the Portenta board which is connected to.

![The pinout of the Portenta Cat. M1/NB IoT GNSS Shield.](assets/ASX00027-pinout.png)

## GSM

### Requirements

The GSM feature requires:

* An antenna (e.g [Dipole antenna, at the Arduino store](https://store.arduino.cc/products/dipole-pentaband-waterproof-antenna) connected to the **RF OUT** antenna connector on the top side of the shield
* SIM card capable of running according to Cat. M1 specifications (check with your provider if your SIM card has this feature)

To check if your setup is properly working, you can open an example sketch from the GSM library inside the Mbed Portenta Core. Under **Examples > GSM > GSMClient**, open a sketch that allows you to connect to the SIM card provider, then connect to a webpage, download its content and display it inside the Serial Monitor.

Make sure you go to the `arduino_secrets.h` tab and:

* Enter the PIN of your SIM card and store it in the variable `SECRET_PIN`.
* Check the mobile APN of your SIM card provider, e.g "online.provider.com", and save it inside the `SECRET_APN`. You can find this information by searching online for APN + provider name.

APN stands for 'Access Point Name'. An APN is a gateway between a cellular network and the Internet.

After finishing this setup, compile, and upload the program. If everything went fine, you should see the HTML content of the webpage printed in the Serial Monitor.

***Sometimes it takes time to connect to the provider's APN, please be patient, it can take up to 30 minutes. If you cannot connect after that time, make sure you entered the correct SIM pin and the APN. If the issue persists, contact your provider and verify whether Cat. M1 is enabled on your SIM card.***

### API

To get familiar with the commands, you can take a look at the [GSM library](https://www.arduino.cc/en/Reference/GSM) which uses the same API.

This library contains some commands that are quite different, because it leverages mbed APIs. In this case, it uses the NetworkInterface, CellularContext and CellularDevice classes. For more information about API visit [https://os.mbed.com/docs/mbed-os/v6.14/apis/network-interface-apis.html](https://os.mbed.com/docs/mbed-os/v6.14/apis/network-interface-apis.html).

| Command                                                        | Information                                                                                                             |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `GSM.begin(PIN, APN, USERNAME, PASSWORD, CATNB/CATM1, BAND_#)` | Unlock the SIM card using the PIN parameter and connects to the provider                                                |
| `GSMClient`                                                    | Client constructor, on the examples we define it as client                                                              |
| `GSM.getTime()`                                                | Returns the time, you can set a new one with setTime()                                                                  |
| `GSM.getLocalTime()`                                           | Returns the local time                                                                                                  |
| `GSM.setTime()`                                                | Set the time, it will be saved and it can be read with getTime()                                                        |
| `GSM.debug()`                                                  | After this command, the Serial Monitor will output more detailed info about the GSM class commands, connections, etc... |
| `GSMClient.connect(server,port)`                               | Connect to a remote server                                                                                              |
| `GSMClient.available()`                                        | Check if the server that is connected to has some bytes ready to be read                                                |
| `GSMClient.read()`                                             | Returns data from the server                                                                                            |
| `GSMClient.stop()`                                             | Disconnects from the server                                                                                             |

### Available Frequency Bands

It is possible to establish a connection within desired frequency band for the Portenta Cat. M1/NB IoT GNSS Shield. To do this, you need to define frequency bands for `GSM.begin(PIN, APN, USERNAME, PASSWORD, CATNB/CATM1, BAND_#)` by replacing `BAND_#` with desired band.

The **list of available frequency bands** that can be used for the device's credential configuration is as follows:

| 32-bit Hexadecimal Value | LTE Band | Band Designation | Argument Designation |
| ------------------------ | -------- | ---------------- | -------------------- |
| 0x01                     | LTE 2100 | B1               | BAND_1               |
| 0x02                     | LTE 1900 | B2               | BAND_2               |
| 0x04                     | LTE 1800 | B3               | BAND_3               |
| 0x08                     | LTE 1700 | B4               | BAND_4               |
| 0x10                     | LTE 850  | B5               | BAND_5               |
| 0x80                     | LTE 900  | B8               | BAND_8               |
| 0x800                    | LTE 700  | B12              | BAND_12              |
| 0x1000                   | LTE 700  | B13              | BAND_13              |
| 0x20000                  | LTE 850  | B18              | BAND_18              |
| 0x40000                  | LTE 800  | B19              | BAND_19              |
| 0x80000                  | LTE 800  | B20              | BAND_20              |
| 0x1000000                | LTE 1900 | B25              | BAND_25              |
| 0x2000000                | LTE 850  | B26              | BAND_26              |
| 0x8000000                | LTE 700  | B28              | BAND_28              |

These are Cat.M and Cat.NB frequency bands that are available for use with TX62-W, referred to as the LTE Cat.M1 and Cat.NB1 Engine. The Portenta Cat. M1/NB IoT GNSS Shield is capable of the present network connectivity thanks to its onboard TX62-W Cellular-GNSS LPWAN modem.

The band configuration is available to allow the user to restrict to a specific or combination of frequency bands. It helps to operate under enforced frequency policy requirements, or to lower the network search time, reducing the device power consumption.

If you leave the frequency band `BAND_#` field blank for the `GSM.begin(PIN, APN, USERNAME, PASSWORD, CATNB/CATM1, BAND_#)` method, it will configure using the default setting, which allows it to search within all available supported bands. The Portenta Cat. M1/NB IoT GNSS Shield will then select a compatible network automatically depending on the availability in the operating region.

Each country has a compatible frequency band, so it is a good practice to check the if desired band is suitable for its region. You can check the frequency band compatibility of the region by using a website that compiles network status such as [here](https://www.frequencycheck.com/countries).

#### Connect to Your Provider

***__Please be aware that the Portenta Cat. M1/NB IoT GNSS Shield is not certified as an End-Device by all cellular network providers__. If you encounter difficulties with network connection, we recommend checking with your service provider to verify if End-Device certification is required for network access. Switching to a provider that does not have such requirements may resolve these issues. We advise reviewing this compatibility information during setup to ensure optimal device performance and to prevent potential service interruptions.***

You need to enter the Pin code and the APN link of your provider.

The username and password depend on your provider; these are required to authenticate with the APN gateway. These values can usually be found by searching online for APN credentials and provider names. Sometimes they can be left blank.

The following sketch will initialize the SIM card and connect to your provider network within supported bands:

```cpp
#include <GSM.h>

char pin[]      = SECRET_PIN;     //example "1234"
char apn[]      = SECRET_APN;    //example "live.provider.com"
char username[] = SECRET_USERNAME;
char pass[]     = SECRET_PASSWORD;

void setup() {
  Serial.begin(115200);
  while(!Serial) {}

  if(GSM.begin(pin, apn, username, pass, CATM1)){
    Serial.println("connected");
    // ...
  }
}
```

The following example shows how the `GSM.begin()` method would look if you were to define the frequency band for the shield to mask multiple bands to be used or searched. The `BAND_20` and `BAND_19` are one example of a combination of bands to configure credential to restrict the shield's network to the compatible region. It will allow to increase the network search speed and reduce the time spent seeking, saving power consumption of the device.

```cpp
void setup() {
  Serial.begin(115200);
  while(!Serial) {}

  if(GSM.begin(pin, apn, username, pass, CATM1, BAND_20 | BAND_19)){
    Serial.println("connected");
    // ...
  }
}
```

Please check how the frequency band configuration works briefly within the [Available Frequency Bands section](#available-frequency-bands). The list of available frequency bands for the shield's cellular connectivity configuration can also be found in the previous [section](#available-frequency-bands).

#### Send a HTTP GET Request and Receive Data

The following sketch will connect to your provider and use a HTTP GET request to get data from the server you are connected to. In this case, it connects to "example.com" and prints out the content through the Serial Monitor.

```cpp
#include <GSM.h>

REDIRECT_STDOUT_TO(Serial);

char pin[]      = SECRET_PIN; 		//example "1234"
char apn[]      = SECRET_APN;		  //example "live.provider.com"
char username[] = SECRET_USERNAME;
char pass[]     = SECRET_PASSWORD;

const char  server[] = "www.example.com";
const char* ip_address;
int port = 80;

GSMClient client;

void setup() {
  Serial.begin(115200);
  while(!Serial) {}

  GSM.begin(pin, apn, username, pass, CATNB);
  
  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  if (client.connect(server, port)) {
    Serial.println("connected to server");
    // Make a HTTP request:
    client.println("GET / HTTP/1.1");
    client.print("Host: ");
    client.println(server);
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("unable to connect to server");
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
```

## GPS

### Requirements

The GPS feature requires:

* A GPS active antenna (e.g [GPS active antenna 28dB](https://www.digikey.com/en/products/detail/adafruit-industries-llc/960/5353630)) connected to the **GNS ANT** antenna connector on the top side of the shield.
* You may need a connector converter from the active GPS antenna, we used this one [Coaxial to SMA](https://www.digikey.com/en/products/detail/taoglas-limited/CAB.719/3664639)

To check if your setup is properly working, you can open an example inside the GSM library from the Mbed Portenta Core, going to **Examples > GSM > GNSSClient**. You will open an sketch that connects to the SIM card provider and initializes the active GPS antenna. At this point, it will print out GPS readings.

Make sure you go to the `arduino_secrets.h` tab and:

* Add the PIN of the SIM card you are using and store it in the variable `SECRET_PIN`.
* Browse your IT provider and check the mobile APN link, e.g "online.provider.com" save it inside the `SECRET_APN`

***Sometimes it takes time to connect to the provider's APN, please be patient, it can take up to 30 minutes. If you cannot connect after that time, make sure you added the correct SIM pin and the APN. If the issue continues, contact your provider and verify whether Cat. M1 is enabled on your SIM card.***

### API

| Command                 | Information                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `GPS.begin()`           | Initialize the GPS modem                                     |
| `GPS.end()`             | Turn OFF the GPS modem                                       |
| `GPS.available()`       | Check if the GPS has new data to be read                     |
| `GPS.read()`            | Returns a `char` with the reading from the GPS module        |
| `GPS.readAndPrint()`    | Output data on the Serial Monitor, only if there is new data |
| `GPS.readAndDrop()`     | Read the data and do nothing with it                         |
| `GPS.checkGNSSEngine()` | Check if the GNSS modem is receiving data correctly          |

#### Get GPS Data

The following example connects to the GSM provider, then initializes the GPS antenna, gets data and prints them out on the Serial Monitor. As done previously, you need to provide the GSM data by filling the secrets in `arduino_secrets.h`

Open the example by going to **Examples > GSM > GNSSClient**.

```arduino
  #include <GPS.h>
  #include <GSM.h>

  REDIRECT_STDOUT_TO(Serial);

  #include "arduino_secrets.h"
  char pin[]      = SECRET_PIN;
  char apn[]      = SECRET_APN;
  char username[] = SECRET_USERNAME;
  char pass[]     = SECRET_PASSWORD;

  void setup() {
    Serial.begin(115200);
    while (!Serial) {}
    //GSM.debug(Serial);
    Serial.println("\nStarting connection to GSM...");
    GSM.begin(pin, apn, username, pass, CATNB);

    Serial.println("\nEnable GNSS Engine..."); 
    GPS.begin();  //start and enable the GNSS engine
    Serial.println("\nGNSS Engine enabled...");
  }

  void loop() {
    while(GPS.available()){
      Serial.print((char) GPS.read());
      delay(1);
    }

    delay(1000);
  }
```

***Remember to connect to the GSM provider first and secondly connect to the GNSS (mandatory).***

You will see the **NMEA** data in the Serial Monitor.

![NMEA log example Serial Monitor](assets/NMEA_output.png)

#### Parse NMEA GPS Sentences

Previously we went through how to show the GPS data in the Serial Monitor, but it was not possible to evaluate those messages (NMEA sentences).

To do so, you can use an **NMEA parser**. This will convert messages received from the GPS modem, parsing and saving them into variables. You can use the **107-Arduino-NMEA-Parser** library. This library can be found in the library manager inside the Arduino IDE.

In this way, it is possible to interact with the data that you need for your application, for instance getting only latitude and longitude. You will be able to save those values into variables, instead of having the whole NMEA messages.

Open the example from the library at **Examples > 107-Arduino-NMEA-Parser > NMEA-Basic** and add the following:

Include the needed libraries.

```cpp
  #include "GPS.h"
  #include "GSM.h"
  #include "ArduinoNmeaParser.h"
  #include "Arduino_secrets.h"

  char pin[]      = SECRET_PIN;
  char apn[]      = SECRET_APN;
  char username[] = SECRET_LOGIN;
  char pass[]     = SECRET_PASS;
```

Inside the `setup()` initialize the GSM and GPS modules.

```cpp
  void setup(){
    Serial.begin(115200);
    while (!Serial) {}
    Serial.println("GSM...");
    GSM.begin(pin, apn, username, pass, CATNB);
    Serial.println("GPS...");
    GPS.begin();
    Serial.println("Success");
  }
```

Edit the loop to parse the `GPS` readings instead of the `Serial1`.

```cpp
  void loop(){
    while(GPS.available()){
      parser.encode((char)GPS.read());
    }
  }
```

***You will see the output data as various "-1" until the GPS has enough visible satellites to get the correct data. Make sure the GPS antenna is pointing at the sky.***

#### Low Power GPS

The GPS antenna is active, that means that it needs power to function as it has electronics inside of it.

One way to save power on your project is to enable the GPS module only when it needs to read data:

```cpp
  //Start the GPS module
  GPS.begin();    

  // Print data
  while(GPS.available()){
    Serial.print((char) GPS.read());
    delay(1);
  }

  //stop and disable the GNSS engine
  GPS.end();
```

By using this method, you don't need to initialize the GPS inside the `setup()`.

## Conclusion

This cheat sheet is written as a quick reference to look up the GSM and GPS feature of this product. For a more in-depth walk through experience, please have a look at the other tutorials.

## Troubleshooting

- If you are getting compiling errors using GPS and GSM, make sure you included first the `GPS.h` library and then the `GSM.h`.
- Sometimes, while the GPS module is getting readings, you will not be able to upload a new sketch. Double tap the reset button on your Portenta H7 and upload the new sketch.
