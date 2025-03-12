---
identifier: TPX00095-TPX00096-TPX00097
title: WisGate Edge Pro
type: pro
variant: 'Collective Datasheet'
author: Julián Caro Linares
---

![](assets/featured.png)

# Description

The WisGate Edge Pro gateway, featuring RAKWirelessTM technology, is designed for professional applications using LoRa® technology.

Different models (SKU) are compatible with three radio frequency bands adopted in different regions: Europe, United States, Australia and New Zealand*.

# Target Areas

Lora, Industrial, Professional IoT

# Contents

## Features
### General Specifications Overview

<!---
General Specifications Overview: This section covers the main technical descriptions and a full summary of the main technical specifications of the product. The section normally starts with another descriptive 3/4 lines paragraph this time focused mostly on the technical features of the product plus a table with its main technical specifications. It is important to note that this section and the following related one where the product specifications are broken down into detail in new sections and tables hugely vary from product to product, being really important to cover all the main technical features of each product properly. That info will be expanded later in the specific sections related to that feature. The actual text and the following table are intended for example purposes.
-->

The Portenta C33 is a powerful microcontroller board designed for low-cost IoT applications. Based on the high-performance R7FA6M5BH2CBG microcontroller from Renesas®, it offers a range of key features and a low-power design that make it well-suited for a variety of applications. The board has been designed with the same form factor as the Portenta H7 and is backward compatible, making it fully compatible with all Portenta family shields and carriers through its MKR-styled and high-density connectors. The following table summarizes the board's main features.


| Feature               | Description                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| Computing Unit        | MT7628                                                                  |
| RAM Memory            | DDR2 RAM 128 MB                                                         |
| Operating temperature | -30 ºC to +55 ºC                                                        |
| Wi-Fi®                | 2.4 GHz (802.11 bgn), TODO                     |
| PWM Pins              | PWM Pins with 8 bits resolution (x13)                                   |
| Secure Element        | ATECC608A-MAHDA-T Module (x1)                                           |
| Communication         | UART (x4), I2C (x3), SPI (x2), CAN (external transceiver required) (x1) |
| Camera                | 20 pin Arducam camera connector                                         |
| Display               | D1N, D0N, D1P, D0P, CKN, CKP, D68-D75                                   |
| Audio                 | 3-pins Audio Jack Connector                                             |
| Power                 | Input voltage (VIN): 6-24 V / DC Current per I/O Pin: 8 mA              |
| Dimensions            | 114 mm x 86.5 mm                                                        |
| Weight                | 67 g                                                                    |
| Operating Temperature | -40 °C to +85 °C                                                        |
| Certifications        | CE, FCC, IC, RoHS, REACH, UKCA, WEEE, Japan (No Radio)                  |


| Feature                                       | Description                                                                                                                                                                                                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Computing                                     | MT7628, DDR2 RAM 128 MB                                                                                                                                                                                                                |
| Wi-Fi Features                                | Frequency: 2.4 GHz (802.11b / g / n)  2x2 MIMO  RX Sensitivity: ﹣95 dBm (Min)  TX Power: 20 dBm (Max)  Operation channels: 2.4 GHz: 1-13                                                                                              |
| LoRa Features                                 | SX1303 mPCIe card (connects maximum of two)  8 Channels (16 channels optional)  RX Sensitivity: ﹣139 dBm (Min)  TX Power: 17 dBm (Max)  Listen Before Talk  Frequency: EU868, IN865, US915, AU915, KR920, AS923-1/2/3/4, EU433, CN470 |
| Cellular Features (available with RAK7289CV2) | Nano SIM Card: 12.30 mm x 8.80 mm x 0.67 mm  Plus                                                                                                                                                                                      |
| ETH                                           | RJ45 (10/100 M)                                                                                                                                                                                                                        |
| Antenna                                       | LoRa: N-Type connector (one for the 8-channel gateway and two for the 16-channel gateway)  Wi-Fi / GPS / LTE: Internal antenna                                                                                                         |
| Ingress protection                            | IP67                                                                                                                                                                                                                                   |
| Enclosure material                            | Aluminium and plastic                                                                                                                                                                                                                  |
| Dimensions                                    | 240 mm x 240 mm x 89.5 mm                                                                                                                                                                                                              |
| Weight                                        | 4.6 kg Gateway only                                                                                                                                                                                                                    |
| Operating temperature                         | ﹣30˚ C to ﹢55˚ C                                                                                                                                                                                                                     |
| Storage Temperature                           | ﹣40˚ C to ﹢85˚ C                                                                                                                                                                                                                     |
| Operating humidity                            | 0% to 95% (non-condensing)                                                                                                                                                                                                             |
| Storage Humidity                              | 0% to 95% (non-condensing)                                                                                                                                                                                                             |
| Installation Method                           | Pole or wall mounting                                                                                                                                                                                                                  |


