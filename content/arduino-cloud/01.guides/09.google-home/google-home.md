---
title: 'Google Home™'
description: 'Learn how to connect the Arduino Cloud with Google Home™.'
tags:
- Google Home™
author: 'Hannes Siebeneicher'
featuredImage: 'cloud'
---

## Introduction

This tutorial guides you on how to connect the Arduino Cloud to your Google Home™ allowing you to interact with your devices, simply through your Google Home Assistant: use voice commands, the Google Home app, or create new routines integrating Arduino solutions.

It requires your board to be [compatible with the Arduino Cloud](https://docs.arduino.cc/arduino-cloud/hardware/devices/).

## Goals

The goals of this tutorial are:

- Create a Google Home compatible variable.
- Control the built-in LED with Google Home.

## Hardware & Software Needed

- [Arduino Cloud](https://cloud.arduino.cc/).
- [A Cloud compatible Arduino board](https://docs.arduino.cc/arduino-cloud/hardware/devices/).
- [Google Home™](https://home.google.com/welcome/).

To familiarize yourself with the Arduino Cloud check out our [getting started guide](https://docs.arduino.cc/arduino-cloud/guides/overview/).

## Cloud Setup

Before we start, make sure you have an Arduino Cloud compatible board.

Then, we need to configure a Thing in the [Arduino Cloud](https://app.arduino.cc/things) consisting of one CloudSwitch variables called `led`. Follow the instructions below to do so.

### Thing & Device Configuration

1. Create a new Thing, by clicking on the **"Create Thing"** button.
2. Click on the **"Select Device"** in the **"Associated Devices"** section of your Thing.
3. Click on **"Set Up New Device"**, and continue to set up your device.

If you need more information on how to set up your device check out our [getting started guide](https://docs.arduino.cc/arduino-cloud/guides/overview/#2-configure-a-device).

### Create Variables

The next step is to create a Cloud variable, which we will later interact with via our Google Home.

1. While in Thing configuration, click on **"Add Variable"** which will open a new window.
2. Name your variable `led`, select `Smart home`, and select it to be of a `Switch` type.
3. Click on **"Add Variable"** at the bottom of the window.
4. Make sure the **Smart Home Integration** is set to Google Home.

***Most Cloud variables are compatible with both Alexa and Google Home but there is an icon on the right side of the type that indicates the compatibility***

Your Thing should look something like this when you are finished:

![Finished Thing interface.](./assets/thing.png)

***Learn more about how variables work in the [Variables documentation](/arduino-cloud/cloud-interface/variables)***

#### Detect Your Device with Google Home

1. **Network Connection:** Ensure the board is connected to the network.
2. **Google Home App:** Open the app, navigate to Devices, and click "Add Device."
3. **Integration Method:** Select "Works with Google Home" and then choose the "Arduino" action.
4. **Device Pairing:** Link your Arduino account if requested and proceed to add your devices (one for each variable) by associating them with a room.

![Google Home Device Pairing](./assets/googleHome.png)

**Congratulations!** Your device is now successfully configured to work with Google Home.