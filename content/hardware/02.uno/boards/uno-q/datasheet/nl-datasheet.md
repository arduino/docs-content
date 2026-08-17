---
identifier: ABX00162-ABX00173
title: Arduino® UNO Q
type: maker
---

# Nederlands

![](assets/featured.png)

# Beschrijving

<p style="text-align: justify;">De Arduino® UNO Q (hierna UNO Q) is een single-boardcomputer die de Qualcomm® Dragonwing™ QRB2210-microprocessor (MPU) combineert, een quad-core Arm® Cortex®-A53 met Debian Linux OS, met de STMicroelectronics STM32U585-microcontroller (MCU), een Arm® Cortex®-M33 met Arduino Core op Zephyr OS. Het Linux-systeem en de microcontroller communiceren via Bridge, de RPC-bibliotheek (Remote Procedure Call) van Arduino. Hierdoor kunnen Arduino-sketch op de microcontroller toegang krijgen tot Linux-services voor taken op hoog niveau, terwijl Linux-applicaties kunnen communiceren met randapparatuur van de microcontroller om realtime bewerkingen binnen hetzelfde project af te handelen.</p>

<p style="text-align: justify;">De UNO Q is uitgerust met ingebouwd eMMC-geheugen (opties: 16 GB, 32 GB) en LPDDR4X SDRAM (opties: 2 GB, 4 GB) om Linux en je projecten soepel te laten draaien. Het beschikt over dual-band Wi-Fi® 5 en Bluetooth® 5.1 voor draadloze connectiviteit, een USB-C®-aansluiting met stroomvoorziening en video-uitgang, en Arduino-compatibele headers voor eenvoudige uitbreiding met shields, carriers en accessoires.</p>

<p style="text-align: justify;">UNO Q sluit naadloos aan op Arduino App Lab, waardoor ontwikkelaars Arduino-sketch, Linux-toepassingen en AI-modellen in één omgeving kunnen combineren. App Lab kan rechtstreeks op het bord of vanaf een aangesloten pc worden uitgevoerd en biedt kant-en-klare voorbeelden, evenals de flexibiliteit om apps op maat te maken die perfect bij je projecten passen.</p>

# Doelgebieden

Prototyping, Edge AI & ML, Machine Vision, Onderwijs, Slimme apparaten, Robotica, Huis- en gebouwautomatisering, Gaming

<div style="page-break-after: always;"></div>

# INHOUD

## Toepassingsvoorbeelden

<p style="text-align: justify;">UNO Q combineert een Linux-processor met AI-mogelijkheden met een realtime microcontroller, waardoor het het beste van krachtige rekenkracht en deterministische besturing biedt. Naast deze dubbele architectuur ondersteunt het een breed ecosysteem van Arduino-shields, carrier, Modulino®-nodes en accessoires van derden, waardoor het een flexibel platform is voor allerlei toepassingen.</p>

- **Prototyping:** Snelle proof-of-concepts, zoals op beeldverwerking gebaseerde inspectietools, slimme kiosken of compacte edge-computers met ingebouwde connectiviteit.

- **Onderwijs:** Lesgeven in Linux, realtime programmeren, AI en computervisie via projectmatig leren, van wetenschappelijke experimenten tot interactieve educatieve robots.

- **Robotica:** Zelfrijdende bezorgrobots, metgezelrobots die gebaren volgen en robotarmen met visuele feedback, waarbij Linux-beeldverwerking wordt gecombineerd met motorbesturing via een microcontroller.

- **Slimme consumentenapparaten:** doe-het-zelf slimme camera’s, interactieve schermen of AR-projecten die draaien op dubbele camera’s en GPU-versnelling.

- **Woning- en gebouwautomatisering:** slimme deurbellen met gezichtsherkenning, spraakgestuurde systemen en gepersonaliseerde klimaatregelaars.

- **Gaming:** Emulatie van retroconsoles, zelfgebouwde arcadekasten of verbeterde gameplay met gebarenbesturing, gezichtsherkenning en realtime feedback.

<div style="page-break-after: always;"></div>

## Functies

### UNO Q-varianten

UNO Q is verkrijgbaar in twee uitvoeringen:

- **ABX00162**: 2 GB RAM, 16 GB intern geheugen
- **ABX00173**: 4 GB RAM, 32 GB intern geheugen

### Overzicht algemene specificaties

#### Verwerking & Geheugen

![](assets/ABX00162-ABX00173-main-components.png)

| **Subsysteem** | **Details**                                                                                                                                                                                                                                                                                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hoofd-MPU      | - Qualcomm Dragonwing™ QRB2210 - System-on-Chip (SoC) (MPU) (SOC1): 4 × Arm Cortex-A53 @ 2,0 GHz, 64-bits <br></br>- Adreno 702 GPU @ 845 MHz (3D-graphics) <br></br>- Dual ISPs: 13 MP + 13 MP of 25 MP @ 30 fps <br></br>- Debian OS (upstream-ondersteuning) <br></br>- I/O: USB 3.1 met rolwisselingsmogelijkheden via USB-connector, SDIO 3.0, 4-lane MIPI-CSI-2 & 4-lane MIPI-DSI |
| Real-time MCU | - ST STM32U585 (MCU) (MCU1), Arm Cortex-M33 tot 160 MHz <br></br>- Arduino Core op Zephyr OS <br></br>- 2 MB Flash, 786 kB SRAM                                                                                                                                                                                                                                                   |
| Systeemgeheugen | - eMMC-opties van 16 of 32 GB (EMMC1) voor besturingssysteem/gegevens <br></br>- LPDDR4X-opties van 2 GB of 4 GB (single-rank, 32-bit) (DRAM1)                                                                                                                                                                                                                                                                 |

<p style="text-align: justify;">De Qualcomm Dragonwing™ QRB2210 I/O werkt op 1,8 V.
De MPU stuurt de MIPI-CSI-2-camera- en MIPI-DSI-beeldscherminterfaces op JMEDIA aan, evenals de 1,8 V MPU (SoC) GPIO- en audio-uitgangen die via JMISC toegankelijk zijn.
JMISC is een header voor verschillende spanningen die naast de 1,8 V MPU-lijnen ook 3,3 V MCU-signalen en analoge audio doorgeeft. De DisplayPort-video wordt verzorgd door de ingebouwde ANX7625, die de MIPI-DSI van de MPU omzet naar DisplayPort Alt-Mode via USB-C.
De STM32U585 regelt de ADC, PWM, CAN, de LED-matrix en de 3,3 V-aansluitingen (JDIGITAL, JANALOG, JSPI en Qwiic).</p>

#### Connectiviteit & Media

![](assets/ABX00162-ABX00173-comm-components.png)

| **Subsysteem**      | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Draadloze module    | - WCBN3536A (Qualcomm WCN3980) (U2901) <br></br>- Wi-Fi® 5 802.11a/b/g/n/ac (dual-band) + Bluetooth® 5.1                                                                                                                                                                                                                                                                                                                                                                         |
| USB-C-poort (JUSB1) | - USB 3.1 met rolwisselfunctie<br></br>- DisplayPort Alt-Mode via de ANX7625 DSI-naar-DP-brug (U3001) (SuperSpeed-differentiaalparen op de Type-C worden doorgestuurd voor DP Alt-Mode)<br></br>- Video-uitgang (SBC-modus): ondersteunt Full HD (1920 × 1080p) beeldschermen; optimale resolutie is 1280 × 720p<br></br>- USB Power Delivery-onderhandeling vraagt alleen om een **5 V / 3 A**-contract (geen profielen met hogere spanning)<br></br>- VBUS-belastingsschakelaar/back-drive-beveiliging (Q2801) |

De draadloze module maakt gebruik van SDIO voor Wi-Fi®-gegevens en een UART voor Bluetooth®-besturing, met een gedeelde printplaatantenne.

#### Uitbreiding & Kopteksten

![](assets/ABX00162-ABX00173-header-expansion.png)

| **Interface (connector)** | **Spanning & aantal pinnen**       | **Details**                                                  |
| ------------------------- | ----------------------------- | ------------------------------------------------------------ |
| JMEDIA (JMEDIA1)          | 1,8 V-signalen, 60-pins         | - Snelheidscamera-/beeldschermsporen (MIPI DSI, CSI) <br></br>- Camerabesturingsbus (CCI I²C) - speciaal, geen algemene GPIO- <br></br>- Cameraklokken (SOC_CAM_MCLK0/1) <br></br>- Bevat ook voedingsspanningen (+3V3 OUT, VIN IN) en GND                                                                                                                                       |
| JMISC (JMISC1)            | Gemengd 1,8 V / 3,3 V, 60-pins   | - Gemengde GPIO- en SDIO- <br></br>- MCU-randapparatuur: SDMMC1, TRACE, PSSI (parallelle camera), I²C4, MCO/CRS_SYNC, OPAMP1-pinnen <br></br>- Audio-eindpunten: Mic2 INP/INM/BIAS, Hoofdtelefoon L/R + REF, LineOut P/M, Oortelefoon P/R, HS_DET <br></br>- MPU (SoC) GPIO-banken (SE0) op 1,8 V <br></br>- Bevat ook voedingsspanningen (+5V USB OUT, +3V3 OUT, +1V8 OUT, VBAT OUT, VCOIN IN) en GND |
| JCTL (JCTL1)              | 1,8 V, 10-pins                 | - SE4 UART-console <br></br>- Ingang voor geforceerd opstarten via USB <br></br>- PMIC-reset-ingang <br></br>- VBUS-voedingsschakelaar uitschakelen <br></br>- 1,8 V-rail en GND                                                                                                                                                                                                                              |
| JDIGITAL (JDIGITAL1)      | 3,3 V, 18-pins                 | - Digitale I/O voor SPI, I²C, UART, PWM, CAN                                                                                                                                                                                                                                                                                                                                      |
| JANALOG (JANALOG1)        | 3,3 V, 14-pins                 | - Analoge I/O- <br></br>- ADC-kanalen en referenties                                                                                                                                                                                                                                                                                                                             |
| JSPI (JSPI1)              | 3,3 V-logica, 6-pins + 5 V VBUS | - Speciale SPI: MOSI, MISO, SCLK <br></br>- MCU-reset (NRST) <br></br>- Aarde <br></br>- 5 V VBUS (USB-voeding)                                                                                                                                                                                                                                                                 |
| Qwiic (QWIIC1)            | 3,3 V, 4-pins                  | - I²C (Qwiic-ecosysteem)                                                                                                                                                                                                                                                                                                                                                         |
### Gerelateerde producten