### Microcontroller

<!---
Subsection about a Main Feature: The subsection inside features and under General Specification Overview to talk about some of the main features of the product, from the microprocessor's main specifications to the wifi chipset, Camera, Audio, Important Interfaces like CAN, etc. Ideally those sections should contain an initial 2/3 line paragraph, a table or multiple tables explaining the main specs and related media like images or schemas to explain better the technical specifications. Warnings and Note blocks regarding special things of the feature to take into account are also recommended it.
-->

| Component                | Details                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| ST STM32H747XI Processor | Dual-core Arm® Cortex®-M7 core at up to 480 MHz + Arm® 32-bit Cortex®-M4 core at up to 240 MHz |
| Flash Memory             | 2 MB of Flash Memory with read-while-write support                                             |
| Programming Memory       | 1 MB of RAM                                                                                    |

### Inputs

<!---
Subsection about a Main Feature: The subsection inside features and under General Specification Overview talks about some of the main features of the product, from the microprocessor's main specifications, to the wifi chipset, Camera, Audio, Important Interfaces like CAN, etc. Ideally those sections should contain an initial 2/3 line paragraph, a table or multiple tables explaining the main specs and related media like images or schemas to explain better the technical specifications. Warnings and Note blocks regarding special things of the feature to take into account are also recommended.
-->

| Characteristics               | Details                  |
| ----------------------------- | ------------------------ |
| Number of inputs              | 8x Analog/Digital inputs |
| Inputs overvoltage protection | yes                      |
| Antipolarity protection       | yes                      |
| Input impedance               | 8.9 kΩ                   |

### Outputs

<!---
Subsection about a Main Feature: The subsection inside features and under General Specification Overview talks about some of the main features of the product, from the microprocessor's main specifications, to the wifi chipset, Camera, Audio, Important Interfaces like CAN, etc. Ideally those sections should contain an initial 2/3 line paragraph, a table or multiple tables explaining the main specs and related media like images or schemas to explain better the technical specifications. Warnings and Note blocks regarding special things of the feature to take into account are also recommended it.
-->

| Characteristics                       | Details                                          |
| ------------------------------------- | ------------------------------------------------ |
| Number of outputs                     | 4x relays (NO)                                   |
| Max current per relay                 | 10 A                                             |
| Max peak current per relay            | 15 A                                             |
| Continuous current per terminal       | 10 A                                             |
| Short-circuit protection              | No, external fuse required                       |
| Relay rated voltage                   | 250 VAC                                          |
| Relay Max voltage                     | 400 VAC                                          |
| Rated load AC1                        | 2500 VA                                          |
| Rated load AC15 (230 VAC)             | 500 VA                                           |
| Breaking capacity DC1: 24/30/110/220V | 10/4/0.3/0.12 A                                  |
| Minimum switching load                | 300 mW (5 V/5 mA)                                |
| Max output line length (unshielded)   | 100 m                                            |
| Relay response time from state 0 to 1 | 6 ms for relay output                            |
| Relay response time from state 1 to 0 | 4 ms for relay output                            |
| Bounce time NO                        | 3 ms                                             |
| Bounce time NC                        | 6 ms                                             |
| Relay mechanical durability           | 10 million cycles                                |
| Relay electrical durability           | 10 thousand cycles with a resistive load of 10 A |




### Communication

<!---
Subsection about a Main Feature: The subsection inside features and under General Specification Overview talks about some of the main features of the product, from the microprocessor's main specifications, to the wifi chipset, Camera, Audio, Important Interfaces like CAN, etc. Ideally those sections should contain an initial 2/3 line paragraph, a table or multiple tables explaining the main specs and related media like images or schemas to explain better the technical specifications. Warnings and Note blocks regarding special things of the feature to take into account are also recommended.
-->

