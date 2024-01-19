---
identifier: AFX00001-AFX00002-AFX00003
title: Arduino Opta®
type: pro
variant: 'Collective Datasheet'
author: Ali Jahangiri, Julián Caro Linares
---
![](assets/featured.png)

# Description
Arduino Opta® is a secure, easy-to-use micro PLC with Industrial IoT capabilities. Designed in partnership with leading relay manufacturer Finder®, it allows professionals to scale up industrial and building automation projects while taking advantage of the Arduino ecosystem.

The Arduino Opta® family has three variants: the Arduino Opta® Lite, Arduino Opta® RS485, and Arduino Opta® WiFi, all of them documented inside this document.


# Target Areas:
Industrial IoT, Building automation, Electrical loads management, Industrial automation


# CONTENTS
## Product Variants
There are three variants of the Arduino Opta® created to fit the different needs of each industry and application. The difference between each of the variants can be found in the following table:

<table style="page-break-before: auto;">
   <thead>
      <tr>
         <th style="text-align: center;">Name</th>
         <th style="text-align: center;">Arduino Opta® Lite</th>
         <th style="text-align: center;">Arduino Opta® RS485</th>
         <th style="text-align: center;">Arduino Opta® WiFi</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td style="text-align: center;">SKU</td>
         <td style="text-align: center;">AFX00003</td>
         <td style="text-align: center;">AFX00001</td>
         <td style="text-align: center;">AFX00002</td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;">USB</td>
         <td style="vertical-align: middle;text-align: center;">
            <p>USB-C®</p>
         </td>
         <td style="text-align: center;">
            <p>USB-C®</p>
         </td>
         <td style="text-align: center;">
            <p>USB-C®</p>
         </td>
      </tr>
      <tr>
         <td style="text-align: center;">Ethernet Support</td>
         <td style="text-align: center;">10/100BASE-T Port</td>
         <td style="text-align: center;">10/100BASE-T Port</td>
         <td style="text-align: center;">10/100BASE-T Port</td>
      </tr>
      <tr>
         <td style="text-align: center;">RS-485</td>
         <td style="text-align: center;">N/A</td>
         <td style="text-align: center;">Half-duplex</td>
         <td style="text-align: center;">Half-duplex</td>
      </tr>
      <tr>
         <td style="text-align: center;">Wi-Fi®</td>
         <td style="text-align: center;">N/A</td>
         <td style="text-align: center;">N/A</td>
         <td style="text-align: center;">802.11 b/g/n</td>
      </tr>
      <tr>
         <td style="text-align: center;">Bluetooth®</td>
         <td style="text-align: center;">N/A</td>
         <td style="text-align: center;">N/A</td>
         <td style="text-align: center;">Bluetooth® Low Energy</td>
      </tr>
   </tbody>
</table>

## Application Examples
Arduino Opta® is designed for industrial standard machinery control as a PLC with advanced features such as AI and connectivity capabilities. It is readily integrated into the Arduino hardware and software ecosystem, including real-time monitoring via the Arduino Cloud.


- **Conveyor belt management:** Arduino Opta® offers the possibility to configure its inputs as digital or analog to flexibly collect data from several types of sensors. Thanks to the Wi-Fi®/Bluetooth® Low Energy connectivity, Arduino Opta® can also be smoothly integrated with sensing boards, like the Nicla® ones from the Arduino ecosystem, leveraging Arduino Opta's potential with vision, sound, weight detection, air quality measurement and many other capabilities. 

    Arduino Opta® can use the data from the various sensors as they are or, thanks to its powerful microcontroller, use the outcome from a computation, to operate a wide variety of industrial machinery through its high-performing relays.

    All these features, wrapped in a compact form factor, make Arduino Opta® the ideal solution for product flow management in conveyor belts, automated packing or bottling lines. 

- **Real-time industrial monitoring:** Get instant access to your factory floor data and to the insights of your industrial processes to leverage your manufacturing excellence to continuous improvement. Implement visual management and KPIs monitoring thanks to the Arduino Opta's built-in connectivity features (Ethernet on all the product variants, Fieldbus and WiFi®/Bluetooth® Low Energy upon choice), delivering in a simple, fast and reliable way the data collected through beautiful dashboards in Arduino Cloud.
  
- **Predictive **maintenance**:** Combine the possibility to interact with wireless and wired sensors, given by the multiple connectivity options of Arduino Opta®, with the powerful microcontroller computational capabilities to implement AI algorithms for predictive maintenance. Edge computing and monitoring capabilities, thanks to the Arduino Cloud features, can help to identify small drifts in your processes to address issues before they become a problem, reducing production line downtimes and ensuring quality outcomes.


