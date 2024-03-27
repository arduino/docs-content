---
identifier: ASX00055
title: Arduino® Portenta Mid Carrier
type: pro
author: José Bagur
---

![](assets/Portenta_Mid_Carrier_Top_View.png)

# Description 

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier speeds up project building for the Portenta board family, making connecting to High-Density signals through special headers easier. It works well with the Portenta C33, H7, and X8 boards, perfect for the Internet of Things, asset tracking, machine vision, robotics, and automation projects and applications. This carrier offers a variety of ports like CAN bus lines, Ethernet, microSD, and USB, plus connections for cameras and display shields. It also has special debug pins and a battery backup for real-time clocks, simplifying development. These key aspects make the Portenta Mid Carrier a vital tool for developing smart, connected devices quickly and effectively.
</p>

# Target Areas

Rapid prototyping, asset tracking, Internet of Things, machine vision, robotics, and automatization

# CONTENTS
## Application Examples

<div style="text-align:justify;">
The Arduino Portenta Mid Carrier enhances various prototyping applications thanks to its flexible design. The Portenta Mid Carrier provides a robust platform for many projects, from industry-ready prototypes to machine vision and cellular connectivity testing. Here are some application examples:

- **Prototyping**: The Portenta Mid Carrier facilitates industry-ready prototyping by combining with Portenta family boards to expose essential peripherals such as microSD, Ethernet, and USB. It also simplifies debugging and inspection with dedicated pins for CAN bus lines, streamlining the development process.
- **Prototyping with external devices**: Enhance your Portenta boards with the Portenta Mid Carrier, which is ready for integration with a broad spectrum of external hardware components or devices. This adaptability makes it ideal for projects requiring embedded sensing or straightforward actuation, ensuring comprehensive support.
- **Reference design**: The Portenta Mid Carrier serves as an excellent reference design and aids in the development of custom products within the Portenta ecosystem. Arduino PRO's full development, production, and operation support provides a solid foundation for tailoring solutions to specific business needs.
- **Frictionless machine vision prototyping**: Pair the Portenta Mid Carrier with an MIPI or Arducam® camera to effortlessly embark on machine vision projects. Whether for object detection and recognition, defect identification, or asset tracking, the Portenta Mid Carrier streamlines the creation of complex vision-based applications.
- **Rapid testing of cellular connectivity**: Utilize the mini PCIe connector on the Portenta Mid Carrier for swift cellular connectivity testing. This feature is invaluable for applications in smart cities/buildings, remote maintenance, and fleet management, ensuring rapid data transmission even in locations lacking Wi-Fi® coverage.
</div>

<div style="page-break-after: always;"></div>

## Features
### General Specifications Overview

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier is an excellent tool for building scalable projects based on the Portenta Family. The Carrier was designed to give quick access to all the essential signals of the Portenta family boards, making it easier to add new features to your projects with its Ethernet and mPCIe connectors. The Carrier includes a microSD card slot starting from an external source, and it has CAN bus lines for connecting to actuators, which helps manage devices easily. You can also develop machine vision applications using the onboard camera connectors. The Carrier is also a straightforward reference design for creating their hardware. 

The main features of the Portenta Mid Carrier are highlighted in the table below.
</p>

<div style="text-align:center;">

