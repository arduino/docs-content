---
identifier: ABX00071
title: Arduino® Nano 33 BLE Rev2
type: maker
---

![](assets/featured.jpg)

# Description

The **Arduino Nano 33 BLE Rev2**\* is a miniature-sized module containing a NINA B306 module, based on Nordic nRF52480 and containing a Cortex M4F. The BMI270 and BMM150 jointly provide a 9-axis IMU. The module can either be mounted as a DIP component (when mounting pin headers) or as a SMT component, directly soldering it via the castellated pads.

\*The Arduino Nano 33 BLE Rev2 product has two SKUs:
* Without headers (ABX00071)
* With headers (ABX00072)

# Target Areas

Maker, enhancements, IoT application

# Features

- **NINA B306 Module**
  - **Processor**
    - 64 MHz Arm® Cortex®-M4F (with FPU)
    - 1 MB Flash + 256 KB RAM
  - **Bluetooth® 5 multiprotocol radio**
    - 2 Mbps
    - CSA #2
    - Advertising Extensions
    - Long Range
    - +8 dBm TX power
    - -95 dBm sensitivity
    - 4.8 mA in TX (0 dBm)
    - 4.6 mA in RX (1 Mbps)
    - Integrated balun with 50 Ω single-ended output
    - IEEE 802.15.4 radio support
    - Thread
    - Zigbee
  - **Peripherals**
    - Full-speed 12 Mbps USB
    - NFC-A tag
    - Arm CryptoCell CC310 security subsystem
    - QSPI/SPI/TWI/I²S/PDM/QDEC
    - High speed 32 MHz SPI
    - Quad SPI interface 32 MHz
    - EasyDMA for all digital interfaces
    - 12-bit 200 ksps ADC
    - 128 bit AES/ECB/CCM/AAR co-processor
- **BMI270** 6-axis IMU (Accelerometer and Gyroscope)
  - 16-bit
  - 3-axis accelerometer with ±2g/±4g/±8g/±16g range
  - 3-axis gyroscope with ±125dps/±250dps/±500dps/±1000dps/±2000dps range
- **BMM150** 3-axis IMU (Magnetometer)
  - 3-axis digital geomagnetic sensor
  - 0.3μT resolution
  - ±1300μT (x,y-axis), ±2500μT (z-axis)
- **MP2322** DC-DC
  - Regulates input voltage from up to 21V with a minimum of 65% efficiency @minimum load
  - More than 85% efficiency @12V

# Contents

## The Board

As all Nano form factor boards, Nano 33 BLE Rev2 does not have a battery charger but can be powered through USB or headers.

**NOTE:** Arduino Nano 33 BLE Rev2 only supports 3.3V I/Os and is **NOT** 5V tolerant so please make sure you are not directly connecting 5V signals to this board or it will be damaged. Also, as opposed to Arduino Nano boards that support 5V operation, the 5V pin does NOT supply voltage but is rather connected, through a jumper, to the USB power input.

### Ratings

#### Recommended Operating Conditions

| Symbol | Description                                      | Min             | Max            |
|--------|--------------------------------------------------|-----------------|----------------|
|        | Conservative thermal limits for the whole board: | -40 °C ( 40 °F) | 85°C ( 185 °F) |

### Power Consumption

| Symbol | Description                         | Min | Typ | Max | Unit |
|--------|-------------------------------------|-----|-----|-----|------|
| PBL    | Power consumption with busy loop    |     | TBC |     | mW   |
| PLP    | Power consumption in low power mode |     | TBC |     | mW   |
| PMAX   | Maximum Power Consumption           |     | TBC |     | mW   |


<div style="page-break-after: always;"> </div>

## Functional Overview

### Board Topology

Top:
![Board topology top](assets/BLE_Rev2_Top.png)

| **Ref.** | **Description**                                   | **Ref.** | **Description**                  |
|----------|---------------------------------------------------|----------|----------------------------------|
| U1       | NINA-B306 Module Bluetooth® Low Energy 5.0 Module | U6       | MP2322GQH Step Down Converter    |
| U2       | BMI270 Sensor IMU                                 | PB1      | IT-1185AP1C-160G-GTR Push button |
| U7       | BMM150 Magnetometer IC                            | DL1      | Led L                            |

Bottom:
![Board topology bot](assets/BLE_Rev2_Bottom.png)

| **Ref.** | **Description** | **Ref.** | **Description** |
|----------|-----------------|----------|-----------------|
| SJ1      | VUSB Jumper     | SJ2      | D7 Jumper       |
| SJ3      | 3v3 Jumper      | SJ4      | D8 Jumper       |

