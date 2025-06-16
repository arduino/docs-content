---
identifier: ABX00112-ABX00137
title: Arduino® Nano Matter
type: maker
author: José Bagur, Christopher Méndez
---

![](assets/Nano-Matter_Top.png)

# Description

<p style="text-align: justify;">Expand your home automation and building management projects with the Arduino Nano Matter. This board integrates the high-performance MGM240S microcontroller from Silicon Labs and directly brings the advanced Matter standard for Internet of Things (IoT) connectivity to hobbyists and professionals. The Nano Matter's compact and sturdy build, measuring 18 mm x 45 mm, is perfect for projects that demand energy efficiency and diverse connectivity options, such as Bluetooth® Low Energy and OpenThread. Embrace the simplicity and versatility of the Nano Matter to effortlessly interface with any Matter® compatible devices and leverage the Arduino ecosystem's wide range of peripherals and inputs/outputs to enhance your device connectivity and project capabilities. </p>

# Target Areas

Internet of Things, home automation, professional automation, environmental monitoring, and climate control

# CONTENTS
## Application Examples

The Arduino Nano Matter is not just an IoT board, it is a gateway to innovation in various sectors, from streamlining manufacturing processes to creating responsive and comfortable living and working environments. Discover more about the transformative potential of the Nano Matter in the following application examples:

- **Smart homes**: Transform residential spaces into intelligent environments with the Nano Matter, capable of:
  - **Voice-controlled smart home**: Integrate the Nano Matter with popular voice assistant platforms like Amazon Alexa or Google Assistant, enabling residents to control smart home devices, such as lights, thermostats, and switches, using simple voice commands, enhancing convenience and accessibility.
  - **Smart lighting**: Automate your home lighting system with the Nano Matter to adjust the brightness based on occupancy, time of day, or ambient light levels, saving energy and ensuring optimal lighting conditions in every room.
  - **Automated shades**: Connect the Nano Matter to your motorized shades to automatically adjust them according to sunlight exposure, room occupancy, or specific times of the day, creating the perfect ambiance while improving energy efficiency.
  - **Home health monitoring**: Use the Nano Matter to connect with environmental sensors, monitor indoor conditions like pressure, humidity, and temperature, and maintain a healthy living environment by providing actionable insights for comfort and well-being.

- **Building automation**: Elevate building management with the Nano Matter, enhancing comfort and efficiency through:
  - **HVAC control and monitoring**: Implement the Nano Matter to connect and control HVAC systems across various building zones. Monitor environmental conditions and adjust settings for optimal indoor comfort while maximizing energy efficiency.
  - **Energy management**: Use Nano Matter's connectivity to smart meters and appliances to view a building's energy consumption. Implement energy-saving measures automatically, reducing costs and environmental impact.
  - **Occupancy sensing and space utilization**: With the Nano Matter and Matter-enabled sensors, gain insights into actual building occupancy and use this data to adjust lighting, heating, and cooling systems, ensuring efficient use of space and resources.

- **Industrial automation**: Unlock the full potential of modern manufacturing with the Nano Matter. Designed for seamless integration into industrial settings, the Nano Matter streamlines operations through:
  - **Machine-to-Machine interoperability**: Enhance your factory floor with the Nano Matter boards to enable dynamic supervision between machines. Should one machine begin producing defective parts due to a malfunction, adjacent machines are instantly alerted, halting their operations and notifying a human operator, thus reducing waste and downtime.
  - **Machine status monitoring**: Integrate the Nano Matter into your industrial systems for real-time monitoring of critical conditions such as temperature, pressure, and humidity, ensuring timely maintenance and intervention, preventing costly breakdowns, and maintaining consistent production quality.
  - **Worker safety optimization**: Elevate safety standards in your facility with the Nano Matter, which provides real-time monitoring of environmental conditions and detects personnel presence in hazardous areas, enhancing worker safety by preventing machine operation when a human is detected in dangerous zones.

## Features
### General Specifications Overview

