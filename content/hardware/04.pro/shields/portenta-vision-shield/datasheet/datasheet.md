---
identifier: ASX00021-ASX00026
title: Arduino® Portenta Vision Shield
type: pro
variant: 'Collective Datasheet'
---

![](assets/featured.jpg)

# Description

<p style="text-align: justify;">Enhance your industrial automation and surveillance projects with the Arduino Portenta Vision Shield. This add-on board integrates with the Portenta family, offering advanced machine vision capabilities and extended connectivity. The Vision Shield's compact design and high-density connector ensure a quick and efficient setup. It transforms your Portenta family board into a powerful tool for real-time image processing and edge computing, suitable for demanding industrial environments.</p>

# Target Areas
Industrial automation, surveillance, machine vision, edge computing

# CONTENTS
## Application Examples

<div style="text-align:justify;">
The Vision Shield is an add-on and a gateway to innovative solutions in various industries. Explore the possibilities of integrating advanced machine vision and edge computing into your projects with the following application examples:

- **Industrial automation**: Elevate your automation systems with the Vision Shield, enabling precise and real-time image processing for:
  - **Quality control**: Implement the Vision Shield in production lines to automatically detect product defects and ensure that only high-quality items pass through.
  - **Predictive maintenance**: Use machine vision to monitor equipment and identify early signs of wear or failure, reducing downtime and maintenance costs.
  - **Automated sorting**: Integrate the Vision Shield into conveyor systems to automatically sort items based on color, shape, or size, improving efficiency and accuracy.

- **Surveillance**: Enhance security and monitoring systems with advanced visual capabilities provided by the Vision Shield for:
  - **Real-time threat detection**: Deploy the Vision Shield in security systems to identify and alert authorities of potential threats, such as unauthorized access or suspicious activities, in real-time.
  - **Environmental monitoring**: Utilize the Vision Shield's imaging capabilities to monitor environmental conditions in critical areas, such as chemical plants, to ensure safety and compliance with regulations.
  - **Perimeter surveillanc**e: Implement the Vision Shield in perimeter security to detect intrusions or breaches, triggering immediate responses and minimizing risks.

- **Machine vision and edge computing**: Unlock the potential of edge computing with the Vision Shield, bringing powerful processing capabilities directly to the field for:
  - **Smart agriculture**: Use the Vision Shield to monitor crops and soil conditions, identifying issues such as pest infestations or nutrient deficiencies, and enabling precise interventions to optimize yield.
  - **Autonomous vehicles**: Integrate the Vision Shield into autonomous systems to enhance navigation and obstacle detection, ensuring safe and efficient operation in various environments.
  - **Robotics**: Empower robots with the ability to see and interpret their surroundings using the Vision Shield, enabling complex tasks such as object recognition and manipulation in dynamic settings.
</div>

## Features

### General Specifications Overview

<p style="text-align: justify;">The Vision Shield expands the capabilities of the Portenta H7 (any variant) or Portenta C33 boards, adding advanced vision and audio processing features to them.  

Below is a summary of the shield's key components and their specifications.</p>

| **Feature**            | **Description**                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Onboard Camera         | 1/6″ 640 x 480 VGA 60FPS CMOS image sensor (HM0360)                                  |
| Onboard Microphone     | Ultra-compact, low-power, omnidirectional, digital MEMS microphone (x2) (MP34DT06J)  |
| External Memory        | Onboard microSD card slot                                                            |
| Onboard LoRa® Module   | CMWX1ZZABZ-078 (only in LoRa® variant, SKU: ASX00026)                                |
| Onboard RJ45 Connector | For Ehthernet capabilities (only in Ethernet variant, SKU: ASX00021)                 |
| Dimensions             | 67.07 x 25.39 mm                                                                     |
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
The <strong>Portenta C33</strong> board is not compatible with the onboard camera of the Vision Shield, it is only compatible with the shield's connectivity features (Ethernet or LoRa®).
</div>

<div style="page-break-after: always;"></div>

## Ratings

### Recommended Operating Conditions

<p style="text-align: justify;">
The table below provides a comprehensive guideline for the optimal use of the Vision Shield, outlining typical operating conditions and design limits. The operating conditions of the Vision Shield are largely a function based on its component's specifications.
</p>

<div style="text-align:center;">

|          **Parameter**           |   **Symbol**    | **Min** | **Typ** | **Max** | **Unit** |
|:--------------------------------:|:---------------:|:-------:|:-------:|:-------:|:--------:|
| Supply Input Voltage<sup>1</sup> | V<sub>IN</sub>  |    -    |   3.3   |   3.3   |    V     |
|      Operating Temperature       | T<sub>OP</sub>  |   -40   |    -    |   85    |    °C    |

</div>

