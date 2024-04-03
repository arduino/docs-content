---
identifier: ASX00055
title: Arduino® Portenta Mid Carrier
type: pro
author: José Bagur
---

![](assets/Portenta_Mid_Carrier_Top_View.png)

# Description 

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier streamlines project development for Portenta boards by offering easy access to high-density signals through specialized and dedicated headers. It is compatible with the Portenta C33, H7, and X8 boards and is perfect for many projects, including the Internet of Things applications, asset tracking, machine vision, robotics, and automation. This carrier boasts a variety of ports and interfaces like CAN bus lines, Ethernet, microSD, and USB, along with camera and display connectors. It features debug pins and a real-time clock battery backup, easing development. Its onboard mini PCIe connector also enables quick cellular connectivity testing, ensuring reliable data transmission even in Wi-Fi® in scarce areas. These features make the Portenta Mid Carrier a vital tool for efficiently creating innovative, connected devices.
</p>

# Target Areas

Rapid prototyping, asset tracking, Internet of Things, machine vision, robotics, and automatization

# CONTENTS

## Application Examples

<div style="text-align:justify;">
The Arduino Portenta Mid Carrier enhances various prototyping applications thanks to its flexible design. The Portenta Mid Carrier provides a robust platform for many projects, from industry-ready prototypes to machine vision and cellular connectivity testing. Here are some application examples:

- **Rapid testing of cellular connectivity**: Use the mini PCIe connector on the Portenta Mid Carrier for swift cellular connectivity testing. This feature is invaluable for applications in smart cities/buildings, remote maintenance, and fleet management, ensuring rapid data transmission even in locations lacking Wi-Fi® coverage.
- **Prototyping**: The Portenta Mid Carrier is a versatile tool for prototyping, merging seamlessly with Portenta family boards to unveil essential peripherals like microSD, Ethernet, and USB. This integration facilitates industry-ready prototyping and streamlines debugging and inspection processes through dedicated pins for CAN bus lines. Moreover, its compatibility extends to a wide array of external hardware components and devices, enhancing your Portenta boards for projects that demand embedded sensing or straightforward actuation. This dual functionality ensures the Portenta Mid Carrier provides comprehensive support, simplifying the development process and elevating the potential for innovative project creation.
- **Frictionless machine vision prototyping**: Pair the Portenta Mid Carrier with an MIPI or Arducam® camera to effortlessly embark on machine vision projects. Whether for object detection and recognition, defect identification, or asset tracking, the Portenta Mid Carrier streamlines the creation of complex vision-based applications.
- **Reference design**: The Portenta Mid Carrier serves as an excellent reference design and aids in the development of custom products within the Portenta ecosystem. Arduino PRO's full development, production, and operation support provides a solid foundation for tailoring solutions to specific business needs.
</div>

<div style="page-break-after: always;"></div>

## Features

### General Specifications Overview

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier is an excellent tool for building scalable projects based on the Portenta family boards. The Portenta Mid Carrier was designed to give quick access to all the essential signals of the Portenta family boards, making adding new features to your projects more accessible with its Ethernet and the onboard Mini PCIe connector. With this connector, the Portenta Mid Carrier capabilities are notably enhanced by including cellular connectivity to the carrier, allowing for rapid testing and deployment of applications requiring remote communication. The carrier includes a microSD card slot starting from an external source, and it has CAN bus lines for connecting to actuators, which helps manage devices easily. You can also develop machine vision applications using the onboard camera connectors. The carrier is also a straightforward reference design for creating their hardware. 

The main features of the Portenta Mid Carrier are summarized and highlighted in the table below.
</p>

<div style="text-align:center;">

<table>
<thead>
  <tr>
    <th>Feature</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Ethernet</td>
    <td>RJ45 connector (x1)</td>
  </tr>
  <tr>
    <td>USB Connectivity</td>
    <td>USB-A 2.0 female connector for data logging operations (x1)</td>
  </tr>
  <tr>
    <td>Power Supply</td>
    <td>Various options for easily powering the Carrier: onboard USB-C® port of the Portenta family board connected to the Carrier, and external power supply connected through the onboard screw terminal block and dedicated pins of the breakout header connectors of the Carrier</td>
  </tr>
  <tr>
    <td>Screw Terminal Block</td>
    <td>Used to power the Carrier and for the CAN bus interface (CAN1)</td>
  </tr>
  <tr>
    <td>Breakout Header Connectors</td>
    <td>Available interfaces through the breakout headers are the following: UART (x4), I2S (x1), CAN bus (x2), SPDIF (x1), PDM (x1), GPIO (x7), SPI (x2), I2C (x3), SAI (x1), PWM (x10), ADC (x8)</td>
  </tr>
  <tr>
    <td>Camera Connectors</td>
    <td>MIPI camera (x1), Digital Video Port (DVP) interface (x1)</td>
  </tr>
  <tr>
    <td>Mini PCIe Interface</td>
    <td>Accessible through the Carrier's dedicated Mini PCIe connector, its High-Density connectors, and the dedicated Mini PCIe breakout header</td>
  </tr>
  <tr>
    <td>Debugging</td>
    <td>Onboard JTAG/SWD debug connector</td>
  </tr>
  <tr>
    <td>Battery Socket</td>
    <td>Onboard CR1225 battery socket used for Real-Time Clock (RTC) support</td>
  </tr>
  <tr>
    <td>Dimensions</td>
    <td>114 mm x 86.5 mm</td>
  </tr>
  <tr>
    <td>Weight</td>
    <td>67 g</td>
  </tr>
  <tr>
    <td>Operating Temperature</td>
    <td>-40 °C to +85 °C</td>
  </tr>
  <tr>
    <td>Certifications</td>
    <td>CE, FCC, IC, RoHS, REACH, UKCA, WEEE, Japan (No Radio)</td>
  </tr>
</tbody>
</table>
</div>

<p style="text-align: justify;">
In the following sections, as well as the tables presented in those sections, the communication interfaces and other important features of the Carrier are further detailed.
</p>

<div style="page-break-after: always;"></div>

### Communication Interfaces

<div style="text-align:center;">

<table>
    <thead>
        <tr>
            <th width="30%" style="text-align: right;">Interfaces</th>
            <th style="text-align: left;">Connector</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="vertical-align: top; text-align: right;">Mini PCIe (x1)</td>
            <td style="text-align: left;">Mini PCIe connector (J8), High-Density connectors (J1-J2) and breakout header connector<sup>1</sup> (J16)</td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">Ethernet (x1)</td>
            <td style="text-align: left;">RJ45 connector (J18)</td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">SPI (x2)</td>
            <td style="text-align: left;">
                <ul>
                    <li>SPI0: Breakout header connector (J15) and High-Density connector (J2)</li>
                    <li>SPI1: Breakout header connector (J15) and High-Density connector (J2)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">I2S (x1)</td>
            <td style="text-align: left;">Breakout header connector (J14) and High-Density connector (J1)</td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">I2C (x3)</td>
            <td style="text-align: left;">
                <ul>
                    <li>I2C0: Breakout header connector (J15) and High-Density connector (J1)</li>
                    <li>I2C1: Breakout header connector (J15) and High-Density connector (J1)</li>
                    <li>I2C2: Breakout header connector (J15) and High-Density connector (J2)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">CAN bus (x2)</td>
            <td style="text-align: left;">
                <ul>
                    <li>CAN0<sup>2</sup>: Breakout header connector (J14) and High-Density connector (J1)</li>
                    <li>CAN1<sup>3</sup>: Breakout header connector (J14), High-Density connector (J1), and screw terminal block (J4)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="vertical-align: top; text-align: right;">UART (with flow control) (x4)</td>
            <td style="text-align: left;">
                <ul>
                    <li>SERIAL0: Breakout header connector (J14) and High-Density connector (J1)</li>
                    <li>SERIAL1: Breakout header connector (J14) and High-Density connector (J1)</li>
                    <li>SERIAL2: Breakout header connector (J14) and High-Density connector (J2)</li>
                    <li>SERIAL3: Breakout header connector (J14) and High-Density connector (J2)</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

