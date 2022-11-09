---
identifier: ABX00067
title: Arduino® GIGA R1 WiFi
type: maker
author: Ali Jahangiri
---

![](assets/featured.png)

# Description
The Arduino GIGA R1 WiFi brings the power of the STM32H7 to the Mega form factor, the first to include onboard Wi-Fi® and Bluetooth® connectivity. The board provides 75 digital input/output (12 with PWM capability), 14 analog inputs and 2 analog outputs (DAC) all easily accessibly via pin headers. The STM32 microprocessor with dual core Cortex® M7 and Cortex® M4, together with onboard memory and audio jack enables you to perform machine learning and signal processing on the edge.

# Target Areas
3D printing, Signal Processing, Maker, Robotics

# Features 
- **STM32H747XIH6** Microcontroller
  - Dual core
    - 32-bit Arm® Cortex®-M7 core with double-precision FPU and L1 cache up to 480 MHz
    - 32-bit Arm® 32-bit Cortex®-M4 core with FPU up to 240 MHz
  - Full set of DSP instructions
  - Memory Protection Unit (MPU)
- **Murata® 1DX** Wi-Fi®/Bluetooth® Module
  - Wi-Fi® 802.11b/g/n 65 Mbps
  - Bluetooth® Low Energy (BLE 5 via Cordio stack, BLE 4.2 via Arduino Stack)
  - Micro UFL connector for external antenna
- **Memory**
  - **STM32H747XI**: 
    - 2 MB Flash
    - 1 MB RAM
  - **MX25L12833FZ2I**: 
    - 16 MB NOR Flash
    - QSPI Interface
  - **AS4C4M16SA**
    - 8 MB SDRAM
- **I/O**
  -  Digital I/O Pins: 75
  -  Analog input pins: 14
  -  PWM pins: 12
  -  Analog output (DAC): 2
  -  USB Host: USB 2.0 A
  -  USB Peripheral: USB-c
  -  Logic level: 3.3V

# Contents

# The Board
## Application Examples

The Arduino GIGA R1 WiFi combines the best of the Portenta H7 and the Mega 2560. A generous amount of I/O easily accessible via pins allows for easy and fast testing of new ideas and solutions. The STM32H7 has ample power to handle machine learning. Your IoT projects can even benefit from the Arduino IoT Cloud, with the help of onboard secure element and wireless connectivity.

- **3D Printing:** The Mega form factor has been very popular for creating 3D printers. Connect sensors to the high resolution DAC interfaces to for high performance sensing of the 3D printing process. Together with the dual core computing power, control the printing process like never before. Monitor filament usage and print status locally over Bluetooth or from anywhere in the world with the Arduino IoT Cloud.

- **Audio Processing:** The Arduino GIGA R1 WiFi provides a 3.5 mm audio input/output to easily interact with audio signals in the environment. Analyse and create audio signals directly on the board. Connect a microphone and control a wide range of digital and analog devices. Create your own musical instrument, and change the note through the various inputs. Create a online concert with the Arduino IoT Cloud and connect with people all over the world.

- **Data acquisition device:** With two DAC inputs (as well as the audio input) with up to 12bit resolution you can create your own data acquisition device. Make your own multimeter or even an oscilloscope and create an online dashboard with the Arduino IoT Cloud. Design your own electrochemical experiments, apply custom current/voltage waveforms and check the status of your experiment from the comfort of your home.

## Accessories (Not Included)
- Micro UFL antenna
- USB-c cable
- USB 2.0 A cable

## Related Products
- Arduino Mega Proto Shield Rev3 (A000080)

<!--
### Solution Overview
![Example of a Arduino GIGA connected to a external audio source and micro UFL antenna](assets/gigaSolutionOverview.png)
-->

# Rating

## Recommended Operating Conditions
| Symbol          | Description                      | Min                | Typ | Max                | Unit |
| --------------- | -------------------------------- | ------------------ | --- | ------------------ | ---- |
| V<sub>IN</sub>  | Input voltage from VIN pad       | 6                  | 7.0 | 32                 | V    |
| V<sub>USB</sub> | Input voltage from USB connector | 4.8                | 5.0 | 5.5                | V    |
| V<sub>DD</sub>  | Input high-level voltage         | 0.7*V<sub>DD</sub> |     | V<sub>DD</sub>     | V    |
| V<sub>IL</sub>  | Input low-level voltage          | 0                  |     | 0.3*V<sub>DD</sub> | V    |
| T<sub>OP</sub>  | Operating Temperature            | -20                | 25  | 60                 | °C   |

