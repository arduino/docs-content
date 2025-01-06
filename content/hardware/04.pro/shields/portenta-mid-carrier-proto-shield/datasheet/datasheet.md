---
identifier: ASX00072
title: Arduino® Portenta Mid Carrier Proto Shield
type: pro
variant: 'Datasheet'
author: Taddy Chung
---
![](assets/featured.png)

# Description
<p style="text-align: justify;">The Arduino Portenta Mid Carrier Proto Shield integrates Nicla, Modulino®, UNO Shield, and Portenta, allowing environmental monitoring, motion detection, machine vision, and air quality analysis capabilities. The Modulino® nodes deliver a versatile and user-friendly platform for IoT and electronics, designed to expand effortlessly with additional sensors and components. With easy connectivity using Qwiic cables, they support straightforward daisy-chaining via I2C, making them ideal for beginners and advanced users. Combined with the scalability of Portenta and the adaptability of the UNO Shield, the Portenta Mid Carrier Proto Shield provides a flexible solution for diverse prototyping needs, providing an accessible and powerful development experience.</p>

# Target Areas:

Industrial automation, building automation, smart cities

# CONTENTS

## Application Examples

The Arduino Portenta Mid Carrier Proto Shield, when combined with the Portenta, Nicla, Modulino®, or UNO Shield, provides a comprehensive solution for diverse applications across industries. Below are some examples demonstrating its potential:

- **Industrial automation:** The Portenta Mid Carrier Proto Shield enables advanced monitoring, control, and data processing, enhancing efficiency and reliability in industrial processes.
  - **Predictive maintenance prototyping:** Develop prototypes for industrial machinery using Nicla Vision for real-time equipment inspection and Nicla Sense ME and Sense Env for environmental monitoring. The Portenta H7 processes data, while Cloud integration enables predictive algorithms for proactive maintenance and reduced downtime.
  - **EV charging station prototyping:** Prototype EV charging stations with features like real-time data collection, anomaly detection, and power load management. Integrate Portenta H7 and Cloud connectivity for remote management and performance analytics.
  - **Remotely controlled machine prototyping:** Establish machine control networks with Portenta Mid Carrier and CAN communication. Enable real-time data exchange, remote monitoring, and control via the Cloud to optimize machine performance and reduce downtime.
  - **High-speed test rigs:** Build scalable test rigs for sensor calibration, load testing, and functional validation. Use the Portenta Mid Carrier Proto Shield for central control, environmental monitoring, anomaly detection, and real-time Cloud data transmission.

- **Building automation / Smart cities:** The Portenta Mid Carrier Proto Shield facilitates innovative solutions for environmental monitoring and security systems in smart environments.
  - **Environmental monitoring prototypes:** Use Nicla and Modulino® sensors with Portenta H7 to monitor air quality, noise, and other parameters in real time, supporting informed decision-making.
  - **Intruder detection prototypes:** Leverage Nicla Vision’s motion detection and face recognition for robust security monitoring. Integrate with Portenta H7 and the Arduino Pro 4G module for real-time alerts and remote monitoring.
  - **Asset tracking prototypes:** Create logistics solutions to monitor environmental conditions such as temperature and humidity during transit. Use 4G network and GNSS for seamless Cloud data transmission and analytics to ensure goods integrity.

The Arduino Portenta Mid Carrier Proto Shield provides a ready-to-use platform for developers, enabling rapid prototyping and scalability for production, with intuitive tools like Arduino IDE and seamless Cloud integration.


## Features
### General Specifications Overview

<p style="text-align: justify;">
The Portenta Mid Carrier Proto Shield is a versatile solution for prototyping and automation applications. It integrates seamlessly with Portenta, Nicla, Modulino®, and UNO Shield, offering advanced sensing, data processing, and connectivity support. With components like Nicla Vision for machine vision and Nicla Sense ME for environmental monitoring, it enables real-time analysis and Cloud integration, making it ideal for industrial automation, building automation, and smart city solutions.
</p>

