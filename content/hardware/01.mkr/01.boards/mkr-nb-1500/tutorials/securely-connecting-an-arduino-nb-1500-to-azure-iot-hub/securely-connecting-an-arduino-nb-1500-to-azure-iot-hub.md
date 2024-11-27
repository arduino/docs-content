---
title: "Securely Connecting an Arduino NB 1500 to Azure IoT Hub"
description: "In this tutorial, you'll learn how to connect your Arduino MKR NB 1500 board securely to Microsoft Azure IoT Hub."
coverImage: "assets/blob_0BNRV79ZAC.png"
tags: [arduino, azure, iot]
author: "Arduino_Genuino"
difficulty: advanced
source: "https://create.arduino.cc/projecthub/Arduino_Genuino/securely-connecting-an-arduino-nb-1500-to-azure-iot-hub-af6470"
---

## Components and Supplies

- [Arduino MKR NB 1500](https://store.arduino.cc/arduino-mkr-nb-1500)
- [Micro-USB to USB Cable (Generic)](https://www.sparkfun.com/products/13244)
- 3.7V Lipo Battery
- Micro SIM card

## Apps and Online Services

- [Arduino IDE](https://www.arduino.cc/en/main/software)
- [Microsoft Azure](http://azure.microsoft.com/en-us)

## About This Project

### Introduction

[Azure IoT Hub](https://azure.microsoft.com/en-ca/services/iot-hub/) allows you to "securely connect, monitor, and manage billions of device to develop Internet of Things (IoT) applications."

Devices can connect to Azure IoT Hub using the following protocols: HTTPS, AMPQ and [MQTT](http://mqtt.org/) - Azure also provides SDKs for many programming languages to abstract these protocols. In addition, you can connect to IoT Hub via an MQTT client. [This page](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support) has more information on IoT Hub’s MQTT support. 

This tutorial will walk you through how to connect an [Arduino MKR NB 1500](https://store.arduino.cc/arduino-mkr-nb-1500) board securely to Azure IoT Hub using an MQTT client. MQTT (Message Queuing Telemetry Transport) is a M2M (machine-to-machine) connectivity protocol which provides a messaging subscription and publish transport.

Devices can use SAS tokens or X.509 certificates for authentication with Azure IoT Hub, more information can be found [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-security#authentication). In this tutorial, we'll use an X.509 certificate to authenticate the board.

Every Arduino MKR board with on-board connectivity, including the MKR NB 1500, is equipped with a Microchip [ATECC508A ](https://www.microchip.com/wwwproducts/en/ATECC508A)or [ATECC608A ](https://www.microchip.com/wwwproducts/en/ATECC608A)crypto element. This crypto element can be used to securely generate and store a 256-bit ECC (Elliptic Curve Cryptography) key.

## Software and Hardware Setup

If you don't have the Arduino IDE installed on your computer, [download ](https://www.arduino.cc/en/Main/Software#download)and install it.

Once it is installed, make sure you have the latest "Arduino SAMD Boards" package installed. You can check by opening the Arduino IDE, and opening the **Tools -> Board: "..." -> Board Manager...** menu entry, and searching for "Arduino SAMD". At the time of writing 1.6.20 was the latest version.

![The Boards Manager.](assets/screen_shot_2019-01-14_at_1_41_18_pm_eozydjsucj_MTEFBZMi4I.png)

Next you'll need to install the Arduino libraries that will be used, using the Arduino IDE's library manager. Open the **Sketch -> Include Library -> Manage Libraries...** menu, search for and individually install each of the following libraries:

* MKRNB
* ArduinoBearSSL
* ArduinoECCX08
* ArduinoMqttClient
* Arduino Cloud Provider Examples

Now insert the micro SIM card in the slot on the bottom of the MKR NB 1500 board and attach the 3.7V Lipo battery to the JST PH connector. Then plug in the MKR NB 1500 with the micro USB cable to your computer, select the serial port in the Arduino IDE using the **Tools -> Port "..."** menu and also select Arduino MKR NB 1500 in the **Tools -> Board "..."** menu.

![Select Arduino MKR NB 1500](assets/screen_shot_2019-02-06_at_11_12_43_am_ydThma23S0.png)

### Configuring and Adding the Board to Azure IoT Hub

As mentioned above, Azure IoT Hub allows devices that connect using the MQTT protocol and use X.509 certificates for authentication. We'll use a sketch to generate a self signed X.509 Certificate on the board and then add the SHA1 of this certificate to Azure IoT Hub portal.

The self signed certificate can be generated using an example sketch from the ArduinoECCX08 library. Open the sketch in the Arduino IDE using the **File -> Examples -> ArduinoECCX08 -> Tools -> ECCX08SelfSignedCert**. Click the "Upload" button to build and upload the sketch to your board, then open the Serial Monitor. Make sure the line ending configuration is set to "Both NL & CR."

This sketch will prompt you to permanently configure your ATECC508A to ECC608A crypto element if it is not configured and locked.

 ***Note: This locking process is permanent and irreversible, but is needed to use the the crypto element - the configuration the sketch sets allows to use 5 private key slots with any Cloud provider(or server) and a private key can be regenerated any time for any of  the 5 private key slots (0 - 4).When the board is shipped from the factory, the crypto element is in an un-configured and unlocked state.*** 

After this, you will be prompted for information to include in the self signed certificate, including the issue year, month, day and hour of the certificate and the expiry period in years. For this tutorial we'll be using slot 0 to generate and store the private key used to sign the self signed certificate (slots 1 to 4 can be used to generate and store additional private keys if needed) - then slot 8 will be used to store the issue and expiry date of the certificate along with it's signature.

 ***Note: Since the private key is generated inside the crypto element it never leaves the device and is stored securely and cannot be read.***

![Copy the SHA1 value from the Serial Monitor.](assets/screen_shot_2019-02-06_at_11_18_42_am_0nF40PXFUM.png)

Copy the generated SHA1 value (in this screenshot "**99d6d96fa55bdf08b4040a142a8d0d934bc9d12b**"). We will use it in a later step as a fingerprint for the self signed certificate for the device in Azure IoT Hub.

Now that we have a self signed certificate and the SHA1 fingerprint to identify the board, we need to login into the Azure IoT Hub portal and create a new device for it.

1) Open a web browser and goto [portal.azure.com](https://portal.azure.com/#home).

2) If you don't already have an Azure account, click the "Create one!" link on the page to create an account. Otherwise, enter your email address and click "Next" and follow the login process.

3) On the navigation panel on the left click "Create a resource".

![Click on Create a resource.](assets/screen_shot_2019-02-06_at_11_31_59_am_BCiXzzVb6B.png)

4) Then click "Internet of Things" and "IoT Hub".

![Click "Internet of Things" and "IoT Hub".](assets/screen_shot_2019-02-06_at_11_32_55_am_70FtZx2ONv.png)

5) You will be prompted to select a Subscription, Resource group, Region and IoT Hub Name. In the screenshot below, "Free Trial", "MKR", "East US", and "ArduinoProjectHubTutorial" were used as input. Click "Review + Create" to continue.

![Click "Review + Create".](assets/screen_shot_2019-02-06_at_11_33_57_am_WfK9CNlAeW.png)

6) A confirmation screen will appear click "Create".

![Click on "Create".](assets/screen_shot_2019-02-06_at_11_38_11_am_KIC539EmPB.png)

7) You will have to wait a few minutes for the IoT Hub to be created and deployed.

![Patiently wait for the deployment.](assets/screen_shot_2019-02-06_at_11_39_50_am_miK5xAbnkk.png)

8) Once deployment is complete a "Go to resource" button will appear, click it.

![Click on the "Go to Resource" button.](assets/screen_shot_2019-02-06_at_11_41_24_am_Pc6ceryFpG.png)

9) Now we can create a new IoT device, click "IoT Devices" under the "Explore" heading.

![Click on "IoT Devices"](assets/screen_shot_2019-02-06_at_11_43_03_am_UtlINb9CIv.png)

10) Click the "Add" button to add a new device.

