---
title: 'Using Mini PCIe Interface with the Portenta Max Carrier & Pro 4G Module'
difficulty: intermediate
description: "Learn how to use the mPCIe interface onboard the Portenta Max Carrier with the Arduino Pro 4G Module"
tags:
  - Linux
  - mPCIe
  - Cellular
author: 'Taddy Ho Chung'
hardware:
  - hardware/04.pro/carriers/portenta-max-carrier
  - hardware/04.pro/boards/portenta-x8
  - _snippets/hardware/sim-card
---

## Overview


## Goals

## Hardware and Software Requirements

### Hardware Requirements

### Software Requirements

To use the Portenta Max Carrier with a Portenta X8, please follow these guidelines:

- Ensure your Portenta X8 has the latest Linux image. Check this section to verify that your Portenta X8 is up-to-date.

***For the smooth functioning of the Portenta Mid Carrier with the Portenta X8, it is crucial to have at least Linux **image version 7XX** on the Portenta X8. To update your board to the latest image, use the [Portenta X8 Out-of-the-box](https://docs.arduino.cc/tutorials/portenta-x8/user-manual#out-of-the-box-experience) method or [manually flash it](https://docs.arduino.cc/tutorials/portenta-x8/user-manual#update-using-uuu-tool), downloading the most recent version from this [link](https://downloads.arduino.cc/portentax8image/image-latest.tar.gz).***

### Setting Up the Hardware

The Portenta Max Carrier supports various power supply methods:

- The preferred method is to use an **external 5.0 V power supply, connecting it to the board's XX.** This ensures the carrier, the System on Module (SOM), and any PCIe modules connected are sufficiently powered. It's crucial that the power supply can meet the current demands of all components, as outlined in the provided operating conditions.

- Powering the device through a USB-C® cable connected to any Portenta core board, like the Portenta X8, will also power the core board, the carrier, and PCIe modules.

***The maximum current output of the Portenta Max Carrier is **2.0 A**.***

Below is a diagram illustrating the various power connection options for the Portenta Max Carrier, showing the different methods to supply power:

![Portenta Max Carrier Power Connection Overview](assets/portentaMIDcarrier_powerSource.png)

***It is advised to use a 5.0 V external power source, especially when using modules like the Arduino Pro 4G Module (EMEA / GNSS Global) or other mPCIe modules, to ensure a stable power supply for both the SOM and the carrier during prolonged usage.***

The following image provides a detailed view of the terminal block area on the Portenta Max Carrier, highlighting the exact location for connecting the 5 V power sources within the terminal block:

![Portenta Max Carrier Power Source within Terminal Block](assets/portentaMIDcarrier_powerSource_block.png)

### Recommended Operating Conditions

To ensure the safety and longevity of the board, it is important to be aware of the Portenta Max Carrier's operating conditions. The table provided below outlines the recommended operating conditions for the carrier:

|                   **Parameter**                    | **Min** | **Typ** | **Max** | **Unit** |
|:--------------------------------------------------:|:-------:|:-------:|:-------:|:--------:|
| 5.0 V from onboard screw terminal\* of the Carrier |    -    |   5.0   |    -    |    V     |
|    USB-C® input from the connected Portenta X8     |    -    |   5.0   |    -    |    V     |
|          Current supplied by the carrier           |    -    |    -    |   2.0   |    A     |
|           Ambient operating temperature            |   -40   |    -    |   85    |    °C    |

***The onboard screw terminal powers both the carrier and connected Portenta board.***

To ensure the power demands are met and connectivity is reliable, especially for the PMIC modules' external power, we recommend using cables that conform to the appropriate International Electrotechnical Commission (IEC) Standards and can carry currents up to 2.0 A. **Cables with a cross-sectional area ranging from 0.5 mm² to 0.75 mm², corresponding to AWG 20-18, should be adequate to manage 2.0 A of current.**

### Mini PCI Express

**Mini PCIe**, short for Mini Peripheral Component Interconnect Express, is a compact version of the PCIe interface, predominantly used in laptops and small devices for adding functionalities like Wi-Fi®, Bluetooth®, and cellular modems.

These cards are significantly smaller than standard PCIe cards, typically measuring around 30 mm x 50.95 mm, and are designed to fit into the limited spaces of compact systems. It connects to a motherboard via a dedicated Mini PCIe slot, supporting PCIe and USB 2.0 interfaces. It is available in full-size and half-size variations.

The Portenta Max Carrier has a mini PCIe slot compatible with **Arduino Pro 4G Module**, a Cat.4 modem mini PCIe card with two variants: **EMEA** and **GNSS Global**. The [EG25GGB-MINIPCIE-S](https://www.digikey.com/en/products/detail/quectel/EG25GGB-MINIPCIE-S/13278351) and its module [EG25GGB-256-SGNS](https://www.mouser.com/ProductDetail/Quectel/EG25GGB-256-SGNS?qs=GedFDFLaBXFxjpARmcjQ9Q%3D%3D&_gl=1*1esnx8e*_ga*MTA2MDkzOTk2MC4xNzAzNjg5MDc1*_ga_15W4STQT4T*MTcwMzY4OTA3NC4xLjAuMTcwMzY4OTA3NS41OS4wLjA.) for example denotes the Arduino Pro 4G GNSS Module Global variant.

![Portenta Max Carrier & PRO 4G GNSS Module Global](assets/portentaMIDcarrier_x8_4g.png)

The onboard Mini PCIe slot of the Portenta Max Carrier has the following pin layout:

| **Pin Number** | **Silkscreen Pin** |  **Power Net**  | **Portenta Standard Pin** |                        **High-Density Pin**                         |                  **Pin Detail**                   |
|:--------------:|:------------------:|:---------------:|:-------------------------:|:-------------------------------------------------------------------:|:-------------------------------------------------:|
|       1        |        N/A         |                 |                           |                                                                     |       Connected to pin 23 of J16 connector        |
|       2        |        N/A         | +3V3 PCIE (Out) |                           |                                                                     | From PCIE dedicated high current 3V3 power supply |
|       3        |        N/A         |                 |                           |                                                                     |       Connected to pin 21 of J16 connector        |
|       4        |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       5        |        N/A         |                 |                           |                                                                     |       Connected to pin 19 of J16 connector        |
|       6        |        N/A         |                 |                           |                                                                     |       Connected to pin 17 of J16 connector        |
|       7        |        N/A         |                 |          GPIO_1           |                                J2-48                                |                                                   |
|       8        |        N/A         |                 |                           |                                                                     |         Connected to pin C1 of SIM1 slot          |
|       9        |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       10       |        N/A         |                 |                           |                                                                     |         Connected to pin C7 of SIM1 slot          |
|       11       |        N/A         |                 |         PCIE_CK_N         |                                J2-19                                |                                                   |
|       12       |        N/A         |                 |                           |                                                                     |         Connected to pin C3 of SIM1 slot          |
|       13       |        N/A         |                 |         PCIE_CK_P         |                                J2-17                                |                                                   |
|       14       |        N/A         |                 |                           |                                                                     |         Connected to pin C2 of SIM1 slot          |
|       15       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       16       |        N/A         |                 |                           |                                                                     |       Connected to pin 15 of J16 connector        |
|       17       |        N/A         |                 |                           |                                                                     |       Connected to pin 13 of J16 connector        |
|       18       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       19       |        N/A         |                 |                           |                                                                     |       Connected to pin 11 of J16 connector        |
|       20       |        N/A         |                 |          GPIO_2           |                                J2-50                                |                                                   |
|       21       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       22       |        N/A         |                 |         PCIE_RST          |                                J2-21                                |        Connected to pin 9 of J16 connector        |
|       23       |        N/A         |                 |         PCIE_RX_N         |                                J2-15                                |                                                   |
|       24       |        N/A         | +3V3 PCIE (Out) |                           |                                                                     | From PCIE dedicated high current 3V3 power supply |
|       25       |        N/A         |                 |         PCIE_RX_P         |                                J2-13                                |                                                   |
|       26       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       27       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       28       |        N/A         |                 |                           |                                                                     |       Connected to pin 22 of J16 connector        |
|       29       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       30       |        N/A         |                 |         I2C0_SCL          |                                J1-46                                |       Connected to pin 28 of J15 connector        |
|       31       |        N/A         |                 |         PCIE_TX_N         |                                J2-11                                |                                                   |
|       32       |        N/A         |                 |         I2C0_SDA          |                                J1-44                                |       Connected to pin 26 of J15 connector        |
|       33       |        N/A         |                 |         PCIE_TX_P         |                                J2-9                                 |                                                   |
|       34       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       35       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       36       |        N/A         |                 |         USB0_D_N          |                                J1-28                                |         Connected to USB-A connector J13          |
|       37       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       38       |        N/A         |                 |         USB0_D_P          |                                J1-26                                |         Connected to USB-A connector J13          |
|       39       |        N/A         | +3V3 PCIE (Out) |                           |                                                                     | From PCIE dedicated high current 3V3 power supply |
|       40       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       41       |        N/A         | +3V3 PCIE (Out) |                           |                                                                     | From PCIE dedicated high current 3V3 power supply |
|       42       |        N/A         |                 |                           |                                                                     |       Connected to pin 20 of J16 connector        |
|       43       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       44       |        N/A         |                 |                           |                                                                     |       Connected to pin 18 of J16 connector        |
|       45       |        N/A         |                 |                           |                                                                     |       Connected to pin 12 of J16 connector        |
|       46       |        N/A         |                 |                           |                                                                     |       Connected to pin 16 of J16 connector        |
|       47       |        N/A         |                 |                           |                                                                     |       Connected to pin 10 of J16 connector        |
|       48       |        N/A         |                 |                           |                                                                     |       Connected to pin 14 of J16 connector        |
|       49       |        N/A         |                 |                           |                                                                     |        Connected to pin 8 of J16 connector        |
|       50       |        N/A         |     Ground      |            GND            | J1-22, J1-31, J1-42, J1-47, J1-54 J2-24, J2-33, J2-44, J2-57, J2-70 |                                                   |
|       51       |        N/A         |                 |                           |                                                                     |        Connected to pin 6 of J16 connector        |
|       52       |        N/A         | +3V3 PCIE (Out) |                           |                                                                     | From PCIE dedicated high current 3V3 power supply |

#### Mini PCIe Power Distribution

To accommodate the power requirements and ensure reliable connectivity, it is recommended to use jumper cables with appropriate International Electrotechnical Commission (IEC) Standards that can support a current of up to 2A. **Jumper cables with a cross-sectional area of 0.5 mm² to 0.75 mm² (approximately equivalent to AWG 20-18) should be sufficient to support 2A of current**.

This precaution is necessary to prevent wire overheating and ensure reliable power transmission for the connected Mini PCIe-compatible module, such as Cat.4 modems. Thus, a complete setup to use the mini PCIe interface with the Portenta Max Carrier consists of:

- **PCIE ENABLE (PWM6)** pin supplied with 3.3 V
- Properly inserted mini PCIe module, e.g., Pro 4G GNSS Module Global / Pro 4G EMEA Module

***Please make sure to use a 5.0 V external power source when using an Arduino Pro 4G Module (EMEA / GNSS Global) or any other mPCIe modules to maintain a stable power supply to the Portenta SOM and the carrier, particularly for extended periods of use.***

![Portenta Max Carrier Mini PCIe Configuration](assets/portentaMIDcarrier_mpcie_setup.png)

The following animation shows the assembly process using a mini PCIe slot compatible with the Pro 4G module.

![Portenta Max Carrier & PRO 4G GNSS Module Global Assembly Animation](assets/portentaMIDcarrier_x8_4g_animated.gif)

#### Accessing Mini PCIe Interface

It is possible to know if the compatible mini PCIe module has been correctly set up and detected using the Portenta X8. The Portenta Max Carrier's mini PCIe lanes contain USB lines, and the Pro 4G Module is recognized as a USB module.

Thus, to verify that the Pro 4G Module has been correctly powered up and recognized by the Portenta X8 with the Portenta Max Carrier, the following command is used instead of the `lspci` command:

```bash
lsusb
```

The above command will list the devices that the Portenta X8 has recognized. The following image shows similar results if the Pro 4G Module is detected.

![Portenta Max Carrier Mini PCIe Module Listing](assets/portentaMIDcarrier_mpcie_detection.png)

To learn about the implementation of the Pro 4G Module with the Portenta Max Carrier right away, you can jump to the [Cat.4 Modem (Cellular Connectivity)](#cat4-modem-cellular-connectivity) section under the [Network Connectivity](#network-connectivity) section.

#### Cat.4 Modem (Cellular Connectivity)

The **Cat.4 modem**, designed for mPCIe interfaces, uses LTE (Long Term Evolution) standards. These modems are crucial for achieving high-speed data transmission in various electronic devices.

Cat.4 modems can deliver robust data speeds, with peak download rates of up to 150 Mbps and upload rates reaching 50 Mbps. This performance level is well-suited to various online activities, including high-definition video streaming and expedient large file transfers.

The mPCIe form factor of these modems ensures compatibility with compact devices, including laptops, tablets, and IoT (Internet of Things) systems. Furthermore, these modems maintain backward compatibility with 3G and 2G networks, offering comprehensive network connectivity in diverse locations.

The Portenta Max Carrier takes advantage of this modem via an onboard mini PCIe interface and provides reliable 4G connectivity with backward compatibility for 3G and 2G networks. The **Arduino Pro 4G Module (EMEA / GNSS Global)**, a Cat.4 modem mini PCIe card using PCI Express Mini Card 1.2 Standard Interface, will be the main protagonist of this section.

The following image represents the **Arduino Pro 4G Module EMEA**:

![Arduino PRO 4G Module EMEA](assets/portenta4G_module_emea.png)

The following image represents the **Arduino Pro 4G GNSS Module Global**:

![Arduino PRO 4G GNSS Module Global](assets/portenta4G_module_global.png)

It will be available in two variants, **EMEA** and **Global (covering the US)**, this module can be integrated with various Portenta boards to create expansive smart cities/buildings and implement remote maintenance and fleet management systems.

![Arduino PRO 4G GNSS Module Global / Module EMEA](assets/portentaQuectel_overview.gif)

## Instructions

#### Setting Up Via Out-Of-The-Box Experience

Having the Portenta X8 paired with the Portenta Max Carrier, the modem can be quickly completed through the Out-Of-The-Box setup process.

***If you are not familiar with the Out-Of-The-Box experience of the Portenta X8, it is recommended to read the [Out-Of-The-Box Experience section of the Portenta X8 User Manual](https://docs.arduino.cc/tutorials/portenta-x8/user-manual/#out-of-the-box-experience) to gain a better understanding before proceeding.***

Navigate to the Out-Of-The-Box dashboard of the Portenta X8.

![PRO 4G GNSS Module OOTB Activation - Main Page](assets/portentaMIDcarrier_modem_main.png)

In this dashboard, you will find the **Settings** option. Please click on this option to proceed to the next step.

![PRO 4G GNSS Module OOTB Activation - Settings Option](assets/portentaMIDcarrier_modem_options.png)

You will see three setup options in the **Settings** section. Select the **LTE/4G Sim** option to begin the modem setup.

Make sure the Quectel 4G modem is connected to the mini PCIe slot at this stage, with the **3V3_PCIE** pin of the Mini PCIe power breakout connected to the **3V3_BUCK** of the same breakout header. 

![PRO 4G GNSS Module OOTB Activation - Modem Parameters](assets/portentaMIDcarrier_modem_init.png)

In the **LTE/4G Sim** setting, it will require you to provide the following:

- **APN**
- **PIN**

Additionally, it is necessary to select an **Authentication Protocol**, which could be either:

- **PAP/CHAP**
- **NONE**

Briefly, PAP (Password Authentication Protocol) sends credentials in plain text, which is suitable for low-security or legacy environments. At the same time, CHAP (Challenge-Handshake Authentication Protocol) improves security with three-way handshake and hash functions, protecting against replay attacks and providing a more secure option than PAP.

Make sure to provide these details according to your SIM card settings. After completing these steps, the bottom left of the Out-Of-The-Box interface will display the **4G/LTE Network** connection status.

![PRO 4G GNSS Module OOTB Activation - Network Status](assets/portentaMIDcarrier_modem_netStat.png)

A notification will also appear briefly to inform you that the Portenta X8 has successfully established a network connection if it finds an available network. By selecting **SYSTEM INFO**, you can view detailed information about the established network connection.

![PRO 4G GNSS Module OOTB Activation - System Information](assets/portentaMIDcarrier_modem_sysInfo.png)

With this, you now have the Portenta X8 connected to a 4G/LTE network using the Portenta Max Carrier through the Quectel mini PCIe modem.

#### Setting Up Using Linux Environment

If you choose to establish a network connection via ADB shell, a sequence of commands is required. But before anything else, the Portenta X8 must have the following overlays active:

```bash
ov_som_lbee5kl1dx ov_som_x8h7 ov_carrier_enuc_bq24195 ov_carrier_max_usbfs ov_carrier_max_sdc ov_carrier_max_cs42l52 ov_carrier_max_pcie_mini
```

To set the corresponding overlays, following command can be used:

```bash
fw_setenv overlays 'ov_som_lbee5kl1dx ov_som_x8h7 ov_carrier_enuc_bq24195 ov_carrier_max_usbfs ov_carrier_max_sdc ov_carrier_max_cs42l52 ov_carrier_max_pcie_mini'
```

Afterward, the setup process involves bringing down the `wwan0` interface, setting it to raw IP mode, and then bringing it back up:

```bash
ip link set dev wwan0 down
```

```bash
echo Y > /sys/class/net/wwan0/qmi/raw_ip
```

```bash
ip link set dev wwan0 up
```

The following steps include using `qmicli` commands to check the card status and start a network connection:

```bash
qmicli --device=/dev/cdc-wdm0 --device-open-proxy --uim-get-card-status
```

![PRO 4G GNSS Module - Card Status](assets/portentaMIDcarrier_mpcie_card_status.png)

```bash
qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=iot.1nce.net" --client-no-release-cid
```

![PRO 4G GNSS Module - Network Initialization](assets/portentaMIDcarrier_mpcie_network_start.png)

After establishing the network connection, you can use `udhcpc` to manage dynamic IP configuration:

```bash
udhcpc -q -f -n -i wwan0
```

![PRO 4G GNSS Module - Dynamic IP Configuration](assets/portentaMIDcarrier_mpcie_dynamic.png)

A speed test can be performed to test the speed and performance of the connection. It involves downloading the `speedtest-cli` script, converting it to an executable, and running it inside a Docker container:

```bash
wget -O speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
```

```bash
chmod +x speedtest-cli
```

```bash
docker run python:3.8-slim-buster
```

```bash
docker run -it --mount type=bind,source="$(pwd)",target=/app python:3.8-slim-buster /bin/bash
```

```bash
/app/speedtest-cli
```

Once the speed test concludes, you can see similar behavior to the following image.

![PRO 4G GNSS Module - Speed Test](assets/portentaMIDcarrier_mpcie_4gmodem_result.png)

***The download and upload speed may vary depending on the region.***

This comprehensive setup shows how Mini PCIe cards can be integrated and used in compact systems as carriers, leveraging their ability to provide additional functionalities while maintaining a small footprint.

To compress into a single line of command, the following format is also suggested:

```bash
nmcli c add type gsm ifname cdc-wdm0 con-name wwan0 apn hologram connection.autoconnect yes
```

In case the SIM card requires a PIN number, the format is modified slightly as follows:

```bash
nmcli c add type gsm ifname cdc-wdm0 con-name wwan0 apn mobile.vodafone.it gsm.pin <PIN>
```

## Conclusion
