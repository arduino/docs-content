---
identifier: ABX00162-ABX00173
title: Arduino® UNO Q
type: maker
---
# Deutsch

![](assets/featured.png)

# Beschreibung

<p style="text-align: justify;">Der Arduino® UNO Q (im Folgenden UNO Q) ist ein Einplatinencomputer, der den Qualcomm® Dragonwing™ QRB2210-Mikroprozessor (MPU), einen Quad-Core-Arm®-Cortex®-A53 mit Debian-Linux-Betriebssystem, mit dem STMicroelectronics STM32U585-Mikrocontroller (MCU), einem Arm®-Cortex®-M33, auf dem Arduino Core unter dem Zephyr-Betriebssystem läuft. Das Linux-System und der Mikrocontroller kommunizieren über Bridge, Arduinos RPC-Bibliothek (Remote Procedure Call). Dadurch können Arduino-Sketches auf dem Mikrocontroller auf Linux-Dienste für anspruchsvolle Aufgaben zugreifen, während Linux-Anwendungen mit den Peripheriegeräten des Mikrocontrollers interagieren können, um Echtzeitvorgänge innerhalb desselben Projekts zu bewältigen.</p>

<p style="text-align: justify;">Das UNO Q verfügt über integrierten eMMC-Speicher (Optionen: 16 GB, 32 GB) und LPDDR4X-SDRAM (Optionen: 2 GB, 4 GB), damit Linux und deine Projekte reibungslos laufen. Es verfügt über Dual-Band-Wi-Fi® 5 und Bluetooth® 5.1 für drahtlose Konnektivität, einen USB-C®-Anschluss mit Stromversorgungseingang und Videoausgang sowie Arduino-kompatible headers für eine einfache Erweiterung mit Shields, Carriers und Zubehör.</p>

<p style="text-align: justify;">UNO Q lässt sich nahtlos in das Arduino App Lab integrieren, sodass Entwickler Arduino-Sketches, Linux-Anwendungen und KI-Modelle in einer einzigen Umgebung kombinieren können. Das App Lab kann direkt auf dem Board oder von einem angeschlossenen PC aus ausgeführt werden und bietet einsatzbereite Beispiele sowie die Flexibilität, maßgeschneiderte Apps für deine Projekte zu erstellen.</p>

# Zielgebiete

Prototypenentwicklung, Edge-KI & ML, Bildverarbeitung, Ausbildung, Smart Devices, Robotik, Haus- und Gebäudeautomation, Gaming

<div style="page-break-after: always;"></div>

# INHALT

## Anwendungsbeispiele

<p style="text-align: justify;">UNO Q kombiniert einen KI-fähigen Linux-Prozessor mit einem Echtzeit-Mikrocontroller und bietet so das Beste aus leistungsstarker Datenverarbeitung und deterministischer Steuerung. Neben dieser Dual-Architektur unterstützt es ein breites Ökosystem aus Arduino-Shields, Carriers, Modulino®-nodes und Zubehör von Drittanbietern, was es zu einer flexiblen Plattform für vielfältige Anwendungen macht.</p>

- **Prototyping:** Schnelle Proof-of-Concepts wie bildverarbeitungsbasierte Inspektionswerkzeuge, intelligente Kiosksysteme oder kompakte Edge-Computer mit integrierter Konnektivität.

- **Ausbildung:** Vermittlung von Linux, Echtzeitprogrammierung, KI und Computer Vision durch projektbasiertes Lernen – von wissenschaftlichen Experimenten bis hin zu interaktiven Lernrobotern.

- **Robotik:** Autonome Lieferroboter, Begleiter, die Gesten nachahmen, und Roboterarme mit visuellem Feedback, die Linux-Bildverarbeitung mit MCU-gesteuerter Motorsteuerung kombinieren.

- **Intelligente Verbrauchergeräte:** Selbstgebaute Smart-Kameras, interaktive Displays oder AR-Projekte, die auf Dual-Kameras und GPU-Beschleunigung basieren.

- **Haus- und Gebäudeautomation:** Intelligente Türklingeln mit Gesichtserkennung, sprachgesteuerte Systeme und personalisierte Klimazentralen.

- **Gaming:** Emulation von Retro-Konsolen, maßgeschneiderte Arcade-Automaten oder verbessertes Gameplay mit gestenbasierter Steuerung, Gesichtsverfolgung und Echtzeit-Feedback.

<div style="page-break-after: always;"></div>

## Funktionen

### UNO Q-Varianten

UNO Q ist in zwei Varianten erhältlich:

- **ABX00162**: 2 GB RAM, 16 GB interner Speicher
- **ABX00173**: 4 GB RAM, 32 GB interner Speicher

### Überblick über die allgemeinen technischen Daten

#### Rechenleistung & Arbeitsspeicher

![](assets/ABX00162-ABX00173-main-components.png)

| **Subsystem**  | **Details**                                                  |
| -------------- | ------------------------------------------------------------ |
| Haupt-MPU      | - Qualcomm Dragonwing™ QRB2210 - System-on-Chip (SoC) (MPU) (SOC1): 4 × Arm Cortex-A53 @ 2,0 GHz, 64-Bit- <br></br>- Adreno 702 GPU @ 845 MHz (3D-Grafik) <br></br>- Dual-ISPs: 13 MP + 13 MP oder 25 MP bei 30 fps <br></br>- Debian-Betriebssystem (Upstream-Unterstützung) <br></br>- I/O: USB 3.1 mit Rollentauschfunktion über USB-Anschluss, SDIO 3.0, 4-Lane MIPI-CSI-2 & 4-Lane MIPI-DSI |
| Echtzeit-MCU   | - ST STM32U585 (MCU) (MCU1), Arm Cortex-M33 mit bis zu 160 MHz <br></br>- Arduino Core auf Zephyr OS <br></br>- 2 MB Flash, 786 kB SRAM |
| Systemspeicher | - eMMC mit 16 oder 32 GB (EMMC1) für Betriebssystem und Daten <br></br>- LPDDR4X mit 2 GB oder 4 GB (Single-Rank, 32-Bit) (DRAM1) |

<p style="text-align: justify;">Das Qualcomm Dragonwing™ QRB2210 I/O läuft mit 1.8 V.
Die MPU steuert die MIPI-CSI-2-Kamera- und MIPI-DSI-Display-Schnittstellen auf JMEDIA sowie die 1.8-V-MPU- (SoC-) GPIO- und Audio-Endpunkte, die auf JMISC verfügbar sind.
JMISC ist ein Mixed-Voltage-Anschluss, der neben den 1.8-V-MPU-Leitungen auch 3.3-V-MCU-Signale und analoge Audiosignale überträgt. Das DisplayPort-Videosignal wird vom integrierten ANX7625 bereitgestellt, der das MIPI-DSI-Signal der MPU in den DisplayPort-Alt-Mode über USB-C umwandelt.
Der STM32U585 steuert den ADC, die PWM, den CAN, die LED-Matrix und die 3.3-V-Anschlüsse (JDIGITAL, JANALOG, JSPI und Qwiic).</p>

#### Konnektivität & Medien

![](assets/ABX00162-ABX00173-comm-components.png)

| **Subsystem**           | **Details**                                                  |
| ----------------------- | ------------------------------------------------------------ |
| WLAN-Modul              | - WCBN3536A (Qualcomm WCN3980) (U2901) <br></br>- Wi-Fi® 5 802.11a/b/g/n/ac (Dualband) + Bluetooth® 5.1 |
| USB-C-Anschluss (JUSB1) | - USB 3.1 mit Rollenwechsel-Fähigkeit<br></br>- DisplayPort-Alt-Mode über die ANX7625 DSI-zu-DP-Brücke (U3001) (SuperSpeed-Differenzpaare am Typ-C-Anschluss werden für den DP-Alt-Mode weitergeleitet)<br></br>- Videoausgang (SBC-Modus): Unterstützt Full-HD-Displays (1920 × 1080p); optimale Auflösung ist 1280 × 720p<br></br>- USB Power Delivery-Verhandlung fordert nur einen **5 V / 3 A**-Vertrag an (keine Profile mit höherer Spannung)<br></br>- VBUS-Lastschalter-/Back-Drive-Schutz (Q2801) |

Das wireless Modul nutzt SDIO für Wi-Fi®-Daten und einen UART für die Bluetooth®-Steuerung, mit einer gemeinsamen PCB-Antenne. 

#### Erweiterung & Headers

![](assets/ABX00162-ABX00173-header-expansion.png)

| **Schnittstelle (Anschluss)** | **Spannung & Pin-Anzahl**      | **Details**                                                  |
| ----------------------------- | ------------------------------ | ------------------------------------------------------------ |
| JMEDIA (JMEDIA1)              | 1.8-V-Signale, 60-Pin          | - Hochgeschwindigkeits-Kamera-/Anzeigekanäle (MIPI DSI, CSI) <br></br>- Kamerasteuerbus (CCI I²C) – dediziert, kein universeller GPIO- <br></br>- Kameratakte (SOC_CAM_MCLK0/1) <br></br>- Führt außerdem Stromschienen (+3V3 OUT, VIN IN) und GND |
| JMISC (JMISC1)                | Gemischt 1.8 V / 3.3 V, 60-Pin | - Gemischte GPIO- und SDIO- <br></br>- MCU-Peripheriegeräte: SDMMC1, TRACE, PSSI (Parallelkamera), I²C4, MCO/CRS_SYNC, OPAMP1-Pins <br></br>- Audio-Endpunkte: Mic2 INP/INM/BIAS, Kopfhörer L/R + REF, LineOut P/M, Ohrhörer P/R, HS_DET <br></br>- MPU (SoC) GPIO-Bänke (SE0) bei 1.8 V <br></br>- Führt außerdem Stromschienen (+5V USB OUT, +3V3 OUT, +1V8 OUT, VBAT OUT, VCOIN IN) und GND |
| JCTL (JCTL1)                  | 1.8 V, 10-Pin                  | - SE4-UART-Konsolen- <br></br>- Eingang für erzwungenen USB-Boot <br></br>- PMIC-Reset-Eingang <br></br>- VBUS-Stromschalter deaktivieren <br></br>- 1.8-V-Schiene und GND |
| JDIGITAL (JDIGITAL1)          | 3.3 V, 18-Pin                  | - Digitale Ein-/Ausgänge für SPI, I²C, UART, PWM, CAN        |
| JANALOG (JANALOG1)            | 3.3 V, 14-Pin                  | - Analog-I/O- <br></br>- ADC-Kanäle und Referenzspannungen   |
| JSPI (JSPI1)                  | 3.3-V-Logik, 6-Pin + 5 V VBUS  | - Dediziertes SPI: MOSI, MISO, SCLK <br></br>- MCU-Reset (NRST) <br></br>- Masse <br></br>- 5 V VBUS (USB-Stromversorgung) |
| Qwiic (QWIIC1)                | 3.3 V, 4-Pin                   | - I²C (Qwiic-Ökosystem)                                      |
### Ähnliche Produkte

