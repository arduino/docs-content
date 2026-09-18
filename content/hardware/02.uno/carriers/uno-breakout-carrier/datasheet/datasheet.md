---
identifier: ASX00085
title: Arduino® UNO Breakout Carrier
type: maker
author: Christopher Méndez
---

![](assets/featured.png)

# Description

The Arduino UNO Breakout Carrier is designed to give developers complete, direct access to every signal available on the UNO Q’s JMEDIA and JMISC high-speed connectors. Ideal for advanced prototyping, testing, and integration work, it exposes all lines — including high-speed video, camera, audio, I²C, SPI, UART, PWM, power rails, and control signals — to clearly labeled, easy-to-use breakout headers.

# Target Areas

Rapid Prototyping, Proof of Concept, Edge AI, Research and Development

# Features

* Connectors
  * Two 2x20 Male Headers (2.54 mm)
  * Two 2x30 Male Headers (JMEDIA and JMISC 1.27 mm)
  * 1x8 through-hole pads (2.54 mm)
* Power
  * Powered from the host UNO Q
  * VIN input power rails (+7-24 VDC)
* I/O
  * I2C
  * Microphone In / Headphone Out
  * Earphone Out
  * Audio Line Out
  * PWM
  * PSSI
  * GPIO
  * SPI
  * OPAMP

# Contents

## Application Examples

**Embedded Hardware Development:** 
- **Custom Interface Boards:** Rapidly design and test custom peripherals for the Arduino UNO Q. By providing direct access to the JMEDIA and JMISC connectors, developers can seamlessly route I2C, SPI, UART, and GPIO signals to custom interface boards without the need for complex adapters or soldering.
- **Multimedia System Integration:** Leverage the comprehensive breakout of audio interfaces (HP OUT, LINE OUT, MIC IN, EAR OUT, PWM) to integrate the UNO Q into advanced multimedia and smart audio systems. The clearly labeled 2.54 mm male headers simplify wiring and testing, accelerating the development of complex embedded audio applications.
- **Rapid Hardware Prototyping:** Expand the UNO Q's capabilities by easily integrating third-party modules and external hardware components. The carrier's direct access to power rails and communication buses makes it an ideal platform for building out proofs of concept for advanced IoT, multimedia, and edge computing devices.

**R&D and Testing:**
- **Automated Lab Setups:** Build reliable, organized, and accessible automated test rigs for hardware validation. The Breakout Carrier exposes all critical UNO Q control signals to standard headers, allowing test engineers to quickly connect measurement equipment and script automated QA tests for complex systems.
- **Interface Compliance Testing:** Streamline the verification process for new system designs. Engineers can connect oscilloscopes and logic analyzers directly to the carrier’s accessible pins to probe high-speed communication buses, power rails, and PSSI interfaces, ensuring strict electrical and protocol timing compliance.
- **Mixed-Signal Debugging:** Speed up troubleshooting during product development by providing immediate, clear access to audio and control signals. Teams can isolate issues and verify signal integrity safely without the risk of damaging the main UNO Q board or fabricating temporary breakout solutions.

**Education:**
- **Hardware Prototyping Courses:** Provide a durable, reusable tool for multiple student cohorts learning to build embedded systems around a powerful Linux SBC. The straightforward 2x20 header pinout allows students to easily wire external sensors, actuators, and breadboards, fostering hands-on experimentation in STEM and project-based learning.
- **Mixed-Signal Debugging Workshops:** Facilitate practical lab exercises in university engineering programs. The Breakout Carrier bridges the gap between theory and practice, giving students clear, accessible points to probe audio inputs/outputs, I2C, and GPIO signals using standard lab equipment.
- **Advanced Embedded Linux Projects:** Accelerate cross-disciplinary student projects by simplifying the hardware-software interface. Students can focus on developing custom kernel drivers and multimedia applications on the Arduino UNO Q, using the carrier to effortlessly connect their physical hardware prototypes.


### Related Products
*   Arduino UNO Q (SKU: ABX00162 - ABX00173)

## Ratings

