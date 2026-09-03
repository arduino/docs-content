---
identifier: ABX00162-ABX00173
title: Arduino® UNO Q
type: maker
---

![](assets/featured.png)

# Italiano 

# Descrizione

<p style="text-align: justify;">Arduino® UNO Q (di seguito UNO Q) è un computer a scheda singola che combina il microprocessore (MPU) Qualcomm® Dragonwing™ QRB2210, un Arm® Cortex®-A53 quad-core con sistema operativo Debian Linux, e il microcontrollore (MCU) STM32U585 di STMicroelectronics, un Arm® Cortex®-M33 con Arduino Core su sistema operativo Zephyr. Il sistema Linux e il microcontrollore comunicano tramite Bridge, la libreria RPC (Remote Procedure Call) di Arduino. Questo permette agli sketch Arduino sul microcontrollore di accedere ai servizi Linux per attività di alto livello, mentre le applicazioni Linux possono interagire con le periferiche del microcontrollore per gestire operazioni in tempo reale all’interno dello stesso progetto.</p>

<p style="text-align: justify;">UNO Q è dotata di memoria eMMC integrata (opzioni da 16 GB e 32 GB) e SDRAM LPDDR4X (opzioni da 2 GB e 4 GB) per garantire un funzionamento fluido di Linux e dei tuoi progetti. È dotata di Wi-Fi® 5 dual-band e Bluetooth® 5.1 per la connettività wireless, un connettore USB-C® con ingresso di alimentazione e uscita video, e connettori compatibili con Arduino per una facile espansione con shield, carrier e accessori.</p>

<p style="text-align: justify;">UNO Q si integra perfettamente con Arduino App Lab, consentendo agli sviluppatori di combinare sketch Arduino, applicazioni Linux e modelli di IA in un unico ambiente. App Lab può essere eseguito direttamente sulla scheda o da un PC collegato, offrendo esempi pronti all'uso e la flessibilità necessaria per creare app personalizzate su misura per i tuoi progetti.</p>

# Aree tematiche

Prototipazione, IA e ML per dispositivi edge, visione artificiale, istruzione, dispositivi intelligenti, robotica, domotica e automazione degli edifici, videogiochi

<div style="page-break-after: always;"></div>

# INDICE

## Esempi di applicazione

<p style="text-align: justify;">UNO Q combina un processore Linux con funzionalità di intelligenza artificiale e un microcontrollore in tempo reale, offrendo il meglio dell'elaborazione di alto livello e del controllo deterministico. Oltre a questa doppia architettura, supporta un ampio ecosistema di shield Arduino, schede carrier, Modulino® e accessori di terze parti, rendendola una piattaforma flessibile per diverse applicazioni.</p>

- **Prototipazione:** prototipi rapidi come strumenti di ispezione basati sulla visione artificiale, chioschi intelligenti o computer edge compatti con connettività integrata.

- **Didattica:** Insegnamento di Linux, programmazione in tempo reale, intelligenza artificiale e visione artificiale attraverso un approccio didattico basato sui progetti, dagli esperimenti scientifici ai robot didattici interattivi.

- **Robotica:** robot di consegna autonomi, assistenti in grado di seguire i gesti e bracci robotici con feedback visivo, che combinano la visione artificiale basata su Linux con il controllo dei motori tramite microcontrollore.

- **Dispositivi smart per applicazioni pubbliche:** telecamere intelligenti fai-da-te, display interattivi o progetti di realtà aumentata basati su doppia fotocamera e accelerazione GPU.

- **Automazione per casa ed edifici:** campanelli intelligenti con riconoscimento facciale, sistemi a comando vocale e sistemi di climatizzazione personalizzati.

- **Giochi:** emulazione di console retrò, cabinati arcade personalizzati o un'esperienza di gioco migliorata grazie a comandi basati sui gesti, tracciamento del volto e feedback in tempo reale.

<div style="page-break-after: always;"></div>

## Caratteristiche

### Varianti di UNO Q

UNO Q è disponibile in due versioni:

- **ABX00162**: 2 GB di RAM, 16 GB di memoria integrata
- **ABX00173**: 4 GB di RAM, 32 GB di memoria interna

### Panoramica delle specifiche generali

#### Elaborazione e memoria

![](assets/ABX00162-ABX00173-main-components.png)

| **Subsystem**      | **Dettagli**                                                 |
| ------------------ | ------------------------------------------------------------ |
| MPU principale     | - Qualcomm Dragonwing™ QRB2210 - System-on-Chip (SoC) (MPU) (SOC1): 4 × Arm Cortex-A53 a 2,0 GHz, 64 bit <br></br>- GPU Adreno 702 a 845 MHz (grafica 3D) <br></br>- Doppio ISP: 13 MP + 13 MP o 25 MP a 30 fps <br></br>- Sistema operativo Debian (supporto upstream) <br></br>- I/O: USB 3.1 con funzionalità di commutazione dei ruoli tramite connettore USB, SDIO 3.0, MIPI-CSI-2 a 4 corsie e MIPI-DSI a 4 corsie |
| MCU in tempo reale | - ST STM32U585 (MCU) (MCU1), Arm Cortex-M33 fino a 160 MHz <br></br>- Arduino Core su Zephyr OS <br></br>- 2 MB di memoria Flash, 786 kB di SRAM |
| Memoria di sistema | - Opzioni eMMC da 16 o 32 GB (EMMC1) per sistema operativo/dati <br></br>- Opzioni LPDDR4X da 2 GB o 4 GB (single-rank, 32 bit) (DRAM1) |

<p style="text-align: justify;">Il chip I/O Qualcomm Dragonwing™ QRB2210 funziona a 1,8 V.
L'MPU gestisce le interfacce della fotocamera MIPI-CSI-2 e del display MIPI-DSI su JMEDIA, nonché i terminali GPIO e audio a 1,8 V dell'MPU (SoC) esposti su JMISC.
JMISC è un connettore a tensione mista che trasporta segnali MCU a 3,3 V e audio analogico insieme alle linee MPU a 1,8 V. Il segnale video DisplayPort è fornito dal circuito integrato ANX7625 integrato, che converte il segnale MIPI-DSI dell'MPU in modalità alternativa DisplayPort su USB-C.
L'STM32U585 gestisce l'ADC, il PWM, il CAN, la matrice LED e i connettori da 3,3 V (JDIGITAL, JANALOG, JSPI e Qwiic).</p>


#### Connettività e contenuti multimediali

![](assets/ABX00162-ABX00173-comm-components.png)

| **Subsystem**       | **Dettagli**                                                 |
| ------------------- | ------------------------------------------------------------ |
| Modulo wireless     | - WCBN3536A (Qualcomm WCN3980) (U2901) <br></br>- Wi-Fi® 5 802.11a/b/g/n/ac (dual-band) + Bluetooth® 5.1 |
| Porta USB-C (JUSB1) | - USB 3.1 con funzionalità di commutazione dei ruoli<br></br>- Modalità alternativa DisplayPort tramite il bridge DSI-DP ANX7625 (U3001) (le coppie differenziali SuperSpeed sul cavo Type-C vengono instradate per la modalità alternativa DP)<br></br>- Uscita video (modalità SBC): supporta display Full HD (1920 × 1080p); la risoluzione ottimale è 1280 × 720p<br></br>- La negoziazione USB Power Delivery richiede solo un contratto **5 V / 3 A** (nessun profilo a tensione più alta)<br></br>- Protezione VBUS con interruttore di carico/back-drive (Q2801) |

Il modulo wireless utilizza SDIO per i dati Wi-Fi® e un'interfaccia UART per il controllo Bluetooth®, con un'antenna integrata nel circuito stampato.

#### Espansione e Connettori

![](assets/ABX00162-ABX00173-header-expansion.png)