### Processor

The Main Processor is an Arm® Cortex®-M4F running at up to 64MHz. Most of its pins are connected to the external headers however some are reserved for internal communication with the wireless module and the on-board internal I<sup>2</sup>C peripherals (IMU and Crypto).

**NOTE**: As opposed to other Arduino Nano boards, pins A4 and A5 have an internal pull-up and default to be used as an I<sup>2</sup>C Bus so usage as analog inputs is not recommended.

### IMU

The Arduino Nano 33 BLE Rev2 provides IMU capabilities with 9-axis, through a combination of the BMI270 and BMM150 ICs. The BMI270 includes both a three-axis gyroscope as well as a three-axis accelerometer, while the BMM150 is capable of sensing magnetic field variations in all three dimensions. The information obtained can be used for measuring raw movement parameters as well as for machine learning.

### Power Tree

The board can be powered via USB connector, V<sub>IN</sub> or V<sub>USB</sub> pins on headers.

![Power tree](assets/Nano_33_BLE_Rev2_Power_Tree.svg)

**NOTE:** Since V<sub>USB</sub> feeds V<sub>IN</sub> via a Schottky diode and a DC-DC regulator specified minimum input voltage is 4.5V the minimum supply voltage from USB has to be increased to a voltage in the range between 4.8V to 4.96V depending on the current being drawn.

### Block Diagram

![Block Diagram](assets/Nano_33_BLE_Rev2_Block_Diagram.svg)

## Board Operation

### Getting Started - IDE

If you want to program your Arduino Nano 33 BLE Rev2 while offline you need to install the Arduino Desktop IDE [1] To connect the Arduino Nano 33 BLE Rev2 to your computer, you’ll need a Micro-B USB cable. This also provides power to the board, as indicated by the LED.

### Getting Started - Arduino Web Editor

All Arduino boards, including this one, work out-of-the-box on the Arduino Web Editor, by just installing a simple plugin.

The Arduino Web Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow to start coding on the browser and upload your sketches onto your board.

### Getting Started - Arduino IoT Cloud

All Arduino IoT-enabled products are supported on Arduino IoT Cloud which allows you to Log, graph and analyze sensor data, trigger events, and automate your home or business.

### Sample Sketches

Sample sketches for the Arduino Nano 33 BLE Rev2 can be found either in the “Examples” menu in the Arduino IDE or in the “Documentation” section of the Arduino Pro website.

### Online Resources

Now that you have gone through the basics of what you can do with the board you can explore the endless possibilities it provides by checking exciting projects on ProjectHub, the Arduino Library Reference and the online store where you will be able to complement your board with sensors, actuators and more.

### Board Recovery

All Arduino boards have a built-in bootloader which allows flashing the board via USB. In case a sketch locks up the processor and the board is not reachable anymore via USB it is possible to enter bootloader mode by double-tapping the reset button right after powering up the board.

## Connector Pinouts

![Pinout](assets/pinout.png)

### USB

| Pin | **Function** | **Type**     | **Description**                                                                        |
|-----|--------------|--------------|----------------------------------------------------------------------------------------|
| 1   | VUSB         | Power        | Power Supply Input. If board is powered via VUSB from header this is an Output **(1)** |
| 2   | D-           | Differential | USB differential data -                                                                |
| 3   | D+           | Differential | USB differential data +                                                                |
| 4   | ID           | Analog       | Selects Host/Device functionality                                                      |
| 5   | GND          | Power        | Power Ground                                                                           |

### Headers

The board exposes two 15-pin connectors which can either be assembled with pin headers or soldered through castellated vias.