<table>
<thead>
  <tr>
    <th>Feature</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Ethernet</td>
    <td>RJ45 connector (x1)</td>
  </tr>
  <tr>
    <td>USB Connectivity</td>
    <td>USB-A female connector for data logging and connection to external peripherals (x1)</td>
  </tr>
  <tr>
    <td>Power Supply</td>
    <td>Various options for easily powering the Carrier: onboard USB-C® port of the Portenta family board connected to the Carrier, and external power supply connected through the onboard screw terminal block and dedicated pins of the breakout header connectors of the Carrier</td>
  </tr>
  <tr>
    <td>Screw Terminal Block</td>
    <td>Used to power the carrier and for the CAN bus interface</td>
  </tr>
  <tr>
    <td>Breakout Header Connectors</td>
    <td>Available interfaces through the breakout headers are the following: UART (x4), I2S (x1), CAN bus (x2), SPDIF (x1), PDM (x1), GPIO (x7), SPI (x2), I2C (x3), SAI (x1), PWM (x10), analog channels (x8)</td>
  </tr>
  <tr>
    <td>Camera Connectors</td>
    <td>MIPI camera (x1), Digital Video Port (DVP) interface (x1)</td>
  </tr>
  <tr>
    <td>Debugging</td>
    <td>Onboard JTAG/SWD debug connector</td>
  </tr>
  <tr>
    <td>Dimensions</td>
    <td>114 mm x 86.5 mm</td>
  </tr>
  <tr>
    <td>Weight</td>
    <td>25 g</td>
  </tr>
  <tr>
    <td>Operating Temperature</td>
    <td>-40 °C to +85 °C</td>
  </tr>
</tbody>
</table>
</div>

<div style="page-break-after: always;"></div>

### Related Accessories (Not Included)

- MIPI camera
- microSD card
- CR1225 (3 VDC) coin cell
- Arducam® DVP camera modules
- SIM card (only data compatible)

### Related Products

- Arduino® Portenta X8 (SKU: ABX00049)
- Arduino® Portenta C33 (SKU: ABX00074)
- Arduino® Portenta H7 (SKU: ABX00042/ABX00045/ABX00046)
- Arduino® Pro 4G Module EMEA (SKU: TPX00201)
- Arduino® Pro 4G GNSS Module Global (SKU: TPX00200)
- Arduino® GIGA Display Shield (SKU: ASX00039)
- Arduino USB Type-C® Cable 2-in-1 (SKU: TPX00094)

<div style="page-break-after: always;"></div>

## Ratings

### Recommended Operating Conditions

<p style="text-align: justify;">
The table below provides a comprehensive guideline for the optimal use of the Arduino Portenta Mid Carrier, outlining typical operating conditions and design limits. The operating conditions of the Carrier are largely based on the specifications of its components.
</p>

<div style="text-align:center;">

|           **Parameter**          |    **Symbol**   | **Min** | **Typ** | **Max** | **Unit** |
|:--------------------------------:|:---------------:|:-------:|:-------:|:-------:|:--------:|
|     USB Supply Input Voltage     | V<sub>USB</sub> |    -    |   5.0   |    -    |     V    |
| Supply Input Voltage<sup>1</sup> |  V<sub>IN</sub> |    -    |   5.0   |    -    |     V    |
|       Operating Temperature      |  T<sub>OP</sub> |   -40   |    -    |    85   |    °C    |

</div>

<sup>1</sup> Portenta Mid Carrier powered through its onboard screw terminal block (IN 5V terminal) or its breakout pins header connector (IN 5V pins).

<div style="page-break-after: always;"></div>

## Functional Overview

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier is a powerful tool for developing scalable Portenta-based applications, offering quick access to all high-density signals. It enables expansion with Ethernet and mPCIe connectors and booting from external sources via the microSD card slot. Interacting with actuators is made easy with onboard CAN bus lines, and it supports industrial machine vision with camera connectors. The Carrier also provides a solid base for creating proprietary hardware, streamlining the development process for various projects.
</p>

### Pinout 

The Portenta Mid Carrier pinout is shown in the figure below.

![](assets/Portenta_Mid_Carrier_Pinout.png)

<div style="page-break-after: always;"></div>

### Block Diagram

An overview of the high-level architecture of the Portenta Mid Carrier is illustrated in the figure below.

![](assets/Portenta_Mid_Carrier_Block_Diagram.png)

<div style="page-break-after: always;"></div>

### Power Supply

<div style="text-align:justify;">

The Portenta Mid Carrier can be powered through one of these interfaces:

- **Onboard USB-C® port of the Portenta board**: Provides a convenient way to power the board using standard USB-C® cables and adapters. 
- **External +5 VDC power supply**: This can be connected to the IN 5V pin of the Carrier's screw terminal block; it can also be connected to the IN 5V pins of the breakout header connectors. 