| **Interfaccia (connettore)** | **Tensione e numero di pin**     | **Dettagli**                                                 |
| ---------------------------- | -------------------------------- | ------------------------------------------------------------ |
| JMEDIA (JMEDIA1)             | Segnali a 1,8 V, 60 pin          | - Linee per telecamera/display ad alta velocità (MIPI DSI, CSI) <br></br>- Bus di controllo della telecamera (CCI I²C) - dedicato, non GPIO generico <br></br>- Clock della telecamera (SOC_CAM_MCLK0/1) <br></br>- Trasporta anche linee di alimentazione (+3V3 OUT, VIN IN) e GND |
| JMISC (JMISC1)               | Misto 1,8 V / 3,3 V, 60 pin      | - Misto GPIO e SDIO <br></br>- Periferiche MCU: SDMMC1, TRACE, PSSI (telecamera parallela), I²C4, MCO/CRS_SYNC, pin OPAMP1 <br></br>- Endpoint audio: Mic2 INP/INM/BIAS, Cuffie L/R + REF, LineOut P/M, Auricolare P/R, HS_DET <br></br>- Banchi GPIO MPU (SoC) (SE0) a 1,8 V <br></br>- Trasporta anche i rail di alimentazione (+5V USB OUT, +3V3 OUT, +1V8 OUT, VBAT OUT, VCOIN IN) e GND |
| JCTL (JCTL1)                 | 1,8 V, 10 pin                    | - Console UART SE4 <br></br>- Ingresso avvio USB forzato <br></br>- Ingresso reset PMIC <br></br>- Disabilitazione interruttore di alimentazione VBUS <br></br>- Rotaia da 1,8 V e GND |
| JDIGITAL (JDIGITAL1)         | 3,3 V, 18 pin                    | - I/O digitale per SPI, I²C, UART, PWM, CAN                  |
| JANALOG (JANALOG1)           | 3,3 V, 14 pin                    | - I/O analogici <br></br>- Canali ADC e riferimenti          |
| JSPI (JSPI1)                 | Logica a 3,3 V,  6 pin + 5 V SYS | - SPI dedicato: MOSI, MISO, SCLK <br></br>- Reset MCU (NRST) <br></br>- Massa <br></br>- SYS a 5 V (diode-OR output) |
| Qwiic (QWIIC1)               | 3,3 V, 4 pin                     | - I²C (ecosistema Qwiic)                                     |

### Prodotti correlati

- Shield per Arduino UNO attraverso JDIGITAL e JANALOG
- Carrier compatibili con UNO Q
- Cavo USB-C completo a 24 pin
- Adattatore USB-C con funzione di alimentazione esterna

<div style="page-break-after: always;"></div>

## Specifiche Tecniche

### Potenza in ingresso

![UNO Q Input Methods](assets/ABX00162-ABX00173-power-supply.png)

| **Fonte**   | **Intervallo di tensione** | **Corrente massima** | **Connettore**        |
| ----------- | -------------------------: | -------------------: | --------------------- |
| USB-C VBUS  |                        5 V |           fino a 3 A | Connettore USB-C      |
| VIN (DC IN) |                     7-24 V |                    - | JMEDIA, JANALOG (VIN) |
| Pin 5 V (5V_SYS)     |                        5 V |           fino a 3 A | JANALOG, JMISC, JSPI                |

<p style="text-align: justify;">UNO Q supporta tre tipi di alimentazione: una porta USB-C, un ingresso da 7-24 V CC e il pin <code>5V_SYS</code> disponibile su JANALOG, JMISC o JSPI. Tramite USB Power Delivery, richiede solo il profilo da 5 V / 3 A e non richiede profili PD con tensioni più elevate. Usa un alimentatore e un cavo con valori nominali di 5 V a 3 A per evitare cali di tensione durante brevi picchi di attività, come i burst wireless o l’inizializzazione del display. È anche possibile utilizzare una fonte esterna regolata a  5 V CC per alimentare la scheda tramite il pin <code>5V_SYS</code> su JANALOG, JMISC o JSPI.</p>

<p style="text-align: justify;"><em>Il VBUS USB-C</em> e l'uscita a 5 V del convertitore buck 7-24 V sono combinati <em>tramite un circuito OR a diodi</em> sul bus di sistema a 5 V (<code>5V_SYS</code>). Da <code>5V_SYS</code>, il progetto ricava il nodo del preregolatore a 3,8 V e, successivamente, quello a 3,3 V.
Il PMIC, alimentato da 5V_SYS, genera la tensione di 1,8 V.</p>

<p style="text-align: justify;"><strong>Protezione contro l'inversione di polarità:</strong> verificata con una tensione di -24 V applicata all'ingresso CC (DC IN). Il funzionamento è garantito solo con la polarità corretta. Non applicare tensione inversa durante il normale utilizzo.</p>

<p style="text-align: justify;"><strong>Percorso OR Schottky:</strong> la caduta di tensione in avanti dall'uscita del buck a <code>5V_SYS</code> è stata misurata come segue (iniezione VIN tramite JANALOG, alimentatore Rigol DP832 in serie, misurazione con Keithley DMM6500, carico attivo 8542B). La dissipazione di potenza è calcolata come <code>P = I × Vf</code>.</p>

| **Corrente di carico** | **Caduta di tensione diretta (`Vf`)** | **Dissipazione del diodo** |
| ---------------------: | ------------------------------------: | -------------------------: |
|                  1.0 A |                                0.35 V |                     0.35 W |
|                  1.5 A |                                0.37 V |                     0.56 W |
|                  2.0 A |                                0.39 V |                     0.78 W |

### Condizioni operative consigliate

Usa i limiti riportati di seguito per dimensionare le fonti di alimentazione, definire le tolleranze delle linee di alimentazione e pianificare il margine termico:

| **Parametro**                  | **Simbolo** | **Minimo** | **Tipico** | **Massimo** | **Unità** |
| ------------------------------ | ----------- | :--------: | :--------: | :---------: | :-------: |
| Ingresso USB-C                 | `VBUS_USBC` |    4,5     |    5,0     |     5,5     |     V     |
| Ingresso CC                    | `DC_IN`     |    7,0     |     -      |    24,0     |     V     |
| Linea di alimentazione a 3,3 V | `PWR_3P3V`  |    3,1     |    3,3     |     3,5     |     V     |
| Temperatura di funzionamento   | `T_OP`      |    -10     |     -      |     60      |    °C     |

<p style="text-align: justify;"><em>Il valore minimo</em> indica il valore continuo più basso per il funzionamento normale; brevi cali possono causare reset o interruzioni del collegamento. <em>Il valore tipico</em> corrisponde al punto di progetto nominale. <em>Il valore massimo</em> non deve essere superato. Per <code>DC_IN</code> (7-24 V), scegli un'alimentazione che copra ampiamente il carico a 5 V e usa cavi corti per ridurre la caduta di tensione. L'intervallo <code>PWR_3P3V</code> riflette la tolleranza del regolatore e il carico. L'intervallo di temperatura si riferisce all'aria ambiente vicino alla scheda, e operare vicino ai limiti può ridurre la corrente di uscita disponibile.</p>

### Linee di alimentazione sulla scheda

| **Tensione** | **Linea**        | **Origine / Regolatore**                                     |
| -----------: | ---------------- | ------------------------------------------------------------ |
|        5,0 V | `5V_SYS`         | OR a diodi tra VBUS USB-C e uscita buck 7-24 V (entrambe tramite raddrizzatori Schottky) |
|        3,8 V | `PWR_3P8V`       | Convertitore step-down (buck) da `5V_SYS`                    |
|        3,3 V | `PWR_3P3V`       | Convertitore step-down (buck) da `PWR_3P8V`                  |
|        1,8 V | `VREG_L15A_1P8V` | LDO PM4125 L15A  da `5V_SYS`                                 |

<div style="page-break-after: always;"></div>

## Panoramica delle funzionalità

### Schema dei pin

![](assets/ABX00162-ABX00173_pinout.png)

### Diagramma a blocchi

![](assets/ABX00162-ABX00173_block_diagram.png)

### Alimentazione

<p style="text-align: justify;">UNO Q supporta due tipi di alimentazione: una porta USB-C e un ingresso CC da 7-24 V. 
<em>Il VBUS USB-C</em> e l'uscita a 5 V del convertitore buck da 7-24 V sono collegati <em>in OR tramite diodi</em> al bus di sistema a 5 V (5V_SYS).</p>
<p style="text-align: justify;"><code>5V_SYS</code> alimenta il <strong>PMIC PM4125 (PMIC1)</strong> tramite <code>USB_IN</code>. L'LDO L15A del PMIC fornisce il rail da 1,8 V (<code>VREG_L15A_1P8V</code>) e alimenta i banchi I/O del SoC, l'ANX7625 DVDD18, la logica digitale Wi-Fi® e i level shifter integrati. Il rail da 1,8 V è disponibile anche su JMISC. Da <code>5V_SYS</code>, un buck genera il <code>PWR_3P8V</code> (3,8 V) riservato alla progettazione del sistema e alle funzionalità future. Un secondo buck genera <code>PWR_3P3V</code> per l'STM32U585, l'ANX7625 (linee da 3,3 V), il dominio Wi-Fi® a 3,3 V e i pin dell'header a 3,3 V.</p>
<p style="text-align: justify;">Un <em>MOSFET a canale P protetto</em> (<code>Q2801</code>) può fornire <code>tensione VBUS</code> USB da <code>5V_SYS</code> quando la scheda funziona come host USB/OTG. Il <code>VCOIN</code> alimenta solo il real-time clock del PMIC e non alimenta i domini Linux o MCU. Il <code>VBAT</code> si collega al <code>PWR_3P8V</code> ed è riservato alla progettazione del sistema e a funzionalità future. </p>