## Features
### General Specifications Overview
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Characteristics</th>
            <th colspan="2">Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top;">Supply Voltage</td>
            <td>12...24 VDC</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Inputs</td>
            <td>8x Analog/Digital inputs</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Outputs</td>
            <td>4x Relays - Normally Open (NO) - Max: 10A each</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Processor</td>
            <td>Dual-core ST STM32H747XI Processor</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Program Memory</td>
            <td>1 MB of RAM</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Flash Memory</td>
            <td>2 MB</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Flash QSPI Interface</td>
            <td>16 MB Flash QSPI. Shared between manufacturer's internal usage and data logging </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Programming method</td>
            <td>Arduino + IEC-61131-3 (LD - SFC - FBD - ST - IL)</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">USB Connectivity</td>
            <td>Host and Device operation, Programming/Flashing, Power delivery for programming (Not intended to drive external high-power peripherals)</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Communication</td>
            <td>Ethernet, RS-485 (AFX00001 & AFX00002), Wi-Fi® 2.4 GHz and Bluetooth® LE 4.2 supported by firmware, 5.1 supported by hardware (AFX00002) </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">RTC</td>
            <td>~10 days, NTP sync through Wi-Fi® (AFX00002 only) or Ethernet </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Security</td>
            <td>ATECC608B Crypto Microchip® </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Degree of Protection</td>
            <td>IP20</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Certifications</td>
            <td>cULus, ENEC, FCC, CE, CB, UKCA</td>
        </tr>
    </tbody>
</table>

### Processor
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Component</th>
            <th colspan="2">Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="4" style="vertical-align: top;">ST STM32H747XI Processor</td>
            <td style="vertical-align: top;"><p>Dual-core</p></td>
            <td>
                <p>Arm® Cortex®-M7 core at up to 480 MHz + Arm® 32-bit Cortex®-M4 core at up to 240 MHz</p>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Flash Memory</td>
            <td style="vertical-align: top;">
                <p>2 MB of Flash Memory with read-while-write support</p>
            </td>
        </tr>
        <tr>
            <td>Programming Memory</td>
            <td>1 MB of RAM</td>
        </tr>
        <tr>
        </tr>
    </tbody>
</table>

### Security
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Component</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="15" style="vertical-align: top;">ATECC608B Crypto Microchip®</td>
            <td>Cryptographic co-processor with secure hardware-based key storage</td>
        </tr>
        <tr>
            <td>Protected storage for up to 16 Keys, certificates or data</td>
        </tr>
        <tr>
            <td>Networking key management support</td>
        </tr>
        <tr>
            <td>Secure boot support</td>
        </tr>
        <tr>
            <td>Guaranteed unique 72-bit serial number</td>
        </tr>
    </tbody>
</table>

### Communication
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Interfaces</th>
            <th>Type</th>
            <th>Protocols/Technologies supported</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top;">Ethernet</td>
            <td>10/100BASE-T Port</td>
            <td>TCP/IP, MODBUS TCP</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">RS-485</td>
            <td>Half-duplex without termination resistance</td>
            <td>MODBUS RTU, Custom serial communication</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Wireless connectivity</td>
            <td>Wi-Fi®</td>
            <td>2.4 GHz</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Wireless connectivity</td>
            <td>Bluetooth® Low Energy</td>
            <td>4.2 supported by firmware, 5.1 supported by hardware</td>
        </tr>
    </tbody>
</table>

### Inputs
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Characteristics</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top;">Number of inputs</td>
            <td>8x Analog/Digital inputs</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Inputs overvoltage protection</td>
            <td>yes</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Antipolarity protection</td>
            <td>yes</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Input impedance</td>
            <td>8.9 kΩ</td>
        </tr>
    </tbody>
</table>

#### Analog Inputs
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Characteristics</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top;">Analog Input voltage</td>
            <td>0...10V </td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Analog Input resolution</td>
            <td>12...16 bits - User configurable</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Analog Input LSB value</td>
            <td>166 µV</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Accuracy</td>
            <td>+/- 5%, repeatability +/- 2%</td>
        </tr>
    </tbody>
</table>

#### Digital Inputs
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Characteristics</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top;">Digital Input voltage</td>
            <td>0...24V</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Digital Input voltage logic level</td>
            <td>VIL Max: 4.46 VDC. VHL Min: 6.6 VDC</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Digital Input current</td>
            <td>1.12mA at 10V</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Digital Input frequency</td>
            <td>4.5 kHz</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Cycle time for analog input acquisition</td>
            <td>10 µs</td>
        </tr>
    </tbody>