| Interfaces            | Type                                       | Protocols/Technologies supported                     |
| --------------------- | ------------------------------------------ | ---------------------------------------------------- |
| Ethernet              | 10/100BASE-T Port                          | TCP/IP, MODBUS TCP                                   |
| RS-485                | Half-duplex without termination resistance | MODBUS RTU, Custom serial communication              |
| Wireless connectivity | Wi-Fi®                                     | 2.4 GHz                                              |
| Wireless connectivity | Bluetooth® Low Energy                      | 4.2 supported by firmware, 5.1 supported by hardware |


### Security

<!---
Subsection about a Main Feature: The subsection inside features and under General Specification Overview talks about some of the main features of the product, from the microprocessor's main specifications, to the wifi chipset, Camera, Audio, Important Interfaces like CAN, etc. Ideally those sections should contain an initial 2/3 line paragraph, a table or multiple tables explaining the main specs and related media like images or schemas to explain better the technical specifications. Warnings and Note blocks regarding special things of the feature to take into account are also recommended.
-->

| Component                   | Details                                                           |
| --------------------------- | ----------------------------------------------------------------- |
| ATECC608B Crypto Microchip® | Cryptographic co-processor with secure hardware-based key storage |
|                             | Protected storage for up to 16 Keys, certificates, or data        |
|                             | Networking key management support                                 |
|                             | Secure boot support                                               |
|                             | Guaranteed unique 72-bit serial number                            |


## Accessories (<included / not included>)

<!---
Accessories: This section lists some of the related accessories that come or not with the product, like USB cables, antennas or batteries. It is important to put in whether the accessory is included or not. Actual items only for purposes examples.
-->

- Micro UFL antenna (Included)
- USB-C® cable (Not included)
- USB 2.0 Type-A cable (Not included)

## Related Products

<!---
Related products: This section lists some of the related products like shields or others. Ask and align with the Project Manager responsible for the product and check the sales brief. It is important to put the SKU of each item. Actual items are only for example purposes.
-->

- Arduino Mega Proto Shield Rev3 (A000080)
- Arduino 4 Relays Shield (A000110)
- Arduino Motor Shield Rev3 (A000079)

## Rating

<!---
Rating: This section is really important from the technical point of view, containing important information regarding the minimum and maximum values of this like voltage and current. The better the information is, the fewer support tickets the company will receive due to burn boards.
-->


### Recommended Operating Conditions

<!---
Recommended Operating Conditions/Power Specifications: This section contains the minimum, typical and Maximum main values, normally related to voltage, current and temperature, but there can be additional specifications depending on the product. Table for example purposes. Warnings or Notes are recommended in case the product needs them to make sure the user does not commit mistakes.
-->

| Description                 | Value                     |
| --------------------------- | ------------------------- |
| Temperature Operating Range | -20...50 °C               |
| Protection degree rating    | IP20                      |
| Pollution degree            | 2 conforming to IEC 61010 |

**Note:** V<sub>DD</sub> controls the logic level and is connected to the 3.3V power rail. V<sub>AREF</sub> is for the analog logic.

### Power Specification

<!---
Recommended Operating Conditions/Power Specifications: This section contains the minimum, typical and Maximum main values, normally related to voltage, current and temperature, but there can be additional specifications depending on the product. Table for example purposes. Warnings or Notes are recommended in case the product needs them to make sure the user does not commit mistakes.
-->

| Property               | Min   | Typ | Max  | Unit |
|----------------------- |------ |-----|------|------|
| Supply voltage         | 12    | -   | 24   | V    |
| Permissible range      | 10.2  | -   | 27.6 | V    |
| Power consumption (12V)| 0.6   | -   | 2    | W    |
| Power consumption (24V)| 0.6   | -   | 2.2  | W    |

### Current Consumption

<!---
Current Consumption: This section contains information about the current consumption of the product. This information is really useful but always tricky to get and can help users understand the real estimated current consumption in different scenarios like sleep modes.
-->