![Arduino UNO Q Power Tree](assets/ABX00162-ABX00173_power_tree.png)

<div style="page-break-after: always;"></div>

## Interfaccia utente e indicatori

![](assets/ABX00162-ABX00173-leds.png)

- **LED RGB (controllati da Linux):** Due LED tricolori sono gestiti dal processore applicativo Qualcomm Dragonwing™ QRB2210 e accessibili tramite `/sys/class/leds/`.

  - **LED RGB 1 (D27301):** canali: `red:user` → **GPIO_41**, `green:user` → **GPIO_42**, `blue:user` → **GPIO_60**.

  - **LED RGB 2 (D27302):** canali: `red:panic` → **GPIO_39**, `green:wlan` → **GPIO_40**, `blue:bt` → **GPIO_47**.

    Di default, il LED RGB 2 indica lo stato del sistema, `PANIC`, `WLAN` e `BT`, ma può anche essere controllato dall'utente. La frequenza PWM è di circa 2 kHz per garantire transizioni di colore fluide.

- **LED RGB (controllati da MCU):** Due LED tricolori sono pilotati dal microcontrollore STM32U585.

  - **RGB LED 3 (D27401):** `LED3_R` → **PH10**, `LED3_G` → **PH11**, `LED3_B` → **PH12**.
  - **RGB LED 4 (D27402):** `LED4_R` → **PH13**, `LED4_G` → **PH14**, `LED4_B` → **PH15**.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  I LED RGB sono di tipo "active-low", il che significa che si accendono quando ricevono un segnale logico `0`.
</div>
- **Matrice LED (D27001..D27104):** matrice LED monocromatica blu 8 × 13 (104 pixel) pilotata dall'STM32U585. Visualizza il logo di avvio per circa 20–30 secondi durante l'avvio di Linux. Accedere alla matrice prima che l'avvio sia completato potrebbe interferire con il funzionamento dell'MCU.

- **LED di alimentazione (D27201):** Indicatore verde collegato alla linea a 3,3 V che si accende ogni volta che la scheda è alimentata.

## MPU e MCU

<p style="text-align: justify;">
Un MPU (unità microprocessore) è un processore applicativo ad alte prestazioni progettato per eseguire un sistema operativo completo e software complessi. Un MCU (unità microcontrollore) è un controller compatto ed efficiente dal punto di vista energetico, pensato per garantire tempi di risposta rapidi e precisi nelle operazioni di I/O e di controllo. UNO Q combina entrambi per abbinare l'elaborazione a livello di sistema operativo con un controllo a rapida risposta su una scheda a scheda singola e comunicare tramite Bridge, un livello RPC implementato su entrambi i lati.</p>


### Processore applicativo (MPU)

<p style="text-align: justify;">
Qualcomm® Dragonwing™ QRB2210 è un processore quad-core Arm® Cortex®-A53 che gira con il sistema operativo Debian Linux. Le sue interfacce I/O funzionano a 1,8 V e gestiscono i contenuti multimediali ad alta velocità e le politiche relative a Type-C/PD.
</p>


<ul>
  <li>Intervallo di tensione: 1,8 V per le interfacce GPIO e ad alta velocità dell'MPU (SoC)</li>
  <li>Supporta JMEDIA: canali MIPI-CSI-2 per la telecamera e MIPI-DSI per il display</li>
  <li>Gestisce i pin GPIO e gli endpoint audio dell'MPU a 1,8 V su JMISC (connettore a tensione mista)</li>
  <li>USB-C: cambio di ruolo e negoziazione PD (richiesta di 5 V / 3 A)</li>
  <li>Uscita DisplayPort tramite ANX7625 integrato (converte MIPI-DSI in DP Alt-Mode)</li>
</ul>


### Microcontrollore in tempo reale (MCU)

<p style="text-align: justify;">
STMicroelectronics® STM32U585 è un processore Arm® Cortex®-M33 che esegue Arduino Core sul sistema operativo Zephyr. Offre un  controllo veloce e preciso e connettori I/O a 3,3 V.
</p>


<ul>
  <li>Dominio di tensione: 3,3 V per GPIO e analogico (VREF+ ≈ 3,3 V)</li>
  <li>Gestisce ADC, PWM, CAN, matrice LED e timer</li>
  <li>Supporta connettori da 3,3 V: JDIGITAL, JANALOG, JSPI, Qwiic</li>
</ul>


<p style="text-align: justify;">
JMISC gestisce entrambi i domini: le linee MPU a 1,8 V coesistono con i segnali MCU a 3,3 V (ad es. PSSI, SDMMC1, TRACE, I²C4) e con i segnali analogici/audio. Ti preghiamo di verificare i livelli di tensione quando colleghi schede carrier o circuiti logici esterni.
</p>


## Comunicazione tra processori

<p style="text-align: justify;">Qualcomm® Dragonwing™ QRB2210 (MPU) e l'STM32U585 (MCU) comunicano tramite l'Arduino Bridge, un livello software di chiamata di procedura remota (RPC) implementato sia sul lato Linux che su quello dell'MCU. Bridge fornisce un'API orientata ai servizi che permette a entrambi i processori di esporre servizi che l'altro può chiamare, supportando al contempo notifiche unidirezionali per eventi asincroni. Gestisce l'instradamento dei messaggi tra i processori e supporta diversi trasporti fisici. Attraverso la sua API, Bridge consente chiamate di funzione type-safe, permettendo agli sketch del microcontrollore di invocare servizi Linux e ricevere risposte strutturate, oppure di inviare dati tramite notifiche.</p>

<p style="text-align: justify;">Se serve un indicatore hardware per una scheda carrier o una logica esterna, il firmware può dedicare un GPIO MPU di 1,8 V su JMISC, oppure un GPIO JCTL se disponibile, come uscita pronta o come wake output. Questo segnale può essere ricevuto su un GPIO dell'MCU tramite circuiti  di livello compatibile, come un level shifter o una configurazione open-drain con un resistore pull-up. Il firmware definisce il ruolo esatto di questo segnale. In alternativa, l'attività sul trasporto selezionato (USB CDC, UART o SPI) può fungere da sorgente di riattivazione quando l'MCU è in modalità sleep.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  I segnali GPIO dell'MPU funzionano nel dominio a bassa tensione del processore dell'applicazione (1,8 V). Assicurati che qualsiasi collegamento al microcontrollore sia compatibile in termini di livello con la sua tensione di I/O (3,3 V). Ad esempio, usa un convertitore di livello o una configurazione open-drain con un pull-up verso il rail I/O del microcontrollore.
</div>


<div style="page-break-after: always;"></div>

## Accelerazione hardware

<p style="text-align: justify;">L'UNO Q offre accelerazione hardware sia per la grafica 3D che per la codifica e la decodifica video grazie alla GPU Adreno 702 integrata, che funziona a 845 MHz.</p>

### Accelerazione grafica

<p style="text-align: justify;">La GPU Adreno 702 offre un rendering grafico 3D con accelerazione hardware tramite i driver open source Mesa. Le applicazioni possono accedere all'accelerazione GPU tramite API grafiche standard, tra cui OpenGL, OpenGL ES, Vulkan e OpenCL.</p>

| **API grafica**    | **Driver** | **Supporto hardware** | **Versione attuale del driver** | **Nome del dispositivo** |
| ------------------ | ---------- | --------------------- | ------------------------------- | ------------------------ |
| OpenGL per desktop | freedreno  | -                     | 3.1                             | FD702                    |
| OpenGL ES          | freedreno  | 3.1                   | 3.1                             | FD702                    |
| Vulkan             | turnip     | 1.1                   | 1.0.318                         | Turnip Adreno (TM) 702   |
| OpenCL             | Mesa       | 2.0                   | 2.0                             | -                        |

<p style="text-align: justify;">La GPU Adreno 702 presenta un'architettura a memoria unificata, che condivide la RAM di sistema con la CPU per il trasferimento dei dati. Supporta l'indirizzamento della memoria a 64 bit e offre funzionalità di rendering diretto per prestazioni grafiche ottimali.</p>