**Note 1:** V<sub>DD</sub> controls the logic level and is connected to the 3.3V power rail. V<sub>AREF</sub> is for the analog logic.

## Power Consumption
| Symbol            | Description                                        | Min | Typ | Max | Unit |
| ----------------- | -------------------------------------------------- | --- | --- | --- | ---- |
| P<sub>STDBY</sub> | Average power consumption in standby               |     | TBC |     | mW   |
| P<sub>BLINK</sub> | Average power consumption with blink sketch sketch |     | TBC |     | mW   |
| P<sub>MAX</sub>   | Maximum power consumption                          |     | TBC |     | mW   |
# Functional Overview


## Block Diagram
![Arduino GIGA R1 WiFi Block Diagram](assets/GIGA_R1_WiFi_Block_Diagram.png)

## Board Topology
### Front View
![Top View of Arduino GIGA R1 WiFi](assets/gigaR1Top.png)

| **Ref.** | **Description**                       | **Ref.** | **Description**                     |
| -------- | ------------------------------------- | -------- | ----------------------------------- |
| U1       | STM32H7 Dual Core Microcontroller IC  | U2       | MX25L12833FZ2I 16 MB Flash IC       |
| U3       | AS4C4M16SA 8MB SDRAM IC               | U4       | ATECC608A-MAHDA-T Secure Element IC |
| U5       | LBEE5KL1DX-883 Wi-Fi/Bluetooth Module | U6       | MP2322GQH Buck Converter 3.3V IC    |
| U7       | MP2269GD-Z Buck Converter 5V IC       | JANALOG  | Analog input/output headers         |
| JDIGITAL | Digital input/output headers          | JSIDE    | Digital input/output headers        |
| SPI      | SPI headers                           | JTAG     | JTAG Headers                        |
| J2       | USB 2.0 A Host                        | J15      | 3.5 mm audio in/out                 |
| PB1      | RESET Button                          | PB2      | BOOT0 button                        |
| J14      | Micro UFL connector                   | J5       | Camera                              |
| J6       | Camera                                | DL1      | Power LED                           |
| DL2      | RGB SMLP34RGB2W3 Common anode LED     | J12      | CX90B-16P USB-c connector           |

### Back View
![Back View of Arduino GIGA R1 WiFi](assets/gigaR1Bottom.png)

## Processor
The Arduino GIGA R1 WiFi's main processor is the dual core STM32H747 (U1) including a Cortex® M7 running at 480 MHz and a Cortex® M4 running at 240 MHz. The two cores communicate via a Remote Procedure Call mechanism that allows calling functions on the other processor seamlessly.

## Wi-Fi®/Bluetooth® Connectivity
The Murata® LBEE5KL1DX-883 wireless module (U5) simultaneously provides Wi-Fi® and Bluetooth® connectivity in an ultra small package based on the Cypress CYW4343W. The IEEE802.11 b/g/n Wi-Fi® interface can be operated as an access point (AP), station (STA) or as a dual mode simultaneous AP/STA and supports a maximum transfer rate of 65 Mbps. Bluetooth® interface supports Bluetooth® Classic and Bluetooth® Low Energy. An integrated antenna circuitry switch allows a single external antenna (J14) to be shared between Wi-Fi® and Bluetooth®.

## Onboard Memories
The Arduino GIGA R1 WiFi supplements the 2 MB Flash and 1 MB SRAM on the STM32H747 (U1) with 16 MB of NOR Flash with the MX25L12833FZ2I (U2) as well as 8MB of SDRAM with the AS4C4M16SA (U3). U2 connects over a Quad-SPI interface to the U1. U3 operates at a frequency of 166 MHz.

