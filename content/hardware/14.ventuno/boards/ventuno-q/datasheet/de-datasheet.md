---
identifier: ABX00181
title: Arduino® VENTUNO™ Q
type: maker
---

![](assets/featured.png)

# Deutsch

# Beschreibung

Der Arduino® VENTUNO™ Q ist ein leistungsstarker Edge-AI-Computer, der speziell für KI und Robotik der nächsten Generation entwickelt wurde. Durch die nahtlose Verbindung von Rechenleistung auf Industrie-Niveau mit Echtzeit-Ansteuerung bietet Ihnen der VENTUNO Q die Rechenleistung für den Einsatz komplexer KI-Modelle und die präzise Steuerung zur Beeinflussung der physischen Welt – und das alles über ein einziges, kompaktes Edge-Gerät.

Sein Herzstück bildet eine revolutionäre Dual-Brain-Architektur: Der robuste Qualcomm Dragonwing™ IQ8 (QCS8275) Mikroprozessor (MPU) liefert bis zu 40 Dense-TOPS an AI-Rechenleistung für fortschrittliche Bildverarbeitung und lokale LLMs unter einem vollständigen Ubuntu-Linux-Betriebssystem (Debian wird ebenfalls unterstützt), während der dedizierte STMicroelectronics STM32H5F5-Mikrocontroller (MCU), auf dem Arduino Core unter dem Zephyr-Betriebssystem läuft, die für komplexe Motorsteuerung und Robotik erforderliche Präzision bei geringer Latenz gewährleistet.

Mit VENTUNO Q bleiben Sie vernetzt und einsatzbereit. Es verfügt über integrierte Wi-Fi® 6 (Tri-Band)- und Bluetooth® 5.3-Konnektivität sowie eine umfassende Auswahl an integrierten Anschlüssen, darunter High-Speed-USB 3.0, HDMI, 2,5-Gb-Ethernet und einen M.2-Anschluss für erweiterbaren NVMe-Gen-4-Speicher. Das Board unterstützt nativ das umfangreiche Ökosystem der Arduino UNO Shields und Carrier sowie Raspberry Pi® HATs über einen 40-poligen Steckverbinder und Arduino Modulino®-Knoten über einen Qwiic-Anschluss.

# Anwendungsbereiche

Edge AI, lokale LLM/VLM, intelligente Smart Home-Systeme, Robotik, Bewegungssteuerung, intelligente Smart City, industrielle Bildverarbeitung, Bildung und Forschung

<div style="page-break-after: always;"></div>

# INHALT

## Anwendungsbeispiele

VENTUNO Q kombiniert einen AI-fähigen Linux-Prozessor mit einem Echtzeit-Mikrocontroller und bietet so das Beste aus leistungsstarker Datenverarbeitung und deterministischer Steuerung. Es wurde speziell für Maker und Entwickler konzipiert, die AI nutzen möchten, um die physische Welt direkt zu gestalten.

- **AI-Assistenten & Intelligentes Zuhause:** Entwickeln Sie Offline-Sprachassistenten, lokale agentenbasierte Hubs, berührungslose Kiosksysteme und Echtzeit-Sprachübersetzer.
- **Robotik & Bewegungssteuerung:** Autonome mobile Roboter (AMRs) mit Visual-SLAM, bildverarbeitungsgesteuerte Manipulatoren sowie Begleit- und Serviceroboter.
- **Intelligente Stadt & Industrielle Bildverarbeitung:** Edge-Verkehrsüberwachung, automatisierte Qualitätsprüfung an Fertigungsstraßen, proaktive Standortsicherheit und bildverarbeitungsbasierte Bestandsüberwachung.
- **Bildung & Forschung:** Fortgeschrittene AI-Lernkits, schnelle Forschungsprototypen, sprachbasierte Programmierassistenten und mobile Forschungsplattformen für die Manipulation.

<div style="page-break-after: always;"></div>

## Funktionen

### VENTUNO Q-Varianten

VENTUNO Q ist in einer Variante erhältlich:

- **ABX00181**: 16 GB LPDDR5-RAM, 64 GB eMMC-Speicher

### Übersicht über die allgemeinen technischen Daten

#### Prozessor & Speicher

![](assets/ABX00181_ic_overview.png)

| **Subsystem**  | **Details**                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------- |
| Haupt-MPU      | Qualcomm Dragonwing™ IQ8 (QCS8275)                                                           |
|                | CPU: Octa-Core Arm® Cortex®                                                                  |
|                | Adreno™ 623 GPU (3D-Grafik & OpenCL)                                                         |
|                | Adreno™ VPU 623 (Videoverarbeitung)                                                          |
|                | Hexagon™ Tensor AI-Prozessor (NPU): bis zu 40 Dense TOPS                                     |
|                | Qualcomm Spectra 692 ISP                                                                     |
|                | Ubuntu Linux-Betriebssystem (Debian wird ebenfalls unterstützt)                              |
| Echtzeit-MCU   | ST STM32H5F5 (MCU), Arm® Cortex®-M33 mit bis zu 250 MHz                                      |
|                | Arduino Core auf Zephyr OS                                                                   |
|                | 4 MB Flash, 1,5 MB RAM                                                                       |
| Systemspeicher | eMMC 64 GB für Betriebssystem/Daten                                                          |
|                | OSPI SAIL-Speicher (MX25UW25345GXDI00-TR) für MCU-Boot/gemeinsam genutzte Daten              |
|                | M.2-Anschluss (Key M 2230) für NVMe Gen 4-Speicher (PCIe x4 direkt vom SOM, nicht bootfähig) |
|                | 2 × 8 GB LPDDR5-RAM (insgesamt 16 GB)                                                        |

#### Konnektivität & Medien

![](assets/ABX00181_connector_overview.png)

| **Subsystem**       | **Details**                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Netzwerk & Drahtlos | Wi-Fi® 6 2,4/5/6 GHz (Tri-Band) mit 2 integrierten Antennen (NFA725B-Modul)                                        |
|                     | Bluetooth® 5.3 mit integrierter Antenne                                                                            |
|                     | 1× 2,5-Gbit-RJ45-Ethernet (QCA-8081 PHY)                                                                           |
| USB-Anschlüsse      | 1× USB-C-Anschluss mit Umschaltung zwischen Host- und Gerätefunktion, Stromversorgungsumschaltung und Videoausgang |
|                     | 2x USB 3.0 Typ A                                                                                                   |
|                     | 2x USB 3.0 am JOMEGA-Header                                                                                        |
| Video               | 1x HDMI-Ausgang über integrierte ADV7535 DSI-zu-HDMI-Brücke. HDMI und MIPI DSI nutzen                              |
|                     | dieselben DSI-Leitungen; wenn HDMI aktiv ist, wird MIPI DSI am JMEDIA-Anschluss ausgekuppelt                       |
|                     | Videoausgang (DP-Alt-Modus) über USB-C                                                                             |
| Kamera              | 3x MIPI-CSI-Anschlüsse auf dem Board (J3_1, J3_2, J3_3)                                                            |
|                     | 2x MIPI-CSI-Lanes ebenfalls am JMEDIA-Stecker verfügbar (mit den Onboard-Anschlüssen gemultiplext)                 |
|                     | Unterstützung für USB-Kameras über USB Typ A oder USB-C                                                            |
| Audio               | Audio-Codec: MAX98091ETM+T (Maxim)                                                                                 |
|                     | Auf JMISC: 1x LINE OUT mono, 1x SPEAKER OUT mono, 1x HEADPHONES OUT stereo, 1x MIC IN                              |
|                     | Auf JOMEGA: 1x MIC IN                                                                                              |
| CAN-Schnittstellen  | 1x CAN-FD mit PHY (ATA6563-GBQW1) an Schraubklemme, angesteuert durch MCU (STM32H5F5)                              |
|                     | Die CAN-H- und CAN-L-Leitungen sind TVS-geschützt (PJGBLC24C-AU_R1_000A1, bidirektional, 24 V, 350 W)              |
|                     | Integrierte geteilte Terminierung am Schraubklemmenblock des CAN-Busses (2 × 60,4 Ω + 100 nF)                      |
|                     | 3× CAN-FD (ohne PHY) am JOMEGA-Steckverbinder, über die MCU pin-gemultiplext                                       |
|                     | 1× CAN-FD (ohne PHY) an den UNO-Shield-Steckverbindern (D4/D5), über die MCU pin-gemultiplext                      |

>📝 **Hinweis:** Der CAN-Bus an der Schraubklemme verfügt über eine integrierte geteilte Terminierung (2 × 60,4 Ω + 100 nF). Befindet sich das Board nicht am Ende des Busses, sollte diese Terminierung bei der Auslegung der Netzwerktopologie berücksichtigt werden.

#### Erweiterungen & Steckleisten