| Parameter                                       | Symbol         | Min | Typ | Max | Unit |
| ----------------------------------------------- | -------------- | --- | --- | --- | ---- |
| Deep Sleep Mode Current Consumption<sup>1</sup> | I<sub>DS</sub> | -   | 86  | -   | µA   |
| Normal Mode Current Consumption<sup>2</sup>     | I<sub>NM</sub> | -   | 180 | -   | mA   |


## Functional Overview

<!---
Functional Overview: The functional overview contains important information about the product in terms of pinout, block diagram, mechanical information, power tree and much more. Sections and text for example purposes.
-->

### Pinout

<!---
Pinout: It is always interesting to show the pinout of the product inside the datasheet. Pinout and text for example purposes.
-->

The Portent Hat Carrier pinout is shown in the following figure.

![Portenta Hat Carrier pinout](assets/phc-pinout.png)

<!---
Notes and warnings: If the product has some important tips to take into account regarding its pins it can be a good idea to put that information as a warning. Note code for example purposes
-->

<div style="background-color: #FFCCCC; border-left: 6px solid #FF0000; margin: 20px 0; padding: 15px;">
<strong>Safety Note:</strong> Disconnect power before board modifications. Avoid short-circuiting. Refer to the full guide for more safety tips.
</div>

### Full Pinout Table

<!---
Full Pinout Table: The full pinout tables are done only necessary in case of really complex products intended for the professional sector. These tables are extracted from the Pinout Table Spreadsheet normally done before the graphical simple pinout and used as an internal tool. Following text and tables for example purposes.
-->

The full pinout of the Portenta Hat Carrier is available in the following tables sorted by element/connector.

#### 16-Pin Header (J6)


<div style="text-align:center;">

| Pin number | Silkscreen |   Power Net   | Portenta HD Standard Pin |                           High-Density Pin                           |    Interface     |
| :--------: | :--------: | :-----------: | :----------------------: | :------------------------------------------------------------------: | :--------------: |
|     1      |     A0     |               |        ANALOG_A0         |                                J2-73                                 |                  |
|     2      |     A1     |               |        ANALOG_A1         |                                J2-75                                 |                  |
|     3      |     A2     |               |        ANALOG_A2         |                                J2-77                                 |                  |
|     4      |     A3     |               |        ANALOG_A3         |                                J2-79                                 |                  |
|     5      |     A4     |               |        ANALOG_A4         |                                J2-74                                 |                  |
|     6      |     A5     |               |        ANALOG_A5         |                                J2-76                                 |                  |
|     7      |     A6     |               |        ANALOG_A6         |                                J2-78                                 |                  |
|     8      |     A7     |               |        ANALOG_A7         |                                J2-80                                 |                  |
|     9      |    PWM7    |               |          PWM_7           |                                J2-64                                 |                  |
|     10     |    PWM8    |               |          PWM_8           |                                J2-66                                 |                  |
|     11     |   LICELL   |               |          LICELL          |                                 J2-7                                 | RTC Power Source |
|     12     |    PWM4    |               |          GPIO_0          |                                J2-46                                 |                  |
|     13     |    3V3     | +3V3_PORTENTA |           VCC            |                      J2-23, J2-34, J2-43, J2-69                      |                  |
|     14     |    TX2     |               |        SERIAL2_TX        |                                J2-26                                 |    UART 2 TX     |
|     15     |    GND     |      GND      |           GND            | J1-22, J1-31, J1-42, J1-47, J1-54, J2-24, J2-33, J2-44, J2-57, J2-70 |                  |
|     16     |    RX2     |               |        SERIAL2_RX        |                                J2-28                                 |    UART 2 RX     |

<caption>Table 6: 16-Pin Header (J6) pinout</caption>

</div>

<!---
Div page break tags: Sometimes the format is not perfect and some sections are added/cut in the pages we do not want to. This kind of div page break tag can be used to fix those problems
-->

<div style="page-break-after: always;"></div>


#### Power Block CAN Bus (J9)

<div style="text-align:center;">

