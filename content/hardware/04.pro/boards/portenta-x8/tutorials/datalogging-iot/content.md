---
title: 'Datalogging with MQTT, Node-RED, InfluxDB, Grafana and the Portenta X8'
description: 'This tutorial will show you how to set up a local data logging server using an MQTT broker, Node-RED, InfluxDB, Grafana, and the Arduino® Portenta X8.'
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
- Wi-Fi Access Point (AP) with Internet access
- ADB or SSH 

***If you are new to the Portenta X8 board, check out this [getting started tutorial](/tutorials/portenta-x8/out-of-the-box#controlling-portenta-x8-through-the-terminal) on how to control your board using a terminal or command-line interface.***

## IoT Architecture 101

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



