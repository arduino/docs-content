---
identifier: ABX00074
title: Arduino® Portenta C33
type: pro
---

![](assets/portenta-c33-top-view.png)

# Description 

<p style="text-align: justify;">The Portenta C33 is a powerful System-on-Module designed for low-cost Internet of Things (IoT) applications. Based on the R7FA6M5BH2CBG microcontroller from Renesas®, this board shares the same form factor as the Portenta H7 and it is backward compatible with it, making it fully compatible with all Portenta family shields and carriers through its high-density connectors. As a low-cost device, the Portenta C33 is an excellent choice for developers looking to create IoT devices and applications on a budget. Whether you're building a smart home device or a connected industrial sensor, the Portenta C33 provides the processing power and connectivity options you need to get the job done.</p>

# Target Areas

IoT, building automation, smart cities, and agriculture

# CONTENTS
## Application Examples

<div style="text-align:justify;">
Thanks to its high-performance processor, the Portenta C33 supports many applications. From industrial applications to rapid prototyping, IoT solutions, and building automation, among many others. Here are some examples: 

- **Industrial Automation:** The Portenta C33 can be implemented as a solution for different industrial applications:
    - **Industrial IoT gateway:** Connect your devices, machines, and sensors to a Portenta C33 gateway. Collect operation data in real-time and display them on the Arduino IoT Cloud dashboard, leveraging end-to-end secure data encryption.
    - **Machine monitoring to track OEE/OPE:** Track Overall Equipment efficiency (OEE) and Overall Process Effectiveness (OPE) with Portenta C33 as an IoT node. Collect data and get alerted on machine uptime and unplanned downtime to provide reactive maintenance and improve production rate.
    - **Inline Quality Assurance:** Leverage full compatibility between Portenta C33 and Nicla family to carry out quality control in your production lines. Collect Nicla smart sensing data with Portenta C33 to catch defects early and resolve them before they travel down the line.
- **Prototyping:** The Portenta C33 can assist Portenta and MKR developers with their IoT prototypes by integrating ready-to-use Wi-Fi/Bluetooth® connectivity and various of peripheral interfaces, including CAN, SAI, SPI, I2C. Moreover, the Portenta C33 can be promptly programmed with high-level languages like MicroPython, allowing for rapid prototyping of IoT applications.
- **Building Automation:** The Portenta C33 can be used in multiple building automation applications:
    - **Energy Consumption Monitoring:** Collect and monitor consumption data from all services (e.g., gas, water, electricity) in a single system. Display usage trends in the Arduino IoT Cloud charts, providing an overall image for energy management optimization and cost reduction.
    - **Appliances Control System**: Leverage high-performing Portenta C33 microcontroller to real-time control your appliances. Adjust HVAC heating or improve the efficiency of your ventilation system, control the motors of your curtains, and switch on/off lights. The onboard Wi-Fi connectivity easily allows Cloud integration, so that everything is under control even from remote.
</div>

## Board Overview 

<p style="text-align: justify;">
The Portenta C33 is a powerful microcontroller board designed for low-cost IoT applications. Based on the high-performance R7FA6M5BH2CBG microcontroller from Renesas, it offers a range of key features and a low-power design that make it well-suited for a variety of applications.The board has been designed with the same form factor as the Portenta H7 and is backward compatible, making it fully compatible with all Portenta family shields and carriers through its MKR-styled and high-density connectors. Table 3 summarizes the board's main features.
</p>

<div style="text-align:center;">

