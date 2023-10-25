---
title: "Getting Started"
description: 'The Arduino Cloud is an online platform that makes it easy for you to code, deploy and monitor IoT projects.'
tags:
  - Arduino Cloud, IoT Cloud
author: 'Karl Söderby'
---

The [Arduino Cloud](app.arduino.cc) is a platform for developing Arduino projects and connecting them to the world. It supports secure connections with boards via [Wi-Fi®](), [LoRa®](), [Ethernet]() and [Cellular (GSM/NB-IoT)]().

The Arduino Cloud platform includes:
- an **Integrated Development Environment (IDE)** for programming your boards,
- a **cloud backend service** for synchronizing data from Arduino boards, but also from [Python]() & [JavaScript]() clients,
- a **graphical tool (dashboard)** for controlling and monitoring your board (as well as an [mobile app]()).
- [REST API]() and [command line tools]() for larger scale automations. 

Very simply explained, with the Arduino Cloud you can:
1. Create a program for an Arduino based on a brilliant idea you just hatched.
2. Upload the program to your board and synchronize any data you want to (most commonly through Wi-Fi®).
3. Create a dashboard with a set of widgets to control and monitor your board. 

Once you have setup your project, this is how you could interact & monitor it. 

For example, turning ON / OFF a light connected to a device would work like this:

![Interacting with your device](assets/overview-interaction.png)

And if you want to read the value of a sensor connected to your device, it would work like this:

![Monitoring your device.](assets/overview-monitor.png)

Networking code and data synchronizing is **automatically done**, so just focus on the project, and let the Arduino Cloud handle the rest.

***This document will help you get familiar with the [Arduino Cloud]() service, and once you've got a good hang of it, you can explore the [rest of the documentation]().***

## Compatible Boards

***Throughout the documentation, we will often refer to a "board" as a "device". A board is your physical hardware or virtual setup (Python/JS), and a "device" is how it is configured in the cloud.***

Compatibility with the Arduino Cloud is divided into two categories: 
- **Cloud Editor Support** - you can program **any** official Arduino board in the cloud editor. The editor also supports a large amount of third party boards.
- **IoT Cloud Support** - board with a radio module (e.g. Wi-Fi®) are supported. ESP32 based boards are also supported. 

For more information and list of supported boards, see the links below:
- [Wi-Fi®]()
- [LoRaWAN®]()
- [Ethernet]()
- [Cellular]()

## Overview

![The Arduino Cloud home page.](assets/home.png)

Anything in the Arduino Cloud can be accessed via the left action bar. In the list below, some with links to a documentation pages.

- **[Sketches]()** - your sketches (programs) are stored here, divided into either a "normal" or "cloud" sketch. 
- **[Devices]()** - here you can configure your Arduino boards, ESP32 devices, manual devices (Python, JavaScript and more).
- **[Things]()** - a Thing is a project configuration, where you select device, create variables to synchronize, and enter credentials.
- **[Dashboards]()** - dashboards are used to monitor & control your board through widgets. There's also a [mobile version]() available.
- **[Triggers]()** - triggers can be used to send emails and push notifications based on a value change of a variable.
- **Resources** - helpful links and resources. You might have found this article here.
- **Courses** - tailored content for specific products and kits connected to the Arduino Cloud.
- **[Templates]()** - templates are ready-made project that will automatically configure your device, Thing, 
- **Integrations** - third party services that are integrated with the Arduino Cloud.

## Get Started with Arduino Cloud

Setting up a project in the Arduino Cloud is easy, and can be done through a few simple steps summarized in this section.

### 1. Create an Account