![](assets/Portenta_Mid_Carrier_Power_Tree.png)

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<strong>Reverse polarity protection:</strong> IN 5V pins of the Carrier's screw terminal block and breakout header connectors <strong> do not have</strong> reverse polarity protection. Double-check the polarity of your power supply before connecting it to the Carrier to avoid damaging it. 
</div>

</div>

<div style="background-color: #FFCCCC; border-left: 6px solid #FF0000; margin: 20px 0; padding: 15px;">
<strong>Safety note:</strong> Disconnect power before modifying the Carrier connections and configurations to avoid short-circuiting. For more safety tips, refer to the Carrier's user manual.
</div>

</div>

<div style="page-break-after: always;"></div>

## Device Operation

<div style="text-align:justify;">

### Getting Started - IDE

If you want to program your Arduino Portenta Mid Carrier with any of the Portenta family boards offline, install the Arduino® Desktop IDE **[1]**. To connect the Portenta family board to your computer, you will need a USB-C® cable.

### Getting Started - Arduino Web Editor

All Arduino® devices work out of the box on the Arduino® Web Editor **[2]** by installing a simple plugin. The Arduino® Web Editor is hosted online. Therefore, it will always be up-to-date with all the latest features and support for all boards and devices. Follow **[3]** to start coding on the browser and upload your sketches onto your device.

### Getting Started - Arduino Cloud

All Arduino® IoT-enabled products are supported on Arduino Cloud, which allows you to log, graph, and analyze sensor data, trigger events, and automate your home or business. Take a look at the official documentation to know more.

### Sample Sketches

Sample sketches for the Portenta family boards can be found either in the “Examples” menu in the Arduino® IDE or the “Portenta Family” section of Arduino documentation **[4]**.

### Online Resources

Now that you have gone through the basics of what you can do with the device, you can explore the endless possibilities it provides by checking exciting projects on ProjectHub **[5]**, the Arduino® Library Reference **[6]**, and the online store **[7]** where you will be able to complement your Portenta Mid Carrier with additional extensions, sensors, and actuators.
</div>

<div style="page-break-after: always;"></div>

## Mechanical Information

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier is a double-sided 114 mm x 86.5 mm board with several connectors overhanging its edges. Portenta family boards and mPCIE cards are placed inside the Carrier using dedicated connectors. 
</p>

### Carrier Dimensions

The Portenta Mid Carrier board outline and mounting hole dimensions are shown in the figure below; all the dimensions are in mm. 

![](assets/Portenta_Mid_Carrier_Outline.png)

The Carrier has four 2.7 mm drilled mounting holes for mechanical fixing.

### Carrier Connectors

Connectors of the Portenta Mid Carrier are placed primarily on its edges, but there are also some connectors placed inside of the Carrier;  their placement is shown in the figure below. All the dimensions are in mm. 

![](assets/Portenta_Mid_Carrier_Connectors.png)

## Product Compliance

### Product Compliance Summary

| **Product Compliance** |
| :--------------------: |
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

| **Company name** |                **Arduino S.r.l.**               |
|:----------------:|:--------------------------------------------:|
|  Company address | Via Andrea Appiani, 25 - 20900 MONZA (Italy) |

## Reference Documentation
|        **Ref**                     | **Link**                                                                                    |
|:----------------------------------:|---------------------------------------------------------------------------------------------|
| Arduino IDE (Desktop)              | https://www.arduino.cc/en/Main/Software                                                     |
| Arduino IDE (Cloud)                | https://create.arduino.cc/editor                                                            |
| Arduino Cloud - Getting started    | https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started             |
| Nano Matter Documentation         | https://docs.arduino.cc/hardware/nano-matter                                               |
| Project Hub                        | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending                    |
| Library Reference                  | https://www.arduino.cc/reference/en/                                                        |
| Online Store                       | https://store.arduino.cc/                                                                   |
         

## Document Revision History

|  **Date**  | **Revision** |        **Changes**        |
| :--------: | :----------: | :-----------------------: |
| 21/03/2024 |      1       | Community Preview Release |