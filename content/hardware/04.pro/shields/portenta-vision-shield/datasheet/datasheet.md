---
identifier: ASX00021-ASX00026
title: Arduino® Portenta Vision Shield Rev 2
type: pro
variant: 'Collective Datasheet'
---

![](assets/featured.jpg)

# Description

<p style="text-align: justify;">Enhance your industrial automation and surveillance projects with the Arduino Portenta Vision Shield. This add-on board integrates with the Portenta family, offering advanced machine vision capabilities and extended connectivity. The Portenta Vision Shield's compact design and High-Fensity connector ensure a quick and efficient setup. It transforms your Portenta family board into a powerful tool for real-time image processing and edge computing, suitable for demanding industrial environments.</p>

# Target Areas
Industrial automation, surveillance, machine vision, edge computing

# CONTENTS
## Application Examples

<div style="text-align:justify;">
The Portenta Vision Shield is an add-on and a gateway to innovative solutions in various industries. Explore the possibilities of integrating advanced machine vision and edge computing into your projects with the following application examples:

- **Industrial automation**: Elevate your automation systems with the Portenta Vision Shield, enabling precise and real-time image processing for:
  - **Quality control**: Implement the Portenta Vision Shield in production lines to automatically detect product defects and ensure that only high-quality items pass through.
  - **Predictive maintenance**: Use machine vision to monitor equipment and identify early signs of wear or failure, reducing downtime and maintenance costs.
  - **Automated sorting**: Integrate the Portenta Vision Shield into conveyor systems to automatically sort items based on color, shape, or size, improving efficiency and accuracy.

- **Surveillance**: Enhance security and monitoring systems with advanced visual capabilities provided by the Portenta Vision Shield for:
  - **Real-time threat detection**: Deploy the Portenta Vision Shield in security systems to identify and alert authorities of potential threats, such as unauthorized access or suspicious activities, in real-time.
  - **Environmental monitoring**: Utilize the Portenta Vision Shield's imaging capabilities to monitor environmental conditions in critical areas, such as chemical plants, to ensure safety and compliance with regulations.
  - **Perimeter surveillance**: Implement the Portenta Vision Shield in perimeter security to detect intrusions or breaches, triggering immediate responses and minimizing risks.

- **Machine vision and edge computing**: Unlock the potential of edge computing with the Portenta Vision Shield, bringing powerful processing capabilities directly to the field for:
  - **Smart agriculture**: Use the Portenta Vision Shield to monitor crops and soil conditions, identifying issues such as pest infestations or nutrient deficiencies, and enabling precise interventions to optimize yield.
  - **Autonomous vehicles**: Integrate the Portenta Vision Shield into autonomous systems to enhance navigation and obstacle detection, ensuring safe and efficient operation in various environments.
  - **Robotics**: Empower robots with the ability to see and interpret their surroundings using the Portenta Vision Shield, enabling complex tasks such as object recognition and manipulation in dynamic settings.
</div>

## Features

### General Specifications Overview

<p style="text-align: justify;">The Portenta Vision Shield expands the capabilities of the Portenta H7 (any variant) or Portenta C33 boards, adding advanced vision and audio processing features to them.  

Below is a summary of the shield's key components and their specifications.</p>

| **Feature**            | **Description**                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Onboard Camera         | 1/6″ 640 x 480 VGA 60FPS CMOS image sensor (HM0360)                                  |
| Onboard Microphone     | Ultra-compact, low-power, omnidirectional, digital MEMS microphone (x2) (MP34DT06J)  |
| External Memory        | Onboard microSD card slot                                                            |
| Onboard LoRa® Module   | CMWX1ZZABZ-078 (only in LoRa® variant, SKU: ASX00026)                                |
| Onboard RJ45 Connector | For Ethernet capabilities (only in Ethernet variant, SKU: ASX00021)                  |
| Dimensions             | 66.04 x 25.40 mm                                                                     |
| Weight                 | 8 g                                                                                  |
| Pinout Features        | Onboard High-Density connectors easily connect the shield to Portenta family boards  |

<div style="page-break-after: always;"></div>

### Included Accessories

- No accessories are included

### Related Products

- Portenta H7 (SKU: ABX00042)
- Portenta H7 Lite (SKU: ABX00045)
- Portenta H7 Lite Connected (SKU: ABX00046)
- Portenta C33 (SKU: ABX00074)
- Arduino USB Type-C® Cable 2-in-1 (SKU: TPX00094)

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<strong>The Portenta C33 board is not compatible with the onboard camera of the Portenta Vision Shield</strong>, it is only compatible with the shield's advanced audio and connectivity features (Ethernet or LoRa® depending of the variant).
</div>

