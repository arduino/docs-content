---
identifier: TPX00242
title: Arduino® USB-C Power Supply (45W)
type: maker
---

![Arduino USB-C Power Supply](assets/featured.png)

# Description

<p style="text-align: justify;">The Arduino® USB-C Power Supply (45W) (TPX00242) is a compact, interchangeable plug adapter designed for use with USB-C devices supporting USB Power Delivery (PD). The 45 W multi-voltage power adapter provides intelligent power delivery across five voltage profiles (5 V, 9 V, 12 V, 15 V, 20 V), negotiating the optimal charging parameters for connected devices. With interchangeable regional plugs (EU, UK, US, AU) and broad safety certifications, it provides a universal power solution for development, prototyping, and deployment scenarios worldwide.</p>

<div style="page-break-after: always;"></div>

# CONTENTS

## Features

### General Specifications

![Arduino USB-C Power Supply](assets/power_supply_views.png)

| **Feature**        | **Specification**                                                  |
|--------------------|--------------------------------------------------------------------|
| Model Number       | TPX00242                                                           |
| Adapter Type       | Interchangeable plug-in adapter                                    |
| Output Connector   | USB-C (USB Type-C)                                                 |
| Dimensions (Body)  | 64 × 64 × 30 mm (folded plug) / 64 × 80.06 × 30 mm (unfolded plug) |
| Material           | PC (Polycarbonate) housing                                         |

### Input Specifications

| **Parameter**         | **Specification**     |
|-----------------------|-----------------------|
| Rated Input Voltage   | 100 - 240 V AC        |
| Input Voltage Range   | 90 - 264 V AC         |
| Input Frequency       | 47 - 63 Hz (50/60 Hz) |
| Maximum Input Current | 1.5 A                 |

### Output Specifications

![Arduino USB-C Power Supply Output](assets/power-supply-usbc-port.png)

| **Output Voltage** | **Maximum Current** | **Maximum Power** |
|-------------------:|--------------------:|------------------:|
|           5.0 V DC |               3.0 A |              15 W |
|           9.0 V DC |               3.0 A |              27 W |
|          12.0 V DC |               3.0 A |              36 W |
|          15.0 V DC |               3.0 A |              45 W |
|          20.0 V DC |              2.25 A |              45 W |

**Combined Maximum Output Power:** 45 W

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Note:</strong> The power supply negotiates the appropriate voltage and current with the connected device using USB Power Delivery (PD) protocol. The device will select the optimal power profile based on its requirements.
</div>

### Power Delivery Protocols

| **Protocol** | **Support** |
|--------------|-------------|
| USB PD 3.0   | Supported   |
| PPS          | Supported   |

### Regional Plug Options

![Regional Plug Options](assets/plug_options.png)

| **Region**              | **Plug Type** | **Dimensions (W × H × D)**      |
|-------------------------|---------------|---------------------------------|
| United States (Default) | Type A        | Integrated (foldable)           |
| Europe (EU)             | Type C        | 34.6-36.0 × 27.5 × 37 mm        |
| United Kingdom          | Type G        | 48.98 × 39.83 × 22.23-23.23 mm* |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Note:</strong> Plugs are interchangeable and can be replaced without tools. Make sure the correct plug is attached for your region before use.
</div>

<div style="page-break-after: always;"></div>

## Usage

<p style="text-align: justify;">The Arduino USB-C Power Supply provides optimal power delivery for USB-C devices and their peripherals. When used with USB-C hubs or dongles, this power supply allows stable operation of connected devices alongside multiple peripherals including displays, USB devices, and network adapters.</p>

### Key Use Cases

- **Direct Device Power:** Direct connection to USB-C devices for development and operation
- **Hub/Dongle Power Delivery:** Powers USB-C hubs and dongles with sufficient headroom for multiple peripherals
- **Fast Charging:** Charges USB-C devices with intelligent power negotiation
- **Multi-Device Support:** Compatible with single-board computers, smartphones, tablets, laptops, and other USB-C devices

<div style="background-color: rgba(255, 193, 7, 0.2); border-left: 6px solid rgba(255, 152, 0, 1); margin: 20px 0; padding: 15px;">
  <strong>Important:</strong> When powering USB-C hubs or dongles with multiple high-power peripherals, connect this power supply to the hub's PD input port. The hub will distribute power to the connected device and peripherals simultaneously. Ensure the total power consumption does not exceed 45 W.