<p style="text-align: justify;">
<sup>1</sup>For debugging purposes only.<br> 
<sup>2</sup>CAN0 has no CAN PHY; an external one is needed.<br>
<sup>3</sup>CAN1 has an onboard CAN PHY available through the Carrier's screw terminal block (J4); it can be enabled or disabled via a DIP switch (SW2).<br>
</p>

### Other Features

<div style="text-align:center;">

<table>
<thead>
    <tr>
        <th width="30%" style="text-align: right;">Feature</th>
        <th style="text-align: left;">Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td style="text-align: right;">Additional onboard storage</td>
        <td style="text-align: left;">microSD card slot (J12) for data logging operations</td>
    </tr>
    <tr>
        <td style="text-align: right;">SIM card support</td>
        <td style="text-align: left;">Yes, available through the Carrier's Mini PCIe interface</td>
    </tr>
    <tr>
        <td style="text-align: right;">RTC Support</td>
        <td style="text-align: left;">Yes, available through the Carrier's onboard CR1225 battery socket</td>
    </tr>
    <tr>
        <td style="text-align: right;">USB support</td>
        <td style="text-align: left;">USB-A 2.0 female connector (J13) for data logging operations</td>
    </tr>
    <tr>
        <td style="text-align: right;">Camera support</td>
        <td style="text-align: left;">Yes, through the MIPI camera connector (J10) and the DVP interface connector (J11)</td>
    </tr>
    <tr>
        <td style="text-align: right;">Display support</td>
        <td style="text-align: left;">Yes, available through the Carrier's GIGA Display Shield connector (J19) (x1)</td>
    </tr>
    <tr>
        <td style="text-align: right;">Video support</td>
        <td style="text-align: left;">Only with the Portenta H7 and the Portenta X8 boards through its onboard USB-C® connector</td>
    </tr>
    <tr>
        <td style="text-align: right;">Camera support<sup>4</sup></td>
        <td style="text-align: left;">Yes, available through the MIPI camera connector (J10) and the DVP interface connector (J11)</td>
    </tr>
    <tr>
        <td style="text-align: right;">DIP switches</td>
        <td style="text-align: left;">
            <ul>
                <li>ETH CENTER TAP (SW3): All positions OFF to enable Ethernet for the Portenta X8 board; for the Portenta C33 and H7 boards, Ethernet is always enabled regardless of the switch positions</li>
                <li>BOOT SEL: All positions ON to enable BOOT mode, all positions OFF to enable NORMAL operation mode</li>
            </ul>
        </td>
    </tr>
</tbody>
</table>
</div>

<p style="text-align: justify;">
<sup>4</sup> MIPI cameras are only supported by the Portenta X8 board; DVP interface is compatible with Arducam® DVP camera modules.<br>
</p>

### Related Accessories (Not Included)

- MIPI camera
- microSD card
- CR1225 (3 VDC) coin cell
- Arducam® DVP camera modules
- SIM card (only data compatible)

### Related Products (Not Included)

- Arduino® Portenta X8 (SKU: ABX00049)
- Arduino® Portenta C33 (SKU: ABX00074)
- Arduino® Portenta H7 (SKU: ABX00042/ABX00045/ABX00046)
- Arduino® Pro 4G Module EMEA (SKU: TPX00201)
- Arduino® Pro 4G GNSS Module Global (SKU: TPX00200)
- Arduino® GIGA Display Shield (SKU: ASX00039)
- Arduino USB Type-C® Cable 2-in-1 (SKU: TPX00094)

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<strong>Note:</strong> The Portenta Mid Carrier requires a compatible Portenta family board to operate.
</div>

<div style="page-break-after: always;"></div>

## Ratings

### Recommended Operating Conditions

<p style="text-align: justify;">
The table below provides a comprehensive guideline for the optimal use of the Arduino Portenta Mid Carrier, outlining typical operating conditions and design limits. The operating conditions of the Portenta Mid Carrier are largely based on the specifications of its components.
</p>

<div style="text-align:center;">

|                 **Parameter**                |    **Symbol**   | **Min** | **Typ** | **Max** | **Unit** |
|:--------------------------------------------:|:---------------:|:-------:|:-------:|:-------:|:--------:|
|     USB Supply Input Voltage<sup>1</sup>     | V<sub>USB</sub> |    -    |   5.0   |    -    |     V    |
|       Supply Input Voltage<sup>2</sup>       |  V<sub>IN</sub> |    -    |   5.0   |    -    |     V    |
| Current delivered by the Carrier<sup>3</sup> |  I<sub>C</sub>  |    -    |    -    |   2.0   |     A    |
|             Operating Temperature            |  T<sub>OP</sub> |   -40   |    -    |    85   |    °C    |

</div>

<p style="text-align: justify;">
<sup>1</sup> Carrier powered through the USB-C® port of the connected Portenta family board to the carrier.<br>
<sup>2</sup> Carrier powered through its onboard screw terminal block (J4, IN 5V terminal) or its breakout pin header connector (J15, IN 5V pins).<br>
<sup>3</sup> Available only for the Mini PCIe card connected to the carrier.
</p>

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<p style="text-align: justify;">
<strong>Note:</strong> Remember to check out the power specifications of the Mini PCIe card intended to be connected to the carrier to avoid damage to both the card and the carrier. For more safety tips, refer to the carrier's user manual.
</p>
</div>

<div style="page-break-after: always;"></div>

## Functional Overview

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier is a powerful tool for developing scalable Portenta-based applications, providing quick access to all high-density signals. It enables expansion with Ethernet and the onboard Mini PCIe connector, with the added capability of cellular connectivity through the Mini PCIe interface for applications that need remote access or communication. This makes it even more versatile for projects like smart cities and IoT. Booting projects from external sources is easy with the microSD card slot, and interacting with actuators is straightforward with onboard CAN bus lines. The carrier also supports industrial machine vision with dedicated camera connectors and offers a reliable foundation for creating proprietary hardware, streamlining the development process across various projects.
</p>

### Topology

An overview of the Portenta Mid Carrier topology is illustrated and described in the figure and table below.

![](assets/Portenta_Mid_Carrier_Topology.png)

<div style="text-align:center;">

<table>
    <thead>
        <tr>
            <th>Item</th>
            <th>Feature</th>
            <th>Item</th>
            <th>Feature</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: right;">J1, J2</td>
            <td>High-Density connectors of the Portenta family boards</td>
            <td style="text-align: right;">J3</td>
            <td>JTAG male connector for debugging</td>
        </tr>
        <tr>
            <td style="text-align: right;">J4</td>
            <td>Screw terminal block for power supply and CAN bus interface</td>
            <td style="text-align: right;">J5</td>
            <td>Battery socket</td>
        </tr>
        <tr>
            <td style="text-align: right;">J8</td>
            <td>Mini PCIe connector</td>
            <td style="text-align: right;">J10</td>
            <td>MIPI camera connector (only compatible with Portenta X8 boards)</td>
        </tr>
        <tr>
            <td style="text-align: right;">J11</td>
            <td>DVP interface connector</td>
            <td style="text-align: right;">J12</td>
            <td>microSD card slot</td>
        </tr>
        <tr>
            <td style="text-align: right;">J13</td>
            <td>USB-A 2.0 female connector for data logging operations</td>
            <td style="text-align: right;">J14, J15</td>
            <td>2.54 mm breakout header connectors</td>
        </tr>
        <tr>
            <td style="text-align: right;">J16</td>
            <td>Mini PCIe breakout header connector</td>
            <td style="text-align: right;">J17</td>
            <td>2.54 mm breakout header connectors</td>
        </tr>
        <tr>
            <td style="text-align: right;">J18</td>
            <td>RJ45 connector for Ethernet</td>
            <td style="text-align: right;">J19</td>
            <td>GIGA Display Shield Connector</td>
        </tr>
        <tr>
            <td style="text-align: right;">SIM1</td>
            <td>Nano SIM card connector</td>
            <td style="text-align: right;">SW1</td>
            <td>Boot select switch</td>
        </tr>
        <tr>
            <td style="text-align: right;">SW2</td>
            <td>CAN bus interface enable/disable switch</td>
            <td style="text-align: right;">SW3</td>
            <td>Ethernet enable/disable switch</td>
        </tr>
    </tbody>