The main features of the shield are detailed in the table shown below.

<div style="text-align:center;">

<table>
    <thead>
        <tr>
            <th width="30%" style="text-align: right;">Feature</th>
            <th style="text-align: left;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top; text-align: right;">Compatible Modules</td>
            <td style="text-align: left;">
                <ul>
                    <li>Nicla sensorized nodes</li>
                    <li>Modulino®</li>
                    <li>Arduino® UNO Shields</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Connectors</td>
            <td style="text-align: left;">
                <ul>
                    <li>2x ESLOV connectors (I2C bus)</li>
                    <li>1x QWIIC connector</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Arduino UNO Shields Headers Interfaces</td>
            <td style="text-align: left;">
                <ul>
                    <li>ADC</li>
                    <li>GPIO</li>
                    <li>SPI</li>
                    <li>I2C</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Operating Temperatures</td>
            <td style="text-align: left;">-40° C to +85° C (-40° F to 185° F)</td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Dimensions</td>
            <td style="text-align: left;">61.3 mm x 86.5 mm</td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Power</td>
            <td style="text-align: left;">7-30 VDC via dedicated power jack</td>
        </tr>
    </tbody>
</table>
</div>

<div style="page-break-after: always;"></div>

### Communication Interfaces

The communication interfaces and other important features of the shield are detailed in the table shown below.

<div style="text-align:center;">

<table>
    <thead>
        <tr>
            <th width="30%" style="text-align: right;">Interface</th>
            <th style="text-align: left;">Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top; text-align: right;">Portenta Mid Carrier Headers</td>
            <td style="text-align: left;">
                <ul>
                    <li>2x 44-pin female headers</li>
                    <li>Provides high-density connectivity with Portenta family board</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Modulino® Mounting Holes</td>
            <td style="text-align: left;">
                <ul>
                    <li>Supports modular sensor and component connections</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Arduino UNO Shield Headers</td>
            <td style="text-align: left;">
                <ul>
                    <li>ADC, GPIO, SPI, I2C</li>
                    <li>Expands functionality with standard Arduino UNO Shields</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">QWIIC Connector</td>
            <td style="text-align: left;">
                <ul>
                    <li>1x QWIIC (I2C)</li>
                    <li>Enables quick and simple sensor integration with daisy-chain capabilities</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">ESLOV Connector</td>
            <td style="text-align: left;">
                <ul>
                    <li>2x ESLOV (I2C)</li>
                    <li>Supports scalable module integration and communication</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Nicla Mechanical Interface</td>
            <td style="text-align: left;">
                <ul>
                    <li>Dedicated connectors for Nicla modules</li>
                    <li>Enables advanced sensing and processing with Nicla family board</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

### Related Accessories

- ESLOV cable
- Qwiic cable

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<strong>Note:</strong> The Portenta Mid Carrier Proto Shield requires the Portenta Mid Carrier with a a compatible Portenta family board to operate.
</div>

### Related Products

- Arduino® Portenta Mid Carrier (ASX00055)
- Arduino® Nicla Voice (ABX00061)
- Arduino® Nicla Vision (ABX00051)
- Arduino® Nicla Sense ME (ABX00050)
- Arduino® 4 Relays Shield (A000110)
- Arduino® 9 Axis Motion Shield (A000070)
- Arduino® Ethernet Shield Rev 2 (A000024)
- Arduino® Motor Shield Rev 3 (A000079)

## Ratings

### Recommended Operating Conditions

<p style="text-align: justify;">
The table below provides a comprehensive guideline for the optimal use of the Portenta Mid Carrier Proto Shield, outlining typical operating conditions and design limits. The operating conditions of the Portenta Mid Carrier Proto Shield are largely based on the specifications of its components.
</p>

<div style="text-align:center;">

