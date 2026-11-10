---
identifier: AFX00001-AFX00002-AFX00003
title: Arduino Opta®
type: pro
variant: 'Collective Datasheet'
author: Ali Jahangiri, Julián Caro Linares
---

![](assets/featured.png)

# English

# Description

Arduino Opta® is a secure, easy-to-use micro PLC with Industrial IoT capabilities. Designed in partnership with leading relay manufacturer Finder®, it allows professionals to scale up industrial and building automation projects while taking advantage of the Arduino ecosystem.

The Arduino Opta® family has three variants: the Arduino Opta® Lite, Arduino Opta® RS485, and Arduino Opta® WiFi, all of them documented inside this document.

# Target Areas:

Industrial IoT, Building automation, Electrical loads management, Industrial automation

**Product Intended Use**

Arduino Hardware Products are primarily intended for development and prototyping but may also support production solutions. Developers must design and verify security controls early, based on the intended deployment environment. Security is a shared responsibility between Arduino and the solution builder, who must assess the hardware’s available security features and add any necessary protections.

Visit [docs.arduino.cc/tutorials/security/intended-use-and-security-model/](https://docs.arduino.cc/tutorials/security/intended-use-and-security-model/) for the complete Arduino Hardware Products: Intended use and Security model.

# CONTENTS

## Product Variants

There are three variants of the Arduino Opta® created to fit the different needs of each industry and application. The difference between each of the variants can be found in the following table:

| **Name**         | **Arduino Opta® Lite** | **Arduino Opta® RS485** | **Arduino Opta® WiFi** |
|:-----------------|:-----------------------|:------------------------|:-----------------------|
| SKU              | AFX00003               | AFX00001                | AFX00002               |
| USB              | USB-C®                 | USB-C®                  | USB-C®                 |
| Ethernet Support | 10/100BASE-T Port      | 10/100BASE-T Port       | 10/100BASE-T Port      |
| RS-485           | N/A                    | Half-duplex             | Half-duplex            |
| Wi-Fi®           | N/A                    | N/A                     | 802.11 b/g/n           |
| Bluetooth®       | N/A                    | N/A                     | Bluetooth® Low Energy  |

## Application Examples

Arduino Opta® is designed for industrial standard machinery control as a PLC with advanced features such as AI and connectivity capabilities. It is readily integrated into the Arduino hardware and software ecosystem, including real-time monitoring via the Arduino Cloud.

- **Conveyor belt management:** Arduino Opta® offers the possibility to configure its inputs as digital or analog to flexibly collect data from several types of sensors. Thanks to the Wi-Fi®/Bluetooth® Low Energy connectivity, Arduino Opta® can also be smoothly integrated with sensing boards, like the Nicla® ones from the Arduino ecosystem, leveraging Arduino Opta's potential with vision, sound, weight detection, air quality measurement and many other capabilities. 

    Arduino Opta® can use the data from the various sensors as they are or, thanks to its powerful microcontroller, use the outcome from a computation, to operate a wide variety of industrial machinery through its high-performing relays.

    All these features, wrapped in a compact form factor, make Arduino Opta® the ideal solution for product flow management in conveyor belts, automated packing or bottling lines. 

- **Real-time industrial monitoring:** Get instant access to your factory floor data and to the insights of your industrial processes to leverage your manufacturing excellence to continuous improvement. Implement visual management and KPIs monitoring thanks to the Arduino Opta's built-in connectivity features (Ethernet on all the product variants, Fieldbus and WiFi®/Bluetooth® Low Energy upon choice), delivering in a simple, fast and reliable way the data collected through beautiful dashboards in Arduino Cloud.
  
- **Predictive maintenance:** Combine the possibility to interact with wireless and wired sensors, given by the multiple connectivity options of Arduino Opta®, with the powerful microcontroller computational capabilities to implement AI algorithms for predictive maintenance. Edge computing and monitoring capabilities, thanks to the Arduino Cloud features, can help to identify small drifts in your processes to address issues before they become a problem, reducing production line downtimes and ensuring quality outcomes.

## Features

### General Specifications Overview

| **Characteristics**  | **Details**                                                                                                                              |
|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| Supply Voltage       | 12...24 VDC                                                                                                                              |
| Inputs               | 8x Analog/Digital inputs                                                                                                                 |
| Outputs              | 4x Relays - Normally Open (NO) - Max: 10 A each                                                                                          |
| Processor            | Dual-core ST STM32H747XI Processor                                                                                                       |
| Program Memory       | 1 MB of RAM                                                                                                                              |
| Flash Memory         | 2 MB                                                                                                                                     |
| Flash QSPI Interface | 16 MB Flash QSPI. Shared between manufacturer's internal usage and data logging                                                          |
| Programming method   | Arduino + IEC-61131-3 (LD - SFC - FBD - ST - IL)                                                                                         |
| USB Connectivity     | Host and Device operation, Programming/Flashing, Power delivery for programming (Not intended to drive external high-power peripherals)  |
| Communication        | Ethernet, RS-485 (AFX00001 & AFX00002), Wi-Fi® 2.4 GHz and Bluetooth® LE 4.2 supported by firmware, 5.1 supported by hardware (AFX00002) |
| RTC                  | ~10 days, NTP sync through Wi-Fi® (AFX00002 only) or Ethernet                                                                            |
| Security             | ATECC608B Crypto Microchip®                                                                                                              |
| Degree of Protection | IP20                                                                                                                                     |
| Certifications       | cULus, ENEC, FCC, CE, CB, UKCA                                                                                                           |

### Processor

| **Component**            | **Feature**        | Details                                                                              |
|:-------------------------|:-------------------|:-------------------------------------------------------------------------------------|
| ST STM32H747XI Processor | Dual-core          | Arm® Cortex®-M7 core at up to 480 MHz + Arm® 32-bit Cortex®-M4 core at up to 240 MHz |
|                          | Flash Memory       | 2 MB of Flash Memory with read-while-write support                                   |
|                          | Programming Memory | 1 MB of RAM                                                                          |

### Security

| **Component**               | **Details**                                                       |
|-----------------------------|-------------------------------------------------------------------|
| ATECC608B Crypto Microchip® | Cryptographic co-processor with secure hardware-based key storage |
|                             | Protected storage for up to 16 Keys, certificates or data         |
|                             | Networking key management support                                 |
|                             | Secure boot support                                               |
|                             | Guaranteed unique 72-bit serial number                            |

### Communication

| **Interfaces**        | **Type**                                   | **Protocols/Technologies Supported**                 |
|:----------------------|:-------------------------------------------|:-----------------------------------------------------|
| Ethernet              | 10/100BASE-T Port                          | TCP/IP, MODBUS TCP                                   |
| RS-485                | Half-duplex without termination resistance | MODBUS RTU, Custom serial communication              |
| Expansion Port        | Proprietary Port                           | Expansion module communication                       |
| Wireless Connectivity | Wi-Fi®                                     | 2.4 GHz                                              |
| Wireless Connectivity | Bluetooth® Low Energy                      | 4.2 supported by firmware, 5.1 supported by hardware |

### Inputs

| **Characteristics**           | **Details**              |
|:------------------------------|:-------------------------|
| Number of inputs              | 8x Analog/Digital inputs |
| Inputs overvoltage protection | Yes                      |
| Antipolarity protection       | Yes                      |
| Input impedance               | 8.9 kΩ                   |

#### Analog Inputs

| **Characteristics**     | **Details**                      |
|:------------------------|:---------------------------------|
| Analog Input voltage    | 0...10 V                         |
| Analog Input resolution | 12...16 bits - User configurable |
| Analog Input LSB value  | 166 µV                           |
| Accuracy                | +/- 5%, repeatability +/- 2%     |

#### Digital Inputs

| **Characteristics**                     | **Details**                                                                          |
|:----------------------------------------|:-------------------------------------------------------------------------------------|
| Digital Input voltage                   | 0...24 V                                                                             |
| Digital Input voltage logic level       | Voltage Input Low (VIL) Maximum: 4.46 VDC. Voltage Input High (VIH) Minimum: 6.6 VDC |
| Digital Input current                   | 1.12 mA at 10 V                                                                      |
| Digital Input frequency                 | 4.5 kHz                                                                              |
| Cycle time for analog input acquisition | 10 µs                                                                                |

### Outputs

| **Characteristics**                         | **Details**                                      |
|:--------------------------------------------|:-------------------------------------------------|
| Number of outputs                           | 4x relays (NO)                                   |
| Max current per relay                       | 10 A                                             |
| Max peak current per relay                  | 15 A                                             |
| Continuous current per terminal             | 10 A                                             |
| Short-circuit protection                    | No, external fuse required                       |
| Relay rated voltage                         | 250 VAC                                          |
| Relay Max voltage                           | 400 VAC                                          |
| Rated load AC1                              | 2500 VA                                          |
| Rated load AC15 (230 VAC)                   | 500 VA                                           |
| Breaking capacity DC1: 24/30/110/220 V      | 10/4/0.3/0.12 A                                  |
| Minimum switching load                      | 300 mW (5 V/5 mA)                                |
| Max output line length (unshielded)         | 100 m                                            |
| Relay response time from state 0 to state 1 | 6 ms for relay output                            |
| Relay response time from state 1 to state 0 | 4 ms for relay output                            |
| Bounce time NO                              | 3 ms                                             |
| Bounce time NC                              | 6 ms                                             |
| Relay mechanical durability                 | 10 million cycles                                |
| Relay electrical durability                 | 10 thousand cycles with a resistive load of 10 A |

<div style="page-break-after:always;"></div>

## Ratings

### Recommended Operating Conditions

| **Description**             | **Value**                 |
|:----------------------------|:--------------------------|
| Temperature Operating Range | -20...50 °C               |
| Protection degree rating    | IP20                      |
| Pollution degree            | 2 conforming to IEC 61010 |

### Power Specification

| **Property**             | **Min** | **Typ** | **Max** | **Unit** |
|--------------------------|---------|---------|---------|----------|
| Supply voltage           | 12      | -       | 24      | V        |
| Permissible range        | 10.2    | -       | 27.6    | V        |
| Power consumption (12 V) | 0.6     | -       | 2       | W        |
| Power consumption (24 V) | 0.6     | -       | 2.2     | W        |

<div style="page-break-after:always;"></div>

## Functional Overview

### Product View

![Arduino Opta® Product View](assets/opta_panel.svg)

<div style="page-break-after:always;"></div>

| Item | Feature                                                              | Item | Feature                                                             |
|------|----------------------------------------------------------------------|------|---------------------------------------------------------------------|
| 3A   | Power Supply Terminals 12...24 VDC                                   | 3H   | Ethernet Port Status LEDs                                           |
| 3B   | I1...I8 digital/analog input terminals (0-10 V) configurable via IDE | 3I   | Label Holder                                                        |
| 3C   | Reset Button                                                         | 3J   | RS-485 terminal block (for Modbus RTU or proprietary communication) |
| 3D   | User Programmable button                                             | 3K   | USB-C® for programming and data logging                             |
| 3E   | Status LEDs 1...4 (User Programmable)                                | 3M   | Ethernet port                                                       |
| 3F   | Relay Output Terminals 1...4, NO contact (SPST) 10 A 250 VAC         | 3N   | Port for communication and connection of auxiliary modules          |
| 3G   | Functional Earth                                                     |      |                                                                     |

> [!NOTE]
> The LED above the *User Programmable button* (Ref: 3D) is only available on Arduino Opta® WiFi (AFX00002).

### Wiring Specifications

Following Opta's wiring specifications is important to ensure proper connection and operation of its electrical terminals. The tables shown below provide recommendations for torque application, cable preparation, and accepted wire types of Opta's electrical terminals.

#### Recommended Torque and Cable Preparation

| **Torque** | **Recommended Tool**         | **Stripping Length** |
|:-----------|:-----------------------------|:---------------------|
| 0.80 Nm    | #1 Phillips-head screwdriver | 9 mm                 |

#### Accepted Wire Types

| **Wire Type**      | **Minimum Size** | **Maximum Size**                    |
|:-------------------|:-----------------|:------------------------------------|
| Solid Conductor    | 0.5 mm² (20 AWG) | 6 mm² (10 AWG)/2x4 mm² (2x12 AWG)   |
| Stranded Conductor | 0.5 mm² (20 AWG) | 4 mm² (12 AWG)/2x2.5 mm² (2x14 AWG) |

### Microcontroller

The microcontroller is a dual-core *STM32H747XI*. The main processor is a *Cortex®-M7* running at up to 480 MHz and the second one is a Cortex®-M4 running at up to 240 MHz.

Arduino Opta® can be programmed using the libraries developed for it as part of the standard Arduino Core library.

### Encryption

Encryption capabilities are provided by the *ATECC608B* chipset. This crypto-chip can be used to store sensitive information like security keys to connect to the Arduino Cloud or other third-party services, protecting Arduino Opta® from any unauthorized access in any kind of industrial and professional environment.

### Ethernet

TCP/IP and Modbus TCP communication are supported. The 10/100 Ethernet physical interface is directly connected to the internal Ethernet MAC and provides full-duplex communication with automatic MDIX support. With an internet connection, Ethernet communication can be used to connect the device to the Arduino Cloud or other third-party services.

### Modbus RTU

![Modbus RTU wiring diagram using the RS-485 interface](assets/opta_wiring_modbus.svg)

Modbus RTU communication is supported using Arduino Opta's RS-485 physical interface.

> [!NOTE]
> Arduino Opta® does not have internal terminator resistors, so they need to be added if necessary following the Modbus protocol specification.

The wiring indication may vary depending on the connected device. In case the above connection indication is not resulting in consistent data transmission, invert the wires between A(-) and B(+) and retry.

### Wi-Fi® and Bluetooth® Low Energy (AFX00002 Only)

The onboard wireless module allows simultaneous management of Wi-Fi® and Bluetooth® connectivity. The Wi-Fi® interface can be operated as an Access Point, as a Station or as a dual-mode simultaneous AP/STA, and can handle up to 65 Mbps transfer rate. Bluetooth® interface supports Bluetooth® Low Energy (4.2). 

With an internet connection, the Wi-Fi® communication can be used for connecting to the Arduino Cloud or other third-party services.

### USB-C®

The USB-C® port can be used as a host or as a peripheral, but it cannot be used for both purposes at the same time. It is possible to use the connector to power the processor and flash it, but not to power the PLC outputs and peripherals. Additionally and using a USB memory stick, the USB-C® connector can be used for data logging purposes or to update the program inside the PLC.

### Relay Outputs

Arduino Opta® has four *Normally Open* (NO) powerful 10 A relays which are capable of actuating on loads at a rated voltage of 250 VAC and up to a maximum switching voltage of 400 VAC.

The relay *Maximum Peak Current* is defined as the highest value of inrush current that the relay can endure without undergoing any permanent degradation of its characteristics due to the generated heat. The relay has to be able to hold up that maximum using a duty cycle of less or equal to 10% and for a time equal to or less than 0.5 s.

In the case of Arduino Opta®, relays have a *Maximum Peak Current* of 15 A.

The *Rated Load* is the maximum resistive load that a contact can make, carry and break repeatedly.

- For resistive or slightly inductive loads (AC1 classification), Arduino Opta's *Rated Load* is 2500 VA.
- For small electromagnetic loads (> 72 VA) (AC15 classification) like power contactors, magnetic solenoid valves, electromagnets and AC single-phase supplies, Arduino Opta's *Rated Load* is 500 VA. This value assumes a peak inrush current of approximately 10 times the rated current and keeping it within the maximum peak current.

For controlling DC loads (DC1 classification), the *Breaking Capacity* or maximum value of DC resistive current that a contact can make, carry and break repeatedly, is 10/4/0.3/0.12 A for respectively 24/30/110/220 V.

In the case of the minimum switching load parameters, the minimum values of power, voltage and current that the relays can reliably switch, are 300 mW/ 5 V / 5 mA. This implies that with 5 V the current must be at least 60 mA, with 24 V, it must be at least 12.5 mA, and with 5 mA the voltage must be at least 60 V.

The relays on Arduino Opta® provide a very fast response time of 6/4 ms to change state for closing/reopening, and a bounce time NO/NC of 3/6 ms.

### Expansion Port

The expansion port can be used to expand the Arduino Opta® capabilities with the help of additional modules. It supports up to 5 expansion modules. To avoid potential communication issues, ensure the total number of connected modules does not exceed 5.

> [!NOTE]
> Arduino Opta® is designed and tested with Arduino Opta® expansion modules. Compatibility with non-Arduino expansion modules, including similar-looking modules from other manufacturers, is not ensured.

If any issues occur with module detection or data exchange, double-check the connections and ensure the **Aux connector and clips are securely installed** within the expansion port. If problems persist, inspect for any loose or improperly connected cables.

### Programmable User Button

A pushbutton is accessible on the front panel of the Arduino Opta®. The functionality of this button can be configured via software. Note that the LED above the *User button* is only available on Arduino Opta® WiFi (AFX00002).

### Functional Earth

To avoid and reduce electrical noise, Arduino Opta® has a *Functional Earth* connector (Ref: 3G) near the Ethernet connector. *Functional Earth*, not to be confused with *Ground*, helps the device to reduce electrical interferences in industrial environments, being crucial for having stable Fieldbus communications.

<div style="page-break-after:always;"></div>

## Device Operation

### Getting Started - IDE

If you want to program your Arduino Opta® while offline you need to install the Arduino® Desktop IDE **[1]**. To connect the Arduino Opta® to your computer, you will need a USB-C® cable.

### Getting Started - Arduino Cloud Editor

All Arduino® devices work out-of-the-box on the Arduino® Cloud Editor **[2]** by just installing a simple plugin.

The Arduino® Cloud Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards and devices. Follow **[3]** to start coding on the browser and upload your sketches onto your device.

### Getting Started - Arduino PLC IDE

Arduino Opta® can be also programmed using the industrial-standard **_IEC 61131-3_** programming languages. Download the Arduino® PLC IDE **[4]** software and connect your Arduino Opta® to your computer, using a simple USB-C® cable, to start creating your own PLC industrial solutions.

### Getting Started - Arduino Cloud

All Arduino® IoT enabled products are supported on Arduino Cloud which allows you to log, graph and analyze sensor data, trigger events, and automate your home or business.

### Sample Sketches

Sample sketches for Arduino Opta® can be found either in the “Examples” menu in the Arduino® IDE or the “Arduino Opta® Documentation” section of Arduino® **[5]**.

### Online Resources

Now that you have gone through the basics of what you can do with the device, you can explore the endless possibilities it provides by checking exciting projects on ProjectHub **[6]**, the Arduino® Library Reference **[7]** and the online store **[8]** where you will be able to complement your Arduino Opta® product with additional extensions, sensors and actuators.

## Mean Time Between Failure (MTBF)

MTBF, which stands for Mean Time Between Failure, is calculated according to statistical device failures and indicates the reliability of a device.

The MTBF figure (in hours/years) for each Arduino Opta® variant can be found in the table below. The MTBF figure was calculated according to the MIL-HDBK-217F parts count method.

| **Standard**  | **All Opta® Variants** | **Environmental Conditions** |
|:--------------|:-----------------------|:-----------------------------|
| MIL-HDBK-217F | 766205 h/87 years      | 25 °C                        |

> [!NOTE]
> MTBF is the statistical representation of the likelihood of a unit failing and *does not necessarily represent a product's life*.

## Mechanical Information

### Product Dimensions

![Arduino Opta® Outline. Dimensions are in mm](assets/opta_mechanical.svg)

## Certifications

### Certifications Summary

| Certification | Arduino Opta® RS485 (AFX00001)          | Arduino Opta® WiFi (AFX00002)                                                                                                        | Arduino Opta® Lite (AFX00003)           |
|---------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| CE (EU)       | EN IEC 61326-1:2021, EN IEC 61010 (LVD) | EN IEC 62311:2020, EN IEC 61010 (LVD), EN 301 489-1 V2.2.3, EN 301 489-17 V3.2.4, IEC 61326-1:2021, EN 300 328 V2.2.2:2019-07        | EN IEC 61326-1:2021, EN IEC 61010 (LVD) |
| CB (EU)       | Yes                                     | Yes                                                                                                                                  | Yes                                     |
| WEEE (EU)     | Yes                                     | Yes                                                                                                                                  | Yes                                     |
| ENEC          | Yes                                     | Yes                                                                                                                                  | Yes                                     |
| REACH (EU)    | Yes                                     | Yes                                                                                                                                  | Yes                                     |
| UKCA (UK)     | EN IEC 61326-1:2021                     | EN IEC 62311:2020, EN 300 328 V2.2.2:2019-07, EN 301 489-1 V2.2.3, EN 301 489-17 V3.2.4, IEC 61326-1:2021                            | EN IEC 61326-1:2021                     |
| FCC (US)      | Yes                                     | Yes                                                                                                                                  | Yes                                     |
| IC (Canada)   | -                                       | Yes                                                                                                                                  | -                                       |
| cULus         | UL 61010-2-201                          | UL 61010-2-201                                                                                                                       | UL 61010-2-201                          |

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
| Bis(2-Ethylhexyl) phthalate (DEHP)     | 1000                    |
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

**Note:** This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial environment. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

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

**Important:** The operating temperature of the EUT can’t exceed 50℃ and shouldn’t be lower than -20℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 2014/53/EU. This product is allowed to be used in all EU member states.

| Frequency bands           | Maximum output power (EIRP) |
|---------------------------|-----------------------------|
| 2412-2472 MHz (2.4G WIFI) | 5.42 dBm                    |
| 2402-2480 MHz (BLE)       | 2.41 dBm                    |
| 2402-2480 MHz (EDR)       | -6.27 dBm                   |

## Industry Canada Statement:

Radio apparatus containing digital circuitry which can function separately from the operation of a transmitter or an associated transmitter, shall comply with ICES-003. In such cases, the labelling
requirements of the applicable RSS apply, rather than the labelling requirements in ICES-003. 

This Class A digital apparatus complies with Canadian ICES-003.

French:
Cet appareil numérique de la classe A est conforme à la norme NMB-003 du Canada.

## Company Information

| Company name    | Arduino S.r.l                                  |
|-----------------|------------------------------------------------|
| Company Address | Via Andrea Appiani, 25 - 20900 MONZA (Italy)   |


## Reference Documentation

|             **Ref**             | **Link**                                                                        |
|:-------------------------------:|---------------------------------------------------------------------------------|
|      Arduino IDE (Desktop)      | https://www.arduino.cc/en/software                                              |
|       Arduino Cloud Editor      | https://app.arduino.cc/sketches                                                 |
| Arduino Cloud - Getting started | https://docs.arduino.cc/arduino-cloud/guides/overview                           |
|         Arduino PLC IDE         | https://www.arduino.cc/en/software                                              |
|   Arduino Opta® Documentation   | https://docs.arduino.cc/hardware/opta                                           |
|           Project Hub           | https://projecthub.arduino.cc/                                                  |
|        Library Reference        | https://docs.arduino.cc/language-reference                                      |
|          Online Store           | https://store.arduino.cc/                                                       |

## Revision History

| **Date**   | **Revision** | **Changes**                          |
|:-----------|:-------------|:-------------------------------------|
| 02/03/2023 | 1            | First Release                        |
| 13/04/2023 | 2            | Tech Specs Updates                   |
| 16/05/2023 | 3            | Legal updates                        |
| 07/02/2024 | 4            | MTBF information                     |
| 24/07/2024 | 5            | Wiring specifications                |
| 03/09/2024 | 6            | Cloud Editor updated from Web Editor |
| 11/09/2024 | 7            | ICES certification updates           |
| 24/09/2024 | 8            | Expansion port updates               |
| 02/12/2024 | 9            | Digital input specification update   |
| 20/10/2026 | 10           | Added note for Intended Use          |
| 29/10/2026 | 11           | Expansion port compatibility note    |
| 02/11/2026 | 12           | Formatting and style update          |