<sup>1</sup> Vision Shield powered through a Portenta family board.

### Power Consumption

<p style="text-align: justify;">
The table below summarizes the power consumption of the Vision Shield in different test cases. Notice that the board's operating current will depend greatly on the application.
</p>

|             Parameter             |     Symbol     | Min | Typ | Max | Unit |
|:---------------------------------:|:--------------:|:---:|:---:|:---:|:----:|
| Typical Mode Current Consumption² | I<sub>NM</sub> |  -  | TBD |  -  |  mA  |


<sup>2</sup> Vision Shield powered through a Portenta family board.

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
The Vision Shield can be only powered through its High-Density Connectors (VCC pin).
</div>

## Functional Overview

### Board Topology
![Top view](assets/visionShield_topology_top.png)

![Bottom view](assets/visionShield_topology_bot.png)

| Ref.   | Description                                    | Ref. | Description                                        |
| ------ | ---------------------------------------------- | ---- | -------------------------------------------------- |
| U1     | Voltage Regulator                              | J3   | LoRa® Radio Antenna U.FL Connector (ASX00026 Only) |
| U2,U3  | ST MP34DT06JTR Digital Microphones             | J7   | Ethernet Connector (ASX00021 Only)                 |
| M1     | Murata CMWX1ZZABZ LoRa® Module (ASX00026 Only) | J9   | Micro SD Card Connector                            |
| J1, J2 | High-Density Connectors                        | CN1  | JTAG Connector                                     |
| CAM1   | Camera Module Himax HM-01B0                    |      |                                                    |

### Power
The Portenta H7/C33 supplies 3.3 V power to the LoRa® module (ASX00026 only), Ethernet communication (ASX00021 only), Micro SD slot and dual microphones via the 3.3 V output of the high-density connectors. An onboard LDO regulator supplies a 2.8 V output (300 mA) for the camera module.

### Camera Module

The Himax HM-01B0 Module is a very low-power camera with 324x324 resolution and a maximum of 60 FPS depending on the operating mode. Video data is transferred over a configurable 8-bit interconnect with support for frame and line synchronization. The module delivered with the Portenta Vision Shield is the monochrome version. Configuration is achieved via an I2C connection with the compatible Portenta boards microcontrollers.

HM-01B0 offers very low-power image acquisition and provides the possibility to perform motion detection without main processor interaction. The “Always-on” operation provides the ability to turn on the main processor when movement is detected with minimal power consumption.

***Note: The Portenta C33 is not compatible with the camera of the Portenta Vision Shield***


### Digital Microphones

The dual MP34DT05 digital MEMS microphones are omnidirectional and operate via a capacitive sensing element with a high (64 dB) signal-to-noise ratio. The microphones have been configured to provide separate left and right audio over a single PDM stream.

The sensing element, capable of detecting acoustic waves, is manufactured using a specialized silicon micromachining process dedicated to produce audio sensors.


### Micro SD Card Slot

A Micro SD card slot is available under the Portenta Vision Shield board. Available libraries allow reading and writing to FAT16/32 formatted cards.


### Ethernet (ASX00021 Only)

Ethernet connector allows connecting to 10/100 Base TX networks using the Ethernet PHY available on the Portenta board.


### LoRa® Module (ASX00026 Only)

LoRa® connectivity is provided by the Murata CMWX1ZZABZ module. This module contains an STM32L0 processor along with a Semtech SX1276 Radio. The processor is running on Arduino open-source firmware based on Semtech code.

## Board Operation

### Getting Started – OpenMV

The Portenta Vision Shield and Portenta H7 are supported under OpenMV. In order to easily use OpenMV download the latest OpenMV IDE **[1]** and follow the Portenta Vision Shield official documentation **[2]** to learn how to create OpenMV vision applications.

### Getting Started – IDE

If you want to program your Arduino board while offline you need to install the Arduino Desktop IDE **[3]**. To connect the board to your computer, you will need a USB cable. This also provides power to the board, as indicated by the LED.


### Getting Started – Arduino Web Editor (Create)

All Arduino and Genuino boards, including this one, work out-of-the-box on the Arduino Web Editor **[4]** by just installing a simple plugin.

The Arduino Web Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow **[5]** to start coding on the browser and upload your sketches onto your board.


### Getting Started – Arduino Cloud

All Arduino IoT-enabled products are supported on Arduino Cloud which allows you to Log, graph and analyze sensor data, trigger events, and automate your home or business.

### Online Resources
Now that you have gone through the basics of what you can do with the board you can explore the endless possibilities it provides by checking exciting projects on ProjectHub **[6]**, the Arduino Library Reference **[7]** and the online store **[8]** where you will be able to complement your board with sensors, actuators and more.

