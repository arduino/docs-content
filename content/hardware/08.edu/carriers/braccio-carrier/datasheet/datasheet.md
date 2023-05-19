---
identifier: ASX00032
title: Arduino® Braccio Carrier
type: edu
---

![](assets/featured.png)

# Description
Arduino® Braccio Carrier is an add-on board that sits on top of your favorite Arduino Educational existing product line providing faster prototyping in increasing demands for robotics and automation. The tailor-made Arduino® Braccio Carrier has a collection of features that enables quick and easy learning while building small projects.

# Target Areas
Robotics, Automation, Education, Gaming, Communication

# Features
- **MaxLinear SP335 Transceiver**
  - Multiprotocol transceiver supporting RS-232, RS-485, and RS-422 serial standards
  - Data rates of 20 Mbps in RS-485/422 modes and up to 1Mbps in RS-232
  - ±15kV ESD protection
  - Supply voltage from 3V to 5.5V
- **Display Connector**
  - Flexible flat cable and flexible printed circuit connector with 0.5mm spacing
  - Operating temperature up to 105°C
  - Max current for one contact is 0.5A
  - Robust, reliable and easy to operate for automatic mounting and SMT processes
  - Right angle mounting
  - Plastic tape packaging
- **Mini Joystick Connector**
- **Programmable USB Type-C® Connector**
- **ESD Protection**
  - 4- and 5-line unidirectional transil function for electrostatic discharge protection
  - Low-leakage current: < 500 nA
  - PCB Area: < 2.6 mm2

# Contents
## The Board
The custom-made Arduino® Braccio Carrier provides a wide range of connectivity capabilities to the Arduino® Educational boards. For easy to learn and play around prototyping robotic and smart automation projects in and out of classrooms, Arduino® Braccio Carrier features interfaces for display, servo motors and joystick. Along with high-speed RS-485/422 and RS-232 serial communication, the carrier board offers huge support for several accessories through the IO headers. In situations of long-range operations, RS-485 can support several devices on the same bus in a noisy environment. The board has robust electrostatic discharge protection circuitry to keep the components safe.

### Application Examples
- **Smart Automation**: The industry-standard RS-232 and RS-485/422 serial communication support for Arduino® Braccio Carrier has made it possible to implement smart automation IoT projects for a wide range of projects. The low-power carrier board enables students to take advantage of the onboard connectors and play with the Arduino® hardware for the enhanced learning experience
- **Robotic Arm**: Through servo motor connector supporting up to a total of 6 motors has given a chance to demonstrate robotic application including RC Car. Some of the most interesting robotic applications with faster prototyping come from the student community for various problem statements.
- **Gaming**: Thanks to the Mini Joystick connector provided on the Arduino® Braccio Carrier carrier board which facilitates the implementation of LCD gaming options. Interfacing Mini Joystick with the carrier board integrated with a powerful Arduino® board can deliver some really exciting projects.

### Related Products
- Arduino® Nano RP2040 Connect.

## Technical Specification Overview
Following information outlines the technical overview of the Arduino® Braccio Carrier.

### Peripherals
- **JAX133T-IF05**
  - Display module to allow Braccio ++ to deploy visual information. The module is based on 240RGBX240 Dot-Matrix TFT LCD via FPC interface. It is possible to interconnect via Display Connector J1 found on Arduino® Braccio Carrier.
    | Compatible Connector |
    | :------------------: |
    | J1 (Display CONN)    |

- **Switronic IT-1501-G**
  - Joystick module to allow Braccio ++ manoeuvre. It is possible to interconnect via J3 & J4 Board Connector found on Arduino® Braccio Carrier.
    | Compatible Connector |
    | :------------------: |
    | J3 & J4 Board CONN   |

### Connectors & I/O Port
- **Display Connector J1**
  - Connector available to interface the JAX133T-IF05 display module.
    | Connector Ref.      | Maximum Electrical Operating Range   | Maximum Temperature Operating Range   |
    | ------------------- | ------------------------------------ | ------------------------------------- |
    |  J1                 |  0.5A per Contact                    |  105°C                                |
- **J3 & J4 Board Connector**
  - Board splitter which allows to interface display and joystick at a distance, from which all the motor wire interfaces arrive.
- **Molex 44914-0601**
  - Rectangular power connector with 6 contacts. Available for external power supply and for servo line.
    | No. Connectors   | Maximum Electrical Operating Range   | Maximum Temperature Operating Range   |
    | ---------------- | ------------------------------------ | ------------------------------------- |
    |  2               |  600V @ 8.5A                         |  -40°C ~ +105°C                       |
- **Adam Equipment LHA-04-TS**
  - Connectors available to interface with motors. RS485 smart motors compatible, derived by configuration of 4x SR418D and 2x SR312 models. Lead free and RoHS Compliant.
    | No. Connectors   | Maximum Electrical Operating Range   | Maximum Temperature Operating Range   |
    | ---------------- | ------------------------------------ | ------------------------------------- |
    |  6               |  250VAC @ 3A                         |  -25°C ~ +85°C                        |
- **USB-C® Port**
  - USB Type-C® port available to enable programming, and power supply source port under USB PD 3.0 for Arduino® Braccio Carrier.
    | USB Standard    | USB Power Delivery Rev.    | USB Type               | Purpose                           |
    | --------------- | -------------------------- | ---------------------- | --------------------------------- |
    |  3.1            |  3.0                       |  Type C (Reversible)   |  Power Supply                     |