### Recommended Operating Conditions
|     Symbol     |         Description         |  Min  |  Typ  |  Max  | Unit  |
| :------------: | :-------------------------: | :---: | :---: | :---: | :---: |
|       T        | Conservative thermal limits |  -10  |  20   |  60   |  °C   |
| V<sub>IN</sub> | Input voltage from VIN pad  |   7   |   -   |  24   |   V   |

## Functional Overview

The UNO Breakout Carrier expands the connectivity of the Arduino UNO Q, featuring a variety of 2.54 mm male header connectors.

### Board Topology

![Top view - connectors](assets/ASX00085-topology.png)

| **Ref.** |                **Description**                |
| :------: | :-------------------------------------------: |
|   J14    |      Male header connector 2x20 2.54 mm       |
|   J15    |      Male header connector 2x20 2.54 mm       |
|  JMEDIA  | High-speed male header connector 2x30 1.27 mm |
|  JMISC   | High-speed male header connector 2x30 1.27 mm |


### Pinout

The UNO Breakout Carrier pinout is shown in the following figure.

![UNO Breakout Pinout](assets/ASX00085-simple-pinout.png)

#### J14

| Pin | Function  | Type          | Description                          |
| --- | --------- | ------------- | ------------------------------------ |
| 1   | VIN       | Power In      | Voltage Input                        |
| 2   | GPIO_20   | Digital       | SOC_CAM_MCLK0                        |
| 3   | VIN       | Power In      | Voltage Input                        |
| 4   | GPIO_21   | Digital       | SOC_CAM_MCLK1                        |
| 5   | GND       | Ground        | Ground                               |
| 6   | GND       | Ground        | Ground                               |
| 7   | +5V USB   | Power Out     | +5V USB Power Output                 |
| 8   | GPIO_23   | Digital / I2C | CCI_I2C_SCL0                         |
| 9   | +5V USB   | Power Out     | +5V USB Power Output                 |
| 10  | GPIO_22   | Digital / I2C | CCI_I2C_SDA0                         |
| 11  | GND       | Ground        | Ground                               |
| 12  | GND       | Ground        | Ground                               |
| 13  | +3V3      | Power Out     | +3.3V Power Output                   |
| 14  | GPIO_29   | Digital / I2C | CCI_I2C_SDA1                         |
| 15  | +3V3      | Power Out     | +3.3V Power Output                   |
| 16  | GPIO_30   | Digital / I2C | CCI_I2C_SCL1                         |
| 17  | GND       | Ground        | Ground                               |
| 18  | GND       | Ground        | Ground                               |
| 19  | +1V8      | Power Out     | +1.8V Power Output                   |
| 20  | MIC2_INP  | Analog        | Microphone Input Positive            |
| 21  | +1V8      | Power Out     | +1.8V Power Output                   |
| 22  | MIC2_INM  | Analog        | Microphone Input Negative            |
| 23  | GND       | Ground        | Ground                               |
| 24  | MIC2_BIAS | Analog        | Microphone Bias                      |
| 25  | GND       | Ground        | Ground                               |
| 26  | GND       | Ground        | Ground                               |
| 27  | LINEOUT_P | Analog        | Audio Line Out Positive              |
| 28  | EAR_P_R   | Analog        | Ear Right Positive                   |
| 29  | LINEOUT_M | Analog        | Audio Line Out Negative              |
| 30  | EAR_M_R   | Analog        | Ear Right Negative                   |
| 31  | GND       | Ground        | Ground                               |
| 32  | GND       | Ground        | Ground                               |
| 33  | GND       | Ground        | Ground                               |
| 34  | HPH_L     | Analog        | Headphone Left                       |
| 35  | VBAT      | Power Out     | +3.8V Buck Converter Output          |
| 36  | HPH_R     | Analog        | Headphone Right                      |
| 37  | GND       | Ground        | Ground                               |
| 38  | HPH_REF   | Analog        | Headphone Reference                  |
| 39  | VCOIN     | Power In      | Coin Cell / RTC Backup Voltage Input |
| 40  | HS_DET    | Analog        | Headset Detection                   |

#### J15