| Pin number | Silkscreen  |  Power Net   | Portenta HD Standard Pin |                           High-Density Pin                           |   Interface    |
| :--------: | :---------: | :----------: | :----------------------: | :------------------------------------------------------------------: | :------------: |
|     1      | VIN 7-32VDC | INPUT_7V-32V |                          |                                                                      |                |
|     2      |     GND     |     GND      |           GND            | J1-22, J1-31, J1-42, J1-47, J1-54, J2-24, J2-33, J2-44, J2-57, J2-70 |                |
|     3      |     GND     |     GND      |           GND            | J1-22, J1-31, J1-42, J1-47, J1-54, J2-24, J2-33, J2-44, J2-57, J2-70 |                |
|     4      |     5V      |     +5V      |           VIN            |                  J1-21, J1-24, J1-32, J1-41, J1-48                   |                |
|     5      |    CANH     |              |                          |                          J1-49 (Through U1)                          | CAN BUS - CANH |
|     6      |    CANL     |              |                          |                          J1-51 (Through U1)                          | CAN BUS - CANL |

<caption>Table 7: Power Block CAN Bus (J9) pinout</caption>

</div>

<div style="page-break-after: always;"></div>


### Block Diagram

<!---
Block Diagram: The block diagram is really important from the technical point of view and for certification purposes. Must be good and consistent with Arduino`s visual style. The raw diagram is created by the R&D team and adapted and converted to the final one by the content team using Figma. Clock signals are mandatory for certification purposes. Diagram and text for example purposes.
-->

The block diagram with the main parts of the product can be checked in the following image:

![Arduino GIGA R1 WiFi Block Diagram](assets/GIGA_R1_WiFi_Block_Diagram.png)

### Power Supply

<!---
Power tree: The power tree is really important from the technical point of view and for certification purposes. Must be good and consistent with Arduino`s visual style. The raw diagram is created by the R&D team and adapted and converted to the final one by the content team using Figma. Diagram and text for example purposes.
-->

The Portenta C33 can be powered through one of these interfaces:

- USB-C® port
- 3.7 V single-cell lithium-ion/lithium-polymer battery, connected through the onboard battery connector
- External 5 V power supply connected through the MKR-styled pins

The recommended minimum battery capacity is 700 mAh. The battery is connected to the board via a disconnectable crimp-style connector as shown in Figure 3. The battery connector part number is BM03B-ACHSS-GAN-TF(LF)(SN). 

The following diagram shows the power options available on the Portenta C33 and illustrates the main system power architecture.
</div>

![Power architecture of the Portenta C33](assets/Portenta_C33_Power_Tree.svg)


### Product Topology

<!---
Product Topology: Product topology is an important section of the datasheet and a combination of two elements: the diagram with the main components references, and the table listing and describing those main components. It is important to describe only the components interesting for the final user, so capacitors, resistors and other passive components should not be described in this section as a general rule. Image and text for example purposes
-->

![Top View of Arduino GIGA R1 WiFi](assets/gigaR1WiFiTop.png)

| **Ref.** | **Description**                         | **Ref.** | **Description**                     |
|----------|-----------------------------------------|----------|-------------------------------------|
| U1       | STM32H7 Dual Core Microcontroller IC    | U8       | AT25SF128A-MHB-T 16 MB Flash IC     |
| U3       | AS4C4M16SA 8MB SDRAM IC                 | U4       | ATECC608A-MAHDA-T Secure Element IC |
| U5       | LBEE5KL1DX-883 Wi-Fi®/Bluetooth® Module | U6       | MP2322GQH Buck Converter 3.3V IC    |
| U7       | MP2269GD-Z Buck Converter 5V IC         | JANALOG  | Analog input/output headers         |
| JDIGITAL | Digital input/output headers            | JSIDE    | Digital input/output headers        |
| SPI      | SPI headers                             | JTAG     | JTAG Headers                        |
| J2       | USB 2.0 A Host                          | J15      | 3.5 mm audio in/out                 |
| PB1      | RESET Button                            | PB2      | BOOT0 button                        |
| J14      | Micro UFL connector                     | J5       | Camera                              |
| J6       | Camera                                  | DL1      | Power LED                           |
| DL2      | RGB SMLP34RGB2W3 Common anode LED       | J12      | CX90B-16P USB-C® connector          |

<!---
Product Topology specific subsections: Different subsections about specific features and important parts of the product can be added inside the product topology, explaining for example more information about the microprocessors, the MIPI camera connector, the GPS connectivity, the GPIO pins, JTAG connectors, USB, etc etc. Some of the Portenta Hat Carrier specific sections have been added as a nice example.
-->