</table>

</div>

### Simple Pinout 

The Portenta Mid Carrier simple pinout is shown in the figure below.

![](assets/Portenta_Mid_Carrier_Pinout.png)

<div style="page-break-after: always;"></div>

### Full Pinout

The Portenta Mid Carrier full pinout is shown in the following sections, sorted by the components and connectors of the carrier. 

#### Breakout Header Connector (J14)

<p style="text-align: justify;">
The breakout header connector J14 is used in the Portenta Mid Carrier to expose the connected Portenta family board High-Density signals. J14 is a male header connector with a pin spacing of 2.54 mm.
</p>

<table align = "center">
<thead>
  <tr>
    <th align="center">Pin Number</th>
    <th align="center">Silkscreen</th>
    <th align="center">Power Net</th>
    <th align="center">Portenta HD Standard Pin</th>
    <th align="center">High-Density Pin</th>
    <th align="center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align="center">1</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">2</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align="center"></td>
  </tr>
  <tr> 
    <td align="center">3</td>
    <td align="center">RTS0</td>
    <td align="center"></td>
    <td align="center">SERIAL0_RTS</td>
    <td align="center">J1-38</td>
    <td align="center">UART 0 RTS</td>
  </tr>
  <tr>
    <td align="center">4</td>
    <td align="center">RTS1</td>
    <td align="center"></td>
    <td align="center">SERIAL1_RTS</td>
    <td align="center">J1-37</td>
    <td align="center">UART 1 RTS</td>
  </tr>
  <tr>
    <td align="center">5</td>
    <td align="center">VIN</td>
    <td align="center">+5V</td>
    <td align="center">VIN</td>
    <td align="center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">6</td>
    <td align="center">VIN</td>
    <td align="center">+5V</td>
    <td align="center">VIN</td>
    <td align="center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">RX0</td>
    <td align="center"></td>
    <td align="center">SERIAL0_RX</td>
    <td align="center">J1-36</td>
    <td align="center">UART 0 RX</td>
  </tr>
  <tr>
    <td align="center">9</td>
    <td align="center">RX1</td>
    <td align="center"></td>
    <td align="center">SERIAL1_RX</td>
    <td align="center">J1-35</td>
    <td align="center">UART 1 RX</td>
  </tr>
  <tr>
    <td align="center">10</td>
    <td align="center">TX0</td>
    <td align="center"></td>
    <td align="center">SERIAL0_TX</td>
    <td align="center">J1-34</td>
    <td align="center">UART 0 TX</td>
  </tr>
  <tr>
    <td align="center">11</td>
    <td align="center">TX1</td>
    <td align="center"></td>
    <td align="center">SERIAL1_TX</td>
    <td align="center">J1-33</td>
    <td align="center">UART 1 TX</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">CTS0</td>
    <td align="center"></td>
    <td align="center">SERIAL0_CTS</td>
    <td align="center">J1-40</td>
    <td align="center">UART 0 CTS</td>
  </tr>
  <tr>
    <td align="center">13</td>
    <td align="center">CTS1</td>
    <td align="center"></td>
    <td align="center">SERIAL1_CTS</td>
    <td align="center">J1-39</td>
    <td align="center">UART 1 CTS</td>
  </tr>
  <tr>
    <td align="center">14</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">15</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">RTS2</td>
    <td align="center"></td>
    <td align="center">SERIAL2_RTS</td>
    <td align="center">J2-30</td>
    <td align="center">UART 2 RTS</td>
  </tr>
  <tr>
    <td align="center">17</td>
    <td align="center">RTS3</td>
    <td align="center"></td>
    <td align="center">SERIAL3_RTS</td>
    <td align="center">J2-29</td>
    <td align="center">UART 3 RTS</td>
  </tr>
  <tr>
    <td align="center">18</td>
    <td align="center">VIN</td>
    <td align="center">+5V</td>
    <td align="center">VIN</td>
    <td align="center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">19</td>
    <td align="center">VIN</td>
    <td align="center">+5V</td>
    <td align="center">VIN</td>
    <td align="center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">RX2</td>
    <td align="center"></td>
    <td align="center">SERIAL2_RX</td>
    <td align="center">J2-28</td>
    <td align="center">UART 2 RX</td>
  </tr>
  <tr>
    <td align="center">21</td>
    <td align="center">RX3</td>
    <td align="center"></td>
    <td align="center">SERIAL3_RX</td>
    <td align="center">J2-27</td>
    <td align="center">UART 3 RX</td>
  </tr>
  <tr>
    <td align="center">22</td>
    <td align="center">TX2</td>
    <td align="center"></td>
    <td align="center">SERIAL2_TX</td>
    <td align="center">J2-26</td>
    <td align="center">UART 2 TX</td>
  </tr>
  <tr>
    <td align="center">23</td>
    <td align="center">TX3</td>
    <td align="center"></td>
    <td align="center">SERIAL3_TX</td>
    <td align="center">J2-25</td>
    <td align="center">UART 3 TX</td>
  </tr>
  <tr>
    <td align="center">24</td>
    <td align="center">CTS2</td>
    <td align="center"></td>
    <td align="center">SERIAL2_CTS</td>
    <td align="center">J2-32</td>
    <td align="center">UART 2 CTS</td>
  </tr>
  <tr>
    <td align="center">25</td>
    <td align="center">CTS3</td>
    <td align="center"></td>
    <td align="center">SERIAL3_CTS</td>
    <td align="center">J2-31</td>
    <td align="center">UART 3 CTS</td>
  </tr>
  <tr>
    <td align="center">26</td>
    <td align="center">I2S CLK</td>
    <td align="center"></td>
    <td align="center">I2S_CK</td>
    <td align="center">J1-56</td>
    <td align="center">I2S CK</td>
  </tr>
  <tr>
    <td align="center">27</td>
    <td align="center">CAN0 TX</td>
    <td align="center"></td>
    <td align="center">CAN0_TX</td>
    <td align="center">J1-50</td>
    <td align="center">CAN 0 TX</td>
  </tr>
  <tr>
    <td align="center">28</td>
    <td align="center">I2S WS</td>
    <td align="center"></td>
    <td align="center">I2S_WS</td>
    <td align="center">J1-58</td>
    <td align="center">I2S WS</td>
  </tr>
  <tr> 
    <td align="center">29</td>
    <td align="center">CAN0 RX</td>
    <td align="center"></td>
    <td align="center">CAN0_RX</td>
    <td align="center">J1-52</td>
    <td align="center">CAN 0 RX</td>
  </tr>
  <tr>
    <td align="center">30</td>
    <td align="center">I2S SDI</td>
    <td align="center"></td>
    <td align="center">I2S_SDI</td>
    <td align="center">J1-60</td>
    <td align="center">I2S SDI</td>
  </tr>
  <tr>
    <td align="center">31</td>
    <td align="center">CAN1 TX</td>
    <td align="center"></td>
    <td align="center">CAN1_TX</td>
    <td align="center">J1-49</td>
    <td align="center">CAN 1 TX</td>
  </tr>
  <tr>
    <td align="center">32</td>
    <td align="center">I2S SDO</td>
    <td align="center"></td>
    <td align="center">I2S_SDO</td>
    <td align="center">J1-62</td>
    <td align="center">I2S SDO</td>
  </tr>
  <tr>
    <td align="center">33</td>
    <td align="center">CAN1 RX</td>
    <td align="center"></td>
    <td align="center">CAN1_RX</td>
    <td align="center">J1-51</td>
    <td align="center">CAN 1 RX</td>
  </tr>
  <tr>
    <td align="center">34</td>
    <td align="center">SPDIF TX</td>
    <td align="center"></td>
    <td align="center">SPDIF_TX</td>
    <td align="center">J1-74</td>
    <td align="center">SPDIF TX</td>
  </tr>
  <tr>
    <td align="center">35</td>
    <td align="center">PDM CLK</td>
    <td align="center"></td>
    <td align="center">PDM_CK</td>
    <td align="center">J1-66</td>
    <td align="center">PDM CK</td>
  </tr>
  <tr>
    <td align="center">36</td>
    <td align="center">SPDIF RX</td>
    <td align="center"></td>
    <td align="center">SPDIF_RX</td>
    <td align="center">J1-76</td>
    <td align="center">SPDIF RX</td>
  </tr>
  <tr>
    <td align="center">37</td>
    <td align="center">PDM D0</td>
    <td align="center"></td>
    <td align="center">PDM_D0</td>
    <td align="center">J1-68</td>
    <td align="center">PDM D0</td>
  </tr>
  <tr>
    <td align="center">37</td>
    <td align="center">GPIO0</td>
    <td align="center"></td>
    <td align="center">GPIO_0</td>
    <td align="center">J2-46</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">38</td>
    <td align="center">PDM D1</td>
    <td align="center"></td>
    <td align="center">PDM_D1</td>
    <td align="center">J1-70</td>
    <td align="center">PDM D1</td>
  </tr>
  <tr>
    <td align="center">39</td>
    <td align="center">GPIO1</td>
    <td align="center"></td>
    <td align="center">GPIO_0</td>
    <td align="center">J2-48</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">40</td>
    <td align="center">GPIO6</td>
    <td align="center"></td>
    <td align="center">GPIO_6</td>
    <td align="center">J2-58</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">41</td>
    <td align="center">GPIO2</td>
    <td align="center"></td>
    <td align="center">GPIO_2</td>
    <td align="center">J2-50</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">42</td>
    <td align="center">GPIO5</td>
    <td align="center"></td>
    <td align="center">GPIO_5</td>
    <td align="center">J2-56</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">43</td>
    <td align="center">GPIO3</td>
    <td align="center"></td>
    <td align="center">GPIO_3</td>
    <td align="center">J2-52</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">44</td>
    <td align="center">GPIO4</td>
    <td align="center"></td>
    <td align="center">GPIO_4</td>
    <td align="center">J2-54</td>
    <td align="center"></td>
  </tr>