- **ESLOV Connector**
  - The connector provides the capability of module's automatic configuration and handle the sleep state for low power mode. Connector is designated with J2 reference, providing 5 pins for interrupt and I2C protocol at 5V.
    | Connector Ref.      | Operating Voltage      | Line Feature                 |
    | ------------------- | ---------------------- | ---------------------------- |
    |  J2                 |  5V                    |  I2C Protocol + Interrupt    |

## Ratings
### Recommended Operating Conditions
| Description                                      | Min    | Max   |
| ------------------------------------------------ | :----: | :---: |
| Conservative thermal limits for the whole board: | -40 °C | 85 °C |

## Functional Overview
### Block Diagram
![Arduino Braccio Carrier System Block Diagram](assets/System_Block_Diagram_Braccio_Carrier.jpg)

The USB powers the Arduino® Nano RP2040 Connect which is the heart of the Braccio Carrier as it stores the programs responsible for the functioning of the whole system. The Nano is connected to the joystick which is the input peripheral and LED display screen which is the output peripheral of the microcontroller. Another power supply via USB-C® powers the connected motors which constitute the entire robotics functionality the system. RS485 Transceiver signals the motor connector for the precise motihe motors according to the input given by the user.

![Arduino® Braccio Carrier Block Diagram](assets/Block_Diagram_Braccio_Carrier.svg)

### Board Topology
![Arduino® Braccio Carrier Top View](assets/braccio-connectors.svg)

| **Ref.** | **Description**                    | **Ref.** | **Description**                      |
| -------- | ---------------------------------- | -------- | ------------------------------------ |
| PB1     | Pushbutton SMD                      | PB2      | Mini Joystick                        |
| U1      | 24 Bit I2C SMBUS I/O                | U4       | Line Transceiver                     |
| J1      | CONN FPC SMD                        | J2       | CONN JST 5 POS                       |
| J3      | Board Connector                     | J4       | Board Connector                      |
| U3      | Power Supply Support Circuit        | J8       | USB 3.1 Type C (USB PD 3.0)          |

### Processor
Primary processor of Arduino® Braccio Carrier is the processor of the Arduino® Nano RP2040 Connect microcontroller mounted on it. The microcontroller controls every operation of the Braccio Carrier for the target applications via connections with motors and LED display screen.

### Power Tree
![Braccio Carrier Power Tree](assets/Power_Tree_Braccio_Carrier.jpg)

## Board Operation
### Getting Started - IDE
If you want to program your Arduino® Braccio Carrier while offline you need to install the Arduino® Desktop IDE **[1]** To connect the Arduino® Braccio Carrier to your computer, you’ll need a Type-B USB cable. This also provides power to the board, as indicated by the LED.

### Sample Sketches
Sample sketches for the Arduino® Braccio Carrier can be found either in the “Examples” menu in the Arduino® IDE

### Online Resources
Now that you have gone through the basics of what you can do with the board you can explore the endless possibilities it provides by checking exciting projects on Project Hub **[2]**, the Arduino® Library Reference **[3]** and the online store **[4]** where you will be able to complement your board with sensors, actuators and more.

### Board Recovery
All Arduino® boards have a built-in bootloader which allows flashing the board via USB. In case a sketch locks up the processor and the board is not reachable anymore via USB it is possible to enter bootloader mode by double-tapping the reset button right after power up.

## Connector Pinouts
![Braccio Carrier Pinout](assets/braccio-pinout.png)

## Mechanical Information
### Board Outline
![Outline](assets/braccio-outline.svg)

### Board Mount Holes
![Mount Holes](assets/braccio-mount.svg)

## Certifications
### Declaration of Conformity CE DoC (EU)
We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).

### Declaration of Conformity to EU RoHS & REACH 211 01/19/2021
Arduino® boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.

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

Arduino® Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration
As a global supplier of electronic and electrical components, Arduino® is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino® does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino® has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

### FCC Caution
Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

(1) This device may not cause harmful interference

(2) this device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with minimum distance 20cm between the radiator & your body.

English:
User manuals for license-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual or alternatively on the device or both. This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions:

(1) this device may not cause interference

(2) this device must accept any interference, including interference that may cause undesired operation of the device.

French:
Le présent appareil est conforme aux CNR d’Industrie Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes:

(1) l’ appareil nedoit pas produire de brouillage

(2) l’utilisateur de l’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

**IC SAR Warning:**

English
This equipment should be installed and operated with minimum distance 20 cm between the radiator and your body.

French
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 201453/EU. This product is allowed to be used in all EU member states.

| Frequency bands | Maximum output power (ERP) |
| --------------- | -------------------------- |
| 2400-2483.5 Mhz | 17 dBm                     |

## Company Information
| Company name    | Arduino SRL                                     |
| --------------- | ----------------------------------------------- |
| Company Address | Via Andrea Appiani 25 - 20900 Monza (MB), Italy |

## Reference Documentation
| Ref                       | Link                                                                     |
| ------------------------- | ------------------------------------------------------------------------ |
| Arduino IDE (Desktop)     | https://www.arduino.cc/en/Main/Software                                  |
| Project Hub               | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending |
| Library Reference         | https://www.arduino.cc/reference/en/libraries/                           |
| Online Store              | https://store.arduino.cc/                                                |

## Revision History
| **Date**   | **Revision** | **Changes**                      |
| ---------- | ------------ | -------------------------------- |
| 23/03/2022 | 1            | First Release                    |
| 25/10/2022 | 2            | Minor markdown and heading fixes |