| Pin | Function              | Type          | Description           |
| --- | --------------------- | ------------- | --------------------- |
| 1   | MCU_PSSI_D0 / PC6     | Digital       | MCU GPIO              |
| 2   | MCU_SDMMC1_CMD / PD2  | Digital       | MCU GPIO              |
| 3   | MCU_PSSI_D1 / PC7     | Digital       | MCU GPIO              |
| 4   | MCU_TRACE_CLK / PE2   | Digital       | MCU GPIO              |
| 5   | MCU_PSSI_D2 / PC8     | Digital       | MCU GPIO              |
| 6   | MCU_TRACE_D0 / PE3    | Digital       | MCU GPIO              |
| 7   | MCU_PSSI_D3 / PC9     | Digital       | MCU GPIO              |
| 8   | MCU_TRACE_D2 / PE5    | Digital       | MCU GPIO              |
| 9   | MCU_PSSI_D4 / PE4     | Digital       | MCU GPIO              |
| 10  | MCU_TRACE_D3 / PE6    | Digital       | MCU GPIO              |
| 11  | MCU_PSSI_D5 / PI4     | Digital       | MCU GPIO              |
| 12  | MCU_PE7 / PE7         | Digital       | MCU GPIO              |
| 13  | MCU_PSSI_D6 / PI6     | Digital       | MCU GPIO              |
| 14  | MCU_PE8 / PE8         | Digital       | MCU GPIO              |
| 15  | MCU_PSSI_D7 / PI7     | Digital       | MCU GPIO              |
| 16  | MCU_I2C4_SCL / PF14   | Digital / I2C | MCU GPIO              |
| 17  | MCU_PSSI_PDCK / PD9   | Digital       | MCU GPIO              |
| 18  | MCU_I2C4_SDA / PF15   | Digital / I2C | MCU GPIO              |
| 19  | MCU_PSSI_RDY / PI5    | Digital       | MCU GPIO              |
| 20  | MCU_OPAMP1_VOUT / PA3 | Analog        | MCU GPIO / OPAMP OUT  |
| 21  | MCU_PSSI_DE / PD8     | Digital       | MCU GPIO              |
| 22  | MCU_OPAMP1_VINP / PA0 | Analog        | MCU GPIO / OPAMP IN + |
| 23  | GND                   | Ground        | Ground                |
| 24  | MCU_OPAMP1_VINM / PA1 | Analog        | MCU GPIO / OPAMP IN - |
| 25  | SOC_GPIO_0_SE0        | Digital       | MPU GPIO              |
| 26  | MCU_MCO / PA8         | Digital       | MCU GPIO              |
| 27  | SOC_GPIO_1_SE0        | Digital       | MPU GPIO              |
| 28  | MCU_CRS_SYNC / PA10   | Digital       | MCU GPIO              |
| 29  | SOC_GPIO_2_SE0        | Digital       | MPU GPIO              |
| 30  | GND                   | Ground        | Ground                |
| 31  | SOC_GPIO_3_SE0        | Digital       | MPU GPIO              |
| 32  | SOC_GPIO_98           | Digital       | MPU GPIO              |
| 33  | SOC_GPIO_86_SE0       | Digital       | MPU GPIO              |
| 34  | SOC_GPIO_99           | Digital       | MPU GPIO              |
| 35  | SOC_GPIO_82_SE0       | Digital       | MPU GPIO              |
| 36  | SOC_GPIO_100          | Digital       | MPU GPIO              |
| 37  | SOC_GPIO_18           | Digital       | MPU GPIO              |
| 38  | SOC_GPIO_101          | Digital       | MPU GPIO              |
| 39  | SOC_GPIO_28           | Digital       | MPU GPIO              |
| 40  | GND                   | Ground        | Ground                |

#### JMEDIA

