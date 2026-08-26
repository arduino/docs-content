---
identifier: ABX00181
title: Arduino® VENTUNO™ Q
type: maker
---

![](assets/featured.png)

# Italiano

# Descrizione

Arduino® VENTUNO™ Q è un computer edge AI ad alte prestazioni progettato specificamente per l’intelligenza artificiale e la robotica di nuova generazione.VENTUNO Q offre la potenza di elaborazione necessaria per implementare modelli di intelligenza artificiale complessi e il controllo di precisione per manipolare il mondo fisico, il tutto da un unico dispositivo edge compatto, collegando senza soluzione di continuità l’elaborazione di livello industriale con l’attuazione in tempo reale.

Al suo interno si trova una rivoluzionaria architettura Dual-Brain: il robusto microprocessore (MPU) Qualcomm Dragonwing™ IQ8 (QCS8275) (MPU) offre fino a 40 TOPS di calcolo IA ad alta densità per la visione artificiale avanzata e gli LLM locali in esecuzione su un sistema operativo Ubuntu Linux completo (supporta anche Debian), mentre il microcontrollore (MCU) dedicato STMicroelectronics STM32H5F5, che esegue Arduino Core su Zephyr OS, garantisce la precisione a bassa latenza richiesta per il controllo motorio complesso e la robotica.

VENTUNO Q vi consente di rimanere connessi e pronti all’implementazione. È dotato di connettività Wi-Fi® 6 (tri-band) e Bluetooth® 5.3 integrate, oltre a una suite completa di connettori integrati, tra cui USB 3.0 ad alta velocità, HDMI, Ethernet da 2,5 Gb e un connettore M.2 per l’espansione della memoria NVMe Gen 4. La scheda supporta il vasto ecosistema di shield e carrier Arduino UNO, nonché gli HAT Raspberry Pi® tramite un connettore a 40 pin e gli Arduino Modulino® tramite connettore Qwiic.

# Settori di applicazione

Edge AI, LLM/VLM locali, casa intelligente, robotica, controllo del movimento, città intelligente, visione industriale, istruzione e ricerca

<div style="page-break-after: always;"></div>

# INDICE

## Esempi di applicazione

VENTUNO Q combina un processore Linux con funzionalità di intelligenza artificiale a un microcontrollore in tempo reale, offrendo il meglio dell’elaborazione di alto livello e del controllo deterministico. È progettata specificamente per maker e sviluppatori che desiderano un’intelligenza artificiale in grado di plasmare direttamente il mondo fisico.

- **Assistenti IA e casa intelligente:** creando assistenti vocali offline, hub agenti locali, chioschi con interfaccia touchless e traduttori vocali in tempo reale.
- **Robotica e controllo del movimento:** Robot mobili autonomi (AMR) che utilizzano Visual SLAM, manipolatori guidati dalla visione e robot di compagnia e di servizio.
- **Città intelligenti e visione industriale:** sistemi di monitoraggio del traffico edge, ispezione automatizzata della qualità sulle linee di assemblaggio, sicurezza proattiva dei siti e monitoraggio delle scorte basato sulla visione.
- **Istruzione e ricerca:** kit avanzati di apprendimento basati sull’intelligenza artificiale, prototipazione rapida per la ricerca, assistenti di programmazione vocali e piattaforme mobili di ricerca sulla manipolazione.

<div style="page-break-after: always;"></div>

## Caratteristiche

### Varianti di VENTUNO Q

VENTUNO Q è disponibile in un’unica variante:

- **ABX00181**: 16 GB di RAM LPDDR5, 64 GB di memoria eMMC

### Panoramica delle specifiche generali

#### Elaborazione e memoria

![](assets/ABX00181_ic_overview.png)

| **Sottosistema**   | **Dettagli**                                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| MPU principale     | Qualcomm Dragonwing™ IQ8 (QCS8275)                                                                   |
|                    | CPU: Arm® Cortex® octa-core                                                                          |
|                    | GPU Adreno™ 623 (grafica 3D e OpenCL)                                                                |
|                    | VPU Adreno™ 623 (Elaborazione video)                                                                 |
|                    | Processore AI Hexagon™ Tensor (NPU): fino a 40 TOPS densi                                            |
|                    | ISP Qualcomm Spectra 692                                                                             |
|                    | Sistema operativo Ubuntu Linux (supporta anche Debian)                                               |
| MCU in tempo reale | ST STM32H5F5 (MCU), Arm® Cortex®-M33 fino a 250 MHz                                                  |
|                    | Arduino Core su sistema operativo Zephyr                                                             |
|                    | 4 MB di memoria Flash, 1,5 MB di RAM                                                                 |
| Memoria di sistema | eMMC da 64 GB per sistema operativo/dati                                                             |
|                    | Memoria OSPI SAIL (MX25UW25345GXDI00-TR) per l’avvio della MCU/dati condivisi                        |
|                    | Connettore M.2 Key M 2230 per archiviazione NVMe Gen 4 (PCIe x4 direttamente dal SOM, non avviabile) |
|                    | 2x8 GB di RAM LPDDR5 (16 GB totali)                                                                  |

#### Connettività e supporti multimediali

![](assets/ABX00181_connector_overview.png)

| **Sottosistema** | **Dettagli**                                                                                                      |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| Rete e wireless  | Wi-Fi® 6 a 2,4/5/6 GHz (tri-band) con 2 antenne integrate (modulo NFA725B)                                        |
|                  | Bluetooth® 5.3 con antenna integrata                                                                              |
|                  | 1 porta Ethernet RJ45 da 2,5 Gbit (PHY QCA-8081)                                                                  |
| Connettori USB   | 1 porta USB-C con commutazione del ruolo host/dispositivo, commutazione del ruolo di alimentazione e uscita video |
|                  | 2 porte USB 3.0 Tipo A                                                                                            |
|                  | 2 porte USB 3.0 sull’header JOMEGA                                                                                |
| Video            | 1 uscita HDMI tramite bridge DSI-HDMI ADV7535 integrato. HDMI e MIPI DSI condividono                              |
|                  | le stesse linee DSI; quando l’HDMI è attivo, il MIPI DSI sul connettore JMEDIA viene disattivato                  |
|                  | Uscita video (modalità DP Alt) tramite USB-C                                                                      |
| Fotocamera       | 3 connettori MIPI CSI integrati (J3_1, J3_2, J3_3)                                                                |
|                  | Sono disponibili anche 2 linee MIPI CSI sull’header JMEDIA (multiplexate con i connettori integrati)              |
|                  | Supporto per telecamera USB tramite USB Type-A o USB-C                                                            |
| Audio            | Codec audio: MAX98091ETM+T (Maxim)                                                                                |
|                  | Su JMISC: 1 uscita LINE OUT mono, 1 uscita SPEAKER OUT mono, 1 uscita HEADPHONES OUT stereo, 1 ingresso MIC IN    |
|                  | Su JOMEGA: 1 ingresso MIC IN                                                                                      |
| Interfacce CAN   | 1 CAN-FD con PHY (ATA6563-GBQW1) su morsettiera a vite, pilotato da MCU (STM32H5F5)                               |
|                  | Le linee CAN-H e CAN-L sono protette da TVS (PJGBLC24C-AU_R1_000A1, bidirezionali, 24 V, 350 W)                   |
|                  | Terminazione divisa integrata sul bus CAN con morsetti a vite (2× 60,4 Ω + 100 nF)                                |
|                  | 3x CAN-FD (senza PHY) sull’header JOMEGA, con multiplexing dei pin tramite MCU                                    |
|                  | 1x CAN-FD (senza PHY) sugli header dello UNO Shield (D4/D5), con multiplexing dei pin tramite MCU                 |

>📝 **Note:** Il bus CAN sul morsetto a vite include una terminazione divisa integrata (2× 60,4 Ω + 100 nF). Se la scheda non si trova all’estremità del bus, è necessario tenere conto di tale terminazione nella progettazione della topologia di rete.

#### Espansione e connettori

