---
title: 'Data Logging with MQTT, Node-RED, InfluxDB and Grafana'
description: 'This tutorial will show you how to set up a local data logging application using an MQTT broker, Node-RED, InfluxDB, Grafana, and the Arduino® Portenta X8.'
difficulty: Intermediate
tags:
  - Docker
  - MQTT
  - Mosquitto
  - Node-RED
  - InfluxDB
  - Grafana
author: 'José Bagur, Taddy Chung'
software:
  - Terminal
  - Docker
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

This tutorial will set up a typical Internet of Things (IoT) application: an MQTT data logger. For this application, we are going to use what we call in the Arduino team the "IoT-Quartet," four common building blocks that are popular and regularly used in these types of applications:

- Mosquitto (MQTT broker) 
- Node-RED
- InfluxDB
- Grafana

These four blocks will be running locally on the Portenta X8 board. We will use sensor data gathered using an Arduino MKR WiFi 1010 board to test the data logging application.

## Goals

- Install, configure and run Mosquitto (MQTT broker) locally in the X8
- Install, configure and run Node-RED locally in the X8
- Install, configure and run InfluxDB locally in the X8
- Install, configure and run Grafana locally in the X8
- Send sensor data from an Arduino® MKR WiFi 1010 board to the data logging application running locally in the X8

## Required Hardware and Software

- [Arduino® Portenta X8](https://store.arduino.cc/products/portenta-x8)
- [Arduino® MKR WiFi 1010](https://store.arduino.cc/products/arduino-mkr-wifi-1010)
- USB-C cable (either USB-C to USB-A or USB-C to USB-C)
- 10KΩ potentiometer (x1)
- Breadboard and jumper cables
- Wi-Fi Access Point (AP) with Internet access
- ADB or SSH
- Command-line interface
- [Arduino IDE 2.0](https://www.arduino.cc/en/software)
  
***If you are new to the Portenta X8 board, check out this [getting started tutorial](/tutorials/portenta-x8/out-of-the-box#controlling-portenta-x8-through-the-terminal) on how to control your board using a terminal or command-line interface.***

## IoT Architecture 101

IoT applications and devices are everywhere nowadays, even in places we don't think about there being a device or application connected to the Internet. Rather than a single technology, **IoT is a concept** that refers to the connection of everyday devices, just like your watch, to the Internet and how that Internet connection creates more and different ways to interact with your device and your environment. Interactions between humans and devices or applications create **data** (lots) that must be communicated and processed. 

How can we plan, build and deploy IoT solutions? To answer that question, we must think about **IoT architecture**. Due to the different IoT devices and applications that exist and can exist, there is not just one unique architecture for IoT devices and applications. But, we can talk about a base architecture that can be considered as a starting point for every IoT project. This base architecture consists of **three essential layers**: **perception** (or devices), **network**, and **application**. Let's talk more about these layers:

- **Perception layer**: this is the sensor's layer, where data comes from. In this layer, data is gathered with one or more sensor nodes; actuators, that answer to data collected from sensor nodes, are also in this layer.
- **Network layer**: this is the layer where data from sensor nodes is recollected and then transmitted to back-end services, such as databases. 
- **Application layer**: this layer is what the device or application user sees and interacts with, for example, a dashboard. 

The three-layer IoT architecture can be a starting point for designing and implementing an IoT device or application. In this tutorial, we are going to take this base architecture and set up a data logging application, as shown in the image below:

![IoT application high-level architecture.](assets/x8-data-logging-img_01.png)

In the high-level architecture described in the image above, the perception layer consists of an MKR WiFi 1010 board; this board gathers information from a sensor. The network layer consists of the MQTT broker (Mosquitto), the data forwarder (Node-RED), and the database (InfluxDB). Finally, the application layer consists of a dashboard (Grafana) where information from the sensor node is shown.

Let's start by configuring the MQTT broker!

## Installing Mosquitto

### Testing Mosquitto

## Installing Node-RED

### Testing Node-RED

## Installing InfluxDB

### Testing InfluxDB

## Installing Grafana

### Testing Grafana

## Sending Sensor Data Using the MKR WiFi 1010

## Conclusion

### Next Steps



