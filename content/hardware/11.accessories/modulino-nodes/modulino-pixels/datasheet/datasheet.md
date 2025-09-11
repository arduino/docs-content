---
identifier: ABX00109
title: Arduino® Modulino® Pixels
type: maker
author: Pedro Sousa Lima
---

![](assets/featuredPix.png)

# Description
The Modulino® Pixels features **eight LC8822-2020 RGB LEDs** driven by an on-board **STM32C011F4** microcontroller. This setup enables simple I2C connectivity for controlling colorful visual effects, animations, or status indications in a wide variety of projects.

# Target Areas
Maker, beginner, education

# Contents
## Application Examples
- **Colorful Displays**
  Create dynamic LED patterns, color indicators, or simple pixel-art displays.

- **Notifications & Alerts**
  Represent sensor data or status updates (e.g., temperature ranges, motion detection) via color-coded lights.

- **Interactive Installations**
  Combine with other Modulino® nodes (e.g., Knob or Buttons) to build interactive lighting dashboards or IoT displays.

<div style="page-break-after: always;"></div>

## Features
- **Eight LC8822-2020 RGB LEDs** providing individually addressable full-color output.
- **STM32C011F4** microcontroller that manages LED control over I2C.
- **3.3 V** operation via the Qwiic interface; supports 2.0 V–3.6 V supply range on the MCU.
- **SWD** header for reprogramming and advanced control.
- Ideal for **lighting effects**, **progress bars**, or any **multi-color** output in maker projects.

### Contents
| **SKU**   | **Name**            | **Purpose**                                     | **Quantity** |
| --------- | ------------------- | ----------------------------------------------- | ------------ |
| ABX00109  | Modulino® Pixels    | 8× individually addressable RGB LEDs           | 1            |
|           | I2C Qwiic cable     | Compatible with the Qwiic standard             | 1            |


