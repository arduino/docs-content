---
title: "Localize Your Board with an SMS"
description: "Get the position of your MKR GSM 1400 on your smartphone through an SMS with a Google Maps link."
coverImage: "assets/blob_FLqNPWjaVR.png"
tags: [monitoring, tracking]
difficulty: intermediate
author: "Arduino_Genuino"
source: "https://create.arduino.cc/projecthub/Arduino_Genuino/localize-your-board-with-an-sms-38e331"
---

## Components and Supplies

- [Arduino MKR GSM 1400](https://www.newark.com/55AC1187?COM=ref_hackster)

## About This Project

The purpose of this project is to show how to use the cellular localization of the Arduino MKR GSM 1400. To do this, we implemented a simple application that allows you to retry the latitude and longitude of the MKR GSM when an SMS with a security check letter is received. The sender number is recovered from the SMS received and a reply is created with the proper Google Maps link completed by the coordinates given by the location services provided by the u-blox module.

### What You Need

The project is based on an Arduino MKR GSM 1400, an antenna, a LiPo battery pack, a smartphone, and one data SIM card.

* The Arduino MKR GSM 1400 executes the sketch and supports the GSM connectivity that allows the localization functions required by our project;
* Antenna and battery pack are respectively used tor allow the connection to the cellular data network with a good signal and to power the device when other power supplies are not available;
* The smartphone is needed to send the SMS to the MKR GSM 1400 and ask for GPRS localization;
* The SIM card is required to access the data network and allow network operation;
* PIN, APN and access credentials are required to connect to the data network.

### Hardware Setup

This project does not require anything special. Connect to the board the antenna, insert the SIM card and connect the LiPo battery to the JST connector. 

The LiPo battery is optional, but it allows to cope with the peaks of current that the GSM module might require in particular conditions of poor coverage.

![The hardware.](assets/track_1_MyS8MNGN27.jpg)

### How It Works

This project uses the MKRGSM library to manage the SMS messages and the cell based georeferentiation. 

When an SMS is received, the content is checked to find out if it contains the letter "L". Only if this is the case, the sketch proceeds with the localization and SMS transmission. With this solution, any number may request the location of the system, but only who knows the password (the "secret letter") will get a reply. This is the line that does the check `if (c != 76)` and 76 is the ASCII code of "L". You can change the value to change the letter recognized.

The GSM module does not have a GPS receiver, but the manufacturer has a database of the location of each cell of the GSM network and therefore it provides coordinates for each cell ID supplied. This system is quite accurate in urban areas, where each cell covers a small areas. In rural areas the coverage of each cell is much bigger and the location provided is with coarser approximation. 

To create the link for Google Maps we use a standard URL where we just concatenate the proper Long and Lat values at the end. This URL looks like "https://www.google.com/maps/place/latvalue,longvalue". The position shown on the map will be the one where the cell is physically based; our board is within the radius covered by the cell. 

### The Sketch

Following a detailed description of the Sketch; the first code section is used to includes the libraries required by the application.

**MKRGSM** include all the GSM connection, localization and SMS management functionalities, this are available through the object **GSMClient, GPRS, GSM** and **GSMLocation,** the SMS management APIs are available through the object **GSM_SMS**, the header **ArduinoLowPower** import the APIs that allow low power management of the Board's module.

If you download the code from the Web Editor, you will find an **arduino_secrets.h** file that includes the sensible data like **PIN, APN, user** and **password.** On the web editor, you have to fill the sensible data in the Secrets Tab.

```arduino
// include the GSM library
#include <MKRGSM.h>
#include "ArduinoLowPower.h"
char PINNUMBER [] = SECRET_PINNUMBER;
char GPRS_APN[] = SECRET_GPRS_APN;
char GPRS_LOGIN [] =SECRET_GPRS_LOGIN;
char GPRS_PASSWORD[] =SECRET_GPRS_PASSWORD;
// initialize the library instances
GPRS gprs;
GSM gsmAccess;
GSM_SMS sms;
GSMLocation location;
```

The `measureLocation()` queries the module to retry the coordinates by cellular network, if new coordinate are available it assign it to the global variable otherwise ask again for 45 second, if no are available measures that respect the accuracy constraints it return the last good ones

```arduino
//global variable used for location management
String GSMlatitude = "0.000000";
String GSMlongitude = "0.000000";
// This function use the location's APIs to get the device coordinates and update the global variable if all the requirement are satisfied
void measureLocation() {
unsigned long timeout = millis();
while (millis() - timeout < 45000) {
if (location.available() && location.accuracy() < 300 && location.accuracy() != 0) {
GSMlatitude = String(location.latitude(), 6);
GSMlongitude = String(location.longitude(), 6);
break;
}
}
}
```

The `connectNetwork()` function use the API **smAccess.begin** and **gprs.attachGPRS** to connect the board to the data network; are used the credentials data **pin**, **apn**, **user** and **pass** assigned by the declarations in arduino_secrets.h.

```arduino
// The connectNetwork() function is used for the board data connection
void connectNetwork()
{
bool status = false;
//set global AT command timeout this allow to recover from uart communication
// freeze between samd module and ublox module.
gprs.setTimeout(100000);
gsmAccess.setTimeout(100000);
// Start GSM connection
while (status == false) {
if ((gsmAccess.begin(PINNUMBER) == GSM_READY) &
(gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD) == GPRS_READY)) {
status = true;
} else {
delay(1000);
}
}
}
The setup section allow to initialize all the object used by the sketch, is called the connectionNetwork() function to establish the data connection and the localization structure beginning.
//code section used to initialize data connection and localization object
void setup() {
connectNetwork();
location.begin();
}
```

Last code section is the loop function where are implemented the SMS management and the Location measure, each time that a new SMS is available the board response to the rsender with an SMS with the board's coordinates, to reduce the consumption the board shutdown the module and goes in deep sleep for 60 seconds.

```arduino
void loop() {
 int c;
 String response;
 String messager = "";
 measureLocation();
 unsigned long timeout = millis();
 while (millis() - timeout < 5000) {
if (sms.available()) { //check for SMS available
char senderNumber[20] = {"0"};
sms.remoteNumber(senderNumber, 20); //Get remote number
int c = sms.read();
if (c != 76) {
sms.flush();
break;
}
//concatenate the string message to be sended to the remote number
String txtMsg = "https://www.google.com/maps/place/" + GSMlatitude + "," + GSMlongitude;
// send the message
sms.beginSMS(senderNumber);
sms.print(txtMsg);
sms.endSMS();
break;
}
 }
 //Turn off the GSM module to gain the lowest power consumption from the board while are sleeping
 gsmAccess.shutdown();
 LowPower.sleep(60000); //enable the low power for 60 seconds and after retry the board
 connectNetwork(); //turn on the module and reconnect to data network
}
```

## Complete Sketch
<iframe src='https://create.arduino.cc/editor/Arduino_Genuino/e46cbcc9-24bc-4cdf-b1db-aecc7385e77e/preview?embed&snippet
' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### How to Use It

Set up the hardware as explained above, personalize the sketch with your access credentials, load the sketch on the board, and wait for the connection to be established with the GSM network. This might take 30 seconds.

After that the connection is established, just send an SMS to the MKRGSM SIM number with an "L" as text: this will start the localization process and the board will reply with an SMS containing the Google Maps link with the position requested.