| **Interfaccia (connettore)**      | **Dettagli**                                                                                                                                                         |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connettori UNO Shield             | - Compatibili con gli UNO Shield standard di Arduino (logica a 3,3 V)                                                                                                |
|                                   | - La maggior parte dei pin digitali tollera tensioni a 5 V. I pin A0 e A1 su JANALOG sono ingressi ADC diretti e non tollerano tensioni a 5 V                        |
| Connettore di espansione (JOMEGA) | - Ampie capacità di espansione, tra cui USB 3.0, CAN-FD, JTAG, MIC IN, MPU SPI                                                                                       |
| Connettori carrier                | - JMEDIA: linee per telecamera MIPI CSI0/CSI1 e linee per display MIPI-DSI a 1,8 V                                                                                   |
|                                   | - JMISC: endpoint audio, GPIO dell’MPU a 1,8 V e segnali dell’MCU a 3,3 V                                                                                            |
| Connettore Qwiic                  | - I2C (3,3 V) collegato all’MCU per un accesso immediato plug-and-play ai nodi Modulino®                                                                             |
| Connettore JHAT                   | - Connettore a 40 pin compatibile con Raspberry Pi® (GPIO dell’MPU, con conversione di livello a 3,3 V per la compatibilità HAT tramite TXS0108ERKSR e TXS0104ERUTR) |
| JCTL (debug remoto MPU)           | - Connettore a 10 pin (2×5) per il debug remoto dell’MPU, compatibile con [Arduino Bughopper](https://docs.arduino.cc/hardware/bughopper/)                           |

<div style="page-break-after: always;"></div>

## Specifiche tecniche

### Potenza in ingresso

| **Sorgente**                 | **Intervallo di tensione** | **Corrente massima** | **Connettore**             |
| ---------------------------- | -------------------------: | -------------------: | -------------------------- |
| USB-C PD                     |                     9-20 V |           fino a 3 A | Connettore USB-C           |
| Jack cilindrico (5,5×2,1 mm) |                     7-24 V |           fino a 5 A | Jack cilindrico 5,5×2,1 mm |
| Morsetto a vite              |                     7-24 V |          fino a 10 A | Morsetto a vite            |

![Opzioni di alimentazione in ingresso](assets/ABX00181_power_options.png)

Entrambi i percorsi di ingresso sono protetti da TVS (SMBJ24CA, bidirezionale a 24 V) e passano attraverso interruttori di alimentazione indipendenti (KTS1900GXAA-TA + SQS414CENW-T1_GE3) fino a uno stadio di rilevamento della corrente (INA232AIDDFR). Due convertitori buck multifase (MPQ4371GVE-1001-AECC901-Z) generano la linea principale da 3,3 V, mentre un altro convertitore buck (MPQ4371GVE-1001-AECC901-Z) genera la linea da 5 V. Il controller USB-C® PD (CYPD6129-52LQXI) negozia profili di tensione fino a 20 V da alimentatori USB-C® compatibili.

> 📝 **Nota sulla corrente di ingresso CC e sul bilancio di potenza:** Il connettore jack cilindrico è classificato per un massimo di 5 A. Il bilancio di potenza disponibile dipende dalla tensione di ingresso: a 7 V (5 A) la potenza massima erogabile è di 35 W; a 12 V è di 60 W; a 24 V è di 120 W. Nelle condizioni più sfavorevoli, con MPU, NPU e GPU in funzione contemporaneamente a piena potenza, il SoM da solo può assorbire circa 23-25 W. L’intera scheda, compresi il PHY Ethernet, il codec audio, l’hub USB e altri circuiti integrati integrati, assorbirà una potenza maggiore, lasciando un margine limitato a 7 V prima di raggiungere il limite del connettore.
>
> Quando si alimenta la scheda a 7 V, assicurarsi di tenere conto della caduta di tensione nel cavo, poiché la scheda richiede un minimo di 7 V ai propri connettori e non si accenderà con una tensione inferiore a 7 V.
>
> Le due porte USB di tipo A possono erogare ciascuna fino a 5 V × 1,71 A = 8,55 W, per un assorbimento aggiuntivo massimo combinato di circa 17 W. Con la scheda a piena potenza ed entrambe le porte USB-A al carico massimo, l’assorbimento totale può avvicinarsi ai 42 W, superando il limite di 35 W del jack CC a 7 V e rischiando di danneggiare il connettore.
>
> Il rail da 3,3 V per UNO Shield, HAT e Qwiic (`+3V3_LIMITED`) è limitato a 2,8 A (circa 9,3 W al massimo). Anche il rail da 5 V per shield e HAT (`+5V_LIMITED`) è limitato a 2,8 A (circa 14 W al massimo). Si noti che i rail da 3,3 V e 5 V forniti ai connettori del carrier UNO e a JOMEGA **non** sono limitati in corrente.
>
> **Si raccomanda vivamente l’utilizzo a 12 V o 24 V** per qualsiasi implementazione che preveda contemporaneamente inferenza AI, periferiche USB e shield o HAT collegati.
>
> Per carichi di lavoro intensi che comportano inferenza AI, periferiche USB o applicazioni estese, si raccomanda un alimentatore con una potenza nominale di **60 W o superiore** su tutte le fonti di alimentazione, al fine di garantire che il funzionamento rimanga stabile durante eventuali picchi di consumo. Quando si utilizza il **connettore cilindrico** (5,5×2,1 mm, max 5 A), si raccomanda, a titolo esemplificativo, un'alimentazione di **12 V / 5 A o 24 V / 3 A**.

### Condizioni operative consigliate

| **Parametro**                | **Simbolo**      | **Minimo** | **Tipico** | **Massimo** | **Unità** |
| ---------------------------- | ---------------- | :--------: | :--------: | :---------: | :-------: |
| Ingresso USB-C PD            | V<sub>USBC</sub> |     9      |     -      |    20,0     |     V     |
| Ingresso CC (jack/a vite)    | V<sub>IN</sub>   |    7,0     |     -      |    24,0     |     V     |
| Linea a 5,0 V (uscita)       | V<sub>+5V</sub>  |    4,75    |    5,0     |    5,25     |     V     |
| Linea a 3,3 V (uscita)       | V<sub>3P3</sub>  |    3,14    |    3,3     |    3,47     |     V     |
| Temperatura di funzionamento | T<sub>OP</sub>   |    -10     |     -      |     60      |    °C     |

>📝 **Note:** Il controller USB-C® PD supporta diversi profili di tensione (9 V, 15 V, 20 V) quando è collegato a un alimentatore compatibile con PD.

### Linee di alimentazione integrate sulla scheda

| **Tensione** | **Linea**             | **Origine/Regolatore**                                                                                    |
| :----------: | --------------------- | --------------------------------------------------------------------------------------------------------- |
|    7-24 V    | V<sub>IN</sub>        | Ingresso con jack/morsetti a vite (protetto da TVS, SMBJ24CA)                                             |
|    5,0 V     | +5 V                  | Convertitore buck MPQ4371GVE                                                                              |
|    3,3 V     | +3,3 V                | 2 convertitori buck MPQ4371GVE                                                                            |
|    1,8 V     | SOM_VREG_MDPX3_1P8    | Rotaia da 1,8 V del dominio dell’applicazione principale SOM (accessibile all’utente tramite JMISC, JCTL) |
|    1,8 V     | SOM_VREG_S5S_SPX3_1P8 | Solo per il dominio del sottosistema di sicurezza SOM (RTSS), non per uso generale                        |
|    1,8 V     | +1V8                  | Convertitore buck MPQ2179GQHE (per i circuiti integrati integrati QCA8081, ADV7535, MAX98091)             |
|    1,28 V    | +1,28 V               | LDO MP20312GTF (per il codec audio MAX98091)                                                              |
|    1,1 V     | +1,1 V                | Convertitore buck MPQ2179GQHE (per i circuiti integrati integrati TUSB7340RKMR, QCA8081 e PI7C9X2G304EV)  |

>📝 **Note:** La scheda dispone di tre linee indipendenti da 1,8 V. `SOM_VREG_MDPX3_1P8` è la linea del dominio applicativo principale del SoM QCS8275 e costituisce il riferimento raccomandato per tutte le interfacce da 1,8 V accessibili all’utente, incluse JMISC e JCTL. `SOM_VREG_S5S_SPX3_1P8` è il rail del dominio del sottosistema di sicurezza (RTSS) del SoM e non deve essere utilizzato come alimentazione o riferimento per uso generico. `+1V8` è la tensione di 1,8 V a livello di scheda generata dal convertitore buck MPQ2179GQHE, che alimenta il PHY Ethernet QCA-8081, il bridge per display ADV7535 e il codec audio MAX98091.

>📝 **Note:** Indipendentemente dai binari sopra indicati, il pin 59 del JMISC accetta una batteria di backup per l’RTC fino a 3,3 V per mantenere in funzione gli orologi in tempo reale (RTC) del SOM e dell’MCU quando la scheda è altrimenti spenta. `SOM_VCOIN` (RTC del SOM) e `VBAT` (RTC dell’MCU) sono due ingressi per la batteria di backup dell’RTC che sono fisicamente collegati tra loro su questo singolo pin, anziché su un rail di alimentazione condiviso. Ciascuno di essi è collegato tramite un proprio resistore da 0 Ω a un nodo comune, protetto da un diodo TVS bidirezionale (Vr = 5,5 V) riferito a massa. L’assorbimento di corrente previsto è molto basso e questo pin non fornisce alimentazione per mantenere in funzione il resto della scheda.

### Consumo energetico tipico

Le seguenti misurazioni si basano su una temperatura ambiente di 24,4 °C, utilizzando un analizzatore di potenza, con tre metodi di alimentazione in ingresso: 12 V CC, 24 V CC e USB-C® PD a 20 V. Gli esempi “Blink” sull’MCU, “Hello World” sull’MPU, “Edge AI Assistant” e “Detect Objects” sulla fotocamera dello smartphone sono disponibili come esempi integrati all’interno di Arduino App Lab. L’esempio “Smart Mirror” si basa invece su una nota applicativa.

#### Consumo energetico tipico - 12 V CC

| **Scenario**                                              | **Potenza media** | **Potenza minima** | **Potenza massima** |
| --------------------------------------------------------- | ----------------: | -----------------: | ------------------: |
| Avvio                                                     |            7,07 W |                  – |              17,9 W |
| Blink su MCU                                              |            7,42 W |             5,30 W |              12,6 W |
| "Hello World" su MPU                                      |            7,52 W |             5,32 W |              13,3 W |
| Edge AI Assistant                                         |            13,5 W |             6,13 W |              24,6 W |
| Esempio Smart Mirror¹                                     |            14,7 W |             7,65 W |              33,0 W |
| Rilevamento di oggetti con la fotocamera dello smartphone |            9,63 W |             5,80 W |              21,2 W |

#### Consumo energetico tipico - 24 V CC

| **Scenario**                                              | **Potenza media** | **Potenza minima** | **Potenza massima** |
| --------------------------------------------------------- | ----------------: | -----------------: | ------------------: |
| Avvio                                                     |            9,71 W |                  – |              23,7 W |
| Lampeggiamento su MCU                                     |            10,6 W |             7,04 W |              18,9 W |
| "Hello World" su MPU                                      |            10,8 W |             7,09 W |              18,3 W |
| Assistente AI edge                                        |            15,5 W |             7,44 W |              28,8 W |
| Esempio Smart Mirror¹                                     |            17,3 W |             8,47 W |              36,6 W |
| Rilevamento di oggetti con la fotocamera dello smartphone |            11,5 W |             7,88 W |              24,7 W |

#### Consumo energetico tipico - USB-C® PD (20 V)

| **Scenario**                                              | **Potenza media** | **Potenza minima** | **Potenza massima** |
| --------------------------------------------------------- | ----------------: | -----------------: | ------------------: |
| Avvio                                                     |            6,56 W |                  – |              20,2 W |
| Lampeggiamento sull’MCU                                   |            7,84 W |             6,33 W |              16,1 W |
| “Hello World” sull’MPU                                    |            9,68 W |             6,42 W |              16,1 W |
| Assistente AI edge                                        |            15,3 W |             6,61 W |              25,6 W |
| Esempio Smart Mirror¹                                     |            15,1 W |             8,05 W |              34,2 W |
| Rilevamento di oggetti con la fotocamera dello smartphone |            11,3 W |             7,85 W |              23,1 W |

¹ Configurazione di prova dello Smart Mirror: videocamera USB Logitech BRIO 4K, cuffie USB (microfono e altoparlanti) e display HDMI collegati.

>📝 **Note:** Le misurazioni sono state effettuate utilizzando un analizzatore di potenza Otii Ace Pro a titolo di riferimento. Il picco massimo registrato in tutti gli scenari e per tutte le sorgenti di ingresso è stato di 36,6 W (esempio Smart Mirror a 24 V CC), rientrando nella raccomandazione di un alimentatore da 60 W o superiore sopra indicata.

<div style="page-break-after: always;"></div>

## Panoramica delle funzionalità

### Schema dei pin

![](assets/ABX00181_pinout.png)

### Schema a blocchi

![Panoramica completa dello schema a blocchi](assets/ABX00181_block_diagram.png)

![Schema a blocchi (Pagina 1/2)](assets/ABX00181_block_diagram_pg1.png)

![Schema a blocchi (pagina 2/2)](assets/ABX00181_block_diagram_pg2.png)

### Alimentazione

VENTUNO Q supporta due percorsi di alimentazione indipendenti: una porta USB-C® con negoziazione Power Delivery (PD) fino a 20 V e un ingresso da 7-24 V CC tramite jack cilindrico da 5,5×2,1 mm o morsetto a vite. Entrambi i percorsi sono protetti da TVS bidirezionali da 24 V e instradati attraverso un circuito OR di potenza costituito da interruttori di potenza indipendenti, protetti contro l’inversione di polarità e la corrente inversa (KTS1900 + 2x NMOS), prima di raggiungere i convertitori buck.

Un circuito integrato di rilevamento della corrente (INA232AIDDFR) monitora la corrente di ingresso totale lungo il percorso attivo. Due convertitori buck multifase (MPQ4371GVE-1001-AECC901-Z) generano il rail principale `+3V3`, che alimenta il SOM (QCS8275) e le periferiche a 3,3 V della scheda. Un terzo convertitore buck MPQ4371GVE genera il rail `+5V`.

Un convertitore buck MPQ2179GQHE genera la tensione di `+1V8`, alimentando il PHY Ethernet QCA-8081, il bridge per display ADV7535 e il codec audio MAX98091. Un convertitore buck MPQ2179GQHE genera la tensione di `+1V1`, alimentando il TUSB7340RKMR, il QCA-8081 e lo switch PCIe PI7C9X2G304EV.

Il SOM fornisce il rail del dominio applicativo principale `MDPX3_1P8` (1,8 V) tramite il proprio PMIC interno (`SOM_VREG_MDPX3_1P8`), accessibile all’utente tramite JMISC e JCTL. Il rail separato `SOM_VREG_S5S_SPX3_1P8` è dedicato al sottosistema di sicurezza in tempo reale (RTSS). Non deve essere utilizzato come riferimento generico. Un LDO MP20312GTF genera il rail `+1,28 V` per il codec audio MAX98091.

Gli interruttori di carico dedicati MP5077GG-Z controllano in modo indipendente lo slot M.2 NVMe, il rail `+3V3_LIMITED` (per UNO Shields, HAT e Qwiic) e il rail `+5V_LIMITED` (per shield e HAT). La linea VBUS per ciascuna porta USB di tipo A è abilitata e protetta dal TUSB7340RKMR. Tutti gli altri interruttori di carico delle periferiche sono controllati dalle linee di abilitazione gestite tramite GPIO del SOM, consentendo all’MPU di disattivare l’alimentazione dei sottosistemi inutilizzati.

![Panoramica completa dell’albero di alimentazione di Arduino VENTUNO Q](assets/ABX00181_power_tree.png)

![Albero di alimentazione di Arduino VENTUNO Q (Pagina 1/3)](assets/ABX00181_power_tree_pg1.png)

![Albero di alimentazione di Arduino VENTUNO Q (Pagina 2/3)](assets/ABX00181_power_tree_pg2.png)

![Albero di alimentazione di Arduino VENTUNO Q (Pagina 3/3)](assets/ABX00181_power_tree_pg3.png)

<div style="page-break-after: always;"></div>

## Interfaccia utente e indicatori

| **Indicatore**       | **Tipo**                       | **Controller**                              | **Note**                                                   |
| -------------------- | ------------------------------ | ------------------------------------------- | ---------------------------------------------------------- |
| Matrice LED          | 104 LED blu (LTST-C191TBKT-5A) | MCU tramite GPIO                            | Matrice di visualizzazione programmabile                   |
| 4 LED RGB            | LTST-C28NBEGK-2A               | MCU tramite GPIO                            | Indicatori di stato indirizzabili dall’utente              |
| LED di alimentazione | Verde (LTST-C190KGKT)          | Hardware (linea +3V3)                       | Indica che la linea +3V3 è attiva                          |
| LED di guasto        | Rosso (XHY-STB0603SR)          | Controller USB-C® PD (CYPD6129, GPIO9/P4.1) | Indica una condizione di guasto rilevata dal controller PD |

- **4 LED RGB:** Quattro LED tricolori pilotati dal microcontrollore (MCU) STM32H5F5 tramite 12 pin GPIO individuali (3 per LED). Sono indirizzabili dall’utente e possono essere utilizzati per indicare lo stato dell’applicazione, lo stato di connettività o eventi personalizzati all’interno di uno sketch Arduino.

| **Designatore** | **LED RGB** | **Rosso** | **Verde** | **Blu** |
| --------------- | ----------- | --------- | --------- | ------- |
| DL1_1           | LED RGB 1   | PG3       | PG6       | PK2     |
| DL1_2           | LED RGB 2   | PG4       | PD10      | PK1     |
| DL1_3           | LED RGB 3   | PD11      | PG5       | PK0     |
| DL1_4           | LED RGB 4   | PG2       | PG8       | PC6     |

![](assets/ABX00181_rgb_led.png)

>📝 I LED RGB sono di tipo "active-low" e si accendono quando vengono pilotati al livello logico `0`.

- **Matrice LED:** Una matrice LED monocromatica blu 8×13 (104 pixel) pilotata dal microcontrollore STM32H5F5. Visualizza l’animazione di avvio per circa 20-30 secondi durante l’avvio di Linux. L’accesso alla matrice prima del completamento dell’avvio potrebbe interferire con il funzionamento del microcontrollore.

>📝 **Note:** L’animazione di avvio viene riprodotta solo quando il bootloader del microcontrollore è caricato e è in esecuzione un sketch valido. Se non viene visualizzata, si prega di consultare il [Manuale d’uso di VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) per ulteriori dettagli.

![](assets/ABX00181_matrix.png)

- **LED di alimentazione:** Indicatore verde (LTST-C190KGKT) collegato al rail `+3V3`. Si illumina ogni volta che la scheda è alimentata.

- **LED di errore:** Indicatore rosso pilotato dal controller USB-C® PD (CYPD6129, GPIO9/P4.1). Indica una condizione di errore rilevata dal controller PD.

![](assets/ABX00181_status_led.png)

## MPU e MCU

Un’MPU (unità a microprocessore) è un processore applicativo ad alte prestazioni progettato per eseguire un sistema operativo completo e software complessi. Un’MCU (unità a microcontrollore) è un controller di piccole dimensioni ed efficiente dal punto di vista energetico, progettato per garantire una sincronizzazione rapida e precisa delle operazioni di I/O e di controllo. VENTUNO Q combina entrambe le tecnologie per unire l’elaborazione a livello di sistema operativo con un controllo reattivo e sensibile al fattore tempo su un’unica scheda, e per comunicare tramite Bridge, un livello RPC implementato su entrambi i lati.

### Processore applicativo (MPU)

Il Qualcomm® Dragonwing™ IQ8 (QCS8275) è un processore Arm® Cortex® octa-core che esegue il sistema operativo Ubuntu Linux (è supportato anche Debian). Le sue interfacce I/O funzionano a 1,8 V e gestiscono interfacce multimediali ad alta velocità e inferenza AI.

- Dominio di tensione: 1,8 V per i GPIO dell’MPU (SoC) e le interfacce ad alta velocità.
- Gestisce JMEDIA: linee della fotocamera MIPI CSI e linee del display MIPI-DSI.
- Gestisce i GPIO dell’MPU a 1,8 V e gli endpoint audio sugli header del carrier (JMEDIA, JMISC).
- USB-C: la commutazione dei ruoli è gestita tramite il controller PD CYPD6129, che gestisce autonomamente la negoziazione PD (supporta profili fino a 20 V).
- Uscita DisplayPort tramite multiplexer USB eDP (TMUXHS4446RETT) sul connettore USB-C.
- Gestisce l’NPU Hexagon™ (fino a 40 TOPS densi) e la GPU Adreno™ 623 per carichi di lavoro di intelligenza artificiale e grafica edge.

### Microcontrollore in tempo reale (MCU)

L’STM32H5F5 di STMicroelectronics® è un processore Arm® Cortex®-M33 che esegue Arduino Core su sistema operativo Zephyr a 250 MHz. Fornisce una temporizzazione veloce e deterministica per la robotica, il controllo dei motori e l’I/O generale.

- Dominio di tensione: 3,3 V per GPIO e interfacce analogiche.
- Gestisce ADC, PWM, matrice LED, LED RGB e timer.
- Gestisce i connettori a 3,3 V: JDIGITAL, JANALOG e JSPI.
- Controlla tutte le interfacce CAN-FD: PHY su morsetti a vite e porte senza PHY sui connettori JOMEGA e UNO Shield.

JMISC gestisce entrambi i domini: le linee MPU a 1,8 V coesistono con i segnali MCU a 3,3 V (PSSI, I²C, GPIO) e con l’audio analogico. Verifichi sempre i livelli di tensione quando collega un carrier o circuiti logici esterni a JMISC.

>📝 **Note su VDDIO2:** L’STM32H5F5 dispone di un dominio di alimentazione I/O secondario (VDDIO2) alimentato da `SOM_VREG_MDPX3_1P8` (1,8 V). Ciò consente a specifici pin dell’MCU di comunicare direttamente con l’MPU a 1,8 V senza richiedere convertitori di livello esterni. Le seguenti interfacce operano nel dominio VDDIO2:
>
>- **MCU I2C1** viene utilizzato per la comunicazione diretta tra MCU e MPU
>- **I pin GPIO dell’MCU PG9, PG10, PG11, PG12, PG13 e PG14** comunicano direttamente con l’MPU a 1,8 V
>
> Non applicare una logica a 3,3 V a questi pin. Tutti gli altri segnali GPIO dell’MCU funzionano a 3,3 V sul dominio VDDIO standard.

>⚠️ **Avviso relativo al livello di tensione:** i segnali GPIO dell’MPU funzionano a 1,8 V, mentre quelli dell’MCU funzionano a 3,3 V. Assicurarsi che eventuali connessioni esterne ai connettori di espansione siano compatibili con il livello di tensione del rispettivo dominio del processore per evitare danni all’hardware.

## Comunicazione tra processori

Il Qualcomm® Dragonwing™ IQ8 (QCS8275) (MPU) e l’STM32H5F5 (MCU) comunicano tramite l’Arduino Bridge, un livello software di chiamata di procedura remota (RPC) implementato sia sul lato Linux che su quello dell’MCU. Bridge fornisce un’API orientata ai servizi che consente a entrambi i processori di esporre servizi che l’altro possa richiamare, supportando al contempo notifiche unidirezionali per eventi asincroni. Gestisce l’instradamento dei messaggi tra i processori e supporta diversi trasporti fisici.

Attraverso la propria API, Bridge consente chiamate di funzione type-safe, permettendo agli sketch del microcontrollore di invocare servizi Linux e ricevere risposte strutturate o inviare dati tramite notifiche.

Il livello di trasporto fisico tra i due processori include le seguenti interfacce:

| **Interfaccia** | **Direzione**     | **Scopo**                                                          |
| --------------- | ----------------- | ------------------------------------------------------------------ |
| USB 2.0         | SoC -> MCU (host) | Trasporto dati ad alta larghezza di banda                          |
| SWD             | SoC -> MCU        | Interfaccia di debug (con conversione di livello da 1,8 V a 3,3 V) |

Qualora fosse necessario un indicatore hardware per una scheda carrier o una logica esterna, il firmware può dedicare un GPIO MPU a 1,8 V su JMISC, oppure un GPIO JCTL disponibile, come uscita di pronto o di risveglio. Questo segnale può essere ricevuto su un GPIO dell’MCU tramite circuiti compatibili a livello, quali un convertitore di livello o una configurazione a drain aperto con un resistore pull-up.

>📝 I segnali GPIO dell’MPU operano nel dominio a bassa tensione del processore applicativo (1,8 V). Assicurarsi che qualsiasi collegamento al microcontrollore sia compatibile a livello con la sua tensione di I/O (3,3 V). Ad esempio, utilizzare un convertitore di livello o una configurazione a drain aperto con un resistore pull-up collegato alla tensione di I/O del microcontrollore.

<div style="page-break-after: always;"></div>

## Accelerazione hardware

VENTUNO Q offre accelerazione hardware per l’intelligenza artificiale (AI) edge, la grafica 3D e la codifica/decodifica video grazie al processore AI Hexagon™ Tensor (NPU), alla GPU Adreno™ 623 e alla VPU Adreno™ 623 integrati.

### Accelerazione AI (NPU)

Il processore AI Hexagon™ Tensor integrato offre fino a 40 TOPS (Tera Operations Per Second) di calcolo per reti neurali dense. Consente a VENTUNO Q di eseguire offline modelli linguistici di grandi dimensioni (LLM), modelli linguistici visivi (VLM) e complesse pipeline di visione artificiale.

L’NPU è integrata con il Qualcomm AI Stack ed è supportata in modo nativo in Arduino App Lab. Gli sviluppatori possono implementare modelli ottimizzati tramite **TensorFlow Lite, ONNX Runtime e PyTorch**. VENTUNO Q offre inoltre l’integrazione diretta con **Edge Impulse Studio** per un rapido addestramento e l’implementazione di modelli di IA edge personalizzati senza dover scrivere codice boilerplate.

| **Componente**       | **Specifiche**                                          |
| -------------------- | ------------------------------------------------------- |
| Processore           | Processore AI Hexagon™ Tensor                           |
| Prestazioni di picco | Fino a 40 TOPS densi                                    |
| Architettura         | Hexagon DSP + quadruplo HVX + doppio coprocessore HMX   |
| Framework supportati | TensorFlow Lite, ONNX Runtime, PyTorch                  |
| Integrazione         | Qualcomm AI Stack, Arduino App Lab, Edge Impulse Studio |

### Accelerazione grafica (GPU)

La GPU Adreno™ 623 fornisce grafica 3D con accelerazione hardware ed elaborazione generica (GPGPU) sul SoM QCS8275. Su Qualcomm Linux, l’accelerazione GPU è fornita tramite lo stack di driver Adreno proprietario di Qualcomm, attraverso il driver del kernel KGSL.

Per le specifiche hardware complete della GPU, si rimanda alla [Scheda tecnica del QCS8275 (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html) e alla [Guida alla grafica di Qualcomm Linux](https://docs.qualcomm.com/doc/80-70018-19/topic/).

>📝 **Note:** Le librerie del driver Adreno e i file del firmware sono presenti nella directory `/lib/firmware/` sul dispositivo. Non tutte le funzionalità della GPU elencate nella documentazione del QCS8275 potrebbero essere disponibili nel software distribuito con VENTUNO Q. Si prega di consultare la [Documentazione di VENTUNO Q](https://docs.arduino.cc/hardware/ventuno-q/) per l’elenco aggiornato delle funzionalità supportate.

### Accelerazione video (VPU)

La VPU Adreno™ 623 fornisce un’elaborazione video con accelerazione hardware sul SoM QCS8275. I codec supportati, le risoluzioni e i dettagli di integrazione dipendono dallo stack software distribuito con la scheda. Per le specifiche hardware complete, si rimanda alla [Scheda tecnica del QCS8275 (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html).

>📝 **Note:** Non tutti i codec o i framework elencati nella documentazione del QCS8275 potrebbero essere disponibili nel software distribuito con VENTUNO Q. Si prega di consultare la [Documentazione di VENTUNO Q](https://docs.arduino.cc/hardware/ventuno-q/) per l’elenco aggiornato delle funzionalità supportate.

>📝 **Note:** I plugin GStreamer specifici per Qualcomm (`gstreamer1.0-plugins-qcom`) non sono inclusi per impostazione predefinita nell’immagine Ubuntu distribuita con VENTUNO Q. È possibile installarli manualmente qualora siano necessarie acquisizioni da telecamera con accelerazione hardware o pipeline video. Si prega di consultare il [Manuale d’uso di VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) per i dettagli sulla configurazione.

<div style="page-break-after: always;"></div>

## Periferiche e connettori

VENTUNO Q rende accessibile la propria architettura a doppio cervello tramite una serie completa di connettori e header. Gli header gestiti dall’MCU funzionano con logica a **3,3 V**, mentre quelli gestiti dall’MPU funzionano a **1,8 V**. Verifichi sempre il dominio di tensione di qualsiasi header prima di collegare periferiche esterne, al fine di evitare danni all’hardware.

### JANALOG

Il connettore JANALOG fornisce ingressi analogici, linee di alimentazione e segnali di controllo dell’MCU. È compatibile con il layout standard del connettore analogico di Arduino UNO. Gli ingressi analogici fanno riferimento a `VREF+` sulla linea a 3,3 V e non devono superare `VDD + 0,3 V` (~3,6 V). **Non applicare 5 V ai pin analogici**. `IOREF` è un’uscita di riferimento a 3,3 V, pertanto si prega di non reimmettere corrente attraverso di essa.

| **Pin** | **Designazione** | **Rete**              | **Dominio**   | **Pin MCU** | **Note**                                |
| ------: | ---------------- | --------------------- | ------------- | ----------- | --------------------------------------- |
|       1 | NC               | JANALOG_BOOT_MCU_3V3  | 3,3 V MCU     | BOOT0       | Circuito di avvio MCU                   |
|       2 | IOREF            | +3V3_LIMITED          | Alimentazione | -           | Uscita riferimento tensione I/O         |
|       3 | RESET            | JANALOG_RESET_MCU_3V3 | MCU a 3,3 V   | NRST        | Reset MCU                               |
|       4 | +3V3 OUT         | +3V3_LIMITED          | Alimentazione | -           | Uscita alimentazione 3,3 V              |
|       5 | +5V USB          | +5V_LIMITED           | Alimentazione | -           | Uscita alimentazione 5 V (limitata USB) |
|       6 | GND              | GND                   | Alimentazione | -           | Massa                                   |
|       7 | GND              | GND                   | Alimentazione | -           | Massa                                   |
|       8 | VIN              | 7-24 V                | Alimentazione | -           | Ingresso CC (solo alimentazione)        |
|       9 | A0               | JANALOG_A0_MCU_3V3    | Analogico     | PA4         | Ingresso ADC, non tollerante a 5 V      |
|      10 | A1               | JANALOG_A1_MCU_3V3    | Analogico     | PA5         | Ingresso ADC, non tollerante a 5 V      |
|      11 | A2               | JANALOG_A2_MCU_3V3    | Analogico     | PE12        | Ingresso ADC / SPI4_SCK                 |
|      12 | A3               | JANALOG_A3_MCU_3V3    | Analogico     | PE13        | Ingresso ADC / SPI4_MISO                |
|      13 | A4               | JANALOG_A4_MCU_3V3    | Analogico     | PE14        | Ingresso ADC / SPI4_MOSI                |
|      14 | A5               | JANALOG_A5_MCU_3V3    | Analogico     | PE15        | Ingresso ADC                            |

>📝 **Note:** A0 e A1 sono ingressi ADC diretti dell’MCU e non tollerano tensioni a 5 V. L’intervallo di ingresso valido va da 0 V a `VREF+` (~3,3 V). Il pin VIN (pin 8) è un ingresso dedicato esclusivamente all’alimentazione e non deve essere utilizzato come GPIO. Il pin VIN è protetto da un fusibile PTC da 1,1 A, che ne limita la potenza a circa 26 W a 24 V. Si sconsiglia di alimentare la scheda tramite questo pin a pieno carico. È più indicato per prelevare energia per alimentare uno shield o una periferica piuttosto che come fonte di alimentazione principale della scheda.

>📝 **Note:** A4 (PE14) e A5 (PE15) sono pin esclusivamente analogici e compatibili con SPI e non dispongono di una periferica I2C hardware. Gli shield che richiedono l’I2C su A4 e A5 necessiteranno di un I2C software (bit-banging). L’I2C hardware è disponibile sui pin JDIGITAL 17 (SDA, PH12) e 18 (SCL, PH11).

### JDIGITAL

Il connettore JDIGITAL fornisce segnali di I/O digitale, UART, SPI, I2C e PWM pilotati dal microcontrollore con logica a 3,3 V. È compatibile con il layout standard del connettore digitale di Arduino UNO.

| **Pin** | **Denominazione** | **Net**               | **Dominio**     | **Pin MCU** | **Note**                          |
| ------: | ----------------- | --------------------- | --------------- | ----------- | --------------------------------- |
|       1 | D0 / RX           | JDIGITAL_MCU_UART_3V3 | MCU a 3,3 V     | PB11        | UART RX                           |
|       2 | D1 / TX           | JDIGITAL_MCU_UART_3V3 | MCU a 3,3 V MCU | PB10        | UART TX                           |
|       3 | D2                | JDIGITAL_D2_MCU_3V3   | 3,3 V MCU       | PB0         | GPIO                              |
|       4 | D3                | JDIGITAL_D3_MCU_3V3   | 3,3 V MCU       | PB1         | GPIO / PWM                        |
|       5 | D4                | JDIGITAL_D4_MCU_3V3   | MCU a 3,3 V     | PB6         | GPIO / FDCAN2_TX                  |
|       6 | D5                | JDIGITAL_D5_MCU_3V3   | MCU a 3,3 V     | PB5         | GPIO / PWM / FDCAN2_RX            |
|       7 | D6                | JDIGITAL_D6_MCU_3V3   | MCU a 3,3 V     | PB2         | GPIO / PWM                        |
|       8 | D7                | JDIGITAL_D7_MCU_3V3   | MCU a 3,3 V MCU | PB3         | GPIO                              |
|       9 | D8                | JDIGITAL_D8_MCU_3V3   | 3,3 V MCU       | PB4         | GPIO                              |
|      10 | D9                | JDIGITAL_D9_MCU_3V3   | 3,3 V MCU       | PB7         | GPIO / PWM                        |
|      11 | D10 / CS          | JDIGITAL_MCU_SPI_3V3  | MCU a 3,3 V     | PB12        | Selezione chip SPI                |
|      12 | D11 / MOSI        | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU       | PB15        | SPI MOSI / PWM                    |
|      13 | D12 / MISO        | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU       | PB14        | SPI MISO                          |
|      14 | D13 / SCK         | JDIGITAL_MCU_SPI_3V3  | MCU a 3,3 V     | PB13        | Clock SPI                         |
|      15 | GND               | GND                   | Alimentazione   | -           | Massa                             |
|      16 | AREF              | JDIGITAL_AREF_MCU_3V3 | Analogico       | -           | Riferimento di tensione analogico |
|      17 | SDA               | JDIGITAL_MCU_I2C_3V3  | MCU a 3,3 V     | PH12        | Dati I2C (I2C4 / I3C1)            |
|      18 | SCL               | JDIGITAL_MCU_I2C_3V3  | MCU a 3,3 V     | PH11        | Clock I2C (I2C4 / I3C1)           |

>📝 **Note:** Tutte le linee JDIGITAL seguono la logica a 3,3 V dell’MCU. La maggior parte dei pin tollera tensioni fino a 5 V in modalità digitale. AREF è un ingresso di riferimento di tensione analogico per l’ADC dell’MCU. Viene instradato tramite un interruttore analogico integrato (U28, SGM3157YC6/TR) ed è attivo solo quando il pin PI8 dell’MCU è impostato su HIGH.

### JSPI

Il connettore JSPI mette a disposizione un bus SPI dedicato per il collegamento di periferiche quali lettori di schede SD, driver di display o sensori. Fornisce inoltre il segnale RESET e l’alimentazione. Tutti i segnali rientrano nel dominio a 3,3 V dell’MCU.

| **Pin** | **Designazione** | **Rete**         | **Dominio**     | **Pin MCU** | **Note**                      |
| ------: | ---------------- | ---------------- | --------------- | ----------- | ----------------------------- |
|       1 | MISO             | JSPI_MCU_SPI_3V3 | 3,3 V MCU       | PF14        | SPI MISO                      |
|       2 | +5 V             | +5V_LIMITED      | Alimentazione   | -           | Uscita di alimentazione a 5 V |
|       3 | SCK              | JSPI_MCU_SPI_3V3 | MCU a 3,3 V     | PC10        | Clock SPI                     |
|       4 | MOSI             | JSPI_MCU_SPI_3V3 | MCU a 3,3 V MCU | PC12        | SPI MOSI                      |
|       5 | RESET            | MCU_NRST         | 3,3 V MCU       | NRST        | Reset MCU                     |
|       6 | GND              | GND              | Alimentazione   | -           | Massa                         |

>⚠️ **Nota sulla protezione dell’alimentazione:** I binari da 3,3 V e 5 V sui connettori JSPI e UNO Shield sono protetti da interruttori di carico dedicati (MP5077GG-Z), ciascuno con una corrente massima di **2,8 A**. Questi interruttori impediscono alle periferiche collegate di assorbire una corrente eccessiva e proteggono la scheda dal rischio di retroalimentazione. Non tentare di bypassare o disattivare questi interruttori.

### Qwiic

Il connettore Qwiic fornisce un bus I2C a 3,3 V per il collegamento plug-and-play ai nodi Modulino® e ai sensori di terze parti compatibili, senza necessità di saldature. Il connettore è polarizzato e ammette un unico orientamento per il collegamento.

| **Pin** | **Designazione** | **Rete**     | **Dominio**   | **Pin MCU** | **Note**                                |
| ------: | ---------------- | ------------ | ------------- | ----------- | --------------------------------------- |
|       1 | GND              | GND          | Alimentazione | -           | Massa                                   |
|       2 | VCC              | +3V3_LIMITED | Alimentazione | -           | Alimentazione a 3,3 V per i dispositivi |
|       3 | SDA              | I2C3_SDA     | MCU a 3,3 V   | PC9         | Dati I2C                                |
|       4 | SCL              | I2C3_SCL     | MCU a 3,3 V   | PA8         | Clock I2C                               |

>📝 **Note:** I connettori Qwiic sono espandibili in configurazione a catena ed è possibile collegare più moduli in serie sullo stesso bus I2C. Il bus I2C è collegato all’MCU.

### JCTL (Debug remoto MPU)

L’header JCTL è un connettore a 10 pin (2×5) che fornisce l’accesso alla console UART dell’MPU, il controllo di override dell’avvio e i segnali di gestione dell’alimentazione. Arduino Bughopper è lo strumento consigliato per l’interfacciamento con questo header. La maggior parte dei pin di segnale attivi è protetta da ESD tramite diodi TVS (il pin 10 non lo è). I pin di segnale operano in domini di tensione misti: 1,8 V, 3,3 V e 7-24 V; si prega di fare riferimento alla tabella dei pin riportata di seguito. Il pin 9 espone direttamente la linea `SOM_VREG_MDPX3_1P8`; non applicare alcuna tensione esterna a questo pin.

| **Pin** | **Designazione**       | **Rete**           | **Dominio**                       | **Pin MPU** | **Note**                                                                                                                                                                |
| ------: | ---------------------- | ------------------ | --------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       1 | GND                    | GND                | Alimentazione                     | -           | Massa                                                                                                                                                                   |
|       2 | FORCED_USB_BOOT_N      | FORCE_BOOT_3V3     | 3,3 V                             | -           | Dominio a 3,3 V. Controlla 2 NMOS che pilotano MD_FORCE_USB_BOOT_1V8 e RTSS_FORCE_USB_BOOT_1V8. Portare a livello BASSO per entrare in modalità EDL al prossimo riavvio |
|       3 | PMIC_POWER_EN          | PMIC_POWER_EN      | 1,8 V MPU                         | -           | Abilitazione alimentazione PMIC                                                                                                                                         |
|       4 | TX                     | UART_DBG_1V8       | 1,8 V MPU                         | GPIO_43     | UART TX di debug MPU                                                                                                                                                    |
|       5 | GPIO                   | MD_GPIO_103        | 1,8 V MPU                         | GPIO_103    | GPIO per uso generico                                                                                                                                                   |
|       6 | RX                     | UART_DBG_1V8       | 1,8 V MPU                         | GPIO_44     | UART di debug MPU (RX)                                                                                                                                                  |
|       7 | GND                    | GND                | Alimentazione                     | -           | Massa                                                                                                                                                                   |
|       8 | RESIN_N                | RESIN_N            | 3,3 V                             | -           | Open-drain, protetto da TVS. Portare a livello LOW per il riavvio a caldo (i binari di tensione rimangono attivi)                                                       |
|       9 | +1V8 OUT               | SOM_VREG_MDPX3_1P8 | Alimentazione                     | -           | Dominio MDPX3 a 1,8 V diretto, non applicare tensione esterna                                                                                                           |
|      10 | POWER_SWITCH_DISABLE_N | PWR_DISABLE        | 7-24 V (fino a un massimo di 5 V) | -           | Non protetto da TVS. Portare a livello LOW per il riavvio a freddo (controlla l’alimentazione principale)                                                               |

> ⚠️ **Da leggere prima di collegare qualsiasi cosa al JCTL**
>
> Il pin 9 espone direttamente `SOM_VREG_MDPX3_1P8` (~1,8 V); non applicare alcuna tensione esterna a questo pin. I pin operano in domini di tensione misti: i pin 2 e 8 appartengono al dominio a 3,3 V, i pin 4 e 6 (UART) a quello a 1,8 V, il pin 10 è l’ingresso di abilitazione per l’interruttore di alimentazione principale VIN; grazie a un divisore di tensione interno, consente il collegamento diretto a VIN; portarlo al di sotto di 0,85 V per disabilitare l’alimentazione principale, mantenerlo al di sopra di 1 V per il funzionamento normale e non superare i 5 V esternamente. Il pin 10 non è protetto da TVS. L’applicazione di tensioni errate a qualsiasi pin JCTL attivo può danneggiare in modo permanente il SoM QCS8275.
>
> **Si raccomanda vivamente l’uso dell’Arduino Bughopper** per la maggior parte dei casi di debug, poiché include traduttori di livello e stadi di uscita compatibili con open-drain progettati specificamente per un’interfaccia JCTL sicura.
>
> Se si sceglie invece di utilizzare un adattatore USB-UART diverso o hardware di debug personalizzato, assicurarsi che tutte le linee di segnale siano pilotate alla tensione corretta per il rispettivo dominio, che il pin 10 non venga mai pilotato oltre i 5 V e che non esista alcun percorso di retroalimentazione verso il rail `SOM_VREG_MDPX3_1P8`.

> 📝 **Riepilogo del controllo dell’avvio:**
>
> - **Riavvio a caldo** (solo MPU, i rail di tensione rimangono attivi): Portare il pin 8 (RESIN_N) a LIVELLO BASSO tramite open-drain.
> - **Riavvio a freddo** (ciclo di alimentazione completo, fonte di alimentazione principale disattivata): Portare il pin 10 (POWER_SWITCH_DISABLE_N) a livello LOW tramite open-drain.
> - **Modalità EDL / Download di emergenza**: Portare il pin 2 (FORCED_USB_BOOT_N) a livello LOW tramite open-drain, quindi attivare un riavvio tramite il pin 8 o il pin 10.
>
> Questo connettore è destinato all’uso in fase di sviluppo e debug.

### JHAT

L’header JHAT è un header standard a 40 pin compatibile con Raspberry Pi®, pilotato dall’MPU (QCS8275) con logica a **3,3 V**. Esso espone i segnali I2C, SPI, UART, I2S e GPIO generici provenienti dall’MPU. I pin di alimentazione forniscono 3,3 V e 5 V agli HAT collegati.

Tutti i segnali GPIO vengono convertiti dal dominio a 1,8 V dell’MPU al dominio HAT a 3,3 V tramite quattro convertitori di livello bidirezionali integrati: tre dispositivi TXS0108ERKSR a 8 canali (U33_2, U33_3, U33_4) e un dispositivo TXS0104ERUTR a 4 canali (U21), garantendo la compatibilità diretta con i progetti HAT standard per Raspberry Pi® senza necessità di ulteriori conversioni di livello.

| **Pin** | **Denominazione** | **Pin MPU** | **Funzione alternativa** | **Dominio**   | **Note**                   |
| ------: | ----------------- | ----------- | ------------------------ | ------------- | -------------------------- |
|       1 | Uscita +3V3       | -           | -                        | Alimentazione | Uscita alimentazione 3,3 V |
|       2 | Uscita +5V        | -           | -                        | Alimentazione | Uscita alimentazione 5 V   |
|       3 | GPIO 2 (SDA)      | MD_GPIO_17  | QUP0_SE0_I2C_SDA         | MPU a 3,3 V   | Dati I2C1                  |
|       4 | +5V OUT           | -           | -                        | Alimentazione | Uscita alimentazione 5 V   |
|       5 | GPIO 3 (SCL)      | MD_GPIO_18  | QUP0_SE0_I2C_SCL         | 3,3 V MPU     | Clock I2C1                 |
|       6 | GND               | -           | -                        | Alimentazione | Massa                      |
|       7 | GPIO 4            | MD_GPIO_83  | GPCLK0                   | 3,3 V MPU     | GPIO generico              |
|       8 | GPIO 14 (TX)      | MD_GPIO_86  | QUP1_SE2_UART_TX         | 3,3 V MPU     | UART0 TX                   |
|       9 | GND               | -           | -                        | Alimentazione | Massa                      |
|      10 | GPIO 15 (RX)      | MD_GPIO_87  | QUP1_SE2_UART_RX         | 3,3 V MPU     | UART0 RX                   |
|      11 | GPIO 17           | MD_GPIO_85  | QUP1_SE2_UART_RFR        | 3,3 V MPU     | UART RFR/RTS               |
|      12 | GPIO 18 (CLK)     | MD_GPIO_116 | LPI_I2S1_SCK             | 3,3 V MPU     | Clock PCM                  |
|      13 | GPIO 27           | MD_GPIO_109 | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      14 | GND               | -           | -                        | Alimentazione | Massa                      |
|      15 | GPIO 22           | MD_GPIO_90  | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      16 | GPIO 23           | MD_GPIO_105 | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      17 | Uscita +3V3       | -           | -                        | Alimentazione | Uscita alimentazione 3,3 V |
|      18 | GPIO 24           | MD_GPIO_106 | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      19 | GPIO 10 (MOSI)    | MD_GPIO_26  | QUP0_SE3_SPI_MOSI        | 3,3 V MPU     | SPI0 MOSI                  |
|      20 | GND               | -           | -                        | Alimentazione | Massa                      |
|      21 | GPIO 9 (MISO)     | MD_GPIO_25  | QUP0_SE3_SPI_MISO        | 3,3 V MPU     | SPI0 MISO                  |
|      22 | GPIO 25           | MD_GPIO_107 | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      23 | GPIO 11 (SCLK)    | MD_GPIO_27  | QUP0_SE3_SPI_SCK         | 3,3 V MPU     | Clock SPI0                 |
|      24 | GPIO 8 (CE0)      | MD_GPIO_28  | QUP0_SE3_SPI_CS          | 3,3 V MPU     | CE0 SPI0                   |
|      25 | GND               | -           | -                        | Alimentazione | Massa                      |
|      26 | GPIO 7 (CE1)      | MD_GPIO_88  | GPIO                     | 3,3 V MPU     | SPI0 CE1                   |
|      27 | GPIO 0 (SDA)      | MD_GPIO_19  | QUP0_SE1_I2C_SDA         | 3,3 V MPU     | I2C0 / EEPROM SDA          |
|      28 | GPIO 1 (SCL)      | MD_GPIO_20  | QUP0_SE1_I2C_SCL         | 3,3 V MPU     | I2C0 / EEPROM SCL          |
|      29 | GPIO 5            | MD_GPIO_89  | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      30 | GND               | -           | -                        | Alimentazione | Massa                      |
|      31 | GPIO 6            | MD_GPIO_80  | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      32 | GPIO 12 (PWM0)    | MD_GPIO_77  | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      33 | GPIO 13 (PWM1)    | MD_GPIO_81  | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      34 | GND               | -           | -                        | Alimentazione | Massa                      |
|      35 | GPIO 19 (FS)      | MD_GPIO_117 | LPI_I2S1_WS              | 3,3 V MPU     | Sincronizzazione frame PCM |
|      36 | GPIO 16           | MD_GPIO_84  | QUP1_SE2_UART_CTS        | 3,3 V MPU     | CTS UART                   |
|      37 | GPIO 26           | MD_GPIO_108 | GPIO                     | 3,3 V MPU     | GPIO generico              |
|      38 | GPIO 20 (DIN)     | MD_GPIO_118 | LPI_I2S1_DATA0           | 3,3 V MPU     | Ingresso dati PCM          |
|      39 | GND               | -           | -                        | Alimentazione | Massa                      |
|      40 | GPIO 21 (DOUT)    | MD_GPIO_119 | LPI_I2S1_DATA1           | 3,3 V MPU     | Uscita dati PCM            |

>📝 **Note:** Sebbene i segnali GPIO dell’MPU siano internamente a 1,8 V, i convertitori di livello integrati TXS0108ERKSR e TXS0104ERUTR li presentano a 3,3 V sul connettore JHAT, rendendoli direttamente compatibili con i livelli logici standard degli HAT per Raspberry Pi®. Non applichi tensioni superiori a 3,3 V a nessun pin di segnale JHAT. I pin di alimentazione (3,3 V e 5 V) sono uscite della scheda; si prega di non reimmettere corrente attraverso di essi da un HAT collegato.

>📝 **Nota:** i pin UART JHAT 8, 10, 11 e 36 (TX, RX, RFR e CTS) condividono lo stesso UART QUP1_SE2 del modulo Wi-Fi®/Bluetooth® LE integrato. I segnali TX, RX e RFR vengono convertiti in livello tramite U33_4 (TXS0108ERKSR), mentre il segnale CTS viene convertito separatamente tramite U21 (TXS0104ERUTR) insieme ai pin GPIO 26, GPIO 20 (I2S_DATA0) e GPIO 21 (I2S_DATA1) sui pin 37, 38 e 40. Questi pin non sono disponibili per l’uso con HAT esterni ogni volta che il Bluetooth è attivo.

### JMISC

Il connettore JMISC è un connettore ad alta densità a 60 pin che riunisce il bus parallelo PSSI della MCU per la telecamera, i GPIO della MCU, l’I2C della MCU, i segnali audio (microfono, cuffie, uscita altoparlante mono, uscita di linea), l’SPI del SoC della MPU, i GPIO della MPU e i segnali I2S della MPU. Si tratta di un connettore a tensione mista: **i segnali dell’MCU sono a 3,3 V**, **i segnali dell’MPU sono a 1,8 V** e i pin audio/microfono sono analogici.

| **Pin** | **Designazione**   | **Dominio**   | **Pin MCU** | **Pin MPU** | **Note**                                      |
| ------: | ------------------ | ------------- | ----------- | ----------- | --------------------------------------------- |
|       1 | MCU_PSSI_D0        | 3,3 V MCU     | PA9         | -           | Bit di dati PSSI 0                            |
|       2 | MCU_TRACE_CLK      | 3,3 V MCU     | PE2         | -           | Clock di tracciamento MCU                     |
|       3 | MCU_PSSI_D1        | 3,3 V MCU     | PC7         | -           | Bit di dati PSSI 1                            |
|       4 | MCU_TRACE_D0       | 3,3 V MCU     | PE3         | -           | Dati di tracciamento MCU 0                    |
|       5 | MCU_PSSI_D2        | 3,3 V MCU     | PC8         | -           | Bit di dati PSSI 2                            |
|       6 | MCU_TRACE_D1       | MCU a 3,3 V   | PE4         | -           | Dati di tracciamento MCU 1                    |
|       7 | MCU_PSSI_D3        | MCU a 3,3 V   | PE1         | -           | Bit di dati PSSI 3                            |
|       8 | MCU_TRACE_D2       | MCU a 3,3 V   | PE5         | -           | Dati di tracciamento MCU 2                    |
|       9 | MCU_PSSI_D4        | MCU a 3,3 V   | PC11        | -           | Bit di dati PSSI 4                            |
|      10 | MCU_TRACE_D3       | MCU a 3,3 V   | PE6         | -           | Dati di tracciamento MCU 3                    |
|      11 | MCU_PSSI_D5        | MCU a 3,3 V   | PD3         | -           | Bit di dati PSSI 5                            |
|      12 | MCU_USART2_RX      | MCU a 3,3 V   | PE7         | -           | Ricezione USART2 dell’MCU                     |
|      13 | MCU_PSSI_D6        | MCU a 3,3 V   | PF4         | -           | Bit di dati PSSI 6                            |
|      14 | MCU_USART2_TX      | 3,3 V MCU     | PE8         | -           | MCU USART2 TX                                 |
|      15 | MCU_PSSI_D7        | 3,3 V MCU     | PI7         | -           | Bit di dati PSSI 7                            |
|      16 | MCU_I2C_SCL        | 3,3 V MCU     | PF1         | -           | Clock I2C2 dell’MCU                           |
|      17 | MCU_PSSI_PDCK      | 3,3 V MCU     | PA6         | -           | Clock pixel PSSI                              |
|      18 | MCU_I2C_SDA        | 3,3 V MCU     | PF0         | -           | Dati I2C2 dell’MCU                            |
|      19 | MCU_PSSI_RDY       | 3,3 V MCU     | PI5         | -           | PSSI pronto                                   |
|      20 | MCU_GPIO_PA0       | 3,3 V MCU     | PA0         | -           | GPIO MCU                                      |
|      21 | MCU_PSSI_DE        | 3,3 V MCU     | PH8         | -           | Abilitazione dati PSSI                        |
|      22 | MCU_GPIO_PA1       | 3,3 V MCU     | PA1         | -           | GPIO dell’MCU                                 |
|      23 | MCU_UART4_RX       | 3,3 V MCU     | PA11        | -           | UART4 RX dell’MCU                             |
|      24 | MCU_GPIO_PA2       | 3,3 V MCU     | PA2         | -           | GPIO dell’MCU                                 |
|      25 | MCU_UART4_TX       | 3,3 V MCU     | PA12        | -           | UART4 TX dell’MCU                             |
|      26 | GND                | Alimentazione | -           | -           | Massa                                         |
|      27 | GND                | Alimentazione | -           | -           | Massa                                         |
|      28 | EAR_P              | Analogico     | -           | -           | Uscita altoparlante P (mono)                  |
|      29 | MIC_INP            | Analogico     | -           | -           | Ingresso microfono+                           |
|      30 | EAR_M              | Analogico     | -           | -           | Uscita altoparlante M (mono)                  |
|      31 | MIC_INN            | Analogico     | -           | -           | Ingresso microfono −                          |
|      32 | LINEOUT_P          | Analogico     | -           | -           | Uscita di linea P                             |
|      33 | MIC_BIAS           | Analogico     | -           | -           | Polarizzazione microfono                      |
|      34 | LINEOUT_M          | Analogico     | -           | -           | Uscita linea M                                |
|      35 | GND                | Alimentazione | -           | -           | Massa                                         |
|      36 | HPH_L              | Analogico     | -           | -           | Cuffia sinistra                               |
|      37 | SOC_SPI_MISO       | MPU a 1,8 V   | -           | GPIO_10     | MPU SPI MISO (SE0)                            |
|      38 | HPH_R              | Analogico     | -           | -           | Cuffia destra                                 |
|      39 | SOC_SPI_MOSI       | 1,8 V MPU     | -           | GPIO_11     | MPU SPI MOSI (SE0)                            |
|      40 | HPH_REF            | Analogico     | -           | -           | Riferimento cuffie                            |
|      41 | SOC_SPI_SCK        | 1,8 V MPU     | -           | GPIO_12     | Clock SPI MPU (SE0)                           |
|      42 | HS_DET             | Analogico     | -           | -           | Rilevamento cuffie                            |
|      43 | SOC_SPI_CS0        | 1,8 V MPU     | -           | GPIO_13     | Selezione chip SPI MPU 0 (SE0)                |
|      44 | GND                | Alimentazione | -           | -           | Massa                                         |
|      45 | SOC_SPI_CS2        | 1,8 V MPU     | -           | GPIO_15     | Selezione chip SPI MPU 2 (SE0)                |
|      46 | SOC_MI2S_SCK       | 1,8 V MPU     | -           | GPIO_120    | Clock I2S                                     |
|      47 | SOC_SPI_CS1        | 1,8 V MPU     | -           | GPIO_14     | Selezione chip SPI MPU 1 (SE0)                |
|      48 | SOC_MI2S_WS        | 1,8 V MPU     | -           | GPIO_121    | Selezione parola I2S                          |
|      49 | SOC_GPIO_73        | 1,8 V MPU     | -           | GPIO_73     | GPIO SoC MPU                                  |
|      50 | SOC_MI2S_DATA0     | 1,8 V MPU     | -           | GPIO_122    | Dati I2S 0                                    |
|      51 | SOC_GPIO_74        | 1,8 V MPU     | -           | GPIO_74     | GPIO SoC MPU                                  |
|      52 | SOC_MI2S_DATA1     | 1,8 V MPU     | -           | GPIO_123    | Dati I2S 1                                    |
|      53 | +3V3 OUT           | Alimentazione | -           | -           | Uscita alimentazione 3,3 V                    |
|      54 | +5V OUT            | Alimentazione | -           | -           | Uscita alimentazione 5 V                      |
|      55 | +3V3 OUT           | Alimentazione | -           | -           | Uscita alimentazione 3,3 V                    |
|      56 | +5V OUT            | Alimentazione | -           | -           | Uscita alimentazione 5 V                      |
|      57 | SOM_VREG_MDPX3_1P8 | Alimentazione | -           | -           | Rotaia SOM da 1,8 V                           |
|      58 | GND                | Alimentazione | -           | -           | Massa                                         |
|      59 | SOM_VCOIN / VBAT   | Backup RTC    | -           | -           | Ingresso batteria di backup RTC per SOM e MCU |
|      60 | NON COLLEGATO      | -             | -           | -           | -                                             |

>📝 **Note:** i pin dell’MCU sono a 3,3 V, quelli del SoC MPU sono a 1,8 V, mentre i pin audio/microfono sono analogici. Si raccomanda di non mescolare domini di tensione diversi. Le linee GPIO del SoC su JMISC sono dedicate all’interfaccia e non costituiscono GPIO generici per maker.

>📝 **Note:** il pin 59 di JMISC accetta una batteria di backup RTC fino a 3,3 V per mantenere in funzione gli orologi in tempo reale (RTC) del SOM e dell’MCU quando la scheda è altrimenti spenta. `SOM_VCOIN` (RTC del SOM) e `VBAT` (RTC dell’MCU) sono due ingressi per la batteria di backup dell’RTC che sono fisicamente collegati tra loro su questo singolo pin, anziché su un rail di alimentazione condiviso. Ciascuno si collega tramite un proprio resistore da 0 Ω a un nodo comune, protetto da un diodo TVS bidirezionale (Vr = 5,5 V) con riferimento a massa. L’assorbimento di corrente previsto è molto basso e questo pin non fornisce alimentazione per mantenere in funzione il resto della scheda.

### JMEDIA

Il connettore JMEDIA è un connettore ad alta densità a 60 pin che trasporta i segnali MIPI DSI (display), MIPI CSI0 e CSI1, i segnali di clock della fotocamera e i bus I2C di controllo della fotocamera. Tutti i segnali si trovano nel **dominio MPU a 1,8 V**. I pin di alimentazione forniscono un'uscita a 3,3 V e accettano un ingresso da 7 a 24 V CC.

| **Pin** | **Denominazione** | **Dominio**   | **Pin MPU** | **Note**                                        |
| ------: | ----------------- | ------------- | ----------- | ----------------------------------------------- |
|       1 | GND               | Alimentazione | -           | Massa                                           |
|       2 | GND               | Alimentazione | -           | Massa                                           |
|       3 | MIPI_DSI0_CLK_M   | MIPI D-PHY    | -           | Clock DSI −                                     |
|       4 | MIPI_DSI0_L1_P    | MIPI D-PHY    | -           | Lana DSI 1 +                                    |
|       5 | MIPI_DSI0_CLK_P   | MIPI D-PHY    | -           | Clock DSI +                                     |
|       6 | MIPI_DSI0_L1_M    | MIPI D-PHY    | -           | Lana DSI 1 −                                    |
|       7 | GND               | Alimentazione | -           | Massa                                           |
|       8 | GND               | Alimentazione | -           | Massa                                           |
|       9 | MIPI_DSI0_L2_M    | MIPI D-PHY    | -           | Lana DSI 2 −                                    |
|      10 | MIPI_DSI0_L0_P    | MIPI D-PHY    | -           | Lana DSI 0 +                                    |
|      11 | MIPI_DSI0_L2_P    | MIPI D-PHY    | -           | Lana DSI 2 +                                    |
|      12 | MIPI_DSI0_L0_M    | MIPI D-PHY    | -           | Lana DSI 0 −                                    |
|      13 | GND               | Alimentazione | -           | Massa                                           |
|      14 | GND               | Alimentazione | -           | Massa                                           |
|      15 | MIPI_DSI0_L3_M    | MIPI D-PHY    | -           | Lana DSI 3 −                                    |
|      16 | SOC_CAM_MCLK0     | 1,8 V MPU     | GPIO_67     | Clock master della fotocamera 0                 |
|      17 | MIPI_DSI0_L3_P    | MIPI D-PHY    | -           | Corsia DSI 3 +                                  |
|      18 | SOC_CAM_MCLK1     | 1,8 V MPU     | GPIO_68     | Clock master della fotocamera 1                 |
|      19 | GND               | Alimentazione | -           | Massa                                           |
|      20 | GND               | Alimentazione | -           | Massa                                           |
|      21 | CSI0_LN0_M        | MIPI D-PHY    | -           | Lana dati CSI0 0 −                              |
|      22 | CCI_I2C2_SDA      | 1,8 V MPU     | GPIO_59     | Controllo fotocamera I2C2 SDA                   |
|      23 | CSI0_LN0_P        | MIPI D-PHY    | -           | CSI0, corsia dati 0 +                           |
|      24 | CCI_I2C2_SCL      | 1,8 V MPU     | GPIO_60     | Controllo fotocamera I2C2 SCL                   |
|      25 | GND               | Alimentazione | -           | Massa                                           |
|      26 | GND               | Alimentazione | -           | Massa                                           |
|      27 | CSI0_LN1_M        | MIPI D-PHY    | -           | Lana dati CSI0 1 −                              |
|      28 | CSI1_LN3_P        | MIPI D-PHY    | -           | Lana dati CSI1 3 +                              |
|      29 | CSI0_LN1_P        | MIPI D-PHY    | -           | Lana dati CSI0 1 +                              |
|      30 | CSI1_LN3_M        | MIPI D-PHY    | -           | Lana dati CSI1 3 −                              |
|      31 | GND               | Alimentazione | -           | Massa                                           |
|      32 | GND               | Alimentazione | -           | Massa                                           |
|      33 | CSI0_CLK_M        | MIPI D-PHY    | -           | Clock CSI0 −                                    |
|      34 | CSI1_LN2_P        | MIPI D-PHY    | -           | Lana dati CSI1 2 +                              |
|      35 | CSI0_CLK_P        | MIPI D-PHY    | -           | Clock CSI0 +                                    |
|      36 | CSI1_LN2_M        | MIPI D-PHY    | -           | Lana dati CSI1 2 −                              |
|      37 | GND               | Alimentazione | -           | Massa                                           |
|      38 | GND               | Alimentazione | -           | Massa                                           |
|      39 | CSI0_LN2_M        | MIPI D-PHY    | -           | Lana dati CSI0 2 −                              |
|      40 | CSI1_CLK_P        | MIPI D-PHY    | -           | Clock CSI1 +                                    |
|      41 | CSI0_LN2_P        | MIPI D-PHY    | -           | Lana dati CSI0 2 +                              |
|      42 | CSI1_CLK_M        | MIPI D-PHY    | -           | Clock CSI1 −                                    |
|      43 | GND               | Alimentazione | -           | Massa                                           |
|      44 | GND               | Alimentazione | -           | Massa                                           |
|      45 | CSI0_LN3_M        | MIPI D-PHY    | -           | Lana dati CSI0 3 −                              |
|      46 | CSI1_LN1_P        | MIPI D-PHY    | -           | Lana dati CSI1 1 +                              |
|      47 | CSI0_LN3_P        | MIPI D-PHY    | -           | Lana dati CSI0 3 +                              |
|      48 | CSI1_LN1_M        | MIPI D-PHY    | -           | Lana dati CSI1 1 −                              |
|      49 | GND               | Alimentazione | -           | Massa                                           |
|      50 | GND               | Alimentazione | -           | Massa                                           |
|      51 | CCI_I2C0_SCL      | 1,8 V MPU     | GPIO_58     | Controllo fotocamera I2C0 SCL                   |
|      52 | CSI1_LN0_P        | MIPI D-PHY    | -           | Lana dati CSI1 0 +                              |
|      53 | CCI_I2C0_SDA      | 1,8 V MPU     | GPIO_57     | Controllo fotocamera I2C0 SDA                   |
|      54 | CSI1_LN0_M        | MIPI D-PHY    | -           | Lana dati CSI1 0 −                              |
|      55 | GND               | Alimentazione | -           | Massa                                           |
|      56 | GND               | Alimentazione | -           | Massa                                           |
|      57 | VIN IN            | Alimentazione | -           | Ingresso 7-24 V CC (max 1,5 A, protetto da PTC) |
|      58 | +3V3 OUT          | Alimentazione | -           | Uscita di alimentazione a 3,3 V                 |
|      59 | VIN IN            | Alimentazione | -           | Ingresso 7-24 V CC (max 1,5 A, protetto da PTC) |
|      60 | Uscita +3V3       | Alimentazione | -           | Uscita di alimentazione a 3,3 V                 |

>📝 **Note:** I pin VIN su JMEDIA (pin 57 e 59) appartengono alla stessa rete, protetta da un fusibile PTC da 1,5 A (F3, MF-MSMF150/24X) e da un diodo TVS da 24 V. Questi possono fornire alimentazione a una scheda carrier, ma non sono destinati ad alimentare l’intera scheda VENTUNO Q da una fonte esterna.

>📝 **Note:** Le coppie differenziali MIPI CSI/DSI sono segnali D-PHY e non devono essere utilizzate come I/O generici. Tutti i segnali di controllo (CCI_I2C, CAM_MCLK) appartengono al dominio MPU a 1,8 V. Il VIN sui pin 57 e 59 è esclusivamente la tensione di alimentazione in CC.

### JOMEGA

L’header JOMEGA è un connettore di espansione ad alta densità a 100 pin che fornisce segnali USB 3.0, CAN-FD, JTAG, GPIO dell’MPU, SPI e UART per il debug e la gestione dell’alimentazione. I domini di tensione sono misti: l’USB e alcuni segnali di controllo funzionano a 3,3 V, mentre i segnali di debug JTAG, SPI e UART funzionano a 1,8 V nel dominio dell’MPU.

| **Pin** | **Designazione**          | **Dominio**   | **Pin MCU** | **Pin MPU** | **Note**                                       |
| ------: | ------------------------- | ------------- | ----------- | ----------- | ---------------------------------------------- |
|       1 | VIN                       | Alimentazione | -           | -           | Ingresso 7-24 V CC                             |
|       2 | GND                       | Alimentazione | -           | -           | Massa                                          |
|       3 | VIN                       | Alimentazione | -           | -           | Ingresso 7-24 V CC                             |
|       4 | GND                       | Alimentazione | -           | -           | Massa                                          |
|       5 | VIN                       | Alimentazione | -           | -           | Ingresso 7-24 V CC                             |
|       6 | GND                       | Alimentazione | -           | -           | Massa                                          |
|       7 | VIN                       | Alimentazione | -           | -           | Ingresso 7-24 V CC                             |
|       8 | GND                       | Alimentazione | -           | -           | Massa                                          |
|       9 | VIN                       | Alimentazione | -           | -           | Ingresso 7-24 V CC                             |
|      10 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      11 | VIN                       | Alimentazione | -           | -           | Ingresso 7-24 V CC                             |
|      12 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      13 | VIN                       | Alimentazione | -           | -           | Ingresso 7-24 V CC                             |
|      14 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      15 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      16 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      17 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      18 | USB3.0_1_SS_TX_P          | USB 3.0       | -           | -           | Porta USB 1 SuperSpeed TX+                     |
|      19 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      20 | USB3.0_1_SS_TX_N          | USB 3.0       | -           | -           | Porta USB 1 SuperSpeed TX−                     |
|      21 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      22 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      23 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      24 | USB3.0_1_HS_D_P           | USB 3.0       | -           | -           | Porta USB 1 HighSpeed D+                       |
|      25 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      26 | USB3.0_1_HS_D_N           | USB 3.0       | -           | -           | Porta USB 1 HighSpeed D−                       |
|      27 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      28 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      29 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      30 | USB3.0_1_SS_RX_P          | USB 3.0       | -           | -           | Porta USB 1 SuperSpeed RX+                     |
|      31 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      32 | USB3.0_1_SS_RX_N          | USB 3.0       | -           | -           | Porta USB 1 SuperSpeed RX−                     |
|      33 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      34 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      35 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      36 | USB3.0_2_SS_TX_P          | USB 3.0       | -           | -           | Porta USB 2 SuperSpeed TX+                     |
|      37 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      38 | USB3.0_2_SS_TX_N          | USB 3.0       | -           | -           | Porta USB 2 SuperSpeed TX−                     |
|      39 | IO0_3V3                   | MCU a 3,3 V   | PC0         | -           | GPIO dell’MCU                                  |
|      40 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      41 | IO1_3V3                   | 3,3 V MCU     | PC1         | -           | GPIO MCU                                       |
|      42 | USB3.0_2_HS_D_P           | USB 3.0       | -           | -           | Porta USB 2 HighSpeed D+                       |
|      43 | IO2_3V3                   | 3,3 V MCU     | PC2         | -           | GPIO MCU                                       |
|      44 | USB3.0_2_HS_D_N           | USB 3.0       | -           | -           | Porta USB 2 HighSpeed D−                       |
|      45 | IO3_3V3                   | 3,3 V MCU     | PC3         | -           | GPIO MCU                                       |
|      46 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      47 | IO4_3V3                   | 3,3 V MCU     | PD12        | -           | GPIO MCU                                       |
|      48 | USB3.0_2_SS_RX_P          | USB 3.0       | -           | -           | Porta USB 2 SuperSpeed RX+                     |
|      49 | IO5_3V3                   | MCU a 3,3 V   | PD13        | -           | GPIO MCU                                       |
|      50 | USB3.0_2_SS_RX_N          | USB 3.0       | -           | -           | Porta USB 2 SuperSpeed RX−                     |
|      51 | IO6_3V3                   | 3,3 V MCU     | PD14        | -           | GPIO MCU                                       |
|      52 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      53 | IO7_3V3                   | 3,3 V MCU     | PD15        | -           | GPIO MCU                                       |
|      54 | USB3.0_1_PWRON_3V3        | 3,3 V         | -           | -           | Abilitazione alimentazione porta USB 1         |
|      55 | IO8_3V3                   | 3,3 V MCU     | PI2         | -           | GPIO MCU                                       |
|      56 | USB3.0_1_OVERCUR_3V3      | 3,3 V         | -           | -           | Flag di sovracorrente porta USB 1              |
|      57 | MIC_INP                   | Analogico     | -           | -           | Ingresso microfono+                            |
|      58 | USB3.0_2_PWRON_3V3        | 3,3 V         | -           | -           | Abilitazione alimentazione porta USB 2         |
|      59 | MIC_INN                   | Analogico     | -           | -           | Ingresso microfono−                            |
|      60 | USB3.0_2_OVERCUR_3V3      | 3,3 V         | -           | -           | Flag di sovracorrente porta USB 2              |
|      61 | MIC_BIAS                  | Analogico     | -           | -           | Polarizzazione microfono                       |
|      62 | SPI_ICS_MISO              | 1,8 V MPU     | -           | GPIO_39     | MPU SPI MISO (SPI_ICS_1V8)                     |
|      63 | TMS                       | 1,8 V MPU     | -           | -           | JTAG TMS (JTAG_1V8)                            |
|      64 | SPI_ICS_MOSI              | 1,8 V MPU     | -           | GPIO_40     | MPU SPI MOSI                                   |
|      65 | TDO                       | 1,8 V MPU     | -           | -           | JTAG TDO                                       |
|      66 | SPI_ICS_SCK               | 1,8 V MPU     | -           | GPIO_37     | Clock SPI MPU                                  |
|      67 | TDI                       | 1,8 V MPU     | -           | -           | TDI JTAG                                       |
|      68 | SPI_ICS_CS                | 1,8 V MPU     | -           | GPIO_38     | Selezione chip SPI MPU                         |
|      69 | TCK                       | 1,8 V MPU     | -           | -           | Clock JTAG                                     |
|      70 | PM_PS_HOLD_1V8            | 1,8 V MPU     | -           | -           | Mantenimento stato di alimentazione MPU        |
|      71 | SRST_N                    | 1,8 V MPU     | -           | -           | Reset di sistema JTAG                          |
|      72 | FORCED_USB_BOOT_1V8       | 1,8 V MPU     | -           | GPIO_52     | Modalità di avvio USB forzata                  |
|      73 | TRST_N                    | 1,8 V MPU     | -           | -           | Reset TAP JTAG                                 |
|      74 | PWR_EN_N                  | 1,8 V MPU     | -           | -           | Abilitazione alimentazione (attivo basso)      |
|      75 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      76 | USER_BUTTON               | 3,3 V         | -           | GPIO_79     | Ingresso pulsante utente                       |
|      77 | SOM_VREG_S5S_SPX3_1P8     | Alimentazione | -           | -           | Rotaia SOM RTSS da 1,8 V                       |
|      78 | PM_RESIN_N_3V3            | 3,3 V         | -           | -           | Ingresso di reset del PMIC dell’MPU            |
|      79 | SOM_VREG_MDPX3_1P8        | Alimentazione | -           | -           | Rotaia SOM da 1,8 V                            |
|      80 | RTSS_RESIN_N_1V8          | 1,8 V MPU     | -           | -           | Ingresso di reset RTSS                         |
|      81 | SOM_VREG_MDPX3_1P8        | Alimentazione | -           | -           | Linea SOM a 1,8 V                              |
|      82 | RTSS_PS_HOLD_SPX3_1P8_1V8 | MPU a 1,8 V   | -           | -           | Mantenimento dello stato di alimentazione RTSS |
|      83 | UART_DBG_TX               | 1,8 V MPU     | -           | GPIO_71     | UART TX di debug MPU                           |
|      84 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      85 | UART_DBG_RX               | 1,8 V MPU     | -           | GPIO_72     | UART RX di debug MPU                           |
|      86 | CAN1_TX                   | 3,3 V MCU     | PD5         | -           | Bus CAN-FD 1 TX (senza PHY)                    |
|      87 | PWR_DISABLE_7-24V         | Sistema       | -           | -           | Disattiva il percorso di alimentazione VIN     |
|      88 | CAN1_RX                   | 3,3 V MCU     | PI9         | -           | Bus CAN-FD 1 RX (senza PHY)                    |
|      89 | FORCE_BOOT_3V3            | 3,3 V         | -           | -           | Override avvio forzato                         |
|      90 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      91 | +3V3 OUT                  | Alimentazione | -           | -           | Uscita alimentazione 3,3 V                     |
|      92 | CAN2_TX                   | MCU a 3,3 V   | PA10        | -           | Bus CAN-FD 2 TX (senza PHY)                    |
|      93 | +3V3 OUT                  | Alimentazione | -           | -           | Uscita alimentazione 3,3 V                     |
|      94 | CAN2_RX                   | 3,3 V MCU     | PD9         | -           | Bus CAN-FD 2 RX (senza PHY)                    |
|      95 | +3V3 OUT                  | Alimentazione | -           | -           | Uscita di alimentazione a 3,3 V                |
|      96 | GND                       | Alimentazione | -           | -           | Massa                                          |
|      97 | +5V OUT                   | Alimentazione | -           | -           | Uscita di alimentazione a 5 V                  |
|      98 | CAN3_TX                   | MCU a 3,3 V   | PF6         | -           | Bus CAN-FD 3 TX (senza PHY)                    |
|      99 | +5V OUT                   | Alimentazione | -           | -           | Uscita alimentazione 5 V                       |
|     100 | CAN3_RX                   | 3,3 V MCU     | PF7         | -           | Bus CAN-FD 3 RX (senza PHY)                    |

>📝 **Note:** I segnali JTAG e SPI ICS appartengono al dominio MPU a 1,8 V. Si prega di non applicare direttamente la logica a 3,3 V. I bus CAN FD su JOMEGA non dispongono di un livello fisico PHY; è necessario un ricetrasmettitore CAN esterno. I pin VIN sono destinati esclusivamente all’ingresso di alimentazione.

### Connettori MIPI CSI per telecamere (J3_1, J3_2, J3_3)

VENTUNO Q mette a disposizione tre connettori indipendenti per telecamere MIPI CSI (J3_1, J3_2, J3_3), ciascuno dei quali è un connettore FPC a 22 pin (TF31-22S-0.5SH, passo da 0,5 mm). Ciascuno supporta telecamere MIPI CSI-2 a 4 lane. I segnali di controllo (I2C, GPIO) funzionano a **3,3 V** sia per il GPIO di abilitazione sul pin 17 sia per i bus I2C sui pin 20–21. I segnali I2C vengono convertiti internamente a 1,8 V prima di raggiungere il bus `CCI_I2C` del SoM. Le coppie differenziali MIPI sono D-PHY e non devono essere utilizzate come GPIO.

#### J3_1 - Telecamera 2

| **Pin** | **Designazione** | **Dominio**   | **Pin MPU** | **Note**                                                                  |
| ------: | ---------------- | ------------- | ----------- | ------------------------------------------------------------------------- |
|       1 | GND              | Alimentazione | -           | Massa                                                                     |
|       2 | LN0_M            | MIPI D-PHY    | -           | Lana dati CSI2 0 −                                                        |
|       3 | LN0_P            | MIPI D-PHY    | -           | Lana dati CSI2 0 +                                                        |
|       4 | GND              | Alimentazione | -           | Massa                                                                     |
|       5 | LN1_M            | MIPI D-PHY    | -           | Lana dati CSI2 1 −                                                        |
|       6 | LN1_P            | MIPI D-PHY    | -           | Lana dati CSI2 1 +                                                        |
|       7 | GND              | Alimentazione | -           | Massa                                                                     |
|       8 | CLK_M            | MIPI D-PHY    | -           | Lana di clock CSI2 −                                                      |
|       9 | CLK_P            | MIPI D-PHY    | -           | Linea di clock CSI2 +                                                     |
|      10 | GND              | Alimentazione | -           | Massa                                                                     |
|      11 | LN2_M            | MIPI D-PHY    | -           | Linea dati CSI2 2 −                                                       |
|      12 | LN2_P            | MIPI D-PHY    | -           | Lana dati CSI2 2 +                                                        |
|      13 | GND              | Alimentazione | -           | Massa                                                                     |
|      14 | LN3_M            | MIPI D-PHY    | -           | Lana dati CSI2 3 −                                                        |
|      15 | LN3_P            | MIPI D-PHY    | -           | Lana dati CSI2 3 +                                                        |
|      16 | GND              | Alimentazione | -           | Massa                                                                     |
|      17 | GPIO_PIN17_3V3   | 3,3 V         | GPIO_82     | GPIO della fotocamera                                                     |
|      18 | NON COLLEGATO    | -             | -           | -                                                                         |
|      19 | GND              | Alimentazione | -           | Massa                                                                     |
|      20 | SCL              | 3,3 V         | GPIO_62     | Clock I2C della fotocamera (CCI_I2C4, con conversione di livello a 1,8 V) |
|      21 | SDA              | 3,3 V         | GPIO_61     | Dati I2C della fotocamera (CCI_I2C4, con conversione di livello a 1,8 V)  |
|      22 | +3V3             | Alimentazione | -           | Alimentazione a 3,3 V per il modulo fotocamera                            |

#### J3_2 - Fotocamera 0

| **Pin** | **Designazione** | **Dominio**   | **Pin MPU** | **Note**                                                                  |
| ------: | ---------------- | ------------- | ----------- | ------------------------------------------------------------------------- |
|       1 | GND              | Alimentazione | -           | Massa                                                                     |
|       2 | LN0_M            | MIPI D-PHY    | -           | Lana dati CSI0 0 −                                                        |
|       3 | LN0_P            | MIPI D-PHY    | -           | Lana dati CSI0 0 +                                                        |
|       4 | GND              | Alimentazione | -           | Massa                                                                     |
|       5 | LN1_M            | MIPI D-PHY    | -           | Lana dati CSI0 1 −                                                        |
|       6 | LN1_P            | MIPI D-PHY    | -           | Lana dati CSI0 1 +                                                        |
|       7 | GND              | Alimentazione | -           | Massa                                                                     |
|       8 | CLK_M            | MIPI D-PHY    | -           | Lana di clock CSI0 −                                                      |
|       9 | CLK_P            | MIPI D-PHY    | -           | Linea di clock CSI0 +                                                     |
|      10 | GND              | Alimentazione | -           | Massa                                                                     |
|      11 | LN2_M            | MIPI D-PHY    | -           | Linea dati CSI0 2 −                                                       |
|      12 | LN2_P            | MIPI D-PHY    | -           | Lana dati CSI0 2 +                                                        |
|      13 | GND              | Alimentazione | -           | Massa                                                                     |
|      14 | LN3_M            | MIPI D-PHY    | -           | Lana dati CSI0 3 −                                                        |
|      15 | LN3_P            | MIPI D-PHY    | -           | Lana dati CSI0 3 +                                                        |
|      16 | GND              | Alimentazione | -           | Massa                                                                     |
|      17 | GPIO_PIN17_3V3   | 3,3 V         | GPIO_64     | GPIO della fotocamera                                                     |
|      18 | NON COLLEGATO    | -             | -           | -                                                                         |
|      19 | GND              | Alimentazione | -           | Massa                                                                     |
|      20 | SCL              | 3,3 V         | GPIO_58     | Clock I2C della fotocamera (CCI_I2C0, con conversione di livello a 1,8 V) |
|      21 | SDA              | 3,3 V         | GPIO_57     | Dati I2C della fotocamera (CCI_I2C0, con conversione di livello a 1,8 V)  |
|      22 | +3V3             | Alimentazione | -           | Alimentazione a 3,3 V per il modulo fotocamera                            |

#### J3_3 - Fotocamera 1

| **Pin** | **Denominazione** | **Dominio**   | **Pin MPU** | **Note**                                                                  |
| ------: | ----------------- | ------------- | ----------- | ------------------------------------------------------------------------- |
|       1 | GND               | Alimentazione | -           | Massa                                                                     |
|       2 | LN0_M             | MIPI D-PHY    | -           | Lana dati CSI1 0 −                                                        |
|       3 | LN0_P             | MIPI D-PHY    | -           | Lana dati CSI1 0 +                                                        |
|       4 | GND               | Alimentazione | -           | Massa                                                                     |
|       5 | LN1_M             | MIPI D-PHY    | -           | Lana dati CSI1 1 −                                                        |
|       6 | LN1_P             | MIPI D-PHY    | -           | Lana dati CSI1 1 +                                                        |
|       7 | GND               | Alimentazione | -           | Massa                                                                     |
|       8 | CLK_M             | MIPI D-PHY    | -           | Lana di clock CSI1 −                                                      |
|       9 | CLK_P             | MIPI D-PHY    | -           | Linea di clock CSI1 +                                                     |
|      10 | GND               | Alimentazione | -           | Massa                                                                     |
|      11 | LN2_M             | MIPI D-PHY    | -           | Linea dati CSI1 2 −                                                       |
|      12 | LN2_P             | MIPI D-PHY    | -           | Lana dati CSI1 2 +                                                        |
|      13 | GND               | Alimentazione | -           | Massa                                                                     |
|      14 | LN3_M             | MIPI D-PHY    | -           | Lana dati CSI1 3 −                                                        |
|      15 | LN3_P             | MIPI D-PHY    | -           | Lana dati CSI1 3 +                                                        |
|      16 | GND               | Alimentazione | -           | Massa                                                                     |
|      17 | GPIO_PIN17_3V3    | 3,3 V         | GPIO_75     | GPIO della fotocamera                                                     |
|      18 | NON COLLEGATO     | -             | -           | -                                                                         |
|      19 | GND               | Alimentazione | -           | Massa                                                                     |
|      20 | SCL               | 3,3 V         | GPIO_60     | Clock I2C della fotocamera (CCI_I2C2, con conversione di livello a 1,8 V) |
|      21 | SDA               | 3,3 V         | GPIO_59     | Dati I2C della fotocamera (CCI_I2C2, con conversione di livello a 1,8 V)  |
|      22 | +3V3              | Alimentazione | -           | Alimentazione a 3,3 V per il modulo fotocamera                            |

>📝 **Note:** Le linee differenziali MIPI D-PHY non sono I/O generici.

## Periferiche ad alta velocità

### Connettività di rete

Wi-Fi® 6 tri-banda (2,4/5/6 GHz) e Bluetooth® 5.3 tramite il modulo integrato NFA725B. Connettività cablata tramite Ethernet RJ45 a 2,5 Gbps (PHY QCA-8081).

### Archiviazione

Archiviazione NVMe Gen 4 espandibile tramite connettore M.2 2230 Key M (MDT580M01001), collegato direttamente al SOM QCS8275 tramite un’interfaccia PCIe Gen 4 a 4 lane. Lo slot M.2 non è avviabile, in conformità con le specifiche del QCS8275. L’alimentazione dello slot viene attivata in modo indipendente tramite un interruttore di carico MP5077GG-Z controllato dall’MPU.

Lo switch di pacchetti PCIe Gen 2 PI7C9X2G304EV presente sulla scheda è dedicato al controller host USB 3.0 xHCI (TUSB7340RKMR) e al modulo Wi-Fi® (NFA725B).

> 📝 **Note:** L’MPU gestisce l’alimentazione dello slot M.2. Se l’MPU non ha completato l’avvio o se la gestione dell’alimentazione non è stata abilitata, un’unità NVMe installata non riceverà alimentazione e non verrà rilevata. Si tratta di un comportamento previsto durante le prime fasi dell’avvio.

### USB-C

Il connettore USB-C supporta la commutazione dei ruoli host/dispositivo, la commutazione dei ruoli di alimentazione, l’uscita in modalità alternativa DisplayPort (Alt-Mode) e la negoziazione USB Power Delivery fino a 20 V tramite il controller PD CYPD6129-52LQXI. Le coppie differenziali SuperSpeed sul connettore USB-C sono condivise tra i dati USB 3.0 SuperSpeed e la modalità alternativa DisplayPort tramite il multiplexer USB eDP integrato (TMUXHS4446RETT).

**Quando la modalità alternativa DisplayPort è attiva**, le linee SuperSpeed vengono riassegnate a DisplayPort. I dati USB vengono quindi limitati alle velocità USB 2.0 (HighSpeed, 480 Mbps) esclusivamente sulla coppia HS_D+/D−. La piena velocità dei dati USB 3.0 SuperSpeed è disponibile solo quando la modalità alternativa DisplayPort non è attiva.

Il CYPD6129 monitora sia il VBUS che il VIN per determinare lo stato di alimentazione della scheda e negozia i profili PD di conseguenza. Il LED di errore (rosso, GPIO9/P4.1 sul CYPD6129) indica le condizioni di errore. Di seguito sono riassunti i principali scenari di alimentazione:

| **Scenario**                                                                    | **Risultato atteso**                                                                      |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| VIN collegato, USB non collegato                                                | Sistema alimentato da VIN, controller PD in modalità batteria                             |
| VIN collegato, USB collegato                                                    | Sistema alimentato da VIN, negoziazione PD e ruolo dati consentiti                        |
| VIN non collegato, da USB-C a USB-C                                             | Sistema alimentato da VBUS, avvia la negoziazione PD, con obiettivo 20 V a 3 A            |
| VIN non collegato, da USB-C a USB-A                                             | PD rileva una sorgente non PD, sistema spento, LED di errore lampeggiante                 |
| VIN non collegato, da USB-C a USB-A -> VIN collegato al volo                    | PD riconosce il VIN, sblocca il VIN, mantiene VBUS bloccato                               |
| VIN non collegato, da USB-C a USB-C (potenza negoziata) → VIN collegato al volo | Sistema alimentato da VBUS, VIN disattivato, il LED di errore mostra una sequenza diversa |

>📝 **Note:** Il CYPD6129 è programmato per richiedere un profilo di tensione PD superiore a 5 V prima di abilitare il percorso di alimentazione principale. Il collegamento tramite un cavo standard da USB-C a USB-A, o una porta USB-C che fornisce solo 5 V senza negoziazione PD, non alimenterà la scheda e causerà il lampeggiamento del LED di errore. Utilizzi sempre un alimentatore USB-C compatibile con PD che supporti 9 V, 15 V o 20 V per un funzionamento affidabile alimentato tramite USB-C.
>
> Il CYPD6129 rimane sempre alimentato tramite un convertitore buck dedicato (LMR51440SDRRR, U26) alimentato da qualsiasi fonte di alimentazione collegata, consentendogli di monitorare e negoziare l’alimentazione in modo indipendente prima di abilitare il percorso di alimentazione della scheda principale.

### USB Tipo A

Entrambe le porte USB 3.0 Tipo A sono protette in modo indipendente da interruttori di carico dedicati (MP5077GG-Z). Il VBUS di ciascuna porta è limitato in modo rigido a 1,71 A dalla rete di resistori ILIM. L’abilitazione dell’alimentazione per ciascuna porta è gestita dal TUSB7340RKMR.

| **Parametro**              | **Valore**                            |
| -------------------------- | ------------------------------------- |
| Tensione VBUS              | 5 V                                   |
| Corrente massima per porta | 1,71 A (impostata da ILIM, per porta) |
| Protezione                 | Interruttore di carico MP5077GG-Z     |
| Controllo di abilitazione  | TUSB7340RKMR                          |

>📝 **Note:** Il limite di corrente di 1,71 A per porta è impostato a livello hardware e non può essere sovrascritto a livello software. Non tentare di bypassare l’interruttore di carico.

### Display

La scheda fornisce le seguenti uscite video:

- **HDMI** tramite il connettore HDMI dedicato, gestito dal bridge DSI-HDMI ADV7535 integrato. L’ADV7535 utilizza le linee MIPI DSI provenienti dal SoM. Quando l’HDMI è attivo, le linee MIPI-DSI sull’header JMEDIA non sono disponibili.
- **DisplayPort Alt Mode** tramite il connettore USB-C attraverso il multiplexer USB eDP integrato (TMUXHS4446RETT).
- **MIPI DSI su JMEDIA** disponibile quando l’uscita HDMI non è attiva (richiede la configurazione dell’overlay DSI).

### Telecamera

VENTUNO Q supporta l’ingresso della telecamera tramite tre connettori MIPI CSI integrati (J3_1, J3_2, J3_3) e tramite l’header del carrier JMEDIA.

**VENTUNO Q in modalità standalone (impostazione predefinita):**

Tutti e tre i connettori CSI integrati (J3_1, J3_2, J3_3) sono disponibili contemporaneamente per l’ingresso della telecamera. Si tratta di una configurazione dedicata esclusivamente alla telecamera e MIPI DSI non è attivo per impostazione predefinita. L’uscita video è disponibile tramite il connettore HDMI o la modalità alternativa DisplayPort su USB-C.

>📝 **Note:** Il [modulo mini-telecamera Arducam IMX577](https://www.arducam.com/arducam-imx577-mini-camera-module-for-qualcomm-rb3g2.html) (codice articolo B0488) è compatibile con VENTUNO Q tramite i suoi connettori MIPI CSI integrati. Si prega di consultare il [Manuale d’uso di VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) per le istruzioni relative al collaudo e alla configurazione.

**VENTUNO Q con una scheda carrier compatibile:**

Una scheda carrier collegata a JMEDIA consente di utilizzare un display MIPI DSI insieme alle telecamere integrate. Se l’overlay DSI della scheda carrier è abilitato, la telecamera 0 (J3_2) non è disponibile, poiché condivide il bus CCI_I2C0 (GPIO_57/58) con l’header JMEDIA. Le telecamere 1 (J3_3) e 2 (J3_1) rimangono disponibili.

>📝 **Note:** La disponibilità delle telecamere quando è collegata una scheda carrier dipende dalla configurazione specifica della scheda stessa. Per ulteriori dettagli, si prega di consultare la documentazione della scheda carrier.

<div style="page-break-after: always;"></div>

## Funzionamento del dispositivo

### Per iniziare - Arduino App Lab

Arduino App Lab [1] è un editor unificato che consente di creare ed eseguire progetti su entrambi i processori di VENTUNO Q. Combina la programmazione embedded (sketch), lo sviluppo Linux e l’intelligenza artificiale edge in un unico ambiente.

Un progetto è un’**App** che può includere:

- Un programma Python® in esecuzione sul sistema Linux (Qualcomm Dragonwing™ IQ8)
- Uno sketch Arduino in esecuzione sul microcontrollore (STM32H5F5)
- **Bricks** opzionali (servizi preconfigurati quali modelli di IA, server web o client API) che vengono distribuiti insieme all’App e funzionano sul sistema Linux.

Le App utilizzano **Bridge** per lo scambio di dati tra il lato Linux e il microcontrollore.

**Tre configurazioni. Un’unica esperienza.**

![](assets/ABX00181_modes.png)

- **Modalità computer a scheda singola:** App Lab viene eseguito direttamente su VENTUNO Q. Collegate un monitor tramite HDMI (o USB-C), una tastiera e un mouse per ottenere un ambiente di sviluppo all-in-one. Non è necessario alcun PC.
- **Modalità ospitata su PC:** collegate VENTUNO Q al vostro computer tramite USB-C o rete ed eseguite App Lab sul vostro PC.
- **Modalità in rete:** VENTUNO Q funziona in modalità headless, senza display, tastiera o mouse. Accedete alla scheda da remoto tramite Wi-Fi® o Ethernet.

>📝 **Note:** In modalità **PC Hosted**, per la configurazione iniziale è necessaria una connessione dati USB. Successivamente, è possibile utilizzare il target **Network** tramite LAN (SSH).

In modalità **Computer a scheda singola**, non è necessario alcun collegamento dati USB: accendete la scheda e utilizzate la destinazione **Rete** una volta che questa si sarà collegata alla vostra rete. Le periferiche USB (tastiera, mouse, videocamera USB, microfono) possono essere collegate direttamente alle porte USB-A integrate. Quando la modalità alternativa DisplayPort è attiva sulla porta USB-C, la velocità di trasmissione dati USB viene ridotta.

Per le istruzioni complete di installazione, la configurazione iniziale e le indicazioni per il primo utilizzo, consultare il [Manuale d’uso di VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Note:** se si effettua l’alimentazione tramite USB-C per la prima volta, il LED di errore potrebbe lampeggiare quando la scheda è collegata a un computer o a una porta USB-C non PD. La scheda richiede un’alimentazione compatibile con PD di almeno 9 V per l’avvio. Per un funzionamento a piena prestazione, comprese l’inferenza AI, le periferiche collegate e gli HAT collegati, si raccomanda un’alimentazione di 12 V o superiore tramite USB-C PD (fino a 20 V) oppure tramite il connettore cilindrico o i morsetti a vite (7-24 V). Si rimanda alla sezione [Alimentazione in ingresso](#potenza-in-ingresso) per i limiti di tensione e corrente per ciascuna fonte.

>📝 **Note:** Il primo avvio richiede 20-30 secondi durante l’avvio di Linux. La matrice LED visualizza un’animazione di avvio quando viene caricato il bootloader dell’MCU ed è in esecuzione uno sketch valido. Attendere il completamento di tale processo prima di interagire con la scheda. Se l’animazione non viene visualizzata, si prega di consultare il [Manuale d’uso di VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) per ulteriori dettagli.

### Bricks

I "Bricks" sono moduli preconfezionati disponibili in Arduino App Lab, che includono modelli di intelligenza artificiale, servizi web, integrazioni di sensori, database e interfacce utente, i quali vengono distribuiti insieme alla vostra app sul lato Linux senza che sia necessario scrivere l’infrastruttura sottostante. Per una guida completa alla selezione e all’utilizzo dei Bricks, si rimanda al [Manuale d’uso di VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Note:** mentre un’App è associata e in esecuzione, le interfacce USB potrebbero essere occupate dal sistema. Per utilizzare strumenti CLI esterni tramite USB, arrestare l’App o scollegare la scheda.

### Pulsanti e modalità di avvio

VENTUNO Q include due pulsanti integrati: un **pulsante verticale** e un **pulsante utente**.

![](assets/ABX00181_vertical_button.png)

### Pulsante verticale

Il pulsante verticale è collegato al pin GPIO PK13 dell’MCU. Può essere utilizzato per interagire con la scheda e spegnerla.

- **Pressione singola (modalità Single-Board Computer):** attiva una finestra di dialogo di spegnimento sullo schermo. L’utente può confermare per spegnere immediatamente oppure annullare per chiudere la finestra e proseguire il normale funzionamento. Se non viene effettuata alcuna interazione, la scheda si spegne automaticamente dopo 60 secondi.
- **Pressione prolungata (oltre 10 secondi, modalità SSH / ADB):** Spegne completamente il sistema. La scheda rimarrà spenta fino a quando l’alimentazione non verrà scollegata e ricollegata.

>📝 **Note:** Lo spegnimento tramite pressione prolungata arresta completamente l’ambiente Linux e interrompe tutte le applicazioni in esecuzione. Si raccomanda di salvare il lavoro e di assicurarsi che i processi esterni siano stati arrestati in modo sicuro, ove applicabile. La scheda si avvia automaticamente all’alimentazione e non è necessario premere il pulsante per un avvio normale.

### Pulsante utente

![](assets/ABX00181_user_button.png)

Il pulsante utente è collegato all’MPU (GPIO_79) ed è disponibile come ingresso generico. Può essere letto dalle applicazioni e dagli script Linux utilizzando interfacce GPIO standard. Per ulteriori esempi di utilizzo, si rimanda al [Manuale d’uso di VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

<div style="page-break-after: always;"></div>

## Informazioni meccaniche

La scheda misura 160 mm × 100 mm. L’altezza totale, esclusi il dissipatore di calore e la ventola del SoM, è di 25,8 mm. Il connettore JHAT a 40 pin è conforme alle specifiche meccaniche standard HAT di Raspberry Pi®, garantendo la compatibilità fisica con gli accessori HAT conformi.

![](assets/ABX00181_general_dimensions.svg)

I connettori UNO Shield mantengono la spaziatura standard dell’Arduino UNO, garantendo la compatibilità meccanica ed elettrica diretta con l’ecosistema UNO Shield.

La scheda presenta tre serie di fori con diverse funzioni meccaniche:

- **4 distanziatori M2,5** (altezza 5 mm, saldati alla scheda) per il montaggio del dissipatore di calore, situati a 9,78 mm dal bordo destro e a 10,02 mm e 42,63 mm dal bordo superiore.
- **4 fori di montaggio angolari da 3,2 mm** per l’installazione in involucri, su pannelli o su schede carrier personalizzate e accessori.
- **2× 3,2 mm** fori di montaggio HAT conformi alle specifiche meccaniche standard Raspberry Pi® HAT, compatibili con distanziatori M3 per il fissaggio di accessori HAT.
- **1× distanziatore M2** (altezza 4 mm) per il fissaggio di una scheda di memoria M.2 2230 NVMe nello slot M.2.

VENTUNO Q viene fornito con 4 distanziatori esagonali M3 e 4 dadi M3, contenuti in una bustina separata. In ambienti sensibili alle scariche elettrostatiche (ESD), fissare un distanziatore e un dado a ciascuno dei quattro fori di montaggio angolari per sollevare la scheda dalla superficie di lavoro e aumentare lo spazio libero.

| **Articolo**               | **Dimensioni**                                                                 |
| -------------------------- | ------------------------------------------------------------------------------ |
| Distanziatore esagonale M3 | Lunghezza esagono 20 mm, lunghezza filettatura 6 mm, diametro filettatura 3 mm |
| Dado M3                    | Altezza 2,4 mm, larghezza esagono 5,6 mm, diametro interno 3 mm                |

![](assets/ABX00181_esd_standoff.png)

### Dissipatore di calore e progettazione termica del SoM

Il SoM Qualcomm® Dragonwing™ IQ8 (QCS8275) richiede un raffreddamento attivo per un funzionamento prolungato a piena prestazione. L’ingombro del SoM sulla scheda misura **57,5 mm × 57,5 mm**, con il centro situato a **14,26 mm** dal bordo sinistro e a **14,73 mm** dal bordo inferiore, con uno scostamento orizzontale di **8,95 mm** e uno scostamento verticale di **8,55 mm** rispetto all’area attiva del SoM.

![](assets/ABX00181_active_fan.png)

I quattro distanziatori M2,5 definiscono lo schema di montaggio per il gruppo dissipatore e ventola in dotazione, posizionato simmetricamente attorno all’ingombro del SoM per garantire una forza di serraggio uniforme su tutto il coperchio del SoM.

Nelle condizioni più sfavorevoli, con MPU, NPU e GPU in funzione contemporaneamente a piena potenza, la scheda può assorbire circa 25 W o più. La soluzione di raffreddamento attivo inclusa è ottimizzata per questo carico termico. Si assicuri che la ventola rimanga operativa durante carichi di lavoro prolungati ad alte prestazioni.

![](assets/ABX00181_som_heatsink.svg)

>📝 **Note:** L’utilizzo della scheda in presenza di carichi di lavoro intensi legati all’intelligenza artificiale o all’elaborazione senza un raffreddamento adeguato può innescare il throttling termico del SoM QCS8275, riducendone le prestazioni. Verifichi sempre il margine termico per il Suo caso d’uso specifico e l’ambiente dell’involucro.

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

## Marchi commerciali

I termini HDMI, HDMI High-Definition Multimedia Interface, l’immagine commerciale HDMI e i loghi HDMI sono marchi o marchi registrati di HDMI Licensing Administrator, Inc.

# Informazioni sull’azienda

| Ragione sociale | Arduino S.r.l.                              |
| --------------- | ------------------------------------------- |
| Indirizzo       | Via Andrea Appiani 25, 20900 Monza (Italia) |

# Riferimenti alla documentazione

| N.  | Riferimento               | Link                                                                                       |
| :-: | ------------------------- | ------------------------------------------------------------------------------------------ |
|  1  | Arduino App Lab           | [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)                   |
|  2  | Documentazione VENTUNO Q  | [https://docs.arduino.cc/hardware/ventuno-q/](https://docs.arduino.cc/hardware/ventuno-q/) |
|  3  | Project Hub               | [https://projecthub.arduino.cc/](https://projecthub.arduino.cc/)                           |
|  4  | Riferimenti alla libreria | [https://docs.arduino.cc/libraries/](https://docs.arduino.cc/libraries/)                   |
|  5  | Negozio Arduino           | [https://store.arduino.cc/](https://store.arduino.cc/)                                     |

# Cronologia delle revisioni del documento

| **Data**   | **Revisione** | **Modifiche**  |
| :--------: | :-----------: | -------------- |
| 25/08/2026 |       1       | Prima versione |