</div>

### Connection Method

<p style="text-align: justify;">For standalone device operation, connect the power supply's USB-C output directly to your device's USB-C port. For expanded I/O with USB-C hubs or dongles, connect the power supply to the hub's USB-C PD port, then connect the hub to your device.</p>

<div style="page-break-after: always;"></div>

## Technical Specifications

### Output Characteristics

#### Voltage Regulation

| **Output Voltage** | **Voltage Range** | **Regulation** |
|-------------------:|------------------:|----------------|
|              5.0 V |      4.6 - 5.25 V | ±5%            |
|              9.0 V |     8.55 - 9.45 V | ±5%            |
|             12.0 V |     11.4 - 12.6 V | ±5%            |
|             15.0 V |   14.25 - 15.75 V | ±5%            |
|             20.0 V |     19.0 - 21.0 V | ±5%            |

#### Ripple and Noise

| **Parameter**                | **Specification**                |
|------------------------------|----------------------------------|
| Ripple and Noise (all modes) | 150 mVp-p maximum (at full load) |
| Measurement Bandwidth        | 20 MHz                           |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Measurement Conditions:</strong> Ripple and noise measurements are performed with a 20 MHz bandwidth-limited oscilloscope, with the output terminated by a parallel combination of 0.1 μF ceramic capacitor and 10 μF electrolytic capacitor.
</div>

#### Dynamic Response

| **Parameter** | **Specification**                          |
|---------------|--------------------------------------------|
| Turn-on Delay | 3 seconds maximum @ 115 V AC, full load    |
| Hold-up Time  | 5 ms minimum @ 230 V AC, full load         |
| Rise Time     | 80 ms maximum (10% to 90% of rated output) |

### Efficiency

| **Output Mode** | **Average Efficiency** |
|-----------------|------------------------|
| 5.0 V / 3.0 A   | 81.39% minimum         |
| 9.0 V / 3.0 A   | 86.62% minimum         |
| 12.0 V / 3.0 A  | 87.40% minimum         |
| 15.0 V / 3.0 A  | 87.73% minimum         |
| 20.0 V / 2.25 A | 87.73% minimum         |

**No-Load Power Consumption:** ≤ 0.1 W @ 115-230 V AC

### Protection Features

| **Protection Type**         | **Specification**                                                  |
|-----------------------------|--------------------------------------------------------------------|
| Over Current Protection     | 105% - 150% of maximum load / auto-recovery hiccup mode            |
| Short Circuit Protection    | Output automatically shuts down / auto-recovery when fault removed |
| Over Voltage Protection     | Hiccup protection mode / auto-recovery when fault removed          |
| Over Temperature Protection | Thermal shutdown with auto-recovery                                |

<div style="page-break-after: always;"></div>

### Operating Conditions

| **Parameter**         | **Range**                     |
|-----------------------|-------------------------------|
| Operating Temperature | 0 °C - 35 °C                  |
| Storage Temperature   | -40 °C - 70 °C                |
| Operating Humidity    | 10% - 90% RH (non-condensing) |
| Storage Humidity      | 5% - 95% RH (non-condensing)  |
| Operating Altitude    | Up to 5000 m                  |
| Storage Altitude      | Up to 5000 m                  |

### Safety and EMC Specifications

#### Electrical Safety

| **Parameter**          | **Specification**                       |
|------------------------|-----------------------------------------|
| Dielectric Strength    | 3000 V AC @ 50 Hz, 5 mA max, 60 seconds |
| Production Hi-Pot Test | 3600 V AC @ 50 Hz, 5 mA max, 3 seconds  |
| Leakage Current        | 0.25 mA maximum @ 230 V AC / 50 Hz      |
| Insulation Resistance  | 10 MΩ minimum @ 500 V DC, 90% RH        |
| Protection Class       | Class II (double insulated)             |

#### EMI/EMC Compliance

| **Standard**        | **Compliance**                                  |
|---------------------|-------------------------------------------------|
| Conducted Emissions | EN55032, FCC Part 15, AS/NZS CISPR32            |
| Radiated Emissions  | EN55032, FCC Part 15                            |
| ESD Immunity        | EN 61000-4-2 (±4 kV contact, ±8 kV air)         |
| EFT/Burst Immunity  | EN 61000-4-4 (±1 kV)                            |
| Surge Immunity      | EN 61000-4-5 (±2 kV common, ±1 kV differential) |