|            **Parameter**             |    **Symbol**    | **Min** | **Typ** | **Max** | **Unit** |
|:------------------------------------:|:----------------:|:-------:|:-------:|:-------:|:--------:|
| Power Jack Input Voltage<sup>1</sup> | V<sub>JACK</sub> |   7.0   |    -    |  30.0   |    V     |
|        Operating Temperature         |  T<sub>OP</sub>  |   -40   |    -    |   85    |    °C    |

</div>

<sup>1</sup> The Portenta Mid Carrier Proto Shield is powered via the power barrel jack (J5), supporting an input voltage range of 7.0 to 30.0 VDC.

## Functional Overview

<p style="text-align: justify;">
The Portenta Mid Carrier Proto Shield is designed for modular integration and advanced prototyping within the Arduino ecosystem. It features dual 44-pin Portenta Mid Carrier headers, offering high-density connectivity for advanced applications and integration with the Portenta ecosystem. It has two ESLOV connectors and one QWIIC connector for I2C communication, ensuring uninterrupted connectivity with sensors and peripherals.

The shield also features Arduino UNO headers that provide ADC, GPIO, SPI, and I2C interfaces compatible with standard Arduino shields. Dedicated mechanical interfaces for Nicla and Modulino® modules enable specialized sensing and data acquisition. These features make the Portenta Mid Carrier Proto Shield a robust, functional, and scalable platform for project development.
</p>

### Pinout

The Portenta Mid Carrier Proto Shield connectors pinout is shown in the figure below.

![](assets/Mid-Carrier-Proto-Shield-Pinout.png)

<div style="page-break-after: always;"></div>

### Block Diagram

An overview of the high-level architecture of the Portenta Mid Carrier Proto Shield is illustrated in the figure below.

![](assets/Proto_Shield_Env_Block_Diagram.png)

<div style="page-break-after: always;"></div>

### Shield Topology

| **Ref.** | **Description**                                                           | **Ref.** | **Description**                                                                                                      |
|----------|---------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------|
| J1, J4   | ESLOV SM05B-SRSS-TB(LF)(SN) SMD JST Connector, 5 Position, 1.0 mm Pitch   | J2       | QWIIC SM04B-SRSS-TB(LF)(SN) JST Connector, 4 Position, Side Entry, 1.0 mm Pitch                                      |
| J3       | PH2-06-UA Through-Hole Header, 6 Position, 2.54 mm (0.100") Pitch         | J5       | 19TW-746 Power Jack Connector, 2.1 x 5.5 mm, DC 30 V 0.5 A                                                           |
| J6       | 10166143-00024C1LF SMD Header Connector, 24 Position, 2x12, 1.27 mm Pitch | J14, J15 | Portenta Mid Carrier Interface X6521FV-2x22-C85D32 Through-Hole Vertical Female Header, 2x22 Position, 2.54 mm Pitch |
| JANALOG  | UNO Shield 20TW-995 Connector Strip, Female, Single Pin, 14V Rated        | JDIGITAL | UNO Shield 20TW-994 Connector Strip, Female, Single Pin, 18V Rated                                                   |

### Power Supply

<div style="text-align:justify;">

The Portenta Mid Carrier Proto Shield requires external power through the onboard power barrel jack:

- **Power Barrel Jack (J5):** Accepts an external power supply with an input voltage range of 7.0 to 30.0 VDC.

The figure below provides a detailed overview of the power option and the main system power architecture of the Portenta Mid Carrier Proto Shield.

![](assets/Proto_Shield_Env_Power_Tree.png)

<div style="page-break-after: always;"></div>

## Device Operation

<div style="text-align:justify;">

### Getting Started - IDE

To program your Portenta Mid Carrier Proto Shield offline with a Portenta family board, install the Arduino Desktop IDE **[1]**. You will need a compatible USB cable to connect the Portenta board to your computer.

### Getting Started - Arduino Web Editor

All Arduino devices work out of the box on the Arduino Cloud Editor **[2]** by installing a simple plugin. The Arduino Cloud Editor is hosted online. Therefore, it will always be up-to-date with all the latest features and support for all boards and devices. Follow **[3]** to start coding on the browser and upload your sketches onto your device.

### Getting Started - Arduino Cloud

All Arduino IoT-enabled products are supported on Arduino Cloud, which allows you to log, graph, and analyze sensor data, trigger events, and automate your home or business. Refer to the official documentation for more details.

### Sample Sketches

Sample sketches for the Portenta Mid Carrier Proto Shield are available in the **Examples** menu in the Arduino IDE or the **Portenta Mid Carrier Proto Shield Documentation** section of Arduino documentation **[4]**.

### Online Resources

Now that you have gone through the basics of what you can do with the device, you can explore the endless possibilities it provides by checking exciting projects on Arduino Project Hub **[5]**, the Arduino Library Reference **[6]**, and the online store **[7]** where you will be able to complement your Portenta Mid Carrier Proto Shield board with additional extensions, sensors, and actuators.
</div>

<div style="page-break-after: always;"></div>

## Mechanical Information

<p style="text-align: justify;">
The Portenta Mid Carrier Proto Shield is a double-sided board measuring 61.28 mm x 86.5 mm. It includes two ESLOV connectors, one QWIIC connector, a Modulino®, a Nicla mechanical interface, an Arduino UNO Shield interface, and a Portenta Mid Carrier interface with two 44-pin female headers.
</p>

### Shield Dimensions

The outline of the Portenta Mid Carrier Proto Shield is shown in the figure below, with all dimensions provided in millimeters (mm).

![](assets/Proto_Shield_Outline_top.png)

<p style="text-align: justify;">
The shield includes mounting holes for the Modulino®.
</p>

<div style="page-break-after: always;"></div>

### Shield Connectors

<p style="text-align: justify;">
The connectors of the Portenta Mid Carrier Proto Shield are mainly found along its edges, with additional connectors positioned within the shield’s interior. Their placement is illustrated in the figures below, with all dimensions provided in millimeters (mm).
</p>

![](assets/Proto_Shield_Connectors_top.png)

![](assets/Proto_Shield_Connectors_side.png)

![](assets/Proto_Shield_Connectors_bottom.png)

<div style="page-break-after: always;"></div>

## Product Compliance

### Declaration of Conformity CE DoC (EU)

<p style="text-align: justify;">
We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).
</p>

### Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

<p style="text-align: justify;">
Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.
</p>

| **Substance**                          | **Maximum Limit (ppm)** |
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

<div style="page-break-after: always;"></div>

Exemptions: No exemptions are claimed.

<p style="text-align: justify;">
Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.
</p>

### Conflict Minerals Declaration

<p style="text-align: justify;">
As a global supplier of electronic and electrical components, Arduino is aware of our obligations concerning laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence, Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.
</p>

## Company Information

| **Company Information** | **Details**                                |
|-------------------------|--------------------------------------------|
| **Company Name**        | Arduino S.r.l.                             |
| **Company Address**     | Via Andrea Appiani, 25-20900 Monza (Italy) |

## Reference Documentation

| **No.** | **Reference**                                   | **Link**                                                            |
|:-------:|-------------------------------------------------|---------------------------------------------------------------------|
|    1    | Arduino IDE (Desktop)                           | https://www.arduino.cc/en/Main/Software                             |
|    2    | Arduino IDE (Cloud)                             | https://create.arduino.cc/editor                                    |
|    3    | Arduino Cloud - Getting Started                 | https://docs.arduino.cc/arduino-cloud/guides/overview/              |
|    4    | Portenta Mid Carrier Proto Shield Documentation | https://docs.arduino.cc/hardware/portenta-mid-carrier-proto-shield/ |
|    5    | Project Hub                                     | https://create.arduino.cc/projecthub                                |
|    6    | Library Reference                               | https://www.arduino.cc/reference/en/                                |
|    7    | Online Store                                    | https://store.arduino.cc/                                           |

## Document Revision History

|  **Date**  | **Revision** |     **Changes**     |
|:----------:|:------------:|:-------------------:|
| 07/01/2025 |       1      |    First release    |