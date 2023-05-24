---
title: 'Smart Irrigation System Using Edge Control'
description: "This application note describes how to control a four zones irrigation system using the Edge Control and the Arduino IoT Cloud."
difficulty: intermediate
tags:
  - Irrigation System
  - Arduino Edge Control
  - MKR WiFi 1010
  - Motorized Valve
  - 4-20mA Sensors
  - Arduino IoT Cloud
  - Application Note
author: 'Christopher Mendez'
libraries:
  - name: Arduino_EdgeControl
    url: https://github.com/arduino-libraries/Arduino_EdgeControl
  - name: ArduinoHTTPClient
    url: https://github.com/arduino-libraries/ArduinoHttpClient
  - name: Arduino_JSON
    url: https://github.com/arduino-libraries/Arduino_JSON
  - name: Arduino_ConnectionsHandler
    url: https://github.com/arduino-libraries/Arduino_ConnectionHandler
  - name: ArduinoJson
    url: https://github.com/bblanchon/ArduinoJson
  - name: ArduinoIoTCloud
    url: https://github.com/arduino-libraries/ArduinoIoTCloud  
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
  - arduino-agent
hardware:
  - hardware/05.pro-solutions/boards/solutions-and-kits/edge-control
  - hardware/05.pro-solutions/boards/solutions-and-kits/enclosure-kit
  - hardware/01.mkr/01.boards/mkr-wifi-1010
---

## Introduction

The health of our crops depends on being able to provide favorable environmental conditions for their proper development. Among the most important factors is irrigation, water allows the assimilation and transport of nutrients in plants, among many other things vital to life.

![Thumbnail](assets/)

Smart farming is more accessible today than ever using the Arduino series of professional solutions. Taking advantage of the control capabilities and analysis of sensor variables, Arduino Edge Control is perfect for managing our crops.

## Goals

The goal of this application note is to showcase a smart farming irrigation system using a combination of an Arduino Edge Control, an MKR WiFi 1010, and the Arduino IoT Cloud. The project's objectives are the following:

- Independently control 4 irrigation zones using motorized ball valves.
- Get water from a smart tank with water level monitoring.
- Program irrigation timers from remote through Arduino IoT Cloud by using WiFi connectivity.
- Manually activate irrigation from Arduino IoT Cloud through dedicated widgets.
- Monitor average irrigation time and water consumption on dedicated charts on Arduino IoT Cloud.
- Provide a weather station on Arduino Cloud, using API connected to a weather website to decide on whether to irrigate or not.

## Hardware and Software Requirements

![Materials](assets/)

### Hardware Requirements
- Arduino Edge Control
- MKR WiFi 1010
- Arduino Edge Control Enclosure Kit
- 4-20mA Liquid Level Sensor
- 4x 2 Wires Motorized ball Valves
- 11' of 1/2" PVC pipes
- 3x 1/2" PVC TEE
- 8x 1/2" PVC elbow
- 1/2" Manual Valve
- 4x 1/2" PVC caps
- 11x 1/2" PVC male adapters
- 7x 1/2" wall pipe brackets
- 4x Rectangular planters
- DIN rail
- 6x Cable glands
- 20' Duplex cable AWG 18
- Electrical Register Box
- Water Tank

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor).
- If you are going to use an offline Arduino IDE, you must install the following libraries: `Arduino_EdgeControl`, `ArduinoIoTCloud`, `Arduino_JSON`, `ArduinoJson`, `ArduinoHttpClient` and `Arduino_ConnectionsHandler`. You can install them using the Arduino IDE Library Manager.
- The [smart irrigation system codes](assets/Edge-Control_MKR_Codes.zip).
- [Arduino Create Agent](https://create.arduino.cc/getting-started/plugin/welcome) to add the Portenta H7 to the IoT Cloud.

## Smart Irrigation System Setup

The electrical connections of the intended application are shown in the diagram below:

![Electrical connections of the irrigation system](assets/wiring-diagram.png)

The Arduino Edge Control board will be powered with an external 12V DC power supply connected to BATT+ and GND of J11 respectively.
The four motorized ball valves will be connected to the Arduino Edge Control Latching outputs of J9 connector from OUT0 to OUT3.
The water level transmitter will be connected to +19V reference and 4-20mA input 1 of J7 connector.


## Smart Irrigation System Overview