- Arduino UNO-shields via JDIGITAL en JANALOG
- UNO Q-compatibele carrierboards
- Volledige 24-pins USB-C-kabel
- USB-C-dongle met ondersteuning voor externe stroomvoorziening

<div style="page-break-after: always;"></div>

## Beoordelingen

### Ingangsvermogen

![UNO Q Input Methods](assets/ABX00162-ABX00173-power-supply.png)

| **Bron**  | **Spanningsbereik** | **Maximale stroomsterkte** | **Aansluiting**         |
|-------------|------------------:|--------------------:|-----------------------|
| USB-C VBUS  |               5 V |           tot 3 A | USB-C-aansluiting       |
| VIN (DC IN) |            7-24 V |                   - | JMEDIA, JANALOG (VIN) |
| 5 V-pin     |               5 V |           tot 3 A | JANALOG               |

<p style="text-align: justify;">De UNO Q ondersteunt twee voedingsingangen: een USB-C-poort en een 7-24 V DC-ingang. Via USB Power Delivery vraagt het apparaat alleen het 5 V / 3 A-profiel aan en geen PD-profielen met een hogere spanning. Gebruik een voeding en kabel die geschikt zijn voor 5 V bij 3 A om onderspanning te voorkomen tijdens korte pieken in het stroomverbruik, zoals draadloze bursts of het initialiseren van het scherm. Je kunt ook een gereguleerde externe 5 V DC-bron gebruiken om het bord van stroom te voorzien via de 5 V-pin op de JANALOG-header.</p>

<p style="text-align: justify;"><em>De USB-C VBUS</em> en de 5 V-uitgang van de 7-24 V-buck worden <em>via een diode-OR-schakeling</em> samengevoegd tot de 5 V-systeembus (<code>5V_SYS</code>). Vanuit <code>5V_SYS</code> leidt het ontwerp het 3,8 V-voorregelknooppunt af en vervolgens de 3,3 V.
De PMIC, gevoed door 5V_SYS, levert de 1,8V-spanning.</p>

<p style="text-align: justify;"><strong>Bescherming tegen omgekeerde polariteit:</strong> Getest met -24 V op de DC IN-aansluiting. Het apparaat werkt alleen bij de juiste polariteit. Zorg ervoor dat je tijdens normaal gebruik geen omgekeerde spanning aanbrengt.</p>

<p style="text-align: justify;"><strong>Schottky OR-pad:</strong> De voorwaartse spanningsval tussen de buck-uitgang en <code>5V_SYS</code> werd als volgt gemeten (JANALOG VIN-injectie, Rigol DP832-voeding in serie, Keithley DMM6500-meting, 8542B actieve belasting). Het vermogensverlies wordt berekend als <code>P = I × Vf</code>.</p>

| **Belastingsstroom** | **Voorwaartse spanningsval (`Vf`)** | **Diodevermogen** |
|-----------------:|------------------------:|----------------------:|
|            1,0 A |                  0,35 V |                0,35 W |
|            1,5 A |                  0,37 V |                0,56 W |
|            2,0 A |                  0,39 V |                0,78 W |

### Aanbevolen bedrijfsomstandigheden

Gebruik de onderstaande grenswaarden om de capaciteit van de voedingsbronnen te bepalen, de toleranties van de voedingsspanningen vast te stellen en de thermische marge in te calculeren:

| **Parameter**         | **Symbool**  | **Minimum** | **Typisch** | **Maximum** | **Eenheid** |
|-----------------------|-------------|:-----------:|:-----------:|:-----------:|:--------:|
| USB-C-ingang           | `VBUS_USBC` |     4,5     |     5,0     |     5,5     |    V     |
| DC-ingang              | `DC_IN`     |     7,0     |      -      |    24,0     |    V     |
| 3,3 V-systeemspanning     | `PWR_3P3V`  |     3,1     |     3,3     |     3,5     |    V     |
| Bedrijfstemperatuur | `T_OP`      |     -10     |      -      |     60      |    °C    |

<p style="text-align: justify;"><em>Minimum</em> geeft de laagste continue waarde aan voor normaal gebruik; korte dalingen kunnen resets of verbroken verbindingen veroorzaken. <em>Typisch</em> is het nominale ontwerppunt. <em>Maximum</em> mag niet worden overschreden. Kies voor <code>DC_IN</code> (7-24 V) een voeding die ruimschoots voldoende is voor de 5 V-belasting en gebruik korte kabels om spanningsverlies te beperken. Het <code>PWR_3P3V-bereik</code> geeft de tolerantie van de regelaar en de belasting weer. Het temperatuurbereik heeft betrekking op de omgevingslucht in de board van de printplaat, en als je dicht bij de grenzen werkt, kan de beschikbare uitgangsstroom afnemen.</p>

### Spanningsrails aan boord

| **Spanning** | **Rail**         | **Bron / Regelaar**                                                       |
|------------:|------------------|------------------------------------------------------------------------------|
|       5,0 V | `5V_SYS`         | Diode-OR van USB-C VBUS en 7-24 V buck-uitgang (beide via Schottky-gelijkrichters) |
|       3,8 V | `PWR_3P8V`       | Step-down (buck) vanaf `5V_SYS`                                               |
|       3,3 V | `PWR_3P3V`       | Step-down (buck) vanaf `PWR_3P8V`                                             |
|       1,8 V | `VREG_L15A_1P8V` | PM4125 LDO L15A  van `5V_SYS`                                               |

<div style="page-break-after: always;"></div>

## Functioneel overzicht

### Pinconfiguratie

![](assets/ABX00162-ABX00173_pinout.png)

### Blokschema

![](assets/ABX00162-ABX00173_block_diagram.png)

### Voeding

<p style="text-align: justify;">De UNO Q ondersteunt twee voedingsingangen: een USB-C-poort en een 7-24 V DC-ingang. 
<em>De USB-C VBUS</em> en de 5 V-uitgang van de 7-24 V-buck zijn <em>via een diode-OR-schakeling</em> samengevoegd tot de 5 V-systeembus (5V_SYS).</p>
<p style="text-align: justify;"><code>5V_SYS</code> voedt de <strong>PM4125 PMIC (PMIC1)</strong> via <code>USB_IN</code>. De L15A LDO van de PMIC levert de 1,8 V-rail (<code>VREG_L15A_1P8V</code>) en voedt de SoC I/O-banken, ANX7625 DVDD18, Wi-Fi® digitale logica en de ingebouwde level shifters. De 1,8 V-rail is ook beschikbaar op JMISC. Vanuit <code>5V_SYS</code> genereert een buck de <code>PWR_3P8V</code> (3,8 V), gereserveerd voor systeemontwerp en toekomstige functies. Een tweede buck-regelaar genereert <code>PWR_3P3V</code> voor de STM32U585, de ANX7625 (3,3 V-rails), het Wi-Fi® 3,3 V-domein en de 3,3 V-headerpinnen.</p>
<p style="text-align: justify;">Een <em>beveiligde P-kanaal MOSFET</em> (<code>Q2801</code>) kan USB <code>VBUS</code> leveren vanaf <code>5V_SYS</code> wanneer het bord als USB-host/OTG werkt. De <code>VCOIN</code> voorziet alleen de realtimeklok van de PMIC van stroom en levert geen stroom aan de Linux- of MCU-domeinen. De <code>VBAT</code> is aangesloten op de <code>PWR_3P8V</code> en is gereserveerd voor systeemontwerp en toekomstige functies. </p>

![Arduino UNO Q Power Tree](assets/ABX00162-ABX00173_power_tree.png)

<div style="page-break-after: always;"></div>

## Gebruikersinterface & Indicatoren

![](assets/ABX00162-ABX00173-leds.png)

- **RGB-leds (aangestuurd via Linux):** Twee driekleurige leds worden aangestuurd door de Qualcomm Dragonwing™ QRB2210-applicatieprocessor en zijn toegankelijk via `/sys/class/leds/`.

  - **RGB LED 1 (D27301):** kanalen: `red:user` → **GPIO_41**, `green:user` → **GPIO_42**, `blue:user` → **GPIO_60**.
  - **RGB LED 2 (D27302):** kanalen: `red:panic` → **GPIO_39**, `green:wlan` → **GPIO_40**, `blue:bt` → **GPIO_47**.
    
    Standaard geeft RGB-led 2 de systeemstatus, `PANIC`, `WLAN` en `BT` aan, maar je kunt hem ook zelf instellen. De PWM-frequentie is ongeveer 2 kHz voor vloeiende kleurovergangen.

