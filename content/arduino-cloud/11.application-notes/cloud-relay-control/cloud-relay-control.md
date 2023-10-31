---
title: 'Controlling relays from the Arduino IoT Cloud'
compatible-products: [mkr-wifi-1010, mkr-proto-relay-shield]
difficulty: beginner
description: 'Learn how to control the relays onboard the MKR Relay Shield through the Arduino IoT Cloud dashboard.'
tags:
  - Relays
author: 'Karl Söderby'
---

## Introduction

In this tutorial, we will go through how to control a MKR WiFi 1010 + a MKR Relay shield from the [Arduino IoT Cloud](https://create.arduino.cc/iot/things). We will create a simple configuration that allows us activate each of the relays on the shield through a dashboard in the cloud.

## Goals

The goals of this project are:

- Set up the Arduino IoT Cloud.
- Create a program that controls the relays.
- Create a dashboard to remotely control the relays.
- Use the Arduino IoT Cloud Remote app to control relays.

## Hardware & Software needed

- [Arduino IoT Cloud](https://create.arduino.cc/iot/)
- [Arduino MKR WiFi 1010](https://store.arduino.cc/mkr-wifi-1010)
- [Arduino MKR Relay Shield](https://store.arduino.cc/arduino-mkr-relay-proto-shield)
- Arduino IoT Cloud Remote app (optional). 
  - [Play Store](https://play.google.com/store/apps/details?id=cc.arduino.cloudiot&hl=en&gl=US)
  - [Apple Store](https://apps.apple.com/us/app/arduino-iot-cloud-remote/id1514358431)

## Circuit

![Mount the board on top of the shield.](assets/cloud-relay-control-circuit.png)

## Overview

In this guide we will:
- Configure a manual device in the Arduino Cloud,
- install the Arduino IoT Cloud Python library,
- write a Python script that connects to the Arduino Cloud. 

## Requirements

To follow this guide, make sure to have:

- An [Arduino account](https://login.arduino.cc/login),
- a version of [Python](https://www.python.org/downloads/) installed,
- [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) package manager installed,
- [Arduino IoT Python Client](https://pypi.org/project/arduino-iot-client/) installed.
- A code editor (we recommend [VSCode](https://code.visualstudio.com/) with the Python extension installed).

***The experience with Python and the `pip` package mangager varies depending on your computer and operating system. Python needs to be in your PATH to use the Arduino IoT Cloud Python client.***

## Cloud Setup

To set up the Arduino Cloud, follow the steps below. In there, we will
- create and configure a device,
- create a Thing,
- create cloud variables.


### Device Configuration

To configure a device, navigate to the [app.arduino.cc/devices](app.arduino.cc/devices) and click on the **"create a new device"** button. Connect your board to your computer, and make sure you have the [Create Agent](https://create.arduino.cc/getting-started/plugin/welcome) installed. Your board will appear, and the installation takes a couple of minutes.

***Learn more about Devices in the [Devices documentation]().***

### Thing Configuration

1. Create a new Thing, by clicking on the **"Create Thing"** button.
2. Click on the **"Select Device"** in the **"Associated Devices"** section of your Thing. Your previously configured device will appear from the list.
3. In the network section, enter your network credentials.

***Learn more about Things in the [Things documentation]().***

### Create Variables

Next step is to create some cloud variables, which we will later sync with our Arduino MKR WiFi 1010 board.

While in Thing configuration, click on **"Add Variable"** which will open a new window. Add the following variables with the specified configurations:

| Variable Name | Data Type | Permission   |
| ------------- | --------- | ------------ |
| `relay_1`     | Boolean   | Read & Write |
| `relay_2`     | Boolean   | Read & Write |

Your Thing interface should now look something like this:

![]()

***Need help understanding cloud variables? Check out the [Variables]() section.***

### Create Sketch

After your device & Thing is configured, you can program your board. Navigate to the **"Sketch"** tab inside your Thing, where you can compile & upload your programs. You will find the sketch for this application in the code snippet below:

```arduino

```

Upload this sketch to your board, and your board will start attempting to connect to the Arduino Cloud and sync its data.

You can verify that your device is connecting properly, by checking the Serial Monitor just after connection. Error codes are printed here.

### Create a Dashboard

Once you have your device running a sketch and syncing with the Arduino Cloud, you can create a **dashboard**, a visualization tool for monitoring & interacting with your board.

Navigate to [app.arduino.cc/dashboard](app.arduino.cc/dashboard) and create a dashboard. Add two switches (or any other preferred widgets), and link them to each `relay_x` variable that we created earlier. These switches will be directly linked with your Arduino MKR WiFi 1010's variables, and will turn ON/OFF the relays on your board.

You can also access your dashboard via the [Arduino IoT Remote app]().

![Interact with your board]()

***For more information on dashboards, available widgets and how to link them to your sketch, visit the [Dashboard & Widgets]() section.***

## Step 3: Connecting a component with higher voltage

>**Note:** Working with higher voltage components should be done with extreme caution. Do not alter the circuit while it is connected to a higher power source, and do not connect any high voltage components directly to the Arduino. 

Up until now, we have simply activated the relays, but we still haven't connected anything to them. While we are not going to go in-depth on how to connect high power components, we can take a look at how we could connect something that operates on maximum 24V.

Let's begin with the high power pins on the MKR Relay Shield. There are **six in total** for both relays, where there are three different type of connections: NO, COM and NC. 

![MKR Relay Shield's high power pins.](assets/MKRRELAY_T1_IMG06.png)

In this scenario, we are going to use the **NC** configuration, which means that writing a **LOW** signal to the relay will connect the NC pin to COM, which provides power to the component connected. The circuit for this could look like this:

![A circuit involving a 24V component.](assets/cloud-relay-control-img11.png)

In this circuit, we are using a 24V power supply and a 24V heater. To control them, we need to use the following commands:

To activate the relays:

```
digitalWrite(relay_1, LOW)
```

To de-activate the relays:

```
digitalWrite(relay_1, HIGH)
```

>**Note:** Use extreme caution when creating higher power circuits. Make sure that both the power supply and the component does not exceed 24V. For example, connecting it straight to a wall socket without a power converter would supply 220-240V, which is **10 times as high.**

## Conclusion

In this tutorial, we have gone through the necessary steps to connect a MKR WiFi 1010 + a MKR Relay Shield to the Arduino IoT Cloud. The relays can now be used to trigger higher voltage components, such as smaller heaters, fans or light bulbs. 

### More tutorials

You can find more tutorials in the [Arduino IoT Cloud documentation page](/arduino-cloud/).