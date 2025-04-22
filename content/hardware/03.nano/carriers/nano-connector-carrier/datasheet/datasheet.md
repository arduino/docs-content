---
identifier: ASX00061
title: Nano Connector Carrier
type: maker
variant: 'Datasheet'
author: Christopher Méndez
---

![](assets/nano_connector_top.png)

# Description

The Nano Connector Carrier is a practical solution for expanding the capabilities of our Nano product family, this carrier brings plug-and-play compatibility with Qwiic and Grove modules, making rapid prototyping easier than ever.

Whether you're diving into MicroPython, Matter, building with Modulinos, or developing AI-powered applications, this carrier provides a simple platform to bring your ideas to life.

The onboard microSD card slot unlocks new possibilities for data logging, edge AI, and real-time storage needs.

# Target Areas:

Industrial Automation, Rapid Prototyping, Proof of Concept, Edge AI

# CONTENTS

## Application Examples

**Industrial Automation:** 
- **Data Logging:** Data Logger as a compact, all-in-one device for efficient data collection and storage, ideal for IoT and sensor-based applications. With Nano boards advanced features and a compact design, it simplifies sensor interfacing, data management, and storage, making it perfect for smart homes, industrial monitoring, and research projects.
- **Predictive Maintenance:** Leverage the powerful features of the Nano Connector Carrier to develop a robust predictive maintenance prototype for industrial machinery. Utilize Modulino to monitor key operational parameters and detect anomalies or early signs of wear, enabling proactive maintenance and reducing downtime. Enhance this system with the Nano 33 BLE Sense, which continuously gathers crucial environmental data—including temperature, humidity, and vibrations—to assess the overall health of the machinery.
- **Proof of Concept:** Expand your Nano boards capabilities with Nano Connector Carrier. The Nano Connector Carrier is ready to be used with a wide range of external hardware components or modules, covering all your needs, from embedded sensing to actuation.

**Prototyping:**
- **Compact Device:** Effortlessly integrate the Connector Carrier into your interactive prototype, whether NANO bard is based on. Its plug and play sensors and actuators make development seamless. Whether you're using modules from our Qwiic or Grove series, its compact design allows you to experiment in small spaces, making it a perfect platform for testing and validating your tech ideas.
- **Smart Home:** Easily prototype any smart device that can monitor and adjust temperature, humidity, or occupancy levels by combining Nano Connector Carrier, Modulinos and Nano Matter. Integrate with Matter-compatible smart home systems like Alexa or Google Home for frictionless voice control and automation.
- **Controller:** By using the Nano Connector Carrier, you can easily prototype versatile RC - MIDI - RF - BLE - HID - DMX controller for your any projects. With plug-and-play support for sensors and actuators, you can create custom interfaces that respond to touch, motion, or even pressure. Whether you're using Modulinos or 3rd party sensors, the compact design and battery compatibility allow for a fully portable setup.

**Education:**
- **Micropython Learning:** Easily dive into MicroPython with the Nano Connector Carrier, Modulinos and Nano ESP32 as your learning platform. Its plug-and-play support for sensors and actuators allows you to experiment with real-world applications right away—whether you're reading sensor data, controlling LEDs, or building interactive projects. 
- **Cross-Disciplinary Student Projects:** The Connector Carrier accelerates interdisciplinary collaboration by enabling rapid prototyping in both classroom and lab environments. Its compact, modular design allows students across various fields—including engineering, computer science and arts, to quickly develop, test, and refine ideas using Arduino Nano boards. With built-in connectivity and expansion options, students can seamlessly integrate sensors, actuators, and communication modules, fostering hands-on experimentation and innovation. 
- **Sustainability and Green Tech:** Energy Management project where students can design and test systems that monitor or reduce energy use in buildings or devices, promoting sustainability and teaching about renewable energy or energy efficiency, within integrated solar or wind power systems.

## Features
### General Specifications Overview

The main features of the Nano Connector Carrier are detailed in the table shown below.

| **Feature**            | **Description**                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Interfaces             | 2x Grove analog/digital connector <br></br> 1x Grove I2C connector <br></br> 1x Grove UART connector <br></br> 1x Qwiic I2C connector <br></br> 1x microSD card reader |
| I/O Voltage            | Switch between 3.3 V and 5 V                                                                                                                                           |
| Dimensions             | 28 mm x 43 mm                                                                                                                                                          |
| Operating Temperatures | -40 °C to +85 °C                                                                                                                                                       |


### Board Selection

The Nano Connector Carrier lets you select between 5 V or 3.3 V Nano boards to ensure compatibility with the whole Nano family. For this, toggle the carrier onboard switch to its respective position following the table below.

| **3V3**                | **5V**       |
| ---------------------- | ------------ |
| Nano ESP32             | Arduino Nano |
| Nano 33 IoT            | Nano Every   |
| Nano 33 BLE            | Nano R4      |
| Nano 33 BLE Sense      |              |
| Nano 33 BLE Sense Rev2 |              |
| Nano RP2040 Connect    |              |
| Nano Matter            |              |

![Board Selector Switch](assets/board-selector.png)

Setting the switch to a certain position (3V3 or 5V) also manages the voltage output on the Grove connector VCC pin.

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<strong>Note:</strong> The logic and power voltage of the Qwiic connector and the microSD card slot is always 3.3 V regardless of the board selector switch position.
</div>

### Qwiic I2C Connector

The Qwiic connector is connected to the standard I2C bus on the board (A4, A5). This connector is powered via 3.3 V following the Qwiic standard system and making the Nano Connector Carrier compatible with the Arduino Modulino nodes.

Its logic level is fixed to 3.3 V, and it is translated to the host Nano board voltage defined by the board selector switch.

![Arduino Nano R4 Qwiic Connector](assets/Nano_R4-Qwiic-connector.png)

### Grove Connectors

The Nano Connector Carrier features 4x Grove connectors that expose the host board main communication interfaces.


### Micro SD Card 

### Communication Interfaces

The Nano Connector Carrier exposes all the Nano host board connections and communication interfaces through the header pins and connectors.  

| Interfaces     | Connector                                                                     |
| -------------- | ----------------------------------------------------------------------------- |
| UART (x1)      | - Grove connector                                                             |
| SPI (x1)       | - Nano header connector <br></br>- Micro SD card slot                         |
| I2C (x1)       | - Nano header connector <br></br>- Qwiic connector <br></br>- Grove connector |
| Analog/Digital | - Nano header connector <br></br>- 2x Grove connectors                        |

### Related Products