- **RGB-leds (aangestuurd door MCU):** Twee driekleurige leds worden aangestuurd door de STM32U585.

  - **RGB LED 3 (D27401):** `LED3_R` → **PH10**, `LED3_G` → **PH11**, `LED3_B` → **PH12**.
  - **RGB LED 4 (D27402):** `LED4_R` → **PH13**, `LED4_G` → **PH14**, `LED4_B` → **PH15**.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  De RGB-leds werken op het 'active-low'-principe, wat betekent dat ze gaan branden als ze op logische `0` worden gezet.
</div>

- **LED-matrix (D27001..D27104):** 8 × 13 monochrome blauwe LED-matrix (104 pixels), aangestuurd door de STM32U585. Deze toont het opstartlogo gedurende ongeveer 20–30 seconden tijdens het opstarten van Linux. Toegang tot de matrix voordat het opstarten is voltooid, kan de werking van de MCU verstoren.

- **Stroom-LED (D27201):** Groene indicator die is aangesloten op de 3,3 V-voeding en gaat branden zodra het bord stroom krijgt.

## MPU & MCU

<p style="text-align: justify;">
Een MPU (Microprocessor Unit) is een krachtige applicatieprocessor die is ontworpen om een volledig besturingssysteem en complexe software te draaien. Een MCU (Microcontroller Unit) is een kleine, energiezuinige controller die is gericht op snelle, nauwkeurige timing voor I/O en besturing. UNO Q combineert beide om rekenkracht op OS-niveau te koppelen aan responsieve, tijdkritische besturing op een single-board en te communiceren via Bridge, een RPC-laag die aan beide kanten is geïmplementeerd.</p>

### Applicatieprocessor (MPU)
<p style="text-align: justify;">
De Qualcomm® Dragonwing™ QRB2210 is een quad-core Arm® Cortex®-A53 die draait op het Debian Linux-besturingssysteem. De I/O werkt op 1,8 V en ondersteunt snelle media en Type-C/PD-functionaliteit.
</p>

<ul>
  <li>Spanningsbereik: 1,8 V voor MPU (SoC) GPIO en hogesnelheidsinterfaces</li>
  <li>Aansluitingen voor JMEDIA: MIPI-CSI-2-camera en MIPI-DSI-beeldscherm</li>
  <li>Aansturing van 1,8 V MPU GPIO- en audio-aansluitingen op JMISC (header voor gemengde spanningen)</li>
  <li>USB-C: rolwisseling en PD-onderhandeling (verzoek om 5 V / 3 A)</li>
  <li>DisplayPort-uitgang via de ingebouwde ANX7625 (zet MIPI-DSI om naar DP Alt-Mode)</li>
</ul>

### Real-time microcontroller (MCU)
<p style="text-align: justify;">
De STMicroelectronics® STM32U585 is een Arm® Cortex®-M33 met Arduino Core op het Zephyr-besturingssysteem. Hij biedt snelle, nauwkeurige timing voor besturingstaken en 3,3 V I/O-aansluitingen.
</p>

<ul>
  <li>Spanningsbereik: 3,3 V voor GPIO en analoog (VREF+ ≈ 3,3 V)</li>
  <li>Beheert ADC, PWM, CAN, LED-matrix en timers</li>
  <li>Ondersteunt 3,3 V-connectoren: JDIGITAL, JANALOG, JSPI, Qwiic</li>
</ul>

<p style="text-align: justify;">
JMISC ondersteunt beide domeinen: 1,8 V MPU-lijnen lopen parallel aan 3,3 V MCU-signalen (bijv. PSSI, SDMMC1, TRACE, I²C4) en analoge/audiosignalen. Controleer de spanningsniveaus wanneer je carriers of externe logica aansluit.
</p>

## Communicatie tussen processors

<p style="text-align: justify;">De Qualcomm® Dragonwing™ QRB2210 (MPU) en de STM32U585 (MCU) communiceren via de Arduino Bridge, een op software gebaseerde RPC-laag (Remote Procedure Call) die zowel aan de Linux- als aan de MCU-kant is geïmplementeerd. Bridge biedt een servicegerichte API waarmee beide processors diensten kunnen aanbieden die de andere kan aanroepen, terwijl het ook eenrichtingsmeldingen voor asynchrone gebeurtenissen ondersteunt. Het regelt de routering van berichten tussen processors en ondersteunt meerdere fysieke transporten. Via de API maakt Bridge typeveilige functieaanroepen mogelijk, waardoor microcontroller-sketch Linux-services kunnen aanroepen en gestructureerde reacties kunnen ontvangen, of gegevens kunnen pushen via meldingen.</p>

<p style="text-align: justify;">Als er een hardware-indicator nodig is voor een carrierboard of externe logica, kan de firmware een 1,8V MPU-GPIO op JMISC, of een beschikbare JCTL-GPIO, toewijzen als ‘ready’- of ‘wake’-uitgang. Dit signaal kan worden ontvangen op een MCU GPIO via niveau-compatibele schakelingen, zoals een niveauverschuiver of een open-drain-configuratie met een pull-up-weerstand. De firmware bepaalt de exacte functie van dit signaal. Als alternatief kan activiteit op het geselecteerde transport (USB CDC, UART of SPI) dienen als wake-bron wanneer de MCU in de slaapstand staat.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  De GPIO-signalen van de MPU werken in het laagspanningsdomein van de applicatieprocessor (1,8 V). Zorg ervoor dat elke aansluiting op de microcontroller niveau-compatibel is met de I/O-spanningsrail van de microcontroller (3,3 V). Gebruik bijvoorbeeld een levelshifter of een open-drain-configuratie met een pull-up naar de I/O-rail van de microcontroller.
</div>

<div style="page-break-after: always;"></div>

## Hardwareversnelling

<p style="text-align: justify;">De UNO Q biedt hardwareversnelling voor zowel 3D-graphics als videocodering en -decodering via de ingebouwde Adreno 702 GPU, die op 845 MHz draait.</p>

### Grafische versnelling

<p style="text-align: justify;">De Adreno 702 GPU zorgt voor hardwareversnelde 3D-grafische weergave via open-source Mesa-stuurprogramma’s. Apps kunnen gebruikmaken van GPU-versnelling via standaard grafische API’s, zoals OpenGL, OpenGL ES, Vulkan en OpenCL.</p>

| **Grafische API** | **Stuurprogramma** | **Ondersteunde hardware** | **Huidige versie van het stuurprogramma** | **Naam van het apparaat**        |
|------------------|------------|----------------------|----------------------------|------------------------|
| Desktop OpenGL   | freedreno  | -                    | 3.1                        | FD702                  |
| OpenGL ES        | freedreno  | 3.1                  | 3.1                        | FD702                  |
| Vulkan           | turnip     | 1.1                  | 1.0.318                    | Turnip Adreno (TM) 702 |
| OpenCL           | Mesa       | 2.0                  | 2.0                        | -                      |

<p style="text-align: justify;">De Adreno 702 GPU beschikt over een gedeelde geheugenarchitectuur, waarbij het systeemgeheugen met de CPU wordt gedeeld voor gegevensoverdracht. Hij ondersteunt 64-bits geheugenadressering en biedt directe weergavemogelijkheden voor optimale grafische prestaties.</p>

| **Parameter**                  | **Specificatie**                |
|--------------------------------|----------------------------------|
| Klokfrequentie                | 845 MHz                          |
| Geheugenarchitectuur            | Unified (gedeeld met het systeem-RAM) |
| Beschikbaar videogeheugen         | 1740 MB                          |
| Geheugenadressering              | 64-bits                           |
| Directe weergave               | Ja                              |
| Maximale grootte 2D-textuur        | 16384 × 16384 pixels             |
| Maximale grootte 3D-textuur        | 2048³ voxels                     |
| Maximale grootte van de kubuskaart          | 16384 × 16384 pixels             |
| OpenGL Shading Language (GLSL) | 1.40                             |
| OpenGL ES-shadingtaal     | 3.10 ES                          |

<p style="text-align: justify;">De Mesa-grafische stack biedt ondersteuning voor standaard OpenGL-uitbreidingen en -functies. Toepassingen die gebruikmaken van OpenGL, OpenGL ES of Vulkan maken automatisch gebruik van hardwareversnelling zonder dat je iets extra’s hoeft in te stellen. Standaard grafische hulpprogramma’s zoals <code>mesa-utils</code> en <code>vulkan-tools</code> werken direct op de UNO Q.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Opmerking:</strong> De OpenGL- en Vulkan-stuurprogramma’s zijn beschikbaar via de open-source Mesa-stuurprogramma’s <strong>freedreno (OpenGL/OpenGL ES)</strong> en <strong>turnip (Vulkan)</strong>, die transparantie en ondersteuning door de community bieden. Hoewel de Adreno 702-hardware Vulkan 1.1 ondersteunt, biedt de huidige stuurprogramma-implementatie Vulkan 1.0.318. <strong>Er zijn geen UNO Q-specifieke OpenGL- of Vulkan-voorbeelden. Je kunt echter wel de standaard Mesa-hulpprogramma's en voorbeelden van het Mesa-project als referentie gebruiken.</strong>
</div>

### Videoversnelling

<p style="text-align: justify;">De Adreno 702 GPU beschikt over speciale hardware-videocodecs en -decoders die via de <code>V4L2 (Video4Linux2)</code> API toegankelijk zijn via de apparaten <code>/dev/video0</code> en <code>/dev/video1</code>. Er is hardwareversnelling beschikbaar voor de volgende videocodecs:</p>

