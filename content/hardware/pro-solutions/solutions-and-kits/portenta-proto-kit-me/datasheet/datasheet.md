---
identifier: AKX00073
title: Arduino® Portenta Proto Kit ME
type: pro
author: José Bagur
---

![](assets/proto-kit-perspective.png)

# Description

<p style="text-align: justify;">Expand your environmental monitoring and motion detection projects with the Arduino Portenta Proto Kit ME (Motion Environment). This kit integrates multiple Arduino Pro products, offering a complete toolkit for collecting data in applications such as predictive maintenance, asset tracking, smart building systems and industrial automation. Designed for reliability and efficiency, the kit features robust sensing capabilities and seamless Cloud connectivity enabled by the Arduino Pro 4G Module. Leverage the Portenta Proto Kit ME to accelerate your prototyping process and transition smoothly from functional prototypes to final products.</p>

# Target Areas

Predictive maintenance, asset tracking, smart building systems, industrial automation, research and development

# CONTENTS
## Application Examples

<p style="text-align: justify;">The Arduino Portenta Proto Kit ME (Motion Environment) is not just a prototyping platform, it is a versatile toolkit for innovation in motion detection and environmental monitoring, designed for applications across industrial automation, smart buildings and logistics. Discover how the Portenta Proto Kit ME can bring your ideas to life through the following application examples:</p>

- **Industrial automation**: Enhance operational efficiency and reliability with the Portenta Proto Kit ME, offering solutions for:
  - <p style="text-align: justify;"><strong>Predictive maintenance</strong>: Use the Nicla Sense ME to collect environmental data such as temperature, humidity and motion to monitor equipment health. Combine this data with the Portenta H7 board for advanced processing and Cloud integration to detect anomalies, schedule proactive maintenance and minimize downtime.</p>
  - <p style="text-align: justify;"><strong>High-speed test rigs</strong>: Design modular and scalable test benches for industrial applications, integrating motion detection, environmental monitoring and data exchange. Use the Portenta Proto Kit ME to perform sensor calibration, load testing and real-time functional evaluations, transmitting data to the Cloud for analysis.</p>
  - <p style="text-align: justify;"><strong>Remotely monitored machinery</strong>: Build systems for real-time monitoring and control using the Nicla Sense ME for motion and environmental sensing. Integrate with the Portenta H7 board and leverage Cloud connectivity to monitor equipment status, adjust parameters and receive alerts remotely, ensuring efficient operations.</p>

- **Building automation/smart cities**: Create smarter, more connected environments with the Portenta Proto Kit ME, enabling innovative solutions such as:
  - <p style="text-align: justify;"><strong>Environmental monitoring</strong>: Use the Nicla Sense ME to track indoor air quality, temperature and humidity in real time. Process the data locally with the Portenta H7 board to make informed decisions for optimizing indoor environments, improving comfort and ensuring energy efficiency.</p>
  - <p style="text-align: justify;"><strong>Intrusion detection systems</strong>: Develop motion-sensitive security systems using the Nicla Sense ME to detect unauthorized movement or environmental anomalies. Send alerts to designated devices via the Arduino Pro 4G Module for immediate action and remote monitoring.</p>
  - <p style="text-align: justify;"><strong>Smart logistics</strong>: Monitor goods in transit with the Nicla Sense ME to track motion, environmental conditions and vibration. Use cloud connectivity with the Portenta H7 board for seamless data transmission and analytics, enabling efficient logistics management and goods protection.</p>

- **Smart mobility**: Enable innovative applications in transportation and logistics with advanced motion and environmental sensing:
  - <p style="text-align: justify;"><strong>Vibration monitoring</strong>: Use the Nicla Sense ME to detect vibrations during transit, ensuring the safety of delicate goods or identifying potential issues in vehicle performance.</p>
  - <p style="text-align: justify;"><strong>Route optimization</strong>: Collect motion and environmental data to optimize delivery routes, integrating real-time insights through Cloud analytics for enhanced operational efficiency.</p>

## Features
### Kit Contents

