---
title: 'Portenta Max Carrier User Manual'
description: 'Get a general overview of Portenta Max Carrier and its features.'
difficulty: intermediate
tags:
  - CAN
  - RS-232
  - RS-422
  - RS-485
  - Audio
  - WiFi
  - LoRa
  - CAT-M1 / NB-IoT
  - Connectivity
author: 'Christopher Méndez'
hardware:
  - hardware/04.pro/carriers/portenta-max-carrier
  - hardware/04.pro/boards/portenta-x8
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/boards/portenta-h7-lite
  - hardware/04.pro/boards/portenta-h7-lite-connected
  - hardware/04.pro/boards/portenta-c33
software:
  - ide-v1
  - ide-v2
  - iot-cloud
---

## Overview

This user manual offers a detailed guide on the Portenta Max Carrier, consolidating all its features for easy reference. It will show how to set up, adjust, and assess its main functionalities. This manual will guide as a key to proficiently operate the Portenta Max Carrier, making it suitable for project developments related to industrial automation, manufacturing automation, robotics, and prototyping.

![Portenta Max Carrier Overview](assets/overview.png)

## Hardware and Software Requirements

### Hardware Requirements

* [Portenta Max Carrier](https://store.arduino.cc/products/portenta-max-carrier) (x1)
* [Portenta X8](https://store.arduino.cc/products/portenta-x8) (x1)
* [Portenta C33](https://store.arduino.cc/products/portenta-c33) (x1)
* [Portenta H7](https://store.arduino.cc/products/portenta-h7) (x1)
* USB-C® cable (either USB-C® to USB-A or USB-C® to USB-C®) (x1)
* Wi-Fi® Access Point or Ethernet with Internet access (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)

## Product Overview

Max Carrier transforms Portenta modules into single-board computers that enable edge AI for high-performance industrial, building automation and robotics applications.
Thanks to dedicated high-density connectors, it can be paired with Portenta X8, H7 or C33, allowing you to easily prototype and deploy your industrial projects.

This Arduino Pro carrier further augments Portenta connectivity options with Fieldbus, LoRa®, Cat-M1 and NB-IoT.
Among the many available plug-and-play connectors there are Gigabit Ethernet, USB-A, audio jacks, microSD, mini-PCIe, MIPI camera, FD-CAN and Serial RS-232/422/485.
Max Carrier can be powered via external supply (6-36V) or battery via the onboard 18650 Li-ion battery connector.

![Portenta X8 Coupling](assets/portenta-x8.gif)

### Carrier Architecture Overview

![Portenta Max Carrier board overview](assets/architecture-v3.png)

Here is an overview of the board's architecture's main components shown in the image above:

- **Compatible core**: The board is compatible with Portenta X8 (ABX00049), Portenta H7 (ABX00042/ABX00045/ABX00046), and Portenta C33 (ABX00074). The Portenta H7 and C33 are limited in camera support and the Ethernet speed to 100 Mbit.
  
- **Power management**: The Portenta Max Carrier can either be powered through the power jack (6 ~ 36V DC) or a 18650 Li-ion/LiPo battery (3.7V) that can be used as backup power source if the external power supply fails.

The battery is charged while the minimum input voltage to the power jack is met.

- **USB connectivity**: The Portenta Max Carrier also includes a USB 2.0 Hi-Speed Hub controller based on the USB2514B/M2 that manages the 2 USB devices from the USB type A connector plus the LoRa® and PCIe modules. J15 is protected by a NCP383LMUAJAATXG power switch and current limiter.

  A USB-A female connector is used for data logging and the connection of external peripherals like keyboards, mice, hubs, and similar devices.
  
- **Ethernet connectivity**: The Gigabit Ethernet physical interface (J17) is directly connected to the high density connector to the Portenta board. The connector includes an activity LED indication (orange) and speed indication (green). __Note:__ Gigabit Ethernet functionality is only supported on the Portenta X8.

- **Serial Transceiver**: The Portenta Max Carrier includes a multi-protocol transceiver supporting RS-232, RS-485, and RS-422 serial standards (configurable) based on the SP335 IC. It is connected to a 6P6C Connector (RJ11, RJ12, RJ14, RJ25).

- **CAN Transceiver**: The Portenta Max Carrier includes a high speed CAN transceiver based on the TJA1049T/3J IC. It is connected to a 4P4C connector (RJ9, RJ10, RJ22).

- **Mini PCIe**: The Portenta Max Carrier includes one female mini PCI Express card slot. The connector is right angled and the board includes 2 removable standoffs for external module support. The Max Carrier supports two different Mini PCIe sizes. Pins 8, 10, 12 and 14 are reserved for UIM (in this case SIM).
__Note:__ USB, I2C and SIM functionality over PCIe is available only for the X8. Full PCIe functionality not provided at this time.

- **Cell Modem**: The SARA-R412M-02B is a multi-region modem capable of connecting to 2G/Cat-M1/NB-IoT networks worldwide. A dedicated SMA connector allows for an external antenna. The chip operates over the 1V8 power line. A microSIM slot is available, the corresponding SIM card slot for the cell modem is on the top side of the board, directly adjacent to the module.

- **Audio**: The Portenta Max Carrier enables connections to analog audio channels. This is done through the low power CS42L52 stereo CODEC providing ADC/DAC between analog signals and the I2S protocol. An internal Class D amplifier eliminates the need for external audio amplification circuitry. 

- **LoRa® Module**: The Portenta Max Carrier provides long range wireless connectivity for low bandwidth applications with the onboard Murata CMWX1ZZABZ-078 LoRa® transceiver module. This module operates on 3V3. A dedicated SMA connector allows for an external antenna. 

- **Storage**: The board has a MicroSD card slot for data logging operation and bootloading operation from external memory.

- **Debug interface**: Debugging capabilities are integrated directly into the Portenta Max Carrier and are accessible via microUSB. The J-link debugger is compatible with the Segger® J-Link OB and Blackmagic probes, driven by the STM32F405RGT6 controller. In addition to providing access to the Portenta board JTAG ports, different sniffer channels for I2C, CAN and UART lines. The debugger firmware can be updated via SWD on CN3. Additionally, headers for debugging the LoRa® are accessible via CN2 with SWD
   
- **DIP switch**: The carrier has a DIP switch with two position and allows different profiles depending on the paired Portenta board. The DIP switch has ETH CENTER TAP and BTSEL switches.
  
  when paired with **Portenta X8**, the ETH CENTER TAP will control 1 Gbit Ethernet capacity, while the BTSEL will make the system boot from SD Card memory if turned on or from MMC memory if selected in off position.
  
  The **Portenta H7/C33** will have the 100 Mbit Ethenet capacity controlled by ETH CENTER TAP, but BTSEL does not modify any settings.

### Carrier Topology

![Portenta Max Carrier Topology](assets/maxCarrierDesignators.png)

| **Ref.** | **Description**                                        | **Ref.**       | **Description**                                           |
| -------- | ------------------------------------------------------ | -------------- | --------------------------------------------------------- |
| U1       | SARA-R412M-02B 4G LTE/Cat-M1/NB-IoT Modem IC           | U2             | CS42L52-CNZ Stereo Codec IC                               |
| U3       | USB2514Bi/M2 4-port USB 2.0 Hub IC                     | U4             | SP335EER1-L RS232/RS485/RS422 Transceiver IC              |
| U5       | TJA1049 CAN Transceiver IC                             | U6             | MPM3550EGLE Non-isolated DC-DC IC                         |
| U7       | NCP383 Current Limiting IC                             | U8,U20,U21,U22 | SN74LVC1T45 Bi-directional logic level converter IC       |
| U9       | DSC6111HI2B 12MHz MEMS Oscillator IC                   | U10            | SN74LVC1G125 Single Bus Buffer Gate IC                    |
| U11      | BQ24195RGET 4.5A Single Cell Charger IC                | U12            | AP7311 1.8V 150mA LDO Linear Regulator IC                 |
| U13      | TPS54620 6A Buck Regulator IC                          | U14            | AP2112K-3.3TRG1 3.3V 600mA LDO Regulator IC               |
| U15      | STM32F405RG 168MHz 32 bit Arm® Cortex®-M4 MCU IC         | U16-U19        | 74LVC1G157 Single 2-input multiplexer IC                  |
| U23      | CMWX1ZZABZ-078 Murrata LoRa® module                    | U24, U25       | LM73100 Ideal Diode with Reverse Polarity Protection      |
| J1, J2   | DF40HC(3.5)-80DS-0.4V(51) High Density Connectors      | J3             | Right-Angle SMA Connector for Modem                       |
| J4       | 2-1734248-0 FPC Connector                              | J5             | FW-20-05-G-D-254-150 Signal Break                         |
| J6       | 615006138421 RS232/RS485 Connector                     | J7             | 615006138421 CAN Connector                                |
| J8       | 1759546-1 Mini PCIe Connector                          | J9             | Right-Angle SMA Connector for LoRa®                       |
| J10      | ZX62-AB-5PA(31) Micro USB Debugger Connector with VBUS | J11            | 114-00841-68 Micro SD Connector                           |
| J12      | SJ-3524-SMT-TR 3.5mm Headphone Out                     | J13            | SJ-3524-SMT-TR 3.5mm Line In Right                        |
| J14      | SJ-3524-SMT-TR 3.5mm Line In Left                      | J15            | 61400826021 2-port USB 2.0 Female Connector               |
| J16      | 254TR Positive Li-ion Terminal                         | J17            | TRJK7003A97NL Gigabit Ethernet Connector                  |
| J18      | 254TR Negative Li-ion Terminal                         |             |  |
| J20      | 110990030 Connector for Speaker                  | X1             | PJ-102A 5.5mm Power Jack Adapter                          |
| CN1      | FTSH-105-01-F-DV 10-pin JTAG Header                    | CN2            | Debug Header                                              |
| CN3      | LoRa® Debug Header                                     | SIM1           | 2199337-5 microSIM Card Holder (for on-board modem)       |
| SW1      | 218-2LPST Boot Select Switch                           | SW2            | 218-2LPST Switch *(2)*                                    |
| PB1      | PTS820J25KSMTRLFS Power On Button                      | PB2            | PTS820J25KSMTRLFS Reset Button                            |

### Pinout

* ![Portenta Max Carrier Pinout](assets/ABX00043-pinout.png)

The full __pinout__ is available and downloadable as PDF from the link below:

* [Portenta Max Carrier Full Pinout](https://docs.arduino.cc/resources/pinouts/ABX00043-full-pinout.pdf)

### Datasheet

The full __datasheet__ is available and downloadable as PDF from the link below:

* [Portenta Max Carrier Datasheet](https://docs.arduino.cc/resources/datasheets/ABX00043-datasheet.pdf)

### Schematics

The full __schematics__ are available and downloadable as PDF from the link below:

* [Portenta Max Carrier Schematics](https://docs.arduino.cc/resources/schematics/ABX00043-schematics.pdf)

### STEP Files

The full __STEP__ files are available and downloadable from the link below:

* [Portenta Max Carrier STEP files](assets/ABX00043-step.zip)

## First Use Of Your Portenta Max Carrier
### Stack The Carrier

The Portenta Max Carrier design allows to stack the Portenta board with ease. The following figure shows how the Portenta boards pairs via the High-Density connectors.

![Portenta board stack](assets/x8-mount.png)

With the Portenta mounted to the carrier, you can proceed to power the carrier and begin prototyping.

### Power The Board

The Portenta Max Carrier can be powered using the following methods:

- Using an external **6 to 36V power supply** connected to the `Power Jack` of the board.
- Using a **3.7V 18650 Li-ion battery** inserted in the on-board battery socket.
- Using a USB-C® cable connected to the Portenta core board of your choice. (This option does not power the Modem and Mini PCIe connector).

![Portenta Max Carrier power options](assets/power-options.png)

### Carrier Characteristics Highlight

The Portenta Max Carrier provides its platform to the Portenta X8, H7, and C33 with different capabilities. The following table summarizes the carrier's features depending on the combination of the paired Portenta.

| Function                 | Portenta H7 Support | Portenta X8 Support | Notes                                                                   |
| ------------------------ | ------------------- | ------------------- | ----------------------------------------------------------------------- |
| USB Host                 | USB 1.0             | USB 2.0             | Max Speed: USB 1.0 - 12 Mbps, USB 2.0 - 480 Mbps                        |
| Ethernet                 | Fast Ethernet       | 1 Gbps              | Fast Ethernet - 100 Mbps                                                |
| CAN                      | Yes                 | Yes                 |                                                                         |
| Mini PCIe (USB)          | USB 1.0             | USB 2.0             | Max Speed: USB 1.0 - 12 Mbps, USB 2.0 - 480 Mbps                        |
| Mini PCIe (PCIe)         | No                  | PCIe 2.0            | Portenta H7 only supports USB based PCIe cards                          |
| Battery Charger          | Yes                 | Yes                 |                                                                         |
| LoRa®                    | Yes                 | Yes                 |                                                                         |
| NBIoT/CatM1/2G           | No                  | Yes                 | Communication with the modem is via USB, no firmware support for the H7 |
| Camera                   | No                  | MIPI up to 4 lanes  | No MIPI camera support on H7                                            |
| Audio                    | Limited             | Yes                 | No firmware support for the H7                                          |
| RS232/422/485            | Yes                 | Yes                 |                                                                         |
| on board JTAG  debugging | Yes                 | No                  |                                                                         |
| on board console to USB  | Yes                 | Yes                 |                                                                         |
| on board bus sniffing    | Limited             | Limited             | Only hardware support                                                   |

This provides a general idea how the Portenta Hat Carrier will perform depending on the paired Portenta board. Each feature is explained in the following section after quick guide covering how to properly interface the Portenta boards.

### Using Portenta X8 with Linux

### Using Portenta X8 with Arduino
### Using Portenta H7 with Arduino
### Using Portenta C33 with Arduino

### Hello World Using Linux
### Hello World Using Arduino
## High-Density Connectors

## Network Connectivity
### Ethernet
The Portenta Max Carrier is equipped with an Ethernet interface, specifically an RJ45 connector supporting 1000 Base-T.

![Portenta Max Carrier Ethernet Port](assets/ethernet.png)

Ethernet performance differs based on the associated Portenta board:

- With the Portenta X8: The system supports 1 Gbit Ethernet.
- When combined with the Portenta H7 or C33: The performance is limited at 100 Mbit Ethernet.

To configure the Ethernet settings, depending on the paired Portenta board, one must use the provided DIP switch located on the Portenta Hat Carrier. For an in-depth understanding of the DIP switch, kindly refer to [this section](#dip-switch-configuration).

Using the Portenta X8 in combination with the Hat Carrier allows you to evaluate the Ethernet speed. First, ensure the Portenta X8 is mounted on the Hat Carrier, and then connect them using a LAN cable. To measure the bandwidth, use the `iperf3` tool, which is available [here](https://github.com/userdocs/iperf3-static).



#### Using a Portenta X8 (Linux)

#### Using a Portenta H7 (Arduino)
```arduino
/**
  Web Client (Ethernet version)
  Name: opta_ethernet_web_client.ino
  Purpose: This sketch connects an Opta device to ip-api.com via Ethernet
  and fetches IP details for the device.

  @author Arduino PRO Content Team
  @version 2.0 15/08/23
*/

// Include the necessary libraries.
#include <Ethernet.h>
#include <Arduino_JSON.h>

// Server address for ip-api.com.
const char* server = "ip-api.com";

// API endpoint path to get IP details in JSON format.
String path = "/json/";

// Static IP configuration for the Opta device.
IPAddress ip(10, 0, 0, 177);

// Ethernet client instance for the communication.
EthernetClient client;

// JSON variable to store and process the fetched data.
JSONVar doc;

// Variable to ensure we fetch data only once.
bool dataFetched = false;

void setup() {
  // Begin serial communication at a baud rate of 115200.
  Serial.begin(115200);

  // Wait for the serial port to connect,
  // This is necessary for boards that have native USB.
  while (!Serial);

  // Attempt to start Ethernet connection via DHCP,
  // If DHCP failed, print a diagnostic message.
  if (Ethernet.begin() == 0) {
    Serial.println("- Failed to configure Ethernet using DHCP!");

    // Try to configure Ethernet with the predefined static IP address.
    Ethernet.begin(ip);
  }
  delay(2000);
}

void loop() {
  // Ensure we haven't fetched data already,
  // ensure the Ethernet link is active,
  // establish a connection to the server,
  // compose and send the HTTP GET request.
  if (!dataFetched) {
    if (Ethernet.linkStatus() == LinkON) {
      if (client.connect(server, 80)) {
        client.print("GET ");
        client.print(path);
        client.println(" HTTP/1.1");
        client.print("Host: ");
        client.println(server);
        client.println("Connection: close");
        client.println();

        // Wait and skip the HTTP headers to get to the JSON data.
        char endOfHeaders[] = "\r\n\r\n";
        client.find(endOfHeaders);

        // Read and parse the JSON response.
        String payload = client.readString();
        doc = JSON.parse(payload);

        // Check if the parsing was successful.
        if (JSON.typeof(doc) == "undefined") {
          Serial.println("- Parsing failed!");
          return;
        }

        // Extract and print the IP details.
        Serial.println("*** IP Details:");
        Serial.print("- IP Address: ");
        Serial.println((const char*)doc["query"]);
        Serial.print("- City: ");
        Serial.println((const char*)doc["city"]);
        Serial.print("- Region: ");
        Serial.println((const char*)doc["regionName"]);
        Serial.print("- Country: ");
        Serial.println((const char*)doc["country"]);
        Serial.println("");

        // Mark data as fetched.
        dataFetched = true;
      }
      // Close the client connection once done.
      client.stop();
    } else {
      Serial.println("- Ethernet link disconnected!");
    }
  }
}
```
### LTE CAT.M1 NB-IoT
### LoRa®
## Mini PCIe
## MIPI Camera
## Audio Interface
## DIP Switch Configuration
## USB Interface
## MicroSD Storage
## CAN Bus (Onboard Transceiver)
### JTAG Pins
## Communication
### SPI
### I2C
### CAN Bus
### Serial RS-232 / RS-422 / RS-485
### UART

## Support

If you encounter any issues or have questions while working with the Portenta Max Carrier, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for the Portenta Max Carrier. The Arduino Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Portenta Max Carrier help center page](https://support.arduino.cc/hc)

### Forum

Join our community forum to connect with other Portenta Max Carrier users, share your experiences, and ask questions. The forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Portenta Max Carrier.

- [Portenta Max Carrier category in the Arduino Forum](https://forum.arduino.cc/c/hardware/portenta/portenta-max-carrier/175)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Portenta Max Carrier.

- [Contact us page](https://www.arduino.cc/pro/contact-us)