| **Parametro**                         | **Specifiche**                              |
| ------------------------------------- | ------------------------------------------- |
| Frequenza di clock                    | 845 MHz                                     |
| Architettura di memoria               | Unificata (condivisa con la RAM di sistema) |
| Memoria video disponibile             | 1740 MB                                     |
| Indirizzamento della memoria          | 64 bit                                      |
| Rendering diretto                     | Sì                                          |
| Dimensione massima della texture 2D   | 16384 × 16384 pixel                         |
| Dimensione massima della texture 3D   | 2048³ voxel                                 |
| Dimensione massima della mappa cubica | 16384 × 16384 pixel                         |
| OpenGL Shading Language (GLSL)        | 1.40                                        |
| Linguaggio di shading OpenGL ES       | 3.10 ES                                     |

<p style="text-align: justify;">Lo stack grafico Mesa offre il supporto per le estensioni e le funzionalità standard di OpenGL. Le applicazioni che utilizzano OpenGL, OpenGL ES o Vulkan ricorreranno automaticamente all'accelerazione hardware senza bisogno di ulteriori configurazioni. Le utility grafiche standard, come <code>mesa-utils</code> e <code>vulkan-tools</code>, funzionano immediatamente su UNO Q.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Nota:</strong> i driver OpenGL e Vulkan sono disponibili tramite i driver Mesa open source <strong>freedreno (OpenGL/OpenGL ES)</strong> e <strong>turnip (Vulkan)</strong>, che garantiscono trasparenza e supporto da parte della comunità. Sebbene l'hardware Adreno 702 supporti Vulkan 1.1, l'attuale implementazione del driver fornisce Vulkan 1.0.318. <strong>Non ci sono esempi OpenGL o Vulkan specifici per UNO Q. Tuttavia, le utility standard di Mesa e gli esempi del progetto Mesa possono essere utilizzati come riferimento.</strong>
</div>


### Accelerazione video

<p style="text-align: justify;">La GPU Adreno 702 include codificatori e decodificatori video hardware dedicati, accessibili tramite l'API <code>V4L2 (Video4Linux2)</code> attraverso i dispositivi <code>/dev/video0</code> e <code>/dev/video1</code>. L'accelerazione hardware è disponibile per i seguenti codec video:</p>

| **Codec**    | **Codifica** | **Decodifica** | **Elemento GStreamer**    |
| ------------ | ------------ | -------------- | ------------------------- |
| H.264 (AVC)  | Sì           | Sì             | v4l2h264enc / v4l2h264dec |
| H.265 (HEVC) | Sì           | Sì             | v4l2h265enc / v4l2h265dec |
| VP9          | No           | Sì             | v4l2vp9dec                |

<p style="text-align: justify;">L'encoder e il decoder video hardware trasferiscono le operazioni di compressione e decompressione dalla CPU a un hardware dedicato, consentendo un'elaborazione video efficiente in tempo reale. Questo riduce il consumo energetico del sistema e permette alla CPU di concentrarsi sulla logica dell'applicazione. L'accelerazione hardware è disponibile per risoluzioni fino a 1920×1080 (Full HD), inclusi formati comuni come il 720p (1280×720).</p>

#### Integrazione con GStreamer

<p style="text-align: justify;">L'approccio consigliato per accedere all'accelerazione video hardware è tramite <strong>GStreamer</strong>, che offre un'interfaccia di pipeline di alto livello per i dispositivi V4L2. I seguenti elementi GStreamer consentono l'elaborazione video con accelerazione hardware:</p>

Per la decodifica H.264, puoi usare la seguente pipeline:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h264parse ! v4l2h264dec \
  ! videoconvert ! autovideosink
```

Per la decodifica H.265, puoi usare la seguente pipeline:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h265parse ! v4l2h265dec \
  ! videoconvert ! autovideosink
```

Per la decodifica VP9, puoi usare la seguente pipeline:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.webm \
  ! matroskademux ! queue ! v4l2vp9dec \
  ! videoconvert ! autovideosink
```

Per la codifica H.264, puoi usare la seguente pipeline:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc ! h264parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Per la codifica H.265, puoi usare la seguente pipeline:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1920,height=1080,framerate=30/1 \
  ! v4l2h265enc ! h265parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Per la codifica e la decodifica simultanee, puoi usare la seguente pipeline:

```bash
gst-launch-1.0 -v videotestsrc num-buffers=1000 \
  ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc capture-io-mode=4 output-io-mode=2 ! h264parse \
  ! v4l2h264dec capture-io-mode=4 output-io-mode=2 ! videoconvert \
  ! autovideosink