|     **Feature**     | **Description**                                                                                                                                                              |
|:-------------------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Microcontroller   | 200MHz, Arm Cortex-M33 core microcontroller (R7FA6M5BH2CBG)                                                                                                                  |
|   Internal Memory   | 2MB Flash and 256kB SRAM                                                                                                                                                     |
|   External Memory   | 6MB QSPI Flash memory (MX25L12833F)                                                                                                                                          |
|     Connectivity    | 2.4GHz Wi-Fi (802.11 b/g/n) and Bluetooth® 5.0 (ESP32­-C3-­MINI-­1U)                                                                                                         |
|       Ethernet      | Ethernet physical layer (PHY) transceiver (LAN8742AI)                                                                                                                        |
|       Security      | IoT-ready secure element (SE050C2)                                                                                                                                           |
|   USB Connectivity  | USB-C port for power and data (accessible also through the board's high-density connectors)                                                                                  |
|     Power Supply    | Various options for easily powering the board: USB-C port, single cell lithium-ion/lithium-polymer battery and external power supply connected through MKR-styled connectors |
|  Analog Peripherals | Two, eight channel 12-bit analog-to-digital converter (ADC) and two 12-bit digital-to-analog converter (DAC)                                                                 |
| Digital Peripherals | GPIO (x7), I2C (x1), UART (x4), SPI (x2), PWM (x10), CAN (x2), I2S (x1), SPDIF (x1), PDM (x1), and SAI (x1)                                                                  |
|      Debugging      | JTAG/SWD debug port (accessible through the board's high-density connectors)                                                                                                 |
|      Dimensions     | 66.04mm x 25.40mm                                                                                                                                                            |
|    Surface-mount    | Castellated pins allow the board to be positioned as a surface-mountable module                                                                                              |

**<caption>Table 1: Portenta C33 main features</caption>**
</div>

[comment]: <> (Force page break here) 
[comment]: <> (<div style="page-break-after: always;"></div>)


### Microcontroller

<table>
<thead>
  <tr>
    <th>Component</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="6">R7FA6M5BH2CBG</td>
    <td>32-bit Arm Cortex-M33 microcontroller, with a maximum operating frequency of 200 MHz</td>
  </tr>
  <tr>
    <td>2 MB of flash memory and 256 KB of SRAM</td>
  </tr>
  <tr>
    <td>Several peripheral interfaces, including UART, I2C, SPI, USB, CAN, and Ethernet</td>
  </tr>
  <tr>
    <td>Hardware-based security features, such as a True Random Number Generator (TRNG), a Memory Protection Unit (MPU), and a TrustZone-M security extension.</td>
  </tr>
  <tr>
    <td>Onbaord power management features that allow it to operate on low power.</td>
  </tr>
  <tr>
    <td>Designed to operate over a wide temperature range, from -40°C to 105°C, making it suitable for use in harsh environments.</td>
  </tr>
</tbody>
</table>

### Communication

<table>
<thead>
  <tr>
    <th>Component</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">ESP32­-C3-­MINI-­1U</td>
    <td>2.4 GHz Wi­Fi (802.11 b/g/n) support</td>
  </tr>
  <tr>
    <td>Bluetooth® 5.0 support</td>
  </tr>
</tbody>
</table>

### Security

<table>
<thead>
  <tr>
    <th>Component</th>
    <th>Details</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="6">NXP SE050C2</td>
    <td>Secure boot process that verifies the authenticity and integrity of the firmware before it is loaded into the device</td>
  </tr>
  <tr>
    <td>Built-in hardware cryptography engine that can perform various encryption and decryption functions, including AES, RSA, and ECC.</td>
  </tr>
  <tr>
    <td>Secure storage for sensitive data, such as private keys, credentials, and certificates. This storage is protected by strong encryption and can only be accessed by authorized parties.</td>
  </tr>
  <tr>
    <td>Secure communication protocols support, such as TLS, which helps to protect data in transit from unauthorized access or interception.</td>
  </tr>
  <tr>
    <td>Tamper detection features that can detect if the device has been physically tampered with. This helps to prevent attacks such as probing or power analysis attacks that attempt to access the device's sensitive data.</td>
  </tr>
  <tr>
    <td>Common Criteria security standard certification, which is an internationally recognized standard for evaluating the security of IT products.</td>
  </tr>
</tbody>
</table>

### Included Accesories 

- Wi-Fi W.FL antenna (not compatible with Portenta H7 U.FL antenna)

### Related Products

- ESLOV connector
- Arduino® Portenta H7 (SKU: ABX00042)
- Arduino® Portenta H7 Lite (SKU: ABX00045)
- Arduino® Portenta H7 Lite Connected (SKU: ABX00046)
- Arduino® Nicla Sense ME (SKU: ABX00050)

  
## Specifications

### Recommended Operating Conditions 

<p style="text-align: justify;">
Table 2 provides a comprehensive guideline for the optimal use of the Portenta C33, outlining typical operating conditions and design limits. The operating conditions of the Portenta C33 are largely a function of the operating conditions specified by its components.
</p>

<div style="text-align:center;">

|         **Parameter**        |    **Symbol**   | **Min** | **Typ** | **Max** | **Unit** |
|:----------------------------:|:---------------:|:-------:|:-------:|:-------:|:--------:|
|   USB Supply Input Voltage   | V<sub>USB</sub> |    -    |   5.0   |    -    |     V    |
| Battery Supply Input Voltage | V<sub>USB</sub> |   -0.3  |   3.7   |   4.8   |     V    |
|     Supply Input Voltage     |  V<sub>IN</sub> |   4.1   |   5.0   |   6.0   |     V    |
|     Operating Temperature    |  T<sub>OP</sub> |   -40   |    -    |    85   |    °C    |

**<caption>Table 2: Recommended Operating Conditions</caption>**
</div>

### Current Consumption

<p style="text-align: justify;">
The operating current of the Portenta C33 depends greatly on the application. Table 3 summarizes the board's power consumption in a defined application and conditions.
</p>

<div style="text-align:center;">

|       **Parameter**       |    **Symbol**   |                                **Condition**                                | **Typ** | **Unit** |
|:-------------------------:|:---------------:|:---------------------------------------------------------------------------:|:-------:|:--------:|
| Board Current Consumption | I<sub>TOT</sub> | V<sub>BAT</sub>=3.7V, USB cable disconnected, all peripherals in sleep mode |    -    |     -    |

**<caption>Table 3: Power Consumption in a Defined Application and Conditions</caption>**
</div>


*<p style="text-align: justify;">**Note**: Current consumption measurements were taken under controlled laboratory conditions, with the Portenta C33 running a specific application and connected to a specific power source. Results may vary depending on the application and operating conditions.</p>*

[comment]: <> (Force page break here) 
<div style="page-break-after: always;"></div>

## Hardware

<p style="text-align: justify;">
The core of the Portenta C33 is the R7FA6M5BH2CBG microcontroller from Renesas. The board also contains several peripherals connected to its microcontroller. 
</p>

### Block Diagram

An overview of the Portenta C33 high-level architecture is illustrated in Figure 2.

**![Figure 1. High-level architecture of the Portenta C33](assets/Portenta_C33_Block_Diagram.svg)**

### Power Supply 

The Portenta C33 can be powered through one of these interfaces:

- USB-C port
- 3.7V single cell lithium-ion/lithium-polymer battery, connected through the onboard battery connector
- External 5V power supply connected through the MKR-styled pins

The figure below shows the power options available on the board and illustrates its power architecture. 

### Mechanical Specification

#### Board Dimensions 

**![Figure 3. Portenta C33 dimensions (top view)](assets/portentaC33_mechanical_top.svg)**

**![Figure 4. Portenta C33 dimensions (bottom view)](assets/portentaC33_mechanical_bot.svg)**

## Certifications

### Certifications Summary

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
|    SRRC (China)   |     Yes    |
|    CCC (China)    |     Yes    |

### Declaration of Conformity CE DoC (EU)
We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).

### Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.

| Substance                              | **Maximum limit (ppm)** |
|----------------------------------------|-------------------------|
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

Exemptions: No exemptions are claimed.

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration
As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

## FCC Caution
Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

(1) This device may not cause harmful interference

(2) this device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator & your body.

English:
User manuals for license-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual or alternatively on the device or both. This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions:

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

## Company Information

| Company name    | Arduino SRL                                     |
|-----------------|-------------------------------------------------|
| Company Address | Via Andrea Appiani, 25 - 20900 MONZA（Italy)    |
## Document Revision History

| Date       | **Revision** | **Changes**                        |
|------------|--------------|------------------------------------|
| 13/03/2023 | 1            | First release                      |

