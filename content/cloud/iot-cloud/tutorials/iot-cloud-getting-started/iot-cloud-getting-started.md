---
title: "Getting started with the Arduino IoT Cloud"
compatible-products: [mkr-1000-wifi, mkr-wifi-1010, nano-33-iot, nano-rp2040-connect]
difficulty: easy
description: 'Learn how to configure devices, creating things and programming your boards.'
tags:
  - Getting started
author: 'Karl Söderby'
featuredImage: 'cloud'
---

Getting started with the Arduino IoT Cloud involves just a few simple steps that are quick and easy to follow! Further down this article, there is a section called **A walk through the cloud configuration**, which is there to guide you through the Arduino IoT Cloud. But first, let’s take a look at what we need in order to get started.

But if you’re itching to get started and explore the Arduino IoT Cloud yourself, that is also perfectly fine! You can always come back here for more information!

<a href="https://create.arduino.cc/iot/things" target="_blank">Go to Arduino IoT Cloud</a>

---

## A cloud compatible board (required)

To use the Arduino IoT Cloud, all we need is a **cloud compatible board**. You can choose between using an official Arduino board, or a board based on the ESP32 / ESP8266 microcontroller.

### Arduino boards

In the picture below, we can see all official Arduino boards that are compatible.

![Compatible IoT Cloud boards.](assets/iot-cloud-compatible-boards.png)