</table>

### Outputs
<table>
    <thead>
        <tr style="text-align: middle;">
            <th width="30%">Characteristics</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top;">Number of outputs</td>
            <td>4x relays (NO)</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Max current per relay</td>
            <td>10A</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Max peak current per relay</td>
            <td>15A</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Continuous current per terminal</td>
            <td>10A</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Short-circuit protection</td>
            <td>No, external fuse required</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Relay rated voltage</td>
            <td>250 VAC</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Relay Max voltage</td>
            <td>400 VAC</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Rated load AC1</td>
            <td>2500 VA</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Rated load AC15 (230 VAC)</td>
            <td>500 VA</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Breaking capacity DC1: 24/30/110/220V</td>
            <td>10/4/0.3/0.12A</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Minimum switching load</td>
            <td>300mW (5V/5mA)</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Max output line length (unshielded)</td>
            <td>100 m</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Relay response time from state 0 to state 1</td>
            <td>6 ms for relay output</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Relay response time from state 1 to state 0</td>
            <td>4 ms for relay output</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Bounce time NO</td>
            <td>3 ms</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Bounce time NC</td>
            <td>6 ms</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Relay mechanical durability</td>
            <td>10 million cycles</td>
        </tr>
        <tr>
            <td style="vertical-align: top;">Relay electrical durability</td>
            <td>10 thousand cycles with a resistive load of 10A</td>
        </tr>
    </tbody>
</table>

<div style="page-break-after:always;"></div>

## Ratings
### Recommended Operating Conditions

| Description                                       | Value                     |
|---------------------------------------------------|---------------------------|
| Temperature Operating Range                       | -20...50 °C                |
| Protection degree rating                          | IP20                      |
| Pollution degree                                  | 2 conforming to IEC 61010 |

### Power Specification

| Property               | Min   | Typ | Max  | Unit |
|----------------------- |------ |-----|------|------|
| Supply voltage         | 12    | -   | 24   | V    |
| Permissible range      | 10.2  | -   | 27.6 | V    |
| Power consumption (12V)| 0.6   | -   | 2    | W    |
| Power consumption (24V)| 0.6   | -   | 2.2  | W    |

<div style="page-break-after:always;"></div>

## Functional Overview
### Product View
![Arduino Opta® Product View](assets/opta_panel.svg)

<div style="page-break-after:always;"></div>

| Item | Feature                                                             | Item | Feature                                                             |
|------|---------------------------------------------------------------------|------|---------------------------------------------------------------------|
| 3A   | Power Supply Terminals 12...24 VDC                                  | 3H   | Ethernet Port Status LEDs                                           |
| 3B   | I1...I8 digital/analog input terminals (0-10V) configurable via IDE | 3I   | Label Holder                                                        |
| 3C   | Reset Button                                                        | 3J   | RS-485 terminal block (for Modbus RTU or proprietary communication) |
| 3D   | User Programmable button                                            | 3K   | USB-C® for programming and data logging                                |
| 3E   | Status LEDs 1...4 (User Programmable)                               | 3M   | Ethernet port                                                       |
| 3F   | Relay Output Terminals 1...4, NO contact (SPST) 10A 250 VAC         | 3N   | Port for communication and connection of auxiliary modules          |
| 3G   | Functional Earth                                                    |      |                                                                     |

**Note:** The LED above the *User Programmable button* (Ref: 3D) is only available on Arduino Opta® WiFi (AFX00002).

### Microcontroller
The microcontroller is a dual-core *STM32H747XI*. The main processor is a *Cortex®-M7* running at up to 480 MHz and the second one is a Cortex®-M4 running at up to 240 MHz.

Arduino Opta® can be programmed using the libraries developed for it as part of the standard Arduino Core library.

### Encryption
Encryption capabilities are provided by the *ATECC608B* chipset. This crypto-chip can be used to store sensitive information like security keys to connect to the Arduino® IoT Cloud or other third-party services, protecting Arduino Opta® from any unauthorized access in any kind of industrial and professional environment.

### Ethernet
TCP/IP and Modbus TCP communication are supported. The 10/100 Ethernet physical interface is directly connected to the internal Ethernet MAC and provides full-duplex communication with automatic MDIX support. With an internet connection, Ethernet communication can be used to connect the device to the Arduino® IoT Cloud or other third-party services.

### Modbus RTU
![Modbus RTU wiring diagram using the RS-485 interface](assets/opta_wiring_modbus.svg)