| Pin | **Function** | **Type**     | **Description**                                                                     |
|-----|--------------|--------------|-------------------------------------------------------------------------------------|
| 1   | D13          | Digital      | GPIO                                                                                |
| 2   | +3V3         | Power Out    | Internally generated power output to external devices                               |
| 3   | AREF         | Analog       | Analog Reference; can be used as GPIO                                               |
| 4   | A0/DAC0      | Analog       | ADC in/DAC out; can be used as GPIO                                                 |
| 5   | A1           | Analog       | ADC in; can be used as GPIO                                                         |
| 6   | A2           | Analog       | ADC in; can be used as GPIO                                                         |
| 7   | A3           | Analog       | ADC in; can be used as GPIO                                                         |
| 8   | A4/SDA       | Analog       | ADC in; I2C SDA; Can be used as GPIO **(1)**                                        |
| 9   | A5/SCL       | Analog       | ADC in; I2C SCL; Can be used as GPIO **(1)**                                        |
| 10  | A6           | Analog       | ADC in; can be used as GPIO                                                         |
| 11  | A7           | Analog       | ADC in; can be used as GPIO                                                         |
| 12  | VUSB         | Power In/Out | Normally NC; can be connected to VUSB pin of the USB connector by shorting a jumper |
| 13  | RST          | Digital In   | Active low reset input (duplicate of pin 18)                                        |
| 14  | GND          | Power        | Power Ground                                                                        |
| 15  | VIN          | Power In     | Vin Power input                                                                     |
| 16  | TX           | Digital      | USART TX; can be used as GPIO                                                       |
| 17  | RX           | Digital      | USART RX; can be used as GPIO                                                       |
| 18  | RST          | Digital      | Active low reset input (duplicate of pin 13)                                        |
| 19  | GND          | Power        | Power Ground                                                                        |
| 20  | D2           | Digital      | GPIO                                                                                |
| 21  | D3/PWM       | Digital      | GPIO; can be used as PWM                                                            |
| 22  | D4           | Digital      | GPIO                                                                                |
| 23  | D5/PWM       | Digital      | GPIO; can be used as PWM                                                            |
| 24  | D6/PWM       | Digital      | GPIO, can be used as PWM                                                            |
| 25  | D7           | Digital      | GPIO                                                                                |
| 26  | D8           | Digital      | GPIO                                                                                |
| 27  | D9/PWM       | Digital      | GPIO; can be used as PWM                                                            |
| 28  | D10/PWM      | Digital      | GPIO; can be used as PWM                                                            |
| 29  | D11/MOSI     | Digital      | SPI MOSI; can be used as GPIO                                                       |
| 30  | D12/MISO     | Digital      | SPI MISO; can be used as GPIO                                                       |

### Debug

On the bottom side of the board, under the communication module, debug signals are arranged as 3x2 test pads with 100 mil pitch with pin 4 removed. Pin 1 is depicted in Figure 3 – Connector Positions

| Pin | **Function** | **Type**   | **Description**                                                   |
|-----|--------------|------------|-------------------------------------------------------------------|
| 1   | +3V3         | Power Out  | Internally generated power output to be used as voltage reference |
| 2   | SWD          | Digital    | nRF52480 Single Wire Debug Data                                   |
| 3   | SWCLK        | Digital In | nRF52480 Single Wire Debug Clock                                  |
| 5   | GND          | Power      | Power Ground                                                      |
| 6   | RST          | Digital In | Active low reset input                                            |

## Mechanical Information

### Board Outline and Mounting Holes

The board measures are mixed between metric and imperial. Imperial measures are used to maintain a 100 mil pitch grid between pin rows to allow them to fit a breadboard whereas board length is Metric

![Board layout](assets/Outline.png)

## Certifications

### Declaration of Conformity CE DoC (EU)

We declare under our sole responsibility that the products above conform with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).

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

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (<https://echa.europa.eu/web/guest/candidate-list-table>), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration

As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regard to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder or as a component in metal alloys. As part of our reasonable due diligence, Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

## FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

(1) This device may not cause harmful interference

 (2) this device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with a minimum distance of 20cm between the radiator & your body.

English:
User manuals for license-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual, alternatively on the device or both. This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions:

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

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

Hereby, Arduino S.r.l. declares that this product complies with essential requirements and other relevant provisions of Directive 2014/53/EU. This product is allowed to be used in all EU member states.

| Frequency bands | Maximum output power (ERP) |
|-----------------|----------------------------|
| 863-870Mhz      | TBD                        |

## Company Information

| Company name    | Arduino S.r.l                           |
|-----------------|-----------------------------------------|
| Company Address | Via Andrea Appiani 25 20900 MONZA Italy |

## Reference Documentation

| Reference                 | **Link**                                                                                                                                                             |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Arduino IDE (Desktop)     | <https://www.arduino.cc/en/software>                                                                                                                                   |
| Arduino IDE (Cloud)       | <https://create.arduino.cc/editor>                                                                                                                                     |
| Cloud IDE Getting Started | <https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-4b3e4a>                                                                  |
| Forum                     | <http://forum.arduino.cc/>                                                                                                                                             |
| Nina B306                 | <https://content.u-blox.com/sites/default/files/NINA-B3_DataSheet_UBX-17052099.pdf>                                                                                    |                                                                                                               |
| ProjectHub                | <https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending>                                                                                             |
| Library Reference         | <https://www.arduino.cc/reference/en/>                                                                                                                                 |

## Revision History

| Date       | **Revision** | **Changes**                           |
|------------|--------------|---------------------------------------|
|            |              |                                       |

