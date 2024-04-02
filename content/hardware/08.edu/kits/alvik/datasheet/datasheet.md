---
identifier: AKX00066
title: Arduino® Alvik
type: educational
---
![](assets/perspective_top.jpg)

# Description
Arduino Alvik is a powerful and versatile robot car specifically designed for programming and robotics education.

Powered by [Arduino® Nano ESP32](https://docs.arduino.cc/hardware/nano-esp32/), Arduino Alvik offers a diverse learning paths through different programming languages, including MicroPython, Arduino C, and block-based coding, and it enables different possibilities to explore robotics, IoT and AI.

# Target areas:
Maker, Edu, MicroPython

# Features

* **Core**
  * STM32 ARM Cortex-M4 32 Bit
* **Controller**
  * Arduino NANO ESP32
* **Connectivity**
  * Wi-Fi®
  * Bluetooth® LE
* **Sensors**
  * RGB Color detection
  * ToF 8x8 Array - up to 350 cm
  * IMU - 6 degree
  * 3x Line follower
  * 7x Touch sensor
* **Motors**
  * High precision with magnetic encoder
  * Up to 15 cm/s
* **Extensions**
  * Servo motor
  * I2C Grove
  * QWIIC
  * Lego Technic
  * M3 Screws

# Contents

## Overview
Arduino Alvik is battery powered and comes with 2 MCUs:

 - at the core there is the STM32 ARM Cortex-M4 that controls all the sensors and actuators
 - at the top a Nano ESP32 that can communicate with STM32 trough a set of dedicated APIs

![](assets/datasheet_main_components.png)

## Tech Specs
![](assets/alvik_components.png)

### MCUs

| **MCU**             | **Product page**                                                                                           | **Datasheet**                                                               |
|---------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| STM32F411RC         | [link](https://www.st.com/en/microcontrollers-microprocessors/stm32f411rc.html#st_description_sec-nav-tab) | [link](assets/STM32_datasheet.pdf)                                          |
| Arduino® Nano ESP32 | [link](https://docs.arduino.cc/hardware/nano-esp32/)                                                       | [link](https://docs.arduino.cc/resources/datasheets/ABX00083-datasheet.pdf) |

### Inputs

| **Description**             | **Part Name** | **Product page**                                                                                                   | **Datasheet**                          |
|-----------------------------|---------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Color detection             | APDS-9660     | [link](https://www.broadcom.com/products/optical-sensors/integrated-ambient-light-and-proximity-sensors/apds-9960) | [link](assets/APDS-9960_datasheet.pdf) |
| IMU                         | LSM6DSOXTR    | [link](https://www.st.com/en/mems-and-sensors/lsm6dsox.html)                                                       | [link](assets/LSM6_datasheet.pdf)      |
| Time of Flight              | VL53L7CXV0GC  | [link](https://www.st.com/en/imaging-and-photonics-solutions/vl53l7cx.html)                                        | [link](assets/VL53_datasheet.pdf)      |
| Capacitive Touch Controller | AT42QT2120    | [link](https://www.microchip.com/en-us/product/AT42QT2120)                                                         | [link](assets/at42qt2120.pdf)          |
| Line Follower Arrays        | Custom made   |                                                                                                                    |                                        |


Attach to the Capacitive Touch Controller there are seven capacitive buttons on the top of the main board and in addition there is a line follower array made up by three phototransistor and five infrared LEDs.
The three phototransistor are link directly to the analog ports of the STM32.

### Outputs

| **Description** | **Info**                                     |
|-----------------|----------------------------------------------|
| RGB LED Left    | 3 channel LED                                |
| RGB LED Right   | 3 channel LED                                |
| Motor Left      | High precision motors with magnetic encoder  |
| Motor Right     | High precision motors with magnetic encoder  |

The datasheet of the motors is [here](assets/motor_specs.pdf)

The two motors are drived by the MAX22211 driver:

| **Description**   | **Part Name** | **Product page**                                         | **Datasheet**               |
|-------------------|---------------|----------------------------------------------------------|-----------------------------|
| Dual Motor Driver | MAX22211      | [link](https://www.analog.com/en/products/max22211.html) | [link](assets/max22211.pdf) |



### Connectors

The connectors are placed in the back of the robot, the pinout is shown in the following image:

![connectors pinout](assets/datasheet_connectors.png)

### Power

The power distribution in the robot is explained by the following scheme:

![power scheme](assets/power.png)

There are three level of power:

| **Level** | **Description**                                                                     |
|-----------|-------------------------------------------------------------------------------------|
| +3V7      | From the battery, the reference level is 3.7V but it can goes from 3.0V to 4.2V |
| +5V       | After the Boost Converter                                                           |
| +3V3      | After the Step Down Converter                                                       |

## Functional Overview

### Block Diagram

![block diagram](assets/block_diagram.png)

## Mechanical Information

![parts](assets/mech_parts.png)

| **Part**             | **q.ty** |
|----------------------|:--------:|
| Main PCB             |     1    |
| Front PCB            |     1    |
| Arduino Nano ESP32   |     1    |
| INOX M3 x 5mm        |     5    |
| 18650 Li-Ion Battery |     1    |
| Main Chassis         |     1    |
| Ball caster holder   |     1    |
| Inox stell ball 9mm  |     1    |
| Motor holder         |     2    |
| Motors               |     2    |
| Rubber wheel         |     2    |
| 2x6mm screw          |     2    |
| Battery panel        |     1    |

## Certifications

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
| Bis(2-Ethylhexyl} phthalate (DEHP)     | 1000                    |
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

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40 ℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 201453/EU. This product is allowed to be used in all EU member states.

## Company Information

| Company name    | Arduino S.r.l.                                |
| --------------- | --------------------------------------------- |
| Company Address | Via Andrea Appiani, 25 Monza, MB, 20900 Italy |


## Reference Documentation

| Ref                          | Link                                                                                            |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| Arduino IDE (Desktop)        | <https://www.arduino.cc/en/Main/Software>                                                       |
| Arduino Web Editor (Cloud)   | <https://create.arduino.cc/editor>                                                              |
| Web Editor - Getting Started | <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor> |
| Project Hub                  | <https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending>                      |
| Library Reference            | <https://github.com/arduino-libraries/>                                                         |
| Online Store                 | <https://store.arduino.cc/>                                                                     |

## Change Log

| **Date**   | **Changes**                                            |
| ---------- | ------------------------------------------------------ |
| 08/06/2023 | Release                                                |
| 09/01/2023 | Update power tree flowchart.                           |
| 09/11/2023 | Update SPI section, update analog/digital pin section. |
| 11/06/2023 | Correct company name, correct VBUS/VUSB                |
| 11/09/2023 | Block Diagram Update, Antenna Specifications           |
| 11/15/2023 | Ambient temperature update                             |
| 11/23/2023 | Added label to LP modes                                |