| **Codec**    | **Codering** | **Decodering** | **GStreamer-element**     |
|--------------|--------------|--------------|---------------------------|
| H.264 (AVC)  | Ja          | Ja          | v4l2h264enc / v4l2h264dec |
| H.265 (HEVC) | Ja          | Ja          | v4l2h265enc / v4l2h265dec |
| VP9          | Nee           | Ja          | v4l2vp9dec                |

<p style="text-align: justify;">De hardware-videocodec en -decoder nemen de compressie- en decompressietaken over van de CPU en voeren deze uit op speciale hardware, waardoor efficiënte realtime videoverwerking mogelijk wordt. Dit verlaagt het stroomverbruik van het systeem en zorgt ervoor dat de CPU zich kan concentreren op de applicatielogica. Hardwareversnelling is beschikbaar voor resoluties tot 1920×1080 (Full HD), inclusief gangbare formaten zoals 720p (1280×720).</p>

#### Integratie met GStreamer

<p style="text-align: justify;">De aanbevolen manier om gebruik te maken van hardwareversnelling voor video is via <strong>GStreamer</strong>, dat een hoogwaardige pijplijninterface biedt voor V4L2-apparaten. De volgende GStreamer-elementen zorgen voor hardwareversnelde videoverwerking:</p>

Voor het decoderen van H.264 kun je de volgende pijplijn gebruiken:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h264parse ! v4l2h264dec \
  ! videoconvert ! autovideosink
```

Voor het decoderen van H.265 kun je de volgende pijplijn gebruiken:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h265parse ! v4l2h265dec \
  ! videoconvert ! autovideosink
```

Voor het decoderen van VP9 kun je de volgende pijplijn gebruiken:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.webm \
  ! matroskademux ! queue ! v4l2vp9dec \
  ! videoconvert ! autovideosink
```

Voor H.264-codering kun je de volgende pijplijn gebruiken:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc ! h264parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Voor H.265-codering kun je de volgende pijplijn gebruiken:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1920,height=1080,framerate=30/1 \
  ! v4l2h265enc ! h265parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Voor gelijktijdige codering en decodering kun je de volgende pijplijn gebruiken:

```bash
gst-launch-1.0 -v videotestsrc num-buffers=1000 \
  ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc capture-io-mode=4 output-io-mode=2 ! h264parse \
  ! v4l2h264dec capture-io-mode=4 output-io-mode=2 ! videoconvert \
  ! autovideosink