### Board Recovery
All Arduino boards have a built-in bootloader which allows flashing the board via USB. In case a sketch locks up the processor and the board is not reachable anymore via USB it is possible to enter bootloader mode by double-tapping the reset button right after the power-up.

## Connector Pinouts
### JTAG

| Pin                          | Function | Type          | Description                                    |
| ---------------------------- | -------- | ------------- | ---------------------------------------------- |
| 1                            | VDDIO    | Power         | Positive Reference voltage for debug interface |
| 2                            | SWD      | I/O           | Single Wire Debug Data                         |
| 3,5,9                        | GND      | Power         | Negative reference voltage for debug interface |
| 4                            | SCK      | Output        | Single Wire Debug Clock                        |
| 6                            | SWO      | I/O           | Single Wire Debug Trace                        |
| 10                           | RESET    | Input         | CPU Reset                                      |
| 7,11,12,13,14,15,17,18,19,20 | NC       | Not Connected |                                                |


<div style="break-after:page"></div>

### High-Density Connector
![High-density connector pinout](assets/visionShield_HD_pinout.png)

## Mechanical Information
### Board Outline
![Board dimensions](assets/visionShield_outline.png)

### Mounting Instructions
![Mounting details](assets/visionShield_mounting.png)

### Connector and Component Positions
![Connectors positions TOP](assets/visionShield_connectors_top.png)

![Connectors positions BOTTOM](assets/visionShield_connectors_bot.png)



## Certifications
### Declaration of Conformity CE/RED DoC (EU)
We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).

### Declaration of Conformity to EU RoHS & REACH 191 11/26/2018
Arduino boards are in compliance with Directive 2011/65/EU of the European Parliament and Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.

| **Substance**                          | **Maximum Limit (ppm)** |
| -------------------------------------- | ----------------------- |
| Lead (Pb)                              | 1000                    |
| Cadmium (Cd)                           | 100                     |
| Mercury (Hg)                           | 1000                    |
| Hexavalent Chromium (Cr6+)             | 1000                    |
| Poly Brominated Biphenyls (PBB)        | 1000                    |
| Poly Brominated Diphenyl ethers (PBDE) | 1000                    |
| Bis(2-Ethylhexyl} phthalate (DEHP)     | 1000                    |
| Benzyl butyl phthalate (BBP)           | 1000                    |
| Dibutyl phthalate (DBP)                | 1000                    |
| Diisobutyl phthalate (DIBP)            | 1000                    |

Exemptions : No exemptions are claimed.

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration
As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

## FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment. 
This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
FCC RF Radiation Exposure Statement:

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with a minimum distance 20 cm between the radiator& your body.

<table>
  <tr>
   <td>Antenna manufacturer:
   </td>
   <td>Dynaflex
   </td>
  </tr>
  <tr>
   <td>Antenna Model:
   </td>
   <td>2G-3G-4G ADHESIVE MOUNT ANTENNA DIPOLE
   </td>
  </tr>
  <tr>
   <td>Antenna type:
   </td>
   <td>External omnidirectional dipole antenna
   </td>
  </tr>
  <tr>
   <td>Antenna gain:
   </td>
   <td>-1 dBi
   </td>
  </tr>
</table>

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 201453/EU. This product is allowed to be used in all EU member states.

| Frequency bands | Maximum Output Power (ERP) |
| --------------- | -------------------------- |
| 863-870 MHz     | 0.73 dBm                   |


## Company Information


| Company name    | Arduino S.r.l.                             |
| --------------- | ------------------------------------------ |
| Company Address | Via Andrea Appiani, 25 20900 MONZA (Italy) |

## Reference Documentation

| **Ref**                              | **Link**                                                                 |
| ------------------------------------ | ------------------------------------------------------------------------ |
| OpenMV IDE                           | https://openmv.io/pages/download                                         |
| Portenta Vision Shield Documentation | https://docs.arduino.cc/hardware/portenta-vision-shield                  |
| Arduino IDE (Desktop)                | https://www.arduino.cc/en/Main/Software                                  |
| Arduino IDE (Cloud)                  | https://create.arduino.cc/editor                                         |
| Cloud IDE Getting Started            | https://docs.arduino.cc/arduino-cloud/guides/overview                    |
| ProjectHub                           | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending |
| Library Reference                    | https://www.arduino.cc/reference/en/                                     |
| Arduino Store                        | https://store.arduino.cc/                                                |

## Change Log

| **Date**   | **Revision** | **Changes**                            |
| ---------- | ------------ | -------------------------------------- |
| 20/11/2023 | 4            | Structure Updates. FCC Caution Updated |
| 15/11/2023 | 3            | Updates as a Collective Datasheet      |
| 13/01/2022 | 2            | Information update                     |
| 03/03/2021 | 1            | First Release                          |
