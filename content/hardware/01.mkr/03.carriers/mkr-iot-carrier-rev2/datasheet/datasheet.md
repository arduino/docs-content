---
identifier: ABX00073
title: Arduino® MKR IoT Carrier
type: maker
revision: Rev2
variant: Rev2
---

![](assets/featured.png)

# Description
The **MKR IoT Carrier Rev2** provides infinite possibilities for IoT projects, including a TFT display to display information, Grove connectors and multiple sensors.

The integrated sensors, circuits and display leave you free to focus on programming and prototyping your ideas.

# Target areas:
IoT applications, MKR hobbyists

# Features

***Note: This board is passive and requires a MKR board to function.***

***Requirements: This device require the library Arduino_MKRIoTCarrier version to be 2.0.0 or later in order to function***

* **Grove Connectors**
  * Easy interface with wide range of Grove modules and sensors
  * 2x analog sensor input
  * 1x I2C interface

* **ST LSM6DSOXTR 6-axis IMU**
  * 3D Gyroscope
    * ±2/±4/±8/±16 g full scale
  * 3D Accelerometer
    * ±125/±250/±500/±1000/±2000 dps full scale
  * Advanced pedometer, step detector and step counter
  * Significant Motion Detection, Tilt detection
  * Standard interrupts: free-fall, wake-up, 6D/4D orientation, click and double-click
  * Programmable finite state machine: accelerometer, gyroscope and external sensors
  * Machine Learning Core
  * Embedded temperature sensor

* **Rounded 1.3” TFT Display**
  * 240 x 240 resolution
  * 36 x 40 mm

- **Bosch BME688** Environmental sensing with Artificial Intelligence
  - Operating range
    - Pressure: 300-1100 hPa
    - Humidity: 0-100%
    - Temperature: -40 - +85°C
  - eNose Gas sensor
    - Sensor-to-sensor deviation (IAQ): ± 15% ± 15 IAQ
    - Standard scan speed: 10.8 s/scan
    - Electric charge for standard scan: 0.18 mAh (5 scans - 1 min)
    - Major Sensor outputs
      - Index for air quality (IAQ)
      - bVOC- & CO2-equivalents (ppm)
      - Gas scan result (%)
      - Intensity level

* **Broadcom APDS-9660 RGB and Gesture Sensor**
  * Ambient light and RGB Colour Sensing
  * Proximity Sensing
  * Gesture Detection
  * UV/IR Blocking Filter
  * I2C interface to Arduino MKR board

* **Relays**
  * 2x KEMET EE2-5NU-L relays
  * 5V Coil voltage
  * 2A Current
  * 220V DC, 250V AC
  * Non-latching
  * Common, normally open and normally closed contacts
  * LED Status Indicator

* **Peripherals**
  * 5x Capacitive buttons
  * Buzzer
  * 5x Digital RGB LEDs
  * Rounded OLED 1,3” Display
  * 5x Capacitive qTouch buttons

* **Memory**
  * Micro SD Card

* **Power**
  * Li-ion 18650 3.7 v battery holder
  * USB Battery charging via MKR Board (Runs up to 48h with a 3.7v 2500mAh)

* **I/O**
  * All sensors feature wake up function
  * 2x Analog Grove connectors
  * 1x I2C Grove connector
  * 2x relay connector

* **Safety information**
  * Class A

# Contents

## The Board

### Application Examples

**Light controller:** Control your house lightning with the **MKR IoT Carrier Rev2**, using the RGB light sensor. This feature identifies the general amount of light in a room or environment and adapts. If the board is connected to Wi-Fi®, you can manage and control your device remotely on a smartphone via the IoT Cloud.

**Light and water controller for greenhouse:** With moisture sensor, pressure sensor and temperature the IoT Carrier can evaluate and recognize the moisture of the soil, depending on air humidity and sun. Through the various sensors, it can reconstruate suitable climate (e.g. tropical) with the help of heaters and relays to increase the humidity. It can also be programmed with a watering system thanks to the relays.

**Weather station:** With temperature sensor, pressure sensor, humidity sensor and light sensors, you can easily use your IoT carrier as a local weather station. The various sensors can via sensors collect statistics about the different variables required to display weather.

### Accessories