- Arduino-UNO-Shields von JDIGITAL und JANALOG
- UNO Q-kompatible Carrier Boards
- Komplettes 24-Pin USB-C-Kabel
- USB-C-Dongle mit externer Stromversorgung

<div style="page-break-after: always;"></div>

## Elektrische Kenndaten

### Eingangsleistung

![UNO Q-Eingabemethoden](assets/ABX00162-ABX00173-power-supply.png)

| **Quelle**  | **Spannungsbereich** | **Maximalstrom** | **Anschluss**         |
| ----------- | -------------------: | ---------------: | --------------------- |
| USB-C VBUS  |                  5 V |       bis zu 3 A | USB-C-Anschluss       |
| VIN (DC IN) |               7-24 V |                - | JMEDIA, JANALOG (VIN) |
| 5-V-Pin     |                  5 V |       bis zu 3 A | JANALOG               |

<p style="text-align: justify;">UNO Q unterstützt zwei Stromversorgungsanschlüsse: einen USB-C-Anschluss und einen 7-24V Gleichstromeingang. Über USB Power Delivery fordert es nur das 5-V/3-A-Profil an und keine PD-Profile mit höherer Spannung. Verwende ein Netzteil und ein Kabel, die für 5 V bei 3 A ausgelegt sind, um eine Unterspannung während kurzer Aktivitätsspitzen wie z. B. bei einer drahtlosen Datenübertragung oder der Initialisierung des Displays zu vermeiden. Eine geregelte externe 5-V-Gleichstromquelle kann ebenfalls verwendet werden, um das Board über den 5-V-Pin am JANALOG-Header mit Strom zu versorgen.</p>

<p style="text-align: justify;"><em>Der USB-C-VBUS</em> und der 5-V-Ausgang des 7-24-V-Buck-Wandlers werden über <em>eine Dioden-ODER-Verknüpfung</em> auf den 5-V-Systembus (<code>5V_SYS</code>) geführt. Aus <code>5V_SYS</code> leitet das Design den 3.8-V-Vorreglerknoten und anschließend die 3,3 V ab.
Der PMIC, der mit 5V_SYS betrieben wird, liefert die 1.8-V-Spannung.</p>

<p style="text-align: justify;"><strong>Verpolungsschutz:</strong> Getestet bei einer Spannung von -24 V am DC IN-Anschluss. Der Betrieb ist nur bei korrekter Polarität gewährleistet. Lege während des normalen Betriebs keine Verpolungsspannung an.</p>

<p style="text-align: justify;"><strong>Schottky-OR-Pfad:</strong> Der Vorwärtsspannungsabfall vom Buck-Ausgang zu <code>5V_SYS</code> wurde wie folgt gemessen (JANALOG VIN-Einspeisung, Rigol DP832-Versorgung in Reihe geschaltet, Keithley DMM6500-Messung, 8542B-Aktivlast). Die Verlustleistung wird berechnet als <code>P = I × Vf</code>.</p>

| **Laststrom** | **Durchlassspannungsabfall (`Vf`)** | **Diodenverlustleistung** |
| ------------: | ----------------------------------: | ------------------------: |
|         1,0 A |                              0,35 V |                    0,35 W |
|         1,5 A |                              0,37 V |                    0,56 W |
|         2,0 A |                              0,39 V |                    0,78 W |

### Empfohlene Betriebsbedingungen

Verwende die folgenden Grenzwerte, um die Größe der Stromversorgungen zu bestimmen, die Toleranzen der Versorgungsspannungen festzulegen und die thermische Reserve zu planen:

| **Parameter**        | **Symbol**  | **Minimum** | **Typisch** | **Maximum** | **Einheit** |
| -------------------- | ----------- | :---------: | :---------: | :---------: | :---------: |
| USB-C-Eingang        | `VBUS_USBC` |     4,5     |     5,0     |     5,5     |      V      |
| Gleichstromeingang   | `DC_IN`     |     7,0     |      -      |    24,0     |      V      |
| 3.3-V-Systemspannung | `PWR_3P3V`  |     3,1     |     3,3     |     3,5     |      V      |
| Betriebstemperatur   | `T_OP`      |     -10     |      -      |     60      |     °C      |

<p style="text-align: justify;"><em>„Minimum“</em> gibt den niedrigsten Dauerbetriebswert für den regulären Betrieb an; kurze Einbrüche können zu Resets oder Verbindungsabbrüchen führen. <em>„Typisch“</em> ist der Nenn-Auslegungspunkt. <em>„Maximum“</em> darf nicht überschritten werden. Wähle für <code>DC_IN</code> (7-24 V) eine Versorgungsspannung, die die 5-V-Last problemlos abdeckt, und verwende kurze Kabel, um den Spannungsabfall zu verringern. Der Bereich <code>PWR_3P3V</code> spiegelt die Toleranz des Reglers und die Last wider. Der Temperaturbereich bezieht sich auf die Umgebungsluft in der Nähe dem Board, und ein Betrieb nahe den Grenzwerten kann den verfügbaren Ausgangsstrom verringern.</p>

### Spannungsversorgungen

| **Spannung** | **Schiene**      | **Herkunft / Regler**                                        |
| -----------: | ---------------- | ------------------------------------------------------------ |
|        5,0 V | `5V_SYS`         | Dioden-ODER-Verknüpfung aus USB-C-VBUS und 7-24-V-Buck-Ausgang (beide über Schottky-Gleichrichter) |
|        3,8 V | `PWR_3P8V`       | Abwärtswandler (Buck) von `5V_SYS`                           |
|        3.3 V | `PWR_3P3V`       | Abwärtswandler (Buck) von `PWR_3P8V`                         |
|        1.8 V | `VREG_L15A_1P8V` | PM4125 LDO L15A  von `5V_SYS`                                |

<div style="page-break-after: always;"></div>

## Funktionsübersicht

### Pinbelegung

![](assets/ABX00162-ABX00173_pinout.png)

### Blockdiagramm

![](assets/ABX00162-ABX00173_block_diagram.png)

### Stromversorgung

<p style="text-align: justify;">Das UNO Q unterstützt zwei Stromversorgungsanschlüsse: einen USB-C-Anschluss und einen 7-24-V-Gleichstromeingang. 
<em>Der USB-C-VBUS</em> und der 5-V-Ausgang des 7-24-V-Buck-Wandlers werden über <em>eine Dioden-ODER-Verknüpfung</em> auf den 5-V-Systembus (5V_SYS) geführt.</p>
<p style="text-align: justify;"><code>5V_SYS</code> versorgt den <strong>PM4125-PMIC (PMIC1)</strong> über <code>USB_IN</code>. Der L15A-LDO des PMIC liefert die 1.8-V-Schiene (<code>VREG_L15A_1P8V</code>) und versorgt die SoC-I/O-Bänke, den ANX7625 DVDD18, die digitale Wi-Fi®-Logik und die integrierten Pegelumsetzer. Die 1.8-V-Schiene ist auch am JMISC verfügbar. Aus <code>5V_SYS</code> erzeugt ein Buck-Wandler die <code>PWR_3P8V</code> (3,8 V), die für das Systemdesign und zukünftige Funktionen reserviert ist. Ein zweiter Buck-Wandler erzeugt <code>PWR_3P3V</code> für den STM32U585, den ANX7625 (3.3-V-Schienen), den Wi-Fi®-3.3-V-Bereich und die 3.3-V-Header-Pins.</p>
<p style="text-align: justify;">Ein <em>geschützter P-Kanal-MOSFET</em> (<code>Q2801</code>) kann <code>USB-VBUS</code> von <code>5V_SYS</code> liefern, wenn das Board als USB-Host/OTG betrieben wird. <code>VCOIN</code> versorgt nur die Echtzeituhr des PMIC mit Strom und nicht die Linux- oder MCU-Domänen. <code>VBAT</code> ist mit <code>PWR_3P8V</code> verbunden und für das Systemdesign sowie zukünftige Funktionen reserviert. </p>

![Arduino UNO Q Power Tree](assets/ABX00162-ABX00173_power_tree.png)

<div style="page-break-after: always;"></div>

## UI & Anzeigen

![](assets/ABX00162-ABX00173-leds.png)

- **RGB-LEDs (Linux-gesteuert):** Zwei dreifarbige LEDs werden vom Qualcomm Dragonwing™ QRB2210-Anwendungsprozessor angesteuert und über `/sys/class/leds/` bereitgestellt.

  - **RGB-LED 1 (D27301):** Kanäle: `red:user` → **GPIO_41**, `green:user` → **GPIO_42**, `blue:user` → **GPIO_60**.
  - **RGB-LED 2 (D27302):** Kanäle: `red:panic` → **GPIO_39**, `green:wlan` → **GPIO_40**, `blue:bt` → **GPIO_47**.
    
    Standardmäßig zeigt die RGB-LED 2 den Systemstatus sowie die Zustände `PANIC`, `WLAN` und `BT` an, kann aber auch vom Benutzer gesteuert werden. Die PWM-Frequenz beträgt etwa 2 kHz, um fließende Farbübergänge zu gewährleisten.

- **RGB-LEDs (MCU-gesteuert):** Zwei dreifarbige LEDs werden vom STM32U585 angesteuert.

  - **RGB-LED 3 (D27401):** `LED3_R` → **PH10**, `LED3_G` → **PH11**, `LED3_B` → **PH12**.
  - **RGB-LED 4 (D27402):** `LED4_R` → **PH13**, `LED4_G` → **PH14**, `LED4_B` → **PH15**.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Die RGB-LEDs sind aktiv-niedrig, das heißt, sie leuchten auf, wenn sie auf Logik-`0` gesetzt werden.