</tbody>
</table>

#### Breakout Header Connector (J15)

<p style="text-align: justify;">
The breakout header connector J15 is used in the Portenta Mid Carrier to expose the connected Portenta family board High-Density signals. J15 is a male header connector with a pin spacing of 2.54 mm.
</p>

<table align = "center">
<thead>
  <tr>
    <th align="center">Pin Number</th>
    <th align="center">Silkscreen</th>
    <th align="center">Power Net</th>
    <th align="center">Portenta HD Standard Pin</th>
    <th align="center">High-Density Pin</th>
    <th align="center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align="center">1</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">2</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">GND</td>
    <td align="center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">3</td>
    <td align="center">VCC</td>
    <td align="center">+3V3<br>Portenta</td>
    <td align="center">VCC</td>
    <td align="center">J2-23, J2-34, J2-43, J2-69</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">4</td>
    <td align="center">VCC</td>
    <td align="center">+3V3<br>Portenta</td>
    <td align="center">VCC</td>
    <td align="center">J2-23, J2-34, J2-43, J2-69</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">5</td>
    <td align="center">VIN</td>
    <td align="center">+5V</td>
    <td align="center">VIN</td>
    <td align="center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">6</td>
    <td align="center">VIN</td>
    <td align="center">+5V</td>
    <td align="center">VIN</td>
    <td align="center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">7</td>
    <td align="center">VREFP</td>
    <td align="center"></td>
    <td align="center">ANALOG_VREF_P</td>
    <td align="center">J2-71</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">VREFN</td>
    <td align="center"></td>
    <td align="center">ANALOG_VREF_N</td>
    <td align="center">J2-72</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">9</td>
    <td align="center">A0</td>
    <td align="center"></td>
    <td align="center">ANALOG_A0</td>
    <td align="center">J2-73</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">10</td>
    <td align="center">SPI0 CS</td>
    <td align="center"></td>
    <td align="center">SPI0_CS</td>
    <td align="center">J2-53</td>
    <td align="center">SPI 0 CS</td>
  </tr>
  <tr>
    <td align="center">11</td>
    <td align="center">A1</td>
    <td align="center"></td>
    <td align="center">ANALOG_A1</td>
    <td align="center">J2-75</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">SPI0 SCLK</td>
    <td align="center"></td>
    <td align="center">SPI0_CK</td>
    <td align="center">J2-37</td>
    <td align="center">SPI 0 CK</td>
  </tr>
  <tr>
    <td align="center">13</td>
    <td align="center">A2</td>
    <td align="center"></td>
    <td align="center">ANALOG_A2</td>
    <td align="center">J2-77</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">14</td>
    <td align="center">SPI0 CIPO</td>
    <td align="center"></td>
    <td align="center">SPI0_MISO</td>
    <td align="center">J2-39</td>
    <td align="center">SPI 0 CIPO</td>
  </tr>
  <tr>
    <td align="center">15</td>
    <td align="center">A3</td>
    <td align="center"></td>
    <td align="center">ANALOG_A3</td>
    <td align="center">J2-79</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">SPI0 COPI</td>
    <td align="center"></td>
    <td align="center">SPI0_MOSI</td>
    <td align="center">J2-41</td>
    <td align="center">SPI 0 COPI</td>
  </tr>
  <tr>
    <td align="center">17</td>
    <td align="center">A4</td>
    <td align="center"></td>
    <td align="center">ANALOG_A4</td>
    <td align="center">J2-74</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">18</td>
    <td align="center">SPI1 CS</td>
    <td align="center"></td>
    <td align="center">SPI1_CS</td>
    <td align="center">J2-36</td>
    <td align="center">SPI 1 CS</td>
  </tr>
  <tr>
    <td align="center">19</td>
    <td align="center">A5</td>
    <td align="center"></td>
    <td align="center">ANALOG_A5</td>
    <td align="center">J2-76</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">SPI1 SCLK</td>
    <td align="center"></td>
    <td align="center">SPI1_CK</td>
    <td align="center">J2-38</td>
    <td align="center">SPI 1 CK</td>
  </tr>
  <tr>
    <td align="center">21</td>
    <td align="center">A6</td>
    <td align="center"></td>
    <td align="center">ANALOG_A6</td>
    <td align="center">J2-78</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">22</td>
    <td align="center">SPI1 CIPO</td>
    <td align="center"></td>
    <td align="center">SPI1_MISO</td>
    <td align="center">J2-40</td>
    <td align="center">SPI 1 CIPO</td>
  </tr>
  <tr>
    <td align="center">23</td>
    <td align="center">A7</td>
    <td align="center"></td>
    <td align="center">ANALOG_A7</td>
    <td align="center">J2-80</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">24</td>
    <td align="center">SPI1 COPI</td>
    <td align="center"></td>
    <td align="center">SPI1_MOSI</td>
    <td align="center">J2-42</td>
    <td align="center">SPI 1 COPI</td>
  </tr>
  <tr>
    <td align="center">25</td>
    <td align="center">PWM0</td>
    <td align="center"></td>
    <td align="center">PWM_0</td>
    <td align="center">J2-59</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">26</td>
    <td align="center">I2C0 SDA</td>
    <td align="center"></td>
    <td align="center">I2C0_SDA</td>
    <td align="center">J1-44</td>
    <td align="center">I2C 0 SDA</td>
  </tr>
  <tr>
    <td align="center">27</td>
    <td align="center">PWM1</td>
    <td align="center"></td>
    <td align="center">PWM_1</td>
    <td align="center">J2-61</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">28</td>
    <td align="center">I2C0 SCL</td>
    <td align="center"></td>
    <td align="center">I2C0_SCL</td>
    <td align="center">J1-46</td>
    <td align="center">I2C 0 SCL</td>
  </tr>
  <tr>
    <td align="center">29</td>
    <td align="center">PWM2</td>
    <td align="center"></td>
    <td align="center">PWM_2</td>
    <td align="center">J2-63</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">30</td>
    <td align="center">I2C1 SDA</td>
    <td align="center"></td>
    <td align="center">I2C1_SDA</td>
    <td align="center">J1-43</td>
    <td align="center">I2C 1 SDA</td>
  </tr>
  <tr>
    <td align="center">31</td>
    <td align="center">PWM3</td>
    <td align="center"></td>
    <td align="center">PWM_3</td>
    <td align="center">J2-65</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">32</td>
    <td align="center">I2C1 SCL</td>
    <td align="center"></td>
    <td align="center">I2C1_SCL</td>
    <td align="center">J1-45</td>
    <td align="center">I2C 1 SCL</td>
  </tr>
  <tr>
    <td align="center">33</td>
    <td align="center">PWM4</td>
    <td align="center"></td>
    <td align="center">PWM_4</td>
    <td align="center">J2-67</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">34</td>
    <td align="center">I2C2 SDA</td>
    <td align="center"></td>
    <td align="center">I2C2_SDA</td>
    <td align="center">J2-45</td>
    <td align="center">I2C 2 SDA</td>
  </tr>
  <tr>
    <td align="center">35</td>
    <td align="center">PWM5</td>
    <td align="center"></td>
    <td align="center">PWM_5</td>
    <td align="center">J2-60</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">36</td>
    <td align="center">I2C2 SCL</td>
    <td align="center"></td>
    <td align="center">I2C2_SCL</td>
    <td align="center">J2-47</td>
    <td align="center">I2C 2 SCL</td>
  </tr>
  <tr>
    <td align="center">37</td>
    <td align="center">PWM6</td>
    <td align="center"></td>
    <td align="center">PWM_6</td>
    <td align="center">J2-62</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">38</td>
    <td align="center">SAI CLK</td>
    <td align="center"></td>
    <td align="center">SAI_CK</td>
    <td align="center">J2-49</td>
    <td align="center">SAI CLK</td>
  </tr>
  <tr>
    <td align="center">39</td>
    <td align="center">PWM7</td>
    <td align="center"></td>
    <td align="center">PWM_7</td>
    <td align="center">J2-64</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">40</td>
    <td align="center">SAI FS</td>
    <td align="center"></td>
    <td align="center">SAI_FS</td>
    <td align="center">J2-51</td>
    <td align="center">SAI FS</td>
  </tr>
  <tr>
    <td align="center">41</td>
    <td align="center">PWM8</td>
    <td align="center"></td>
    <td align="center">PWM_8</td>
    <td align="center">J2-66</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">42</td>
    <td align="center">SAI D0</td>
    <td align="center"></td>
    <td align="center">SAI_D0</td>
    <td align="center">J2-53</td>
    <td align="center">SAI D0</td>
  </tr>
  <tr>
    <td align="center">43</td>
    <td align="center">PWM9</td>
    <td align="center"></td>
    <td align="center">PWM_9</td>
    <td align="center">J2-68</td>
    <td align="center"></td>
  </tr>
  <tr>
    <td align="center">44</td>
    <td align="center">SAI D1</td>
    <td align="center"></td>
    <td align="center">SAI_D1</td>
    <td align="center">J2-55</td>
    <td align="center">SAI D1</td>
  </tr>