<div style="page-break-after: always;"></div>

## Ratings

### Recommended Operating Conditions

<p style="text-align: justify;">
The table below provides a comprehensive guideline for the optimal use of the Portenta Vision Shield, outlining typical operating conditions and design limits. The operating conditions of the Portenta Vision Shield are largely a function based on its component's specifications.
</p>

<div style="text-align:center;">

|          **Parameter**           |   **Symbol**    | **Min** | **Typ** | **Max** | **Unit** |
|:--------------------------------:|:---------------:|:-------:|:-------:|:-------:|:--------:|
| Supply Input Voltage<sup>1</sup> | V<sub>IN</sub>  |    -    |   3.3   |   3.3   |    V     |
|      Operating Temperature       | T<sub>OP</sub>  |   -40   |    -    |   85    |    °C    |

</div>

<sup>1</sup> Portenta Vision Shield powered through a Portenta family board.

### Power Consumption

<p style="text-align: justify;">
The table below summarizes the power consumption of the Portenta Vision Shield in different test cases. Notice that the board's operating current will depend greatly on the application.
</p>

|             Parameter             |     Symbol     | Min | Typ | Max | Unit |
|:---------------------------------:|:--------------:|:---:|:---:|:---:|:----:|
| Typical Mode Current Consumption² | I<sub>NM</sub> |  -  | TBD |  -  |  mA  |


<sup>2</sup> Portenta Vision Shield powered through a Portenta family board.

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
The Portenta Vision Shield can be only powered through its High-Density Connectors (VCC pin).
</div>

<div style="page-break-after: always;"></div>

## Functional Overview

<p style="text-align: justify;">The core of the Portenta Vision Shield is its integration with the Portenta family boards, leveraging their processing power for advanced vision and audio applications. The Portenta Vision Shield is equipped with key peripherals, such as dual MEMS microphones (MP34DT06J) and a high-performance camera module (HM0360), all directly interfaced with the main Portenta family board. Two different variants of the shield offer advanced connectivity capabilities, via Ethernet (variant SKU: ASX00021) and via LoRa® variant (SKU: ASX00026).</p>

### Pinout

<p style="text-align: justify;">The pinout for the Portenta Vision Shield Ethernet is shown in the figure below.</p>

![](assets/Vision_Shield_Pinout.png)

<div style="page-break-after: always;"></div>

### Block Diagram

<p style="text-align: justify;">An overview of the high-level architecture of the Portenta Vision Shield Ethernet variant (SKU: ASX00021) is illustrated in the figure below.</p>

<p style="text-align: justify;">An overview of the high-level architecture of the Portenta Vision Shield LoRa® variant (SKU: ASX00026) is illustrated in the figure below.</p>

<div style="page-break-after: always;"></div>

### Power Supply

<p style="text-align: justify;">The Portenta Vision Shield is powered exclusively through the VCC pins (+3V3) of its High Density Connectors. These connectors are designed to be used with boards from the Portenta family, such as the Portenta H7 board (any variant) or the Portenta C33 board. The power is supplied directly from the connected Portenta family board, which acts as the power source for the Portenta Vision Shield.</p>

The detailed figure below illustrates the power architecture of the Portenta Vision Shield.

<div style="page-break-after: always;"></div>

## Device Operation

<div style="text-align:justify;">

### Getting Started – OpenMV IDE
The Portenta Vision Shield and the Portenta H7 boards are supported under OpenMV. In order to easily use OpenMV download the latest OpenMV IDE version **[1]** and follow the Portenta Vision Shield official documentation **[2]** to learn how to create OpenMV vision applications.

### Getting Started - Arduino IDE

If you want to program your Portenta family board offline, install the Arduino Desktop IDE **[3]**. To connect the Portenta family board to your computer, you will need a USB-C® cable.

### Getting Started - Arduino Web Editor

All Arduino devices work out of the box on the Arduino Cloud Editor **[4]** by installing a simple plugin. The Arduino Cloud Editor is hosted online. Therefore, it will always be up-to-date with all the latest features and support for all boards and devices. Follow **[5]** to start coding on the browser and upload your sketches onto your device.

### Getting Started - Arduino Cloud

All Arduino IoT-enabled products are supported on Arduino Cloud, which allows you to log, graph, and analyze sensor data, trigger events, and automate your home or business. Take a look at the official documentation to know more.

### Sample Sketches

Sample sketches for the Portenta Vision Shield can be found either in the “Examples” menu in the Arduino IDE or the “Portenta Vision Shield Documentation” section of Arduino documentation **[6]**.

### Online Resources