![Add a new device.](assets/screen_shot_2019-02-06_at_11_44_53_am_SScl9pCOoY.png)

11) Enter a name for the device, below "MyMKRNB1500" was entered, then click the "X.509 Self-Signed" tab. Paste the SHA1 from the Arduino IDE's serial monitor for both the Primary and Secondary Thumbprint. Then click the "Save" button to create the device.

![Name your device.](assets/screen_shot_2019-02-06_at_11_46_27_am_mW0Ct5VJgL.png)

12) You will now see a new entry on the IoT Devices page.

![A new entry is available on the IoT Devices page.](assets/screen_shot_2019-02-06_at_11_48_58_am_N4DTasqUY8.png)

## Connecting the Board to Azure IoT Hub

1) Open the Azure IoT Hub NB sketch in the Arduino IDE using **File -> Examples -> Arduino Cloud Provider Examples -> Azure IoT Hub-> Azure_IoT_Hub_NB**.

2) In the arduino_secrets.h tab, fill in the pin (if required) for the SIM card.

```arduino
// NB settings
#define SECRET_PINNUMBER ""
```

3) Update the broker value with the endpoint created in the Azure IoT Hub portal.

```
// Fill in the hostname of your Azure IoT Hub broker
#define SECRET_BROKER    "<hub name>.azure-devices.net"
```

