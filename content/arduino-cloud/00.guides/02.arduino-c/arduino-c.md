---
title: 'Arduino / C++'
description: 'Get started with the Arduino IoT Cloud using the Arduino / C++ programming language.'
tags: [IoT Cloud, Setup]
author: 'Karl Söderby'
---

The default option for programming your board to connect to the Arduino IoT Cloud is by using the **Arduino / C++ language**. The configuration and connection between your board and the IoT Cloud is supported by the [ArduinoIoTCloud library](https://github.com/arduino-libraries/ArduinoIoTCloud) & [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) libraries.

Whenever you create a [Thing](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/cloud-interface/things) in the IoT Cloud, you automatically start generating a set of files that will handle the configurations, credentials & connection:
- `<sketchname>.ino` - your main sketch file,
- `thingProperties.h` - your main configuration file,
- `arduino_secrets.h` - your credentials file (for API key, Wi-Fi network etc.)

In this guide, we will take a look at how you can connect to the IoT Cloud using the Arduino / C++ programming language.

***If you want to find out more about what the Arduino Cloud service can do, go to the [overview](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/guides/overview) section.*** 

## Requirements

- [Registered account at Arduino](https://login.arduino.cc/login),
- [Cloud compatible board](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/hardware/devices#type-of-devices)

## Setup

In this section, we will go through the steps necessary to connect your Arduino board to the IoT Cloud. To follow these steps, please make sure you have a [registered Arduino account](https://login.arduino.cc/login), and that you have access to the [Arduino Cloud](app.arduino.cc).

### Configure Device

First navigate to [IoT Cloud](app.arduino.cc), and click on the **Devices** tab. Here you can see all your devices, and configure a new one. Depending on what type of board you have, the configuration will vary. 

***For more details, see the [documentation for IoT Cloud devices](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/hardware/devices).***

### Configure Thing

Next, navigate to the **Things** tab. Here you will see a list of your Things, and a button to create a new one. When you create a new Thing, you will open up a new configuration space.

![Arduino IoT Cloud Thing Interface](assets/thing-config.png)

A "Thing" is a virtual twin of your hardware, and it is here that we create variables that we want to synchronize between the cloud and board. Any changes we make here will be reflected in an [automatically generated sketch](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/cloud-interface/sketches#iot-sketches).

1. First, let's attach the device we want to use, by clicking the **"Select Device"** button in the **"Associated Devices"** section to the right. 
2. let's create a new variable, call it `test`, and select it to be a `boolean` type and with a **read/write** permission.
3. finally, configure your network in the **Network** section. Here you will enter your Wi-Fi® credentials, and if you are using an ESP32 based board, you need to enter the secret key here. 

All the above configurations have now been generated into a set of files that can be accessed in the **Sketch** tab.

***For more details, see the [documentation for IoT Cloud Things](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/cloud-interface/things).***

### Complete Sketch

The automatically generated sketch is now available to be edited. This sketch includes all necessities to connect to the cloud, and has a callback function generated for each **read/write** variable.

Below is a sketch generated for a single `boolean` variable called `test`. We modified it to turn on/off the built-in LED of the board anytime the `test` bool is `true`.

```arduino
#include "thingProperties.h"

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  

  Serial.begin(9600);
  delay(1500); 

  initProperties();

  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();
}

void onTestChange()  {
  if(test){
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else{
    digitalWrite(LED_BUILTIN, LOW);
  }
}
```

- The sketch is automatically updated whenever you change your Thing (e.g. adding a variable, changing device),
- **Read/Write** permission variables adds a callback function to the bottom of your code. This function executes whenever the variable changes,
- the `ArduinoCloud.update()` function synchronises data between the board and cloud.
- if we update the `test` variable in the sketch, if it is connected to the cloud, we will see the change there as well. 

### Compile & Upload

When our sketch is ready, we can **compile & upload** our sketch to our board. This process can take some time, depending on how large your sketch is.

1. First, make sure your board is connected and visible in the board selection menu.
2. Click the verify/upload button.
3. Wait until the code has successfully been uploaded.
4. Open the serial monitor tool to check for debug messages. If your board is failing to connect, it will print the errors here.

### Verify Connection

After a complete upload, you can verify the connection by checking the Thing interface. Here you can see the latest value & time stamp, as well as your device status (online/offline).

In this case, we have just a single boolean variable named `test`, which is used to switch the state of the built-in LED.

To control the state of the `test` variable, we can setup a **dashboard** and a **switch widget**. This will allow us to control the LED remotely.

1. Go to **Dashboards**, and create a new dashboard.
2. Click on the edit button at the top left, then on the **"Add"** button. Select the Thing you want to associate it with, and then click on **"Create Widgets"**.
3. A switch widget will have generated, which is now linked to your board. Flicking it should control the state of the LED (on/off).

![Controlling built-in LED via a switch widget.]()

***You can find more details in the [Arduino IoT Cloud dashboards documentation](https://docscontentprivate-karlsoderbycloudv2.gatsbyjs.io/arduino-cloud/cloud-interface/dashboard-widgets).***