| **Schnittstelle (Stecker)**      | **Details**                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| UNO-Shield-Steckleisten          | - Kompatibel mit Standard-Arduino-UNO-Shields (3,3-V-Logik)                                                                                            |
|                                  | - Die meisten digitalen Pins sind 5-V-tolerant. A0 und A1 auf JANALOG sind direkte ADC-Eingänge und nicht 5-V-tolerant                                 |
| Erweiterungssteckleiste (JOMEGA) | - Umfangreiche Erweiterungsmöglichkeiten, darunter USB 3.0, CAN-FD, JTAG, MIC IN, MPU-SPI                                                              |
| Carrier-Steckleisten             | - JMEDIA: MIPI-CSI0/CSI1-Kamerakanäle und MIPI-DSI-Displaykanäle mit 1,8 V                                                                             |
|                                  | - JMISC: Audio-Endpunkte, MPU-GPIO bei 1,8 V und MCU-Signale bei 3,3 V                                                                                 |
| Qwiic-Anschluss                  | - I2C (3,3 V), verbunden mit der MCU für sofortigen Plug-and-Play-Zugriff auf Modulino®-Knoten                                                         |
| JHAT-Anschluss                   | - Raspberry Pi®-kompatibler 40-poliger Steckverbinder (MPU-GPIO, über TXS0108ERKSR und TXS0104ERUTR auf 3,3 V pegelkonvertiert für HAT-Kompatibilität) |
| JCTL (MPU-Fern-Debugging)        | – 10-polige (2×5) Stiftleiste für MPU-Fern-Debugging, kompatibel mit [Arduino Bughopper](https://docs.arduino.cc/hardware/bughopper/)                  |

<div style="page-break-after: always;"></div>

## Nennwerte

### Eingangsleistung

| **Quelle**                 | **Spannungsbereich** | **Maximale Stromstärke** | **Anschluss**            |
| -------------------------- | -------------------: | -----------------------: | ------------------------ |
| USB-C PD                   |               9–20 V |               bis zu 3 A | USB-C-Anschluss          |
| Rundstecker (5,5 × 2,1 mm) |               7–24 V |               bis zu 5 A | 5,5 × 2,1 mm Rundstecker |
| Schraubklemme              |               7–24 V |              bis zu 10 A | Schraubklemme            |

![Eingangsversorgungsoptionen](assets/ABX00181_power_options.png)

Beide Eingangswege sind durch TVS-Schutzdioden (SMBJ24CA, 24 V bidirektional) geschützt und führen über unabhängige Leistungsschalter (KTS1900GXAA-TA + SQS414CENW-T1_GE3) zu einer Stufe zur Messung der Stromstärke (INA232AIDDFR). Zwei mehrphasige Buck-Wandler (MPQ4371GVE-1001-AECC901-Z) erzeugen die 3,3-V-Hauptspannungsschiene, während ein weiterer Buck-Wandler (MPQ4371GVE-1001-AECC901-Z) die 5-V-Spannungsschiene erzeugt. Der USB-C®-PD-Controller (CYPD6129-52LQXI) handelt Spannungsprofile von bis zu 20 V mit kompatiblen USB-C®-Stromversorgungen aus.

> 📝 **Hinweis zum Gleichstrom-Eingang und zur Leistungsauslegung:** Der Barrel-Stecker ist für eine Stromstärke von maximal 5 A ausgelegt. Die verfügbare Leistung hängt von der Eingangsspannung ab: Bei 7 V (5 A) beträgt die maximal lieferbare Leistung 35 W; bei 12 V sind es 60 W; bei 24 V beträgt sie 120 W. Im ungünstigsten Fall, wenn MPU, NPU und GPU gleichzeitig mit voller Leistung laufen, kann das SoM allein etwa 23–25 W aufnehmen. Das gesamte Board einschließlich des Ethernet-PHY, des Audio-Codecs, des USB-Hubs und anderer integrierter Schaltkreise verbraucht noch mehr, sodass bei 7 V nur noch wenig Spielraum bleibt, bevor die Grenze des Steckers erreicht wird.
>
> Wenn du das Board mit 7 V versorgst, musst du unbedingt den Spannungsverlust im Kabel berücksichtigen, da das Board an seinen Anschlüssen mindestens 7 V benötigt und sich bei einer Spannung unter 7 V nicht einschaltet.
>
> Die beiden USB-Typ-A-Anschlüsse können jeweils bis zu 5 V × 1,71 A = 8,55 W liefern, was zusammen eine zusätzliche Leistungsaufnahme von maximal ~17 W ergibt. Bei voller Leistung des Boards und maximaler Auslastung beider USB-A-Anschlüsse kann die Gesamtleistungsaufnahme fast 42 W erreichen, was die 35-W-Grenze der Gleichstrombuchse bei 7 V überschreitet und zu einer Beschädigung des Anschlusses führen kann.
>
> Die 3,3-V-Schiene für UNO-Shields, HATs und Qwiic (`+3V3_LIMITED`) ist auf 2,8 A begrenzt (maximal ~9,3 W). Die 5-V-Schiene für Shields und HATs (`+5V_LIMITED`) ist ebenfalls auf 2,8 A begrenzt (maximal ~14 W). Hinweis: Die 3,3-V- und 5-V-Versorgungsspannungen, die an die UNO-Carrier-Anschlüsse und an JOMEGA geliefert werden, **sind** nicht strombegrenzt.
>
> **Der Betrieb mit 12 V oder 24 V wird dringend empfohlen** für alle Einsatzszenarien, bei denen gleichzeitig AI-Inferenz, USB-Peripheriegeräte und angeschlossene Shields oder HATs zum Einsatz kommen.
>
> Bei hoher Auslastung durch AI-Inferenz, USB-Peripheriegeräte oder erweiterte Anwendungen wird ein Netzteil mit einer Nennleistung von **60 W oder mehr** für alle Stromquellen empfohlen, um sicherzustellen, dass der Betrieb auch bei möglichen Verbrauchsspitzen stabil bleibt. Bei Verwendung der **Hohlsteckerbuchse** (5,5 × 2,1 mm, max. 5 A) wird beispielsweise eine Stromversorgung mit **12 V / 5 A oder 24 V / 3 A** empfohlen.

### Empfohlene Betriebsbedingungen

| **Parameter**                                | **Symbol**       | **Minimum** | **Typisch** | **Maximum** | **Einheit** |
| -------------------------------------------- | ---------------- | :---------: | :---------: | :---------: | :---------: |
| USB-C-PD-Eingang                             | V<sub>USBC</sub> |      9      |      -      |    20,0     |      V      |
| Gleichstromeingang (Buchse/Schraubanschluss) | V<sub>IN</sub>   |     7,0     |      -      |    24,0     |      V      |
| 5,0-V-Schiene (Ausgang)                      | V<sub>+5V</sub>  |    4,75     |     5,0     |    5,25     |      V      |
| 3,3-V-Schiene (Ausgang)                      | V<sub>3P3</sub>  |    3,14     |     3,3     |    3,47     |      V      |
| Betriebstemperatur                           | T<sub>OP</sub>   |     -10     |      -      |     60      |     °C      |

>📝 **Hinweis:** Der USB-C®-PD-Controller unterstützt mehrere Spannungsprofile (9 V, 15 V, 20 V), wenn er an ein PD-fähiges Netzteil angeschlossen ist.

### Integrierte Spannungsschienen

| **Spannung** | **Spannungsschiene**  | **Herkunft/Regler**                                                                                    |
| :----------: | --------------------- | ------------------------------------------------------------------------------------------------------ |
|    7–24 V    | V<sub>IN</sub>        | Eingang über Buchse/Schraubklemme (TVS-geschützt, SMBJ24CA)                                            |
|    5,0 V     | +5 V                  | MPQ4371GVE-Buck-Wandler                                                                                |
|    3,3 V     | +3,3 V                | 2x MPQ4371GVE-Abwärtswandler                                                                           |
|    1,8 V     | SOM_VREG_MDPX3_1P8    | 1,8-V-Versorgungsspannung der SOM-Hauptanwendungsdomäne (für den Anwender über JMISC, JCTL zugänglich) |
|    1,8 V     | SOM_VREG_S5S_SPX3_1P8 | Ausschließlich für den SOM-Sicherheitssubsystem-Bereich (RTSS), nicht für den allgemeinen Gebrauch     |
|    1,8 V     | +1V8                  | MPQ2179GQHE-Abwärtswandler (für die integrierten Schaltkreise QCA8081, ADV7535, MAX98091)              |
|    1,28 V    | +1,28 V               | MP20312GTF-LDO (für den Audio-Codec MAX98091)                                                          |
|    1,1 V     | +1,01 V               | MPQ2179GQHE-Abwärtswandler (für die integrierten ICs TUSB7340RKMR, QCA8081 und PI7C9X2G304EV)          |

>📝 **Hinweis:** Mit dem Board verfügt man über drei unabhängige 1,8-V-Versorgungsspannungen. `SOM_VREG_MDPX3_1P8` ist die Versorgungsspannung der Hauptanwendungsdomäne des QCS8275-SoM und dient als empfohlene Referenz für alle für den Anwender zugänglichen 1,8-V-Schnittstellen, einschließlich JMISC und JCTL. `SOM_VREG_S5S_SPX3_1P8` ist die Spannungsversorgung der Sicherheits-Subsystem-Domäne (RTSS) des SoM und sollte nicht als allgemeine Versorgungsspannung oder Referenzspannung verwendet werden. `+1V8` ist die auf Board-Ebene vorhandene 1,8-V-Versorgungsspannung, die vom MPQ2179GQHE-Buck-Wandler erzeugt wird und den QCA-8081-Ethernet-PHY, die ADV7535-Display-Brücke sowie den MAX98091-Audio-Codec versorgt.

>📝 **Hinweis:** Unabhängig von den oben genannten Spannungsschienen akzeptiert der JMISC-Pin 59 eine RTC-Pufferbatterie mit bis zu 3,3 V, um die Echtzeituhren (RTC) des SOM und der MCU aufrechtzuerhalten, wenn das Board ansonsten nicht mit Strom versorgt wird. `SOM_VCOIN` (SOM-RTC) und `VBAT` (MCU-RTC) sind zwei Eingänge für RTC-Pufferbatterien, die physikalisch an diesem einzelnen Pin miteinander verbunden sind und nicht über eine gemeinsame Versorgungsschiene. Jeder ist über einen eigenen 0-Ω-Widerstand mit einem gemeinsamen Knoten verbunden, der durch eine bidirektionale TVS-Diode (Vr = 5,5 V) mit Bezug auf Masse geschützt ist. Die zu erwartende Stromstärke ist sehr gering, und dieser Pin liefert keine Stromversorgung, um den Rest des Boards im Betrieb zu halten.

### Typische Leistungsaufnahme

Die folgenden Messungen basieren auf einer Umgebungstemperatur von 24,4 °C und wurden mit einem Leistungsanalysator für drei Stromversorgungsmethoden durchgeführt: 12 V DC, 24 V DC und USB-C® PD bei 20 V. „Blink“ auf der MCU, „Hello World“ auf der MPU sowie „Edge AI Assistant“ und „Detect Objects“ auf der Smartphone-Kamera sind als integrierte Beispiele im Arduino App Lab verfügbar. Das Beispiel „Smart Mirror“ basiert auf einem speziellen Hinweis.

#### Typische Leistungsaufnahme – 12 V DC

| **Szenario**                               | **Durchschnittliche Leistung** | **Minimale Leistung** | **Maximale Leistung** |
| ------------------------------------------ | -----------------------------: | --------------------: | --------------------: |
| Hochfahren                                 |                         7,07 W |                     – |                17,9 W |
| Blinken auf der MCU                        |                         7,42 W |                5,30 W |                12,6 W |
| „Hello World“ auf der MPU                  |                         7,52 W |                5,32 W |                13,3 W |
| „Edge AI Assistant“                        |                         13,5 W |                6,13 W |                24,6 W |
| Beispiel „Smart Mirror“¹                   |                         14,7 W |                7,65 W |                33,0 W |
| Objekterkennung über die Smartphone-Kamera |                         9,63 W |                5,80 W |                21,2 W |

#### Typische Leistungsaufnahme – 24 V DC

| **Szenario**                           | **Durchschnittliche Leistung** | **Minimale Leistung** | **Maximale Leistung** |
| -------------------------------------- | -----------------------------: | --------------------: | --------------------: |
| Hochfahren                             |                         9,71 W |                     – |                23,7 W |
| Blinken auf der MCU                    |                         10,6 W |                7,04 W |                18,9 W |
| „Hello World“ auf der MPU              |                         10,8 W |                7,09 W |                18,3 W |
| Edge-AI-Assistent                      |                         15,5 W |                7,44 W |                28,8 W |
| Beispiel „Smart Mirror“¹               |                         17,3 W |                8,47 W |                36,6 W |
| Objekterkennung über Smartphone-Kamera |                         11,5 W |                7,88 W |                24,7 W |

#### Typischer Stromverbrauch – USB-C® PD (20 V)

| **Szenario**                           | **Durchschnittliche Leistung** | **Minimale Leistung** | **Maximale Leistung** |
| -------------------------------------- | -----------------------------: | --------------------: | --------------------: |
| Hochfahren                             |                         6,56 W |                     – |                20,2 W |
| Blinken auf der MCU                    |                         7,84 W |                6,33 W |                16,1 W |
| „Hello World“ auf der MPU              |                         9,68 W |                6,42 W |                16,1 W |
| Edge-AI-Assistent                      |                         15,3 W |                6,61 W |                25,6 W |
| Beispiel „Smart Mirror“¹               |                         15,1 W |                8,05 W |                34,2 W |
| Objekterkennung über Smartphone-Kamera |                         11,3 W |                7,85 W |                23,1 W |

¹ Konfiguration „Smart Mirror“: Logitech BRIO 4K-USB-Kamera, USB-Headset (Mikrofon und Lautsprecher) sowie ein angeschlossenes HDMI-Display.

>📝 **Hinweis:** Die Messungen wurden zur Orientierung mit einem Otii Ace Pro-Leistungsanalysator durchgeführt. Der höchste über alle Szenarien und Eingangsquellen hinweg gemessene Spitzenwert betrug 36,6 W (Beispiel „Smart Mirror“ bei 24 V Gleichstrom) und lag damit innerhalb der oben genannten Empfehlung für ein Netzteil mit mindestens 60 W.

<div style="page-break-after: always;"></div>

## Funktionsübersicht

### Pinbelegung

![](assets/ABX00181_pinout.png)

### Blockdiagramm

![Vollständige Übersicht über das Blockdiagramm](assets/ABX00181_block_diagram.png)

![Blockschaltbild (Seite 1/2)](assets/ABX00181_block_diagram_pg1.png)

![Blockschaltbild (Seite 2/2)](assets/ABX00181_block_diagram_pg2.png)

### Stromversorgung

VENTUNO Q unterstützt zwei unabhängige Stromversorgungswege: einen USB-C®-Anschluss mit Power Delivery (PD)-Aushandlung bis zu 20 V sowie einen 7–24-V-Gleichstromeingang über die 5,5 × 2,1-mm-Hohlsteckerbuchse oder die Schraubklemme. Beide Pfade sind durch bidirektionale 24-V-TVS geschützt und werden über ein Strom-ODER aus unabhängigen, gegen Verpolung und Stromstärke geschützten Leistungsschaltern (KTS1900 + 2x NMOS) geleitet, bevor sie die Abwärtswandler erreichen.

Ein IC zur Messung der Stromstärke (INA232AIDDFR) überwacht die Gesamtstromstärke über den aktiven Pfad. Zwei mehrphasige Abwärtswandler (MPQ4371GVE-1001-AECC901-Z) erzeugen die Hauptspannungsschiene „+3,3 V“, die das SOM (QCS8275) und die 3,3-V-Peripheriegeräte mit dem Board versorgt. Ein dritter MPQ4371GVE-Abwärtswandler erzeugt die „+5 V“-Spannungsschiene.

Ein MPQ2179GQHE-Buck-Wandler erzeugt die `+1V8`-Versorgungsspannung und versorgt damit den QCA-8081-Ethernet-PHY, die ADV7535-Display-Brücke und den MAX98091-Audio-Codec. Ein MPQ2179GQHE-Abwärtswandler erzeugt die `+1V1`-Spannungsschiene und versorgt den TUSB7340RKMR sowie den QCA-8081 und den PI7C9X2G304EV-PCIe-Switch.

Das SOM stellt die `MDPX3_1P8` (1,8 V)-Versorgungsspannung für den Hauptanwendungsbereich über seinen internen PMIC (`SOM_VREG_MDPX3_1P8`) bereit, auf den der Benutzer über JMISC und JCTL zugreifen kann. Die separate Versorgungsspannung `SOM_VREG_S5S_SPX3_1P8` ist für das Echtzeit-Sicherheitssubsystem (RTSS) vorgesehen. Sie sollte nicht als allgemeine Referenzspannung verwendet werden. Ein MP20312GTF-LDO erzeugt die `+1,28 V`-Versorgungsspannung für den MAX98091-Audio-Codec.

Spezielle MP5077GG-Z-Lastschalter schalten den M.2-NVMe-Steckplatz, die `+3V3_LIMITED`-Spannungsschiene (für UNO-Shields, HATs und Qwiic) sowie die `+5V_LIMITED`-Spannungsschiene (für Shields und HATs) unabhängig voneinander frei. Die VBUS-Versorgungsspannung für jeden USB-Typ-A-Anschluss wird durch den TUSB7340RKMR freigeschaltet und geschützt. Alle anderen peripheren Lastschalter werden über GPIO-gesteuerte Freigabeleitungen des SOM gesteuert, wodurch die MPU nicht genutzte Subsysteme stromlos schalten kann.

![Vollständige Übersicht über den Stromversorgungsbaum des Arduino VENTUNO Q](assets/ABX00181_power_tree.png)

![Stromversorgungsbaum des Arduino VENTUNO Q (Seite 1/3)](assets/ABX00181_power_tree_pg1.png)

![Stromversorgungsbaum des Arduino VENTUNO Q (Seite 2/3)](assets/ABX00181_power_tree_pg2.png)

![Arduino VENTUNO Q-Stromversorgungsbaum (Seite 3/3)](assets/ABX00181_power_tree_pg3.png)

<div style="page-break-after: always;"></div>

## Benutzeroberfläche & Anzeigen

| **Anzeige**  | **Typ**                           | **Steuergerät**                             | **Hinweise**                                             |
| ------------ | --------------------------------- | ------------------------------------------- | -------------------------------------------------------- |
| LED-Matrix   | 104 blaue LEDs (LTST-C191TBKT-5A) | MCU über GPIO                               | Programmierbare Anzeigematrix                            |
| 4x RGB-LEDs  | LTST-C28NBEGK-2A                  | MCU über GPIO                               | Vom Benutzer adressierbare Statusanzeigen                |
| Betriebs-LED | Grün (LTST-C190KGKT)              | Hardware (+3V3-Schiene)                     | Zeigt an, dass die +3V3-Schiene aktiv ist                |
| Fehler-LED   | Rot (XHY-STB0603SR)               | USB-C®-PD-Controller (CYPD6129, GPIO9/P4.1) | Zeigt einen vom PD-Controller erkannten Fehlerzustand an |

- **4× RGB-LEDs:** Vier dreifarbige LEDs, die vom Mikrocontroller (MCU) STM32H5F5 über 12 einzelne GPIO-Pins (3 pro LED) angesteuert werden. Sie sind vom Benutzer adressierbar und können zur Anzeige des Anwendungsstatus, des Verbindungsstatus oder benutzerdefinierter Ereignisse innerhalb eines Arduino-Sketches verwendet werden.

| **Bezeichnung** | **RGB-LED** | **Rot** | **Grün** | **Blau** |
| --------------- | ----------- | ------- | -------- | -------- |
| DL1_1           | RGB-LED 1   | PG3     | PG6      | PK2      |
| DL1_2           | RGB-LED 2   | PG4     | PD10     | PK1      |
| DL1_3           | RGB-LED 3   | PD11    | PG5      | PK0      |
| DL1_4           | RGB-LED 4   | PG2     | PG8      | PC6      |

![](assets/ABX00181_rgb_led.png)

>📝 Die RGB-LEDs sind aktiv-niedrig und leuchten auf, wenn sie auf den Logikwert `0` gesetzt werden.

- **LED-Matrix:** Eine 8×13-Monochrom-LED-Matrix in Blau (104 Pixel), die von der STM32H5F5-MCU angesteuert wird. Sie zeigt während des Linux-Startvorgangs etwa 20–30 Sekunden lang die Boot-Animation an. Ein Zugriff auf die Matrix vor Abschluss des Startvorgangs kann den Betrieb der MCU beeinträchtigen.

>📝 **Hinweis:** Die Boot-Animation wird nur abgespielt, wenn der MCU-Bootloader geladen ist und ein gültiger Sketch ausgeführt wird. Sollte sie nicht erscheinen, entnehmen Sie bitte weitere Details dem [VENTUNO Q-Benutzerhandbuch](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

![](assets/ABX00181_matrix.png)

- **Betriebs-LED:** Grüne LED (LTST-C190KGKT), die an die `+3V3`-Spannungsschiene angeschlossen ist. Sie leuchtet, sobald das Board mit Strom versorgt wird.

- **Fehler-LED:** Rote Anzeige, die vom USB-C®-PD-Controller (CYPD6129, GPIO9/P4.1) angesteuert wird. Sie signalisiert einen vom PD-Controller erkannten Fehlerzustand.

![](assets/ABX00181_status_led.png)

## MPU und MCU

Eine MPU (Mikroprozessoreinheit) ist ein leistungsstarker Anwendungsprozessor, der für den Betrieb eines vollständigen Betriebssystems und komplexer Software ausgelegt ist. Eine MCU (Mikrocontroller-Einheit) ist ein kleiner, energieeffizienter Controller, der für eine schnelle und präzise Zeitsteuerung von Ein- und Ausgängen sowie für Steuerungsaufgaben konzipiert ist. VENTUNO Q kombiniert beides, um Rechenleistung auf Betriebssystemebene mit reaktionsschneller, zeitkritischer Steuerung auf einem einzigen Board zu vereinen und über „Bridge“ zu kommunizieren – eine RPC-Schicht, die auf beiden Seiten implementiert ist.

### Anwendungsprozessor (MPU)

Der Qualcomm® Dragonwing™ IQ8 (QCS8275) ist ein Octa-Core-Arm®-Cortex®-Prozessor, auf dem das Betriebssystem Ubuntu Linux läuft (Debian wird ebenfalls unterstützt). Seine E/A-Schnittstellen arbeiten mit 1,8 V und er bewältigt Hochgeschwindigkeits-Medienschnittstellen sowie AI-Inferenz.

- Spannungsbereich: 1,8 V für MPU (SoC)-GPIO und Hochgeschwindigkeitsschnittstellen.
- Steuert JMEDIA: MIPI-CSI-Kamerakanäle und MIPI-DSI-Displaykanäle.
- Steuert 1,8-V-MPU-GPIO-Pins und Audio-Endpunkte an den Carrier-Headern (JMEDIA, JMISC).
- USB-C: Die Rollenumschaltung wird über den PD-Controller CYPD6129 verwaltet, der die PD-Verhandlung eigenständig durchführt (unterstützt Profile bis zu 20 V).
- DisplayPort-Ausgang über USB-eDP-MUX (TMUXHS4446RETT) am USB-C-Anschluss.
- Betreibt die Hexagon™-NPU (bis zu 40 Dense-TOPS) und die Adreno™ 623-GPU für Edge-AI- und Grafik-Workloads.

### Echtzeit-Mikrocontroller (MCU)

Der STMicroelectronics® STM32H5F5 ist ein Arm® Cortex®-M33, auf dem der Arduino Core unter dem Zephyr-Betriebssystem mit 250 MHz läuft. Er bietet schnelle, deterministische Zeitsteuerung für Robotik, Motorsteuerung und allgemeine E/A-Anwendungen.

- Spannungsbereich: 3,3 V für GPIO- und analoge Schnittstellen.
- Verwaltet ADC, PWM, LED-Matrix, RGB-LEDs und Timer.
- Verarbeitet 3,3-V-Anschlüsse: JDIGITAL, JANALOG und JSPI.
- Steuert alle CAN-FD-Schnittstellen: PHY an der Schraubklemme und No-PHY-Ports an den JOMEGA- und UNO-Shield-Anschlüssen.

JMISC verwaltet beide Domänen: 1,8-V-MPU-Leitungen liegen neben 3,3-V-MCU-Signalen (PSSI, I²C, GPIO) und analogem Audio. Überprüfen Sie stets die Spannungspegel, wenn Sie Carrier oder externe Logik an JMISC anschließen.

>📝 **Hinweis zu VDDIO2:** Der STM32H5F5 verfügt über eine sekundäre I/O-Spannungsdomäne (VDDIO2), die über `SOM_VREG_MDPX3_1P8` (1,8 V) mit Spannung versorgt wird. Dies ermöglicht es bestimmten MCU-Pins, direkt mit der MPU bei 1,8 V zu kommunizieren, ohne dass externe Pegelwandler erforderlich sind. Die folgenden Schnittstellen arbeiten in der VDDIO2-Domäne:
>
>- **MCU I2C1** wird für die direkte Kommunikation zwischen MCU und MPU verwendet
>- **Die MCU-GPIOs PG9, PG10, PG11, PG12, PG13 und PG14** kommunizieren direkt mit der MPU bei 1,8 V
>
> Legen Sie an diesen Pins keine 3,3-V-Logik an. Alle anderen MCU-GPIO-Signale arbeiten mit 3,3 V im Standard-VDDIO-Bereich.

>⚠️ **Warnung zum Spannungspegel:** MPU-GPIO-Signale arbeiten mit 1,8 V, während MCU-GPIO-Signale mit 3,3 V arbeiten. Stellen Sie sicher, dass alle externen Anschlüsse an den Erweiterungssteckleisten mit dem Spannungspegel der jeweiligen Prozessordomäne kompatibel sind, um Hardwareschäden zu vermeiden.

## Kommunikation zwischen den Prozessoren

Der Qualcomm® Dragonwing™ IQ8 (QCS8275) (MPU) und der STM32H5F5 (MCU) kommunizieren über die Arduino-Bridge, eine softwarebasierte Remote-Procedure-Call-Schicht (RPC), die sowohl auf der Linux- als auch auf der MCU-Seite implementiert ist. Die Bridge stellt eine serviceorientierte API bereit, die es jedem Prozessor ermöglicht, Dienste für den anderen Prozessor bereitzustellen, und gleichzeitig einseitige Benachrichtigungen für asynchrone Ereignisse unterstützt. Sie verwaltet das Nachrichten-Routing zwischen den Prozessoren und unterstützt mehrere physikalische Transportprotokolle.

Über ihre API ermöglicht die Bridge typsichere Funktionsaufrufe, sodass Mikrocontroller-Sketches Linux-Dienste aufrufen und strukturierte Antworten empfangen oder Daten über Benachrichtigungen übermitteln können.

Die physische Transportschicht zwischen den beiden Prozessoren umfasst die folgenden Schnittstellen:

| **Schnittstelle** | **Richtung**      | **Zweck**                                                |
| ----------------- | ----------------- | -------------------------------------------------------- |
| USB 2.0           | SoC -> MCU (Host) | Datentransport mit hoher Bandbreite                      |
| SWD               | SoC -> MCU        | Debug-Schnittstelle (Pegelumsetzung von 1,8 V auf 3,3 V) |

Falls für einen Carrier-Board oder externe Logik eine Hardware-Anzeige erforderlich ist, kann die Firmware einen 1,8-V-MPU-GPIO auf JMISC oder einen verfügbaren JCTL-GPIO als „Ready“- oder „Wake“-Ausgang zuweisen. Dieses Signal kann über eine pegelkompatible Schaltung, wie beispielsweise einen Pegelumsetzer oder eine Open-Drain-Konfiguration mit einem Pull-up-Widerstand, an einem MCU-GPIO empfangen werden.

>📝 MPU-GPIO-Signale arbeiten im Niederspannungsbereich des Anwendungsprozessors (1,8 V). Stellen Sie sicher, dass jede Verbindung zum Mikrocontroller mit dessen E/A-Spannungsschiene (3,3 V) pegelkompatibel ist. Verwenden Sie beispielsweise einen Pegelumsetzer oder eine Open-Drain-Konfiguration mit einem Pull-up-Widerstand zur E/A-Schiene des Mikrocontrollers.

<div style="page-break-after: always;"></div>

## Hardwarebeschleunigung

VENTUNO Q bietet Hardwarebeschleunigung für Edge-AI, 3D-Grafik sowie Video-Kodierung und -Dekodierung durch den integrierten Hexagon™ Tensor AI-Prozessor (NPU), die Adreno™ 623 GPU und die Adreno™ VPU 623.

### AI-Beschleunigung (NPU)

Der integrierte Hexagon™ Tensor-AI-Prozessor liefert bis zu 40 „dense TOPS“ (Tera Operations Per Second) an Rechenleistung für neuronale Netze. Damit kann VENTUNO Q lokale LLMs (Large Language Models), VLMs (Vision Language Models) und komplexe Computer-Vision-Pipelines offline ausführen.

Die NPU ist in den Qualcomm AI Stack integriert und wird nativ im Arduino App Lab unterstützt. Entwickler können Modelle bereitstellen, die über **TensorFlow Lite, ONNX Runtime und PyTorch** optimiert wurden. VENTUNO Q bietet zudem eine direkte Integration mit **Edge Impulse Studio** für das schnelle Training und die Bereitstellung benutzerdefinierter Edge-AI-Modelle ohne das Schreiben von Boilerplate-Programmen.

| **Komponente**          | **Spezifikation**                                       |
| ----------------------- | ------------------------------------------------------- |
| Prozessor               | Hexagon™ Tensor AI-Prozessor                            |
| Spitzenleistung         | Bis zu 40 Dense TOPS                                    |
| Architektur             | Hexagon-DSP + vier HVX- + zwei HMX-Coprozessoren        |
| Unterstützte Frameworks | TensorFlow Lite, ONNX Runtime, PyTorch                  |
| Integration             | Qualcomm AI Stack, Arduino App Lab, Edge Impulse Studio |

### Grafikbeschleunigung (GPU)

Die Adreno™ 623-GPU bietet auf dem QCS8275-SoM hardwarebeschleunigte 3D-Grafik und allgemeine Rechenleistung (GPGPU). Unter Qualcomm Linux erfolgt die GPU-Beschleunigung über den proprietären Adreno-Treiberstack von Qualcomm mittels des KGSL-Kernel-Treibers.

Die vollständigen GPU-Hardware-Spezifikationen finden Sie im [QCS8275-Datenblatt (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html) sowie im [Qualcomm Linux Graphics Guide](https://docs.qualcomm.com/doc/80-70018-19/topic/).

>📝 **Hinweis:** Die Adreno-Treiberbibliotheken und Firmware-Dateien befinden sich auf dem Gerät im Verzeichnis `/lib/firmware/`. Möglicherweise sind nicht alle in der QCS8275-Dokumentation aufgeführten GPU-Funktionen in der mit VENTUNO Q ausgelieferten Software verfügbar. Die aktuelle Liste der unterstützten Funktionen finden Sie in der [VENTUNO Q-Dokumentation](https://docs.arduino.cc/hardware/ventuno-q/).

### Videobeschleunigung (VPU)

Die Adreno™ VPU 623 bietet hardwarebeschleunigte Videoverarbeitung auf dem QCS8275-SoM. Die unterstützten Codecs, Auflösungen und Integrationsdetails hängen vom mit dem Board gelieferten Software-Stack ab. Die vollständigen Hardware-Spezifikationen finden Sie im [QCS8275-Datenblatt (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html).

>📝 **Hinweis:** Möglicherweise sind nicht alle in der QCS8275-Dokumentation aufgeführten Codecs oder Frameworks in der mit VENTUNO Q ausgelieferten Software verfügbar. Die aktuelle Liste der unterstützten Funktionen finden Sie in der [VENTUNO Q-Dokumentation](https://docs.arduino.cc/hardware/ventuno-q/).

>📝 **Hinweis:** Die Qualcomm-spezifischen GStreamer-Plugins (`gstreamer1.0-plugins-qcom`) sind standardmäßig nicht im mit VENTUNO Q ausgelieferten Ubuntu-Image enthalten. Sie können manuell installiert werden, wenn eine hardwarebeschleunigte Kameraaufnahme oder Videopipelines benötigt werden. Einzelheiten zur Konfiguration finden Sie im [VENTUNO Q-Benutzerhandbuch](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

<div style="page-break-after: always;"></div>

## Peripheriegeräte & Anschlüsse

VENTUNO Q stellt seine Dual-Brain-Architektur über einen umfassenden Satz an Anschlüssen und Steckverbindern zur Verfügung. MCU-gesteuerte Anschlüsse arbeiten mit einer Logikspannung von **3,3 V**, während MPU-gesteuerte Anschlüsse mit **1,8 V** betrieben werden. Überprüfen Sie stets den Spannungsbereich eines jeden Anschlusses, bevor Sie externe Peripheriegeräte anschließen, um Hardwareschäden zu vermeiden.

### JANALOG

Der JANALOG-Steckverbinder bietet analoge Eingänge, Versorgungsspannungen und MCU-Steuersignale. Er ist kompatibel mit dem Standard-Layout des analogen Steckverbinders des Arduino UNO. Analoge Eingänge beziehen sich auf `VREF+` auf der 3,3-V-Versorgungsspannung und sollten `VDD + 0,3 V` (~3,6 V) nicht überschreiten. **Legen Sie keine 5 V an analoge Pins an**. `IOREF` ist ein 3,3-V-Referenzausgang; bitte leiten Sie daher keine Stromrückführung über diesen Pin.

| **Pin** | **Bezeichnung** | **Netz**              | **Domäne**      | **MCU-Pin** | **Hinweise**                             |
| ------: | --------------- | --------------------- | --------------- | ----------- | ---------------------------------------- |
|       1 | NC              | JANALOG_BOOT_MCU_3V3  | 3,3 V MCU       | BOOT0       | MCU-Bootstrap                            |
|       2 | IOREF           | +3V3_LIMITED          | Stromversorgung | -           | I/O-Spannungsreferenzausgang             |
|       3 | RESET           | JANALOG_RESET_MCU_3V3 | 3,3 V MCU       | NRST        | MCU-Reset                                |
|       4 | +3V3 OUT        | +3V3_LIMITED          | Stromversorgung | -           | 3,3-V-Versorgungsausgang                 |
|       5 | +5V USB         | +5V_LIMITED           | Stromversorgung | -           | 5-V-Versorgungsausgang (USB-begrenzt)    |
|       6 | GND             | GND                   | Stromversorgung | -           | Masse                                    |
|       7 | GND             | GND                   | Stromversorgung | -           | Masse                                    |
|       8 | VIN             | 7–24 V                | Stromversorgung | -           | Gleichstromeingang (nur Stromversorgung) |
|       9 | A0              | JANALOG_A0_MCU_3V3    | Analog          | PA4         | ADC-Eingang, nicht 5-V-tolerant          |
|      10 | A1              | JANALOG_A1_MCU_3V3    | Analog          | PA5         | ADC-Eingang, nicht 5-V-tolerant          |
|      11 | A2              | JANALOG_A2_MCU_3V3    | Analog          | PE12        | ADC-Eingang / SPI4_SCK                   |
|      12 | A3              | JANALOG_A3_MCU_3V3    | Analog          | PE13        | ADC-Eingang / SPI4_MISO                  |
|      13 | A4              | JANALOG_A4_MCU_3V3    | Analog          | PE14        | ADC-Eingang / SPI4_MOSI                  |
|      14 | A5              | JANALOG_A5_MCU_3V3    | Analog          | PE15        | ADC-Eingang                              |

>📝 **Hinweis:** A0 und A1 sind direkte ADC-Eingänge der MCU und nicht 5-V-tolerant. Der gültige Eingangsbereich liegt zwischen 0 V und `VREF+` (~3,3 V). Der VIN-Pin an Pin 8 dient ausschließlich der Stromversorgung und sollte nicht als GPIO verwendet werden. Der VIN-Pin ist durch eine 1,1-A-PTC-Sicherung geschützt, die die Leistung bei 24 V auf ca. 26 W begrenzt. Die Stromversorgung des Boards über diesen Pin wird unter Volllast nicht empfohlen. Er eignet sich besser zur Entnahme von Strom für die Versorgung eines Shields oder eines Peripheriegeräts als zur Stromversorgung des Boards.

>📝 **Hinweis:** A4 (PE14) und A5 (PE15) sind ausschließlich analoge und SPI-fähige Pins und verfügen über kein Hardware-I2C-Peripheriegerät. Shields, die I2C an A4 und A5 benötigen, erfordern Software-I2C (Bit-Banging). Hardware-I2C ist an den JDIGITAL-Pins 17 (SDA, PH12) und 18 (SCL, PH11) verfügbar.

### JDIGITAL

Der JDIGITAL-Steckverbinder stellt digitale I/O-, UART-, SPI-, I2C- und PWM-Signale bereit, die von der MCU mit 3,3-V-Logik angesteuert werden. Er ist kompatibel mit dem Standard-Layout des digitalen Steckverbinders des Arduino UNO.

| **Pin** | **Bezeichnung** | **Net**               | **Domäne**      | **MCU-Pin** | **Hinweise**              |
| ------: | --------------- | --------------------- | --------------- | ----------- | ------------------------- |
|       1 | D0 / RX         | JDIGITAL_MCU_UART_3V3 | 3,3 V MCU       | PB11        | UART RX                   |
|       2 | D1 / TX         | JDIGITAL_MCU_UART_3V3 | 3,3 V MCU       | PB10        | UART TX                   |
|       3 | D2              | JDIGITAL_D2_MCU_3V3   | 3,3 V MCU       | PB0         | GPIO                      |
|       4 | D3              | JDIGITAL_D3_MCU_3V3   | 3,3 V MCU       | PB1         | GPIO / PWM                |
|       5 | D4              | JDIGITAL_D4_MCU_3V3   | 3,3-V-MCU       | PB6         | GPIO / FDCAN2_TX          |
|       6 | D5              | JDIGITAL_D5_MCU_3V3   | 3,3-V-MCU       | PB5         | GPIO / PWM / FDCAN2_RX    |
|       7 | D6              | JDIGITAL_D6_MCU_3V3   | 3,3-V-MCU       | PB2         | GPIO / PWM                |
|       8 | D7              | JDIGITAL_D7_MCU_3V3   | 3,3 V MCU       | PB3         | GPIO                      |
|       9 | D8              | JDIGITAL_D8_MCU_3V3   | 3,3 V MCU       | PB4         | GPIO                      |
|      10 | D9              | JDIGITAL_D9_MCU_3V3   | 3,3 V MCU       | PB7         | GPIO / PWM                |
|      11 | D10 / CS        | JDIGITAL_MCU_SPI_3V3  | 3,3-V-MCU       | PB12        | SPI-Chip-Select           |
|      12 | D11 / MOSI      | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU       | PB15        | SPI MOSI / PWM            |
|      13 | D12 / MISO      | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU       | PB14        | SPI MISO                  |
|      14 | D13 / SCK       | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU       | PB13        | SPI-Takt                  |
|      15 | GND             | GND                   | Stromversorgung | -           | Masse                     |
|      16 | AREF            | JDIGITAL_AREF_MCU_3V3 | Analog          | -           | Analoge Spannungsreferenz |
|      17 | SDA             | JDIGITAL_MCU_I2C_3V3  | 3,3 V MCU       | PH12        | I2C-Daten (I2C4 / I3C1)   |
|      18 | SCL             | JDIGITAL_MCU_I2C_3V3  | 3,3 V MCU       | PH11        | I2C-Takt (I2C4 / I3C1)    |

>📝 **Hinweis:** Alle JDIGITAL-Leitungen entsprechen der 3,3-V-MCU-Logik. Die meisten Pins sind im Digitalmodus als Eingänge 5-V-tolerant. AREF ist ein analoger Spannungsreferenz-Eingang für den ADC der MCU. Er wird über einen integrierten Analogschalter (U28, SGM3157YC6/TR) geleitet und ist nur aktiv, wenn der MCU-Pin PI8 auf HIGH gesetzt ist.

### JSPI

Der JSPI-Stecker stellt einen dedizierten SPI-Bus für den Anschluss von Peripheriegeräten wie SD-Kartenlesern, Display-Treibern oder Sensoren bereit. Er liefert zudem RESET und Stromversorgung. Alle Signale liegen im 3,3-V-MCU-Bereich.

| **Pin** | **Bezeichnung** | **Netz**         | **Spannungsbereich** | **MCU-Pin** | **Hinweise** |
| ------: | --------------- | ---------------- | -------------------- | ----------- | ------------ |
|       1 | MISO            | JSPI_MCU_SPI_3V3 | 3,3 V MCU            | PF14        | SPI MISO     |
|       2 | +5 V            | +5V_LIMITED      | Stromversorgung      | -           | 5-V-Ausgang  |
|       3 | SCK             | JSPI_MCU_SPI_3V3 | 3,3-V-MCU            | PC10        | SPI-Takt     |
|       4 | MOSI            | JSPI_MCU_SPI_3V3 | 3,3 V MCU            | PC12        | SPI MOSI     |
|       5 | RESET           | MCU_NRST         | 3,3 V MCU            | NRST        | MCU-Reset    |
|       6 | GND             | GND              | Stromversorgung      | -           | Masse        |

>⚠️ **Hinweis zum Stromschutz:** Die 3,3-V- und 5-V-Versorgungsspannungen an den JSPI- und UNO-Shield-Anschlüssen sind durch spezielle Lastschalter (MP5077GG-Z) geschützt, die jeweils auf **2,8 A** begrenzt sind. Diese Schalter verhindern, dass angeschlossene Peripheriegeräte übermäßige Stromstärken beziehen, und schützen das Board vor Rückspeisung. Versuchen Sie nicht, diese Schalter zu umgehen oder zu deaktivieren.

### Qwiic

Der Qwiic-Anschluss bietet einen 3,3-V-I2C-Bus für den Plug-and-Play-Anschluss an Modulino®-Knoten und kompatible Sensoren von Drittanbietern, ohne dass ein Löten erforderlich ist. Der Anschluss ist polarisiert und lässt sich nur in einer einzigen Ausrichtung anschließen.

| **Pin** | **Bezeichnung** | **Netz**     | **Domäne**      | **MCU-Pin** | **Hinweise**                |
| ------: | --------------- | ------------ | --------------- | ----------- | --------------------------- |
|       1 | GND             | GND          | Stromversorgung | -           | Masse                       |
|       2 | VCC             | +3V3_LIMITED | Stromversorgung | -           | 3,3-V-Versorgung für Geräte |
|       3 | SDA             | I2C3_SDA     | 3,3 V MCU       | PC9         | I2C-Daten                   |
|       4 | SCL             | I2C3_SCL     | 3,3 V MCU       | PA8         | I2C-Takt                    |

>📝 **Hinweis:** Qwiic-Anschlüsse sind in Kettenform erweiterbar, und mehrere Module können auf demselben I2C-Bus in Reihe geschaltet werden. Der I2C-Bus ist mit der MCU verbunden.

### JCTL (MPU-Fern-Debugging)

Der JCTL-Stecker ist ein 10-poliger (2×5) Anschluss, der Zugriff auf die MPU-UART-Konsole, die Steuerung der Boot-Überschreibung sowie Signale für das Energiemanagement bereitstellt. Arduino Bughopper ist das empfohlene Tool für die Anbindung an diesen Stecker. Die meisten aktiven Signalpins sind über TVS-Dioden ESD-geschützt (Pin 10 ist es nicht). Die Signalpins arbeiten in gemischten Spannungsbereichen (1,8 V, 3,3 V und 7–24 V); siehe dazu die untenstehende Pin-Tabelle. Pin 9 legt die Spannung `SOM_VREG_MDPX3_1P8` direkt frei; legen Sie an diesen Pin keine externe Spannung an.

| **Pin** | **Bezeichnung**        | **Netz**           | **Spannungsbereich** | **MPU-Pin** | **Hinweise**                                                                                                                                                                          |
| ------: | ---------------------- | ------------------ | -------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       1 | GND                    | GND                | Stromversorgung      | -           | Masse                                                                                                                                                                                 |
|       2 | FORCED_USB_BOOT_N      | FORCE_BOOT_3V3     | 3,3 V                | -           | 3,3-V-Domäne. Steuert zwei NMOS-Transistoren, die MD_FORCE_USB_BOOT_1V8 und RTSS_FORCE_USB_BOOT_1V8 ansteuern. Auf LOW setzen, um beim nächsten Neustart in den EDL-Modus zu wechseln |
|       3 | PMIC_POWER_EN          | PMIC_POWER_EN      | 1,8 V MPU            | -           | PMIC-Stromfreigabe                                                                                                                                                                    |
|       4 | TX                     | UART_DBG_1V8       | 1,8 V MPU            | GPIO_43     | MPU-Debug-UART-TX                                                                                                                                                                     |
|       5 | GPIO                   | MD_GPIO_103        | 1,8 V MPU            | GPIO_103    | Allzweck-GPIO                                                                                                                                                                         |
|       6 | RX                     | UART_DBG_1V8       | 1,8 V MPU            | GPIO_44     | MPU-Debug-UART-Empfänger                                                                                                                                                              |
|       7 | GND                    | GND                | Stromversorgung      | -           | Masse                                                                                                                                                                                 |
|       8 | RESIN_N                | RESIN_N            | 3,3 V                | -           | Open-Drain, TVS-geschützt. Für einen Hot-Reboot auf LOW ziehen (Spannungsschienen bleiben eingeschaltet)                                                                              |
|       9 | +1V8 OUT               | SOM_VREG_MDPX3_1P8 | Stromversorgung      | -           | MDPX3-Domäne 1,8 V direkt, keine externe Spannung anlegen                                                                                                                             |
|      10 | POWER_SWITCH_DISABLE_N | PWR_DISABLE        | 7–24 V (max. 5 V)    | -           | Nicht TVS-geschützt. Auf LOW ziehen für einen Kaltstart (schaltet die Hauptstromversorgung ab)                                                                                        |

> ⚠️ **Bitte lesen Sie dies, bevor Sie irgendetwas an den JCTL anschließen**
>
> Pin 9 legt `SOM_VREG_MDPX3_1P8` (~1,8 V) direkt frei; legen Sie an diesem Pin keine externe Spannung an. Die Pins arbeiten in gemischten Spannungsbereichen: Die Pins 2 und 8 liegen im 3,3-V-Bereich, die Pins 4 und 6 (UART) im 1,8-V-Bereich, Pin 10 ist der Freigabeeingang für den Haupt-VIN-Stromschalter; ein interner Spannungsteiler ermöglicht den direkten Anschluss an VIN. Ziehen Sie die Spannung unter 0,85 V, um die Hauptstromversorgung zu deaktivieren; halten Sie sie für den Normalbetrieb über 1 V und überschreiten Sie extern nicht 5 V. Pin 10 ist nicht durch TVS-Dioden geschützt. Das Anlegen falscher Spannungen an einen aktiven JCTL-Pin kann den QCS8275-SoM dauerhaft beschädigen.
>
> **Der Arduino Bughopper wird dringend empfohlen** für die meisten Debugging-Anwendungsfälle, da er Pegelwandler und Open-Drain-kompatible Ausgangsstufen enthält, die speziell für eine sichere Anbindung an JCTL entwickelt wurden.
>
> Sollten Sie sich stattdessen für einen anderen USB-zu-UART-Adapter oder eine benutzerdefinierte Debug-Hardware entscheiden, stellen Sie sicher, dass alle Signalleitungen mit der für ihren jeweiligen Bereich korrekten Spannung angesteuert werden, dass Pin 10 niemals über 5 V angesteuert wird und dass kein Rückstrompfad zur `SOM_VREG_MDPX3_1P8`-Schiene besteht.

> 📝 **Zusammenfassung der Boot-Steuerung:**
>
> - **Hot-Reboot** (nur MPU, Spannungsschienen bleiben aktiv): Ziehen Sie Pin 8 (RESIN_N) über Open-Drain auf LOW.
> - **Cold-Reboot** (vollständiger Stromzyklus, Hauptstromversorgung abgeschaltet): Setzen Sie Pin 10 (POWER_SWITCH_DISABLE_N) über Open-Drain auf LOW.
> - **EDL / Notfall-Download-Modus**: Setzen Sie Pin 2 (FORCED_USB_BOOT_N) über Open-Drain auf LOW und lösen Sie anschließend über Pin 8 oder Pin 10 einen Neustart aus.
>
> Dieser Anschluss ist für Entwicklungs- und Debugging-Zwecke vorgesehen.

### JHAT

Der JHAT-Steckverbinder ist ein standardmäßiger, mit dem Raspberry Pi® kompatibler 40-poliger Steckverbinder, der von der MPU (QCS8275) mit **3,3 V**-Logik angesteuert wird. Er stellt I2C-, SPI-, UART-, I2S- und universelle GPIO-Signale der MPU bereit. Die Stromversorgungspins liefern 3,3 V und 5 V an angeschlossene HATs.

Alle GPIO-Signale werden durch vier integrierte bidirektionale Pegelwandler – drei 8-Kanal-TXS0108ERKSR-Bausteine (U33_2, U33_3, U33_4) sowie einem 4-Kanal-Baustein vom Typ TXS0104ERUTR (U21), was eine direkte Kompatibilität mit Standard-Raspberry-Pi®-HAT-Designs ohne zusätzliche Pegelumsetzung ermöglicht.

| **Pin** | **Bezeichnung** | **MPU-Pin** | **Alternative Funktion** | **Domäne**      | **Hinweise**              |
| ------: | --------------- | ----------- | ------------------------ | --------------- | ------------------------- |
|       1 | +3V3 OUT        | -           | -                        | Stromversorgung | 3,3-V-Versorgungsausgang  |
|       2 | +5V OUT         | -           | -                        | Stromversorgung | 5-V-Ausgang               |
|       3 | GPIO 2 (SDA)    | MD_GPIO_17  | QUP0_SE0_I2C_SDA         | 3,3-V-MPU       | I2C1-Daten                |
|       4 | +5V OUT         | -           | -                        | Stromversorgung | 5-V-Ausgang               |
|       5 | GPIO 3 (SCL)    | MD_GPIO_18  | QUP0_SE0_I2C_SCL         | 3,3 V MPU       | I2C1-Takt                 |
|       6 | GND             | -           | -                        | Stromversorgung | Masse                     |
|       7 | GPIO 4          | MD_GPIO_83  | GPCLK0                   | 3,3 V MPU       | Allgemeiner GPIO          |
|       8 | GPIO 14 (TX)    | MD_GPIO_86  | QUP1_SE2_UART_TX         | 3,3 V MPU       | UART0 TX                  |
|       9 | GND             | -           | -                        | Stromversorgung | Masse                     |
|      10 | GPIO 15 (RX)    | MD_GPIO_87  | QUP1_SE2_UART_RX         | 3,3 V MPU       | UART0 RX                  |
|      11 | GPIO 17         | MD_GPIO_85  | QUP1_SE2_UART_RFR        | 3,3 V MPU       | UART RFR/RTS              |
|      12 | GPIO 18 (CLK)   | MD_GPIO_116 | LPI_I2S1_SCK             | 3,3 V MPU       | PCM-Takt                  |
|      13 | GPIO 27         | MD_GPIO_109 | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      14 | GND             | -           | -                        | Stromversorgung | Masse                     |
|      15 | GPIO 22         | MD_GPIO_90  | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      16 | GPIO 23         | MD_GPIO_105 | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      17 | +3V3 OUT        | -           | -                        | Stromversorgung | 3,3-V-Versorgungsausgang  |
|      18 | GPIO 24         | MD_GPIO_106 | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      19 | GPIO 10 (MOSI)  | MD_GPIO_26  | QUP0_SE3_SPI_MOSI        | 3,3 V MPU       | SPI0 MOSI                 |
|      20 | GND             | -           | -                        | Stromversorgung | Masse                     |
|      21 | GPIO 9 (MISO)   | MD_GPIO_25  | QUP0_SE3_SPI_MISO        | 3,3 V MPU       | SPI0 MISO                 |
|      22 | GPIO 25         | MD_GPIO_107 | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      23 | GPIO 11 (SCLK)  | MD_GPIO_27  | QUP0_SE3_SPI_SCK         | 3,3 V MPU       | SPI0-Takt                 |
|      24 | GPIO 8 (CE0)    | MD_GPIO_28  | QUP0_SE3_SPI_CS          | 3,3 V MPU       | SPI0 CE0                  |
|      25 | GND             | -           | -                        | Stromversorgung | Masse                     |
|      26 | GPIO 7 (CE1)    | MD_GPIO_88  | GPIO                     | 3,3 V MPU       | SPI0 CE1                  |
|      27 | GPIO 0 (SDA)    | MD_GPIO_19  | QUP0_SE1_I2C_SDA         | 3,3 V MPU       | I2C0 / EEPROM SDA         |
|      28 | GPIO 1 (SCL)    | MD_GPIO_20  | QUP0_SE1_I2C_SCL         | 3,3 V MPU       | I2C0 / EEPROM SCL         |
|      29 | GPIO 5          | MD_GPIO_89  | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      30 | GND             | -           | -                        | Stromversorgung | Masse                     |
|      31 | GPIO 6          | MD_GPIO_80  | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      32 | GPIO 12 (PWM0)  | MD_GPIO_77  | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      33 | GPIO 13 (PWM1)  | MD_GPIO_81  | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      34 | GND             | -           | -                        | Stromversorgung | Masse                     |
|      35 | GPIO 19 (FS)    | MD_GPIO_117 | LPI_I2S1_WS              | 3,3 V MPU       | PCM-Frame-Synchronisation |
|      36 | GPIO 16         | MD_GPIO_84  | QUP1_SE2_UART_CTS        | 3,3 V MPU       | UART-CTS                  |
|      37 | GPIO 26         | MD_GPIO_108 | GPIO                     | 3,3 V MPU       | Allgemeiner GPIO          |
|      38 | GPIO 20 (DIN)   | MD_GPIO_118 | LPI_I2S1_DATA0           | 3,3 V MPU       | PCM-Dateneingang          |
|      39 | GND             | -           | -                        | Stromversorgung | Masse                     |
|      40 | GPIO 21 (DOUT)  | MD_GPIO_119 | LPI_I2S1_DATA1           | 3,3 V MPU       | PCM-Datenausgang          |

>📝 **Hinweis:** Obwohl die MPU-GPIO-Signale intern bei 1,8 V liegen, stellen die integrierten Pegelwandler TXS0108ERKSR und TXS0104ERUTR diese am JHAT-Anschluss mit 3,3 V bereit, wodurch sie direkt mit den Standard-Logikpegeln des Raspberry Pi® HAT kompatibel sind. Legen Sie an keinen JHAT-Signalpin Spannungen über 3,3 V an. Die Stromversorgungs-Pins (3,3 V und 5 V) sind Ausgänge mit dem Board; bitte leiten Sie über diese keine Stromrückführung von einem angeschlossenen HAT zurück.

>📝 **Hinweis:** Die JHAT-UART-Pins 8, 10, 11 und 36 (TX, RX, RFR und CTS) nutzen denselben QUP1_SE2-UART wie das integrierte Wi-Fi®/Bluetooth® LE-Modul. TX, RX und RFR werden über U33_4 (TXS0108ERKSR) pegelkonvertiert, während CTS zusammen mit GPIO 26, GPIO 20 (I2S_DATA0) und GPIO 21 (I2S_DATA1) an den Pins 37, 38 und 40. Diese Pins stehen nicht für die Nutzung durch externe HATs zur Verfügung, solange Bluetooth aktiv ist.

### JMISC

Der JMISC-Steckverbinder ist ein 60-poliger Hochdichte-Steckverbinder, der den parallelen PSSI-Kamerabus der MCU, die GPIO-Pins der MCU, den I2C-Bus der MCU, Audio-Signale (Mikrofon, Kopfhörer, Mono-Lautsprecherausgang, Line-Out), den SoC-SPI-Bus der MPU, die GPIO-Pins der MPU sowie die I2S-Signale der MPU vereint. Es handelt sich um einen gemischten Spannungs-Steckverbinder: **MCU-Signale liegen bei 3,3 V**, **MPU-Signale bei 1,8 V** und die Audio-/Mikrofon-Pins sind analog.

| **Pin** | **Bezeichnung**     | **Domäne**      | **MCU-Pin** | **MPU-Pin** | **Hinweise**                                   |
| ------: | ------------------- | --------------- | ----------- | ----------- | ---------------------------------------------- |
|       1 | MCU_PSSI_D0         | 3,3 V MCU       | PA9         | -           | PSSI-Datenbit 0                                |
|       2 | MCU_TRACE_CLK       | 3,3 V MCU       | PE2         | -           | MCU-Trace-Takt                                 |
|       3 | MCU_PSSI_D1         | 3,3 V MCU       | PC7         | -           | PSSI-Datenbit 1                                |
|       4 | MCU_TRACE_D0        | 3,3 V MCU       | PE3         | -           | MCU-Trace-Daten 0                              |
|       5 | MCU_PSSI_D2         | 3,3 V MCU       | PC8         | -           | PSSI-Datenbit 2                                |
|       6 | MCU_TRACE_D1        | 3,3 V MCU       | PE4         | -           | MCU-Trace-Daten 1                              |
|       7 | MCU_PSSI_D3         | 3,3 V MCU       | PE1         | -           | PSSI-Datenbit 3                                |
|       8 | MCU_TRACE_D2        | 3,3 V MCU       | PE5         | -           | MCU-Trace-Daten 2                              |
|       9 | MCU_PSSI_D4         | 3,3 V MCU       | PC11        | -           | PSSI-Datenbit 4                                |
|      10 | MCU_TRACE_D3        | 3,3 V MCU       | PE6         | -           | MCU-Trace-Daten 3                              |
|      11 | MCU_PSSI_D5         | 3,3 V MCU       | PD3         | -           | PSSI-Datenbit 5                                |
|      12 | MCU_USART2_RX       | 3,3 V MCU       | PE7         | -           | MCU USART2-Empfang                             |
|      13 | MCU_PSSI_D6         | 3,3 V MCU       | PF4         | -           | PSSI-Datenbit 6                                |
|      14 | MCU_USART2_TX       | 3,3 V MCU       | PE8         | -           | MCU USART2 TX                                  |
|      15 | MCU_PSSI_D7         | 3,3 V MCU       | PI7         | -           | PSSI-Datenbit 7                                |
|      16 | MCU_I2C_SCL         | 3,3 V MCU       | PF1         | -           | MCU-I2C2-Takt                                  |
|      17 | MCU_PSSI_PDCK       | 3,3 V MCU       | PA6         | -           | PSSI-Pixeltakt                                 |
|      18 | MCU_I2C_SDA         | 3,3 V MCU       | PF0         | -           | MCU-I2C2-Daten                                 |
|      19 | MCU_PSSI_RDY        | 3,3 V MCU       | PI5         | -           | PSSI-Bereit                                    |
|      20 | MCU_GPIO_PA0        | 3,3 V MCU       | PA0         | -           | MCU-GPIO                                       |
|      21 | MCU_PSSI_DE         | 3,3 V MCU       | PH8         | -           | PSSI-Datenfreigabe                             |
|      22 | MCU_GPIO_PA1        | 3,3 V MCU       | PA1         | -           | MCU-GPIO                                       |
|      23 | MCU_UART4_RX        | 3,3 V MCU       | PA11        | -           | MCU UART4 RX                                   |
|      24 | MCU_GPIO_PA2        | 3,3 V MCU       | PA2         | -           | MCU-GPIO                                       |
|      25 | MCU_UART4_TX        | 3,3 V MCU       | PA12        | -           | MCU UART4 TX                                   |
|      26 | GND                 | Stromversorgung | -           | -           | Masse                                          |
|      27 | GND                 | Stromversorgung | -           | -           | Masse                                          |
|      28 | EAR_P               | Analog          | -           | -           | Lautsprecherausgang P (Mono)                   |
|      29 | MIC_INP             | Analog          | -           | -           | Mikrofon-Eingang+                              |
|      30 | EAR_M               | Analog          | -           | -           | Lautsprecherausgang M (Mono)                   |
|      31 | MIC_INN             | Analog          | -           | -           | Mikrofon-Eingang−                              |
|      32 | LINEOUT_P           | Analog          | -           | -           | Line-Ausgang P                                 |
|      33 | MIC_BIAS            | Analog          | -           | -           | Mikrofon-Vorspannung                           |
|      34 | LINEOUT_M           | Analog          | -           | -           | Line-Out M                                     |
|      35 | GND                 | Stromversorgung | -           | -           | Masse                                          |
|      36 | HPH_L               | Analog          | -           | -           | Kopfhörer links                                |
|      37 | SOC_SPI_MISO        | 1,8 V MPU       | -           | GPIO_10     | MPU SPI MISO (SE0)                             |
|      38 | HPH_R               | Analog          | -           | -           | Kopfhörer rechts                               |
|      39 | SOC_SPI_MOSI        | 1,8 V MPU       | -           | GPIO_11     | MPU SPI MOSI (SE0)                             |
|      40 | HPH_REF             | Analog          | -           | -           | Kopfhörer-Referenz                             |
|      41 | SOC_SPI_SCK         | 1,8 V MPU       | -           | GPIO_12     | MPU SPI-Takt (SE0)                             |
|      42 | HS_DET              | Analog          | -           | -           | Headset-Erkennung                              |
|      43 | SOC_SPI_CS0         | 1,8 V MPU       | -           | GPIO_13     | MPU-SPI-Chipauswahl 0 (SE0)                    |
|      44 | GND                 | Stromversorgung | -           | -           | Masse                                          |
|      45 | SOC_SPI_CS2         | 1,8 V MPU       | -           | GPIO_15     | MPU-SPI-Chipauswahl 2 (SE0)                    |
|      46 | SOC_MI2S_SCK        | 1,8 V MPU       | -           | GPIO_120    | I2S-Takt                                       |
|      47 | SOC_SPI_CS1         | 1,8 V MPU       | -           | GPIO_14     | MPU-SPI-Chipauswahl 1 (SE0)                    |
|      48 | SOC_MI2S_WS         | 1,8 V MPU       | -           | GPIO_121    | I2S-Wortauswahl                                |
|      49 | SOC_GPIO_73         | 1,8 V MPU       | -           | GPIO_73     | MPU-SoC-GPIO                                   |
|      50 | SOC_MI2S_DATA0      | 1,8 V MPU       | -           | GPIO_122    | I2S-Daten 0                                    |
|      51 | SOC_GPIO_74         | 1,8 V MPU       | -           | GPIO_74     | MPU-SoC-GPIO                                   |
|      52 | SOC_MI2S_DATA1      | 1,8 V MPU       | -           | GPIO_123    | I2S-Daten 1                                    |
|      53 | +3V3 OUT            | Stromversorgung | -           | -           | 3,3-V-Versorgungsausgang                       |
|      54 | +5V OUT             | Stromversorgung | -           | -           | 5-V-Versorgungsausgang                         |
|      55 | +3V3 OUT            | Stromversorgung | -           | -           | 3,3-V-Versorgungsausgang                       |
|      56 | +5V OUT             | Stromversorgung | -           | -           | 5-V-Versorgungsausgang                         |
|      57 | SOM_VREG_MDPX3_1P8  | Stromversorgung | -           | -           | SOM-1,8-V-Versorgungsspannung                  |
|      58 | GND                 | Stromversorgung | -           | -           | Masse                                          |
|      59 | SOM_VCOIN / VBAT    | RTC-Puffer      | -           | -           | Eingang für RTC-Pufferbatterie von SOM und MCU |
|      60 | NICHT ANGESCHLOSSEN | -               | -           | -           | -                                              |

>📝 **Hinweis:** Die MCU-Pins sind mit 3,3 V, die MPU-SoC-Pins mit 1,8 V betrieben, die Audio-/Mikrofon-Pins sind analog. Mischen Sie die Spannungsbereiche nicht. Die SoC-GPIO-Leitungen auf dem JMISC sind für bestimmte Schnittstellen vorgesehen und keine universellen Maker-GPIOs.

>📝 **Hinweis:** Pin 59 des JMISC akzeptiert eine RTC-Pufferbatterie mit bis zu 3,3 V, um die Echtzeituhren des SOM und der MCU aufrechtzuerhalten, wenn das Board ansonsten nicht mit Strom versorgt wird. `SOM_VCOIN` (SOM-RTC) und `VBAT` (MCU-RTC) sind zwei Eingänge für RTC-Pufferbatterien, die physikalisch an diesem einzigen Pin miteinander verbunden sind und nicht über eine gemeinsame Versorgungsschiene. Jeder ist über einen eigenen 0-Ω-Widerstand mit einem gemeinsamen Knoten verbunden, der durch eine bidirektionale TVS-Diode (Vr = 5,5 V) mit Bezug auf Masse geschützt ist. Die zu erwartende Stromstärke ist sehr gering, und dieser Pin liefert keine Stromversorgung, um den Rest des Boards im Betrieb zu halten.

### JMEDIA

Der JMEDIA-Steckverbinder ist ein 60-poliger Hochdichte-Steckverbinder, der MIPI DSI (Display), MIPI CSI0 und CSI1, Kamerataktsignale sowie I2C-Busse zur Kamerasteuerung überträgt. Alle Signale liegen im **1,8-V-MPU-Bereich**. Die Stromversorgungs-Pins liefern 3,3 V Ausgangsspannung und akzeptieren eine Eingangsspannung von 7–24 V Gleichstrom.

| **Pin** | **Bezeichnung** | **Domäne**      | **MPU-Pin** | **Hinweise**                                           |
| ------: | --------------- | --------------- | ----------- | ------------------------------------------------------ |
|       1 | GND             | Stromversorgung | -           | Masse                                                  |
|       2 | GND             | Stromversorgung | -           | Masse                                                  |
|       3 | MIPI_DSI0_CLK_M | MIPI D-PHY      | -           | DSI-Takt −                                             |
|       4 | MIPI_DSI0_L1_P  | MIPI D-PHY      | -           | DSI-Lane 1 +                                           |
|       5 | MIPI_DSI0_CLK_P | MIPI D-PHY      | -           | DSI-Takt +                                             |
|       6 | MIPI_DSI0_L1_M  | MIPI D-PHY      | -           | DSI-Lane 1 −                                           |
|       7 | GND             | Stromversorgung | -           | Masse                                                  |
|       8 | GND             | Stromversorgung | -           | Masse                                                  |
|       9 | MIPI_DSI0_L2_M  | MIPI D-PHY      | -           | DSI-Kanal 2 −                                          |
|      10 | MIPI_DSI0_L0_P  | MIPI D-PHY      | -           | DSI-Kanal 0 +                                          |
|      11 | MIPI_DSI0_L2_P  | MIPI D-PHY      | -           | DSI-Kanal 2 +                                          |
|      12 | MIPI_DSI0_L0_M  | MIPI D-PHY      | -           | DSI-Lane 0 −                                           |
|      13 | GND             | Stromversorgung | -           | Masse                                                  |
|      14 | GND             | Stromversorgung | -           | Masse                                                  |
|      15 | MIPI_DSI0_L3_M  | MIPI D-PHY      | -           | DSI-Lane 3 −                                           |
|      16 | SOC_CAM_MCLK0   | 1,8 V MPU       | GPIO_67     | Kamera-Master-Takt 0                                   |
|      17 | MIPI_DSI0_L3_P  | MIPI D-PHY      | -           | DSI-Lane 3 +                                           |
|      18 | SOC_CAM_MCLK1   | 1,8 V MPU       | GPIO_68     | Kameramastertakt 1                                     |
|      19 | GND             | Stromversorgung | -           | Masse                                                  |
|      20 | GND             | Stromversorgung | -           | Masse                                                  |
|      21 | CSI0_LN0_M      | MIPI D-PHY      | -           | CSI0-Datenleitung 0 −                                  |
|      22 | CCI_I2C2_SDA    | 1,8 V MPU       | GPIO_59     | Kamerasteuerung I2C2 SDA                               |
|      23 | CSI0_LN0_P      | MIPI D-PHY      | -           | CSI0-Datenleitung 0 +                                  |
|      24 | CCI_I2C2_SCL    | 1,8 V MPU       | GPIO_60     | Kamerasteuerung I2C2 SCL                               |
|      25 | GND             | Stromversorgung | -           | Masse                                                  |
|      26 | GND             | Stromversorgung | -           | Masse                                                  |
|      27 | CSI0_LN1_M      | MIPI D-PHY      | -           | CSI0-Datenleitung 1 −                                  |
|      28 | CSI1_LN3_P      | MIPI D-PHY      | -           | CSI1-Datenleitung 3 +                                  |
|      29 | CSI0_LN1_P      | MIPI D-PHY      | -           | CSI0-Datenleitung 1 +                                  |
|      30 | CSI1_LN3_M      | MIPI D-PHY      | -           | CSI1-Datenleitung 3 −                                  |
|      31 | GND             | Stromversorgung | -           | Masse                                                  |
|      32 | GND             | Stromversorgung | -           | Masse                                                  |
|      33 | CSI0_CLK_M      | MIPI D-PHY      | -           | CSI0-Takt −                                            |
|      34 | CSI1_LN2_P      | MIPI D-PHY      | -           | CSI1-Datenleitung 2 +                                  |
|      35 | CSI0_CLK_P      | MIPI D-PHY      | -           | CSI0-Takt +                                            |
|      36 | CSI1_LN2_M      | MIPI D-PHY      | -           | CSI1-Datenleitung 2 −                                  |
|      37 | GND             | Stromversorgung | -           | Masse                                                  |
|      38 | GND             | Stromversorgung | -           | Masse                                                  |
|      39 | CSI0_LN2_M      | MIPI D-PHY      | -           | CSI0-Datenleitung 2 −                                  |
|      40 | CSI1_CLK_P      | MIPI D-PHY      | -           | CSI1-Takt +                                            |
|      41 | CSI0_LN2_P      | MIPI D-PHY      | -           | CSI0-Datenleitung 2 +                                  |
|      42 | CSI1_CLK_M      | MIPI D-PHY      | -           | CSI1-Takt −                                            |
|      43 | GND             | Stromversorgung | -           | Masse                                                  |
|      44 | GND             | Stromversorgung | -           | Masse                                                  |
|      45 | CSI0_LN3_M      | MIPI D-PHY      | -           | CSI0-Datenleitung 3 −                                  |
|      46 | CSI1_LN1_P      | MIPI D-PHY      | -           | CSI1-Datenleitung 1 +                                  |
|      47 | CSI0_LN3_P      | MIPI D-PHY      | -           | CSI0-Datenleitung 3 +                                  |
|      48 | CSI1_LN1_M      | MIPI D-PHY      | -           | CSI1-Datenleitung 1 −                                  |
|      49 | GND             | Stromversorgung | -           | Masse                                                  |
|      50 | GND             | Stromversorgung | -           | Masse                                                  |
|      51 | CCI_I2C0_SCL    | 1,8 V MPU       | GPIO_58     | Kamerasteuerung I2C0 SCL                               |
|      52 | CSI1_LN0_P      | MIPI D-PHY      | -           | CSI1-Datenleitung 0 +                                  |
|      53 | CCI_I2C0_SDA    | 1,8 V MPU       | GPIO_57     | Kamerasteuerung I2C0 SDA                               |
|      54 | CSI1_LN0_M      | MIPI D-PHY      | -           | CSI1-Datenleitung 0 −                                  |
|      55 | GND             | Stromversorgung | -           | Masse                                                  |
|      56 | GND             | Stromversorgung | -           | Masse                                                  |
|      57 | VIN IN          | Stromversorgung | -           | 7–24 V DC-Eingang (max. 1,5 A, PTC-geschützt)          |
|      58 | +3V3 OUT        | Stromversorgung | -           | 3,3-V-Ausgang                                          |
|      59 | VIN IN          | Stromversorgung | -           | 7–24 V Gleichstrom-Eingang (max. 1,5 A, PTC-gesichert) |
|      60 | +3V3 OUT        | Stromversorgung | -           | 3,3-V-Ausgang                                          |

> 📝 **Hinweis:** Die VIN-Pins auf dem JMEDIA-Board (Pins 57 und 59) gehören zum selben Netz und sind durch eine 1,5-A-PTC-Sicherung (F3, MF-MSMF150/24X) sowie eine 24-V-TVS-Diode geschützt. Sie können einen Carrier mit Strom versorgen, sind jedoch nicht dafür vorgesehen, das gesamte VENTUNO Q-Board über eine externe Quelle mit Strom zu versorgen.

>📝 **Hinweis:** Die MIPI-CSI/DSI-Differentialpaare sind D-PHY-Signale und sollten nicht als universelle Ein-/Ausgänge verwendet werden. Alle Steuersignale (CCI_I2C, CAM_MCLK) liegen im 1,8-V-MPU-Bereich. VIN an den Pins 57 und 59 dient ausschließlich der Gleichstrom-Eingangsspannungsversorgung.

### JOMEGA

Der JOMEGA-Steckverbinder ist ein 100-poliger Erweiterungssteckverbinder mit hoher Pin-Dichte, der USB 3.0-, CAN-FD-, JTAG-, MPU-GPIO-, SPI- und UART-Debug- sowie Energiemanagement-Signale bereitstellt. Die Spannungsdomänen sind gemischt: USB und einige Steuersignale werden mit 3,3 V angesteuert, während JTAG-, SPI- und UART-Debug-Signale mit 1,8 V im MPU-Bereich angesteuert werden.

| **Pin** | **Bezeichnung**           | **Domäne**      | **MCU-Pin** | **MPU-Pin** | **Hinweise**                               |
| ------: | ------------------------- | --------------- | ----------- | ----------- | ------------------------------------------ |
|       1 | VIN                       | Stromversorgung | -           | -           | 7–24 V DC-Eingang                          |
|       2 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|       3 | VIN                       | Stromversorgung | -           | -           | 7–24 V DC-Eingang                          |
|       4 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|       5 | VIN                       | Stromversorgung | -           | -           | 7–24 V DC-Eingang                          |
|       6 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|       7 | VIN                       | Stromversorgung | -           | -           | 7–24 V DC-Eingang                          |
|       8 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|       9 | VIN                       | Stromversorgung | -           | -           | 7–24 V DC-Eingang                          |
|      10 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      11 | VIN                       | Stromversorgung | -           | -           | 7–24 V DC-Eingang                          |
|      12 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      13 | VIN                       | Stromversorgung | -           | -           | 7–24 V DC-Eingang                          |
|      14 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      15 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      16 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      17 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      18 | USB3.0_1_SS_TX_P          | USB 3.0         | -           | -           | USB-Anschluss 1 SuperSpeed TX+             |
|      19 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      20 | USB3.0_1_SS_TX_N          | USB 3.0         | -           | -           | USB-Anschluss 1 SuperSpeed TX−             |
|      21 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      22 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      23 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      24 | USB3.0_1_HS_D_P           | USB 3.0         | -           | -           | USB-Anschluss 1 HighSpeed D+               |
|      25 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      26 | USB3.0_1_HS_D_N           | USB 3.0         | -           | -           | USB-Anschluss 1 HighSpeed D−               |
|      27 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      28 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      29 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      30 | USB3.0_1_SS_RX_P          | USB 3.0         | -           | -           | USB-Anschluss 1 SuperSpeed RX+             |
|      31 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      32 | USB3.0_1_SS_RX_N          | USB 3.0         | -           | -           | USB-Anschluss 1 SuperSpeed RX−             |
|      33 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      34 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      35 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      36 | USB3.0_2_SS_TX_P          | USB 3.0         | -           | -           | USB-Anschluss 2 SuperSpeed TX+             |
|      37 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      38 | USB3.0_2_SS_TX_N          | USB 3.0         | -           | -           | USB-Anschluss 2 SuperSpeed TX−             |
|      39 | IO0_3V3                   | 3,3 V MCU       | PC0         | -           | MCU-GPIO                                   |
|      40 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      41 | IO1_3V3                   | 3,3 V MCU       | PC1         | -           | MCU-GPIO                                   |
|      42 | USB3.0_2_HS_D_P           | USB 3.0         | -           | -           | USB-Anschluss 2 HighSpeed D+               |
|      43 | IO2_3V3                   | 3,3 V MCU       | PC2         | -           | MCU-GPIO                                   |
|      44 | USB3.0_2_HS_D_N           | USB 3.0         | -           | -           | USB-Anschluss 2 HighSpeed D−               |
|      45 | IO3_3V3                   | 3,3 V MCU       | PC3         | -           | MCU-GPIO                                   |
|      46 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      47 | IO4_3V3                   | 3,3 V MCU       | PD12        | -           | MCU-GPIO                                   |
|      48 | USB3.0_2_SS_RX_P          | USB 3.0         | -           | -           | USB-Anschluss 2 SuperSpeed RX+             |
|      49 | IO5_3V3                   | 3,3 V MCU       | PD13        | -           | MCU-GPIO                                   |
|      50 | USB3.0_2_SS_RX_N          | USB 3.0         | -           | -           | USB-Anschluss 2 SuperSpeed RX−             |
|      51 | IO6_3V3                   | 3,3 V MCU       | PD14        | -           | MCU-GPIO                                   |
|      52 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      53 | IO7_3V3                   | 3,3 V MCU       | PD15        | -           | MCU-GPIO                                   |
|      54 | USB3.0_1_PWRON_3V3        | 3,3 V           | -           | -           | Stromfreigabe für USB-Anschluss 1          |
|      55 | IO8_3V3                   | 3,3 V MCU       | PI2         | -           | MCU-GPIO                                   |
|      56 | USB3.0_1_OVERCUR_3V3      | 3,3 V           | -           | -           | Überstrom-Flag für USB-Anschluss 1         |
|      57 | MIC_INP                   | Analog          | -           | -           | Mikrofon-Eingang+                          |
|      58 | USB3.0_2_PWRON_3V3        | 3,3 V           | -           | -           | Stromfreigabe USB-Anschluss 2              |
|      59 | MIC_INN                   | Analog          | -           | -           | Mikrofon-Eingang−                          |
|      60 | USB3.0_2_OVERCUR_3V3      | 3,3 V           | -           | -           | Überstrom-Flag für USB-Anschluss 2         |
|      61 | MIC_BIAS                  | Analog          | -           | -           | Mikrofon-Vorspannung                       |
|      62 | SPI_ICS_MISO              | 1,8 V MPU       | -           | GPIO_39     | MPU SPI MISO (SPI_ICS_1V8)                 |
|      63 | TMS                       | 1,8 V MPU       | -           | -           | JTAG TMS (JTAG_1V8)                        |
|      64 | SPI_ICS_MOSI              | 1,8 V MPU       | -           | GPIO_40     | MPU SPI MOSI                               |
|      65 | TDO                       | 1,8 V MPU       | -           | -           | JTAG TDO                                   |
|      66 | SPI_ICS_SCK               | 1,8 V MPU       | -           | GPIO_37     | MPU-SPI-Takt                               |
|      67 | TDI                       | 1,8 V MPU       | -           | -           | JTAG-TDI                                   |
|      68 | SPI_ICS_CS                | 1,8 V MPU       | -           | GPIO_38     | MPU-SPI-Chipauswahl                        |
|      69 | TCK                       | 1,8 V MPU       | -           | -           | JTAG-Takt                                  |
|      70 | PM_PS_HOLD_1V8            | 1,8 V MPU       | -           | -           | MPU-Leistungszustandshaltung               |
|      71 | SRST_N                    | 1,8 V MPU       | -           | -           | JTAG-System-Reset                          |
|      72 | FORCED_USB_BOOT_1V8       | 1,8 V MPU       | -           | GPIO_52     | USB-Boot-Modus erzwingen                   |
|      73 | TRST_N                    | 1,8 V MPU       | -           | -           | JTAG-TAP-Reset                             |
|      74 | PWR_EN_N                  | 1,8 V MPU       | -           | -           | Stromversorgung aktivieren (aktiv niedrig) |
|      75 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      76 | USER_BUTTON               | 3,3 V           | -           | GPIO_79     | Tasten-Eingang des Benutzers               |
|      77 | SOM_VREG_S5S_SPX3_1P8     | Stromversorgung | -           | -           | SOM RTSS 1,8-V-Schiene                     |
|      78 | PM_RESIN_N_3V3            | 3,3 V           | -           | -           | MPU-PMIC-Reset-Eingang                     |
|      79 | SOM_VREG_MDPX3_1P8        | Stromversorgung | -           | -           | SOM 1,8-V-Versorgungsspannung              |
|      80 | RTSS_RESIN_N_1V8          | 1,8 V MPU       | -           | -           | RTSS-Reset-Eingang                         |
|      81 | SOM_VREG_MDPX3_1P8        | Stromversorgung | -           | -           | SOM 1,8-V-Versorgungsspannung              |
|      82 | RTSS_PS_HOLD_SPX3_1P8_1V8 | 1,8 V MPU       | -           | -           | RTSS-Stromversorgungs-Hold-Modus           |
|      83 | UART_DBG_TX               | 1,8 V MPU       | -           | GPIO_71     | MPU-Debug-UART-TX                          |
|      84 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      85 | UART_DBG_RX               | 1,8 V MPU       | -           | GPIO_72     | MPU-Debug-UART-Empfang                     |
|      86 | CAN1_TX                   | 3,3 V MCU       | PD5         | -           | CAN-FD-Bus 1, Senden (ohne PHY)            |
|      87 | PWR_DISABLE_7-24V         | System          | -           | -           | Deaktiviert den VIN-Strompfad              |
|      88 | CAN1_RX                   | 3,3 V MCU       | PI9         | -           | CAN-FD-Bus 1 RX (ohne PHY)                 |
|      89 | FORCE_BOOT_3V3            | 3,3 V           | -           | -           | Boot-Übersteuerung erzwingen               |
|      90 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      91 | +3V3 OUT                  | Stromversorgung | -           | -           | 3,3-V-Versorgungsausgang                   |
|      92 | CAN2_TX                   | 3,3 V MCU       | PA10        | -           | CAN-FD-Bus 2 TX (ohne PHY)                 |
|      93 | +3V3 OUT                  | Stromversorgung | -           | -           | 3,3-V-Versorgungsausgang                   |
|      94 | CAN2_RX                   | 3,3 V MCU       | PD9         | -           | CAN-FD-Bus 2 RX (ohne PHY)                 |
|      95 | +3V3 OUT                  | Stromversorgung | -           | -           | 3,3-V-Versorgungsausgang                   |
|      96 | GND                       | Stromversorgung | -           | -           | Masse                                      |
|      97 | +5V OUT                   | Stromversorgung | -           | -           | 5-V-Versorgungsausgang                     |
|      98 | CAN3_TX                   | 3,3 V MCU       | PF6         | -           | CAN-FD-Bus 3 TX (ohne PHY)                 |
|      99 | +5V OUT                   | Stromversorgung | -           | -           | 5-V-Versorgungsausgang                     |
|     100 | CAN3_RX                   | 3,3 V MCU       | PF7         | -           | CAN-FD-Bus 3 RX (ohne PHY)                 |

>📝 **Hinweis:** Die JTAG- und SPI-ICS-Signale liegen im 1,8-V-MPU-Bereich. Bitte legen Sie keine 3,3-V-Logik direkt an. Die CAN-FD-Busse auf dem JOMEGA verfügen über keine physikalische PHY-Schicht; ein externer CAN-Transceiver ist erforderlich. Die VIN-Pins dienen ausschließlich als Stromversorgungseingang.

### MIPI-CSI-Kameraanschlüsse (J3_1, J3_2, J3_3)

VENTUNO Q verfügt über drei unabhängige MIPI-CSI-Kameraanschlüsse (J3_1, J3_2, J3_3), jeweils ein 22-poliger FPC-Stecker (TF31-22S-0,5SH, 0,5-mm-Raster). Jeder unterstützt 4-Lane-MIPI-CSI-2-Kameras. Steuersignale (I2C, GPIO) werden mit **3,3 V** betrieben, sowohl für den Enable-GPIO an Pin 17 als auch für die I2C-Busse an den Pins 20–21. Die I2C-Signale werden intern auf 1,8 V umgewandelt, bevor sie den SoM-Bus `CCI_I2C` erreichen. MIPI-Differenzpaare sind D-PHY und sollten nicht als GPIO verwendet werden.

#### J3_1 – Kamera 2

| **Pin** | **Bezeichnung**     | **Domäne**      | **MPU-Pin** | **Hinweise**                                                |
| ------: | ------------------- | --------------- | ----------- | ----------------------------------------------------------- |
|       1 | GND                 | Stromversorgung | -           | Masse                                                       |
|       2 | LN0_M               | MIPI D-PHY      | -           | CSI2-Datenleitung 0 −                                       |
|       3 | LN0_P               | MIPI D-PHY      | -           | CSI2-Datenleitung 0 +                                       |
|       4 | GND                 | Stromversorgung | -           | Masse                                                       |
|       5 | LN1_M               | MIPI D-PHY      | -           | CSI2-Datenleitung 1 −                                       |
|       6 | LN1_P               | MIPI D-PHY      | -           | CSI2-Datenleitung 1 +                                       |
|       7 | GND                 | Stromversorgung | -           | Masse                                                       |
|       8 | CLK_M               | MIPI D-PHY      | -           | CSI2-Taktleitung −                                          |
|       9 | CLK_P               | MIPI D-PHY      | -           | CSI2-Taktleitung +                                          |
|      10 | GND                 | Stromversorgung | -           | Masse                                                       |
|      11 | LN2_M               | MIPI D-PHY      | -           | CSI2-Datenleitung 2 −                                       |
|      12 | LN2_P               | MIPI D-PHY      | -           | CSI2-Datenleitung 2 +                                       |
|      13 | GND                 | Stromversorgung | -           | Masse                                                       |
|      14 | LN3_M               | MIPI D-PHY      | -           | CSI2-Datenleitung 3 −                                       |
|      15 | LN3_P               | MIPI D-PHY      | -           | CSI2-Datenleitung 3 +                                       |
|      16 | GND                 | Stromversorgung | -           | Masse                                                       |
|      17 | GPIO_PIN17_3V3      | 3,3 V           | GPIO_82     | Kamera-GPIO                                                 |
|      18 | NICHT ANGESCHLOSSEN | -               | -           | -                                                           |
|      19 | GND                 | Stromversorgung | -           | Masse                                                       |
|      20 | SCL                 | 3,3 V           | GPIO_62     | Kamera-I2C-Takt (CCI_I2C4, auf 1,8 V pegelkonvertiert)      |
|      21 | SDA                 | 3,3 V           | GPIO_61     | I2C-Daten der Kamera (CCI_I2C4, auf 1,8 V pegelkonvertiert) |
|      22 | +3V3                | Stromversorgung | -           | 3,3-V-Versorgung für das Kameramodul                        |

#### J3_2 – Kamera 0

| **Pin** | **Bezeichnung**     | **Domäne**      | **MPU-Pin** | **Hinweise**                                                |
| ------: | ------------------- | --------------- | ----------- | ----------------------------------------------------------- |
|       1 | GND                 | Stromversorgung | -           | Masse                                                       |
|       2 | LN0_M               | MIPI D-PHY      | -           | CSI0-Datenleitung 0 −                                       |
|       3 | LN0_P               | MIPI D-PHY      | -           | CSI0-Datenleitung 0 +                                       |
|       4 | GND                 | Stromversorgung | -           | Masse                                                       |
|       5 | LN1_M               | MIPI D-PHY      | -           | CSI0-Datenleitung 1 −                                       |
|       6 | LN1_P               | MIPI D-PHY      | -           | CSI0-Datenleitung 1 +                                       |
|       7 | GND                 | Stromversorgung | -           | Masse                                                       |
|       8 | CLK_M               | MIPI D-PHY      | -           | CSI0-Taktleitung −                                          |
|       9 | CLK_P               | MIPI D-PHY      | -           | CSI0-Taktleitung +                                          |
|      10 | GND                 | Stromversorgung | -           | Masse                                                       |
|      11 | LN2_M               | MIPI D-PHY      | -           | CSI0-Datenleitung 2 −                                       |
|      12 | LN2_P               | MIPI D-PHY      | -           | CSI0-Datenleitung 2 +                                       |
|      13 | GND                 | Stromversorgung | -           | Masse                                                       |
|      14 | LN3_M               | MIPI D-PHY      | -           | CSI0-Datenleitung 3 −                                       |
|      15 | LN3_P               | MIPI D-PHY      | -           | CSI0-Datenleitung 3 +                                       |
|      16 | GND                 | Stromversorgung | -           | Masse                                                       |
|      17 | GPIO_PIN17_3V3      | 3,3 V           | GPIO_64     | Kamera-GPIO                                                 |
|      18 | NICHT ANGESCHLOSSEN | -               | -           | -                                                           |
|      19 | GND                 | Stromversorgung | -           | Masse                                                       |
|      20 | SCL                 | 3,3 V           | GPIO_58     | Kamera-I2C-Takt (CCI_I2C0, auf 1,8 V pegelkonvertiert)      |
|      21 | SDA                 | 3,3 V           | GPIO_57     | I2C-Daten der Kamera (CCI_I2C0, auf 1,8 V pegelkonvertiert) |
|      22 | +3V3                | Stromversorgung | -           | 3,3-V-Versorgung für das Kameramodul                        |

#### J3_3 – Kamera 1

| **Pin** | **Bezeichnung**     | **Domäne**      | **MPU-Pin** | **Hinweise**                                            |
| ------: | ------------------- | --------------- | ----------- | ------------------------------------------------------- |
|       1 | GND                 | Stromversorgung | -           | Masse                                                   |
|       2 | LN0_M               | MIPI D-PHY      | -           | CSI1-Datenleitung 0 −                                   |
|       3 | LN0_P               | MIPI D-PHY      | -           | CSI1-Datenleitung 0 +                                   |
|       4 | GND                 | Stromversorgung | -           | Masse                                                   |
|       5 | LN1_M               | MIPI D-PHY      | -           | CSI1-Datenleitung 1 −                                   |
|       6 | LN1_P               | MIPI D-PHY      | -           | CSI1-Datenleitung 1 +                                   |
|       7 | GND                 | Stromversorgung | -           | Masse                                                   |
|       8 | CLK_M               | MIPI D-PHY      | -           | CSI1-Taktleitung −                                      |
|       9 | CLK_P               | MIPI D-PHY      | -           | CSI1-Taktleitung +                                      |
|      10 | GND                 | Stromversorgung | -           | Masse                                                   |
|      11 | LN2_M               | MIPI D-PHY      | -           | CSI1-Datenleitung 2 −                                   |
|      12 | LN2_P               | MIPI D-PHY      | -           | CSI1-Datenleitung 2 +                                   |
|      13 | GND                 | Stromversorgung | -           | Masse                                                   |
|      14 | LN3_M               | MIPI D-PHY      | -           | CSI1-Datenleitung 3 −                                   |
|      15 | LN3_P               | MIPI D-PHY      | -           | CSI1-Datenleitung 3 +                                   |
|      16 | GND                 | Stromversorgung | -           | Masse                                                   |
|      17 | GPIO_PIN17_3V3      | 3,3 V           | GPIO_75     | Kamera-GPIO                                             |
|      18 | NICHT ANGESCHLOSSEN | -               | -           | -                                                       |
|      19 | GND                 | Stromversorgung | -           | Masse                                                   |
|      20 | SCL                 | 3,3 V           | GPIO_60     | Kamera-I2C-Takt (CCI_I2C2, auf 1,8 V pegelkonvertiert)  |
|      21 | SDA                 | 3,3 V           | GPIO_59     | Kamera-I2C-Daten (CCI_I2C2, auf 1,8 V pegelkonvertiert) |
|      22 | +3V3                | Stromversorgung | -           | 3,3-V-Versorgung für das Kameramodul                    |

>📝 **Hinweis:** Die differentiellen MIPI-D-PHY-Leitungen sind keine universellen Ein-/Ausgänge.

## Hochgeschwindigkeits-Peripheriegeräte

### Netzwerk

Tri-Band-Wi-Fi® 6 (2,4/5/6 GHz) und Bluetooth® 5.3 über das integrierte Modul NFA725B. Kabelgebundene Konnektivität über 2,5 Gbit/s RJ45-Ethernet (QCA-8081 PHY).

### Speicher

Erweiterbarer NVMe-Gen-4-Speicher über einen M.2-2230-Key-M-Anschluss (MDT580M01001), der über eine 4-Lane-PCIe-Gen-4-Schnittstelle direkt mit dem QCS8275-SOM verbunden ist. Der M.2-Steckplatz ist gemäß der QCS8275-Spezifikation nicht bootfähig. Die Stromversorgung des Steckplatzes wird unabhängig über einen von der MPU gesteuerten MP5077GG-Z-Lastschalter geschaltet.

Der mit dem Board integrierte PCIe-Gen-2-Paket-Switch PI7C9X2G304EV ist ausschließlich für den USB-3.0-xHCI-Host-Controller (TUSB7340RKMR) und das Wi-Fi®-Modul (NFA725B) vorgesehen.

> 📝 **Hinweis:** Die MPU steuert die Stromversorgung des M.2-Steckplatzes. Wenn die MPU den Bootvorgang noch nicht abgeschlossen hat oder die Stromversorgungssteuerung nicht aktiviert wurde, erhält ein installiertes NVMe-Laufwerk keine Stromversorgung und wird nicht erkannt. Dies ist ein erwartetes Verhalten während der frühen Bootphase.

### USB-C

Der USB-C-Anschluss unterstützt den Wechsel zwischen Host- und Gerätefunktion, den Wechsel der Stromversorgungsfunktion, die Ausgabe im DisplayPort-Alt-Mode sowie die USB-Power-Delivery-Aushandlung bis zu 20 V über den PD-Controller CYPD6129-52LQXI. Die SuperSpeed-Differenzpaare am USB-C-Anschluss werden über den integrierten USB-eDP-MUX (TMUXHS4446RETT) gemeinsam von USB 3.0 SuperSpeed-Daten und dem DisplayPort-Alt-Mode genutzt.

**Wenn der DisplayPort-Alt-Mode aktiv ist**, werden die SuperSpeed-Lanes dem DisplayPort zugewiesen. USB-Daten werden dann ausschließlich auf dem HS_D+/D−-Paar auf USB-2.0-Geschwindigkeiten (HighSpeed, 480 Mbit/s) begrenzt. Die volle USB-3.0-SuperSpeed-Datenübertragung ist nur verfügbar, wenn der DisplayPort-Alt-Mode nicht aktiv ist.

Der CYPD6129 überwacht sowohl VBUS als auch VIN, um den Stromversorgungszustand des Boards zu ermitteln, und handelt entsprechend PD-Profile aus. Die Fehler-LED (rot, GPIO9/P4.1 am CYPD6129) zeigt Fehlerzustände an. Die wichtigsten Stromversorgungsszenarien sind im Folgenden zusammengefasst:

| **Szenario**                                                                                                  | **Erwartetes Ergebnis**                                                                        |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| VIN angeschlossen, USB nicht angeschlossen                                                                    | System wird über VIN mit Strom versorgt, PD-Controller im Batteriemodus                        |
| VIN angeschlossen, USB angeschlossen                                                                          | System wird über VIN mit Strom versorgt, PD-Aushandlung und Datenübertragung sind zulässig     |
| VIN nicht angeschlossen, USB-C zu USB-C                                                                       | System wird über VBUS mit Strom versorgt, PD-Aushandlung beginnt, Zielwert 20 V bei 3 A        |
| VIN nicht angeschlossen, USB-C an USB-A                                                                       | PD erkennt eine Nicht-PD-Quelle, System ausgeschaltet, Fehler-LED blinkt                       |
| VIN nicht angeschlossen, USB-C an USB-A -> VIN wird während des Betriebs angeschlossen                        | PD erkennt VIN, schaltet VIN frei, hält VBUS gesperrt                                          |
| VIN nicht angeschlossen, USB-C an USB-C (Leistung ausgehandelt) → VIN wird während des Betriebs angeschlossen | System wird über VBUS mit Strom versorgt, VIN gesperrt, Fehler-LED zeigt ein anderes Muster an |

>📝 **Hinweis:** Der CYPD6129 ist so programmiert, dass er ein PD-Spannungsprofil von über 5 V benötigt, bevor der Hauptstrompfad freigegeben wird. Der Anschluss über ein Standard-USB-C-zu-USB-A-Kabel oder einen USB-C-Anschluss, der ohne PD-Aushandlung nur 5 V liefert, versorgt das Board nicht mit Strom und führt dazu, dass die Fehler-LED blinkt. Verwenden Sie für einen zuverlässigen Betrieb über USB-C stets ein PD-fähiges USB-C-Netzteil, das 9 V, 15 V oder 20 V unterstützt.
>
> Der CYPD6129 wird stets über einen eigenen Buck-Wandler (LMR51440SDRRR, U26) mit Strom versorgt, der von einer beliebigen angeschlossenen Stromquelle gespeist wird. So kann er die Stromversorgung eigenständig überwachen und aushandeln, bevor er den Strompfad zum Hauptboard freigibt.

### USB Typ A

Beide USB-3.0-Typ-A-Anschlüsse sind unabhängig voneinander durch dedizierte Lastschalter (MP5077GG-Z) geschützt. Der VBUS jedes Anschlusses ist durch das ILIM-Widerstandsnetzwerk fest auf 1,71 A begrenzt. Die Stromfreigabe für jeden Anschluss wird vom TUSB7340RKMR verwaltet.

| **Parameter**                                | **Wert**                                      |
| -------------------------------------------- | --------------------------------------------- |
| VBUS-Spannung                                | 5 V                                           |
| Maximaler Wert der Stromstärke pro Anschluss | 1,71 A (durch ILIM festgelegt, pro Anschluss) |
| Schutz                                       | MP5077GG-Z-Lastschalter                       |
| Freigabesteuerung                            | TUSB7340RKMR                                  |

>📝 **Hinweis:** Die Stromstärke von 1,71 A pro Port ist hardwaremäßig festgelegt und kann nicht softwaremäßig außer Kraft gesetzt werden. Versuchen Sie nicht, den Lastschalter zu umgehen.

### Anzeige

Mit dem Board werden die folgenden Anzeigeausgänge geboten:

- **HDMI** über den dedizierten HDMI-Anschluss, angesteuert durch die integrierte ADV7535-DSI-zu-HDMI-Brücke. Der ADV7535 nutzt die MIPI-DSI-Leitungen vom SoM. Wenn HDMI aktiv ist, stehen die MIPI-DSI-Leitungen am JMEDIA-Header nicht zur Verfügung.
- **DisplayPort Alt Mode** über den USB-C-Anschluss mittels des integrierten USB-eDP-MUX (TMUXHS4446RETT).
- **MIPI DSI auf JMEDIA** verfügbar, wenn der HDMI-Ausgang nicht aktiv ist (erfordert eine DSI-Overlay-Konfiguration).

### Kamera

VENTUNO Q unterstützt den Kameraeingang über drei integrierte MIPI-CSI-Anschlüsse (J3_1, J3_2, J3_3) sowie über den JMEDIA-Carrier-Header.

**VENTUNO Q im Standalone-Betrieb (Standard):**

Alle drei integrierten CSI-Anschlüsse (J3_1, J3_2, J3_3) stehen gleichzeitig für den Kameraeingang zur Verfügung. Hierbei handelt es sich um eine reine Kamerakonfiguration, und MIPI DSI ist standardmäßig nicht aktiv. Die Bildschirausgabe erfolgt über den HDMI-Anschluss oder den USB-C-DisplayPort-Alt-Modus.

>📝 **Hinweis:** Das [Arducam IMX577 Mini-Kameramodul](https://www.arducam.com/arducam-imx577-mini-camera-module-for-qualcomm-rb3g2.html) (Artikelnummer B0488) ist über seine integrierten MIPI-CSI-Anschlüsse mit dem VENTUNO Q kompatibel. Anweisungen zum Testen und zur Konfiguration finden Sie im [VENTUNO Q-Benutzerhandbuch](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

**VENTUNO Q mit einem kompatiblen Carrier:**

Ein an JMEDIA angeschlossene Carrier-Board ermöglicht neben den integrierten Kameras den Anschluss eines MIPI-DSI-Displays. Ist das DSI-Overlay der Carrier aktiviert, steht Kamera 0 (J3_2) nicht zur Verfügung, da sie sich den CCI_I2C0-Bus (GPIO_57/58) mit dem JMEDIA-Header teilt. Die Kameras 1 (J3_3) und 2 (J3_1) bleiben verfügbar.

>📝 **Hinweis:** Die Verfügbarkeit der Kameras bei angeschlossenem Carrier hängt von der jeweiligen Konfiguration des Carriers ab. Einzelheiten entnehmen Sie bitte der Dokumentation des jeweiligen Carriers.

<div style="page-break-after: always;"></div>

## Bedienung des Geräts

### Erste Schritte – Arduino App Lab

Arduino App Lab [1] ist ein einheitlicher Editor, mit dem Projekte auf beiden Prozessoren des VENTUNO Q erstellt und ausgeführt werden können. Er vereint Embedded-Programmierung (Sketches), Linux-Entwicklung und Edge-AI in einer einzigen Umgebung.

Ein Projekt ist eine **App**, die Folgendes umfassen kann:

- Ein Python®-Programm, das auf dem Linux-System (Qualcomm Dragonwing™ IQ8) ausgeführt wird
- Einen Arduino-Sketch, der auf dem Mikrocontroller (STM32H5F5) ausgeführt wird
- Optionale **Bricks** (vorkonfigurierte Dienste wie AI-Modelle, Webserver oder API-Clients), die zusammen mit der App bereitgestellt werden und auf dem Linux-System laufen.

Apps nutzen **Bridge**, um Daten zwischen der Linux-Seite und dem Mikrocontroller auszutauschen.

**Drei Konfigurationen. Ein Erlebnis.**

![](assets/ABX00181_modes.png)

- **Single-Board-Computer-Modus:** App Lab läuft direkt auf dem VENTUNO Q. Schließen Sie einen Monitor über HDMI (oder USB-C), eine Tastatur und eine Maus an, um eine All-in-One-Entwicklungsumgebung zu erhalten. Es wird kein PC benötigt.
- **PC-Hosted-Modus:** Verbinden Sie den VENTUNO Q über USB-C oder das Netzwerk mit Ihrem Computer und führen Sie App Lab auf Ihrem PC aus.
- **Netzwerkmodus:** VENTUNO Q läuft headless ohne Bildschirm, Tastatur oder Maus. Greifen Sie über Wi-Fi® oder Ethernet remote auf das Board zu.

>📝 **Hinweis:** Im **PC-Hosted-Modus** ist für die erste Konfiguration eine USB-Datenverbindung erforderlich. Danach können Sie das **Netzwerk**-Ziel über LAN (SSH) nutzen.

Im **Single-Board-Computer**-Modus ist keine USB-Datenverbindung erforderlich. Schalten Sie das Board ein und nutzen Sie das **Netzwerk**-Ziel, sobald es sich in Ihr Netzwerk eingekoppelt hat. USB-Peripheriegeräte (Tastatur, Maus, USB-Kamera, Mikrofon) können direkt an die integrierten USB-A-Anschlüsse angeschlossen werden. Wenn der DisplayPort-Alt-Modus am USB-C-Anschluss aktiv ist, wird die USB-Datenübertragungsrate reduziert.

Ausführliche Anweisungen zur Konfiguration, Erstkonfiguration und Anleitung zur ersten Inbetriebnahme finden Sie im [VENTUNO Q-Benutzerhandbuch](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Hinweis:** Wenn Sie das Board zum ersten Mal über USB-C mit Strom versorgen, blinkt die Fehler-LED möglicherweise, wenn es an einen Computer oder einen nicht-PD-fähigen USB-C-Anschluss angeschlossen wird. Das Board benötigt zum Starten eine PD-fähige Stromversorgung von mindestens 9 V. Für den Betrieb mit voller Leistung, einschließlich AI-Inferenz, angeschlossener Peripheriegeräte und montierter HATs, wird eine Versorgungsspannung von 12 V oder höher empfohlen, entweder über USB-C PD (bis zu 20 V) oder über die Rundsteckerbuchse bzw. die Schraubklemmen (7–24 V). Informationen zu den Spannungs- und Stromstärke-Grenzen pro Stromquelle finden Sie im Abschnitt [Eingangsspannung](#eingangsleistung).

>📝 **Hinweis:** Der erste Startvorgang dauert 20–30 Sekunden, während Linux hochfährt. Die LED-Matrix zeigt eine Startanimation an, sobald der MCU-Bootloader geladen ist und ein gültiger Sketch ausgeführt wird. Warten Sie, bis dieser Vorgang abgeschlossen ist, bevor Sie mit dem Board interagieren. Sollte die Animation nicht erscheinen, finden Sie weitere Informationen im [VENTUNO Q-Benutzerhandbuch](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

### Bricks

„Bricks“ sind vorgefertigte Bausteine im Arduino App Lab, darunter AI-Modelle, Webdienste, Sensorintegrationen, Datenbanken und Benutzeroberflächen, die auf der Linux-Seite zusammen mit Ihrer App bereitgestellt werden, ohne dass Sie die zugrunde liegende Infrastruktur selbst programmieren müssen. Eine vollständige Anleitung zur Auswahl und Verwendung von „Bricks“ finden Sie im [VENTUNO Q-Benutzerhandbuch](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Hinweis:** Während eine App gebunden ist und ausgeführt wird, können USB-Schnittstellen vom System belegt sein. Um externe CLI-Tools über USB zu verwenden, beenden Sie die App oder trennen Sie die Verbindung mit dem Board.

### Tasten & Startmodi

VENTUNO Q verfügt über zwei integrierte Tasten: einen **vertikalen Taster** und eine **Benutzertaste**.

![](assets/ABX00181_vertical_button.png)

### Vertikaler Taster

Der vertikale Taster ist mit dem MCU-GPIO-Pin PK13 verbunden. Er kann zur Interaktion mit dem Board und zum Herunterfahren des Boards verwendet werden.

- **Einmaliges Drücken (Single-Board-Computer-Modus):** Löst einen Herunterfahrdialog auf dem Bildschirm aus. Der Benutzer kann bestätigen, um das Gerät sofort auszuschalten, oder „Abbrechen“ wählen, um den Dialog zu schließen und den normalen Betrieb fortzusetzen. Wenn keine Interaktion erfolgt, schaltet sich das Board nach 60 Sekunden automatisch aus.
- **Langes Drücken (10+ Sekunden, SSH-/ADB-Modus):** Das System wird vollständig heruntergefahren. Das Board bleibt ausgeschaltet, bis die Stromversorgung unterbrochen und wiederhergestellt wird.

>📝 **Hinweis:** Ein Herunterfahren durch langes Drücken beendet die Linux-Umgebung vollständig und unterbricht alle laufenden Anwendungen. Speichern Sie Ihre Arbeit und stellen Sie sicher, dass externe Prozesse gegebenenfalls sicher beendet werden. Das Board startet automatisch, sobald es mit Strom versorgt wird; das Drücken des Tasters ist für einen normalen Start nicht erforderlich.

### Benutzer-Taste

![](assets/ABX00181_user_button.png)

Die Benutzertaste ist mit der MPU (GPIO_79) verbunden und steht als universeller Eingang zur Verfügung. Sie kann von Linux-Anwendungen und -Skripten über Standard-GPIO-Schnittstellen ausgelesen werden. Anwendungsbeispiele finden Sie im [VENTUNO Q-Benutzerhandbuch](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

<div style="page-break-after: always;"></div>

## Mechanische Angaben

Das Board misst 160 mm × 100 mm. Die Gesamthöhe ohne SoM-Kühlkörper und Lüfter beträgt 25,8 mm. Der 40-polige JHAT-Steckverbinder entspricht der mechanischen Standardspezifikation für Raspberry Pi® HATs und gewährleistet somit die physikalische Kompatibilität mit konformem HAT-Zubehör.

![](assets/ABX00181_general_dimensions.svg)

Die UNO-Shield-Anschlüsse behalten den Standard-Abstand der Arduino-UNO-Baugröße bei, was eine direkte mechanische und elektrische Kompatibilität mit dem UNO-Shield-Ökosystem ermöglicht.

Mit dem Board verfügt man über drei Lochreihen, die unterschiedlichen mechanischen Zwecken dienen:

- **4× M2,5-Abstandshalter** (5 mm Höhe, mit dem Board gelötet) zur Befestigung des Kühlkörpers, angeordnet 9,78 mm vom rechten Rand sowie 10,02 mm und 42,63 mm vom oberen Rand entfernt.
- **4× 3,2 mm** Befestigungslöcher an den Ecken für den Einbau in Gehäuse, auf Schalttafeln oder auf kundenspezifischen Carrier und Zubehörteilen.
- **2× 3,2 mm** HAT-Befestigungslöcher gemäß der mechanischen Standardspezifikation für Raspberry Pi® HAT, kompatibel mit M3-Abstandshaltern zur Befestigung von HAT-Zubehör.
- **1× M2-Abstandshalter** (4 mm Höhe) zur Befestigung einer M.2 2230 NVMe-Speicherkarte im M.2-Steckplatz.

VENTUNO Q wird mit 4× M3-Sechskant-Abstandshaltern und 4× M3-Muttern geliefert, die in einem separaten Beutel enthalten sind. In ESD-empfindlichen Umgebungen befestigen Sie bitte jeweils einen Abstandshalter und eine Mutter an jeder der vier Eckbefestigungslöcher, um das Board von der Arbeitsfläche abzuheben und den Abstand zu vergrößern.

| **Artikel**                 | **Abmessungen**                                                  |
| --------------------------- | ---------------------------------------------------------------- |
| M3-Sechskant-Abstandshalter | Sechskantlänge 20 mm, Gewindelänge 6 mm, Gewindedurchmesser 3 mm |
| M3-Mutter                   | Höhe 2,4 mm, Sechskant-Flachmaß 5,6 mm, Innendurchmesser 3 mm    |

![](assets/ABX00181_esd_standoff.png)

### SoM-Kühlkörper und thermisches Design

Das Qualcomm® Dragonwing™ IQ8 (QCS8275) SoM erfordert eine aktive Kühlung für den dauerhaften Betrieb bei voller Leistung. Die SoM-Grundfläche mit dem Board misst **57,5 mm × 57,5 mm**, zentriert bei **14,26 mm** vom linken Rand und **14,73 mm** vom unteren Rand entfernt, mit einem horizontalen Versatz von **8,95 mm** und einem vertikalen Versatz von **8,55 mm** zum aktiven Bereich des SoM.

![](assets/ABX00181_active_fan.png)

Die vier M2,5-Abstandshalter definieren das Befestigungsmuster für die mitgelieferte Kühlkörper- und Lüfterbaugruppe, die symmetrisch um die SoM-Grundfläche angeordnet ist, um eine gleichmäßige Klemmkraft über den gesamten SoM-Deckel zu gewährleisten.

Unter Worst-Case-Bedingungen, bei denen MPU, NPU und GPU gleichzeitig mit voller Leistung laufen, kann das Board etwa 25 W oder mehr aufnehmen. Die mitgelieferte aktive Kühllösung ist für diese thermische Belastung optimiert. Stellen Sie sicher, dass der Lüfter während anhaltender Hochleistungs-Workloads betriebsbereit bleibt.

![](assets/ABX00181_som_heatsink.svg)

>📝 **Hinweis:** Der Betrieb des Boards unter hoher AI- oder Rechenlast ohne ausreichende Kühlung kann zu einer thermischen Drosselung des QCS8275-SoM führen, wodurch die Leistung beeinträchtigt wird. Überprüfen Sie stets den thermischen Spielraum für Ihren jeweiligen Anwendungsfall und die Gehäuseumgebung.

<div style="page-break-after: always;"></div>

# Safety Information

Maintain a minimum separation distance of 20 cm between the device and the user during operation. The 5 GHz frequency band may be subject to operational restrictions depending on the country of use.

**Bulgarian (BG):**

Поддържайте минимално разстояние от 20 см между устройството и потребителя по време на работа.
Честотната лента 5 GHz може да бъде обект на ограничения за използване в зависимост от държавата.

**Croatian (HR):**

Održavajte minimalnu udaljenost od 20 cm između uređaja i korisnika tijekom rada.
Frekvencijski pojas od 5 GHz može podlijegati ograničenjima ovisno o zemlji uporabe.

**Czech (CS):**

Udržujte minimální vzdálenost 20 cm mezi zařízením a uživatelem během provozu.
Pásmo 5 GHz může podléhat provozním omezením v závislosti na zemi použití.

**Danish (DA):**

Oprethold en minimumsafstand på 20 cm mellem enheden og brugeren under drift.
5 GHz-båndet kan være underlagt driftsmæssige begrænsninger afhængigt af brugslandet.

**Dutch (NL):**

Houd tijdens gebruik een minimale afstand van 20 cm tussen het apparaat en de gebruiker aan.
De 5GHz-band kan onderhevig zijn aan gebruiksbeperkingen afhankelijk van het land van gebruik.

**Estonian (ET):**

Hoidke seadme ja kasutaja vahel töötamise ajal vähemalt 20 cm kaugust.
5 GHz sagedusribale võivad kehtida kasutuspiirangud sõltuvalt kasutusriigist.

**Finnish (FI):**

Pidä laitteen ja käyttäjän välillä vähintään 20 cm etäisyys käytön aikana.
5 GHz taajuuskaistaan voi kohdistua käyttörajoituksia käyttömaasta riippuen.

**French (FR):**

Maintenez une distance minimale de 20 cm entre l’appareil et l’utilisateur pendant son fonctionnement.
La bande de fréquences 5 GHz peut être soumise à des restrictions d’utilisation selon le pays.

**German (DE):**

Halten Sie während des Betriebs einen Mindestabstand von 20 cm zwischen dem Gerät und dem Benutzer ein.
Das 5‑GHz‑Frequenzband kann je nach Einsatzland Nutzungsbeschränkungen unterliegen.

**Greek (EL):**

Διατηρείτε ελάχιστη απόσταση 20 cm μεταξύ της συσκευής και του χρήστη κατά τη λειτουργία.
Η ζώνη συχνοτήτων 5 GHz ενδέχεται να υπόκειται σε περιορισμούς ανάλογα με τη χώρα χρήσης.

**Hungarian (HU):**

A működés során tartson legalább 20 cm távolságot az eszköz és a felhasználó között.
Az 5 GHz-es frekvenciasáv használata országtól függően korlátozott lehet.

**Irish (GA):**

Coinnigh ar a laghad fad 20 cm idir an gléas agus an t‑úsáideoir le linn úsáide.
D’fhéadfadh srianta oibriúcháin a bheith ar an mbanda minicíochta 5 GHz ag brath ar an tír.

**Italian (IT):**

Mantenere una distanza minima di 20 cm tra il dispositivo e l’utente durante il funzionamento.
La banda di frequenza a 5 GHz può essere soggetta a restrizioni operative a seconda del paese.

**Latvian (LV):**

Uzturiet vismaz 20 cm attālumu starp ierīci un lietotāju darbības laikā.
5 GHz frekvenču joslai var būt izmantošanas ierobežojumi atkarībā no valsts.

**Lithuanian (LT):**

Naudojimo metu laikykite bent 20 cm atstumą tarp įrenginio ir naudotojo.
5 GHz dažnių juostai gali būti taikomi naudojimo apribojimai priklausomai nuo šalies.

**Maltese (MT):**

Żomm distanza minima ta’ 20 cm bejn l-apparat u l-utent waqt l-użu.
Il-medda tal-frekwenza 5 GHz tista’ tkun soġġetta għal restrizzjonijiet skont il-pajjiż.

**Polish (PL):**

Podczas pracy zachowaj minimalną odległość 20 cm między urządzeniem a użytkownikiem.
Pasmo częstotliwości 5 GHz może podlegać ograniczeniom w zależności od kraju użytkowania.

**Portuguese (PT):**

Mantenha uma distância mínima de 20 cm entre o dispositivo e o utilizador durante o funcionamento.
A banda de frequência de 5 GHz pode estar sujeita a restrições de utilização dependendo do país.

**Romanian (RO):**

Mențineți o distanță minimă de 20 cm între dispozitiv și utilizator în timpul funcționării.
Banda de frecvență de 5 GHz poate face obiectul unor restricții în funcție de țara de utilizare.

**Slovak (SK):**

Počas prevádzky dodržiavajte minimálnu vzdialenosť 20 cm medzi zariadením a používateľom.
Pásmo 5 GHz môže podliehať prevádzkovým obmedzeniam v závislosti od krajiny použitia.

**Slovenian (SL):**

Med delovanjem ohranjajte najmanj 20 cm razdalje med napravo in uporabnikom.
Pas frekvenc 5 GHz je lahko omejen glede na državo uporabe.

**Spanish (ES):**

Mantenga una distancia mínima de 20 cm entre el dispositivo y el usuario durante su funcionamiento.
La banda de frecuencia de 5 GHz puede estar sujeta a restricciones según el país de uso.

**Swedish (SV):**

Håll ett minsta avstånd på 20 cm mellan enheten och användaren under drift.
5 GHz-bandet kan vara föremål för driftbegränsningar beroende på användningsland.

## ESD Warning

This product is a development board that contains ESD-sensitive components. Appropriate anti-static precautions should be taken when handling the device. Avoid touching exposed connectors, pins, or circuitry. Where a heatsink is installed, handle the board by the heatsink to minimise the risk of electrostatic discharge damage. Improper handling or exposure to electrostatic discharge may result in permanent damage to the product.

## Antenna Use and Compliance

- This product is approved to operate with the built-in (internal) antenna only
- The internal antenna is part of the certified module configuration and must be used for normal operation
- RF connectors may be present for development or testing purposes only
- Use of an external antenna is not part of the approved configuration
- External antenna use requires additional regulatory assessment before use

### Warning - External Antenna Use

- Connecting an external antenna may result in non-compliance with regulatory requirements
- This includes the module approval associated with FCC ID J9C-QCNFA725
- Use of an external antenna may change RF output power
- Use of an external antenna may change frequency behavior
- Use of an external antenna may change radiation characteristics
- These changes may cause the product to exceed allowed regulatory limits
- Use of an external antenna may invalidate device approval
- Use of an external antenna may void the authorization to operate the device
- Unauthorized changes, including antenna modifications, may void regulatory approvals

### Requirements for Integrators

- End products must use the internal antenna to maintain regulatory compliance
- If an external antenna is used, the integrator must perform a full regulatory assessment
- If an external antenna is used, the integrator must obtain required certifications for the final product
- Any antenna used must meet the approved gain, radiation pattern, and performance characteristics
- Approved antenna characteristics are defined in the applicable regulatory documentation, including the Qualcomm module label guide

### Operation in the 6 GHz Band

- Operation in the 6 GHz band is only permitted with the approved internal antenna configuration
- If an external antenna is used, 6 GHz operation must be disabled
- If an external antenna is used, the product must not transmit in the 6 GHz band
- Operation outside the approved configuration may violate regional regulations

### Responsibility

- The manufacturer or integrator is responsible for ensuring the final product complies with all applicable regulatory requirements
- Changes to the antenna system or RF design may require additional testing and certification

# Certifications

## RED / UK

| CE                     | Europe - EU Declaration of Conformity                                                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Česky [Czech]          | Arduino S.r.l tímto prohlašuje, že tento Radiolan je ve shodě se základními požadavky a dalšími příslušnými ustanoveními směrnice 2014/53/EU.                                                    |
| Dansk [Danish]         | Undertegnede Arduino S.r.l erklærer herved, at følgende udstyr Radiolan overholder de væsentlige krav og øvrige relevante krav i direktiv 2014/53/EU.                                            |
| Deutsch [German]       | Hiermit erklärt Arduino S.r.l dass sich das Gerät Radiolan in Übereinstimmung mit den grundlegenden Anforderungen und den übrigen einschlägigen Bestimmungen der Richtlinie 2014/53/EU befindet. |
| Eesti [Estonian]       | Käesolevaga kinnitab Arduino S.r.l seadme Radiolan vastavust direktiivi 2014/53/EU põhinõuetele ja nimetatud direktiivist tulenevatele teistele asjakohastele sätetele.                          |
| English                | Hereby, Arduino S.r.l, declares that this Radiolan is in compliance with the essential requirements and other relevant provisions of Directive 2014/53/EU.                                       |
| Español [Spanish]      | Por medio de la presente Arduino S.r.l declara que el Radiolan cumple con los requisitos esenciales y cualesquiera otras disposiciones aplicables o exigibles de la Directiva 2014/53/EU.        |
| Ελληνική [Greek]       | ΜΕ ΤΗΝ ΠΑΡΟΥΣΑ Arduino S.r.l ΔΗΛΩΝΕΙ ΟΤΙ Radiolan ΣΥΜΜΟΡΦΩΝΕΤΑΙ ΠΡΟΣ ΤΙΣ ΟΥΣΙΩΔΕΙΣ ΑΠΑΙΤΗΣΕΙΣ ΚΑΙ ΤΙΣ ΛΟΙΠΕΣ ΣΧΕΤΙΚΕΣ ΔΙΑΤΑΞΕΙΣ ΤΗΣ ΟΔΗΓΙΑΣ 2014/53/EU.                                          |
| Français [French]      | Par la présente Arduino S.r.l déclare que l'appareil Radiolan est conforme aux exigences essentielles et aux autres dispositions pertinentes de la directive 2014/53/EU.                         |
| Íslenska [Icelandic]   | Hér með lýsir Arduino S.r.l yfir því að Radiolan er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU.                                                            |
| Italiano [Italian]     | Con la presente Arduino S.r.l dichiara che questo Radiolan è conforme ai requisiti essenziali ed alle altre disposizioni pertinenti stabilite dalla direttiva 2014/53/EU.                        |
| Latviski [Latvian]     | Ar šo Arduino S.r.l deklarē, ka Radiolan atbilst Direktīvas 2014/53/EU būtiskajām prasībām un citiem ar to saistītajiem noteikumiem.                                                             |
| Lietuvių [Lithuanian]  | Šiuo Arduino S.r.l deklaruoja, kad šis Radiolan atitinka esminius reikalavimus ir kitas 2014/53/EU Direktyvos nuostatas.                                                                         |
| Malti [Maltese]        | Hawnhekk, Arduino S.r.l, jiddikjara li dan Radiolan jikkonforma mal-ħtiġijiet essenzjali u ma provvedimenti oħrajn relevanti li hemm fid-Dirrettiva 2014/53/EU.                                  |
| Magyar [Hungarian]     | Alulírott, Arduino S.r.l nyilatkozom, hogy a Radiolan megfelel a vonatkozó alapvetõ követelményeknek és az 2014/53/EU irányelv egyéb elõírásainak.                                               |
| Nederlands [Dutch]     | Hierbij verklaart Arduino S.r.l dat het toestel Radiolan in overeenstemming is met de essentiële eisen en de andere relevante bepalingen van richtlijn 2014/53/EU.                               |
| Norsk [Norwegian]      | Arduino S.r.l erklærer herved at utstyret Radiolan er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU.                                                        |
| Polski [Polish]        | Niniejszym Arduino S.r.l oświadcza, że Radiolan jest zgodny z zasadniczymi wymogami oraz pozostałymi stosownymi postanowieniami Dyrektywy 2014/53/EU.                                            |
| Português [Portuguese] | Arduino S.r.l declara que este Radiolan está conforme com os requisitos essenciais e outras disposições da Directiva 2014/53/EU.                                                                 |
| Slovensko [Slovenian]  | Arduino S.r.l izjavlja, da je ta Radiolan v skladu z bistvenimi zahtevami in ostalimi relevantnimi določili direktive 2014/53/EU.                                                                |
| Slovensky [Slovak]     | Arduino S.r.l týmto vyhlasuje, že Radiolan spĺňa základné požiadavky a všetky príslušné ustanovenia Smernice 2014/53/EU.                                                                         |
| Suomi [Finnish]        | Arduino S.r.l vakuuttaa täten että Radiolan tyyppinen laite on direktiivin 2014/53/EU oleellisten vaatimusten ja sitä koskevien direktiivin muiden ehtojen mukainen.                             |
| Svenska [Swedish]      | Härmed intygar Arduino S.r.l att denna Radiolan står I överensstämmelse med de väsentliga egenskapskrav och övriga relevanta bestämmelser som framgår av direktiv 2014/53/EU.                    |
| **UK**                 | **United Kingdom - UKCA Declaration of Conformity**                                                                                                                                              |
| United Kingdom         | Hereby, Arduino S.r.l, declares that this Radiolan is in compliance with the essential requirements and other relevant provisions of The Radio Equipment Regulations 2017.                       |

The full text of the EU and UKCA declaration of conformity is available at the following internet address: <https://docs.arduino.cc/certifications>

The product complies with the requirements of the RoHS Directive (2011/65/EU and 2015/863/EU) and the REACH Regulation (EC) 1907/2006. A copy of the compliance documentation is available at: <https://docs.arduino.cc/certifications>

Requirements in:

Belgium (BE), Bulgaria (BG), Czech Republic (CZ), Denmark (DK), Germany (DE), Iceland (IS), Estonia (EE), Ireland (IE), Greece (EL), Spain (ES), France (FR), Croatia (HR), Italy (IT), Cyprus (CY), Latvia (LV), Liechtenstein (LI), Lithuania (LT), Luxembourg (LU), Hungary (HU), Malta (MT), Netherlands (NL), Norway (NO), Austria (AT), Poland (PL), Portugal (PT), Romania (RO), Slovenia (SI), Slovakia (SK), Turkey (TR), Finland (FI), Sweden (SE), Switzerland (CH), United Kingdom (North Irland) (UK(NI)), and United Kingdom (UK).

Operations in the 5.15-5.35GHz band are restricted to indoor usage only.

For Low power indoor (LPI use): Operations in the 5955 - 6415MHz are restricted to indoor usage only.

This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

### Radio Equipment Information (RED Compliance)

This radio equipment operates in the following frequency bands and with the maximum radio-frequency power indicated below:

| **Radio Technology**                | **Frequency Band** | **Maximum Transmit Power** |
|-------------------------------------|--------------------|----------------------------|
| Bluetooth® EDR                      | 2400 - 2483.5 MHz  | 18.31 dBm                  |
| Bluetooth® LE                       | 2400 - 2483.5 MHz  | 9.97 dBm                   |
| Wi-Fi® 2.4 GHz                      | 2400 - 2483.5 MHz  | 19.91 dBm EIRP             |
| Wi-Fi® 5 GHz                        | 5150 - 5350 MHz    | 22.92 dBm EIRP             |
| Wi-Fi® 5 GHz                        | 5470 - 5725 MHz    | 22.97 dBm EIRP             |
| Wi-Fi® 5 GHz                        | 5725 - 5850 MHz    | 13.84 dBm EIRP             |
| Wi-Fi® 6 GHz (LPI client)           | 5945 - 6425 MHz    | 22.83 dBm EIRP             |
| Wi-Fi® 6 GHz (VLP)                  | 5945 - 6425 MHz    | 13.77 dBm EIRP             |

In accordance with EU regulations (RED Directive 2014/53/EU), the use of the 5 GHz band may be subject to national restrictions.

## UKCA Declaration of Conformity

Arduino S.r.l. hereby declares that this product is in compliance with the essential requirements and other relevant provisions of the applicable UK regulations. A copy of the UK Declaration of Conformity is available at: <https://docs.arduino.cc/certifications>

## FCC

Contains FCC ID: J9C-QCNFA725

**FCC compliance information**

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

This product does not contain any user serviceable components. Any unauthorized product changes or modifications will invalidate warranty and all applicable regulatory certifications and approvals, including authority to operate this device.

**FCC Part 15 Digital Emissions Compliance**

We Arduino S.r.l. - Via Andrea Appiani 25, 20900 Monza (Italy), declare under our sole responsibility that the product Arduino® VENTUNO Q complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

**WARNING:** This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates and radiates radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications.

However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from the one the receiver is connected to.
- Consult the dealer or an experienced radio/TV technician for help.

The user may find the following booklet prepared by the Federal Communications Commission helpful:

**The Interference Handbook**

This booklet is available from the U.S. Government Printing Office, Washington, D.C. 20402. Stock No.004-000-00345-4.

**Radiation Exposure Statement**

1. This transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.
2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated, keeping the radiator at least 20cm or more away from the person's body.

**FCC 6 GHz Statement**

a. The operation of this device is prohibited on oil platforms and aircraft, except that operation of this device in 5.925-6.425 GHz is permitted in large aircraft while flying above 10,000 feet.

b. Installation on outdoor fixed infrastructure is prohibited.

c. Controlling or communications with unmanned aircraft systems, including drones, is prohibited.

## ISED

Contains IC: 2723A-QCNFA725

*English:*

This device complies with Canadian RSS-247.
This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.

*French:*

Ce dispositif est conforme à la norme CNR-247 d'Industrie Canada applicable aux appareils radio exempts de licence. Son fonctionnement est sujet aux deux conditions suivantes: (1) le dispositif ne doit pas produire de brouillage préjudiciable, et (2) ce dispositif doit accepter tout brouillage reçu, y compris un brouillage susceptible de provoquer un fonctionnement indésirable.

*English:*

Caution:

(i) the device for operation in the band 5150-5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems;

(iv) Users should also be advised that high-power radars are allocated as primary users (i.e. priority users) of the bands 5250-5350 MHz and 5650-5850 MHz and that these radars could cause interference and/or damage to LE-LAN devices.

*French:*

Avertissement :

Le guide d'utilisation des dispositifs pour réseaux locaux doit inclure des instructions précises sur les restrictions susmentionnées, notamment :

(i) les dispositifs fonctionnant dans la bande 5 150-5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux ;

(iv) Les radars à haute puissance sont désignés comme utilisateurs principaux (c'est-à-dire utilisateurs prioritaires) des bandes de fréquences 5250-5350 MHz et 5650-5850 MHz. Ces radars peuvent causer des interférences et/ou endommager les dispositifs LE-LAN.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Note:</strong> For 5GHz and/or when co-located with 5 GHz transmitters, the following statements should be provided in the user information.
</div>

**Radiation Exposure Statement**

1. To comply with the Canadian RF exposure compliance requirements, this device and its antenna must not be co-located or operating in conjunction with any other antenna or transmitter.
2. To comply with RSS 102 RF exposure compliance requirements, this equipment should be installed and operated, keeping the radiator at least 20cm or more away from the person's body.

**Déclaration d'exposition aux rayonnements**

1. Pour se conformer aux exigences de conformité RF canadienne l'exposition, cet appareil et son antenne ne doivent pas être co-localisés ou fonctionnant en conjonction avec une autre antenne ou transmetteur.
2. Pour se conformer aux exigences de conformité CNR 102 RF exposition, cet équipement doit être installé et utilisé en maintenant le radiateur à au moins 20cm ou plus du corps de la personne.

**6 GHz General statement**

*English:*

Devices shall not be used for control of or communications with unmanned aircraft systems. Devices shall not be used on oil platforms. Devices shall not be used on aircraft, except for the low-power indoor access points, indoor subordinate devices, low-power client devices, and very low-power devices operating in the 5925-6425 MHz band, that may be used on large aircraft as defined in the Canadian Aviation Regulations, while flying above 3,048 metres (10,000 feet).

*French :*

Les dispositifs ne doivent pas être utilisés pour commander des systèmes d'aéronef sans pilote ni pour communiquer avec de tels systèmes; Les dispositifs ne doivent pas être utilisés sur les plateformes de forage pétrolier; Les dispositifs ne doivent pas être utilisés dans les aéronefs, à l'exception des points d'accès intérieurs de faible puissance, des dispositifs subordonnés intérieurs, des dispositifs clients de faible puissance et des dispositifs de très faible puissance fonctionnant dans la bande de 5 925 à 6 425 MHz, qui peuvent être utilisés dans les gros aéronefs tel qu'il est défini dans le Règlement de l'aviation canadien, et ce, lorsqu'ils volent à une altitude supérieure à 3 048 mètres (10 000 pieds).

## MIC

Contains MIC: 003-230390 / D220065003

5GHz band (W52,W53): Indoor use only (except communicate to high power radio)

5GHz 帯(W52, W53)は屋内利用に限る (高出力システムと通信する場合を除く)

## Anatel

ANATEL: 13700-21-02245

Este equipamento não tem direito à proteção contra interferência prejudicial e não pode causar interferência em sistemas devidamente autorizados.

Para maiores informações, consulte o site da ANATEL - <https://www.gov.br/anatel>

## NCC

Contains NCC: CCAI21Y10060T5

台灣: 國家通訊傳播委員會

取得審驗證明之低功率射頻器材，非經核准，公司、商號或使 用者均不得擅自變更頻率、加大功率或變更原設計之特性及功能。低功率射頻器材之使用不得影響飛航安全及干擾合法通信；經發現有干擾現象時，應立即停用，並改善至無干擾時方得繼續使用。前述合法通信，指依電信管理法規定作業之無線電通信。低功率射頻器材須忍受合法通信或工業、科學及醫療用電波輻射性電機設備之干擾。

應避免影響附近雷達系統之操作

    高增益指向性天線只得應用於固定式點對點系統。

## OFCA

5150 ~5350MHz & 6GHz band Wi-Fi (LPI) are also required to be used indoor in HongKong.

## Trademarks

The terms HDMI, HDMI High-Definition Multimedia Interface, HDMI trade dress and the HDMI Logos are trademarks or registered trademarks of HDMI Licensing Administrator, Inc.

# Unternehmensinformationen

| Firmenname | Arduino S.r.l.                               |
| ---------- | -------------------------------------------- |
| Adresse    | Via Andrea Appiani 25, 20900 Monza (Italien) |

# Referenz zur Dokumentation

| Nr. | Referenz                | Link                                                                                       |
| :-: | ----------------------- | ------------------------------------------------------------------------------------------ |
|  1  | Arduino App Lab         | [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)                   |
|  2  | VENTUNO Q-Dokumentation | [https://docs.arduino.cc/hardware/ventuno-q/](https://docs.arduino.cc/hardware/ventuno-q/) |
|  3  | Projekt Hub             | [https://projecthub.arduino.cc/](https://projecthub.arduino.cc/)                           |
|  4  | Bibliotheksreferenz     | [https://docs.arduino.cc/libraries/](https://docs.arduino.cc/libraries/)                   |
|  5  | Arduino Shop            | [https://store.arduino.cc/](https://store.arduino.cc/)                                     |

# Versionshistorie des Dokuments

| **Datum**   | **Revision** | **Änderungen**         |
| :---------: | :----------: | ---------------------- |
| 25.08.2026  |      1       | Erste Veröffentlichung |