4) Update the device id value, with the name of the device you created in the Azure IoT Hub portal.

```
// Fill in the device id
#define SECRET_DEVICE_ID "<device id>"
```

5) Upload the sketch to your board and open the serial monitor. The board will attempt to connect to the cellular network and if successful try to connect to Azure IoT Hub using MQTT.

![Open the serial monitor.](assets/screen_shot_2019-02-06_at_12_17_47_pm_742RPWyv70.png)

## Interacting with the Board on Azure IoT Core

Now that your board has successfully connected to Azure IoT Hub, we can use the Azure IoT Hub portal to interact with it. The sketch sends a message to the **devices/{deviceId}/messages/events/** topic every 5 seconds and listens for messages on the **devices/{deviceId}/messages/devicebound/#** topic.

In the Azure IoT Hub portal, click the device id row in the IoT Devices table for your board. Then click the "Message to device" button in the toolbar.

![Click "Message to device"](assets/screen_shot_2019-02-06_at_12_06_14_pm_554ggffxiP.png)

You can now enter a message body to send to the device, in the screenshot below "**Hello there :)**" was entered. Click the "Send Message" button in the toolbar to send the message.

![Send your message!](assets/screen_shot_2019-02-06_at_12_07_18_pm_jZHRAyebN2.png)

When the board receives the message, the Serial Monitor in the Arduino IDE will display it.

![The message in the Serial Monitor.](assets/screen_shot_2019-02-06_at_12_10_00_pm_gG05TyCAkn.png)

To view the messages the board is sending:

1) Log into [shell.azure.com](https://shell.azure.com/) (select "Bash" if this is your first time when prompted).

2) Install the IoT Hub Extension:

```arduino
az extension add --name azure-cli-iot-ext
```

3) Run the following command, replace `<hub name>` with the name of your hub (enter y if prompted for dependency update):

```arduino
az iot hub monitor-events --hub-name <hub name> 
```

4) You will see messages printed to the shell:

![Azure Cloud Shell.](assets/screen_shot_2019-02-06_at_3_52_49_pm_Z5dD8i6OYs.png)

## Complete Sketch

```arduino
*
  Azure IoT Hub NB
  This sketch securely connects to an Azure IoT Hub using MQTT over NB IoT/LTE Cat M1.
  It uses a private key stored in the ATECC508A and a self signed public
  certificate for SSL/TLS authentication.
  It publishes a message every 5 seconds to "devices/{deviceId}/messages/events/" topic
  and subscribes to messages on the "devices/{deviceId}/messages/devicebound/#"
  topic.
  The circuit:
  - MKR NB 1500 board
  - Antenna
  - SIM card with a data plan
  - LiPo battery
  The following tutorial on Arduino Project Hub can be used
  to setup your Azure account and the MKR board:
  https://create.arduino.cc/projecthub/Arduino_Genuino/securely-connecting-an-arduino-nb-1500-to-azure-iot-hub-af6470
  This example code is in the public domain.
*/

#include <ArduinoBearSSL.h>
#include <ArduinoECCX08.h>
#include <utility/ECCX08SelfSignedCert.h>
#include <ArduinoMqttClient.h>
#include <MKRNB.h>

#include "arduino_secrets.h"