#### High-Density Connectors (J1-J2)

<p style="text-align: justify;">The High-Density connectors (J1-J2) provide connectivity with the Portenta family boards. For detailed information, refer to the Portenta Hat Carrier pinout and the respective documentation for the Portenta family boards. In the following image, the Portenta X8 board High-Density connectors pinout is shown as an example.</p>

![Portenta X8 High-Density connectors pinout](assets/phc_high-density-connector-x8.png)

#### JTAG Connector (J3)

<p style="text-align: justify;">Debugging capabilities are integrated directly into the Portenta Hat Carrier and are accessible via the 10-pin JTAG connector (J3) shown in Figure 7.</p>

#### USB-A (J4)

<p style="text-align: justify;">The onboard USB-A connector (female), shown in Figure 7, is integrated into the Portenta Hat Carrier for multiple purposes, including:</p>

- Connecting external peripherals such as mouse devices, keyboards, USB cameras, hubs, and hard drives.
- Data logging using a USB memory stick.

![JTAG and USB-A connectors of the Portenta Hat Carrier](assets/portentaHatCarrier_usbjtagConnectors.png)

#### 40-Pin Header Connector (J5)

<p style="text-align: justify;">The Portenta Hat Carrier features a 40-pin header connector as shown in Figure 8, making it compatible with most of the Raspberry Pi® Hats available on the market.</p>

![Raspberry Pi®-compatible 40-pin header connector](assets/portentaHatCarrier_raspiConnector.png)

The main interfaces and general-purpose pins available through this connector include:

- SPI (x1)
- I2S (x1)
- SAI (x1)
- 5 VDC (x2)
- 3.3 VDC (x2)
- I2C (x2)
- UART (without flow control) (x2)
- PWM (x7)
- GND (x8)
- GPIO (x26)

#### MicroSD Card Slot (J7)

The onboard microSD card slot can be used for:

- Data logging operations
- Media purposes

![MicroSD card slot of the Portenta Hat Carrier](assets/portentaHatCarrier_microSDConnector.png)

## Device Operation

<!---
Device Operation: This section is the only section where we mention software-related topics, like IDEs and additional documentation, tools and resources. Normally is generic and only needs to change names and make sure citations are in order but make sure that is this way for your products. Some products are also compatible with Linux, micropython or PLC IDE.
-->

### Getting Started - IDE

If you want to program your <NAME_OF_PRODUCT> while offline you need to install the Arduino® Desktop IDE **[1]**. To connect the <NAME_OF_PRODUCT> to your computer, you will need a <CABLE_TYPE> cable, which can also provide power to the board, as indicated by the LED (DL1).

### Getting Started - Arduino Web Editor

All Arduino boards, including this one, work out-of-the-box on the Arduino® Web Editor **[2]**, by just installing a simple plugin.

The Arduino Web Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow **[3]** to start coding on the browser and upload your sketches onto your board.

### Getting Started - Arduino Cloud

All Arduino IoT enabled products are supported on Arduino Cloud which allows you to log, graph and analyze sensor data, trigger events, and automate your home or business.

### Online Resources

Now that you have gone through the basics of what you can do with the board you can explore the endless possibilities it provides by checking exciting projects on ProjectHub **[4]**, the Arduino Library Reference **[5]**, and the online store **[6]**; where you will be able to complement your board with sensors, actuators and more.

### Board Recovery

<!---
Board Recovery:  Make sure to explain how to put the board in recovery mode. If that information is not available, please remove.
-->

All Arduino boards have a built-in bootloader which allows flashing the board via USB. In case a sketch locks up the processor and the board is not reachable anymore via USB, it is possible to enter bootloader mode by double-tapping the reset button right after the power-up.

## Mechanical Information

<!---
Mechanical Information: Information related to measurements and drawings, putting special attention to the main components, connectors, holes and more. Nano Matter drawings and text as an example.
-->

<p style="text-align: justify;">
The Nano Matter is a double-sided 18 mm x 45 mm board with a USB-C® port overhanging the top edge and dual
castellated/through-hole pins around the two long edges; the onboard wireless antenna is located in the center of the bottom edge of the board.
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