<p style="text-align: justify;">
The Arduino Nano Matter merges the well-known Arduino way of making complex technology more accessible, bringing Matter, one of the most popular IoT connectivity standards, closer to the hobbyist and professional world. The powerful MGM240S multi-protocol wireless module from Silicon Labs is the main controller of the board.

The main features are highlighted in the table shown below.
</p>


| Feature             | Description                                                                                                                                                            |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Microcontroller     | 78 MHz, 32-bit Arm® Cortex®-M33 core (MGM240SD22VNA)                                                                                                                   |
| Internal Memory     | 1536 kB Flash and 256 kB RAM                                                                                                                                           |
| Connectivity        | 802.15.4 Thread, Bluetooth® Low Energy 5.3, and Bluetooth® Mesh                                                                                                        |
| Security            | Secure Vault® from Silicon Labs                                                                                                                                        |
| USB Connectivity    | USB-C® port for power and data                                                                                                                                         |
| Power Supply        | Various options for easily powering the board: USB-C® port and external power supply connected through the board's Nano-styled header connector pins (5V, VIN)         |
| Analog Peripherals  | 12-bit ADC (x20), up to 12-bit DAC (x4)                                                                                                                                |
| Digital Peripherals | GPIO (x22 - All exposed I/O can be used as digital), UART (x2), I2C (x2), SPI (x2), PWM (x22) with a maximum of 5 simultaneously operational channels                  |
| Debugging           | JTAG/SWD debug port (accessible through the board's test pads)                                                                                                         |
| Dimensions          | 18 mm x 45 mm                                                                                                                                                          |
| Weight              | 4 g                                                                                                                                                                    |
| Pinout features     | The Nano Matter (ABX00112) has castellated/through-hole pins for SMD mounting, while the Nano Matter (ABX00137) comes with headers pre-installed for easy prototyping. |


<div style="page-break-after: always;"></div>

### Included Accessories

- No accessories are included

### Related Products

- Arduino USB Type-C® Cable 2-in-1 (SKU: TPX00094)
- Arduino Nano Screw Terminal Adapter (SKU: ASX00037-3P)

<div style="page-break-after: always;"></div>

## Ratings

### Recommended Operating Conditions

<p style="text-align: justify;">
The table below provides a comprehensive guideline for the optimal use of the Nano Matter, outlining typical operating conditions and design limits. The operating conditions of the Nano Matter are largely a function based on its component's specifications.
</p>

<div style="text-align:center;">

|          **Parameter**           |   **Symbol**    | **Min** | **Typ** | **Max** | **Unit** |
| :------------------------------: | :-------------: | :-----: | :-----: | :-----: | :------: |
| Input voltage from USB connector | V<sub>USB</sub> |   4.8   |   5.0   |   5.5   |    V     |
|    Input voltage from VIN pad    | V<sub>IN</sub>  |    6    |   7.0   |   21    |    V     |
|      Operating Temperature       | T<sub>OP</sub>  |   -40   |    -    |   85    |    °C    |

</div>


### Power Consumption

<p style="text-align: justify;">
The table below summarizes the power consumption of the Nano Matter in different test cases. Notice that the board's operating current will depend greatly on the application.
</p>

|             Parameter             |     Symbol     | Min | Typ | Max | Unit |
|:---------------------------------:|:--------------:|:---:|:---:|:---:|:----:|
| Typical Mode Current Consumption² | I<sub>NM</sub> |  -  | 16  |  -  |  mA  |


<sup>2</sup> Nano Matter powered through the 5V pin (+5 VDC), running a Matter color lightbulb example.

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
To use the Nano Matter in <strong>low-power mode</strong>, the board must be powered through the <strong>pin 3.3V</strong>.
</div>


<div style="page-break-after: always;"></div>

## Functional Overview

<p style="text-align: justify;">
The core of the Nano Matter is the MGM240SD22VNA microcontroller from Silicon Labs. The board also contains several peripherals and actuators connected to its microcontroller, such as a push button and an RGB LED available for the user. 
</p>

### Pinout

The Nano-styled header connectors pinout is shown in the figure below.

![](assets/Nano_Matter_Pinout.png)

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
The <strong>Nano Matter with headers (ABX00137)</strong> shares the same architecture as the <strong>Nano Matter (ABX00112)</strong> but comes with headers pre-installed.
</div>

<div style="page-break-after: always;"></div>

### Block Diagram

An overview of the high-level architecture of the Nano Matter is illustrated in the figure below.

![](assets/Nano_Matter_Block_Diagram.png)

<div style="page-break-after: always;"></div>

### Power Supply

<div style="text-align:justify;">

The Nano Matter can be powered through one of the following interfaces:

- **Onboard USB-C® port**: Provides a convenient way to power the board using standard USB-C® cables and adapters.
- **VIN pad**: Applying 6 to 21 VDC to the VIN pin of the Nano-styled header connector. 
- **5V pad**: Applying +5 VDC to the 5V pin of the Nano-styled header connector.

A detailed figure below illustrates the power options available on the Nano Matter and the main system power architecture.

![](assets/Nano_Matter_Power_Tree.png)

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<strong>Low-Power Tip:</strong> For power efficiency, safely cut the LED jumper and connect an external +3.3 VDC power supply to the board's 3V3 pin. This configuration does not power the board's USB bridge.
</div>

</div>

<div style="background-color: #FFCCCC; border-left: 6px solid #FF0000; margin: 20px 0; padding: 15px;">
<strong>Safety Note:</strong> Disconnect power before board modifications. Avoid short-circuiting. Refer to the full guide for more safety tips.
</div>

<div style="page-break-after: always;"></div>

## Device Operation

<div style="text-align:justify;">

### Getting Started - IDE

If you want to program your Nano Matter offline, install the Arduino Desktop IDE **[1]**. To connect the Nano Matter to your computer, you will need a USB-C® cable.

### Getting Started - Arduino Cloud Editor

All Arduino devices work out of the box on the Arduino Cloud Editor **[2]** by installing a simple plugin. The Arduino Cloud Editor is hosted online. Therefore, it will always be up-to-date with all the latest features and support for all boards and devices. Follow **[3]** to start coding on the browser and upload your sketches onto your device.

### Getting Started - Arduino Cloud

All Arduino IoT-enabled products are supported on Arduino Cloud, which allows you to log, graph, and analyze sensor data, trigger events, and automate your home or business. Take a look at the official documentation to know more.

### Sample Sketches

Sample sketches for the Nano Matter can be found either in the “Examples” menu in the Arduino IDE or the “Nano Matter Documentation” section of Arduino documentation **[4]**.

### Online Resources

Now that you have gone through the basics of what you can do with the device, you can explore the endless possibilities it provides by checking exciting projects on Arduino Project Hub **[5]**, the Arduino Library Reference **[6]**, and the online store **[7]** where you will be able to complement your Nano Matter board with additional extensions, sensors, and actuators.
</div>

<div style="page-break-after: always;"></div>

## Mechanical Information

<p style="text-align: justify;">
The Nano Matter is a double-sided 18 mm x 45 mm board featuring a USB-C® port extending from the top edge. The onboard wireless antenna is positioned at the center of the bottom edge.

The Nano Matter (ABX00112) has dual castellated/through-hole pins along both long edges, making it easy to solder onto a custom PCB for direct integration.

The Nano Matter with headers pre-installed (ABX00137) is also available, providing convenient access for probing and testing.
</p>

### Board Dimensions

The Nano Matter board outline and mounting holes dimensions are shown in the figure below; all the dimensions are in mm. 

![](assets/Nano_Matter_Outline.png)

The Nano Matter has four 1.65 mm drilled mounting holes for mechanical fixing.

### Board Connectors

Connectors of the Nano Matter are placed on the top side of the board; their placement is shown in the figure below; all the dimensions are in mm. 

![](assets/Nano_Matter_Connectors.png)

<p style="text-align: justify;">
The Nano Matter was designed to be usable as a surface-mount module and presents a dual inline package (DIP) format with the Nano-styled header connectors on a 2.54 mm pitch grid with 1 mm holes.
</p>

### Board Peripherals and Actuators 

<p style="text-align: justify;">
The Nano Matter has one push button and one RGB LED available for the user; both the push button and the RGB LED are placed on the top side of the board.  Their placement is shown in the figure below; all the dimensions are in mm.
</p>

![](assets/Nano_Matter_PeripheralsActuators.png)

<p style="text-align: justify;">
The Nano Matter is designed to be usable as a surface-mount module and presents a dual inline package (DIP) format with the Nano-styled header connectors on a 2.54 mm pitch grid with 1 mm holes.
</p>

<div style="page-break-after: always;"></div>

## Product Compliance

### Product Compliance Summary

| **Product Compliance** |
|:----------------------:|
|  CE (European Union)   |
|          RoHS          |
|         REACH          |
|          WEEE          |
|       FCC (USA)        |
|      IC (Canada)       |
|       UKCA (UK)        |
|        Matter®         |
|       Bluetooth®       |

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

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration

As a global supplier of electronic and electrical components, Arduino is aware of our obligations concerning laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence, Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

## FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

1. This device may not cause harmful interference

2. This device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment

3. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

<div style="page-break-after: always;"></div>

**Note:** This equipment has been tested and found to comply with the limits for a Class B digital
device, pursuant to part 15 of the FCC Rules. These limits are designed to provide
reasonable protection against harmful interference in a residential installation. This equipment
generates, uses and can radiate radio frequency energy and, if not installed and used in
accordance with the instructions, may cause harmful interference to radio communications.
However, there is no guarantee that interference will not occur in a particular installation. If
this equipment does cause harmful interference to radio or television reception, which can be
determined by turning the equipment off and on, the user is encouraged to try to correct the
interference by one or more of the following measures:
- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the
receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.

English:
User manuals for license-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual or alternatively on the device or both. This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions:

1. This device may not cause interference

2. This device must accept any interference, including interference that may cause undesired operation of the device.

French:
Le présent appareil est conforme aux CNR d’Industrie Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes:

1. L’ appareil nedoit pas produire de brouillage

2. L’utilisateur de l’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

**IC SAR Warning:**

English:
This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

French:
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85 °C and shouldn’t be lower than -40 °C.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 2014/53/EU. This product is allowed to be used in all EU member states.

## Company Information

| **Company name** |              **Arduino S.r.l.**              |
|:----------------:|:--------------------------------------------:|
| Company address  | Via Andrea Appiani, 25 - 20900 MONZA (Italy) |

## Reference Documentation
|             **Ref**             | **Link**                                                                        |
|:-------------------------------:|---------------------------------------------------------------------------------|
|      Arduino IDE (Desktop)      | https://www.arduino.cc/en/Main/Software                                         |
|       Arduino IDE (Cloud)       | https://create.arduino.cc/editor                                                |
| Arduino Cloud - Getting started | https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started |
|    Nano Matter Documentation    | https://docs.arduino.cc/hardware/nano-matter                                    |
|           Project Hub           | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending        |
|        Library Reference        | https://www.arduino.cc/reference/en/                                            |
|          Online Store           | https://store.arduino.cc/                                                       |
         

## Document Revision History

|  **Date**  | **Revision** |                      **Changes**                      |
| :--------: | :----------: | :---------------------------------------------------: |
| 11/02/2025 |      5       | Header Version and SKU added as Collective Datasheet  |
| 14/11/2024 |      4       | Official launch revision and power information update |
| 05/09/2024 |      3       |         Cloud Editor updated from Web Editor          |
| 07/05/2024 |      2       |                     Board update                      |
| 21/03/2024 |      1       |               Community Preview Release               |
