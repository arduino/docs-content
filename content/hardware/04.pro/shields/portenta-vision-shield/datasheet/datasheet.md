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
  - **Perimeter surveillanc**e: Implement the Portenta Vision Shield in perimeter security to detect intrusions or breaches, triggering immediate responses and minimizing risks.

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

## Functional Overview

<p style="text-align: justify;">The core of the Portenta Vision Shield is its integration with the Portenta family boards, leveraging their processing power for advanced vision and audio applications. The Portenta Vision Shield is equipped with key peripherals, such as dual MEMS microphones (MP34DT06J) and a high-performance camera module (HM0360), all directly interfaced with the main Portenta family board. Two different variants of the shield offer advanced connectivity capabilities, via Ethernet (variant SKU: ASX00021) and via LoRa® variant (SKU: ASX00026).</p>

### Pinout

The high-density connector pinout for the Portenta Vision Shield Ethernet variant (SKU: ASX00021) is shown in the figure below.

The high-density connector pinout for the Portenta Vision Shield LoRa® variant (SKU: ASX00026) is shown in the figure below.

<div style="page-break-after: always;"></div>

### Block Diagram

An overview of the high-level architecture of the Portenta Vision Shield Ethernet variant (SKU: ASX00021) is illustrated in the figure below.

An overview of the high-level architecture of the Portenta Vision Shield LoRa® variant (SKU: ASX00026) is illustrated in the figure below.

<div style="page-break-after: always;"></div>

### Power Supply

<p style="text-align: justify;">The Portenta Vision Shield is powered exclusively through the VCC pins (+3V3) of its High Density Connectors. These connectors are designed to be used with boards from the Portenta family, such as the Portenta H7 board (any variant) or the Portenta C33 board. The power is supplied directly from the connected Portenta family board, which acts as the power source for the Portenta Vision Shield.</p>

The detailed figure below illustrates the power architecture of the Portenta Vision Shield.

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

<p style="text-align: justify;">The Portenta Vision Shield is a double-sided board measuring 67.07 x 25.39 mm. It features an RJ45 connector that overhangs the top edge (present only in the Ethernet variant, SKU: ASX00021), an onboard camera positioned near the center of the board, and a LoRa® module located near the bottom edge (only in the LoRa® variant, SKU: ASX00026). Additionally, the shield includes two High-Density connectors at the bottom edge, enabling quick and efficient integration with Portenta Family boards.</p>

### Board Dimensions

<p style="text-align: justify;">The outline and mounting hole dimensions of the Portenta Vision Shield are shown in the figure below, with all measurements in millimeters (mm).</p>

### Board Connectors

Connectors of the Portenta Vision Shield are placed on the top and bottom side of the shield; their placement are shown in the figures below; all the dimensions are in mm.