## Certifications

<!---
Important legal information regarding certifications, only change the section "Certification Summary and double check with the Certification and Project Manager of the product the information written.
-->

### Certifications Summary

<!---
Certification Summary: A table including the main certification of the products. Add certifications serial names if possible.
-->

| **Certification** | **Status** |
|:-----------------:|:----------:|
|  CE/RED (Europe)  |     Yes    |
|     UKCA (UK)     |     Yes    |
|     FCC (USA)     |     Yes    |
|    IC (Canada)    |     Yes    |
| MIC/Telec (Japan) |     Yes    |
|  RCM (Australia)  |     Yes    |
|        RoHS       |     Yes    |
|       REACH       |     Yes    |
|        WEEE       |     Yes    |

### Declaration of Conformity CE DoC (EU)

<p style="text-align: justify;">We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).</p>

### Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

<p style="text-align: justify;">Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.</p>

| Substance                              | **Maximum limit (ppm)** |
|----------------------------------------|-------------------------|
| Lead (Pb)                              | 1000                    || **Date**   | **Revision** | **Changes**               |
| ---------- | ------------ | ------------------------- |
| 02/11/2023 | 2            | Flashing Mode Description |
| 25/10/2023 | 1            | First Release             |
| Poly Brominated Biphenyls (PBB)        | 1000                    |
| Poly Brominated Diphenyl ethers (PBDE) | 1000                    |
| Bis(2-Ethylhexyl) phthalate (DEHP)     | 1000                    |
| Benzyl butyl phthalate (BBP)           | 1000                    |
| Dibutyl phthalate (DBP)                | 1000                    |
| Diisobutyl phthalate (DIBP)            | 1000                    |

Exemptions: No exemptions are claimed.

<p style="text-align: justify;">Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.</p>

### Conflict Minerals Declaration

<p style="text-align: justify;">As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regard to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder or as a component in metal alloys. As part of our reasonable due diligence, Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.</p>

### FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

(1) This device may not cause harmful interference

(2) this device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator & your body.

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

(1) this device may not cause interference

(2) this device must accept any interference, including interference that may cause undesired operation of the device.

French:
Le présent appareil est conforme aux CNR d’Industrie Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes:

(1) l’ appareil nedoit pas produire de brouillage

(2) l’utilisateur de l’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

**IC SAR Warning:**

English:
This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

French:
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 2014/53/EU. This product is allowed to be used in all EU member states.

# Company Information

<!---
Company information: Make sure is updated and always the same.
-->

| Company name    | Arduino SRL                                   |
|-----------------|-----------------------------------------------|
| Company Address | Via Andrea Appiani, 25 - 20900 MONZA（Italy)  |


# Reference Documentation

<!---
Reference Documentation: Make sure the quotes this is coherent with the "Device Operation" section.
-->

| Ref                       | Link                                                                                                                                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arduino IDE (Desktop)     | [https://www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software)                                                                                                             |
| Arduino IDE (Cloud)       | [https://create.arduino.cc/editor](https://create.arduino.cc/editor)                                                                                                                           |
| Cloud IDE Getting Started | [https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor](https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor) |
| Project Hub               | [https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending](https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending)                                           |
| Library Reference         | [https://github.com/arduino-libraries/](https://github.com/arduino-libraries/)                                                                                                                 |
| Online Store              | [https://store.arduino.cc/](https://store.arduino.cc/)                                                                                                                                         |

## Revision History

<!---
Revision History: Every time there are updates or important changes a new line must be added. Always use date format: dd/mm/yyyy, put the revisions sorted by the most recent one. Put simple but descriptive information in the "Changes" column.
-->

|  **Date**  | **Revision** |                      **Changes**                       |
| :--------: | :----------: | :----------------------------------------------------: |
| 23/01/2024 |      7       |               Updated Interfaces section               |
| 14/12/2023 |      6       |            Updated Related Product section             |
| 14/11/2023 |      5       |             FCC and Block Diagram Updates              |
| 30/10/2023 |      4       |          I2C ports information section added           |
| 20/06/2023 |      3       | Power tree added, related products information updated |
| 09/06/2023 |      2       |      Board's power consumption information added       |
| 14/03/2023 |      1       |                     First release                      |