```

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Accesso per sviluppatori:</strong> È possibile accedere ai dispositivi video V4L2 tramite le API standard di Linux, il che consente l'integrazione diretta nelle applicazioni C/C++ utilizzando libv4l2 o tramite framework di livello superiore come GStreamer, FFmpeg o OpenCV con supporto backend V4L2.
</div>


### Supporto OpenCL

<p style="text-align: justify;">Il supporto per OpenCL 2.0 è disponibile tramite l'implementazione Mesa, consentendo l'elaborazione su GPU generica (GPGPU) per attività di elaborazione parallela, calcolo scientifico e operazioni ad alta intensità di calcolo. Le funzionalità OpenCL dell'Adreno 702 permettono di trasferire i carichi di lavoro ad alta intensità di calcolo dalla CPU alla GPU, migliorando così le prestazioni.</p>

<div style="page-break-after: always;"></div>

## Periferiche

![UNO Q Peripherals](assets/ABX00162-ABX00173_headers.png)

- **JDIGITAL (A2) (JDIGITAL1) / JANALOG (A3) (JANALOG1):** GPIO a 3,3 V con supporto per ingressi SPI, UART, CAN, PWM e ADC. Gli ingressi analogici fanno riferimento a `VREF+` sul rail da 3,3 V. L'intervallo di ingresso valido va da 0 V a `VREF+`. Alcuni pad STM32U585 tollerano 5 V in modalità digitale, tuttavia quando configurati come ADC o qualsiasi funzione analogica (come da *A0* a *A5*), non tollerano 5 V e non devono superare `VDD + 0,3 V`. Per tensioni più elevate, usa un condizionamento esterno come un partitore di tensione o un buffer. Per *A4/A5* quando vengono usati come I2C3 (PC1/PC0), usa solo pull-up a 3,3 V. Inoltre, **~D3 (PB0)** utilizza una struttura I/O di tipo TT ed è tollerante a 3,6 V, ma non è tollerante a 5 V in nessuna modalità, compresa quella digitale.

- **Connettore QWIIC (A4) (QWIIC1):** Bus I²C aggiuntivo (logica a 3,3 V). Viene mappato come **PD13 (I2C4_SDA)** e **PD12 (I2C4_SCL)**. Garantisce la compatibilità plug-and-play con i  Modulino® nodes e con sensori e attuatori di terze parti.

- **JSPI (A5) (JSPI1):** Connettore SPI a 3,3 V per periferiche che fornisce i segnali MOSI, MISO e SCLK, con selezione del chip disponibile tramite un pin GPIO su JDIGITAL/JMISC. I pin utilizzano la configurazione di tipo FT STM32U585 con MISO su PC2, MOSI su PC3 e SCK su PD1. Sono tolleranti a 5 V come ingressi o in open-drain, mentre le uscite pilotano 3,3 V. Aggiungi un convertitore di livello se è richiesta una soglia di ingresso a 5 V o una segnalazione bidirezionale a 5 V. Include un pin di alimentazione `5V_SYS`.

- **JMEDIA (B2) (JMEDIA1):** Segnali video e di visualizzazione a quattro canali nel dominio a 1,8 V (MIPI-CSI-2 e MIPI-DSI).

- **JMISC (B1) (JMISC):** Connettore multifunzione che combina segnali MCU a 3,3 V e segnali MPU a 1,8 V. Fornisce il bus PSSI (telecamera parallela) dell'MCU, i pin di test SDMMC1, TRACE, I2C4, MCO/CRS_SYNC e i pin analogici OPAMP1. Inoltre, dispone di uscite audio (Mic2, Cuffie L/R+REF, LineOut P/M, Auricolare P/R, HS_DET) e linee di alimentazione (+3V3, +5V_SYS, +1V8, VBAT e VCOIN per uso di sistema). Rispetta i domini di tensione: **i pin MCU sono a 3,3 V, i GPIO MPU sono a 1,8 V**.

- **JCTL (A1) (JCTL1):** Pin boot, reset e segnali di riattivazione a basso consumo (logica a 1,8 V).

<p style="text-align: justify;"><strong>SE4 UART</strong> è la console di sistema (<code>shell UART</code>). È separata dalle UART delle applicazioni e non dovrebbe essere utilizzata per le operazioni di I/O dell'utente. Funziona nel dominio I/O <strong>a 1,8 V</strong> dell'MPU.</p>

<p style="text-align: justify;">Non utilizzare le linee del Qualcomm Dragonwing™ QRB2210 riservate a <strong>I²C</strong>, <strong>JMEDIA CCI</strong> (Camera Control Interface) o <strong>MI2S0</strong> (bus audio I²S) come I/O generici. Questi segnali sono dedicati all'interfaccia, funzionano a <strong>1,8 V</strong> e sono riservati nell'albero dei dispositivi Linux. I connettori li rendono disponibili solo per quelle funzioni.</p>

### JMISC (B1) (JMISC1) - Schema dei pin

| **Pin** | **Denominazione** | **Pin MCU/SoC** | **Dominio**   | **Note**                                                     |
| ------: | ----------------- | --------------- | ------------- | ------------------------------------------------------------ |
|       1 | MCU_PSSI_D0       | PC6             | MCU a 3,3 V   | PSSI D0                                                      |
|       2 | MCU_SDMMC1_CMD    | PD2             | MCU a 3,3 V   | Comando/test SDMMC1                                          |
|       3 | MCU_PSSI_D1       | PC7             | MCU a 3,3 V   | PSSI D1                                                      |
|       4 | MCU_TRACE_CLK     | PE2             | MCU a 3,3 V   | Clock di tracciamento                                        |
|       5 | MCU_PSSI_D2       | PC8             | MCU a 3,3 V   | PSSI D2                                                      |
|       6 | MCU_TRACE_D0      | PE3             | MCU a 3,3 V   | Dati di tracciamento 0                                       |
|       7 | MCU_PSSI_D3       | PC9             | MCU a 3,3 V   | PSSI D3                                                      |
|       8 | MCU_TRACE_D2      | PE5             | MCU a 3,3 V   | Dati di tracciamento 2                                       |
|       9 | MCU_PSSI_D4       | PE4             | MCU a 3,3 V   | PSSI D4                                                      |
|      10 | MCU_TRACE_D3      | PE6             | MCU a 3,3 V   | Dati di tracciamento 3                                       |
|      11 | MCU_PSSI_D5       | PI4             | MCU a 3,3 V   | PSSI D5                                                      |
|      12 | MCU_PE7           | PE7             | MCU a 3,3 V   | GPIO                                                         |
|      13 | MCU_PSSI_D6       | PI6             | MCU a 3,3 V   | PSSI D6                                                      |
|      14 | MCU_PE8           | PE8             | MCU a 3,3 V   | GPIO                                                         |
|      15 | MCU_PSSI_D7       | PI7             | MCU a 3,3 V   | PSSI D7                                                      |
|      16 | MCU_I2C4_SCL      | PF14            | MCU a 3,3 V   | SCL I²C4                                                     |
|      17 | MCU_PSSI_PDCK     | PD9             | MCU a 3,3 V   | Segnale di clock PSSI                                        |
|      18 | MCU_I2C4_SDA      | PF15            | MCU a 3,3 V   | I²C4 SDA                                                     |
|      19 | MCU_PSSI_RDY      | PI5             | MCU a 3,3 V   | PSSI pronto                                                  |
|      20 | MCU_OPAMP1_VOUT   | PA3             | Analogico     | Uscita VOUT dell'amplificatore operazionale 1                |
|      21 | MCU_PSSI_DE       | PD8             | MCU a 3,3 V   | Abilitazione dati PSSI                                       |
|      22 | MCU_OPAMP1_VINP   | PA0             | Analogico     | VINP dell'amplificatore operazionale 1                       |
|      23 | MCU_MCO           | PA8             | MCU a 3,3 V   | Uscita clock MCU                                             |
|      24 | MCU_OPAMP1_VINM   | PA1             | Analogico     | VINM dell'amplificatore operazionale 1                       |
|      25 | MCU_CRS_SYNC      | PA10            | MCU a 3,3 V   | Sincronizzazione CRS                                         |
|      26 | GND               | -               | Alimentazione | Massa                                                        |
|      27 | GND               | -               | Alimentazione | Massa                                                        |
|      28 | EAR_P_R           | -               | Analogico     | Audio auricolare P_R                                         |
|      29 | MIC2_INP          | -               | Analogico     | Mic2 IN+                                                     |
|      30 | EAR_M_R           | -               | Analogico     | Audio auricolare M_R                                         |
|      31 | MIC2_INM          | -               | Analogico     | Ingresso Mic2−                                               |
|      32 | LINEOUT_P         | -               | Analogico     | Uscita di linea P                                            |
|      33 | MIC2_BIAS         | -               | Analogico     | Polarizzazione Mic2                                          |
|      34 | LINEOUT_M         | -               | Analogico     | Uscita di linea M                                            |
|      35 | GND               | -               | Alimentazione | Massa                                                        |
|      36 | HPH_L             | -               | Analogico     | Cuffia sinistra                                              |
|      37 | SOC_GPIO_0_SE0    | -               | 1,8 V MPU     | GPIO 0 del SoC (SE0)                                         |
|      38 | HPH_R             | -               | Analogico     | Uscita cuffie R                                              |
|      39 | SOC_GPIO_1_SE0    | -               | 1,8 V MPU     | GPIO 1 del SoC (SE0)                                         |
|      40 | HPH_REF           | -               | Analogico     | Riferimento cuffie                                           |
|      41 | SOC_GPIO_2_SE0    | -               | 1,8 V MPU     | SoC GPIO 2 (SE0)                                             |
|      42 | HS_DET            | -               | Analogico     | Rilevamento cuffie                                           |
|      43 | SOC_GPIO_3_SE0    | -               | 1,8 V MPU     | SoC GPIO 3 (SE0)                                             |
|      44 | GND               | -               | Alimentazione | Massa                                                        |
|      45 | SOC_GPIO_86_SE0   | -               | 1,8 V MPU     | SoC GPIO 86 (SE0)                                            |
|      46 | SOC_GPIO_98       | -               | 1,8 V MPU     | SoC GPIO 98                                                  |
|      47 | SOC_GPIO_82_SE0   | -               | 1,8 V MPU     | SoC GPIO 82 (SE0)                                            |
|      48 | SOC_GPIO_99       | -               | 1,8 V MPU     | SoC GPIO 99                                                  |
|      49 | SOC_GPIO_18       | -               | 1,8 V MPU     | GPIO 18 del SoC                                              |
|      50 | SOC_GPIO_100      | -               | 1,8 V MPU     | SoC GPIO 100                                                 |
|      51 | SOC_GPIO_28       | -               | 1,8 V MPU     | GPIO 28 del SoC                                              |
|      52 | SOC_GPIO_101      | -               | 1,8 V MPU     | SoC GPIO 101                                                 |
|      53 | +3V3 (OUT)        | -               | Alimentazione | Uscita di alimentazione a 3,3 V                              |
|      54 | +5V_SYS (OUT)     | -               | Alimentazione | Ingresso o uscita di alimentazione; alimentazione della sorgente e della scheda collegate in OR tramite diodi Schottky |
|      55 | +3V3 (OUT)        | -               | Alimentazione | Uscita di alimentazione a 3,3 V                              |
|      56 | +5V_SYS (OUT)     | -               | Alimentazione | Ingresso o uscita di alimentazione; alimentazione della sorgente e della scheda collegate in OR tramite diodi Schottky |
|      57 | +1V8 (IN)         | -               | Alimentazione | 1,8 V in ingresso                                            |
|      58 | GND               | -               | Alimentazione | Massa                                                        |
|      59 | VCOIN (IN)        | -               | Alimentazione | Tensione di sistema (PMIC RTC)                               |
|      60 | VBAT (OUT)        | -               | Alimentazione | Tensione di sistema (Riservato alla progettazione del sistema e a funzionalità future) |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Nota: le linee GPIO del SoC su JMISC sono dedicate all'interfaccia (non sono GPIO del maker). Le MCU hanno una logica a 3,3 V, le MPU a 1,8 V, mentre i canali audio/microfono sono analogici.
</div>
<div style="page-break-after: always;"></div>

### JMEDIA (B2) (JMEDIA1) - Schema dei pin

| **Pin** | **Denominazione**       | **Ambito**    | **Note**                            |
| ------: | ----------------------- | ------------- | ----------------------------------- |
|       1 | GND                     | Alimentazione | Massa                               |
|       2 | GND                     | Alimentazione | Massa                               |
|       3 | MIPI_DSI0_CLK_M         | MIPI D-PHY    | Clock DSI −                         |
|       4 | MIPI_DSI0_L1_P          | MIPI D-PHY    | DSI corsia 1 +                      |
|       5 | MIPI_DSI0_CLK_P         | MIPI D-PHY    | Clock DSI +                         |
|       6 | MIPI_DSI0_L1_M          | MIPI D-PHY    | DSI corsia 1 −                      |
|       7 | GND                     | Alimentazione | Massa                               |
|       8 | GND                     | Alimentazione | Massa                               |
|       9 | MIPI_DSI0_L2_M          | MIPI D-PHY    | DSI corsia 2 −                      |
|      10 | MIPI_DSI0_L0_P          | MIPI D-PHY    | DSI corsia 0 +                      |
|      11 | MIPI_DSI0_L2_P          | MIPI D-PHY    | DSI corsia 2 +                      |
|      12 | MIPI_DSI0_L0_M          | MIPI D-PHY    | DSI corsia 0 −                      |
|      13 | GND                     | Alimentazione | Massa                               |
|      14 | GND                     | Alimentazione | Massa                               |
|      15 | MIPI_DSI0_L3_M          | MIPI D-PHY    | DSI corsia 3 −                      |
|      16 | SOC_CAM_MCLK0 (GPIO_20) | 1,8 V MPU     | Clock principale della fotocamera 0 |
|      17 | MIPI_DSI0_L3_P          | MIPI D-PHY    | DSI corsia 3 +                      |
|      18 | SOC_CAM_MCLK1 (GPIO_21) | 1,8 V MPU     | Clock principale della fotocamera 1 |
|      19 | GND                     | Alimentazione | Massa                               |
|      20 | GND                     | Alimentazione | Massa                               |
|      21 | CSI0_C0_LN0_M           | MIPI D-PHY    | CSI0 dati0 −                        |
|      22 | CCI_I2C_SDA1 (GPIO_29)  | 1,8 V MPU     | Controllo fotocamera I²C SDA1       |
|      23 | CSI0_B0_LN0_P           | MIPI D-PHY    | CSI0 data0 +                        |
|      24 | CCI_I2C_SCL1 (GPIO_30)  | 1,8 V MPU     | Controllo fotocamera I²C SCL1       |
|      25 | GND                     | Alimentazione | Massa                               |
|      26 | GND                     | Alimentazione | Massa                               |
|      27 | CSI0_B1_LN1_M           | MIPI D-PHY    | CSI0 dati1 −                        |
|      28 | CSI1_B2_LN3_P           | MIPI D-PHY    | CSI1 dati3 +                        |
|      29 | CSI0_A1_LN1_P           | MIPI D-PHY    | CSI0 dati1 +                        |
|      30 | CSI1_C2_LN3_M           | MIPI D-PHY    | Dati CSI13 −                        |
|      31 | GND                     | Alimentazione | Massa                               |
|      32 | GND                     | Alimentazione | Massa                               |
|      33 | CSI0_A0_CLK_M           | MIPI D-PHY    | Clock CSI0 −                        |
|      34 | CSI1_C1_LN2_P           | MIPI D-PHY    | CSI1 dati2 +                        |
|      35 | CSI0_NC_CLK_P           | MIPI D-PHY    | Clock CSI0 +                        |
|      36 | CSI1_A2_LN2_M           | MIPI D-PHY    | CSI1 dati2 −                        |
|      37 | GND                     | Alimentazione | Massa                               |
|      38 | GND                     | Alimentazione | Massa                               |
|      39 | CSI0_A2_LN2_M           | MIPI D-PHY    | Dati CSI02 −                        |
|      40 | CSI1_NC_CLK_P           | MIPI D-PHY    | Segnale di clock CSI1 +             |
|      41 | CSI0_C1_LN2_P           | MIPI D-PHY    | CSI0 dati2 +                        |
|      42 | CSI1_A0_CLK_M           | MIPI D-PHY    | Clock CSI1 −                        |
|      43 | GND                     | Alimentazione | Massa                               |
|      44 | GND                     | Alimentazione | Massa                               |
|      45 | CSI0_C2_LN3_M           | MIPI D-PHY    | CSI0 dati3 −                        |
|      46 | CSI1_A1_LN1_P           | MIPI D-PHY    | CSI1 dati1 +                        |
|      47 | CSI0_B2_LN3_P           | MIPI D-PHY    | CSI0 dati3 +                        |
|      48 | CSI1_B1_LN1_M           | MIPI D-PHY    | CSI1 dati1 −                        |
|      49 | GND                     | Alimentazione | Massa                               |
|      50 | GND                     | Alimentazione | Massa                               |
|      51 | CCI_I2C_SCL0 (GPIO_23)  | 1,8 V MPU     | Controllo fotocamera I²C SCL0       |
|      52 | CSI1_B0_LN0_P           | MIPI D-PHY    | CSI1 data0 +                        |
|      53 | CCI_I2C_SDA0 (GPIO_22)  | 1,8 V MPU     | Controllo fotocamera I²C SDA0       |
|      54 | CSI1_C0_LN0_M           | MIPI D-PHY    | CSI1 data0 −                        |
|      55 | GND                     | Alimentazione | Massa                               |
|      56 | GND                     | Alimentazione | Massa                               |
|      57 | VIN (IN)                | Alimentazione | Ingresso 7-24 V                     |
|      58 | +3V3 (OUT)              | Alimentazione | Uscita 3,3 V                        |
|      59 | VIN (IN)                | Alimentazione | Ingresso 7-24 V                     |
|      60 | +3V3 (OUT)              | Alimentazione | Uscita 3,3 V                        |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Nota: le linee MIPI CSI/DSI sono coppie differenziali D-PHY e non I/O generici. Le linee di controllo (CCI_I2C_*, SOC_CAM_MCLK*) appartengono al dominio MPU a 1,8 V. VIN su JMEDIA è l'ingresso grezzo da 7-24 V (solo alimentazione).
</div>
<div style="page-break-after: always;"></div>

### Qwiic (A4) (QWIIC1) - Schema dei pin

| **Pin** | **Denominazione** | **Rete / Funzione** | **Dominio**   | **Note**                            |
| ------: | ----------------- | ------------------- | ------------- | ----------------------------------- |
|       1 | GND               | Massa               | Alimentazione | -                                   |
|       2 | +3V3 OUT          | PWR_3P3V            | Alimentazione | Alimentazione per dispositivi Qwiic |
|       3 | SDA               | PD13 (I2C4_SDA)     | 3,3 V         | -                                   |
|       4 | SCL               | PD12 (I2C4_SCL)     | 3,3 V         | -                                   |

### JSPI (A5) (JSPI1) - Schema dei pin

| **Pin** | **Denominazione** | **Rete / Funzione** | **Dominio**   | **Note**                                                     |
| ------: | ----------------- | ------------------- | ------------- | ------------------------------------------------------------ |
|       1 | MISO              | PC2 (SPI2_MISO)     | 3,3 V         | -                                                            |
|       2 | +5V               | 5V_SYS              | Alimentazione | Ingresso o uscita di alimentazione; alimentazione della sorgente e della scheda collegate in OR tramite diodi Schottky |
|       3 | SCK               | PD1 (SPI2_SCK)      | 3,3 V         | -                                                            |
|       4 | MOSI              | PC3 (SPI2_MOSI)     | 3,3 V         | -                                                            |
|       5 | RESET             | MCU_NRST            | 3,3 V         | -                                                            |
|       6 | GND               | Massa               | Alimentazione | -                                                            |

### JCTL (A1) (JCTL1) - Schema dei pin

| **Pin** | **Denominazione** | **Rete / Funzione**                               | **Dominio**   | **Note**                   |
| ------: | ----------------- | ------------------------------------------------- | ------------- | -------------------------- |
|       1 | GND               | Massa                                             | Alimentazione | -                          |
|       2 | USB_BOOT          | Circuito di avvio                                 | 1,8 V         | -                          |
|       3 | VOL_DOWN          | GPIO_36                                           | 1,8 V         | GPIO                       |
|       4 | SOC_SE4_TX        | UART TX della console (SE4)                       | 1,8 V         | Console di sistema         |
|       5 | VOL_UP            | GPIO_96                                           | 1,8 V         | GPIO                       |
|       6 | SOC_SE4_RX        | UART console RX (SE4)                             | 1,8 V         | Console di sistema         |
|       7 | GND               | Massa                                             | Alimentazione | -                          |
|       8 | PMIC_RESET        | Reset PM4125                                      | 1,8 V         | -                          |
|       9 | +1V8 OUT          | VREG_L15A_1P8V                                    | Alimentazione | Riferimento 1,8 V          |
|      10 | VBUS_DISABLE      | Disattivazione interruttore di alimentazione VBUS | 1,8 V         | Controlla il percorso VBUS |

<div style="page-break-after: always;"></div>

### JDIGITAL (A2) (JDIGITAL1) - Schema dei pin

| **Pin** | **Denominazione** | **Pin MCU** | **Funzioni**                                | **Ambito**    | **Note**                                     |
| ------: | ----------------- | ----------- | ------------------------------------------- | ------------- | -------------------------------------------- |
|       1 | D0                | PB7         | - USART1_RX <br></br>- TIM4_CH2             | 3,3 V         | UART                                         |
|       2 | D1                | PB6         | - USART1_TX <br></br>- TIM4_CH1             | 3,3 V         | UART                                         |
|       3 | D2                | PB3         | - TIM2_CH2                                  | 3,3 V         | -                                            |
|       4 | ~D3               | PB0         | - OPAMP2_OUTPUT <br></br>- TIM3_CH3         | 3,3 V         | PWM / non compatibile con 5 V                |
|       5 | D4                | PA12        | - FDCAN1_TX <br></br>- TIM1_ETR             | 3,3 V         | -                                            |
|       6 | ~D5               | PA11        | - FDCAN1_RX <br></br>- TIM1_CH4             | 3,3 V         | PWM                                          |
|       7 | ~D6               | PB1         | - TIM3_CH4                                  | 3,3 V         | PWM                                          |
|       8 | D7                | PB2         | - TIM8_CH4N                                 | 3,3 V         | -                                            |
|       9 | D8                | PB4         | - TIM3_CH1                                  | 3,3 V         | -                                            |
|      10 | ~D9               | PB8         | - TIM4_CH3                                  | 3,3 V         | PWM                                          |
|      11 | ~D10              | PB9         | - SPI2_SS (Chip Select) <br></br>- TIM4_CH4 | 3,3 V         | PWM                                          |
|      12 | ~D11              | PB15        | - SPI2_MOSI <br></br>- TIM1_CH3N            | 3,3 V         | PWM                                          |
|      13 | D12               | PB14        | - SPI2_MISO <br></br>- TIM1_CH2N            | 3,3 V         | -                                            |
|      14 | D13               | PB13        | - SPI2_SCK <br></br>- TIM1_CH1N             | 3,3 V         | -                                            |
|      15 | GND               | -           | - Massa                                     | Alimentazione | -                                            |
|      16 | AREF              | -           | - Riferimento analogico                     | -             | Pin di riferimento analogico (non è un GPIO) |
|      17 | D20               | PB11        | - I2C2_SDA <br></br>- TIM2_CH4              | 3,3 V         | -                                            |
|      18 | D21               | PB10        | - I2C2_SCL <br></br>- TIM2_CH3              | 3,3 V         | -                                            |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Tutte le linee JDIGITAL utilizzano una logica a 3,3 V. La maggior parte dei pin utilizza una struttura I/O di tipo FT e tollera 5 V in ingresso. D3 (PB0) utilizza una struttura I/O di tipo TT e tollera solo 3,6 V; non applicare 5 V a questo pin in nessuna modalità.
</div>
### JANALOG (A3) (JANALOG1) - Schema dei pin

| **Pin** | **Denominazione** | **Pin netto / MCU** | **Funzioni**                                                | **Ambito**        | **Note**                                                     |
| ------: | ----------------- | ------------------- | ----------------------------------------------------------- | ----------------- | ------------------------------------------------------------ |
|       1 | BOOT              | MCU_BOOT0           | - Circuito di avvio                                         | 3,3 V             | -                                                            |
|       2 | IOREF             | PWR_3P3V            | - Riferimento di tensione I/O (rispecchia il rail da 3,3 V) | Alimentazione     | Solo uscita; non reimmettere corrente                        |
|       3 | RESET             | MCU_NRST            | - Reset MCU                                                 | 3,3 V             | -                                                            |
|       4 | Uscita +3,3 V     | PWR_3P3V            | Alimentazione a -3,3 V                                      | Alimentazione     | -                                                            |
|       5 | +5V OUT           | 5V_SYS              | Alimentazione a -5 V (diode-OR output)                      | Alimentazione     | Ingresso o uscita di alimentazione; alimentazione della sorgente e della scheda collegate in OR tramite diodi Schottky |
|       6 | GND               | GND                 | - Massa                                                     | Alimentazione     | -                                                            |
|       7 | GND               | GND                 | - Massa                                                     | Alimentazione     | -                                                            |
|       8 | VIN IN            | DC_IN               | - Ingresso 7-24 V                                           | Alimentazione     | Solo alimentazione                                           |
|       9 | A0 / D14          | PA4                 | - Ingresso ADC <br></br>- DAC0 <br></br>- TIM2_CH1          | Analogico / 3,3 V | ADC diretto / non tollerante a 5 V                           |
|      10 | A1 /  D15         | PA5                 | - Ingresso ADC <br></br>- DAC1 <br></br>- TIM3_CH1          | Analogico / 3,3 V | ADC diretto / non compatibile con 5 V                        |
|      11 | A2 /  D16         | PA6                 | - Ingresso ADC <br></br>- OPAMP2_INPUT+ <br></br>- TIM3_CH2 | Analogico / 3,3 V |                                                              |
|      12 | A3 /  D17         | PA7                 | - Ingresso ADC <br></br>- OPAMP2_INPUT−                     | Analogico / 3,3 V | -                                                            |
|      13 | A4 /  D18         | PC1                 | - Ingresso ADC <br></br>- I2C3_SDA <br></br>- LPTIM1_CH1    | Analogico / 3,3 V | -                                                            |
|      14 | A5 /  D19         | PC0                 | - Ingresso ADC <br></br>- I2C3_SCL <br></br>- LPTIM1_IN1    | Analogico / 3,3 V | -                                                            |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  A0 (PA4) e A1 (PA5) sono ingressi diretti dell'ADC dell'STM32U585 con riferimento a <code>VREF+</code>. Non tollerano tensioni a 5 V. L'intervallo di ingresso valido è <code>0-VREF+</code> (≈3,3 V). Il valore massimo assoluto sul pin è <code>VDD + 0,3 V</code>, circa 3,6 V. Oltre questo livello, i diodi di protezione interni dell’MCU iniziano a condurre. Il connettore fornisce anche i pin di alimentazione <code>5V_SYS</code> (protetti dal diodo Schottky-OR) e <code>PWR_3P3V</code> (solo in uscita), diversi dai pin A0/A1 compatibili con l'ADC. Non applicare 5 V a <strong>A0</strong> o <strong>A1</strong>. IOREF è collegato al rail da 3,3 V (<code>PWR_3P3V</code>) ed è fornito come riferimento/uscita per gli shield. Non deve essere utilizzato per reimmettere alimentazione nella scheda.
</div>

## Periferiche ad alta velocità

- **USB-C:** USB 3.1 con funzionalità di commutazione dei ruoli. Modalità alternativa DisplayPort tramite bridge DSI-DP ANX7625. Le coppie differenziali SuperSpeed del connettore sono condivise tra la modalità alternativa DP e i dati USB 3.1. Quando la modalità alternativa DisplayPort è attiva, la velocità dei dati USB viene ridotta.

- **Telecamera:** **MIPI-CSI-2** a quattro canali (I/O a 1,8 V).

- **Display:** **MIPI-DSI** a quattro linee collegato all'**ANX7625** per la modalità alternativa DisplayPort su USB-C. Quando funziona in modalità Single-Board Computer (SBC), la scheda supporta display Full HD (1920 × 1080p) con una risoluzione ottimale di 1280 × 720p.

- **Connessione wireless:** Wi-Fi® dual-band (802.11a/b/g/n/ac) e Bluetooth® 5.1 su un unico modulo.

<div style="page-break-after: always;"></div>

## Funzionamento del dispositivo

### Per iniziare - Arduino App Lab

Arduino App Lab [1] è un editor unificato che permette di creare ed eseguire progetti su entrambi i processori della scheda. Un progetto è un'**App** che può includere: 

- Un programma Python® che gira sul sistema Linux (Qualcomm Dragonwing™ QRB2210)
- Uno sketch Arduino che gira sul microcontrollore (MCU) (STM32U585)
- **Brick** opzionali (applicazioni preconfigurate come modelli di IA, server web o client API) che vengono distribuiti insieme all'app (funzionano anche sul sistema Linux).

Le app usano **Bridge** per scambiare dati tra il sistema Linux e il microcontrollore.

Arduino App Lab può essere installato sul tuo PC oppure eseguito direttamente sull'UNO Q in modalità Single-Board Computer. Per questa configurazione, si consiglia la variante dell'UNO Q con 4 GB di LPDDR4X, per garantire memoria sufficiente per un funzionamento stabile e per applicazioni che richiedono molte risorse. Per utilizzare la scheda: 

- Avvia un esempio pronto all'uso in Arduino App Lab, personalizzalo in base alle tue esigenze oppure crea una nuova applicazione da zero utilizzando l'editor integrato.
- Premi il pulsante **Run** in Arduino App Lab [1].
- L'editor compila il componente Linux, carica lo sketch sulla MCU, installa il Brick selezionato e avvia tutto sulla scheda.
- I log di entrambe le parti sono disponibili nell'editor e puoi eseguire iterazioni senza uscire da Arduino App Lab.

Per la prima configurazione:

1. Installa Arduino App Lab [1], avvialo e collega UNO Q: usa un cavo dati USB-C per la modalità con PC host, oppure alimenta semplicemente la scheda per la modalità SBC.
2. La scheda verificherà automaticamente la presenza di aggiornamenti. Se sono disponibili aggiornamenti, ti verrà chiesto di installarli. Una volta completato l'aggiornamento, sarà necessario riavviare l'Arduino App Lab[1].
3. Durante la prima configurazione, ti verrà chiesto di inserire un nome e una password per il dispositivo. Ti verrà inoltre chiesto di inserire le credenziali Wi-Fi® della tua rete locale.
4. Per provare la scheda, vai su un'app di esempio nella sezione **"Examples"** dell'Arduino App Lab[1] e clicca sul pulsante "Run" in alto a destra. Puoi anche creare una nuova app nella sezione **"App"**.
5. Puoi controllare lo stato dell'app nella scheda "Console" in App Lab.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;"> <p style="text-align: justify;">
<strong>Nota:</strong> in modalità <strong>PC-hosted</strong>, per la configurazione iniziale è necessaria una connessione <em>dati USB</em>. Successivamente potrai utilizzare la destinazione <strong>di rete</strong> tramite LAN (SSH). In modalità <strong>Single-Board Computer (SBC)</strong>, non è necessario alcun collegamento dati USB per la configurazione: basta alimentare la scheda e utilizzare la destinazione <strong>di rete</strong> una volta che si è collegata alla tua rete. Per le periferiche in modalità SBC (tastiera, mouse, videocamera USB, microfono), usa un dongle USB-C con funzionalità di alimentazione esterna. Quando la modalità alternativa DisplayPort è attiva, la velocità dei dati USB viene ridotta.</p>
</div>


Usa una fonte di alimentazione USB-C da 5 V / 3 A e un cavo USB-C, oppure alimenta il dispositivo tramite i pin 5 V o VIN come specificato nella [sezione sull'alimentazione in ingresso](#input-power) (USB-C è solo a 5 V / VIN è da 7-24 V).

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Il primo avvio richiede in genere 20-30 secondi mentre Linux si inizializza. Aspetta che la sequenza del LED di avvio o l'animazione della matrice LED finisca prima di interagire con la scheda.
</div>


### Bricks

<p style="text-align: justify;">I<strong> Brick</strong> sono elementi modulari di Arduino App Lab che ti permettono di ampliare la tua applicazione senza dover scrivere tutta l'infrastruttura di base. Ogni Brick racchiude funzionalità già pronte, come l'integrazione di sensori, modelli di IA, database o interfacce utente, che puoi inserire direttamente in un progetto. I Brick più comuni offrono:</p>

<ul>
  <li>Un modello di IA (ad esempio, classificazione di oggetti o individuazione di parole chiave)</li>
  <li>Un'interfaccia utente web o un servizio API REST</li>
  <li>Un'integrazione con una fonte di dati esterna</li>
</ul>


<p style="text-align: justify;">I Bricks vengono distribuiti insieme all'app e gestiti dal lato Linux. Il flusso di lavoro tipico è il seguente:</p>

<ol>
  <li>Crea <strong>un'app</strong> su Arduino App Lab.</li>
  <li>Scegli qualsiasi <strong>Brick</strong> che l'app deve utilizzare.</li>
  <li>Inserisci il tuo codice Python® (Linux) e/o il tuo sketch Arduino (MCU).</li>
  <li>Il Brick deve essere importato nel tuo file `main.py` e inizializzato seguendo l'API del Brick.</li>
 <li>Clicca su <strong>Run</strong> per distribuire l'applicazione Linux, programmare la MCU e avviare la tua app insieme ai relativi Bricks.</li>
  <li>Lo strumento <strong>Bridge</strong> gestisce lo scambio di dati tra Linux e l'MCU.</li>
</ol>


<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Mentre un'app è in esecuzione, le interfacce USB potrebbero essere occupate dal sistema. Usa Arduino App Lab [1] per l'implementazione e il monitoraggio. Per utilizzare strumenti CLI esterni tramite USB, ferma l'app o scollega la scheda.
</div>


### Hello World

<p style="text-align: justify;">Programmiamo UNO Q con il classico "Hello World" di Arduino: l'esempio <em>del LED lampeggiante</em>. Questo ci aiuta a verificare che la scheda sia collegata correttamente ad Arduino App Lab.</p>

<ol>
  <li>Apri l'App Lab di Arduino. Si trova nella sezione <strong>Esempi</strong>.</li>
  <li>Se non stai utilizzando la modalità single-board computer <strong>collega UNO Q</strong> al tuo PC.</li>
  <li>Apri " <em>Blink LED</em>". Dai un'occhiata alle note dell'esempio per capire come funziona l'app.</li>
  <li>Clicca su<strong>Run</strong> e attendi che il caricamento sia completato.</li>
</ol>


<p style="text-align: justify;">Ora dovresti vedere il canale rosso del LED RGB integrato accendersi per un secondo, poi spegnersi per un secondo, e così via. Il LED è controllato dal microcontrollore STM32U585 tramite lo sketch Arduino.</p>

<p style="text-align: justify;">Puoi partire da un'app vuota oppure utilizzare un esempio già pronto. Se è la prima volta che la usi, ti consigliamo l'esempio "Hello World" per imparare la struttura di base.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Ogni volta che avvii un'app, lo sketch del microcontrollore viene compilato e l'applicazione Python® si avvia sul sistema Linux. A seconda della complessità, l'operazione può richiedere fino a un minuto.
</div>
### Come verificare se l'app è in esecuzione

<p style="text-align: justify;">Apri la <strong>Console</strong> in App Lab. Ci sono tre schede:</p>

<ul>
  <li><strong>Start-up:</strong> log della sequenza di avvio, compresa la compilazione dell'MCU e l'installazione di Linux</li>
  <li><strong>Main (Python®)</strong>: output dell'applicazione Python® (<code>print()</code>)</li>
  <li><strong>Sketch (microcontrollore)</strong>: output seriale dallo sketch Arduino (<code>Serial.println()</code>)</li>
</ul>
<p style="text-align: justify;">Un'app può avviarsi correttamente ma presentare comunque problemi di esecuzione. Controlla il log di Python® per verificare la presenza di errori. Se si verifica un errore di compilazione dello sketch, l'avvio viene interrotto.</p>

<div style="page-break-after: always;"></div>

### Pulsante di accensione

<p style="text-align: justify;">UNO Q include un <strong>pulsante di accensione (JBTN1)</strong> che puoi usare per riavviare la scheda.</p> 

![UNO Q Power Button](assets/ABX00162-ABX00173-power-button.png)

<strong>Pressione prolungata (≥ 5 s):</strong> riavvia il sistema Linux (MPU). Questa operazione non interrompe l'alimentazione della scheda.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
<strong>Nota:</strong> un riavvio tramite pressione prolungata riavvia l'ambiente Linux e potrebbe interrompere le app in esecuzione. Salva il lavoro e assicurati di chiudere in modo sicuro i processi esterni, se necessario. La scheda si avvia automaticamente all'accensione. Per l'avvio normale non è necessario premere il pulsante.
</div>
### Risorse online

<p style="text-align: justify;">Scopri i progetti della community su Project Hub [3], consulta la sezione Library Reference [4] per conoscere le API supportate e trova accessori come i sensori Qwiic, gli UNO shield e carrier nell'Arduino Store [5].</p>

## Informazioni tecniche

<p style="text-align: justify;">La scheda misura 68,58 mm × 53,34 mm, con le parti sul lato inferiore che non superano i 2 mm di spessore, in modo da poterla impilare con un carrier. Il distribuzione e la disposizione dei pin seguono lo standard UNO e sono compatibili con il loro formato.</p>

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
| 26/08/2026 |      15      | Update 5 V power pin (5V_SYS) input option on JANALOG, JMISC, JSPI |
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