</tbody>
</table>

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<p style="text-align: justify;">
<strong>Reverse polarity protection:</strong> IN 5V pins of the carrier's screw terminal block (J4) and breakout header connector (J15) <strong> do not have</strong> reverse polarity protection. Double-check the polarity of your power supply before connecting it to the carrier to avoid damaging it. 
</p>
</div>

#### Screw Terminal Block (J4) 

<p style="text-align: justify;">
The screw terminal block connector J4 is used to power the Portenta Mid Carrier and to expose the CAN bus interface (CAN1) to the user. 
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">VIN</td>
    <td align = "center">+5V</td>
    <td align = "center">VIN</td>
    <td align = "center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">VCC</td>
    <td align = "center">+3V3<br>Portenta</td>
    <td align = "center">VCC</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">CANH</td>
    <td align = "center"></td>
    <td align = "center">CAN1 TX</td>
    <td align = "center">J1-49 (through U2)</td>
    <td align = "center">CAN BUS 1<br>CANH</td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">CANL</td>
    <td align = "center"></td>
    <td align = "center">CAN1 RX</td>
    <td align = "center">J1-51 (through U2)</td>
    <td align = "center">CAN BUS 1<br>CANL</td>
  </tr>
</tbody>
</table>

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<p style="text-align: justify;">
<strong>Reverse polarity protection:</strong> IN 5V pins of the carrier's screw terminal block (J4) and breakout header connector (J15) <strong> do not have</strong> reverse polarity protection. Double-check the polarity of your power supply before connecting it to the carrier to avoid damaging it. 
</p>
</div>

#### JTAG/SWD Connector (J3)

<p style="text-align: justify;">
The JTAG/SWD connector J3 can be used in the Portenta Mid Carrier to test and debug the connected Portenta family board. 
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center">+3V3<br>Portenta</td>
    <td align = "center">VCC</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">JTAG_SWD</td>
    <td align = "center">J1-75</td>
    <td align = "center">JTAG SWD</td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">JTAG_SCK</td>
    <td align = "center">J1-77</td>
    <td align = "center">JTAG SCK</td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">JTAG_SWO</td>
    <td align = "center">J1-79</td>
    <td align = "center">JTAG SWO</td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">NC</td>
    <td align = "center">NC</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">JTAG_TDI</td>
    <td align = "center">J1-78</td>
    <td align = "center">JTAG TDI</td>
  </tr>
  <tr>
    <td align = "center">9</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">JTAG_TRST</td>
    <td align = "center">J1-80</td>
    <td align = "center">JTAG TRST</td>
  </tr>
  <tr>
    <td align = "center">10</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">JTAG_RST</td>
    <td align = "center">J1-73</td>
    <td align = "center">JTAG RST</td>
  </tr>
</tbody>
</table>

#### MIPI Connector (J10)

<p style="text-align: justify;">

The MIPI connector J10 of the Portenta Mid Carrier can be used to connect compatible MIPI cameras to the carrier. Notice that **MIPI cameras are only compatible with the Portenta X8 board**.