</div>

- **LED-Matrix (D27001..D27104):** 8 × 13 monochrome blaue LED-Matrix (104 Pixel), angesteuert vom STM32U585. Sie zeigt während des Linux-Startvorgangs etwa 20–30 Sekunden lang das Boot-Logo an. Ein Zugriff auf die Matrix vor Abschluss des Startvorgangs kann den Betrieb der MCU beeinträchtigen.

- **Betriebs-LED (D27201):** Grüne LED, die an die 3.3-V-Versorgungsspannung angeschlossen ist und leuchtet, sobald das Board mit Strom versorgt wird.

## MPU & MCU

<p style="text-align: justify;">
Eine MPU (Microprocessor Unit) ist ein leistungsstarker Anwendungsprozessor, der für die Ausführung eines vollständigen Betriebssystems und komplexer Software ausgelegt ist. Eine MCU (Microcontroller Unit) ist ein kleiner, energieeffizienter Controller, der auf schnelle, präzise Zeitsteuerung für E/A und Steuerung ausgelegt ist. UNO Q kombiniert beides, um Rechenleistung auf Betriebssystemebene mit reaktionsschneller, zeitkritischer Steuerung auf einem einzigen Board zu vereinen und über Bridge zu kommunizieren, eine RPC-Schicht, die auf beiden Seiten implementiert ist.</p>

### Anwendungsprozessor (MPU)
<p style="text-align: justify;">
Der Qualcomm® Dragonwing™ QRB2210 ist ein Quad-Core-Prozessor auf Basis des Arm® Cortex®-A53, auf dem das Betriebssystem Debian Linux läuft. Seine I/O-Schnittstellen arbeiten mit 1.8 V und er unterstützt Hochgeschwindigkeitsmedien sowie Type-C/PD-Funktionen.
</p>

<ul>
  <li>Spannungsbereich: 1.8 V für MPU (SoC)-GPIO und Hochgeschwindigkeitsschnittstellen</li>
  <li>Unterstützt JMEDIA: MIPI-CSI-2-Kamera- und MIPI-DSI-Display-Kanäle</li>
  <li>Steuert 1.8-V-MPU-GPIO- und Audio-Endpunkte auf JMISC (Mixed-Voltage-Header) an</li>
  <li>USB-C: Rollenwechsel und PD-Aushandlung (Anforderung: 5 V / 3 A)</li>
  <li>DisplayPort-Ausgang über den integrierten ANX7625 (konvertiert MIPI-DSI in DP Alt-Mode)</li>
</ul>

### Echtzeit-Mikrocontroller (MCU)
<p style="text-align: justify;">
Der STMicroelectronics® STM32U585 ist ein Arm® Cortex®-M33, auf dem der Arduino Core unter dem Zephyr-Betriebssystem läuft. Er bietet eine schnelle, präzise Zeitsteuerung für Steuerungsaufgaben und 3.3-V-I/O-Anschlüsse.
</p>

<ul>
  <li>Spannungsbereich: 3,3 V für GPIO und Analog (VREF+ ≈ 3,3 V)</li>
  <li>Verwaltet ADC, PWM, CAN, LED-Matrix und Timer</li>
  <li>Unterstützt 3.3-V-headers: JDIGITAL, JANALOG, JSPI, Qwiic</li>
</ul>

<p style="text-align: justify;">
JMISC unterstützt beide Bereiche: 1.8-V-MPU-Leitungen werden neben 3.3-V-MCU-Signalen (z. B. PSSI, SDMMC1, TRACE, I²C4) und Analog-/Audiosignalen verwendet. Bitte überprüfe die Spannungspegel, wenn du den Carrier oder externe Logik anschließen.
</p>

## Kommunikation zwischen Prozessoren

<p style="text-align: justify;">Der Qualcomm® Dragonwing™ QRB2210 (MPU) und der STM32U585 (MCU) kommunizieren über die Arduino Bridge, eine softwarebasierte RPC-Schicht (Remote Procedure Call), die sowohl auf der Linux- als auch auf der MCU-Seite implementiert ist. Bridge bietet eine serviceorientierte API, die es beiden Prozessoren ermöglicht, Dienste für den jeweils anderen bereitzustellen, und gleichzeitig Einweg-Benachrichtigungen für asynchrone Ereignisse unterstützt. Sie verwaltet das Nachrichten-Routing zwischen den Prozessoren und unterstützt mehrere physikalische Transportprotokolle. Über ihre API ermöglicht die Bridge typsichere Funktionsaufrufe, sodass Mikrocontroller-Sketches Linux-Dienste aufrufen und strukturierte Antworten empfangen oder Daten über Benachrichtigungen pushen können.</p>

<p style="text-align: justify;">Wenn für einen Carrier oder externe Logik eine Hardware-Anzeige benötigt wird, kann die Firmware einen 1.8-V-MPU-GPIO auf JMISC oder einen verfügbaren JCTL-GPIO als „Ready“- oder „Wake“-Ausgang zuweisen. Dieses Signal kann über eine pegelkompatible Schaltung, wie z. B. einen Pegelumsetzer oder eine Open-Drain-Konfiguration mit Pull-up-Widerstand, an einem MCU-GPIO empfangen werden. Die Firmware definiert die genaue Funktion dieses Signals. Alternativ kann die Aktivität auf dem ausgewählten Transport (USB CDC, UART oder SPI) als Wake-Quelle dienen, wenn sich die MCU im Schlafmodus befindet.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Die MPU-GPIO-Signale arbeiten im Niederspannungsbereich des Anwendungsprozessors (1.8 V). Stelle sicher, dass alle Verbindungen zum Mikrocontroller mit dessen I/O-Spannungsversorgung (3.3 V) pegelkompatibel sind. Verwende zum Beispiel einen Pegelumsetzer oder eine Open-Drain-Konfiguration mit einem Pull-up zur I/O-Spannungsversorgung des Mikrocontrollers.
</div>

<div style="page-break-after: always;"></div>

## Hardwarebeschleunigung

<p style="text-align: justify;">Der UNO Q bietet Hardwarebeschleunigung sowohl für 3D-Grafiken als auch für die Videokodierung/-dekodierung dank der integrierten Adreno 702-GPU, die mit 845 MHz läuft.</p>

### Grafikbeschleunigung

<p style="text-align: justify;">Die Adreno 702 GPU bietet hardwarebeschleunigtes 3D-Grafik-Rendering über Open-Source-Mesa-Treiber. Anwendungen können über Standard-Grafik-APIs wie OpenGL, OpenGL ES, Vulkan und OpenCL auf die GPU-Beschleunigung zugreifen.</p>

| **Grafik-API** | **Treiber** | **Hardware-Unterstützung** | **Aktuelle Treiberversion** | **Gerätename**         |
| -------------- | ----------- | -------------------------- | --------------------------- | ---------------------- |
| Desktop OpenGL | freedreno   | -                          | 3.1                         | FD702                  |
| OpenGL ES      | freedreno   | 3.1                        | 3.1                         | FD702                  |
| Vulkan         | turnip      | 1.1                        | 1.0.318                     | Turnip Adreno (TM) 702 |
| OpenCL         | Mesa        | 2.0                        | 2.0                         | -                      |

<p style="text-align: justify;">Die Adreno 702 GPU verfügt über eine einheitliche Speicherarchitektur, bei der sie sich den System-RAM mit der CPU für den Datentransfer teilt. Sie unterstützt 64-Bit-Speicheradressierung und bietet Direct-Rendering-Funktionen für optimale Grafikleistung.</p>

| **Parameter**                  | **Spezifikation**                                  |
| ------------------------------ | -------------------------------------------------- |
| Taktfrequenz                   | 845 MHz                                            |
| Speicherarchitektur            | Einheitlich (gemeinsam mit dem System-RAM genutzt) |
| Verfügbarer Videospeicher      | 1740 MB                                            |
| Speicheradressierung           | 64-Bit                                             |
| Direktes Rendering             | Ja                                                 |
| Maximale Größe der 2D-Textur   | 16384 × 16384 Pixel                                |
| Maximale Größe der 3D-Textur   | 2048³ Voxel                                        |
| Maximale Größe der Cube-Map    | 16384 × 16384 Pixel                                |
| OpenGL Shading Language (GLSL) | 1.40                                               |
| OpenGL ES Shading Language     | 3.10 ES                                            |

<p style="text-align: justify;">Der Mesa-Grafikstack bietet Unterstützung für Standard-OpenGL-Erweiterungen und -Funktionen. Anwendungen, die OpenGL, OpenGL ES oder Vulkan nutzen, verwenden automatisch die Hardwarebeschleunigung, ohne dass eine zusätzliche Konfiguration erforderlich ist. Standard-Grafik-Tools wie <code>mesa-utils</code> und <code>vulkan-tools</code> funktionieren auf dem UNO Q sofort nach der Installation.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Hinweis:</strong> Die OpenGL- und Vulkan-Treiber sind über die Open-Source-Mesa-Treiber <strong>„freedreno“ (OpenGL/OpenGL ES)</strong> und <strong>„turnip“ (Vulkan)</strong> verfügbar, was für Transparenz und Community-Unterstützung sorgt. Während die Adreno 702-Hardware Vulkan 1.1 unterstützt, bietet die aktuelle Treiberimplementierung Vulkan 1.0.318. <strong>Es gibt keine UNO Q-spezifischen OpenGL- oder Vulkan-Beispiele. Allerdings können die Standard-Mesa-Dienstprogramme und Beispiele aus dem Mesa-Projekt als Referenz herangezogen werden.</strong>
</div>

### Videobeschleunigung

<p style="text-align: justify;">Die Adreno 702 GPU verfügt über dedizierte Hardware-Video-Encoder und -Decoder, auf die über die <code>V4L2-API (Video4Linux2)</code> mittels der Geräte <code>/dev/video0</code> und <code>/dev/video1</code> zugegriffen werden kann. Für die folgenden Video-Codecs steht eine Hardwarebeschleunigung zur Verfügung:</p>

