---
title: Connecting the Portenta Max Carrier to The Things Network
description: This tutorial explains how to connect your Portenta Max Carrier to the Things Network(TTN) using its onboard LoRaWAN® module.
difficulty: intermediate
tags:
  - IoT
  - LoRaWAN®
author: Taddy Chung, José Bagur
libraries:
  - name: MKRWAN
hardware:
  - hardware/04.pro/carriers/portenta-max-carrier
  - hardware/04.pro/boards/portenta-h7
software:
  - ide-v1
  - ide-v2
---

## Overview

This tutorial explains how to connect your [Arduino® Max Carrier](http://store.arduino.cc/portenta-max-carrier), with an [Arduino® Portenta H7](https://store.arduino.cc/products/portenta-h7) to The Things Network (TTN) using its onboard LoRaWAN® module. The article will focus on achieving communication between the Max Carrier and an application on TTN. 

## Goals

* Enable LoRaWAN® connectivity on the Portenta Max Carrier.
* Establish a connection between the Portenta Max Carrier and TTN.


### Required Hardware and Software

- [Portenta H7](https://store.arduino.cc/products/portenta-h7).
- [Portenta Max Carrier](http://store.arduino.cc/portenta-max-carrier).
- 868-915 MHz antenna with SMA connector.
- USB-C® cable (either USB-A to USB-C® or USB-C® to USB-C®).
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [Arduino MKRWAN library](https://github.com/arduino-libraries/MKRWAN).  
- An active account in [TTN](https://www.thethingsnetwork.org/).

## The Arduino® Portenta Max Carrier LoRaWAN® Module

The Portenta Max Carrier provides you with an unlimited range of applications, from robotics and medical devices to industrial or automotive applications; the Max Carrier possibilities are endless. One feature that boosts Portenta's Max Carrier possibilities is its **onboard LoRaWAN® module**, the [CMWX1ZZABZ-078](https://www.murata.com/products/connectivitymodule/lpwa/overview/lineup/type-abz-078) from Murata®. LoRaWAN® is a Low Power Wide Area Network (LPWAN) designed to connect low power devices to the Internet. It was developed to meet and fulfill Internet of Things (IoT) devices' requirements, such as low-power consumption and low data throughput. 

![CMWX1ZZABZ-078 LoRaWAN® module in the Portenta Max Carrier.](assets/mc_ard_ttn_module.png)

***For more in-depth information about LoRa® and LoRaWAN®, please read [The Arduino Guide to LoRa® and LoRaWAN®](/learn/communication/lorawan-101).***

## Connecting to TTN

Let's start sending data to TTN using the Portenta Max Carrier LoRaWAN® module. To do this, you will need a TTN account and to be in the range of a public TTN gateway. You can check the [world map](https://www.thethingsnetwork.org/map) of public gateways connected to TTN and see if your region already has a gateway installed. If not, consider installing one!

***Check out [this](https://www.thethingsnetwork.org/docs/gateways/) article from TTN, where you can find how to buy or build your gateway to extend TTN coverage in your region.***

To connect your Portenta Max Carrier to TTN, we must follow these steps:

1. Hardware setup.
2. Software setup.
3. Portenta Max Carrier provisioning. 
4. Create an application in TTN.
5. Send a message to a TTN application.

Let's start!

### 1. Setting up the Hardware 

Begin by attaching the Arduino® Portenta H7 board to the high-density connectors of the Portenta Max Carrier, as shown in the image below:

![CMWX1ZZABZ-078 LoRaWAN® module in the Portenta Max Carrier.](assets/mc_ard_hd_ttn_connectors.png)

To power the CMWX1ZZABZ-078 LoRaWAN® module of the Portenta Max Carrier, you can use the **DC power jack** (with a 4.5V to 36V external DC power supply) of the Portenta Max Carrier or a **18650 3.7V Li-Ion battery**, connected to the Portenta Max Carrier battery clips; you can power the module also directly from the USB-C® connector of the Portenta H7 board. **Also, do not forget to attach an 868-915 MHz antenna to the SMA connector (J9) on the Max Carrier**.

![Power sources and LoRa® antenna connector in the Portenta Max Carrier.](assets/mc_ard_ttn_power.png)

***Using the LoRaWAN® module of the Portenta Max Carrier without an antenna may damage it. Please, do not forget to connect a suitable antenna to the dedicated SMA connector (J9) on the Portenta Max Carrier.***

Now you can connect the Portenta H7 board to your computer using a USB-C® cable. **Don't forget to change the position of the BOOT DIP switch (SW1) to OFF** ; otherwise, you will not be able to program your Portenta H7 board when attached to the Portenta Max Carrier.

![Power sources and LoRa® antenna connector in the Portenta Max Carrier.](assets/mc_ard_ttn_boot_sel.png)

### 2. Setting up the Software

You can use several Arduino libraries with the CMWX1ZZABZ-078 LoRaWAN® module from Murata®; we recommend the [MKRWAN library](https://github.com/arduino-libraries/MKRWAN), developed by the Arduino Team. The MKRWAN library provides you with the APIs to communicate with LoRa® and LoRaWAN® networks using the CMWX1ZZABZ-078 module. You can use this library in the Arduino IDE, both [online](https://create.arduino.cc/editor) and [offline](https://www.arduino.cc/en/software). 

If you are using the online IDE, you don't need to do anything; the library is already installed and ready to be used. If you are using the offline IDE, you must install the library **manually**. Installing the library can be done quickly by navigating to **Tools > Manage Libraries...** and then in the **Library Manager** search for **MKRWAN** library by Arduino; remember to install the latest version of the libraries. You can also access the Library Manager using the left toolbar of the IDE, as shown in the image below:

![Library Manager in the Arduino IDE 2.](assets/mc_ard_ttn_library.png)

***Currently, there are two versions of the MKRWAN library. We recommend using the MKRWAN_v1 library since MKRWAN_v2 library is still in beta phase.***

To use the MKRWAN library with the Portenta Max Carrier, you must define `PORTENTA_CARRIER` before the library inclusion, as shown below:

```arduino
#define PORTENTA_CARRIER
#include <MKRWAN.h>
```

#### 2.1 Updating the LoRaWAN® Module Firmware

The LoRaWAN® module firmware of the Portenta Max Carrier **must be updated** before its first use. This can be done using the example sketch `MKRWANFWUpdate_standalone` of the MKRWAN library. You can open this example by navigating to **File > Examples > MKRWAN**. Before uploading the sketch to the Portenta H7 board, open the `MKRWANFWUpdate_standalone.ino` file and define `PORTENTA_CARRIER` before the library inclusion, as shown in the image below:

![Library Manager in the Arduino IDE 2.](assets/mc_ard_ttn_firmware_1.png)

Upload the sketch, open the Serial Monitor and wait for the firmware update to finish. You should see a confirmation message when the process is done.


### 3. Provisioning the Arduino® Portenta Max Carrier

Device provisioning is a process comparable to bank card numbering. Let's think about bank cards; bank cards numbers start with a six-digit vendor ID number that indicates who allocated and controls the card's security; the remaining digits are unique numbers associated with a specific card. Devices with LoRa® and LoRaWAN® capabilities have a similar system; the **Join Server Unique Identifier** (usually referred to as `JoinEUI`) is a number that manages the security and authorizes the device in a network, while the **Device Unique Identifier** (usually referred to as `DevEUI`) is a unique number that identifies the device. The `JoinEUI` and `DevEUI` are required to send information to TTN; the `JoinEUI` number is provided by the network (in this case TTN) while the `DevEUI` is provided by the manufacturer of the device's LoRa® module. 

The following sketch lets you find out what is the `DevEUI` of your Portenta Max Carrier: 

```arduino
#define PORTENTA_CARRIER
#include <MKRWAN.h>

auto region = US915;

LoRaModem modem(SerialLoRa);

void setup() {
  Serial.begin(115200);
  while(!Serial);

  if(!modem.begin(region)) {
    Serial.println("Failed to start the module...");
    while(1) {}
  }

  Serial.print("Your Portenta Max Carrier DevEUI is: ");
  Serial.println(modem.deviceEUI());  
}

void loop() {}
```

The only line you may need to change before uploading the code is the one that sets the frequency:

```arduino
auto region = US915;
```

Set the frequency designator according to your country. You can find more information about frequency plans definitions used in TTN [here](https://www.thethingsnetwork.org/docs/lorawan/frequency-plans/). After you upload the sketch to your Portenta H7 board, you should see the Portenta Max Carrier `DevEUI` in the Arduino IDE Serial Monitor as shown below:

```arduino
Your Portenta Max Carrier DevEUI is: a861XXXXXXXXXXXX
```

Now, let's use the `DevEUI` number from your Portenta Max Carrier to create an application in TTN. 

### 3. Creating an Application in TTN

To send information to TTN, first we need to **create an application and register a device with it**. Navigate to TTN portal and sign in; after signing in, click on **Create an application**. If you already created an application, click on **Go to applications**.

![TTN console welcome page.](assets/mc_ard_ttn_console_1.png)

Now click on **Create an application**. You will need to add the following information:

* **Owner**: the person or organization that owns the application.
* **Application ID**: a unique identifier for your application (must be lowercase and without spaces).

Complete both fields and click on **Create application**. Now you will be redirected to the application dashboard that shows information of the newly created application. 

![Application dashboard in TTN.](assets/mc_ard_ttn_console_2.png)

Now, scroll to **End devices** in the left toolbar and then click on **Add end device**; a registration page for end devices will open.

![Registering an end device in TTN.](assets/mc_ard_ttn_console_3.png)

On the registration page, click on **Manually**; you will have to add the following information for your Portenta Max Carrier:

* **Frequency plan**: choose a region according to your country.
* **LoRaWAN® version**: 1.0.2.
* **Regional Parameters version**: 1.0.2.

Click on Show advanced activation, **LoRaWAN® class and cluster settings** and choose: 

* **Activation mode**: Over the air activation (OTAA).
* **Additional LoRaWAN® class capabilities**: None (class A only).
* **Network defaults**: Use network's default MAC settings.

Leave the **Cluster settings** option unchecked. Then continue with the following information:

* **DevEUI**: fill it with the `DevEUI` number of your Portenta Max Carrier you found [before](#3-provisioning-the-arduino-portenta-max-carrier).
* **AppEUI**: fill it with zeros or enter your own.
* **AppKey**: generate one or enter your own.
* **Device ID**: A custom identifier for your board, must be lowercase and without spaces. 

Click on **Register end device**; this will take you to a **Device Overview** page where you will see all the information related to the device. Now, you will use some of this information with your Portenta Max Carrier to send data to TTN. 

![Device overview in TTN.](assets/mc_ard_ttn_console_4.png)

### 4. Sending Data to an Application in TTN 

Now, let's start sending information to TTN. The following sketch enables you to join and send data to TTN using the Over the Air (OTAA) device activation method. You will need to define your TTN application's AppEUI and AppKey numbers in the `arduino_secrets.h` file before uploading the code:

```arduino
#define PORTENTA_CARRIER
#include <MKRWAN.h>
#include "arduino_secrets.h"

auto region = US915;

LoRaModem modem(SerialLoRa);

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println(F("Portenta Max Carrier LoRaWAN Example (OTAA)"));
  
  if (!modem.begin(region)) {
    Serial.println(F("Failed to start the module..."));
    while (1) {}
  };
  
  Serial.print(F("Your Portenta Max Carrier module version is: "));
  Serial.println(modem.version());

  if (modem.version() != ARDUINO_FW_VERSION) {
    Serial.println(F("Please make sure that the modem's firmware is updated."));
    Serial.println(F("To update the module's firmware, open and upload the 'MKRWANFWUpdate_standalone.ino' sketch."));
  }
  
  Serial.print(F("Your Portenta Max Carrier DevEUI is: "));
  Serial.println(modem.deviceEUI());

  appKey.trim();
  appEui.trim();

  int connected = modem.joinOTAA(appEui, appKey);

  if (!connected) {
    Serial.println("Something went wrong; are you indoor? Move near a window and retry...");
    while (1) {}
  }

  delay(5000);

  modem.setPort(3);
  modem.beginPacket();
  modem.print("HelLoRa World!");
  int errorCode = modem.endPacket(true);
  if (errorCode > 0) {
    Serial.println("Data sent correctly!");
  } else {
    Serial.println("Error sending data...");
  }
}

void loop() {
  while (modem.available()) {
    Serial.write(modem.read());
  }
  modem.poll();
}
```

The `arduino_secrets.h` file which contains AppEUI and AppKey numbers for the TTN applications can be defined as following code. AppEUI and AppKey information is found on the End device page of the TTN Application. 

```arduino
String appEui = "xxxxxxxxxxxxxxxx";
String appKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
```

If data was sent correctly to TTN, you should see the following messages in the Arduino IDE Serial Monitor: `Data sent correctly!`

In your device overview dashboard on TTN, you should see changes in data activity every time a new message is sent.

## Conclusion

You have now successfully configured and used the onboard LoRaWAN® module of your Portenta Max Carrier. You also have learned how to correctly setup a TTN application and enable LoRaWAN® connectivity between a TTN application and the Portenta Max Carrier.

### Next Steps

- Scale up the usage of Portenta Max Carrier by using its additional peripherals and turning them into interesting industrial-grade projects, taking advantage of LoRaWAN® connectivity.
  
## Troubleshooting

While working on the sketch or when tried to upload the sketch, the Arduino IDE might show some errors preventing to proceed on the development. You can try the following troubleshooting tips to solve the commonly known issues:

* If the sketch upload process fails, check if your Portenta H7 is in bootloader mode. To put the Portenta H7 into Bootloader mode, double-press its RESET button and verify that the green LED is waving. After this, you can try re-uploading the sketch.
* Check the position of the BOOT DIP switch of the Portenta Max Carrier. If the Portenta H7 gets into bootloader mode immediately after power-on, including when connected via USB-C®, change the position of the BOOT DIP switch to OFF.
* If the Arduino IDE fails to compile the sketch, check if you have defined `PORTENTA_CARRIER` before the MKRWAN library inclusion.