Modbus RTU communication is supported using Arduino Opta's RS-485 physical interface. Note that **Arduino Opta® does not have internal terminator resistors** so they need to be added if necessary following the Modbus protocol specification.

The wiring indication may vary depending on the connected device. In case the above connection indication is not resulting in consistent data transmission, invert the wires between A(-) and B(+) and retry.

### Wi-Fi® and Bluetooth® Low Energy (AFX00002 Only)
The onboard wireless module allows simultaneous management of Wi-Fi® and Bluetooth® connectivity. The Wi-Fi® interface can be operated as an Access Point, as a Station or as a dual-mode simultaneous AP/STA, and can handle up to 65 Mbps transfer rate. Bluetooth® interface supports Bluetooth® Low Energy (4.2). 

With an internet connection, the Wi-Fi® communication can be used for connecting to the Arduino® IoT Cloud or other third-party services.

### USB-C®
The USB-C® port can be used as a host or as a peripheral, but it cannot be used for both purposes at the same time. It is possible to use the connector to power the processor and flash it, but not to power the PLC outputs and peripherals. Additionally and using a USB memory stick, the USB-C® connector can be used for data logging purposes or to update the program inside the PLC.

### Relay Outputs
Arduino Opta® has four *Normally Open* (NO) powerful 10A relays which are capable of actuating on loads at a rated voltage of 250 VAC and up to a maximum switching voltage of 400 VAC.

The relay *Maximum Peak Current* is defined as the highest value of inrush current that the relay can endure without undergoing any permanent degradation of its characteristics due to the generated heat. The relay has to be able to hold up that maximum using a duty cycle of less or equal to 10% and for a time equal to or less than 0.5 s.

In the case of Arduino Opta®, relays have a *Maximum Peak Current* of 15A.

The *Rated Load* is the maximum resistive load that a contact can make, carry and break repeatedly. 
- For resistive or slightly inductive loads (AC1 classification), Arduino Opta's *Rated Load* is 2500 VA.
- For small electromagnetic loads (> 72 VA) (AC15 classification) like power contactors, magnetic solenoid valves, electromagnets and AC single-phase supplies, Arduino Opta's *Rated Load* is 500 VA. This value assumes a peak inrush current of approximately 10 times the rated current and keeping it within the maximum peak current.

For controlling DC loads (DC1 classification), the *Breaking Capacity* or maximum value of DC resistive current that a contact can make, carry and break repeatedly, is 10/4/0.3/0.12A for respectively 24/30/110/220V.

In the case of the minimum switching load parameters, the minimum values of power, voltage and current that the relays can reliably switch, are 300 mW/ 5V / 5mA. This implies that with 5V the current must be at least 60mA, with 24V, it must be at least 12.5mA, and with 5mA the voltage must be at least 60V.

The relays on Arduino Opta® provide a very fast response time of 6/4 ms to change state for closing/reopening, and a bounce time NO/NC of 3/6 ms.

### Expansion Port
The expansion port can be used to expand the Arduino Opta® capabilities with the help of additional modules. Reserved for future functionality.

### Programmable User Button
A pushbutton is accessible on the front panel of the Arduino Opta®. The functionality of this button can be configured via software. Note that the LED above the *User button* is only available on Arduino Opta® WiFi (AFX00002).

### Functional Earth
To avoid and reduce electrical noise, Arduino Opta® has a *Functional Earth* connector (Ref: 3G) near the Ethernet connector. *Functional Earth*, not to be confused with *Ground*, helps the device to reduce electrical interferences in industrial environments, being crucial for having stable Fieldbus communications.

## Device Operation
### Getting Started - IDE
If you want to program your Arduino Opta® while offline you need to install the Arduino® Desktop IDE **[1]**. To connect the Arduino Opta® to your computer, you will need a USB-C® cable.

### Getting Started - Arduino Web Editor
All Arduino® devices work out-of-the-box on the Arduino® Web Editor **[2]** by just installing a simple plugin.

The Arduino® Web Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards and devices. Follow **[3]** to start coding on the browser and upload your sketches onto your device.

### Getting Started - Arduino PLC IDE
Arduino Opta® can be also programmed using the industrial-standard **_IEC 61131-3_** programming languages. Download the Arduino® PLC IDE **[4]** software and connect your Arduino Opta® to your computer, using a simple USB-C® cable, to start creating your own PLC industrial solutions.

### Getting Started - Arduino Cloud
All Arduino® IoT enabled products are supported on Arduino Cloud which allows you to log, graph and analyze sensor data, trigger events, and automate your home or business.