| **Codec**    | **Kodierung** | **Dekodierung** | **GStreamer-Element**     |
| ------------ | ------------- | --------------- | ------------------------- |
| H.264 (AVC)  | Ja            | Ja              | v4l2h264enc / v4l2h264dec |
| H.265 (HEVC) | Ja            | Ja              | v4l2h265enc / v4l2h265dec |
| VP9          | Nein          | Ja              | v4l2vp9dec                |

<p style="text-align: justify;">Der Hardware-Video-Encoder und -Decoder entlastet die CPU von Komprimierungs- und Dekomprimierungsaufgaben und überträgt diese auf spezielle Hardware, was eine effiziente Videoverarbeitung in Echtzeit ermöglicht. Das senkt den Stromverbrauch des Systems und ermöglicht es der CPU, sich auf die Anwendungslogik zu konzentrieren. Hardwarebeschleunigung ist für Auflösungen bis zu 1920×1080 (Full HD) verfügbar, einschließlich gängiger Formate wie 720p (1280×720).</p>

#### GStreamer-Integration

<p style="text-align: justify;">Der empfohlene Ansatz für den Zugriff auf die Hardware-Videobeschleunigung erfolgt über <strong>GStreamer</strong>, das eine hochrangige Pipeline-Schnittstelle zu den V4L2-Geräten bereitstellt. Die folgenden GStreamer-Elemente bieten hardwarebeschleunigte Videoverarbeitung:</p>

Für die H.264-Decodierung kann die folgende Pipeline verwendet werden:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h264parse ! v4l2h264dec \
  ! videoconvert ! autovideosink
```

Für die H.265-Decodierung kann die folgende Pipeline verwendet werden:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h265parse ! v4l2h265dec \
  ! videoconvert ! autovideosink
```

Für die VP9-Decodierung kann die folgende Pipeline verwendet werden:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.webm \
  ! matroskademux ! queue ! v4l2vp9dec \
  ! videoconvert ! autovideosink
```

Für die H.264-Kodierung kann die folgende Pipeline verwendet werden:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc ! h264parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Für die H.265-Kodierung kann die folgende Pipeline verwendet werden:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1920,height=1080,framerate=30/1 \
  ! v4l2h265enc ! h265parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Für die gleichzeitige Kodierung und Dekodierung kann die folgende Pipeline verwendet werden:

```bash
gst-launch-1.0 -v videotestsrc num-buffers=1000 \
  ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc capture-io-mode=4 output-io-mode=2 ! h264parse \
  ! v4l2h264dec capture-io-mode=4 output-io-mode=2 ! videoconvert \
  ! autovideosink