| Pin | Function                | Type      | Description        |
| --- | ----------------------- | --------- | ------------------ |
| 1   | GND                     | Ground    | Ground             |
| 2   | GND                     | Ground    | Ground             |
| 3   | NC                      | None      | Not Connected      |
| 4   | NC                      | None      | Not Connected      |
| 5   | NC                      | None      | Not Connected      |
| 6   | NC                      | None      | Not Connected      |
| 7   | GND                     | Ground    | Ground             |
| 8   | GND                     | Ground    | Ground             |
| 9   | NC                      | None      | Not Connected      |
| 10  | NC                      | None      | Not Connected      |
| 11  | GND                     | Ground    | Ground             |
| 12  | NC                      | None      | Not Connected      |
| 13  | GND                     | Ground    | Ground             |
| 14  | GND                     | Ground    | Ground             |
| 15  | NC                      | None      | Not Connected      |
| 16  | SOC_CAM_MCLK0 / GPIO_20 | Digital   | MPU GPIO           |
| 17  | NC                      | None      | Not Connected      |
| 18  | SOC_CAM_MCLK1 / GPIO_21 | Digital   | MPU GPIO           |
| 19  | GND                     | Ground    | Ground             |
| 20  | GND                     | Ground    | Ground             |
| 21  | NC                      | None      | Not Connected      |
| 22  | CCI_I2C_SDA1 / GPIO_29  | I2C       | MPU GPIO           |
| 23  | NC                      | None      | Not Connected      |
| 24  | CCI_I2C_SCL1 / GPIO_30  | I2C       | MPU GPIO           |
| 25  | GND                     | Ground    | Ground             |
| 26  | GND                     | Ground    | Ground             |
| 27  | NC                      | None      | Not Connected      |
| 28  | NC                      | None      | Not Connected      |
| 29  | NC                      | None      | Not Connected      |
| 30  | NC                      | None      | Not Connected      |
| 31  | GND                     | Ground    | Ground             |
| 32  | GND                     | Ground    | Ground             |
| 33  | NC                      | None      | Not Connected      |
| 34  | NC                      | None      | Not Connected      |
| 35  | NC                      | None      | Not Connected      |
| 36  | NC                      | None      | Not Connected      |
| 37  | GND                     | Ground    | Ground             |
| 38  | GND                     | Ground    | Ground             |
| 39  | NC                      | None      | Not Connected      |
| 40  | NC                      | None      | Not Connected      |
| 41  | NC                      | None      | Not Connected      |
| 42  | NC                      | None      | Not Connected      |
| 43  | GND                     | Ground    | Ground             |
| 44  | GND                     | Ground    | Ground             |
| 45  | NC                      | None      | Not Connected      |
| 46  | NC                      | None      | Not Connected      |
| 47  | NC                      | None      | Not Connected      |
| 48  | NC                      | None      | Not Connected      |
| 49  | GND                     | Ground    | Ground             |
| 50  | GND                     | Ground    | Ground             |
| 51  | CCI_I2C_SCL0 / GPIO_23  | I2C       | MPU GPIO           |
| 52  | NC                      | None      | Not Connected      |
| 53  | CCI_I2C_SDA0 / GPIO_22  | I2C       | MPU GPIO           |
| 54  | NC                      | None      | Not Connected      |
| 55  | GND                     | Ground    | Ground             |
| 56  | GND                     | Ground    | Ground             |
| 57  | VIN                     | Power In  | Voltage Input      |
| 58  | +3V3                    | Power Out | +3.3V Power Output |
| 59  | VIN                     | Power In  | Voltage Input      |
| 60  | +3V3                    | Power Out | +3.3V Power Output |

#### JMISC