Now that you have gone through the basics of what you can do with the device, you can explore the endless possibilities it provides by checking exciting projects on Arduino Project Hub **[7]**, the Arduino Library Reference **[8]**, and the online store **[9]** where you will be able to complement your Portenta family board with additional extensions, sensors, and actuators.
</div>

<div style="page-break-after: always;"></div>

## Mechanical Information

<p style="text-align: justify;">The Portenta Vision Shield is a double-sided board measuring 66.04 x 25.40 mm. It features an RJ45 connector that overhangs the top edge (present only in the Ethernet variant, SKU: ASX00021), an onboard camera positioned near the center of the board, and a LoRa® module located near the bottom edge (only in the LoRa® variant, SKU: ASX00026). The Portenta Vision Shield also includes two High-Density connectors at the bottom edge, enabling quick and efficient integration with Portenta Family boards.</p>

### Board Dimensions

<p style="text-align: justify;">The outline and mounting hole dimensions of the Portenta Vision Shield are shown in the figure below, with all measurements in millimeters (mm). The board shown below is the Ethernet variant of the Portenta Vision Shield (SKU: ASX00021).</p>

<img src="assets/Vision_Shield_Outline.png" width="375" height="auto">

The Portenta Vision Shield has four 2.25 mm drilled mounting holes for mechanical fixing.

### Board Connectors

<p style="text-align: justify;">The connectors of the Portenta Vision Shield are placed on the top and bottom side of the shield; their placement are shown in the figures below; all the dimensions are in mm. The shield shown below is the Ethernet variant (SKU: ASX00021).</p>

![](assets/Vision_Shield_Connectors.png)

<p style="text-align: justify;">The Portenta Vision Shield was designed to be used with a Portenta family board. However, you can also design your own hardware and use the Poretnta Vision Shield via its High-Density connectors by following to the Portenta family standard.</p>

<div style="page-break-after: always;"></div>

## Certifications

### Declaration of Conformity CE/RED DoC (EU)

<p style="text-align: justify;">We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).</p>

### Declaration of Conformity to EU RoHS & REACH 191 11/26/2018

<p style="text-align: justify;">Arduino boards are in compliance with Directive 2011/65/EU of the European Parliament and Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.</p>

| **Substance**                          | **Maximum Limit (ppm)** |
| -------------------------------------- | ----------------------- |
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

<p style="text-align: justify;">Arduino boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.</p>

### Conflict Minerals Declaration

<p style="text-align: justify;">As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.</p>

## FCC Caution

<p style="text-align: justify;">Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment. This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.</p>

FCC RF Radiation Exposure Statement:

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with a minimum distance 20 cm between the radiator and your body.

| **Feature**              | **Description**                             |
|--------------------------|---------------------------------------------|
| **Antenna Manufacturer** | Dynaflex                                    |
| **Antenna Model**        | 2G-3G-4G ADHESIVE MOUNT ANTENNA DIPOLE      |
| **Antenna Type**         | External omnidirectional dipole antenna     |
| **Antenna Gain**         | -1 dBi                                      |

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

<p style="text-align: justify;">Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 201453/EU. This product is allowed to be used in all EU member states.</p>

| **Frequency bands** | **Maximum Output Power (ERP)** |
|---------------------|--------------------------------|
| 863-870 MHz         | 0.73 dBm                       |

## Company Information

| **Company name** | **Arduino S.r.l.**                           |
|------------------|----------------------------------------------|
| Company address  | Via Andrea Appiani, 25 - 20900 Monza (Italy) |

## Reference Documentation

| **Reference**                        | **Link**                                                                 |
|--------------------------------------|--------------------------------------------------------------------------|
| OpenMV IDE                           | https://openmv.io/pages/download                                         |
| Portenta Vision Shield Documentation | https://docs.arduino.cc/hardware/portenta-vision-shield                  |
| Arduino IDE (Desktop)                | https://www.arduino.cc/en/Main/Software                                  |
| Arduino IDE (Cloud)                  | https://create.arduino.cc/editor                                         |
| Cloud IDE Getting Started            | https://docs.arduino.cc/arduino-cloud/guides/overview                    |
| Project Hub                          | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending |
| Library Reference                    | https://www.arduino.cc/reference/en/                                     |
| Arduino Store                        | https://store.arduino.cc/                                                |

## Document Revision History

| **Date**   | **Revision** | **Changes**                                      |
|------------|--------------|--------------------------------------------------|
| 30/08/2024 | 5            | Datasheet structure revamp                       |
| 20/11/2023 | 4            | Datasheet structure updated, FCC Caution updated |
| 15/11/2023 | 3            | Datasheet updated as a collective datasheet      |
| 13/01/2022 | 2            | Datasheet information update                     |
| 03/03/2021 | 1            | First release                                    |