<p style="text-align: justify;">The Arduino Portenta Proto Kit ME includes all the hardware components necessary to prototype motion detection and environmental monitoring applications effectively. Below is the list of included items and its main features and specifications:</p>

- Portenta H7 (SKU: ABX00042) (x1)
- Nicla Sense ME (SKU: ABX00050) (x1)
- Portenta Mid Carrier (SKU: ASX00055) (x1)
- Portenta Mid Carrier Proto Shield (x1)
- Arduino Pro 4G GNSS Module Global (SKU: TPX00200) (x1)
- Modulino® nodes (x7):
  - Knob (encoder with push button) (x1)
  - Pixels (8x RGB LEDs) (x1)
  - Distance (Time-of-Flight sensor) (x1)
  - Movement (6-axis IMU) (x1)
  - Buttons (3x push buttons and LEDs) (x1)
  - Buzzer (x1)
  - Thermo (temperature and humidity sensor) (x1)

![Exploded view of the Portenta Proto Kit ME, showcasing most of the kit's components.](assets/proto-kit-perspective-dismounted.png)

<div style="page-break-after: always;"></div>

#### Portenta H7 (SKU: ABX00042)

<p style="text-align: justify;">The Portenta H7 is a dual-core microcontroller board powered by the STMicroelectronics® STM32H747XI, featuring a 32-bit Arm® Cortex®-M7 running at 480 MHz and a Cortex®-M4 at 240 MHz. It includes advanced graphics capabilities and operates within an industrial temperature range (-40 °C to 85 °C).</p>

<img src="assets/portenta_h7.jpg" alt="Portenta H7 board" style="width: 60%; height: auto;"></img>

Below is a summary of the most important specifications of the Portenta H7 board:

| **Feature**                | **Specification**                                                                         |
|----------------------------|-------------------------------------------------------------------------------------------|
| **Microcontroller**        | STMicroelectronics® STM32H747XI Dual 32-bit Arm® Cortex®-M7 and Cortex®-M4                |
| **USB Connector**          | USB-C®                                                                                    |
| **Digital I/O Pins**       | 78 (High-Density Pins)                                                                    |
| **Analog Input Pins**      | 8 (High-Density Pins)                                                                     |
| **PWM Pins**               | 10 (High-Density Pins)                                                                    |
| **Wireless Connectivity**  | Wi-Fi® 2.4 GHz 802.11 b/g/n, Bluetooth® 4.1 (Murata® LBEE5KL1DX)                          |
| **Ethernet Connectivity**  | RMII 10/100 Mbps (LAN8742AI)                                                              |
| **Secure Element**         | NXP® SE050C2 and Microchip® ATECC608                                                      |
| **Clock Speed**            | 480 MHz (M7 core), 240 MHz (M4 core)                                                      |
| **Memory**                 | 2 MB Flash, 1 MB RAM (internal); 16 MB NOR Flash, 8 MB SDRAM (external)                   |
| **Board Dimensions**       | 66.04 mm x 25.40 mm                                                                       |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <p style="text-align: justify;">
    For detailed information about the Portenta H7 board, please refer to its corresponding documentation available on Arduino Docs:
    <a href="https://docs.arduino.cc/hardware/portenta-h7/" target="_blank" style="color: #0056b3; text-decoration: underline;">
      Portenta H7 Official Documentation [8]
    </a>
  </p>
</div>

<div style="page-break-after: always;"></div>

#### Nicla Sense ME (SKU: ABX00050)

<p style="text-align: justify;">The Nicla Sense ME is a compact microcontroller board powered by the Nordic Semiconductor® nRF52832, featuring a 32-bit Arm® Cortex®-M4 running at 64 MHz. This board is designed for environmental monitoring and motion sensing applications, integrating multiple high-performance sensors.</p> 

<img src="assets/nicla_sense_me.jpg" alt="Nicla Sense ME board" style="width: 55%; height: auto;"></img>

Below is a summary of the most important specifications of the Nicla Sense ME board:

| **Feature**               | **Specification**                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Microcontroller**       | Nordic Semiconductor® nRF52832 32-bit Arm® Cortex®-M4                                                                |
| **USB Connector**         | Micro-USB                                                                                                            |
| **Digital I/O Pins**      | 10                                                                                                                   |
| **Analog Input Pins**     | 2                                                                                                                    |
| **PWM Pins**              | 12                                                                                                                   |
| **Wireless Connectivity** | Bluetooth® 5.0 (u-blox® ANNA-B112)                                                                                   |
| **Onboard Sensors**       | BHI260AP (IMU), BMP390 (barometric sensor), BMM150 (geomagnetic sensor), BME688 (gas, temperature, humidity sensors) |
| **Clock Speed**           | 64 MHz                                                                                                               |
| **Memory**                | 512 kB Flash, 64 kB SRAM (internal); 2 MB QSPI Flash (external)                                                      |
| **Onboard Interfaces**    | SPI (x1), I2C (x1), UART (x1)                                                                                        |
| **Dimensions**            | 22.86 mm x 22.86 mm                                                                                                  |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <p style="text-align: justify;">
    For detailed information about the Nicla Sense ME board, please refer to its corresponding documentation available on Arduino Docs:
    <a href="https://docs.arduino.cc/hardware/nicla-sense-me/" target="_blank" style="color: #0056b3; text-decoration: underline;">
      Nicla Sense ME Official Documentation [9]
    </a>
  </p>
</div>

<div style="page-break-after: always;"></div>

#### Portenta Mid Carrier (SKU: ASX00055)

<p style="text-align: justify;">The Arduino Portenta Mid Carrier expands connectivity options for Portenta family boards, including Ethernet, USB-A, mPCIe, CAN, MicroSD, and 4G. It also features JTAG pins for debugging and supports I2C, SPI, PWM, digital, and analog I/Os.</p> 

<img src="assets/portenta_mid_carrier.jpg" alt="Portenta Mid Carrier" style="width: 70%; height: auto;"></img>

Below is a summary of the most important specifications of the Portenta Mid Carrier:

| **Feature**                  | **Specification**                                                                                                                            |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Compatible Boards**        | Portenta X8, Portenta H7 (except MIPI Camera), Portenta C33 (except MIPI Camera)                                                             |
| **Camera Interfaces**        | MIPI Connector (x1), Arducam Connector (x1), USB-A (x1)                                                                                      |
| **Display Interface**        | DSI (x1)                                                                                                                                     |
| **Communication Interfaces** | 4G (mPCIe, x1), Ethernet (x1), SPI (x2), I2C (x3), UART (x4), CAN FD (x2, one without transceiver), I2S (x1), SAI (x1), PDM (x1), SPDIF (x1) |
| **User Interface**           | Power On Push Button (x1)                                                                                                                    |
| **Storage**                  | MicroSD card slot (x1)                                                                                                                       |
| **Hardware Debugging**       | JTAG/SWD                                                                                                                                     |
| **Power Supply**             | Board operating voltage (VIN): +5 VDC; Maximum current provided: 2 A                                                                         |
| **Dimensions**               | 114 mm x 86.5 mm                                                                                                                             |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <p style="text-align: justify;">
    For detailed information about the Portenta Mid Carrier, please refer to its corresponding documentation available on Arduino Docs:
    <a href="https://docs.arduino.cc/hardware/portenta-mid-carrier/" target="_blank" style="color: #0056b3; text-decoration: underline;">
      Portenta Mid Carrier Official Documentation [10]
    </a>
  </p>
</div>

<div style="page-break-after: always;"></div>

#### Arduino Pro 4G GNSS Module Global (SKU: TPX00200)

<p style="text-align: justify;">Designed in the widely used Mini PCI Express (mPCIe) format, this module provides global LTE Cat.4 connectivity, 4G support, and GNSS capabilities.</p>

<img src="assets/4g_module.jpg" alt="Arduino Pro 4G GNSS Module" style="width: 40%; height: auto;"></img>

Below is a summary of the most important specifications of the Arduino Pro 4G GNSS Module Global:

| **Feature**               | **Specification**                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------------|
| **Module Format**         | Mini PCI Express (mPCIe), PCI Express Mini Card 1.2 Standard Interface                        |
| **Cellular Connectivity** | LTE Cat.4 with 2G/3G fallback                                                                 |
| **GNSS**                  | GPS, GLONASS, BeiDou, Galileo, QZSS (Protocol: NMEA 0180, Update Rate: 1 Hz)                  |
| **LTE Characteristics**   | RF Bandwidth: 1.4, 3, 5, 10, 15, 20 MHz; Download: 150 Mbps; Upload: 50 Mbps                  |
| **UMTS Characteristics**  | DC-HSDPA: 42 Mbps (Download); HSUPA: 5.76 Mbps (Upload); WCDMA: 384 kbps                      |
| **GSM Characteristics**   | EDGE: 296 kbps (Download), 236.8 kbps (Upload); GPRS: 107 kbps (Download), 85.6 kbps (Upload) |
| **Antenna Connectors**    | Main, diversity and GNSS antenna receptacles                                                  |
| **Power Supply**          | +3.3 VDC                                                                                      |
| **Interfaces**            | USB, UART, PCM/I2C                                                                            |
| **Certifications**        | CE, ROHS, REACH, UKCA, FCC, IC                                                                |
| **Dimensions**            | 30 mm x 51 mm                                                                                 |
| **Temperature Range**     | Operating: -35 °C to +75 °C; Extended: -40 °C to +80 °C; Storage: -40 °C to +90 °C            |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <p style="text-align: justify;">
    For detailed information about the Arduino Pro 4G GNSS Module Global, please refer to its corresponding documentation available on Arduino Docs:
    <a href="https://docs.arduino.cc/hardware/pro-4g-module/" target="_blank" style="color: #0056b3; text-decoration: underline;">
      Arduino Pro 4G GNSS Module Official Documentation [11]
    </a>
  </p>
</div>

<div style="page-break-after: always;"></div>

### Kit Included Accessories

- +24 VDC/1A power supply (x1) 
- M2.5 nut (x2)
- M2.5 screw (x2)
- M2.5 washer (x2)
- M2.5 x 7 spacer (x2)
- QWIIC cable (x7)
- USB-A to USB-C® cable (x1)
- USB-A to Micro USB cable (x1)
- Arduino Pro 4G Module antennas kit (SKU: TPX002199) (x1)

### Kit Related Products

- Arduino X8 (SKU:ABX00074)
- Arduino Nicla Voice (SKU:ABX00061)
- Arduino Nicla Vision (SKU: ABX00051)
- Arduino Portenta C33 (SKU: ABX00049)

<div style="page-break-after: always;"></div>

## Ratings

### Recommended Operating Conditions

<p style="text-align: justify;">
The table below provides a comprehensive guideline for the optimal use of the Arduino Portenta Proto Kit ME, outlining typical operating conditions and design limits. The operating conditions of the Portenta Proto Kit ME are largely a function based on its component's specifications.
</p>

|                **Parameter**               |    **Symbol**   | **Min** | **Typ** | **Max** | **Unit** |
|:------------------------------------------:|:---------------:|:-------:|:-------:|:-------:|:--------:|
| Input Voltage of the Power Jack Connector¹ | V<sub>PJC</sub> |   7.0   |    -    |    30   |     V    |
|           Operating Temperature²           |  T<sub>O</sub>  |   -40   |    -    |    85   |    °C    |

<sup>1</sup> Onboard power jack connector of the Portenta Mid Carrier Proto Shield.
<sup>2</sup> The operating temperature represents the range for the entire kit and not just an individual component.

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<p style="text-align: justify;"><strong>Note:</strong> While the kit can be powered through different pins and connectors, the recommended method is to use the power jack connector of the Portenta Mid Carrier Proto Shield. Any alternative power options should be carefully evaluated by consulting the individual power specifications of each component to avoid potential damage.</p>
</div>

<div style="page-break-after: always;"></div>

## Kit Power Supply

<p style="text-align: justify;">The Arduino Portenta Proto Kit ME can be powered through one of the following recommended methods:</p>

- <p style="text-align: justify;"><strong>Portenta Mid Carrier Proto Shield onboard power jack</strong>: Provides a dedicated connection to power the kit using a +7 to 30 VDC input. The kit includes a compatible +24 VDC/1A power supply intended to be used with this power jack.</p>
- <p style="text-align: justify;"><strong>USB-C® connector on the Portenta H7 board</strong>: Allows powering the kit with +5 VDC through the Portenta H7's USB-C® port or the terminal pins on the Portenta Mid Carrier.</p>

![Power options of the Portenta Proto Kit ME](assets/kit_power_supply.png)

<div style="background-color: #FFFFE0; border-left: 6px solid #FFD700; margin: 20px 0; padding: 15px;">
<p style="text-align: justify;"><strong>Tip:</strong> To ensure reliable performance, always prioritize using the dedicated power jack on the Portenta Mid Carrier Proto Shield and the kit's provided power supply for configurations requiring higher power stability.</p>
</div>

<div style="background-color: #FFCCCC; border-left: 6px solid #FF0000; margin: 20px 0; padding: 15px;">
<p style="text-align: justify;"><strong>Safety Note:</strong> Always disconnect power before making hardware changes to the kit. Ensure that power specifications are within the recommended limits to avoid damage to components.</p>
</div>

<div style="page-break-after: always;"></div>

## Device Operation

### Getting Started - IDE

<p style="text-align: justify;">If you want to program your Arduino Portenta Proto Kit ME offline, install the Arduino Desktop IDE <strong>[1]</strong>. To connect the Portenta H7 to your computer, you will need a USB-C® cable. Additionally, to program or interact with the Nicla Sense ME, ensure you have a Micro USB cable compatible with the board.</p>

### Getting Started - Arduino Cloud Editor

<p style="text-align: justify;">All components of the Portenta Proto Kit ME work seamlessly on the Arduino Cloud Editor <strong>[2]</strong> by installing a simple plugin. The Arduino Cloud Editor is hosted online, ensuring it is always up-to-date with the latest features and support for all boards and devices. Follow <strong>[3]</strong> to start coding in the browser and upload your sketches onto the Portenta H7 or other components.</p>

### Getting Started - Arduino Cloud

<p style="text-align: justify;">The Portenta Proto Kit ME is fully supported on Arduino Cloud, enabling you to log, graph, and analyze sensor data, trigger events and automate processes for industrial, business, or smart home applications via the Portenta H7 board. Take a look at the official documentation <strong>[3]</strong> to learn more about how to integrate the kit into your IoT projects.</p>

### Sample Sketches

<p style="text-align: justify;">Sample sketches for the Portenta Proto Kit ME can be found either in the “Examples” menu in the Arduino IDE or the “Portenta Proto Kit ME Documentation” section of Arduino documentation <strong>[4]</strong>. These examples include basic and advanced applications showcasing motion and environmental monitoring capabilities.</p>

### Online Resources

<p style="text-align: justify;">Now that you have gone through the basics of what you can do with the Portenta Proto Kit ME, you can explore the endless possibilities it provides by checking exciting projects on Arduino Project Hub <strong>[5]</strong>, the Arduino Library Reference <strong>[6]</strong> and the ACE-220 online course <strong>[7]</strong>. The Enterprise Prototyping with Portenta Proto Kit ME (ACE-220) course is a resource designed to help you master prototyping in embedded electronics and IoT. Gain hands-on experience with the kit and accelerate your journey from concept to innovation by building functional prototypes tailored for industrial and IoT applications.</p>

<div style="page-break-after: always;"></div>

## Mechanical Information

<p style="text-align: justify;">
The Arduino Portenta Proto Kit ME offers significant mechanical flexibility, supporting multiple configurations based on the combination of components used. This section provides the main dimensions of one possible configuration for reference. For detailed mechanical specifications of each individual component, please consult the corresponding documentation available on Arduino Docs.
</p>

### Kit Dimensions

<p style="text-align: justify;">
The figures below show the main dimensions of the kit in a stacked configuration that includes the Portenta H7 board, the Portenta Mid Carrier, the Portenta Mid Carrier Proto Shield, the Arduino Pro 4G Module, one Modulino® node (Pixels), and the Nicla Sense ME board. All dimensions are in millimeters (mm).
</p>

- <p style="text-align: justify;"><strong>Top View</strong>: Displays the width and length of the stacked components configuration of the kit.</p>

![](assets/proto-kit-example-mechanical-1.png)

<div style="page-break-after: always;"></div>

- <p style="text-align: justify;"><strong>Side View</strong>: Displays the height of the stacked components configuration of the kit.</p>

![](assets/proto-kit-example-mechanical-2.png)

<div style="page-break-after: always;"></div>

## Product Compliance

<p style="text-align: justify;">The Arduino Portenta Proto Kit ME is composed of multiple individual Arduino products, each of which complies with specific regulations and certifications. For detailed product compliance information, please refer to the corresponding datasheets of each component included in the kit:</p>

- [Portenta H7 Documentation](https://docs.arduino.cc/hardware/portenta-h7/) **[8]**
- [Nicla Sense ME Documentation](https://docs.arduino.cc/hardware/nicla-sense-me/) **[9]**
- [Portenta Mid Carrier Documentation](https://docs.arduino.cc/hardware/portenta-mid-carrier/) **[10]**
- [Arduino Pro 4G Module Documentation](https://docs.arduino.cc/hardware/pro-4g-module/) **[11]**


## FCC Caution

<p style="text-align: justify;">The components of the Arduino Portenta Proto Kit ME are subject to individual FCC regulations. Please refer to the FCC documentation linked in each Arduino component's datasheet for specific compliance details:</p>

- [Portenta H7 Documentation](https://docs.arduino.cc/hardware/portenta-h7/) **[8]**
- [Nicla Sense ME Documentation](https://docs.arduino.cc/hardware/nicla-sense-me/) **[9]**
- [Portenta Mid Carrier Documentation](https://docs.arduino.cc/hardware/portenta-mid-carrier/) **[10]**
- [Arduino Pro 4G Module Documentation](https://docs.arduino.cc/hardware/pro-4g-module/) **[11]**

## Company Information

| **Company name** |              **Arduino S.r.l.**              |
|:----------------:|:--------------------------------------------:|
| Company address  | Via Andrea Appiani, 25 - 20900 Monza (Italy) |

## Reference Documentation

| **No.** |            **Reference**            | **Link**                                                |
|:-------:|:-----------------------------------:|---------------------------------------------------------|
|    1    |        Arduino IDE (Desktop)        | https://www.arduino.cc/en/software                      |
|    2    |         Arduino Cloud Editor        | https://create.arduino.cc/editor                        |
|    3    |   Arduino Cloud - Getting Started   | https://docs.arduino.cc/arduino-cloud/guides/overview/  |
|    4    | Portenta Proto Kit ME Documentation | https://docs.arduino.cc/hardware/portenta-proto-kit-me/ |
|    5    |         Arduino Project Hub         | https://create.arduino.cc/projecthub                    |
|    6    |      Arduino Library Reference      | https://docs.arduino.cc/language-reference/             |
|    7    |        ACE-220 Online Course        | https://academy.arduino.cc/courses/ace-220              |
|    8    |      Portenta H7 Documentation      | https://docs.arduino.cc/hardware/portenta-h7/           |
|    9    |     Nicla Sense ME Documentation    | https://docs.arduino.cc/hardware/nicla-sense-me/        |
|    10   |  Portenta Mid Carrier Documentation | https://docs.arduino.cc/hardware/portenta-mid-carrier/  |
|    11   | Arduino Pro 4G Module Documentation | https://docs.arduino.cc/hardware/pro-4g-module/         |

## Document Revision History

|  **Date**  | **Revision** |   **Changes**  |
|:----------:|:------------:|:--------------:|
| 20/01/2025 |       3      |  Format fixes  |
| 16/01/2025 |       2      | Review changes |
| 10/01/2025 |       1      |  First release |