### Sample Sketches
Sample sketches for Arduino Opta® can be found either in the “Examples” menu in the Arduino® IDE or the “Arduino Opta® Documentation” section of Arduino® **[5]**.

### Online Resources
Now that you have gone through the basics of what you can do with the device, you can explore the endless possibilities it provides by checking exciting projects on ProjectHub **[6]**, the Arduino® Library Reference **[7]** and the online store **[8]** where you will be able to complement your Arduino Opta® product with additional extensions, sensors and actuators.

<div style="page-break-after: always;"></div>

## Mechanical Information
### Product Dimensions
![Arduino Opta® Outline. Dimensions are in mm](assets/opta_mechanical.svg)

***Note: Terminals can be used with both solid and stranded core wire (min: 0.5 mm<sup>2</sup> / 20 AWG).***

## Certifications

### Certifications Summary

<table>
   <thead>
      <tr>
         <th style="width: 16%;vertical-align: middle;text-align: center;"><strong>Cert</strong></th>
         <th style="width: 28%;vertical-align: middle;text-align: center;"><strong>Arduino Opta® RS485 (AFX00001)</strong></th>
         <th style="width: 28%;vertical-align: middle;text-align: center;"><strong>Arduino Opta® WiFi (AFX00002)</strong></th>
         <th style="width: 28%;vertical-align: middle;text-align: center;"><strong>Arduino Opta® Lite (AFX00003) </strong></th>
      </tr>
      <tr></tr>
   </thead>
   <tbody>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>CE (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>EN IEC 61326-1:2021</p>
            <p>EN IEC 61010 (LVD)</p>
        </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>EN IEC 62311:2020</p>
            <p>EN IEC 61010 (LVD)</p>
            <p>EN 301 489-1 V2.2.3</p>
            <p>EN 301 489-17 V3.2.4</p>
            <p>IEC 61326-1:2021</p>
            <p>EN 300 328 V2.2.2:2019-07</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>EN IEC 61326-1:2021</p>
            <p>EN IEC 61010 (LVD)</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>CB (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>WEEE (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>ENEC</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>REACH (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>UKCA (UK)</strong></td>
         <td style="vertical-align: middle;text-align: center;">EN IEC 61326-1:2021</td>
         <td style="vertical-align: middle;text-align: center;">
         <p>EN IEC 62311:2020</p>
         <p>EN 300 328 V2.2.2:2019-07</p>
         <p>EN 301 489-1 V2.2.3</p>
         <p>EN 301 489-17 V3.2.4</p>
         <p>IEC 61326-1:2021</p>
         <p>EN 300 328 V2.2.2:2019-07</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">EN IEC 61326-1:2021</td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>FCC (US)</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>cULus</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>UL 61010-2-201</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>UL 61010-2-201</p>
         </td>
         <td style="vertical-align: middle;text-align: center;">
            <p>UL 61010-2-201</p>
         </td>
      </tr>
   </tbody>
</table>

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
|---------------------------|---------------------------- |
| 2412-2472 MHz (2.4G WIFI) | 5.42 dBm                    |
| 2402-2480 MHz (BLE)       | 2.41 dBm                    |
| 2402-2480 MHz (EDR)       | -6.27 dBm                   |



## Company Information

| Company name    | Arduino S.r.l                                     |
|-----------------|-------------------------------------------------|
| Company Address | Via Andrea Appiani, 25 - 20900 MONZA （ Italy ) |


## Reference Documentation
|        **Ref**                    | **Link**                                                                                    |
|:---------------------------------:|---------------------------------------------------------------------------------------------|
| Arduino IDE (Desktop)             | https://www.arduino.cc/en/Main/Software                                                     |
| Arduino IDE (Cloud)               | https://create.arduino.cc/editor                                                            |
| Arduino Cloud - Getting started   | https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started             |
| Arduino PLC IDE                   | https://www.arduino.cc/en/Main/Software                                                     |
| Arduino Opta® Documentation       | https://docs.arduino.cc/hardware/opta                                                       |
| Project Hub                       | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending                    |
| Library Reference                 | https://www.arduino.cc/reference/en/                                                        |
| Online Store                      | https://store.arduino.cc/                                                                   |

## Revision History

| Date       | **Revision** | **Changes**        |
|------------|--------------|------------------- |
| 16/05/2023 | 3            | Legal updates      |
| 13/04/2023 | 2            | Tech Specs Updates |
| 02/03/2023 | 1            | First Release      |