| Pin | Function              | Type          | Description                          |
| --- | --------------------- | ------------- | ------------------------------------ |
| 1   | MCU_PSSI_D0 / PC6     | Digital       | MCU GPIO                             |
| 2   | MCU_SDMMC1_CMD / PD2  | Digital       | MCU GPIO                             |
| 3   | MCU_PSSI_D1 / PC7     | Digital       | MCU GPIO                             |
| 4   | MCU_TRACE_CLK / PE2   | Digital       | MCU GPIO                             |
| 5   | MCU_PSSI_D2 / PC8     | Digital       | MCU GPIO                             |
| 6   | MCU_TRACE_D0 / PE3    | Digital       | MCU GPIO                             |
| 7   | MCU_PSSI_D3 / PC9     | Digital       | MCU GPIO                             |
| 8   | MCU_TRACE_D2 / PE5    | Digital       | MCU GPIO                             |
| 9   | MCU_PSSI_D4 / PE4     | Digital       | MCU GPIO                             |
| 10  | MCU_TRACE_D3 / PE6    | Digital       | MCU GPIO                             |
| 11  | MCU_PSSI_D5 / PI4     | Digital       | MCU GPIO                             |
| 12  | MCU_PE7 / PE7         | Digital       | MCU GPIO                             |
| 13  | MCU_PSSI_D6 / PI6     | Digital       | MCU GPIO                             |
| 14  | MCU_PE8 / PE8         | Digital       | MCU GPIO                             |
| 15  | MCU_PSSI_D7 / PI7     | Digital       | MCU GPIO                             |
| 16  | MCU_I2C4_SCL / PF14   | Digital / I2C | MCU GPIO                             |
| 17  | MCU_PSSI_PDCK / PD9   | Digital       | MCU GPIO                             |
| 18  | MCU_I2C4_SDA / PF15   | Digital / I2C | MCU GPIO                             |
| 19  | MCU_PSSI_RDY / PI5    | Digital       | MCU GPIO                             |
| 20  | MCU_OPAMP1_VOUT / PA3 | Analog        | MCU GPIO / OPAMP OUT                 |
| 21  | MCU_PSSI_DE / PD8     | Digital       | MCU GPIO                             |
| 22  | MCU_OPAMP1_VINP / PA0 | Analog        | MCU GPIO / OPAMP IN +                |
| 23  | MCU_MCO / PA8         | Digital       | MCU GPIO                             |
| 24  | MCU_OPAMP1_VINM / PA1 | Analog        | MCU GPIO / OPAMP IN -                |
| 25  | MCU_CRS_SYNC / PA10   | Digital       | MCU GPIO                             |
| 26  | GND                   | Ground        | Ground                               |
| 27  | GND                   | Ground        | Ground                               |
| 28  | EAR_P_R               | Analog        | Ear Right Positive                   |
| 29  | MIC2_INP              | Analog        | Microphone Input Positive            |
| 30  | EAR_M_R               | Analog        | Ear Right Negative                   |
| 31  | MIC2_INM              | Analog        | Microphone Input Negative            |
| 32  | LINEOUT_P             | Analog        | Audio Line Out Positive              |
| 33  | MIC2_BIAS             | Analog        | Microphone Bias                      |
| 34  | LINEOUT_M             | Analog        | Audio Line Out Negative              |
| 35  | GND                   | Ground        | Ground                               |
| 36  | HPH_L                 | Analog        | Headphone Left                       |
| 37  | SOC_GPIO_0_SE0        | Digital       | MPU GPIO                             |
| 38  | HPH_R                 | Analog        | Headphone Right                      |
| 39  | SOC_GPIO_1_SE0        | Digital       | MPU GPIO                             |
| 40  | HPH_REF               | Analog        | Headphone Reference                  |
| 41  | SOC_GPIO_2_SE0        | Digital       | MPU GPIO                             |
| 42  | HS_DET                | Analog        | Headset Detection                    |
| 43  | SOC_GPIO_3_SE0        | Digital       | MPU GPIO                             |
| 44  | GND                   | Ground        | Ground                               |
| 45  | SOC_GPIO_86_SE0       | Digital       | MPU GPIO                             |
| 46  | SOC_GPIO_98           | Digital       | MPU GPIO                             |
| 47  | SOC_GPIO_82_SE0       | Digital       | MPU GPIO                             |
| 48  | SOC_GPIO_99           | Digital       | MPU GPIO                             |
| 49  | SOC_GPIO_18           | Digital       | MPU GPIO                             |
| 50  | SOC_GPIO_100          | Digital       | MPU GPIO                             |
| 51  | SOC_GPIO_28           | Digital       | MPU GPIO                             |
| 52  | SOC_GPIO_101          | Digital       | MPU GPIO                             |
| 53  | +3V3                  | Power Out     | +3.3V Power Output                   |
| 54  | +5V USB               | Power Out     | +5V USB Power Output                 |
| 55  | +3V3                  | Power Out     | +3.3V Power Output                   |
| 56  | +5V USB               | Power Out     | +5V USB Power Output                 |
| 57  | +1V8                  | Power Out     | +1.8V Power Output                   |
| 58  | GND                   | Ground        | Ground                               |
| 59  | VCOIN                 | Power In      | Coin Cell / RTC Backup Voltage Input |
| 60  | VBAT                  | Power Out     | +3.8V Buck Converter Output          |