To use the Arduino Cloud, you will need an Arduino account, which you can register [here](https://login.arduino.cc/login).


By default, you will have a **free plan**, which can be upgraded to a number of affordable plans starting at 1.99$ a month.

***Read more about [Arduino Cloud plans](https://cloud.arduino.cc/plans)***

### 2. Configure a Device

First you will need to connect your board to your computer, and configure your device at [app.arduino.cc/devices](app.arduino.cc/devices).

![Devices in the Arduino Cloud.](assets/device.png)

The configurations varies between boards, but everything is covered in the installation wizard.

***Learn more in the documentation for [Arduino Cloud Devices]().***

### 3. Create a Thing

After configuring a device, we can create a Thing, which is the **virtual twin** of your board. Here we configure network details, select device we want to associate and create the variables that we want to synchronize.

![Things in the Arduino Cloud.](assets/thing.png)

Variables we create will be used in the sketch, and will keep synchronizing as long as the board is connected to the cloud. 

When working with your IoT projects, consider this the "main space" for configurations, as you can access your sketche from here as well. 

***Learn more in the documentation for [Arduino Cloud Things]().***

### 4. Write a Sketch

Once you have done the above configurations, you can move on to **create a program/sketch**. This is where *you* decide what you want to create, and what data you want sent to the cloud.

![A sketch in the Arduino Cloud.](assets/editor.png)

When your program is ready, upload it to your board. If your board supports [Over-the-air (OTA)]() uploads, you can from now on upload without your board being connected to your computer!

***Learn more in the documentation for [Arduino Cloud sketches]().***

### 5. Create a Dashboard

A dashboard allows you to interact with your device from a web interface or mobile app. A dashboard is composed of **widgets**, which you can link to a variable in your Thing.

![Dashboards in the Arduino Cloud.](assets/dashboard.png)

Choose from switches, sliders, RGB picker, message box,  gauges and much more to create dashboards. Dashboards are not linked to a specific Thing/device, meaning you can control many different boards from the same dashboard.

Some widgets can be linked to multiple variables, for example the [Advanced Chart]() widget can graph up to 4 variables from different boards simultaneously! 

***Learn more in the documentation for [Arduino Cloud dashboards]().***

### 6. Track Your Project

Once you done all configurations, created a program & dashboard, you can sit back and monitor & interact with your project from the web interface or the mobile app.

![Arduino Cloud Dashboard & IoT Remote App]()

## Guides

We recommend checking out the following guides to get started with various coding frameworks:
- [Arduino / C++ setup (default setup)]() - the default installation using the built-in code editor and an Arduino / ESP32 board.
- [Python setup]() - set up of a manual device to run on a PC / Linux system such as Raspberry Pi.
- [MicroPython setup]() - setup of MicroPython on a select number of supported boards.
- [JavaScript / node.js setup]() - setup of JavaScript using node.js, perfect for integrating your front-end projects with the Arduino Cloud.

## Features

Make sure to explore the various features of the Arduino Cloud through the links below:
- [**Data Monitoring**](/cloud/iot-cloud/tutorials/cloud-environmental-data) - learn how to easily monitor your Arduino's sensor values through a dashboard.
- [**Variable Synchronisation**](https://docs.arduino.cc/cloud/iot-cloud/tutorials/device-to-device) - variable synchronisation allows you to sync variables across devices, enabling communication between devices with minimal coding.
- [**Scheduler**](https://docs.arduino.cc/cloud/iot-cloud/tutorials/cloud-scheduler) - schedule jobs to go on/off for a specific amount of time (seconds, minutes, hours).
- [**Over-The-Air (OTA) Uploads**](/cloud/iot-cloud/tutorials/ota-getting-started) - upload code to devices not connected to your computer.
- [**Webhooks**](https://docs.arduino.cc/cloud/iot-cloud/tutorials/webhooks) - integrate your project with another service, such as IFTTT.
- [**Amazon Alexa Support**](/cloud/iot-cloud/tutorials/alexa-mkr-rgb-shield) - make your project voice controlled with the Amazon Alexa integration. 
- [**Dashboard Sharing**](https://docs.arduino.cc/cloud/iot-cloud/tutorials/sharing-dashboards) - share your data with other people around the world. 