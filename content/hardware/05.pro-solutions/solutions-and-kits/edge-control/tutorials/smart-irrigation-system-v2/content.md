---
title: 'LoRaWAN® Sensorized Farm Irrigation System Using Arduino® Edge Control'
description: "This application note describes how to control a four zones irrigation system using the Edge Control and the Arduino IoT Cloud with LoRaWAN® connectivity"
difficulty: intermediate
tags:
  - Irrigation System
  - Arduino Edge Control
  - Arduino MKR WAN 1310
  - Solenoid Valve
  - Arduino IoT Cloud
  - Application Note
  - WisGate Lite
  - LoRaWAN®
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
- Water flow sensor (YF-B2 DN15)
- WATERMARK Soil Moisture Sensors.
- 2-Wires Irrigation Solenoid Valves (x4)
- 12 VDC 5Ah acid/lead SLA battery (x1)
- 18 VDC 180 W solar panel.
- 3.4 meters of DN15 PVC pipes (x1)
- DN15 PVC TEE pipes (x3)
- DN15 PVC elbow (x8)
- DN15 Manual Valve (x1)
- DN15 PVC caps (x4)
- DN15 PVC male adapters (x11)
- DN15 wall pipe brackets (x7)
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

## Irrigation System Setup

The electrical connections of the intended application are shown in the diagram below:

![Electrical diagram of the irrigation system](assets/EDGE_CONTROL_DIAGRAM.png)

- The Edge Control board will be powered with a 12 VDC acid/lead SLA battery connected to BATT+ and GND of J11 respectively, the battery will be recharged with an 18 VDC 180W solar panel connected to SOLAR+ and GND on the same connector.

![Power connection diagram](assets/POWER_CONNECTIONS.png)

- The four solenoid valves will be connected to the Edge Control relay contacts of J11 connector following the wiring below. 

![Solenoid valves connection diagram](assets/VALVES_CONNECTIONS.png)

- The water flow sensor will be connected to a +12 VDC output, GND and the signal wire to the IRQ_C_CH_1, of the J3 connector, and the four watermark sensors will be connected to a terminal block rail, one terminal to the common and the others to the watermark sensor inputs from 1 to 4 respectively on J8.

![Watermark and water flow sensors connection diagram](assets/SENSORS_CONNECTIONS.png)

## Irrigation System Overview

The irrigation system works as a whole: it integrates the water flow measurement and the activation of the valves, done by the Edge Control, with the Cloud communication, using the MKR WAN 1310.

The Edge Control is responsible for:

- Measuring the water usage with a water flow sensor.
- Measuring the soil humidity level using watermark sensors.
- Controlling an LCD screen where different system variables will be shown, including soil humidity.
- Deciding whether to irrigate based on local humidity.

The MKR WAN 1310 is responsible for:

- Providing Cloud connectivity using LoRaWAN.
- Reporting the values of the Edge Control sensors on the cloud. 

The communication between both devices is done leveraging the I2C communication protocol.

### Valves Control

The valves can be controlled manually by using the onboard button, one tap opens the valve one, two taps valve two, and so on. Also, the valves can be controlled automatically by the system when the soil moisture is poor. The working time of the valves is monitored and reported on the cloud to enable an efficient visualization of the average daily use.

### Water Usage

The water flow sensor will measure the water used and will calculate its volume in liters. This information will be monitored through the cloud and the integrated LCD.

### Soil moisture measurement

Instead of measuring the percentage of water by volume in a given amount of soil, we will be using watermark sensors that are capable of measuring the physical force holding water in the soil, this is correlated with how difficult it is for the plants to extract water from the soil. 

This measurement is done in Centibars, and we can use the following readings as a general guideline:

- **0-10 Centibars** = Saturated soil
- **10-30 Centibars** = Soil is adequately wet (except coarse sands, which are drying)
- **30-60 Centibars** = Usual range for irrigation (most soils)
- **60-100 Centibars** = Usual range for irrigation in heavy clay
- **100-200 Centibars** = Soil is becoming dangerously dry- proceed with caution!

### Arduino Edge Control Code

```arduino
```

### Arduino MKR WAN 1310 Code

```arduino
```

### The Arduino IoT Cloud Dashboard

## Full Smart Irrigation System Example

### The Irrigation System Working

## Conclusion

### Next Steps