<div style="page-break-after: always;"></div>

## Mechanical Information

### Dimensions

<p style="text-align: justify;">The power supply features a compact cubic form factor suitable for travel and portable use. The interchangeable plug design allows use in multiple regions without adapters as listed in [this section](#regional-plug-options).</p>

![Power Supply Dimensions](assets/mechanical_drawing_power_supply.png)

| **Configuration**           | **Dimensions (W × L × H)**   |
|-----------------------------|------------------------------|
| With US plug folded         | 64 × 64 × 30 mm              |
| With US plug unfolded       | 64 × 80.06 × 30 mm           |

### Package Contents

- 1× Arduino USB-C Power Supply (45W)
- 1× Interchangeable plug (region-specific: EU, UK, or US)

<div style="page-break-after: always;"></div>

## Environmental and Reliability

### Reliability Requirements

| **Parameter**         | **Specification**                                          |
|-----------------------|------------------------------------------------------------|
| MTBF                  | 30,000 hours minimum @ 25°C, 80% load, nominal input       |
| High Temperature Test | Normal operation @ 240 V AC, full load, 35°C ambient       |
| Salt Spray Test       | 24 hours @ 5% salt concentration, no corrosion on contacts |

### Mechanical Stress Tests

| **Test Type**      | **Specification**                                                                          |
|--------------------|--------------------------------------------------------------------------------------------|
| Vibration Test     | 10 - 300 Hz sweep, 1.0 G constant (3.5 mm displacement), 1 hour per axis (X, Y, Z)         |
| Vibration Criteria | No visible damage, normal operation after test                                             |
| Drop Test          | 6 faces, 1 meter height onto concrete surface                                              |
| Drop Criteria      | Plugs may bend, housing may scratch, but no structural damage. Normal operation after test |

### Environmental Compliance

| **Regulation**     |
|--------------------|
| RoHS               |
| REACH              |

<div style="page-break-after: always;"></div>

## Certifications

### Safety Certifications

The Arduino USB-C Power Supply holds the following safety certifications:

| **Certification** | **Region**     | **Standard**         |
|-------------------|----------------|----------------------|
| UL/CUL            | USA/Canada     | UL62368-1, CSA C22.2 |
| ETL               | USA            | UL62368              |
| TUV/GS            | Europe         | EN62368              |
| CE                | Europe         | EN62368              |
| UKCA              | United Kingdom | EN62368              |
| FCC               | USA            | Part 15 Class B      |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Note:</strong> All certifications are maintained and updated regularly. For the most current certification status, please contact Arduino support or refer to product documentation.
</div>

### Declaration of Conformity CE DoC (EU)

English: We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).

French: Nous déclarons sous notre seule responsabilité que les produits indiqués ci-dessus sont conformes aux exigences essentielles des directives de l'Union européenne mentionnées ci-après, et qu'ils remplissent à ce titre les conditions permettant la libre circulation sur les marchés de l'Union européenne (UE) et de l'Espace économique européen (EEE).

### Declaration of Conformity to EU RoHS & REACH

<p style="text-align: justify;">Arduino products are in compliance with Directive 2011/65/EU of the European Parliament and Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.</p>

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

Exemptions: No exemptions are claimed.

<p style="text-align: justify;">Arduino products are fully compliant with the related requirements of European Union Regulation (EC) 1907/2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907/2006/EC.</p>

### Conflict Minerals Declaration

<p style="text-align: justify;">As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.</p>

<div style="page-break-after: always;"></div>

## FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:

(1) This device may not cause harmful interference

(2) this device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment.

## Company Information

| Company name    | Arduino S.r.l.                             |
|-----------------|--------------------------------------------|
| Company address | Via Andrea Appiani 25, 20900 Monza (Italy) |

## Reference Documentation

| No. | Reference     | Link                                                       |
|:---:|---------------|------------------------------------------------------------|
|  1  | Arduino Store | [https://store.arduino.cc/](https://store.arduino.cc/)     |

## Document Revision History

|  **Date**  | **Revision** | **Changes**   |
|:----------:|:------------:|---------------|
| 27/03/2026 |      1       | First release |