</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">CAM_D0_D0_N</td>
    <td align = "center">J2-16</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">CAM_D1_D0_P</td>
    <td align = "center">J2-14</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">CAM_D2_D1_N</td>
    <td align = "center">J2-12</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">CAM_D3_D1_P</td>
    <td align = "center">J2-10</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">CAM_CK_CK_N</td>
    <td align = "center">J2-20</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">9</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">CAM_VS_CK_P</td>
    <td align = "center">J2-18</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">10</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">11</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">GPIO_5</td>
    <td align = "center">J2-56</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">12</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">NC</td>
    <td align = "center">NC</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">13</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">I2C1_SCL</td>
    <td align = "center">J1-45</td>
    <td align = "center">I2C 1 SCL</td>
  </tr>
  <tr>
    <td align = "center">14</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">I2C1_SDA</td>
    <td align = "center">J1-43</td>
    <td align = "center">I2C 1 SDA</td>
  </tr>
  <tr>
    <td align = "center">15</td>
    <td align = "center">N/A</td>
    <td align = "center">+3V3<br>Portenta</td>
    <td align = "center">VCC</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### DVP Interface Connector (J11)

<p style="text-align: justify;">
The DVP interface connector J11 of the Portenta Mid Carrier can be used to connect compatible Arducam® DVP camera modules to the carrier. 
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">VCC</td>
    <td align = "center">+3V3<br>Portenta</td>
    <td align = "center">VCC</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">SCL0</td>
    <td align = "center"></td>
    <td align = "center">I2C0_SCL</td>
    <td align = "center">J1-46</td>
    <td align = "center">I2C 0 SCL</td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">SDA0</td>
    <td align = "center"></td>
    <td align = "center">I2C0_SDA</td>
    <td align = "center">J1-44</td>
    <td align = "center">I2C 0 SDA</td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">VSYNC</td>
    <td align = "center"></td>
    <td align = "center">CAM_VS_CK_P</td>
    <td align = "center">J2-18</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">HREF</td>
    <td align = "center"></td>
    <td align = "center">CAM_HS</td>
    <td align = "center">J2-22</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">PCLK</td>
    <td align = "center"></td>
    <td align = "center">CAM_CK_CK_N</td>
    <td align = "center">J2-20</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">XCLK</td>
    <td align = "center"></td>
    <td align = "center">PWM_0</td>
    <td align = "center">J2-59</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">9</td>
    <td align = "center">DOUT7</td>
    <td align = "center"></td>
    <td align = "center">CAM_D7_D3_P</td>
    <td align = "center">J2-2</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">10</td>
    <td align = "center">DOUT6</td>
    <td align = "center"></td>
    <td align = "center">CAM_D6_D3_N</td>
    <td align = "center">J2-4</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">11</td>
    <td align = "center">DOUT5</td>
    <td align = "center"></td>
    <td align = "center">CAM_D5_D2_P</td>
    <td align = "center">J2-6</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">12</td>
    <td align = "center">DOUT4</td>
    <td align = "center"></td>
    <td align = "center">CAM_D4_D2_N</td>
    <td align = "center">J2-8</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">13</td>
    <td align = "center">DOUT3</td>
    <td align = "center"></td>
    <td align = "center">CAM_D3_D1_P</td>
    <td align = "center">J2-10</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">14</td>
    <td align = "center">DOUT2</td>
    <td align = "center"></td>
    <td align = "center">CAM_D2_D1_N</td>
    <td align = "center">J2-12</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">15</td>
    <td align = "center">DOUT1</td>
    <td align = "center"></td>
    <td align = "center">CAM_D1_D0_P</td>
    <td align = "center">J2-14</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">16</td>
    <td align = "center">DOUT0</td>
    <td align = "center"></td>
    <td align = "center">CAM_D0_D0_N</td>
    <td align = "center">J2-16</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">17</td>
    <td align = "center">PWRENABLE</td>
    <td align = "center"></td>
    <td align = "center">GPIO_3</td>
    <td align = "center">J2-52</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">18</td>
    <td align = "center">PWDN</td>
    <td align = "center"></td>
    <td align = "center">GPIO_4</td>
    <td align = "center">J2-54</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">19</td>
    <td align = "center">PWRENABLE</td>
    <td align = "center"></td>
    <td align = "center">GPIO_3</td>
    <td align = "center">J2-52</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">20</td>
    <td align = "center">PWDN</td>
    <td align = "center"></td>
    <td align = "center">GPIO_4</td>
    <td align = "center">J2-54</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### USB-A 2.0 Female Connector (J13)

<p style="text-align: justify;">
The USB-A 2.0 female connector J13 of the Portenta Mid Carrier can be used for data logging operations and to manage external peripherals with the connected Portenta family board to the carrier. 
</p>

<table align = "center"> 
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center">+5V</td>
    <td align = "center">VIN</td>
    <td align = "center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">USB0_D_N</td>
    <td align = "center">J1-28</td>
    <td align = "center">USB D-</td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">USB0_D_P</td>
    <td align = "center">J1-26</td>
    <td align = "center">USB D+</td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### microSD Card Slot (J12)

<p style="text-align: justify;">
The microSD card slot J12 of the Portenta Mid Carrier can be used for bootloading and data logging operations.
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SDC_D2</td>
    <td align = "center">J1-63</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SDC_D3</td>
    <td align = "center">J1-65</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SDC_CMD</td>
    <td align = "center">J1-57</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center">VDDSDCARD</td>
    <td align = "center">VSD</td>
    <td align = "center">J1-72</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SDC_CLK</td>
    <td align = "center">J1-55</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SDC_D0</td>
    <td align = "center">J1-59</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SDC_D1</td>
    <td align = "center">J1-61</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">CD1</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SDC_CD</td>
    <td align = "center">J1-67</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">CD2</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### RJ45 Ethernet Connector (J18)

<p style="text-align: justify;">
The RJ45 Ethernet connector J18 of the Portenta Mid Carrier can be used for Internet connectivity and networking via Ethernet.
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center">VCC</td>
    <td align = "center">VCC (through SW3)</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_C_N</td>
    <td align = "center">J1-11</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_C_P</td>
    <td align = "center">J1-9</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_B_P</td>
    <td align = "center">J1-5</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_B_N</td>
    <td align = "center">J1-7</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">N/A</td>
    <td align = "center">VCC</td>
    <td align = "center">VCC (through SW3)</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">N/A</td>
    <td align = "center">VCC</td>
    <td align = "center">VCC (through SW3)</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_D_P</td>
    <td align = "center">J1-13</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">9</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_D_N</td>
    <td align = "center">J1-15</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">10</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_A_N</td>
    <td align = "center">J1-3</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">11</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_A_P</td>
    <td align = "center">J1-1</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">12</td>
    <td align = "center">N/A</td>
    <td align = "center">VCC</td>
    <td align = "center">VCC (through SW3)</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">13</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">14</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_LED2</td>
    <td align = "center">J1-19 (through resistor)</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">15</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">ETH_LED1</td>
    <td align = "center">J1-17</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">16</td>
    <td align = "center">N/A</td>
    <td align = "center">VCC</td>
    <td align = "center">VCC (through resistor)</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">17</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">NC</td>
    <td align = "center">NC</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### GIGA Display Shield Connector (J19)