/////// Enter your sensitive data in arduino_secrets.h
const char pinnumber[]   = SECRET_PINNUMBER;
const char broker[]      = SECRET_BROKER;
String     deviceId      = SECRET_DEVICE_ID;

NB nbAccess;
GPRS gprs;

NBClient      nbClient;            // Used for the TCP socket connection
BearSSLClient sslClient(nbClient); // Used for SSL/TLS connection, integrates with ECC508
MqttClient    mqttClient(sslClient);

unsigned long lastMillis = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!ECCX08.begin()) {
    Serial.println("No ECCX08 present!");
    while (1);
  }

  // reconstruct the self signed cert
  ECCX08SelfSignedCert.beginReconstruction(0, 8);
  ECCX08SelfSignedCert.setCommonName(ECCX08.serialNumber());
  ECCX08SelfSignedCert.endReconstruction();

  // Set a callback to get the current time
  // used to validate the servers certificate
  ArduinoBearSSL.onGetTime(getTime);

  // Set the ECCX08 slot to use for the private key
  // and the accompanying public certificate for it
  sslClient.setEccSlot(0, ECCX08SelfSignedCert.bytes(), ECCX08SelfSignedCert.length());

  // Set the client id used for MQTT as the device id
  mqttClient.setId(deviceId);

  // Set the username to "<broker>/<device id>/api-version=2018-06-30" and empty password
  String username;

  username += broker;
  username += "/";
  username += deviceId;
  username += "/api-version=2018-06-30";

  mqttClient.setUsernamePassword(username, "");

  // Set the message callback, this function is
  // called when the MQTTClient receives a message
  mqttClient.onMessage(onMessageReceived);
}

void loop() {
  if (nbAccess.status() != NB_READY || gprs.status() != GPRS_READY) {
    connectNB();
  }

  if (!mqttClient.connected()) {
    // MQTT client is disconnected, connect
    connectMQTT();
  }

  // poll for new MQTT messages and send keep alive
  mqttClient.poll();

  // publish a message roughly every 5 seconds.
  if (millis() - lastMillis > 5000) {
    lastMillis = millis();

    publishMessage();
  }
}

unsigned long getTime() {
  // get the current time from the cellular module
  return nbAccess.getTime();
}

void connectNB() {
  Serial.println("Attempting to connect to the cellular network");

  while ((nbAccess.begin(pinnumber) != NB_READY) ||
         (gprs.attachGPRS() != GPRS_READY)) {
    // failed, retry
    Serial.print(".");
    delay(1000);
  }

  Serial.println("You're connected to the cellular network");
  Serial.println();
}

void connectMQTT() {
  Serial.print("Attempting to MQTT broker: ");
  Serial.print(broker);
  Serial.println(" ");

  while (!mqttClient.connect(broker, 8883)) {
    // failed, retry
    Serial.print(".");
    Serial.println(mqttClient.connectError());
    delay(5000);
  }
  Serial.println();

  Serial.println("You're connected to the MQTT broker");
  Serial.println();

  // subscribe to a topic
  mqttClient.subscribe("devices/" + deviceId + "/messages/devicebound/#");
}

void publishMessage() {
  Serial.println("Publishing message");

  // send message, the Print interface can be used to set the message contents
  mqttClient.beginMessage("devices/" + deviceId + "/messages/events/");
  mqttClient.print("hello ");
  mqttClient.print(millis());
  mqttClient.endMessage();
}

void onMessageReceived(int messageSize) {
  // we received a message, print out the topic and contents
  Serial.print("Received a message with topic '");
  Serial.print(mqttClient.messageTopic());
  Serial.print("', length ");
  Serial.print(messageSize);
  Serial.println(" bytes:");

  // use the Stream interface to print the contents
  while (mqttClient.available()) {
    Serial.print((char)mqttClient.read());
  }
  Serial.println();

  Serial.println();
}
```



## Conclusion

In this tutorial, we covered how to securely use an Arduino MKR NB 1500 board with Azure IoT Hub. A self signed X.509 certificate was used to authenticate with Azure IoT Hub using the MQTT protocol with the ATECC508A or ATECC608A storing the private key associated with the certificate. MQTT messages were sent to and from the board.

This is just the beginning, you can use Azure IoT Hub with many of the other services Azure provides!