***(Not Included)***
* 18650 Li-ion battery
* <u>[Grove sensors](https://search.arduino.cc/search/?q=Grove%20Sensors&tab=store)</u>
* SD Card

### Related Products

* <u>[Arduino® MKR WiFi 1010 (SKU: ABX00023)](https://store.arduino.cc/products/arduino-mkr-wifi-1010)</u>
* <u>[Arduino® MKR Zero (SKU: ABX00012)](https://store.arduino.cc/products/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data)</u>
* <u>[Arduino® MKR WAN 1310 (SKU: MKRWAN1310WANT)](https://store.arduino.cc/products/arduino-mkr-wan-1310)</u>
* <u>[Arduino® MKR GSM 1400 (SKU: MKRGSM1400WANT)](https://store.arduino.cc/products/arduino-mkr-gsm-1400)</u>
* <u>[Arduino® MKR NB 1500 (SKU: MKRNB1500WANT)](https://store.arduino.cc/products/arduino-mkr-nb-1500)</u>


## Functional Overview

### Board Topology

#### Top View

![Top view - components](assets/top_view.svg)

| **Ref.** | **Description**                        | **Ref.** | **Description**                     |
| -------- | -------------------------------------- | -------- | ----------------------------------- |
| U1       | LSM6DSOXTR 6-axis IMU IC               | U2       | APDS-9660 RGB and Gesture Sensor IC |
| U4       | Bosch BME688 Environmental Sensor IC   | L0-L4    | APA1022020-2018 RGB LED IC          |
| J6       | FH26W-45S-0.3SHW(60) Display Connector | PB1      | Reset push-button                   |


#### Bottom View

![Bottom view](assets/bottom_view.svg)

| **Ref.**  | **Description**                       | **Ref.** | **Description**                   |
| --------- | ------------------------------------- | -------- | --------------------------------- |
| J2, J3    | Analog Grove Connectors               | J4       | I2C Grove Connector               |
| J11       | B2B-PH-SM4-TB(LF)(SN) Power Connector | J9, J10  | 1771033 3-pin Relay Connector     |
| JDIGITAL1 | MKR Power and Digital Pin Connector   | JANALOG1 | MKR AREF and Analog Pin Connector |
| S1, S2    | EE2-5NU-L 2A 250V Mechanical Relay    | M1       | Buzzer                            |
| J1        | Micro SD Module                       | J7, J8   | Li-Ion 18650 Holder               |

### Power Tree
The **MKR IoT Carrier Rev2** makes use of the power management features of the Arduino MKR boards to power itself as well as to interface with the Li-Ion battery.

![Power tree](assets/Power_Tree_MKR_IoT_Carrier.png)

## Board Operation

### Getting Started - IDE
If you want to program your **MKR IoT Carrier Rev2** while offline you need to install the Arduino Desktop IDE <sup>[**[1]**](#10-reference-documentation)</sup>. To connect the **MKR IoT Carrier Rev2** to your computer, you’ll need a Micro-B USB cable. This also provides power to the board, as indicated by the LED.

### Getting Started - Arduino Web Editor
All Arduino boards, including this one, work out-of-the-box on the Arduino Web Editor <sup>[**[2]**](#10-reference-documentation)</sup>, by just installing a simple plugin.

The Arduino Web Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow <sup>[**[3]**](#10-reference-documentation)</sup> to start coding on the browser and upload your sketches onto your board.

### Getting Started - Arduino Cloud
All Arduino IoT enabled products are supported on Arduino Cloud which allows you to log, graph and analyze sensor data, trigger events, and automate your home or business.

### Sample Sketches
Sample sketches for the **MKR IoT Carrier Rev2** can be found either in the “Examples” menu in the Arduino IDE and further documentation can be found in Arduino Documentation <sup>[**[7]**](#10-reference-documentation)</sup> which also contains links to the troubleshooting articles.

### Online Resources
Now that you have gone through the basics of what you can do with the board you can explore the endless possibilities it provides by checking exciting projects on ProjectHub <sup>[**[4]**](#10-reference-documentation)</sup>, the Arduino Library Reference <sup>[**[5]**](#10-reference-documentation)</sup> and the online store <sup>[**[6]**](#10-reference-documentation)</sup> where you will be able to complement your board with sensors, actuators and more.

### Board Recovery
All Arduino boards have a built-in bootloader which allows flashing the board via USB. In case a sketch locks up the processor and the board is not reachable anymore via USB it is possible to enter bootloader mode by double-tapping the reset button right after power up.

## Connector Pinouts

![Pinout](assets/Pinout.png)

Detailed information on the pinouts are available in a separate document: <u>[Docs Arduino - MKR IoT Carrier Rev2 pinout](https://docs.arduino.cc/resources/pinouts/ABX00073-full-pinout.pdf)</u>

### Battery Clips

|  Pin  | **Function** | **Type** | **Description**                 |
| :---: | :----------: | :------: | :------------------------------ |
|   1   |     GND      |  Power   | Ground                          |
|   2   |     VBAT     |  Power   | Positive 18650 Battery Terminal |

### Grove Connectors
#### A0

|  Pin  | **Function** | **Type** | **Description**  |
| :---: | :----------: | :------: | ---------------- |
|   1   |     AN0      |  Analog  | Analog Input 0   |
|   2   |      NC      |    NC    | Not Connected    |
|   3   |    +3.3V     |  Power   | +3.3V power rail |
|   4   |     GND      |  Power   | Ground           |

#### A6

|  Pin  | **Function** | **Type** | **Description**  |
| :---: | :----------: | :------: | ---------------- |
|   1   |     AN6      |  Analog  | Analog Input 6   |
|   2   |      NC      |    NC    | Not Connected    |
|   3   |    +3.3V     |  Power   | +3.3V power rail |
|   4   |     GND      |  Power   | Ground           |

#### I<sub>2</sub>C

|  Pin  | **Function** | **Type** | **Description**  |
| :---: | :----------: | :------: | ---------------- |
|   1   |     SCL      | Digital  | I2C Clock Signal |
|   2   |     SDA      | Digital  | I2C Data Signal  |
|   3   |    +3.3V     |  Power   | +3.3V power rail |
|   4   |     GND      |  Power   | Ground           |

### Relays
#### Relay 1 and 2

* Relay 1 driven by digital pin 1
* Relay 2 driven by digital pin 2


|  Pin  | **Function** | **Type** | **Description** |
| :---: | :----------: | :------: | --------------- |
|   1   |      NC      |  Switch  | Normally Closed |
|   2   |     COM      |  Switch  | Common          |
|   3   |      NO      |  Switch  | Normally Open   |

## Mechanical Information

### Board Outline / Mounting Holes

![Mechanical view](assets/mechanical.svg)

### Connectors

![Connectors positioning](assets/connectors.svg)

### Relays Connectors

![Left Side Relay positioning](assets/mechanical_left.svg)

## Ratings

### Absolute Maximum Ratings

| Symbol               | Description                              |  Min  |  Typ  |  Max  | Unit  |
| -------------------- | ---------------------------------------- | :---: | :---: | :---: | :---: |
| T<sub>Max</sub>      | Maximum thermal limit<sup>1</sup>        |  -30  |  20   |  85   |  °C   |
| VBatt<sub>Max</sub>  | Maximum input voltage from battery input |  3.2  |  3.7  |  4.3  |   V   |
| ARelay<sub>Max</sub> | Maximum current through relay switch     |   -   |   -   |   2   |   A   |
| P<sub>Max</sub>      | Maximum Power Consumption                |   -   |   -   | 5000  |  mW   |

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

3. This equipment should be installed and operated with minimum distance 20cm between the radiator & your body.

**English**:
User manuals for licence-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual or alternatively on the device or both. This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions:

(1) this device may not cause interference

(2) this device must accept any interference, including interference that may cause undesired operation of the device.

**French**:
Le présent appareil est conforme aux CNR d’Industrie Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes :

(1) l’ appareil nedoit pas produire de brouillage

(2) l’utilisateur de l’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

**IC SAR Warning:**

**English**
This equipment should be installed and operated with minimum distance 20 cm between the radiator and your body.

**French**:
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 2014/53/EU. This product is allowed to be used in all EU member states.

| Frequency bands | Maximum output power (ERP) |
| :-------------: | :------------------------: |
|   863-870Mhz    |          -3.22dBm          |

## Company Information

| Company name    | Arduino S.r.l.                             |
| --------------- | ------------------------------------------ |
| Company Address | Via Andrea Appiani,25 20900 MONZA (Italy） |

## Reference Documentation

| **Id** | **Ref**                   | **Link**                                                                                                   |
| ------ | ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1      | Arduino IDE (Desktop)     | <u>https://www.arduino.cc/en/Main/Software</u>                                                             |
| 2      | Arduino IDE (Cloud)       | <u>https://create.arduino.cc/editor</u>                                                                    |
| 3      | Cloud IDE Getting Started | <u>https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-4b3e4a</u> |
| 4      | Project Hub               | <u>https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending</u>                            |
| 5      | Library Reference         | <u>https://www.arduino.cc/reference/en/libraries/arduino_mkriotcarrier/</u>                                |
| 6      | Online Store              | <u>https://store.arduino.cc/mkr-iot-carrier-rev2</u>                                                       |
| 7      | Arduino Documentation     | <u>https://docs.arduino.cc/hardware/mkr-iot-carrier-rev2</u>                                               |

## Revision History

| **Date DD/MM/YY** | **Revision** | **Changes**                                           |
| ----------------- | ------------ | ----------------------------------------------------- |
| 20/02/2023        | 3            | Change grove connector power rail from +5.0V to +3.3V |
| 16/01/2023        | 2            | Update Pinout graphic                                 |
| 23/11/2022        | 1            | First Release                                         |