<p style="text-align: justify;">
The GIGA Display Shield connector J19 of the Portenta Mid Carrier can connect the GIGA Display Shield (SKU: ASX00039) to the carrier and the connected Portenta family board.
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">DSI D1N</td>
    <td align = "center"></td>
    <td align = "center">DSI_D1_N</td>
    <td align = "center">J1-12</td>
    <td align = "center">DSI D1 N</td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">DSI D1P</td>
    <td align = "center"></td>
    <td align = "center">DSI_D1_P</td>
    <td align = "center">J1-10</td>
    <td align = "center">DSI D1 P</td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">DSI CKN</td>
    <td align = "center"></td>
    <td align = "center">DSI_CK_N</td>
    <td align = "center">J1-20</td>
    <td align = "center">DSI CK N</td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">DSI CKP</td>
    <td align = "center"></td>
    <td align = "center">DSI_CK_P</td>
    <td align = "center">J1-18</td>
    <td align = "center">DSI CK P</td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">9</td>
    <td align = "center">DSI D0N</td>
    <td align = "center"></td>
    <td align = "center">DSI_D0_N</td>
    <td align = "center">J1-16</td>
    <td align = "center">DSI D0 N</td>
  </tr>
  <tr>
    <td align = "center">10</td>
    <td align = "center">DSI D0P</td>
    <td align = "center"></td>
    <td align = "center">DSI_D0_P</td>
    <td align = "center">J1-14</td>
    <td align = "center">DSI D0 P</td>
  </tr>
  <tr>
    <td align = "center">11</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">12</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">13</td>
    <td align = "center">DSI D2N</td>
    <td align = "center"></td>
    <td align = "center">DSI_D2_N</td>
    <td align = "center">J1-8</td>
    <td align = "center">DSI D2 N</td>
  </tr>
  <tr>
    <td align = "center">14</td>
    <td align = "center">DSI D2P</td>
    <td align = "center"></td>
    <td align = "center">DSI_D2_P</td>
    <td align = "center">J1-6</td>
    <td align = "center">DSI D2 P</td>
  </tr>
  <tr>
    <td align = "center">15</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">16</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">17</td>
    <td align = "center">DSI D3N</td>
    <td align = "center"></td>
    <td align = "center">DSI_D3_N</td>
    <td align = "center">J1-4</td>
    <td align = "center">DSI D3 N</td>
  </tr>
  <tr>
    <td align = "center">18</td>
    <td align = "center">DSI D3P</td>
    <td align = "center"></td>
    <td align = "center">DSI_D3_P</td>
    <td align = "center">J1-2</td>
    <td align = "center">DSI D3 P</td>
  </tr>
  <tr>
    <td align = "center">19</td>
    <td align = "center">NC</td>
    <td align = "center"></td>
    <td align = "center">NC</td>
    <td align = "center">NC</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">20</td>
    <td align = "center">NC</td>
    <td align = "center"></td>
    <td align = "center">NC</td>
    <td align = "center">NC</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">21</td>
    <td align = "center">VIN</td>
    <td align = "center">+5V</td>
    <td align = "center">VIN</td>
    <td align = "center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">22</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">23</td>
    <td align = "center">VCC</td>
    <td align = "center">+3V3<br>Portenta</td>
    <td align = "center">VCC</td>
    <td align = "center">J2-23, J2-34, J2-43, J2-69</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">24</td>
    <td align = "center">VIN</td>
    <td align = "center">+5V</td>
    <td align = "center">VIN</td>
    <td align = "center">J1-21, J1-24, J1-32, J1-41, J1-48</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### Mini PCIe Connector (J8)

<p style="text-align: justify;">
The Mini PCIe connector J8 of the Portenta Mid Carrier can connect compatible Mini PCie cards, for example, the Arduino® Pro 4G Module EMEA (SKU: TPX00201), to the carrier and the connected Portenta family board.
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center">+3V3 PCIE</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">GPIO_1</td>
    <td align = "center">J2-48</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center">USIM PWR</td>
  </tr>
  <tr>
    <td align = "center">9</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">10</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center">USIM DATA</td>
  </tr>
  <tr>
    <td align = "center">11</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_CK_N</td>
    <td align = "center">J2-19</td>
    <td align = "center">PCIE CK N</td>
  </tr>
  <tr>
    <td align = "center">12</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center">USIM CLK</td>
  </tr>
  <tr>
    <td align = "center">13</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_CK_P</td>
    <td align = "center">J2-17</td>
    <td align = "center">PCIE CK P</td>
  </tr>
  <tr>
    <td align = "center">14</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center">USIM RST</td>
  </tr>
  <tr>
    <td align = "center">15</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">16</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">17</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">18</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">19</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">20</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">GPIO_2</td>
    <td align = "center">J2-50</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">21</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">22</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_RST</td>
    <td align = "center">J2-21</td>
    <td align = "center">PCIE RST</td>
  </tr>
  <tr>
    <td align = "center">23</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_RX_N</td>
    <td align = "center">J2-15</td>
    <td align = "center">PCIE RX N</td>
  </tr>
  <tr>
    <td align = "center">24</td>
    <td align = "center">N/A</td>
    <td align = "center">+3V3 PCIE</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">25</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_RX_P</td>
    <td align = "center">J2-13</td>
    <td align = "center">PCIE RX P</td>
  </tr>
  <tr>
    <td align = "center">26</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">27</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">28</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">29</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">30</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">I2C0_SCL</td>
    <td align = "center">J1-46</td>
    <td align = "center">I2C 0 SCL</td>
  </tr>
  <tr>
    <td align = "center">31</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_TX_N</td>
    <td align = "center">J2-11</td>
    <td align = "center">PCIE TX N</td>
  </tr>
  <tr>
    <td align = "center">32</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">I2C0_SDA</td>
    <td align = "center">J1-44</td>
    <td align = "center">I2C 0 SDA</td>
  </tr>
  <tr>
    <td align = "center">33</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_TX_P</td>
    <td align = "center">J2-9</td>
    <td align = "center">PCIE TX P</td>
  </tr>
  <tr>
    <td align = "center">34</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">35</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">36</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">USB0_D_N</td>
    <td align = "center">J1-28</td>
    <td align = "center">USB 0 D-</td>
  </tr>
  <tr>
    <td align = "center">37</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">38</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">USB0_D_P</td>
    <td align = "center">J1-26</td>
    <td align = "center">USB 0 D+</td>
  </tr>
  <tr>
    <td align = "center">39</td>
    <td align = "center">N/A</td>
    <td align = "center">+3V3 PCIE</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">40</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">41</td>
    <td align = "center">N/A</td>
    <td align = "center">+3V3 PCIE</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">42</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">43</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">44</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">45</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">46</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">47</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">48</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">49</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">50</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">51</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">52</td>
    <td align = "center">N/A</td>
    <td align = "center">+3V3 PCIE</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### Mini PCIe Breakout Header Connector (J16)

<p style="text-align: justify;">
The Mini PCIe breakout header connector J16 of the Portenta Mid Carrier can be used to debug the Mini PCIe interface. 
</p>

<table align = "center">
<thead>
  <tr>
    <th>Pin Number</th>
    <th>Silkscreen</th>
    <th>Power Net</th>
    <th>Portenta HD Standard Pin</th>
    <th>High-Density Pin</th>
    <th>Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_CK_P</td>
    <td align = "center">J2-17</td>
    <td align = "center">PCIE CK P</td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_TX_P</td>
    <td align = "center">J2-9</td>
    <td align = "center">PCIE TX P</td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_CK_N</td>
    <td align = "center">J2-19</td>
    <td align = "center">PCIE CK N</td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_TX_N</td>
    <td align = "center">J2-11</td>
    <td align = "center">PCIE TX N</td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_RX_N</td>
    <td align = "center">J2-15</td>
    <td align = "center">PCIE RX N</td>
  </tr>
  <tr>
    <td align = "center">6</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">7</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_RX_P</td>
    <td align = "center">J2-13</td>
    <td align = "center">PCIE RX P</td>
  </tr>
  <tr>
    <td align = "center">8</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">9</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">PCIE_RST</td>
    <td align = "center">J2-21</td>
    <td align = "center">PCIE RST</td>
  </tr>
  <tr>
    <td align = "center">10</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">11</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">12</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">13</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">14</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">15</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">16</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">17</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">18</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">19</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">20</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">21</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">22</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">23</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
    <td align = "center"></td>
  </tr>
  <tr>
    <td align = "center">24</td>
    <td align = "center">N/A</td>
    <td align = "center">GND</td>
    <td align = "center">GND</td>
    <td align = "center">J1-22, J1-31, J1-42, J1-47, J1-54<br>J2-24, J2-33, J2-44, J2-57, J2-70</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