### Block Diagram

An overview of the UNO Breakout Carrier high-level architecture is illustrated in the figure below.

![UNO Breakout Carrier Block Diagram](assets/ASX00085-block-diagram.png)

## Device Operation

### Getting Started

If you want to program your UNO Q to use the UNO Breakout Carrier while offline, you need to install the Arduino® App Lab **[1]**. To connect the UNO Q to your computer, you will need a USB cable or an internet connection (Network Mode), which can also provide power to the board.

### Online Resources

Now that you have learned the basics of what you can do with the carrier, you can explore its endless possibilities by checking out exciting projects on Arduino Project Hub **[4]**, the Arduino Library Reference **[5]**, and the online store **[6]**. Here, you can complement your board with sensors, actuators and more.

## Mechanical Information

### Board Dimensions

The outline and dimensions of the UNO Breakout Carrier and mounting holes can be seen in the following figure;
all the dimensions are in mm.

![Board outline and screw holes](assets/ASX00085-outline.png)

<div style="page-break-after: always;"></div>

### Board Connectors

The UNO Breakout Carrier's connectors are placed on the top side of the board, as shown in the figure below; all
the dimensions are in mm.

![Mechanical View of UNO Breakout Carrier's Connectors](assets/ASX00085-connectors.png)

<div style="page-break-after: always;"></div>

## Certifications

### Certificactions Summary

|  **Certification**  | **Status** |
| :-----------------: | :--------: |
| CE (European Union) |    Yes     |
|        RoHS         |    Yes     |
|        REACH        |    Yes     |
|        WEEE         |    Yes     |
|      FCC (USA)      |    Yes     |
|     IC (Canada)     |    Yes     |
|      UKCA (UK)      |    Yes     |
|      VCC (Japan)    |    Yes     |

### Declaration of Conformity CE DoC (EU)

We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).

### Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.

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

Exemptions : No exemptions are claimed.

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs ([https://echa.europa.eu/web/guest/candidate-list-table](https://echa.europa.eu/web/guest/candidate-list-table)), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration

As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

### FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

(1) This device may not cause harmful interference

(2) this device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator & your body.

English:
User manuals for licence-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual or alternatively on the device or both. This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions:

(1) this device may not cause interference

(2) this device must accept any interference, including interference that may cause undesired operation of the device.

French:
Le présent appareil est conforme aux CNR d’Industrie Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes :

(1) l’ appareil nedoit pas produire de brouillage

(2) l’utilisateur de l’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

**IC SAR Warning:**

English
This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

French:
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85 ℃ and shouldn’t be lower than -40 ℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 201453/EU. This product is allowed to be used in all EU member states.

## Company Information
| Company name    | Arduino S.r.l.                               |
| --------------- | -------------------------------------------- |
| Company Address | Via Andrea Appiani, 25 - 20900 MONZA (Italy) |

## Reference Documentation
| **No.** |          **Ref**          | **Link**                                                                                            |
| :-----: | :-----------------------: | --------------------------------------------------------------------------------------------------- |
|    1    |      Arduino App Lab      | https://docs.arduino.cc/software/app-lab/                                                           |
|    2    |   Arduino IDE (Desktop)   | https://www.arduino.cc/en/Main/Software                                                             |
|    3    |    Arduino IDE (Cloud)    | https://create.arduino.cc/editor                                                                    |
|    4    | Cloud IDE Getting Started | https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-4b3e4a |
|    5    |    Arduino Pro Website    | https://www.arduino.cc/pro                                                                          |
|    6    |        Project Hub        | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending                            |
|    7    |     Library Reference     | https://www.arduino.cc/reference/en/                                                                |
|    8    |       Online Store        | https://store.arduino.cc/                                                                           |

## Change Log
| **Date**   | **Revision** | **Changes**                                 |
|------------|--------------|---------------------------------------------|
| 27/03/2026 | 1            | First Release                               |