```

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Zugriff für Entwickler:</strong> Auf die V4L2-Videogeräte kann über Standard-Linux-APIs zugegriffen werden, was eine direkte Integration in C/C++-Anwendungen mithilfe von libv4l2 oder über übergeordnete Frameworks wie GStreamer, FFmpeg oder OpenCV mit V4L2-Backend-Unterstützung ermöglicht.
</div>

### OpenCL-Unterstützung

<p style="text-align: justify;">Die OpenCL 2.0-Unterstützung ist über die Mesa-Implementierung verfügbar und ermöglicht GPGPU-Berechnungen (General-Purpose GPU) für parallele Verarbeitungsaufgaben, wissenschaftliche Berechnungen und rechenintensive Vorgänge. Dank der OpenCL-Fähigkeiten des Adreno 702 können rechenintensive Aufgaben von der CPU auf die GPU ausgelagert werden, was zu einer Leistungssteigerung führt.</p>

<div style="page-break-after: always;"></div>

## Peripheriegeräte

![UNO Q Peripheriegeräte](assets/ABX00162-ABX00173_headers.png)

- **JDIGITAL (A2) (JDIGITAL1) / JANALOG (A3) (JANALOG1):** 3.3-V-GPIO mit Unterstützung für SPI-, UART-, CAN-, PWM- und ADC-Eingänge. Analoge Eingänge beziehen sich auf `VREF+` auf der 3.3-V-Schiene. Der gültige Eingangsbereich liegt zwischen 0 V und `VREF+`. Einige STM32U585-Pads sind im Digitalmodus 5-V-tolerant, jedoch sind sie bei Konfiguration als ADC oder für eine beliebige analoge Funktion (wie *A0* bis *A5*) nicht 5-V-tolerant und dürfen `VDD + 0,3 V` nicht überschreiten. Verwende für höhere Spannungen eine externe Konditionierung wie einen Spannungsteiler oder einen Puffer. Bei *A4/A5* im Einsatz als I2C3 (PC1/PC0) verwende nur Pull-ups auf 3.3 V. Außerdem verwendet **~D3 (PB0)** eine TT-artige I/O-Struktur und ist 3,6 V-tolerant; es ist in keinem Modus, auch nicht im Digitalmodus, 5 V-tolerant.

- **QWIIC-Anschluss (A4) (QWIIC1):** Zusätzlicher I²C-Bus (3.3-V-Logik). Er ist auf **PD13 (I2C4_SDA)** und **PD12 (I2C4_SCL)** abgebildet. Er garantiert Plug-and-Play-Kompatibilität mit Modulino® nodes sowie Sensoren und Aktoren von Drittanbietern.

- **JSPI (A5) (JSPI1):** 3.3-V-SPI-Anschluss für Peripheriegeräte, der MOSI-, MISO- und SCLK-Signale bereitstellt, wobei die Chip-Auswahl über einen GPIO-Pin auf JDIGITAL/JMISC erfolgt. Die Pins verwenden die STM32U585-FT-Konfiguration mit MISO auf PC2, MOSI auf PC3 und SCK auf PD1. Sie sind als Eingänge oder im Open-Drain-Modus 5-V-tolerant, während die Ausgänge 3.3 V liefern. Füge eine Pegelumsetzung hinzu, wenn eine 5-V-Eingangsschwelle oder eine bidirektionale 5-V-Signalübertragung erforderlich ist. Enthält einen `5V_SYS`-Strompin.

- **JMEDIA (B2) (JMEDIA1):** Vierkanalige Kamera- und Anzeigesignale im 1.8-V-Bereich (MIPI-CSI-2 und MIPI-DSI).

- **JMISC (B1) (JMISC):** Header mit gemischten Funktionen, der 3.3-V-MCU-Signale und 1.8-V-MPU-Signale kombiniert. Er bietet den MCU-PSSI-Bus (Parallelkamera), SDMMC1-Testpins, TRACE, I2C4, MCO/CRS_SYNC sowie die analogen OPAMP1-Pins. Außerdem führt er Audioanschlüsse (Mic2, Headphone L/R+REF, LineOut P/M, Earpiece P/R, HS_DET) und Spannungsschienen (+3V3, +5V_USB, +1V8, VBAT und VCOIN für den Systemgebrauch) heraus. Beachte die Spannungsbereiche: **MCU-Pins sind 3.3 V, MPU-GPIO sind 1.8 V**.

- **JCTL (A1) (JCTL1):** Pins für den Boot-Modus, Reset und Signale zum Aufwachen aus dem Energiesparmodus (1.8-V-Logik).

<p style="text-align: justify;"><strong>SE4 UART</strong> ist die Systemkonsole (<code>Shell-UART</code>). Sie ist von den Anwendungs-UARTs getrennt und sollte nicht für Benutzer-E/A umfunktioniert werden. Sie arbeitet im <strong>1.8-V-E/A-Bereich</strong> der MPU.</p>

<p style="text-align: justify;">Verwende die für <strong>I²C</strong>, <strong>JMEDIA CCI</strong> (Camera Control Interface) oder <strong>MI2S0</strong> (I²S-Audiobus) reservierten Leitungen des Qualcomm Dragonwing™ QRB2210 nicht als allgemeine Ein-/Ausgänge. Diese Signale sind für bestimmte Schnittstellen vorgesehen, arbeiten mit <strong>1.8 V</strong> und sind im Linux-Gerätebaum reserviert. Die Pins sind nur für diese Funktionen freigegeben.</p>

### JMISC (B1) (JMISC1) – Pinbelegung

| **Pin** | **Bezeichnung** | **MCU/SoC-Pin** | **Domäne**      | **Anmerkungen**                                              |
| ------: | --------------- | --------------- | --------------- | ------------------------------------------------------------ |
|       1 | MCU_PSSI_D0     | PC6             | 3.3V MCU        | PSSI D0                                                      |
|       2 | MCU_SDMMC1_CMD  | PD2             | 3.3V MCU        | SDMMC1 CMD / test                                            |
|       3 | MCU_PSSI_D1     | PC7             | 3.3V MCU        | PSSI D1                                                      |
|       4 | MCU_TRACE_CLK   | PE2             | 3.3V MCU        | Trace clock                                                  |
|       5 | MCU_PSSI_D2     | PC8             | 3.3V MCU        | PSSI D2                                                      |
|       6 | MCU_TRACE_D0    | PE3             | 3.3 V MCU       | Trace-Daten 0                                                |
|       7 | MCU_PSSI_D3     | PC9             | 3.3 V MCU       | PSSI D3                                                      |
|       8 | MCU_TRACE_D2    | PE5             | 3.3 V MCU       | Trace-Daten 2                                                |
|       9 | MCU_PSSI_D4     | PE4             | 3.3V MCU        | PSSI D4                                                      |
|      10 | MCU_TRACE_D3    | PE6             | 3.3-V-MCU       | Trace-Daten 3                                                |
|      11 | MCU_PSSI_D5     | PI4             | 3.3V MCU        | PSSI D5                                                      |
|      12 | MCU_PE7         | PE7             | 3.3V MCU        | GPIO                                                         |
|      13 | MCU_PSSI_D6     | PI6             | 3.3V MCU        | PSSI D6                                                      |
|      14 | MCU_PE8         | PE8             | 3.3V MCU        | GPIO                                                         |
|      15 | MCU_PSSI_D7     | PI7             | 3.3V MCU        | PSSI D7                                                      |
|      16 | MCU_I2C4_SCL    | PF14            | 3.3V MCU        | I²C4 SCL                                                     |
|      17 | MCU_PSSI_PDCK   | PD9             | 3.3V MCU        | PSSI clock                                                   |
|      18 | MCU_I2C4_SDA    | PF15            | 3.3 V MCU       | I²C4 SDA                                                     |
|      19 | MCU_PSSI_RDY    | PI5             | 3.3 V MCU       | PSSI bereit                                                  |
|      20 | MCU_OPAMP1_VOUT | PA3             | Analog          | OpAmp1 VOUT                                                  |
|      21 | MCU_PSSI_DE     | PD8             | 3.3-V-MCU       | PSSI-Datenfreigabe                                           |
|      22 | MCU_OPAMP1_VINP | PA0             | Analog          | OpAmp1 VINP                                                  |
|      23 | MCU_MCO         | PA8             | 3.3V MCU        | MCU clock out                                                |
|      24 | MCU_OPAMP1_VINM | PA1             | Analog          | OpAmp1 VINM                                                  |
|      25 | MCU_CRS_SYNC    | PA10            | 3.3 V MCU       | CRS-Synchronisation                                          |
|      26 | GND             | -               | Stromversorgung | Masse                                                        |
|      27 | GND             | -               | Stromversorgung | Masse                                                        |
|      28 | EAR_P_R         | -               | Analog          | Audio ear P_R                                                |
|      29 | MIC2_INP        | -               | Analog          | Mic2 IN+                                                     |
|      30 | EAR_M_R         | -               | Analog          | Audio ear M_R                                                |
|      31 | MIC2_INM        | -               | Analog          | Mic2 IN−                                                     |
|      32 | LINEOUT_P       | -               | Analog          | Line-Ausgang P                                               |
|      33 | MIC2_BIAS       | -               | Analog          | Mic2-Vorspannung                                             |
|      34 | LINEOUT_M       | -               | Analog          | Line-Ausgang M                                               |
|      35 | GND             | -               | Stromversorgung | Masse                                                        |
|      36 | HPH_L           | -               | Analog          | Kopfhörer L                                                  |
|      37 | SOC_GPIO_0_SE0  | -               | 1.8 V MPU       | SoC GPIO 0 (SE0)                                             |
|      38 | HPH_R           | -               | Analog          | Kopfhörer R                                                  |
|      39 | SOC_GPIO_1_SE0  | -               | 1.8 V MPU       | SoC GPIO 1 (SE0)                                             |
|      40 | HPH_REF         | -               | Analog          | Kopfhörer-Referenz                                           |
|      41 | SOC_GPIO_2_SE0  | -               | 1.8 V MPU       | SoC GPIO 2 (SE0)                                             |
|      42 | HS_DET          | -               | Analog          | Headset-Erkennung                                            |
|      43 | SOC_GPIO_3_SE0  | -               | 1.8 V MPU       | SoC GPIO 3 (SE0)                                             |
|      44 | GND             | -               | Stromversorgung | Masse                                                        |
|      45 | SOC_GPIO_86_SE0 | -               | 1.8 V MPU       | SoC GPIO 86 (SE0)                                            |
|      46 | SOC_GPIO_98     | -               | 1.8 V MPU       | SoC GPIO 98                                                  |
|      47 | SOC_GPIO_82_SE0 | -               | 1.8 V MPU       | SoC GPIO 82 (SE0)                                            |
|      48 | SOC_GPIO_99     | -               | 1.8 V MPU       | SoC GPIO 99                                                  |
|      49 | SOC_GPIO_18     | -               | 1.8 V MPU       | SoC GPIO 18                                                  |
|      50 | SOC_GPIO_100    | -               | 1.8 V MPU       | SoC GPIO 100                                                 |
|      51 | SOC_GPIO_28     | -               | 1.8 V MPU       | SoC GPIO 28                                                  |
|      52 | SOC_GPIO_101    | -               | 1.8 V MPU       | SoC GPIO 101                                                 |
|      53 | +3V3 (OUT)      | -               | Stromversorgung | 3.3-V-Ausgang                                                |
|      54 | +5V_USB (OUT)   | -               | Stromversorgung | 5-V-Ausgang                                                  |
|      55 | +3V3 (OUT)      | -               | Stromversorgung | 3.3-V-Ausgang                                                |
|      56 | +5V_USB (OUT)   | -               | Stromversorgung | 5-V-Ausgang                                                  |
|      57 | +1V8 (IN)       | -               | Stromversorgung | 1.8-V-Versorgungsspannung eingehend                          |
|      58 | GND             | -               | Stromversorgung | Masse                                                        |
|      59 | VCOIN (IN)      | -               | Stromversorgung | Systemspannung (PMIC RTC)                                    |
|      60 | VBAT (OUT)      | -               | Stromversorgung | Systemspannung (Reserviert für Systemdesign und zukünftige Funktionen) |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Hinweis: Die SoC-GPIO-Leitungen auf dem JMISC sind für bestimmte Schnittstellen reserviert (keine Maker-GPIO). Die MCUs arbeiten mit 3.3-V-Logik, die MPUs mit 1.8-V-Logik und die Audio-/Mikrofonanschlüsse sind analog.
</div>

<div style="page-break-after: always;"></div>

### JMEDIA (B2) (JMEDIA1) – Pinbelegung

| **Pin** | **Bezeichnung**         | **Bereich**     | **Anmerkungen**          |
| ------: | ----------------------- | --------------- | ------------------------ |
|       1 | GND                     | Stromversorgung | Masse                    |
|       2 | GND                     | Stromversorgung | Masse                    |
|       3 | MIPI_DSI0_CLK_M         | MIPI D-PHY      | DSI-Takt −               |
|       4 | MIPI_DSI0_L1_P          | MIPI D-PHY      | DSI-Kanal 1 +            |
|       5 | MIPI_DSI0_CLK_P         | MIPI D-PHY      | DSI-Takt +               |
|       6 | MIPI_DSI0_L1_M          | MIPI D-PHY      | DSI-Kanal 1 −            |
|       7 | GND                     | Stromversorgung | Masse                    |
|       8 | GND                     | Stromversorgung | Masse                    |
|       9 | MIPI_DSI0_L2_M          | MIPI D-PHY      | DSI-Kanal 2 −            |
|      10 | MIPI_DSI0_L0_P          | MIPI D-PHY      | DSI-Kanal 0 +            |
|      11 | MIPI_DSI0_L2_P          | MIPI D-PHY      | DSI-Kanal 2 +            |
|      12 | MIPI_DSI0_L0_M          | MIPI D-PHY      | DSI-Kanal 0 −            |
|      13 | GND                     | Stromversorgung | Masse                    |
|      14 | GND                     | Stromversorgung | Masse                    |
|      15 | MIPI_DSI0_L3_M          | MIPI D-PHY      | DSI-Kanal 3 −            |
|      16 | SOC_CAM_MCLK0 (GPIO_20) | 1.8 V MPU       | Kamerahaupttakt 0        |
|      17 | MIPI_DSI0_L3_P          | MIPI D-PHY      | DSI-Kanal 3 +            |
|      18 | SOC_CAM_MCLK1 (GPIO_21) | 1.8 V MPU       | Kamerahaupttakt 1        |
|      19 | GND                     | Stromversorgung | Masse                    |
|      20 | GND                     | Stromversorgung | Masse                    |
|      21 | CSI0_C0_LN0_M           | MIPI D-PHY      | CSI0 Daten0 −            |
|      22 | CCI_I2C_SDA1 (GPIO_29)  | 1.8 V MPU       | Kamerasteuerung I²C SDA1 |
|      23 | CSI0_B0_LN0_P           | MIPI D-PHY      | CSI0 Daten0 +            |
|      24 | CCI_I2C_SCL1 (GPIO_30)  | 1.8 V MPU       | Kamerasteuerung I²C SCL1 |
|      25 | GND                     | Stromversorgung | Masse                    |
|      26 | GND                     | Stromversorgung | Masse                    |
|      27 | CSI0_B1_LN1_M           | MIPI D-PHY      | CSI0-Daten1 −            |
|      28 | CSI1_B2_LN3_P           | MIPI D-PHY      | CSI1-Daten3 +            |
|      29 | CSI0_A1_LN1_P           | MIPI D-PHY      | CSI0-Daten1 +            |
|      30 | CSI1_C2_LN3_M           | MIPI D-PHY      | CSI1-Daten3 −            |
|      31 | GND                     | Stromversorgung | Masse                    |
|      32 | GND                     | Stromversorgung | Masse                    |
|      33 | CSI0_A0_CLK_M           | MIPI D-PHY      | CSI0-Takt −              |
|      34 | CSI1_C1_LN2_P           | MIPI D-PHY      | CSI1-Daten2 +            |
|      35 | CSI0_NC_CLK_P           | MIPI D-PHY      | CSI0-Takt +              |
|      36 | CSI1_A2_LN2_M           | MIPI D-PHY      | CSI1-Daten2 −            |
|      37 | GND                     | Stromversorgung | Masse                    |
|      38 | GND                     | Stromversorgung | Masse                    |
|      39 | CSI0_A2_LN2_M           | MIPI D-PHY      | CSI0-Daten2 −            |
|      40 | CSI1_NC_CLK_P           | MIPI D-PHY      | CSI1-Takt +              |
|      41 | CSI0_C1_LN2_P           | MIPI D-PHY      | CSI0 Daten2 +            |
|      42 | CSI1_A0_CLK_M           | MIPI D-PHY      | CSI1-Takt −              |
|      43 | GND                     | Stromversorgung | Masse                    |
|      44 | GND                     | Stromversorgung | Masse                    |
|      45 | CSI0_C2_LN3_M           | MIPI D-PHY      | CSI0-Daten3 −            |
|      46 | CSI1_A1_LN1_P           | MIPI D-PHY      | CSI1 data1 +             |
|      47 | CSI0_B2_LN3_P           | MIPI D-PHY      | CSI0-Daten3 +            |
|      48 | CSI1_B1_LN1_M           | MIPI D-PHY      | CSI1 data1 −             |
|      49 | GND                     | Stromversorgung | Masse                    |
|      50 | GND                     | Stromversorgung | Masse                    |
|      51 | CCI_I2C_SCL0 (GPIO_23)  | 1.8 V MPU       | Kamerasteuerung I²C SCL0 |
|      52 | CSI1_B0_LN0_P           | MIPI D-PHY      | CSI1-Daten0 +            |
|      53 | CCI_I2C_SDA0 (GPIO_22)  | 1.8 V MPU       | Kamerasteuerung I²C SDA0 |
|      54 | CSI1_C0_LN0_M           | MIPI D-PHY      | CSI1 data0 −             |
|      55 | GND                     | Stromversorgung | Masse                    |
|      56 | GND                     | Stromversorgung | Masse                    |
|      57 | VIN (IN)                | Stromversorgung | 7-24 V Eingang           |
|      58 | +3V3 (OUT)              | Stromversorgung | 3.3-V-Ausgang            |
|      59 | VIN (IN)                | Stromversorgung | 7-24 V Eingang           |
|      60 | +3V3 (OUT)              | Stromversorgung | 3.3-V-Ausgang            |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Hinweis: MIPI-CSI/DSI-Lanes sind D-PHY-Differenzpaare und keine universellen Ein-/Ausgänge. Steuerleitungen (CCI_I2C_*, SOC_CAM_MCLK*) gehören zur 1.8-V-MPU-Domäne. VIN am JMEDIA ist der reine 7-24-V-Eingang (nur Stromversorgung).
</div>

<div style="page-break-after: always;"></div>

### Qwiic (A4) (QWIIC1) – Pinbelegung

| **Pin** | **Bezeichnung** | **Netzwerk / Funktion** | **Domäne**      | **Anmerkungen**  |
| ------: | --------------- | ----------------------- | --------------- | ---------------- |
|       1 | GND             | Masse                   | Stromversorgung | -                |
|       2 | +3V3 OUT        | PWR_3P3V                | Stromversorgung | für Qwiic-Geräte |
|       3 | SDA             | PD13 (I2C4_SDA)         | 3.3 V           | -                |
|       4 | SCL             | PD12 (I2C4_SCL)         | 3.3 V           | -                |

### JSPI (A5) (JSPI1) – Pinbelegung

| **Pin** | **Bezeichnung** | **Netzwerk / Funktion** | **Domäne**      | **Anmerkungen**     |
| ------: | --------------- | ----------------------- | --------------- | ------------------- |
|       1 | MISO            | PC2 (SPI2_MISO)         | 3.3 V           | -                   |
|       2 | +5V             | 5V_USB_VBUS             | Stromversorgung | Nur Stromversorgung |
|       3 | SCK             | PD1 (SPI2_SCK)          | 3.3 V           | -                   |
|       4 | MOSI            | PC3 (SPI2_MOSI)         | 3.3 V           | -                   |
|       5 | RESET           | MCU_NRST                | 3.3 V           | -                   |
|       6 | GND             | Masse                   | Stromversorgung | -                   |

### JCTL (A1) (JCTL1) – Pinbelegung

| **Pin** | **Bezeichnung** | **Netz / Funktion**             | **Domäne**      | **Anmerkungen**        |
| ------: | --------------- | ------------------------------- | --------------- | ---------------------- |
|       1 | GND             | Masse                           | Stromversorgung | -                      |
|       2 | USB_BOOT        | Bootstrap                       | 1.8 V           | -                      |
|       3 | VOL_DOWN        | GPIO_36                         | 1.8 V           | GPIO                   |
|       4 | SOC_SE4_TX      | Konsolen-UART-TX (SE4)          | 1.8 V           | Systemkonsole          |
|       5 | VOL_UP          | GPIO_96                         | 1.8 V           | GPIO                   |
|       6 | SOC_SE4_RX      | Konsolen-UART-Empfang (SE4)     | 1.8 V           | Systemkonsole          |
|       7 | GND             | Masse                           | Stromversorgung | -                      |
|       8 | PMIC_RESET      | PM4125-Reset                    | 1.8 V           | -                      |
|       9 | +1V8 OUT        | VREG_L15A_1P8V                  | Stromversorgung | 1.8-V-Referenzspannung |
|      10 | VBUS_DISABLE    | VBUS-Stromschalter deaktivieren | 1.8 V           | Steuert den VBUS-Pfad  |

<div style="page-break-after: always;"></div>

### JDIGITAL (A2) (JDIGITAL1) – Pinbelegung

| **Pin** | **Bezeichnung** | **MCU-Pin** | **Funktionen**                              | **Bereich**     | **Anmerkungen**                   |
| ------: | --------------- | ----------- | ------------------------------------------- | --------------- | --------------------------------- |
|       1 | D0              | PB7         | - USART1_RX <br></br>- TIM4_CH2             | 3.3 V           | UART                              |
|       2 | D1              | PB6         | - USART1_TX <br></br>- TIM4_CH1             | 3.3 V           | UART                              |
|       3 | D2              | PB3         | - TIM2_CH2                                  | 3.3 V           | -                                 |
|       4 | ~D3             | PB0         | - OPAMP2_OUTPUT <br></br>- TIM3_CH3         | 3.3 V           | PWM / nicht 5-V-fest              |
|       5 | D4              | PA12        | - FDCAN1_TX <br></br>- TIM1_ETR             | 3.3 V           | -                                 |
|       6 | ~D5             | PA11        | - FDCAN1_RX <br></br>- TIM1_CH4             | 3.3 V           | PWM                               |
|       7 | ~D6             | PB1         | - TIM3_CH4                                  | 3.3 V           | PWM                               |
|       8 | D7              | PB2         | - TIM8_CH4N                                 | 3.3 V           | -                                 |
|       9 | D8              | PB4         | - TIM3_CH1                                  | 3.3 V           | -                                 |
|      10 | ~D9             | PB8         | - TIM4_CH3                                  | 3.3 V           | PWM                               |
|      11 | ~D10            | PB9         | - SPI2_SS (Chip Select) <br></br>- TIM4_CH4 | 3.3 V           | PWM                               |
|      12 | ~D11            | PB15        | - SPI2_MOSI <br></br>- TIM1_CH3N            | 3.3 V           | PWM                               |
|      13 | D12             | PB14        | - SPI2_MISO <br></br>- TIM1_CH2N            | 3.3 V           | -                                 |
|      14 | D13             | PB13        | - SPI2_SCK <br></br>- TIM1_CH1N             | 3.3 V           | -                                 |
|      15 | GND             | -           | - Masse                                     | Stromversorgung | -                                 |
|      16 | AREF            | -           | - Analoge Referenz                          | -               | Analoger Referenz-Pin (kein GPIO) |
|      17 | D20             | PB11        | - I2C2_SDA <br></br>- TIM2_CH4              | 3.3 V           | -                                 |
|      18 | D21             | PB10        | - I2C2_SCL <br></br>- TIM2_CH3              | 3.3 V           | -                                 |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Alle JDIGITAL-Pins arbeiten mit 3.3-V-Logik. Die meisten Pins verwenden eine I/O-Struktur vom Typ FT und sind als Eingänge 5-V-tolerant. D3 (PB0) verwendet eine I/O-Struktur vom Typ TT und ist nur 3,6-V-tolerant; lege in keinem Modus 5 V an diesen Pin an.
</div>

### JANALOG (A3) (JANALOG1) – Pinbelegung

| **Pin** | **Bezeichnung** | **Netz / MCU-Pin** | **Funktionen**                                             | **Bereich**     | **Anmerkungen**                 |
| ------: | --------------- | ------------------ | ---------------------------------------------------------- | --------------- | ------------------------------- |
|       1 | BOOT            | MCU_BOOT0          | - Boot strap                                               | 3.3 V           | -                               |
|       2 | IOREF           | PWR_3P3V           | – I/O-Spannungsreferenz (spiegelt die 3.3-V-Schiene)       | Stromversorgung | Nur Ausgang; keine Rückspeisung |
|       3 | RESET           | MCU_NRST           | - MCU reset                                                | 3.3 V           | -                               |
|       4 | +3V3 OUT        | PWR_3P3V           | - 3.3-V-Versorgung                                         | Stromversorgung | -                               |
|       5 | +5V USB VBUS    | 5V_USB_VBUS        | - 5-V-Versorgung (Durchleitung)                            | Stromversorgung | Nur Stromversorgung             |
|       6 | GND             | GND                | - Masse                                                    | Stromversorgung | -                               |
|       7 | GND             | GND                | - Masse                                                    | Stromversorgung | -                               |
|       8 | VIN IN          | DC_IN              | - 7-24 V Eingang                                           | Stromversorgung | Nur Stromversorgung             |
|       9 | A0 / D14        | PA4                | - ADC-Eingang <br></br>- DAC0 <br></br>- TIM2_CH1          | Analog / 3.3 V  | Direkter ADC / nicht 5-V-fest   |
|      10 | A1 /  D15       | PA5                | - ADC-Eingang <br></br>- DAC1 <br></br>- TIM3_CH1          | Analog / 3.3 V  | Direkter ADC / nicht 5-V-fest   |
|      11 | A2 /  D16       | PA6                | - ADC-Eingang <br></br>- OPAMP2_INPUT+ <br></br>- TIM3_CH2 | Analog / 3.3 V  |                                 |
|      12 | A3 /  D17       | PA7                | - ADC-Eingang <br></br>- OPAMP2_INPUT−                     | Analog / 3.3 V  | -                               |
|      13 | A4 /  D18       | PC1                | - ADC-Eingang <br></br>- I2C3_SDA <br></br>- LPTIM1_CH1    | Analog / 3.3 V  | -                               |
|      14 | A5 /  D19       | PC0                | - ADC-Eingang <br></br>- I2C3_SCL <br></br>- LPTIM1_IN1    | Analog / 3.3 V  | -                               |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
A0 (PA4) und A1 (PA5) sind direkte ADC-Eingänge des STM32U585, die auf <code>VREF+</code> bezogen sind. Sie sind nicht 5-V-tolerant. Der gültige Eingangsbereich ist <code>0-VREF+</code> (≈3,3 V). Der absolute Höchstwert am Pin beträgt <code>VDD + 0,3 V</code>, also ungefähr 3,6 V. Oberhalb dieses Pegels beginnen die internen Schutzdioden der MCU zu leiten. Der Steckverbinder bietet außerdem die Stromversorgungs-Pins <code>5V_SYS</code> und <code>PWR_3P3V</code>, die ausschließlich für die Stromversorgung vorgesehen sind. Lege keine 5 V an <strong>A0</strong> oder <strong>A1</strong> an.IOREF ist an die 3.3-V-Versorgungsspannung angeschlossen (<code>PWR_3P3V</code>) und dient als Referenz/Ausgang für Shields. Es darf nicht verwendet werden, um Strom zurück in das Board zu leiten.
</div>

## Hochgeschwindigkeits-Peripheriegeräte

- **USB-C:** USB 3.1 mit Rollentausch-Fähigkeit. DisplayPort Alt-Mode über ANX7625 DSI-zu-DP-Brücke. Die SuperSpeed-Differenzpaare des Steckers werden gemeinsam von DP Alt-Mode und USB 3.1-Daten genutzt. Wenn DisplayPort Alt-Mode aktiv ist, wird die USB-Datenübertragungsrate reduziert.

- **Kamera:** Vierkanaliger **MIPI-CSI-2** (1.8 V I/O).

- **Display:** Vierkanaliges **MIPI-DSI** über **ANX7625** für DisplayPort Alt-Mode über USB-C. Im Single-Board-Computer-Modus (SBC) unterstützt das Board Full-HD-Displays (1920 × 1080p) mit einer optimalen Auflösung von 1280 × 720p.

- **Drahtlos:** Dualband-WLAN® (802.11a/b/g/n/ac) und Bluetooth® 5.1 auf einem gemeinsamen Modul.

<div style="page-break-after: always;"></div>

## Bedienung des Geräts

### Erste Schritte – Arduino App Lab

Arduino App Lab [1] ist ein einheitlicher Editor, der Projekte auf beiden Prozessoren des Boards erstellt und ausführt. Ein Projekt ist eine **App**, die Folgendes enthalten kann: 

- Ein Python®-Programm, das auf dem Linux-System (Qualcomm Dragonwing™ QRB2210) läuft
- Ein Arduino-Sketch, der auf dem Mikrocontroller (MCU) (STM32U585) läuft
- Optionale **Brick** (vorkonfigurierte Dienste wie KI-Modelle, Webserver oder API-Clients), die zusammen mit der App bereitgestellt werden (laufen ebenfalls auf dem Linux-System).

Apps nutzen **Bridge**, um Daten zwischen der Linux-Seite und dem Mikrocontroller auszutauschen.

Arduino App Lab kann auf deinem PC installiert oder direkt auf dem UNO Q im Single-Board-Computer-Modus ausgeführt werden. Für diese Konfiguration wird die 4-GB-LPDDR4X-Variante des UNO Q empfohlen, um ausreichend Speicher für einen stabilen Betrieb und ressourcenintensive Anwendungen zu gewährleisten. So nutzt du das Board: 

- Starte ein gebrauchsfertiges Beispiel im Arduino App Lab, passe es an deine Bedürfnisse an oder erstelle mit dem integrierten Editor eine neue Anwendung von Grund auf.
- Klicke im Arduino App Lab auf die Schaltfläche **Run** [1].
- Der Editor erstellt die Linux-Komponente, brennt den MCU-Sketch auf den Chip, stellt den ausgewählten Brick bereit und startet alles auf dem Board.
- Die Protokolle beider Seiten sind im Editor verfügbar, und du kannst sie durchgehen, ohne das Arduino App Lab zu verlassen.

Für die Ersteinrichtung:

1. Installiere das Arduino App Lab [1], starte es und schließe das UNO Q an. Verwende für den PC-Host-Modus ein **USB-C-Datenkabel** oder versorge das Board im SBC-Modus einfach mit Strom.
2. Das Board sucht automatisch nach Updates. Falls Updates verfügbar sind, wirst du aufgefordert, diese zu installieren. Sobald das Update abgeschlossen ist, muss das Arduino App Lab[1] neu gestartet werden.
3. Bei der Ersteinrichtung wirst du aufgefordert, einen Namen und ein Passwort für das Gerät anzugeben. Außerdem musst du die WLAN®-Zugangsdaten für dein lokales Netzwerk eingeben.
4. Um das Board zu testen, ruf eine Beispiel-App im Bereich **"Examples"** des Arduino App Lab[1] auf und klicke oben rechts auf die Schaltfläche "Run". Du kannst auch im Bereich **Apps"** eine neue App erstellen.
5. Der Status der App kann auf der Registerkarte „Konsole“ der App überwacht werden.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;"> <p style="text-align: justify;">
<strong>Hinweis:</strong> Im <strong>PC-Host-Modus</strong> ist für die Ersteinrichtung eine <em>USB-Datenverbindung</em> erforderlich. Danach kannst du das <strong>Netzwerkziel</strong> über LAN (SSH) nutzen. Im <strong>Single-Board-Computer-Modus (SBC)</strong> ist für die Einrichtung keine USB-Datenverbindung erforderlich; schalte einfach die Platine ein und nutze das <strong>Netzwerkziel</strong>, sobald sie sich mit deinem Netzwerk verbunden hat. Für Peripheriegeräte im SBC-Modus (Tastatur, Maus, USB-Kamera, Mikrofon) verwende einen USB-C-Dongle mit externer Stromversorgung. Wenn der DisplayPort-Alt-Modus aktiv ist, wird die USB-Datenübertragungsrate reduziert.</p>
</div>

Verwende eine USB-C-Stromquelle mit 5 V / 3 A und ein entsprechendes Kabel oder versorge das Gerät über die 5-V- oder VIN-Pins, wie im Abschnitt [Eingangsspannung](#input-power) beschrieben (USB-C nur 5 V / VIN 7-24 V).

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Der erste Start dauert in der Regel 20 bis 30 Sekunden, während Linux hochfährt. Warte, bis die Boot-LED-Sequenz oder die LED-Matrix-Animation beendet ist, bevor du mit dem Board interagierst.
</div>

### Bricks

<p style="text-align: justify;"><strong>Bricks</strong> sind modulare Bausteine im Arduino App Lab, mit denen du deine Anwendung erweitern kannst, ohne die gesamte zugrunde liegende Infrastruktur selbst programmieren zu müssen. Jeder Brick enthält vorgefertigte Funktionen wie Sensorintegration, KI-Modelle, Datenbanken oder Benutzeroberflächen, die du einfach in ein Projekt einbinden kannst. Typische Bricks bieten:</p>

<ul>
  <li>Ein KI-Modell (z. B. Objektklassifizierung oder Keyword-Spotting)</li>
  <li>Eine Web-Benutzeroberfläche oder ein REST-API-Dienst</li>
  <li>Eine Anbindung an eine externe Datenquelle</li>
</ul>

<p style="text-align: justify;">Bricks werden zusammen mit der App bereitgestellt und von der Linux-Seite verwaltet. Der typische Arbeitsablauf sieht folgendermaßen aus:</p>

<ol>
  <li>Erstelle eine <strong>App</strong> im Arduino App Lab.</li>
  <li>Wähle einen beliebigen <strong>Brick</strong> aus, den die App verwenden soll.</li>
  <li>Füge deinen Python®-Code (Linux) und/oder deinen Arduino-Sketch (MCU) hinzu.</li>
  <li>Der Brick muss in deine `main.py`-Datei importiert und gemäß der API des Bricks initialisiert werden.</li>
  <li>Klicke auf <strong>Run</strong>, um die Linux-Anwendung bereitzustellen, die MCU zu flashen und deine App zusammen mit den dazugehörigen Bricks zu starten.</li>
  <li>Das <strong>Bridge</strong> -Tool übernimmt den Datenaustausch zwischen Linux und der MCU.</li>
</ol>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Solange eine App gebunden ist und läuft, können die USB-Schnittstellen vom System belegt sein. Nutze das Arduino App Lab [1] zum Bereitstellen und Überwachen. Um externe CLI-Tools über USB zu verwenden, beende die App oder trenne das Board.
</div>

### Hello World

<p style="text-align: justify;">Lass uns das UNO Q mit dem klassischen Arduino Hello World Beispiel programmieren - dem <em>„Blink LED“-Example</em>. So kannst du überprüfen, ob das Board korrekt mit dem Arduino App Lab verbunden ist.</p>

<ol>
  <li>Öffne das Arduino App Lab. Es startet im Bereich <strong>Examples</strong>.</li>
  <li>Wenn du nicht im Ein-Platinen-Computer-Modus arbeitest, <strong>schließe das UNO Q</strong> an deinen PC an.</li>
  <li>Öffne <em>Blink LED</em>. Schau dir die Beispielhinweise an, um zu sehen, wie die App funktioniert.</li>
  <li>Klicke auf <strong>Run</strong> und warte, bis der Upload abgeschlossen ist.</li>
</ol>

<p style="text-align: justify;">Du solltest nun sehen, wie der rote Kanal der integrierten RGB-LED abwechselnd für jeweils eine Sekunde leuchtet und dann für eine Sekunde erlischt. Die LED wird vom Mikrocontroller STM32U585 über den Arduino-Sketch angesteuert.</p>

<p style="text-align: justify;">Du kannst mit einer leeren App beginnen oder ein vorhandenes Beispiel verwenden. Bei der ersten Verwendung empfiehlt sich das „Hello World“-Beispiel, um die grundlegende Struktur kennenzulernen.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Jedes Mal, wenn du eine App startest, wird der Mikrocontroller-Sketch kompiliert und die Python®-Anwendung auf dem Linux-System gestartet. Je nach Komplexität kann dies bis zu einer Minute dauern.
</div>

### So überprüfen, ob die App ausgeführt wird

<p style="text-align: justify;">Öffne die <strong>Konsole</strong> in App Lab. Es gibt drei Registerkarten:</p>

<ul>
  <li><strong>Start-up</strong>: Protokolle der Startsequenz, einschließlich MCU-Kompilierung und Linux-Bereitstellung</li>
  <li><strong>Main (Python®)</strong>: Ausgabe der Python®-Anwendung (<code>print()</code>)</li>
  <li><strong>Sketch (Mikrocontroller)</strong>: Serielle Ausgabe aus dem Arduino-Sketch (<code>Serial.println()</code>)</li>
</ul>

<p style="text-align: justify;">Eine App kann zwar erfolgreich gestartet werden, aber dennoch Laufzeitprobleme aufweisen. Überprüfe das Python®-Protokoll auf Fehler. Tritt ein Fehler bei dem Programmskompilierung auf, wird der Start abgebrochen.</p>

<div style="page-break-after: always;"></div>

### Ein-/Aus-Taste

<p style="text-align: justify;">Das UNO Q verfügt über einen <strong>Power-Taster (JBTN1)</strong>, mit dem du das Board neu starten kannst.</p> 

![UNO Q Ein-/Aus-Taste](assets/ABX00162-ABX00173-power-button.png)

<strong>Langes Drücken (≥ 5 s):</strong> Startet das Linux-System (MPU) neu. Die Stromversorgung dem Board wird dabei nicht unterbrochen.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Hinweis:</strong> Ein Neustart durch langes Drücken startet die Linux-Umgebung neu und kann laufende Apps unterbrechen. Speichere deine Arbeit und sorge gegebenenfalls für ein sicheres Beenden externer Prozesse. Das Board startet automatisch, sobald es mit Strom versorgt wird. Für den normalen Start ist das Drücken der Taste nicht erforderlich.
</div>

### Online-Ressourcen

<p style="text-align: justify;">Entdecke Community-Projekte auf dem Project Hub [3], stöbere in der Bibliotheksreferenz [4] nach unterstützten APIs und finde Zubehör wie Qwiic-Sensoren, UNO-Shields und Carrier im Arduino Store [5].</p>

## Technische Informationen

<p style="text-align: justify;">Das Board misst 68,58 mm × 53,34 mm, wobei die Teile auf der Unterseite weniger als 2 mm hoch sind, damit das Board auf dem Carrier gestapelt werden kann. Die Umrisse und das Lochmuster entsprechen dem UNO-Formfaktor und sind mit diesem kompatibel.</p>

![](assets/mechanical_drawing_unoq.svg)

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


# Certifications

## RED / UK


| CE                     | Europe – EU Declaration of Conformity                                                                                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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
| **UK**                 | **United Kingdom – UKCA Declaration of Conformity**                                                                                                                                              |
| United Kingdom<br/>    | Hereby, Arduino S.r.l, declares that this Radiolan is in compliance with the essential requirements and other relevant provisions of The Redio Equipment Regulations 2017.                       |

The full text of the EU and UKCA declaration of conformity is available at the following internet address: https://docs.arduino.cc/certifications/

Requirements in:

Belgium (BE), Bulgaria (BG), Czech Republic (CZ), Denmark (DK), Germany (DE), Iceland (IS), Estonia (EE), Ireland (IE), Greece (EL), Spain (ES), France (FR), Croatia (HR), Italy (IT), Cyprus (CY), Latvia (LV), Liechtenstein (LI), Lithuania (LT), Luxembourg (LU), Hungary (HU), Malta (MT), Netherlands (NL), Norway (NO), Austria (AT), Poland (PL), Portugal (PT), Romania (RO), Slovenia (SI), Slovakia (SK), Turkey (TR), Finland (FI), Sweden (SE), Switzerland (CH), United Kingdom (North Irland) (UK(NI)), and United Kingdom (UK).

Operations in the 5.15-5.35GHz band are restricted to indoor usage only.

This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

### Radio Equipment Information (RED Compliance)

This radio equipment operates in the following frequency bands and with the maximum radio-frequency power indicated below:

| Radio Technology            | Frequency Band    | Maximum Transmit Power |
|-----------------------------|-------------------|------------------------|
| Bluetooth® Classic          | 2400 - 2483.5 MHz | 15 dBm                 |
| Bluetooth® Low Energy (BLE) | 2400 - 2483.5 MHz | 9.5 dBm                |
| Wi-Fi® 2.4 GHz              | 2400 - 2483.5 MHz | 19.59 dBm EIRP         |
| Wi-Fi® 5 GHz                | 5150 - 5350 MHz   | 17.64 dBm EIRP         |
| Wi-Fi® 5 GHz                | 5470 - 5725 MHz   | 17.64 dBm EIRP         |
| Wi-Fi® 5 GHz                | 5725 - 5850 MHz   | 17.64 dBm EIRP         |
| Wi-Fi® 5 GHz (upper band)   | 5725 - 5875 MHz   | 13.95 dBm EIRP         |

In accordance with EU regulations (RED Directive 2014/53/EU), the use of the 5 GHz band may be subject to national restrictions.

## FCC

**FCC compliance information**

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

This product does not contain any user serviceable components. Any unauthorized product changes or modifications will invalidate warranty and all applicable regulatory certifications and approvals, including authority to operate this device.

**FCC Part 15 Digital Emissions Compliance**

We Arduino S.r.l.  - Via Andrea Appiani 25, 20900 Monza (Italy), declare under our sole responsibility that the product Arduino® UNO Q complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

**WARNING:** This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates and radiates radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications.

However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

* Reorient or relocate the receiving antenna.
* Increase the separation between the equipment and receiver.
* Connect the equipment into an outlet on a circuit different from the one the receiver is connected to.
* Consult the dealer or an experienced radio/TV technician for help.

The user may find the following booklet prepared by the Federal Communications Commission helpful:

**The Interference Handbook**

This booklet is available from the U.S. Government Printing Office, Washington, D.C. 20402. Stock No.004-000-00345-4.

**Radiation Exposure Statement**

1. This transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.
2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated, keeping the radiator at least 20cm or more away from the person's body.

## ISED

*English:*

This device complies with Canadian RSS-247.
This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.

*French :* 

Ce dispositif est conforme à la norme CNR-247 d'Industrie Canada applicable aux appareils radio exempts de licence. Son fonctionnement est sujet aux deux conditions suivantes: (1) le dispositif ne doit pas produire de brouillage préjudiciable, et (2) ce dispositif doit accepter tout brouillage reçu, y compris un brouillage susceptible de provoquer un fonctionnement indésirable.

*English:*

Caution:

(i) the device for operation in the band 5150-5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems;

*French :*

Avertissement :

Le guide d’utilisation des dispositifs pour réseaux locaux doit inclure des instructions précises sur les restrictions susmentionnées, notamment :

(i) les dispositifs fonctionnant dans la bande 5 150-5 250 MHz sont réservés uniquement pour une utilisation à l’intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux ;

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Note:</strong> For 5GHz and/or when co-located with 5 GHz transmitters, the following statements should be provided in the user information. 
</div>

**Radiation Exposure Statement**

1. To comply with the Canadian RF exposure compliance requirements, this device and its antenna must not be co-located or operating in conjunction with any other antenna or transmitter.
2. To comply with RSS 102 RF exposure compliance requirements, this equipment should be installed and operated, keeping the radiator at least 20cm or more away from the person's body.

**Déclaration d'exposition aux rayonnements**

1. Pour se conformer aux exigences de conformité RF canadienne l'exposition, cet appareil et son antenne ne doivent pas être co-localisés ou fonctionnant en conjonction avec une autre antenne ou transmetteur.
2. Pour se conformer aux exigences de conformité CNR 102 RF exposition, cet équipement doit être installé et utilisé en maintenant le radiateur à au moins 20cm ou plus du corps de la personne.

## MIC

5GHz band (W52, W53) Indoor use only. (Except for communication with high power radios and in vehicles at W52).

日本語:

5GHz 帯(W52, W53)は屋内利用に限る (高出力システムと通信する場合を除く)

## SRRC

本设备包含型号核准代码为: ABX00162 - CMIIT ID: 26J996Q0A162 (M) / ABX00173 - CMIIT ID: 26J996Q0A173 (M) 的无线电发射模块。

## ICASA

English:

5GHz band (W52,W53): Indoor use only (except communicate to high power radio)

## NCC

根據 NCC LP0002 低功率射頻器材技術規範_章節3.8.2：
**警語:** 取得審驗證明之低功率射頻器材，非經核准，公司、商號或使用者均不得擅自變更頻
率、加大功率或變更原設計之特性及功能。
低功率射頻器材之使用不得影響飛航安全及干擾合法通信；經發現有干擾現象時，應
立即停用，並改善至無干擾時方得繼續使用。
前述合法通信，指依電信管理法規定作業之無線電通信。
低功率射頻器材須忍受合法通信或工業、科學及醫療用電波輻射性電機設備之干擾。
應避免影響附近雷達系統之操作。

## ANATEL

Este equipamento não tem direito à proteção contra interferência prejudicial e não pode causar interferência em sistemas devidamente autorizados. Para maiores informações, consulte o site da ANATEL –  [http://www.anatel.gov.br](http://www.anatel.gov.br/)

# Company Information

| Company name | Arduino S.r.l.                             |
|--------------|--------------------------------------------|
| Address      | Via Andrea Appiani 25, 20900 Monza (Italy) |

# Documentation Reference

| No. | Reference                   | Link                                                                               |
|:---:|-----------------------------|------------------------------------------------------------------------------------|
|  1  | Arduino App Lab             | [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)           |
|  2  | Arduino UNO Q Documentation | [https://docs.arduino.cc/hardware/uno-q/](https://docs.arduino.cc/hardware/uno-q/) |
|  3  | Project Hub                 | [https://projecthub.arduino.cc/](https://projecthub.arduino.cc/)                   |
|  4  | Library Reference           | [https://docs.arduino.cc/libraries/](https://docs.arduino.cc/libraries/)           |
|  5  | Arduino Store               | [https://store.arduino.cc/](https://store.arduino.cc/)                             |

# Document Revision History

|  **Date**  | **Revision** | **Changes**                                                  |
| :--------: | :----------: | ------------------------------------------------------------ |
| 26/06/2026 |      14      | Add German language                                          |
| 17/06/2026 |      13      | Display output clarification (USB-C and JMEDIA)              |
| 16/06/2026 |      12      | Add Safety information section                               |
| 01/06/2026 |      11      | Add RED radio equipment frequency band and transmit power information |
| 16/05/2026 |      10      | Pin description section updates                              |
| 15/04/2026 |      9       | Add Anatel Certification                                     |
| 24/03/2026 |      8       | General documentation update                                 |
| 17/02/2026 |      7       | Update VBAT description in Power Supply section and JMISC pin 60 note |
| 10/02/2026 |      6       | Translations in Chinese, Portuguese, Certification updates   |
| 19/01/2026 |      5       | Add video output resolution specifications                   |
| 24/11/2025 |      4       | Add hardware acceleration section (graphics APIs, video codecs, OpenCL support); remove incorrect default password reference |
| 05/11/2025 |      3       | Update operational information                               |
| 27/10/2025 |      2       | Mechanical drawing and RTC power detail update               |
| 01/10/2025 |      1       | First release                                                |