```

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Toegang voor ontwikkelaars:</strong> De V4L2-videotoestellen zijn toegankelijk via standaard Linux-API’s, waardoor je ze rechtstreeks kunt integreren in C/C++-toepassingen met behulp van libv4l2 of via frameworks op hoger niveau zoals GStreamer, FFmpeg of OpenCV met ondersteuning voor de V4L2-backend.
</div>

### OpenCL-ondersteuning

<p style="text-align: justify;">OpenCL 2.0 wordt ondersteund via de Mesa-implementatie, waardoor GPGPU-berekeningen mogelijk zijn voor parallelle verwerkingstaken, wetenschappelijke berekeningen en rekenintensieve bewerkingen. Dankzij de OpenCL-mogelijkheden van de Adreno 702 kunnen rekenintensieve taken van de CPU naar de GPU worden verplaatst voor betere prestaties.</p>

<div style="page-break-after: always;"></div>

## Randapparatuur

![UNO Q Peripherals](assets/ABX00162-ABX00173_headers.png)

- **JDIGITAL (A2) (JDIGITAL1) / JANALOG (A3) (JANALOG1):** 3,3 V GPIO met ondersteuning voor SPI-, UART-, CAN-, PWM- en ADC-ingangen. Analoge ingangen zijn gerelateerd aan `VREF+` op de 3,3 V-rail. Het geldige ingangsbereik is 0 V tot `VREF+`. Sommige STM32U585-pads zijn 5 V-tolerant in digitale modus, maar wanneer ze zijn geconfigureerd als ADC of een andere analoge functie (zoals *A0* tot en met *A5*), zijn ze niet 5 V-tolerant en mogen ze `VDD + 0,3 V` niet overschrijden. Gebruik externe conditionering zoals een spanningsdeler of buffer voor hogere spanningen. Gebruik voor *A4/A5* bij gebruik als I2C3 (PC1/PC0) alleen pull-ups naar 3,3 V. Bovendien gebruikt **~D3 (PB0)** een TT-type I/O-structuur en is het 3,6 V-tolerant; het is in geen enkele modus 5 V-tolerant, ook niet in de digitale modus.

- **QWIIC-connector (A4) (QWIIC1):** Extra I²C-bus (3,3 V-logica). Deze is toegewezen aan **PD13 (I2C4_SDA)** en **PD12 (I2C4_SCL)**. Dit garandeert plug-and-play-compatibiliteit met Modulino®-knooppunten en sensoren en actuatoren van derden.

- **JSPI (A5) (JSPI1):** 3,3 V SPI-aansluiting voor randapparatuur die MOSI-, MISO- en SCLK-signalen levert, waarbij chip-select beschikbaar is via een GPIO-pin op JDIGITAL/JMISC. De pinnen gebruiken een STM32U585 FT-configuratie met MISO op PC2, MOSI op PC3 en SCK op PD1. Ze zijn 5 V-tolerant als ingangen of in open-drain, terwijl de uitgangen 3,3 V aansturen. Voeg een niveauverschuiving toe als een 5 V-ingangsdrempel of 5 V bidirectionele signalering vereist is. Bevat een `5V_SYS`-voedingspin.

- **JMEDIA (B2) (JMEDIA1):** Vierkanaals camera- en beeldsignalen in het 1,8 V-bereik (MIPI-CSI-2 en MIPI-DSI).

- **JMISC (B1) (JMISC):** Header met gemengde functies die 3,3 V MCU-signalen en 1,8 V MPU-signalen combineert. Deze biedt een MCU PSSI-bus (parallelle camera), SDMMC1-testpinnen, TRACE, I2C4, MCO/CRS_SYNC en OPAMP1 analoge pinnen. Ook zijn er audio-aansluitingen (Mic2, Headphone L/R+REF, LineOut P/M, Earpiece P/R, HS_DET) en voedingsspanningen (+3V3, +5V_USB, +1V8, VBAT en VCOIN voor systeemgebruik). Let op de spanningsdomeinen: **MCU-pinnen zijn 3,3 V, MPU GPIO zijn 1,8 V**.

- **JCTL (A1) (JCTL1):** Pinnen voor opstartmodus, reset en signalen voor ontwaken uit slaapstand (1,8 V-logica).

<p style="text-align: justify;"><strong>SE4 UART</strong> is de systeemconsole (<code>shell-UART</code>). Deze staat los van de UART’s voor toepassingen en mag niet worden gebruikt voor gebruikers-I/O. Hij werkt binnen het <strong>1,8 V</strong> I/O-domein van de MPU.</p>

<p style="text-align: justify;">Gebruik de Qualcomm Dragonwing™ QRB2210-lijnen die zijn gereserveerd voor <strong>I²C</strong>, <strong>JMEDIA CCI</strong> (Camera Control Interface) of <strong>MI2S0</strong> (I²S-audiobus) niet als algemene I/O. Deze signalen zijn specifiek voor de interface, werken op <strong>1,8 V</strong> en zijn gereserveerd in de Linux-device tree. De headers stellen ze alleen beschikbaar voor die functies.</p>

### JMISC (B1) (JMISC1) - Pin-overzicht

| **Pin** | **Benaming** | **MCU/SoC-pin** | **Domein** | **Opmerkingen**                                                       |
|--------:|-----------------|-----------------|------------|-----------------------------------------------------------------|
|       1 | MCU_PSSI_D0     | PC6             | 3,3 V MCU   | PSSI D0                                                         |
|       2 | MCU_SDMMC1_CMD  | PD2             | 3,3 V MCU   | SDMMC1-commando / test                                               |
|       3 | MCU_PSSI_D1     | PC7             | 3,3 V MCU   | PSSI D1                                                         |
|       4 | MCU_TRACE_CLK   | PE2             | 3,3 V MCU   | Trace-klok                                                     |
|       5 | MCU_PSSI_D2     | PC8             | 3,3 V MCU   | PSSI D2                                                         |
|       6 | MCU_TRACE_D0    | PE3             | 3,3 V MCU   | Tracegegevens 0                                                    |
|       7 | MCU_PSSI_D3     | PC9             | 3,3 V MCU   | PSSI D3                                                         |
|       8 | MCU_TRACE_D2    | PE5             | 3,3 V MCU   | Tracegegevens 2                                                    |
|       9 | MCU_PSSI_D4     | PE4             | 3,3 V MCU   | PSSI D4                                                         |
|      10 | MCU_TRACE_D3    | PE6             | 3,3 V MCU   | Tracegegevens 3                                                    |
|      11 | MCU_PSSI_D5     | PI4             | 3,3 V MCU   | PSSI D5                                                         |
|      12 | MCU_PE7         | PE7             | 3,3 V MCU   | GPIO                                                            |
|      13 | MCU_PSSI_D6     | PI6             | 3,3 V MCU   | PSSI D6                                                         |
|      14 | MCU_PE8         | PE8             | 3,3 V MCU   | GPIO                                                            |
|      15 | MCU_PSSI_D7     | PI7             | 3,3 V MCU   | PSSI D7                                                         |
|      16 | MCU_I2C4_SCL    | PF14            | 3,3 V MCU   | I²C4 SCL                                                        |
|      17 | MCU_PSSI_PDCK   | PD9             | 3,3 V MCU   | PSSI-klok                                                      |
|      18 | MCU_I2C4_SDA    | PF15            | 3,3 V MCU   | I²C4 SDA                                                        |
|      19 | MCU_PSSI_RDY    | PI5             | 3,3 V MCU   | PSSI gereed                                                      |
|      20 | MCU_OPAMP1_VOUT | PA3             | Analoog     | Uitgangssignaal OpAmp1                                                     |
|      21 | MCU_PSSI_DE     | PD8             | 3,3 V MCU   | PSSI-gegevens ingeschakeld                                                |
|      22 | MCU_OPAMP1_VINP | PA0             | Analoog     | OpAmp1 VINP                                                     |
|      23 | MCU_MCO         | PA8             | 3,3 V MCU   | MCU-klokuitgang                                                   |
|      24 | MCU_OPAMP1_VINM | PA1             | Analoog     | OpAmp1 VINM                                                     |
|      25 | MCU_CRS_SYNC    | PA10            | 3,3 V MCU   | CRS-synchronisatie                                                        |
|      26 | GND             | -               | Voeding      | Aarde                                                          |
|      27 | GND             | -               | Voeding      | Aarde                                                          |
|      28 | EAR_P_R         | -               | Analoog     | Audio-oortje P_R                                                   |
|      29 | MIC2_INP        | -               | Analoog     | Mic2 IN+                                                        |
|      30 | EAR_M_R         | -               | Analoog     | Audio-oor M_R                                                   |
|      31 | MIC2_INM        | -               | Analoog     | Mic2 IN−                                                        |
|      32 | LINEOUT_P       | -               | Analoog     | Lijningang P                                                      |
|      33 | MIC2_BIAS       | -               | Analoog     | Voorbelasting microfoon 2                                                       |
|      34 | LINEOUT_M       | -               | Analoog     | Lijningang M                                                      |
|      35 | GND             | -               | Voeding      | Aarde                                                          |
|      36 | HPH_L           | -               | Analoog     | Hoofdtelefoon L                                                     |
|      37 | SOC_GPIO_0_SE0  | -               | 1,8 V MPU   | SoC GPIO 0 (SE0)                                                |
|      38 | HPH_R           | -               | Analoog     | Hoofdtelefoon R                                                     |
|      39 | SOC_GPIO_1_SE0  | -               | 1,8 V MPU   | SoC GPIO 1 (SE0)                                                |
|      40 | HPH_REF         | -               | Analoog     | Hoofdtelefoon REF                                                   |
|      41 | SOC_GPIO_2_SE0  | -               | 1,8 V MPU   | SoC GPIO 2 (SE0)                                                |
|      42 | HS_DET          | -               | Analog     | Headsetdetectie                                                  |
|      43 | SOC_GPIO_3_SE0  | -               | 1,8 V MPU   | SoC GPIO 3 (SE0)                                                |
|      44 | GND             | -               | Voeding      | Aarde                                                          |
|      45 | SOC_GPIO_86_SE0 | -               | 1,8 V MPU   | SoC GPIO 86 (SE0)                                               |
|      46 | SOC_GPIO_98     | -               | 1,8 V MPU   | SoC GPIO 98                                                     |
|      47 | SOC_GPIO_82_SE0 | -               | 1,8 V MPU   | SoC GPIO 82 (SE0)                                               |
|      48 | SOC_GPIO_99     | -               | 1,8 V MPU   | SoC GPIO 99                                                     |
|      49 | SOC_GPIO_18     | -               | 1,8 V MPU   | SoC GPIO 18                                                     |
|      50 | SOC_GPIO_100    | -               | 1,8 V MPU   | SoC GPIO 100                                                    |
|      51 | SOC_GPIO_28     | -               | 1,8 V MPU   | SoC GPIO 28                                                     |
|      52 | SOC_GPIO_101    | -               | 1,8 V MPU   | SoC GPIO 101                                                    |
|      53 | +3V3 (OUT)      | -               | Voeding      | 3,3 V-uitgang                                                 |
|      54 | +5V_USB (OUT)   | -               | Voeding      | 5 V-uitgang                                                   |
|      55 | +3V3 (OUT)      | -               | Voeding      | 3,3 V-uitgang                                                 |
|      56 | +5V_USB (OUT)   | -               | Voeding      | 5 V-uitgang                                                   |
|      57 | +1V8 (IN)       | -               | Voeding      | 1,8 V-rail in                                                   |
|      58 | GND             | -               | Voeding      | Aarde                                                          |
|      59 | VCOIN (IN)      | -               | Voeding      | Systeemspanning (PMIC RTC)                                       |
|      60 | VBAT (OUT)      | -               | Voeding      | Systeemspanning (Gereserveerd voor systeemontwerp en toekomstige functies) |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Opmerking: De SoC-GPIO-pinnen op de JMISC zijn bestemd voor specifieke interfaces (geen Maker-GPIO). De MCU’s werken op 3,3 V-logica, de MPU’s op 1,8 V-logica en de audio-/microfoonpinnen zijn analoog.
</div>

<div style="page-break-after: always;"></div>

### JMEDIA (B2) (JMEDIA1) - Pinkaart

| **Pin** | **Benaming**         | **Domein** | **Opmerkingen**               |
|--------:|-------------------------|------------|-------------------------|
|       1 | GND                     | Voeding      | Aarde                  |
|       2 | GND                     | Voeding      | Aarde                  |
|       3 | MIPI_DSI0_CLK_M         | MIPI D-PHY | DSI-klok −             |
|       4 | MIPI_DSI0_L1_P          | MIPI D-PHY | DSI-baan 1 +             |
|       5 | MIPI_DSI0_CLK_P         | MIPI D-PHY | DSI-klok +             |
|       6 | MIPI_DSI0_L1_M          | MIPI D-PHY | DSI-baan 1 −             |
|       7 | GND                     | Voeding      | Aarde                  |
|       8 | GND                     | Voeding      | Aarde                  |
|       9 | MIPI_DSI0_L2_M          | MIPI D-PHY | DSI-baan 2 −             |
|      10 | MIPI_DSI0_L0_P          | MIPI D-PHY | DSI-baan 0 +             |
|      11 | MIPI_DSI0_L2_P          | MIPI D-PHY | DSI-baan 2 +             |
|      12 | MIPI_DSI0_L0_M          | MIPI D-PHY | DSI-baan 0 −             |
|      13 | GND                     | Voeding      | Aarde                  |
|      14 | GND                     | Voeding      | Aarde                  |
|      15 | MIPI_DSI0_L3_M          | MIPI D-PHY | DSI-baan 3 −             |
|      16 | SOC_CAM_MCLK0 (GPIO_20) | 1,8 V MPU   | Masterklok 0 van de camera   |
|      17 | MIPI_DSI0_L3_P          | MIPI D-PHY | DSI-baan 3 +             |
|      18 | SOC_CAM_MCLK1 (GPIO_21) | 1,8 V MPU   | Hoofdklok camera 1   |
|      19 | GND                     | Voeding      | Aarde                  |
|      20 | GND                     | Voeding      | Aarde                  |
|      21 | CSI0_C0_LN0_M           | MIPI D-PHY | CSI0 data0 −            |
|      22 | CCI_I2C_SDA1 (GPIO_29)  | 1,8 V MPU   | Camera-aansturing I²C SDA1 |
|      23 | CSI0_B0_LN0_P           | MIPI D-PHY | CSI0 data0 +            |
|      24 | CCI_I2C_SCL1 (GPIO_30)  | 1,8 V MPU   | Camera-aansturing I²C SCL1 |
|      25 | GND                     | Voeding      | Aarde                  |
|      26 | GND                     | Voeding      | Aarde                  |
|      27 | CSI0_B1_LN1_M           | MIPI D-PHY | CSI0 data1 −            |
|      28 | CSI1_B2_LN3_P           | MIPI D-PHY | CSI1 data3 +            |
|      29 | CSI0_A1_LN1_P           | MIPI D-PHY | CSI0 data1 +            |
|      30 | CSI1_C2_LN3_M           | MIPI D-PHY | CSI1 data3 −            |
|      31 | GND                     | Voeding      | Aarde                  |
|      32 | GND                     | Voeding      | Aarde                  |
|      33 | CSI0_A0_CLK_M           | MIPI D-PHY | CSI0-klok −            |
|      34 | CSI1_C1_LN2_P           | MIPI D-PHY | CSI1 data2 +            |
|      35 | CSI0_NC_CLK_P           | MIPI D-PHY | CSI0-klok +            |
|      36 | CSI1_A2_LN2_M           | MIPI D-PHY | CSI1 data2 −            |
|      37 | GND                     | Voeding      | Aarde                  |
|      38 | GND                     | Voeding      | Aarde                  |
|      39 | CSI0_A2_LN2_M           | MIPI D-PHY | CSI0 data2 −            |
|      40 | CSI1_NC_CLK_P           | MIPI D-PHY | CSI1-klok +            |
|      41 | CSI0_C1_LN2_P           | MIPI D-PHY | CSI0 data2 +            |
|      42 | CSI1_A0_CLK_M           | MIPI D-PHY | CSI1-klok −            |
|      43 | GND                     | Voeding      | Aarde                  |
|      44 | GND                     | Voeding      | Aarde                  |
|      45 | CSI0_C2_LN3_M           | MIPI D-PHY | CSI0 data3 −            |
|      46 | CSI1_A1_LN1_P           | MIPI D-PHY | CSI1 data1 +            |
|      47 | CSI0_B2_LN3_P           | MIPI D-PHY | CSI0 data3 +            |
|      48 | CSI1_B1_LN1_M           | MIPI D-PHY | CSI1 data1 −            |
|      49 | GND                     | Voeding      | Aarde                  |
|      50 | GND                     | Voeding      | Aarde                  |
|      51 | CCI_I2C_SCL0 (GPIO_23)  | 1,8 V MPU   | Camera-aansturing I²C SCL0 |
|      52 | CSI1_B0_LN0_P           | MIPI D-PHY | CSI1 data0 +            |
|      53 | CCI_I2C_SDA0 (GPIO_22)  | 1,8 V MPU   | Camerabesturing I²C SDA0 |
|      54 | CSI1_C0_LN0_M           | MIPI D-PHY | CSI1 data0 −            |
|      55 | GND                     | Voeding      | Aarde                  |
|      56 | GND                     | Voeding      | Aarde                  |
|      57 | VIN (IN)                | Voeding      | 7-24 V ingang            |
|      58 | +3V3 (OUT)              | Voeding      | 3,3 V-uitgang         |
|      59 | VIN (IN)                | Voeding      | 7-24 V ingang            |
|      60 | +3V3 (OUT)              | Voeding      | 3,3 V-uitgang         |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Opmerking: MIPI CSI/DSI-banen zijn D-PHY-differentiaalparen en geen algemene I/O. Besturingslijnen (CCI_I2C_*, SOC_CAM_MCLK*) behoren tot het 1,8 V MPU-domein. VIN op JMEDIA is de ruwe 7-24 V-ingang (alleen voeding).
</div>

<div style="page-break-after: always;"></div>

### Qwiic (A4) (QWIIC1) - Pinindeling

| **Pin** | **Benaming** | **Netwerk / Functie** | **Domein** | **Opmerkingen**                |
|--------:|-----------------|--------------------|------------|--------------------------|
|       1 | GND             | Aarde             | Voeding      | -                        |
|       2 | +3V3 OUT        | PWR_3P3V           | Voeding      | Voeding voor Qwiic-apparaten |
|       3 | SDA             | PD13 (I2C4_SDA)    | 3,3 V      | -                        |
|       4 | SCL             | PD12 (I2C4_SCL)    | 3,3 V      | -                        |

### JSPI (A5) (JSPI1) - Pinindeling

| **Pin** | **Benaming** | **Netwerk / Functie** | **Domein** | **Opmerkingen**  |
|--------:|-----------------|--------------------|------------|------------|
|       1 | MISO            | PC2 (SPI2_MISO)    | 3,3 V      | -          |
|       2 | +5V             | 5V_USB_VBUS        | Stroom      | Alleen stroom |
|       3 | SCK             | PD1 (SPI2_SCK)     | 3,3 V      | -          |
|       4 | MOSI            | PC3 (SPI2_MOSI)    | 3,3 V      | -          |
|       5 | RESET           | MCU_NRST           | 3,3 V      | -          |
|       6 | GND             | Aarde             | Voeding      | -          |

### JCTL (A1) (JCTL1) - Aansluitingsoverzicht

| **Pin** | **Benaming** | **Netwerk / Functie**        | **Domein** | **Opmerkingen**          |
|--------:|-----------------|---------------------------|------------|--------------------|
|       1 | GND             | Aarde                    | Voeding      | -                  |
|       2 | USB_BOOT        | Opstartspanning                | 1,8 V      | -                  |
|       3 | VOL_DOWN        | GPIO_36                   | 1,8 V      | GPIO               |
|       4 | SOC_SE4_TX      | Console UART TX (SE4)     | 1,8 V      | Systeemconsole     |
|       5 | VOL_UP          | GPIO_96                   | 1,8 V      | GPIO               |
|       6 | SOC_SE4_RX      | Console UART RX (SE4)     | 1,8 V      | Systeemconsole     |
|       7 | GND             | Aarde                    | Voeding      | -                  |
|       8 | PMIC_RESET      | PM4125-reset              | 1,8 V      | -                  |
|       9 | +1V8 OUT        | VREG_L15A_1P8V            | Voeding      | 1,8 V-referentie    |
|      10 | VBUS_DISABLE    | VBUS-voedingsschakelaar uitschakelen | 1,8 V      | Regelt het VBUS-pad |

<div style="page-break-after: always;"></div>

### JDIGITAL (A2) (JDIGITAL1) - Pinindeling

| **Pin** | **Benaming** | **MCU-pin** | **Functies**                               | **Domein** | **Opmerkingen**                   |
| ------: | --------------- | ----------- | ------------------------------------------- | ---------- | --------------------------- |
|       1 | D0              | PB7         | - USART1_RX <br></br>- TIM4_CH2             | 3,3 V      | UART                        |
|       2 | D1              | PB6         | - USART1_TX <br></br>- TIM4_CH1             | 3,3 V      | UART                        |
|       3 | D2              | PB3         | - TIM2_CH2                                  | 3,3 V      | -                           |
|       4 | ~D3             | PB0         | - OPAMP2_OUTPUT <br></br>- TIM3_CH3         | 3,3 V      | PWM / niet 5 V-bestendig      |
|       5 | D4              | PA12        | - FDCAN1_TX <br></br>- TIM1_ETR             | 3,3 V      | -                           |
|       6 | ~D5             | PA11        | - FDCAN1_RX <br></br>- TIM1_CH4             | 3,3 V      | PWM                         |
|       7 | ~D6             | PB1         | - TIM3_CH4                                  | 3,3 V      | PWM                         |
|       8 | D7              | PB2         | - TIM8_CH4N                                 | 3,3 V      | -                           |
|       9 | D8              | PB4         | - TIM3_CH1                                  | 3,3 V      | -                           |
|      10 | ~D9             | PB8         | - TIM4_CH3                                  | 3,3 V      | PWM                         |
|      11 | ~D10            | PB9         | - SPI2_SS (Chip Select) <br></br>- TIM4_CH4 | 3,3 V      | PWM                         |
|      12 | ~D11            | PB15        | - SPI2_MOSI <br></br>- TIM1_CH3N            | 3,3 V      | PWM                         |
|      13 | D12             | PB14        | - SPI2_MISO <br></br>- TIM1_CH2N            | 3,3 V      | -                           |
|      14 | D13             | PB13        | - SPI2_SCK <br></br>- TIM1_CH1N             | 3,3 V      | -                           |
|      15 | GND             | -           | - Aarde                                    | Voeding      | -                           |
|      16 | AREF            | -           | - Analoge referentie                          | -          | Analoge referentie-pin (geen GPIO) |
|      17 | D20             | PB11        | - I2C2_SDA <br></br>- TIM2_CH4              | 3,3 V      | -                           |
|      18 | D21             | PB10        | - I2C2_SCL <br></br>- TIM2_CH3              | 3,3 V      | -                           |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Alle JDIGITAL-lijnen werken op 3,3 V-logica. De meeste pinnen gebruiken een FT-type I/O-structuur en zijn als ingang 5 V-tolerant. D3 (PB0) gebruikt een TT-type I/O-structuur en is slechts 3,6 V-tolerant; leg in geen enkele modus 5 V aan op deze pin.
</div>

### JANALOG (A3) (JANALOG1) - Pinindeling

| **Pin** | **Benaming** | **Net / MCU-pin** | **Functies**                                            | **Domein**     | **Opmerkingen**                     |
|--------:|-----------------|-------------------|----------------------------------------------------------|----------------|-------------------------------|
|       1 | BOOT            | MCU_BOOT0         | - Bootstrap                                             | 3,3 V          | -                             |
|       2 | IOREF           | PWR_3P3V          | - I/O-spanningsreferentie (spiegelt de 3,3 V-spanningsrail)             | Voeding          | Alleen uitgang; geen terugvoeding |
|       3 | RESET           | MCU_NRST          | - MCU-reset                                              | 3,3 V          | -                             |
|       4 | +3V3 OUT        | PWR_3P3V          | - 3,3 V-voeding                                           | Voeding          | -                             |
|       5 | +5V USB VBUS    | 5V_USB_VBUS       | - 5 V-voeding (doorvoer)                              | Stroom          | Alleen stroom                    |
|       6 | GND             | GND               | - Aarde                                                 | Voeding          | -                             |
|       7 | GND             | GND               | - Aarde                                                 | Voeding          | -                             |
|       8 | VIN IN          | DC_IN             | - 7-24 V-ingang                                           | Voeding          | Alleen voeding                    |
|       9 | A0 / D14        | PA4               | - ADC-ingang <br></br>- DAC0 <br></br>- TIM2_CH1          | Analoog / 3,3 V | Directe ADC / niet 5 V-bestendig |
|      10 | A1 /  D15       | PA5               | - ADC-ingang <br></br>- DAC1 <br></br>- TIM3_CH1          | Analoog / 3,3 V | Directe ADC / niet 5 V-bestendig |
|      11 | A2 /  D16       | PA6               | - ADC-ingang <br></br>- OPAMP2_INPUT+ <br></br>- TIM3_CH2 | Analoog / 3,3 V |                               |
|      12 | A3 /  D17       | PA7               | - ADC-ingang <br></br>- OPAMP2_INPUT−                     | Analoog / 3,3 V | -                             |
|      13 | A4 /  D18       | PC1               | - ADC-ingang <br></br>- I2C3_SDA <br></br>- LPTIM1_CH1    | Analoog / 3,3 V | -                             |
|      14 | A5 /  D19       | PC0               | - ADC-ingang <br></br>- I2C3_SCL <br></br>- LPTIM1_IN1    | Analoog / 3,3 V | -                             |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  A0 (PA4) en A1 (PA5) zijn directe ADC-ingangen van de STM32U585 die zijn gekoppeld aan <code>VREF+.</code> Ze zijn niet bestand tegen 5 V. Het geldige ingangsbereik is <code>0-VREF+</code> (≈3,3 V). Het absolute maximum op de pin is <code>VDD + 0,3 V</code>, ongeveer 3,6 V. Boven dit niveau beginnen de interne beveiligingsdiodes van de MCU te geleiden. De header biedt ook <code>5V_SYS-</code> en <code>PWR_3P3V-voedingspinnen</code>, die alleen bedoeld zijn voor de stroomvoorziening. Breng geen 5 V aan op <strong>A0</strong> of <strong>A1</strong>. IOREF is aangesloten op de 3,3 V-rail (<code>PWR_3P3V</code>) en dient als referentie/uitgang voor shields. Het mag niet worden gebruikt om stroom terug te voeren naar het bord.
</div>

## Snelle randapparatuur

- **USB-C:** USB 3.1 met rolwisselfunctie. DisplayPort Alt-Mode via ANX7625 DSI-naar-DP-bridge. De SuperSpeed-differentiële paren van de connector worden gedeeld tussen DP Alt-Mode en USB 3.1-gegevens. Wanneer DisplayPort Alt-Mode actief is, wordt de USB-gegevenssnelheid verlaagd.

- **Camera:** Vierkanalige **MIPI-CSI-2** (1,8 V I/O).

- **Beeldscherm:** Vierbaans **MIPI-DSI** naar **ANX7625** voor DisplayPort Alt-Mode via USB-C. In de Single-Board Computer (SBC)-modus ondersteunt het bord Full HD-schermen (1920 × 1080p) met een optimale resolutie van 1280 × 720p.

- **Draadloos:** Dual-band Wi-Fi® (802.11a/b/g/n/ac) en Bluetooth® 5.1 op één module.

<div style="page-break-after: always;"></div>

## Gebruik van het apparaat

### Aan de slag - Arduino App Lab

Arduino App Lab [1] is een geïntegreerde editor waarmee je projecten kunt bouwen en uitvoeren op beide processors van het bord. Een project is een **app** die het volgende kan bevatten: 

- Een Python®-programma dat draait op het Linux-systeem (Qualcomm Dragonwing™ QRB2210)
- Een Arduino-programma dat op de microcontroller (MCU) (STM32U585) draait
- Optionele **Brick** (kant-en-klare diensten zoals AI-modellen, webservers of API-clients) die samen met de App worden geïmplementeerd (draait ook op het Linux-systeem).

Apps gebruiken **Bridge** om gegevens uit te wisselen tussen de Linux-kant en de microcontroller.

Je kunt Arduino App Lab op je pc installeren of rechtstreeks op de UNO Q uitvoeren in de Single-Board Computer-modus. Voor deze opstelling wordt de 4 GB LPDDR4X-variant van de UNO Q aanbevolen, zodat je zeker bent van voldoende geheugen voor een stabiele werking en voor toepassingen die veel rekenkracht vragen. Om het bord te gebruiken: 

- Start een kant-en-klaar voorbeeld in Arduino App Lab, pas het aan je wensen aan, of bouw een geheel nieuwe app met de ingebouwde editor.
- Druk op de knop **Run** in Arduino App Lab [1].
- De editor bouwt de Linux-component, programmeert de MCU-sketch, implementeert de geselecteerde Brick en start alles op het bord.
- De logbestanden voor beide kanten zijn beschikbaar in de editor en je kunt herhalen zonder Arduino App Lab te verlaten.

Voor de eerste installatie:

1. Installeer Arduino App Lab [1], start het programma op en sluit de UNO Q aan. Gebruik een **USB-C-datakabel** voor de pc-hostmodus, of sluit het bord gewoon aan op de stroomvoorziening voor de SBC-modus.
2. Het bord controleert automatisch of er updates beschikbaar zijn. Als er updates beschikbaar zijn, wordt je gevraagd deze te installeren. Zodra de update is voltooid, moet je de Arduino App Lab[1] opnieuw opstarten.
3. Tijdens de eerste installatie word je gevraagd om een naam en wachtwoord voor het apparaat in te voeren. Je wordt ook gevraagd om de Wi-Fi®-inloggegevens voor je lokale netwerk op te geven.
4. Om het bord te testen, ga je naar een voorbeeld-app in het gedeelte **"Examples"** van het Arduino App Lab[1] en klik je op de knop "Run" rechtsboven. Je kunt ook een nieuwe app maken in het gedeelte **"Apps"**.
5. Je kunt de status van de app bekijken op het tabblad ‘Console’ van de app.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;"> <p style="text-align: justify;">
<strong>Opmerking:</strong> In de modus <strong>‘PC-hosted’</strong> is een <em>USB-dataverbinding</em> nodig voor de eerste installatie. Daarna kun je het <strong>netwerkdoel</strong> via LAN (SSH) gebruiken. In de modus <strong>‘Single-Board Computer’ (SBC)</strong> is er geen USB-dataverbinding nodig voor de installatie; zet het bord gewoon aan en gebruik het <strong>netwerkdoel</strong> zodra het verbinding heeft met je netwerk. Gebruik voor randapparatuur in de SBC-modus (toetsenbord, muis, USB-camera, microfoon) een USB-C-dongle met externe stroomvoorziening. Wanneer DisplayPort Alt-Mode actief is, wordt de USB-datasnelheid verlaagd.</p>
</div>

Gebruik een USB-C-voeding van 5 V / 3 A en een bijbehorende kabel, of voer stroom aan via de 5 V- of VIN-pinnen zoals beschreven in het [gedeelte over voedingsaansluitingen](#input-power) (USB-C is alleen 5 V / VIN is 7-24 V).

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  De eerste keer opstarten duurt meestal 20 tot 30 seconden terwijl Linux opstart. Wacht tot de opstart-LED-reeks of de LED-matrixanimatie is afgelopen voordat je iets met het bord doet.
</div>

### Bricks

<p style="text-align: justify;"><strong>Bricks</strong> zijn modulaire bouwstenen in Arduino App Lab waarmee je je applicatie kunt uitbreiden zonder de hele onderliggende infrastructuur zelf te hoeven schrijven. Elke Brick bevat kant-en-klare functionaliteit, zoals sensorintegratie, AI-modellen, databases of gebruikersinterfaces, die je zomaar in een project kunt plaatsen. Typische Bricks bieden:</p>

<ul>
  <li>Een AI-model (bijvoorbeeld voor objectclassificatie of het herkennen van trefwoorden)</li>
  <li>Een webinterface of REST API-service</li>
  <li>Een koppeling met een externe gegevensbron</li>
</ul>

<p style="text-align: justify;">Bricks worden samen met de app geïmplementeerd en beheerd via de Linux-kant. De gebruikelijke werkwijze is:</p>

<ol>
  <li>Maak een <strong>app</strong> in Arduino App Lab.</li>
  <li>Kies een <strong>Brick</strong> die de app moet gebruiken.</li>
  <li>Voeg uw Python®-code (Linux) en/of uw Arduino-programma (MCU) toe.</li>
  <li>De Brick moet in je `main.py`-bestand worden geïmporteerd en volgens de API van de Brick worden geïnitialiseerd.</li>
  <li>Klik op <strong>'Run'</strong> om de Linux-app te installeren, de MCU te flashen en je app samen met de bijbehorende Bricks te starten.</li>
  <li><strong>De Bridge</strong> -tool zorgt voor de gegevensuitwisseling tussen Linux en de MCU.</li>
</ol>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Zolang een app is gekoppeld en actief is, kunnen de USB-poorten door het systeem worden bezet. Gebruik Arduino App Lab [1] om de app te installeren en te controleren. Als je externe CLI-tools via USB wilt gebruiken, stop dan de app of koppel het bord los.
</div>

### Hallo wereld

<p style="text-align: justify;">Laten we de UNO Q programmeren met de klassieke Arduino "Hello World" - het <em>Blink LED-example</em>. Zo kun je controleren of het bord goed is aangesloten op Arduino App Lab.</p>

<ol>
  <li>Open de Arduino App Lab. Het begint in het gedeelte <strong>Examples</strong></li>.
  <li>Als je niet in de single-board-computer-modus werkt, <strong>sluit je de UNO Q aan</strong> op je pc.</li>
  <li>Open <em>Blink LED</em>. Bekijk de voorbeeldnotities om te zien hoe de App werkt.</li>
  <li>Klik op <strong>'Run'</strong> en wacht tot het uploaden is voltooid.</li>
</ol>

<p style="text-align: justify;">Je zou nu moeten zien dat het rode kanaal van de ingebouwde RGB-led een seconde lang brandt en vervolgens een seconde lang uitgaat, en dat dit zich herhaaldelijk voordoet. De led wordt aangestuurd door de STM32U585-microcontroller via de Arduino-sketch.</p>

<p style="text-align: justify;">Je kunt beginnen met een lege App of een bestaand example gebruiken. Als je dit voor het eerst doet, raden we het voorbeeld ‘Hello World’ aan om de basisstructuur te leren kennen.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Telkens wanneer u een app start, wordt het microcontrollerprogramma gecompileerd en wordt de Python®-toepassing op het Linux-systeem gestart. Afhankelijk van de complexiteit kan dit tot een minuut duren.
</div>

### Hoe je kunt controleren of de App actief is

<p style="text-align: justify;">Open de <strong>console</strong> in App Lab. Er zijn drie tabbladen:</p>

<ul>
  <li><strong>Opstarten</strong>: logbestanden van de opstartprocedure, inclusief het compileren van de MCU en de Linux-implementatie</li>
  <li><strong>Hoofdscherm (Python®)</strong>: uitvoer van de Python®-toepassing (<code>print()</code>)</li>
  <li><strong>Sketch (microcontroller)</strong>: seriële uitvoer van de Arduino-sketch (<code>Serial.println()</code>)</li>
</ul>

<p style="text-align: justify;">Een App kan weliswaar succesvol worden gestart, maar toch problemen tijdens het draaien vertonen. Controleer het Python®-logboek op fouten. Als er een fout optreedt bij het compileren van de sketch, wordt het starten afgebroken.</p>

<div style="page-break-after: always;"></div>

### Voedingsschakelaar

<p style="text-align: justify;">De UNO Q is voorzien van<strong> een voedingsknop (JBTN1) </strong>waarmee u het board kunt herstarten..</p> 

![UNO Q Power Button](assets/ABX00162-ABX00173-power-button.png)

<strong>Lang indrukken (≥ 5 sec.):</strong> hiermee start je het Linux-systeem (MPU) opnieuw op. De stroomtoevoer naar het bord wordt hierbij niet onderbroken.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Let op:</strong> Als je de knop lang ingedrukt houdt, wordt de Linux-omgeving opnieuw opgestart en kunnen actieve apps worden onderbroken. Sla je werk op en zorg ervoor dat externe processen veilig worden afgesloten, indien van toepassing. Het bord start automatisch op zodra er stroom op zit. Voor een normale opstart hoef je de knop niet in te drukken.
</div>

### Online informatie

<p style="text-align: justify;">Ontdek gemeenschapsprojecten op Project Hub [3], blader door de Library Reference [4] voor ondersteunde API’s en vind accessoires zoals Qwiic-sensoren, UNO Shield en carrier boards in de Arduino Store [5].</p>

## Technische gegevens

<p style="text-align: justify;">Het bord heeft afmetingen van 68,58 mm × 53,34 mm en is aan de onderzijde niet dikker dan 2 mm, waardoor het op andere Carrier kan worden gestapeld. De omtrek en het gatenpatroon komen overeen met de UNO-vormfactor en zijn daarmee compatibel.</p>

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


| CE                     | Europe – EU Declaration of Conformity                        |
| ---------------------- | ------------------------------------------------------------ |
| Česky [Czech]          | Arduino S.r.l tímto prohlašuje, že tento Radiolan je ve shodě se základními požadavky a dalšími příslušnými ustanoveními směrnice 2014/53/EU. |
| Dansk [Danish]         | Undertegnede Arduino S.r.l erklærer herved, at følgende udstyr Radiolan overholder de væsentlige krav og øvrige relevante krav i direktiv 2014/53/EU. |
| Deutsch [German]       | Hiermit erklärt Arduino S.r.l dass sich das Gerät Radiolan in Übereinstimmung mit den grundlegenden Anforderungen und den übrigen einschlägigen Bestimmungen der Richtlinie 2014/53/EU befindet. |
| Eesti [Estonian]       | Käesolevaga kinnitab Arduino S.r.l seadme Radiolan vastavust direktiivi 2014/53/EU põhinõuetele ja nimetatud direktiivist tulenevatele teistele asjakohastele sätetele. |
| English                | Hereby, Arduino S.r.l, declares that this Radiolan is in compliance with the essential requirements and other relevant provisions of Directive 2014/53/EU. |
| Español [Spanish]      | Por medio de la presente Arduino S.r.l declara que el Radiolan cumple con los requisitos esenciales y cualesquiera otras disposiciones aplicables o exigibles de la Directiva 2014/53/EU. |
| Ελληνική [Greek]       | ΜΕ ΤΗΝ ΠΑΡΟΥΣΑ Arduino S.r.l ΔΗΛΩΝΕΙ ΟΤΙ Radiolan ΣΥΜΜΟΡΦΩΝΕΤΑΙ ΠΡΟΣ ΤΙΣ ΟΥΣΙΩΔΕΙΣ ΑΠΑΙΤΗΣΕΙΣ ΚΑΙ ΤΙΣ ΛΟΙΠΕΣ ΣΧΕΤΙΚΕΣ ΔΙΑΤΑΞΕΙΣ ΤΗΣ ΟΔΗΓΙΑΣ 2014/53/EU. |
| Français [French]      | Par la présente Arduino S.r.l déclare que l'appareil Radiolan est conforme aux exigences essentielles et aux autres dispositions pertinentes de la directive 2014/53/EU. |
| Íslenska [Icelandic]   | Hér með lýsir Arduino S.r.l yfir því að Radiolan er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. |
| Italiano [Italian]     | Con la presente Arduino S.r.l dichiara che questo Radiolan è conforme ai requisiti essenziali ed alle altre disposizioni pertinenti stabilite dalla direttiva 2014/53/EU. |
| Latviski [Latvian]     | Ar šo Arduino S.r.l deklarē, ka Radiolan atbilst Direktīvas 2014/53/EU būtiskajām prasībām un citiem ar to saistītajiem noteikumiem. |
| Lietuvių [Lithuanian]  | Šiuo Arduino S.r.l deklaruoja, kad šis Radiolan atitinka esminius reikalavimus ir kitas 2014/53/EU Direktyvos nuostatas. |
| Malti [Maltese]        | Hawnhekk, Arduino S.r.l, jiddikjara li dan Radiolan jikkonforma mal-ħtiġijiet essenzjali u ma provvedimenti oħrajn relevanti li hemm fid-Dirrettiva 2014/53/EU. |
| Magyar [Hungarian]     | Alulírott, Arduino S.r.l nyilatkozom, hogy a Radiolan megfelel a vonatkozó alapvetõ követelményeknek és az 2014/53/EU irányelv egyéb elõírásainak. |
| Nederlands [Dutch]     | Hierbij verklaart Arduino S.r.l dat het toestel Radiolan in overeenstemming is met de essentiële eisen en de andere relevante bepalingen van richtlijn 2014/53/EU. |
| Norsk [Norwegian]      | Arduino S.r.l erklærer herved at utstyret Radiolan er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. |
| Polski [Polish]        | Niniejszym Arduino S.r.l oświadcza, że Radiolan jest zgodny z zasadniczymi wymogami oraz pozostałymi stosownymi postanowieniami Dyrektywy 2014/53/EU. |
| Português [Portuguese] | Arduino S.r.l declara que este Radiolan está conforme com os requisitos essenciais e outras disposições da Directiva 2014/53/EU. |
| Slovensko [Slovenian]  | Arduino S.r.l izjavlja, da je ta Radiolan v skladu z bistvenimi zahtevami in ostalimi relevantnimi določili direktive 2014/53/EU. |
| Slovensky [Slovak]     | Arduino S.r.l týmto vyhlasuje, že Radiolan spĺňa základné požiadavky a všetky príslušné ustanovenia Smernice 2014/53/EU. |
| Suomi [Finnish]        | Arduino S.r.l vakuuttaa täten että Radiolan tyyppinen laite on direktiivin 2014/53/EU oleellisten vaatimusten ja sitä koskevien direktiivin muiden ehtojen mukainen. |
| Svenska [Swedish]      | Härmed intygar Arduino S.r.l att denna Radiolan står I överensstämmelse med de väsentliga egenskapskrav och övriga relevanta bestämmelser som framgår av direktiv 2014/53/EU. |
| **UK**                 | **United Kingdom – UKCA Declaration of Conformity**          |
| United Kingdom<br/>    | Hereby, Arduino S.r.l, declares that this Radiolan is in compliance with the essential requirements and other relevant provisions of The Redio Equipment Regulations 2017. |

The full text of the EU and UKCA declaration of conformity is available at the following internet address: https://docs.arduino.cc/certifications/

Requirements in:

Belgium (BE), Bulgaria (BG), Czech Republic (CZ), Denmark (DK), Germany (DE), Iceland (IS), Estonia (EE), Ireland (IE), Greece (EL), Spain (ES), France (FR), Croatia (HR), Italy (IT), Cyprus (CY), Latvia (LV), Liechtenstein (LI), Lithuania (LT), Luxembourg (LU), Hungary (HU), Malta (MT), Netherlands (NL), Norway (NO), Austria (AT), Poland (PL), Portugal (PT), Romania (RO), Slovenia (SI), Slovakia (SK), Turkey (TR), Finland (FI), Sweden (SE), Switzerland (CH), United Kingdom (North Irland) (UK(NI)), and United Kingdom (UK).

Operations in the 5.15-5.35GHz band are restricted to indoor usage only.

This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

### Radio Equipment Information (RED Compliance)

This radio equipment operates in the following frequency bands and with the maximum radio-frequency power indicated below:

| Radio Technology            | Frequency Band    | Maximum Transmit Power |
| --------------------------- | ----------------- | ---------------------- |
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
| ------------ | ------------------------------------------ |
| Address      | Via Andrea Appiani 25, 20900 Monza (Italy) |

# Documentation Reference

| No.  | Reference                   | Link                                                         |
| :--: | --------------------------- | ------------------------------------------------------------ |
|  1   | Arduino App Lab             | [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software) |
|  2   | Arduino UNO Q Documentation | [https://docs.arduino.cc/hardware/uno-q/](https://docs.arduino.cc/hardware/uno-q/) |
|  3   | Project Hub                 | [https://projecthub.arduino.cc/](https://projecthub.arduino.cc/) |
|  4   | Library Reference           | [https://docs.arduino.cc/libraries/](https://docs.arduino.cc/libraries/) |
|  5   | Arduino Store               | [https://store.arduino.cc/](https://store.arduino.cc/)       |

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