#### Serial Breakout Header Connector (J17)

<p style="text-align: justify;">
The serial breakout header connector J17 of the Portenta Mid Carrier can be used to debug the SERIAL1 interface. 
</p>

<table align = "center">
<thead>
  <tr>
    <th align = "center">Pin Number</th>
    <th align = "center">Silkscreen</th>
    <th align = "center">Power Net</th>
    <th align = "center">Portenta HD Standard Pin</th>
    <th align = "center">High-Density Pin</th>
    <th align = "center">Interface</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align = "center">1</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SERIAL1_RX</td>
    <td align = "center">J1-35</td>
    <td align = "center">UART 1 RX</td>
  </tr>
  <tr>
    <td align = "center">2</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SERIAL1_TX</td>
    <td align = "center">J1-33</td>
    <td align = "center">UART 1 TX</td>
  </tr>
  <tr>
    <td align = "center">3</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SERIAL1_RTS</td>
    <td align = "center">J1-37</td>
    <td align = "center">UART 1 RTS</td>
  </tr>
  <tr>
    <td align = "center">4</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">SERIAL1_CTS</td>
    <td align = "center">J1-39</td>
    <td align = "center">UART 1 CTS</td>
  </tr>
  <tr>
    <td align = "center">5</td>
    <td align = "center">N/A</td>
    <td align = "center"></td>
    <td align = "center">GPIO_6</td>
    <td align = "center">J2-58</td>
    <td align = "center"></td>
  </tr>
</tbody>
</table>

<div style="page-break-after: always;"></div>

### Block Diagram

An overview of the high-level architecture of the Portenta Mid Carrier is illustrated in the figure below.

![](assets/Portenta_Mid_Carrier_Block_Diagram.png)

<div style="page-break-after: always;"></div>

### Power Supply

<div style="text-align:justify;">

The figure below shows the power options available on the Arduino Portenta Mod Carrier and illustrates the Carrier's power architecture.

![](assets/Portenta_Mid_Carrier_Power_Tree.png)

The Portenta Mid Carrier can be powered through one of these interfaces:

- **Onboard USB-C® port of the Portenta board**: Provides a convenient way to power the board using standard USB-C® cables and adapters. 
- **External +5 VDC power supply**: This can be connected to the IN 5V pin of the carrier's screw terminal block J4; it can also be connected to the IN 5V pins of the breakout header connector J15. 

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<strong>Reverse polarity protection:</strong> IN 5V pins of the carrier's screw terminal block (J4) and breakout header connector (J15) <strong> do not have</strong> reverse polarity protection. Double-check the polarity of your power supply before connecting it to the Carrier to avoid damaging it. 
</div>

<div style="background-color: #FFCCCC; border-left: 6px solid #FF0000; margin: 20px 0; padding: 15px;">
<strong>Safety note:</strong> Disconnect power before modifying the carrier connections and configurations to avoid short-circuiting. For more safety tips, refer to the Carrier's user manual.
</div>

</div>

<div style="page-break-after: always;"></div>

## Device Operation

<div style="text-align:justify;">

### Getting Started - IDE

If you want to program your Arduino Portenta Mid Carrier with any of the Portenta family boards offline, install the Arduino® Desktop IDE **[1]**. To connect the Portenta family board to your computer, you will need a USB-C® cable.

### Getting Started - Arduino Web Editor

All Arduino® devices work out of the box on the Arduino® Web Editor **[2]** by installing a simple plugin. The Arduino® Web Editor is hosted online. Therefore, it will always be up-to-date with all the latest features and support for all boards and devices. Follow **[3]** to start coding on the browser and upload your sketches onto your device.

### Getting Started - Arduino Cloud

All Arduino® IoT-enabled products are supported on Arduino Cloud, which allows you to log, graph, and analyze sensor data, trigger events, and automate your home or business. Take a look at the official documentation to know more.

### Sample Sketches

Sample sketches for the Portenta family boards can be found either in the “Examples” menu in the Arduino® IDE or the “Portenta Family” section of Arduino documentation **[4]**.

### Online Resources

Now that you have gone through the basics of what you can do with the device, you can explore the endless possibilities it provides by checking exciting projects on ProjectHub **[5]**, the Arduino® Library Reference **[6]**, and the online store **[7]**, where you will be able to complement your Portenta Mid Carrier with additional extensions, sensors, and actuators.
</div>

<div style="page-break-after: always;"></div>

## Mechanical Information

<p style="text-align: justify;">
The Arduino Portenta Mid Carrier is a one-sided 114 mm x 86.5 mm board with several connectors overhanging its edges. Portenta family boards and Mini PCIE cards are placed on the carrier using dedicated connectors. 
</p>

### Carrier Dimensions

The Portenta Mid Carrier board outline and mounting hole dimensions are shown in the figure below; all the dimensions are in millimeters (mm). 

![](assets/Portenta_Mid_Carrier_Outline.png)

The carrier has four 2.7 mm drilled mounting holes for mechanical fixing.

### Carrier Connectors

Connectors of the Portenta Mid Carrier are placed primarily on its edges, but there are also some connectors placed inside of the carrier;  their placement is shown in the figure below. All the dimensions are in millimeters (mm). 

![](assets/Portenta_Mid_Carrier_Connectors.png)

## Product Compliance

### Product Compliance Summary

| **Product Compliance** |
| :--------------------: |
|  CE (European Union)   |
|          RoHS          |
|         REACH          |
|          WEEE          |
|       FCC (USA)        |
|      IC (Canada)       |
|       UKCA (UK)        |
|    Japan (No Radio)    |

### Declaration of Conformity CE DoC (EU)

<p style="text-align: justify;">
We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).
</p>

### Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

<p style="text-align: justify;">
Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.
</p>

| **Substance**                          | **Maximum Limit (ppm)** |
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

<div style="page-break-after: always;"></div>

Exemptions: No exemptions are claimed.

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration

As a global supplier of electronic and electrical components, Arduino is aware of our obligations concerning laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence, Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

## FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

1. This device may not cause harmful interference

2. This device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment

3. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

<div style="page-break-after: always;"></div>

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

1. This device may not cause interference

2. This device must accept any interference, including interference that may cause undesired operation of the device.

French:
Le présent appareil est conforme aux CNR d’Industrie Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes:

1. L’ appareil nedoit pas produire de brouillage

2. L’utilisateur de l’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

**IC SAR Warning:**

English:
This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

French:
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85 °C and shouldn’t be lower than -40 °C.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 2014/53/EU. This product is allowed to be used in all EU member states.

## Company Information

| **Company name** |              **Arduino S.r.l.**              |
|:----------------:|:--------------------------------------------:|
|  Company address | Via Andrea Appiani, 25 - 20900 Monza (Italy) |

## Reference Documentation

|            **Referece**            | **Link**                                                                        |
|:----------------------------------:|---------------------------------------------------------------------------------|
|        Arduino IDE (Desktop)       | https://www.arduino.cc/en/Main/Software                                         |
|         Arduino IDE (Cloud)        | https://create.arduino.cc/editor                                                |
|   Arduino Cloud - Getting Started  | https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started |
| Portenta Mid Carrier Documentation | https://docs.arduino.cc/hardware/portenta-mid-carrier/                          |
|             Project Hub            | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending        |
|          Library Reference         | https://www.arduino.cc/reference/en/                                            |
|            Online Store            | https://store.arduino.cc/                                                       |
         
## Document Revision History

|  **Date**  | **Revision** |  **Changes**  |
|:----------:|:------------:|:-------------:|
| 27/03/2024 |       1      | First release |