## Related Products
- **SKU: ASX00027** – [Arduino® Sensor Kit](https://store.arduino.cc/products/arduino-sensor-kit)  
- **SKU: K000007** – [Arduino® Starter Kit](https://store.arduino.cc/products/arduino-starter-kit-multi-language)  
- **SKU: AKX00026** – [Arduino® Oplà IoT Kit](https://store.arduino.cc/products/opla-iot-kit)

## Rating

### Recommended Operating Conditions
- **Microcontroller supply range:** 2.0 V – 3.6 V (STM32C011F4)
- **Powered at 3.3 V** through the Qwiic interface (in accordance with the Qwiic standard)
- **Operating temperature:** –40 °C to +85 °C

**Typical current consumption:**
- Up to **33 mA per RGB LED*** at full brightness ** 8 LEDs (264 mA total), plus ~3.4 mA for the microcontroller. Actual usage depends on brightness and color settings.

## Power Tree
The power tree for the Modulino® node can be consulted below:

![Modulino® Pixels Power Tree](assets/Modulino_Pixels_Power_Tree.png)

## Block Diagram
This module includes an STM32C011F4 microcontroller managing eight LC8822-2020 RGB LEDs. It communicates with the host via I2C by default but can be reprogrammed via SWD for custom functionality.

![Modulino® Pixels block diagram](assets/BlockDiagramPixels.png)

## Functional Overview
The Modulino® Pixels node uses the on-board **STM32C011F4** to handle LED data and provide an I2C interface. Each of the eight **LC8822-2020 RGB LEDs** can be addressed and controlled individually for color and brightness. Advanced users may reprogram the MCU (via SWD) to alter LED control logic or to interface via other protocols.

### Technical Specifications

| **Specification**       | **Details**                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| **Microcontroller**     | STM32C011F4 (handles I2C, LED driving logic)                                 |
| **LEDs**                | 8× LC8822-2020 RGB LEDs                                                      |
| **Supply Voltage**      | 3.3 V                                                                        |
| **Power Consumption**   | ~80 mA                                                                       |
| **Communication**       | I2C (Qwiic), SWD (debug/reprogram), optional UART/SPI if reprogrammed         |

### Pinout

**Qwiic / I2C (1×4 Header)**  
| **Pin** | **Function**               |
|---------|----------------------------|
| GND     | Ground                    |
| 3.3 V   | Power Supply (3.3 V)      |
| SDA     | I2C Data                  |
| SCL     | I2C Clock                 |

These pads and the Qwiic connectors share the same I2C bus at 3.3 V.

**Additional 1×10 Header (LED & MCU Signals)**
| **Pin** | **Function**      |
|---------|-------------------|
| GND    | Ground          |
| GND    | Ground          |
| 3V3    | 3.3 V Power      |
| RESET  | Reset           |
| SWCLK  | SWD Clock       |
| SWDIO  | SWD Data        |
| TX1    | USART Transmit  |
| RX1    | USART Receive   |
| D0     | Pixels Data Out |
| C0     | Pixels Clock Out|

![Pinout Overview](assets/PixelsPinouts.png)

The header can be used to add more LC8822-2020 RGB's LED in a daisy chain configuration.
Built-in LEDs open for extension

It also has other I2C interface controller IC pins usable for other purposes or for reprogramming it using its SWD interface. These provide a place to mount header pins if desired.

![LED extension](assets/LEDExtention.png)

### Power Specifications
- **Nominal operating voltage:** 3.3 V via Qwiic  
- **MCU voltage range:** 2.0 V–3.6 V  

### Mechanical Information
![Modulino® Pixels Mechanical Information](assets/PixelMec.png)

- Board dimensions: 41 mm × 25.36 mm  
- Thickness: 1.6 mm (±0.2 mm)  
- Four mounting holes (Ø 3.2 mm)  
  - Hole spacing: 16 mm vertically, 32 mm horizontally

### I2C Address Reference

| **Board Silk Name** | **Sensor/Actuator**      | **Modulino® I2C Address (HEX)** | **Editable Addresses (HEX)**             | **Hardware I2C Address (HEX)** |
|---------------------|--------------------------|--------------------------------|------------------------------------------|--------------------------------|
| MODULINO PIXELS     | 8× LC8822-2020 RGB LEDs  | 0x6C                           | Any custom address (via FW config)       | 0x36                           |

**Note:** Default address is **0x6C**. You can change it via the Modulino® library or custom firmware. A white rectangle on the board silk can be used to record a new address.
![Blank silk for identification](assets/I2CTag.png)

## Device Operation
By default, this node operates as an I2C target device on the Qwiic bus. The integrated microcontroller receives LED control commands and drives each of the eight LC8822-2020 RGB LEDs. For advanced usage, you may reprogram the microcontroller to add different communication protocols or custom LED driving modes.

Use any 3.3 V microcontroller or Arduino board. The official Modulino® libraries facilitate controlling the RGB LEDs with easy I2C commands to set colors, brightness, or special effects. Make sure your power supply can handle the current draw if driving all LEDs at full brightness.

# Certifications
## Certifications Summary

| **Certification** | **Status** |
|:-----------------:|:----------:|
|  CE/RED (Europe)  |     Yes    |
|     UKCA (UK)     |     Yes    |
|     FCC (USA)     |     Yes    |
|    IC (Canada)    |     Yes    |
|        RoHS       |     Yes    |
|       REACH       |     Yes    |
|        WEEE       |     Yes    |

## Declaration of Conformity CE DoC (EU)

<p style="text-align: justify;">We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).</p>

## Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

<p style="text-align: justify;">Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.</p>

| Substance                              | **Maximum limit (ppm)** |
|----------------------------------------|-------------------------|
| Lead (Pb)                              | 1000                    |
| Cadmium (Cd)                           | 100                     |
| Mercury (Hg)                           | 1000                    |
| Hexavalent Chromium (Cr6+)             | 1000                    |
| Poly Brominated Biphenyls (PBB)        | 1000                    |
| Poly Brominated Diphenyl ethers (PBDE) | 1000                    |
| Bis(2-Ethylhexyl) phthalate (DEHP)     | 1000                    |
| Benzyl butyl phthalate (BBP)           | 1000                    |
| Dibutyl phthalate (DBP)                | 1000                    |
| Diisobutyl phthalate (DIBP)            | 1000                    |

Exemptions: No exemptions are claimed.

<p style="text-align: justify;">Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.</p>

## FCC WARNING

This device complies with part 15 of the FCC Rules.

Operation is subject to the following two conditions: 

(1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

## IC Caution

This device complies with Industry Canada licence-exempt RSS standard(s). 

Operation is subject to the following two conditions: 

(1) This device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.

## Conflict Minerals Declaration

<p style="text-align: justify;">As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regard to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder or as a component in metal alloys. As part of our reasonable due diligence, Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.</p>

# Company Information

| Company name    | Arduino SRL                                   |
|-----------------|-----------------------------------------------|
| Company Address | Via Andrea Appiani, 25 - 20900 MONZA（Italy)  |

# Reference Documentation

| Ref                       | Link                                                                                                                                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arduino IDE (Desktop)     | [https://www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software)                                                                                                             |
| Arduino Courses           | [https://www.arduino.cc/education/courses](https://www.arduino.cc/education/courses)                                                                                                           |
| Arduino Documentation     | [https://docs.arduino.cc/](https://docs.arduino.cc/)                                                                                                           |
| Arduino IDE (Cloud)       | [https://create.arduino.cc/editor](https://create.arduino.cc/editor)                                                                                                                           |
| Cloud IDE Getting Started | [https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor](https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor) |
| Project Hub               | [https://projecthub.arduino.cc/](https://projecthub.arduino.cc/)                                                                                                                               |
| Library Reference         | [https://github.com/arduino-libraries/](https://github.com/arduino-libraries/)                                                                                                                 |
| Online Store              | [https://store.arduino.cc/](https://store.arduino.cc/)                                                                                                                      |

# Revision History
| **Date**   | **Revision** | **Changes**                                                          |
| ---------- | ------------ | -------------------------------------------------------------------- |
| 01/07/2025 | 4            | Certification                                                        |
| 17/06/2025 | 3            | Nomenclature updates                                                 |
| 23/05/2025 | 2            | Fixed pinout table and power info, removed unrelated characteristics |
| 14/05/2025 | 1            | First release                                                        |