## USB Connector
Two USB ports are provided on the Arduino GIGA R1 WiFi. One USB 2.0 type A (J2) and a USB-c (J12). The USB 2.0 connector allows external devices to be connected as peripherals, while the USB-c connector allows the GIGA board to be connected as a peripheral. Note that super speed pins on J12 are unpopulated. A TVS diode array is placed on the VBUS of each connector (D4,D2) for ESD protection.

## Audio
The STM32H7 (U1) has two digital-to-analog converters (DAC) which drive the stereo audio output on the 3.5 mm connector J15. The DAC has a resolution of up to 12 bits. The right and left channel are also accessible via pins DAC0 and DAC1 respectively. A microphone input is also present on J15, which is shared with analog pin A7. Buffered mode in the STM32H7 can allow for low impedance output. Sample and hold functionality can reduce the power requirements. Up to 10 mega samples per second is supported. 

## Power Tree
![Arduino GIGA R1 WiFi Power Tree](assets/GIGA_R1_WiFi_Power_Tree.png)

Power can either be supplied via the VIN pins, or the 5V of the USB connectors (J2, J12). If power is supplied via VIN, the MP2269GD-Z (U7) buck converter steps the voltage down to 5V. The 5V power rail is then stepped down to 3.3V by the MP2322GQH (U6) buck converter. The logic level of components on the Arduino GIGA is 3.3V.
## Board Operation

### Getting Started - IDE
If you want to program your Arduino® GIGA R1 WiFi while offline you need to install the Arduino® Desktop IDE **[1]** To connect the GIGA R1 WiFi control to your computer, you’ll need a Type-c USB cable. This also provides power to the board, as indicated by the LED.

### Getting Started - Arduino Web Editor
All Arduino® boards, including this one, work out-of-the-box on the Arduino® Web Editor **[2]**, by just installing a simple plugin. 

The Arduino® Web Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow **[3]** to start coding on the browser and upload your sketches onto your board.

### Getting Started - Arduino IoT Cloud
All Arduino® IoT enabled products are supported on Arduino® IoT Cloud which allows you to Log, graph and analyze sensor data, trigger events, and automate your home or business.

### Sample Sketches
Sample sketches for the Arduino® Portenta X8 can be found either in the “Examples” menu in the Arduino® IDE.

### Online Resources
Now that you have gone through the basics of what you can do with the board you can explore the endless possibilities it provides by checking exciting projects on ProjectHub **[4]**, the Arduino® Library Reference **[5]** and the online store **[6]** where you will be able to complement your board with sensors, actuators and more.

### Board Recovery
All Arduino boards have a built-in bootloader which allows flashing the board via USB. In case a sketch locks up the processor and the board is not reachable anymore via USB it is possible to enter bootloader mode by double-tapping the reset button right after power up.

# Mechanical Information

<!--
## Pinout

### JDIGITAL
### JSIDE

### J5

### J6

-->

## Mounting Holes And Board Outline
![Back View of Arduino GIGA R1 WiFi](assets/gigaMechanical.png)
# Certifications

## Declaration of Conformity CE DoC (EU)
We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA). 

## Declaration of Conformity to EU RoHS & REACH 211 01/19/2021
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

## Conflict Minerals Declaration 
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
This equipment should be installed and operated with minimum distance 20 cm between the radiator and your body.  

French: 
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 201453/EU. This product is allowed to be used in all EU member states. 

| Frequency bands      | Maximum output power (ERP) |
| -------------------- | -------------------------- |
| 2.4 GHz, 40 channels | +6dBm                      |


## Company Information

| Company name    | Arduino SRL                                   |
| --------------- | --------------------------------------------- |
| Company Address | Via Andrea Appiani 25, 20900, MONZA MB, Italy |

## Reference Documentation

| Ref                       | Link                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| Arduino IDE (Desktop)     | https://www.arduino.cc/en/Main/Software                                                       |
| Arduino IDE (Cloud)       | https://create.arduino.cc/editor                                                              |
| Cloud IDE Getting Started | https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor |
| Project Hub               | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending                      |
| Library Reference         | https://github.com/arduino-libraries/                                                         |
| Online Store              | https://store.arduino.cc/                                                                     |

## Change Log

| **Date**   | **Changes** |
| ---------- | ----------- |
| 28/10/2022 | Release     |