---
title: 'LoRaWAN® Sensorized Farm Irrigation System Using Arduino® Edge Control'
description: "This application note describes how to control a four zones irrigation system using the Edge Control and the Arduino IoT Cloud with LoRaWAN® connectivity"
difficulty: intermediate
tags:
  - Irrigation System
  - Arduino Edge Control
  - Arduino MKR WAN 1310
  - Latching Valve
  - Arduino IoT Cloud
  - Application Note
  - WisGate Lite
author: 'Christopher Mendez'
libraries:
  - name: Arduino_EdgeControl
    url: https://github.com/arduino-libraries/Arduino_EdgeControl
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
  - arduino-agent
hardware:
  - hardware/05.pro-solutions/boards/solutions-and-kits/edge-control
  - hardware/05.pro-solutions/boards/solutions-and-kits/enclosure-kit
  - hardware/01.mkr/01.boards/mkr-wan-1310
---

## Introduction

We know that agricultural activities are normally carried out in remote environments, this makes access to electricity and connectivity a challenge. 

Smart farming techniques are being implemented more and more due to the importance of optimizing the use of resources. This includes the demand for more efficient, eco-friendly, and more profitable crops.

![Application Note Overview. Each pot represents one individual irrigation zone capable of watering a crop field](assets/Thumbnail-green.png)

Implementing traditional wired communication infrastructure in remote areas can be expensive and time-consuming. LoRaWAN, being a wireless technology, provides a cost-effective alternative as it requires minimal infrastructure setup, reducing installation and maintenance costs.

Arduino has you covered in these scenarios with its Pro solutions. With products designed to work in remote environments, supplying their power from renewable sources and providing long-distance connectivity and low power consumption.

The shown application note is intended to replicate a scaled smart farming application, that can be implemented on real agriculture fields using the same hardware and firmware.

## Goals

The goal of this application note is to showcase a sensorized farming irrigation system using a combination of an Edge Control, an MKR WAN 1310, and the Arduino IoT Cloud. The project's objectives are the following:

- Independently control four irrigation zones using latching valves.
- Leverage MKR WAN 1310 with LoRa and a Wisgate (Lite or PRO) to communicate with Arduino IoT Cloud.
- Monitor soil moisture and decide whether to irrigate based on it. 
- Display the soil humidity level on the Edge Control Enclosure kit LCD.
- Manually activate irrigation through Enclosure Kit built-in push button.
- Monitor average humidity level, irrigation time and water consumption on dedicated charts on Arduino IoT Cloud.
- Get water from a garden hose with a flow sensor able to evaluate the amount of consumed water.

## Hardware and Software Requirements

![Project main hardware and materials](assets/hardware_16-9.png)

### Hardware Requirements
- Arduino Edge Control
- Arduino MKR WAN 1310
- Arduino Edge Control Enclosure Kit
- Water flow sensor (YF-B2 15 mm)
- WATERMARK Soil Moisture Sensors.
- 2-Wires Solenoid Valves (x4)
- 12 VDC 5Ah acid/lead SLA battery (x1)
- 18 VDC 180 W solar panel.
- 3.4 meters of 15 mm PVC pipes (x1)
- 15 mm PVC TEE pipes (x3)
- 15 mm PVC elbow (x8)
- 15 mm Manual Valve (x1)
- 15 mm PVC caps (x4)
- 15 mm PVC male adapters (x11)
- 15 mm wall pipe brackets (x7)
- Rectangular planters (x4)
- DIN rail (x1)
- Cable glands (x6)
- 6 meters of duplex cable AWG 18 (x1)
- Electrical Register Box (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor).
- If you are going to use an offline Arduino IDE, you must install the following libraries: `Arduino_EdgeControl` and `ArduinoIoTCloud`. You can install them through the Arduino IDE Library Manager.
- The [Irrigation System Arduino Sketches](assets/Edge-Control_MKR_Codes.zip).
- [Arduino Create Agent](https://create.arduino.cc/getting-started/plugin/welcome) to provision the MKR WAN 1310 on the Arduino IoT Cloud.

## Sensorized Irrigation System Setup

The electrical connections of the intended application are shown in the diagram below:

[!]()

- The Edge Control board will be powered with a 12 VDC acid/lead SLA battery connected to BATT+ and GND of J11 respectively, the battery will be recharged with a 18 VDC 180W solar panel connected to SOLAR+ and GND on the same connector.

[!]()

- The four solenoid valves will be connected to the Edge Control Latching outputs of J9 connector from OUT0 to OUT6. 

[!]()

- The water flow sensor will be connected to .... of the XX connector.


## Sensorized Irrigation System Overview

### Valves Control

### Water Usage

### Weather Forecast Consideration

### Arduino Edge Control Code

### Arduino MKR WAN 1310 Code

### The Arduino IoT Cloud Dashboard

## Full Smart Irrigation System Example

### The Irrigation System Working

## Conclusion

### Next Steps