- [MKR 1000 WiFi](https://store.arduino.cc/arduino-mkr1000-wifi)
- [MKR WiFi 1010](https://store.arduino.cc/arduino-mkr-wifi-1010)
- [MKR WAN 1300](https://store.arduino.cc/arduino-mkr-wan-1300-lora-connectivity-1414)\*
- [MKR WAN 1310](https://store.arduino.cc/mkr-wan-1310)\*
- [MKR GSM 1400](https://store.arduino.cc/arduino-mkr-gsm-1400)\*
- [MKR NB 1500](https://store.arduino.cc/arduino-mkr-nb-1500-1413)\*
- [Nano RP2040 Connect](https://store.arduino.cc/nano-rp2040-connect)
- [Nano 33 IoT](https://store.arduino.cc/arduino-nano-33-iot)
- [Portenta H7](https://store.arduino.cc/portenta-h7)

>**Please note:** 
The MKR GSM 1400 and MKR NB 1500 require a **SIM card** to connect to the cloud, as they communicate over the mobile networks. The MKR WAN 1300 and 1310 board requires a **Arduino PRO Gateway LoRa** to connect to the cloud.

- You can install the [Arduino PRO Gateway LoRa](https://store.arduino.cc/arduino-pro-gateway-lorar-connectivity) through the [Manager For Linux](https://create.arduino.cc/getting-started/).

***All cloud-compatible Arduino boards come with a hardware secure element (such as the [ECC508](/resources/datasheets/ATECC508A-datasheet.pdf) cryptochip), where you can store your security keys.***

### ESP32 / ESP8266

The Arduino IoT Cloud supports a wide range of 3rd party boards based on the ESP32 and ESP8266 microcontrollers with support for Wi-Fi. To set them up, simply choose the **third party option** in the device setup.

![Configuring 3rd party boards.](assets/3rd-party-support.png)

---

## Need any help?

If you have any problems with the Arduino IoT Cloud, you can browse through common troubleshooting issues and find information on different features in the **Arduino Help Center**. If you don’t find the answer you are looking for, we are always happy to help you with any question regarding our products!

<a href="https://support.arduino.cc/hc/en" target="_blank">Go to Arduino Help Center</a>

---

## A walk through the configuration

![](assets/setup.png)

Setting up the Arduino IoT Cloud and accessing the different features available involves a few simple steps. So let’s take a look at how to go from start to finish!

### 1. Creating an Arduino account

To starting using the Arduino IoT cloud, we first need to [sign up to Arduino](https://login.arduino.cc/login).

#### 2. Go to the Arduino IoT Cloud

After we have signed up, you can access the Arduino IoT Cloud from any page on [arduino.cc](https://www.arduino.cc/) by clicking on the four dots menu in the top right corner. You can also [go directly to the Arduino IoT Cloud](https://create.arduino.cc/iot/).

![Navigating to the cloud.](assets/accesscloud.png)

### 3. Creating a thing

The journey always begin by creating a new **Thing**. In the Thing overview, we can choose what device to use, what Wi-Fi network we want to connect to, and create variables that we can monitor and control. This is the main configuration space, where all changes we make are automatically generated into a **special sketch file**.

![The Thing overview.](assets/thingoverview.png)

### 4. Configuring a device

Devices can easily be added and linked to a Thing. The Arduino IoT Cloud requires your computer to have the [Arduino Agent installed](https://create.arduino.cc/getting-started/plugin/welcome). The configuration process is quick and easy, and can be done by clicking on the **“Select device”** button in the Thing overview. Here, we can choose from any board that has been configured, or select the **“Configure new device”** option.

![Configuring a device.](assets/devicelink.png)

We can also get a complete overview of our devices by clicking the **“Devices"** tab at the top of the Arduino IoT Cloud interface. Here we can manage and add new devices.

![The device tab.](assets/deviceoverview.png)

### 5. Creating variables

The variables we create are automatically generated into a sketch file. There are several data types we can choose from, such as **int, float, boolean, long, char**. There’s also special variables, such as **Temperature, Velocity, Luminance** that can be used. When clicking on the **“Add variable”** button, we can choose name, data type, update setting and interaction mode.

![Creating variables.](assets/variables.png)

### 6. Connecting to a network

To connect to a Wi-Fi network, simply click the **“Configure”** button in the network section. Enter the credentials and click **“Save”**. This information is also generated into your sketch file!

![Entering network credentials.](assets/network.png)

### 7. Editing the sketch

Now, while we have configured variables, devices and network settings we can get to the coding! A special sketch file can now be found in the **“Sketch”** tab, which includes all of these configurations. We can now create a sketch that, for example, reads an analog sensor, and use the **cloud variable** to store it. When the sketch has been uploaded, it will work as a regular sketch, but it will also update the cloud variables that we use!

Additionally, each time we create a variable that has the **Interaction Mode** enabled, a function will also be generated. Each time this variable is triggered from the cloud, it will execute the code within this function! This means that we can leave most of the code out of the **loop()** and only run code when needed.

When we are happy with our sketch, we can upload it to our board, by clicking the upload button.

![Editing a sketch in the cloud editor.](assets/sketchoverview.png)

After we have successfully uploaded the code, we can open the **“Serial Monitor”** tab to view information regarding our connection. If it is successful, it will print **“connected to network_name”** and **“connected to cloud”**. If it fails to connect, it will print the errors here as well.

### 8. Creating a dashboard

Now that we have configured the device & network, created variables, completed the sketch and successfully uploaded the code, we can move on to the fun part: **creating dashboards!**

![](assets/dashboard1.png)

Dashboards are visual user interface for interacting with your boards over the cloud, and we can setup many different setups depending on what your IoT project needs. We can access our dashboards by clicking on the **“Dashboards”** tab at the top of the Arduino IoT Cloud interface, where we can create new dashboards, and see a list of dashboards created for other Things.

![Navigating to dashboards.](assets/navigatedashboard.png)

If we click on **“Create new dashboard”**, we enter a dashboard editor. Here, we can create something called **widgets**. Widgets are the visual representation of our variables we create, and there are many different to choose from. Below is an example using several types of widgets.

![The different widgets available.](assets/dashboard2.png)

When we create widgets, we also need to **link them to our variables**. This is done by clicking on a widget we create, select a Thing, and select a variable that we want to link. Once it is linked, we can either interact with it, for example a button, or we can monitor a value from a sensor. As long as our board is connected to the cloud, the values will update!

Let's say we have a **temperature widget** that we want to link to the **temperature** variable inside the **Cloud project** thing.

![Linking a variable to a widget.](assets/dashboard3.png)

>**Please note:** Not all widgets can be linked to a variable. We can for example not link a **switch widget** to a **int** variable as the data types are different. The variables that a widget can’t link with will be greyed out, so we can’t accidentally link a widget to the wrong variable.

We can also have several things running at once, depending on your Arduino IoT Cloud plan, which we can include in the same dashboard. This is a great feature for tracking multiple boards in for example a larger sensor network, where boards can be connected to different networks around the world, but be monitored from the same dashboard.

---

## Congratulations

![Illustrated character hugging an Arduino Board](assets/endimg.png)

These are the few simple steps needed to create our very own IoT project. Having a project connected to the cloud opens up many possibilities, such as tracking data in real time, trigger remote devices and building wireless systems.

What will you create?


<a href="https://create.arduino.cc/iot/things" target="_blank">Start your IoT journey</a>

---

### More tutorials

You can find more tutorials in the [Arduino IoT Cloud documentation page](/cloud/iot-cloud/).
