---
identifier: ABX00181
title: Arduino® VENTUNO™ Q
type: maker
---

![](assets/featured.png)

# Español

# Descripción

Arduino® VENTUNO™ Q es un ordenador de IA periférico de alto rendimiento diseñado específicamente para la IA y la robótica de última generación. Al combinar a la perfección la informática de nivel industrial con la actuación en tiempo real, VENTUNO Q le ofrece la potencia de procesamiento necesaria para implementar modelos complejos de IA y el control de precisión para manipular el mundo físico, todo ello desde un único y compacto dispositivo periférico.

En su núcleo se encuentra una revolucionaria arquitectura Dual-Brain: el robusto microprocesador (MPU) Qualcomm Dragonwing™ IQ8 (QCS8275) (MPU), que ofrece hasta 40 TOPS densos de computación de IA para visión artificial avanzada y modelos de lenguaje grandes (LLM) locales que ejecutan un sistema operativo Ubuntu Linux completo (también compatible con Debian), mientras que el microcontrolador (MCU) dedicado STM32H5F5 de STMicroelectronics, que ejecuta Arduino Core en el sistema operativo Zephyr, garantiza la precisión de baja latencia necesaria para el control complejo de motores y la robótica.

VENTUNO Q le permite mantenerse conectado y listo para su implementación. Cuenta con conectividad Wi-Fi® 6 (tribanda) y Bluetooth® 5.3 integradas, junto con un completo conjunto de conectores incorporados, entre los que se incluyen USB 3.0 de alta velocidad, HDMI, Ethernet de 2,5 Gb y un conector M.2 para almacenamiento NVMe Gen 4 ampliable. La placa es compatible de forma nativa con el amplio ecosistema de shields y carriers de Arduino UNO, así como con los HAT de Raspberry Pi® a través de un conector de 40 pines y con los nodos Arduino Modulino® mediante el conector Qwiic.

# Áreas de aplicación

IA en el borde, LLM/VLM locales, hogar inteligente, robótica, control de movimiento, ciudad inteligente, visión industrial, educación e investigación

<div style="page-break-after: always;"></div>

# ÍNDICE

## Ejemplos de aplicación

VENTUNO Q combina un procesador Linux con capacidad de IA con un microcontrolador en tiempo real, lo que ofrece lo mejor de la computación de alto nivel y el control determinista. Está diseñado específicamente para creadores y desarrolladores que desean una IA capaz de moldear directamente el mundo físico.

- **Asistentes de IA y hogar inteligente:** Cree asistentes de voz sin conexión, centros de control locales, quioscos con interfaz sin contacto y traductores de voz en tiempo real.
- **Robótica y control de movimiento:** Robots móviles autónomos (AMR) que utilizan SLAM visual, manipuladores guiados por visión y robots de compañía y de servicio.
- **Ciudades inteligentes y visión industrial:** monitores de tráfico en el borde de la red, inspección automatizada de la calidad en líneas de montaje, seguridad proactiva de instalaciones y supervisión de inventario basada en la visión.
- **Educación e investigación:** kits avanzados de aprendizaje de IA, prototipado rápido para investigación, asistentes de programación por voz y plataformas móviles de investigación en manipulación.

<div style="page-break-after: always;"></div>

## Características

### Variantes de VENTUNO Q

VENTUNO Q está disponible en una variante:

- **ABX00181**: 16 GB de RAM LPDDR5, 64 GB de almacenamiento eMMC

### Resumen de las especificaciones generales

#### Procesador y memoria

![](assets/ABX00181_ic_overview.png)

| **Subsistema**      | **Detalles**                                                                                              |
| ------------------- | --------------------------------------------------------------------------------------------------------- |
| MPU principal       | Qualcomm Dragonwing™ IQ8 (QCS8275)                                                                        |
|                     | CPU: Arm® Cortex® de ocho núcleos                                                                         |
|                     | GPU Adreno™ 623 (gráficos 3D y OpenCL)                                                                    |
|                     | VPU Adreno™ 623 (procesamiento de vídeo)                                                                  |
|                     | Procesador de IA Hexagon™ Tensor (NPU): hasta 40 TOPS densos                                              |
|                     | Procesador de señal de imagen (ISP) Qualcomm Spectra 692                                                  |
|                     | Sistema operativo Ubuntu Linux (también compatible con Debian)                                            |
| MCU en tiempo real  | ST STM32H5F5 (MCU), Arm® Cortex®-M33 hasta 250 MHz                                                        |
|                     | Núcleo Arduino en el sistema operativo Zephyr                                                             |
|                     | 4 MB de memoria Flash, 1,5 MB de RAM                                                                      |
| Memoria del sistema | eMMC de 64 GB para el sistema operativo y los datos                                                       |
|                     | Memoria OSPI SAIL (MX25UW25345GXDI00-TR) para el arranque de la MCU y datos compartidos                   |
|                     | Conector M.2 Key M 2230 para almacenamiento NVMe Gen 4 (PCIe x4 directamente desde el SOM, no arrancable) |
|                     | 2 × 8 GB de RAM LPDDR5 (16 GB en total)                                                                   |

#### Conectividad y medios

![](assets/ABX00181_connector_overview.png)

| **Subsistema**    | **Detalles**                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Red e inalámbrico | Wi-Fi® 6 a 2,4/5/6 GHz (tribanda) con 2 antenas integradas (módulo NFA725B)                                             |
|                   | Bluetooth® 5.3 con antena integrada                                                                                     |
|                   | 1 puerto Ethernet RJ45 de 2,5 Gbit (QCA-8081 PHY)                                                                       |
| Conectores USB    | 1 puerto USB-C con conmutación de función de host/dispositivo, conmutación de función de alimentación y salida de vídeo |
|                   | 2 puertos USB 3.0 tipo A                                                                                                |
|                   | 2 puertos USB 3.0 en el conector JOMEGA                                                                                 |
| Vídeo             | 1 salida HDMI a través del DSI bridge a HDMI ADV7535 integrado. HDMI y MIPI DSI comparten                               |
|                   | las mismas líneas DSI; cuando HDMI está activo, el MIPI DSI del conector JMEDIA queda multiplexado                      |
|                   | Salida de vídeo (modo alternativo DP) a través de USB-C                                                                 |
| Cámara            | 3 conectores MIPI CSI integrados en la placa (J3_1, J3_2, J3_3)                                                         |
|                   | 2 carriles MIPI CSI también disponibles en el conector JMEDIA (multiplexados con los conectores integrados)             |
|                   | Compatibilidad con cámaras USB a través de USB tipo A o USB-C                                                           |
| Audio             | Códec de audio: MAX98091ETM+T (Maxim)                                                                                   |
|                   | En JMISC: 1 salida de línea mono, 1 salida de altavoz mono, 1 salida de auriculares estéreo, 1 entrada de micrófono     |
|                   | En JOMEGA: 1 entrada de micrófono                                                                                       |
| Interfaces CAN    | 1 CAN-FD con PHY (ATA6563-GBQW1) en terminal de tornillo, controlado por la MCU (STM32H5F5)                             |
|                   | Las líneas CAN-H y CAN-L están protegidas con TVS (PJGBLC24C-AU_R1_000A1, bidireccionales, 24 V, 350 W)                 |
|                   | Terminación dividida integrada en el bus CAN con bornes de tornillo (2 × 60,4 Ω + 100 nF)                               |
|                   | 3× CAN-FD (sin PHY) en el conector JOMEGA, con multiplexación de pines a través de la MCU                               |
|                   | 1× CAN-FD (sin PHY) en los conectores del UNO Shield (D4/D5), con multiplexación de pines a través de la MCU            |

>📝 **Nota:** El bus CAN del terminal de tornillo incluye una terminación dividida integrada (2 × 60,4 Ω + 100 nF). Si la placa no se encuentra al final del bus, se debe tener en cuenta esta terminación al diseñar la topología de la red.

#### Ampliación y conectores

| **Interfaz (conector)**            | **Detalles**                                                                                                                                                           |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conectores UNO Shield              | - Compatibles con los shields estándar de Arduino UNO (lógica de 3,3 V)                                                                                                |
|                                    | - La mayoría de los pines digitales admiten 5 V. Los pines A0 y A1 de JANALOG son entradas directas del ADC y no admiten 5 V                                           |
| Conector de expansión (JOMEGA)     | - Amplias capacidades de expansión, incluyendo USB 3.0, CAN-FD, JTAG, MIC IN y SPI de la MPU                                                                           |
| Conectores Carrier                 | - JMEDIA: canales de cámara MIPI CSI0/CSI1 y canales de pantalla MIPI-DSI a 1,8 V                                                                                      |
|                                    | - JMISC: terminales de audio, GPIO de la MPU a 1,8 V y señales de la MCU a 3,3 V                                                                                       |
| Conector Qwiic                     | - I2C (3,3 V) conectado a la MCU para un acceso «plug-and-play» instantáneo a los nodos Modulino®                                                                      |
| Conector JHAT                      | - Conector de 40 pines compatible con Raspberry Pi® (GPIO de la MPU, con conversión de nivel a 3,3 V para compatibilidad con HAT mediante TXS0108ERKSR y TXS0104ERUTR) |
| JCTL (depuración remota de la MPU) | - Conector de 10 pines (2×5) para la depuración remota de la MPU, compatible con [Arduino Bughopper](https://docs.arduino.cc/hardware/bughopper/)                      |

<div style="page-break-after: always;"></div>

## Características técnicas

### Alimentación de entrada

| **Fuente**                       | **Rango de tensión** | **Corriente máxima** | **Conector**                      |
| -------------------------------- | -------------------: | -------------------: | --------------------------------- |
| USB-C PD                         |               9-20 V |            hasta 3 A | Conector USB-C                    |
| Conector cilíndrico (5,5×2,1 mm) |               7-24 V |            hasta 5 A | Conector cilíndrico de 5,5×2,1 mm |
| Terminal de tornillo             |               7-24 V |           hasta 10 A | Terminal de tornillo              |

![Opciones de alimentación de entrada](assets/ABX00181_power_options.png)

Ambas vías de entrada cuentan con protección TVS (SMBJ24CA, bidireccional de 24 V) y pasan a través de interruptores de alimentación independientes (KTS1900GXAA-TA + SQS414CENW-T1_GE3) hasta una etapa de detección de corriente (INA232AIDDFR). Dos convertidores reductores multifásicos (MPQ4371GVE-1001-AECC901-Z) generan el raíl principal de 3,3 V, mientras que otro convertidor reductor (MPQ4371GVE-1001-AECC901-Z) genera el raíl de 5 V. El controlador USB-C® PD (CYPD6129-52LQXI) negocia perfiles de tensión de hasta 20 V a partir de fuentes de alimentación USB-C® compatibles.

> 📝 **Nota sobre la corriente de entrada de CC y el presupuesto de potencia:** El conector tipo barril tiene una capacidad nominal máxima de 5 A. El presupuesto de potencia disponible depende de la tensión de entrada: a 7 V (5 A), la potencia máxima suministrable es de 35 W; a 12 V, es de 60 W; a 24 V es de 120 W. En las peores condiciones, con la MPU, la NPU y la GPU funcionando simultáneamente a pleno rendimiento, solo el SoM puede consumir aproximadamente entre 23 y 25 W. La placa completa, incluyendo el PHY de Ethernet, el códec de audio, el concentrador USB y otros circuitos integrados integrados, consumirá más, lo que deja un margen limitado a 7 V antes de alcanzar el límite del conector.
>
> Al alimentar la placa a 7 V, asegúrese de tener en cuenta la caída de tensión en el cable, ya que la placa requiere un mínimo de 7 V en sus conectores y no se encenderá con una tensión inferior a 7 V.
>
> Los dos puertos USB tipo A pueden suministrar cada uno hasta 5 V × 1,71 A = 8,55 W, lo que supone un consumo adicional máximo combinado de aproximadamente 17 W. Con la placa a plena potencia y ambos puertos USB tipo A a carga máxima, el consumo total puede acercarse a los 42 W, lo que supera el límite de 35 W de la toma de CC a 7 V y conlleva el riesgo de dañar el conector.
>
> El raíl de 3,3 V para shields UNO, HAT y Qwiic (`+3V3_LIMITED`) está limitado a 2,8 A (aproximadamente 9,3 W como máximo). La línea de 5 V para shields y HATs (`+5V_LIMITED`) también está limitada a 2,8 A (máximo de ~14 W). Tenga en cuenta que las líneas de 3,3 V y 5 V suministradas a los conectores de la carrier UNO y a JOMEGA **no** tienen limitación de corriente.
>
> **Se recomienda encarecidamente el funcionamiento a 12 V o 24 V** para cualquier implementación que implique inferencia de IA, periféricos USB y shields o HATs conectados simultáneamente.
>
> Para cargas de trabajo intensas que impliquen inferencia de IA, periféricos USB o aplicaciones ampliadas, se recomienda una fuente de alimentación con una potencia nominal de **60 W o superior** en todas las fuentes de alimentación, a fin de garantizar que el funcionamiento se mantenga estable durante posibles picos de consumo. Cuando se utilice el **conector cilíndrico** (5,5 × 2,1 mm, máx. 5 A), se recomienda, a modo de ejemplo, una fuente de alimentación de **12 V / 5 A o 24 V / 3 A**.

### Condiciones de funcionamiento recomendadas

| **Parámetro**                     | **Símbolo**      | **Mínimo** | **Típico** | **Máximo** | **Unidad** |
| --------------------------------- | ---------------- | :--------: | :--------: | :--------: | :--------: |
| Entrada USB-C PD                  | V<sub>USBC</sub> |     9      |     -      |    20,0    |     V      |
| Entrada de CC (conector/tornillo) | V<sub>IN</sub>   |    7,0     |     -      |    24,0    |     V      |
| Vía de 5,0 V (salida)             | V<sub>+5V</sub>  |    4,75    |    5,0     |    5,25    |     V      |
| Vía de 3,3 V (salida)             | V<sub>3P3</sub>  |    3,14    |    3,3     |    3,47    |     V      |
| Temperatura de funcionamiento     | T<sub>OP</sub>   |    -10     |     -      |     60     |     °C     |

>📝 **Nota:** El controlador USB-C® PD admite varios perfiles de tensión (9 V, 15 V, 20 V) cuando se conecta a una fuente de alimentación compatible con PD.

### Líneas de tensión de la placa

| **Tensión** | **Rail**              | **Origen/Regulador**                                                                                              |
| :---------: | --------------------- | ----------------------------------------------------------------------------------------------------------------- |
|   7-24 V    | V<sub>IN</sub>        | Entrada con conector jack/bornes de tornillo (protegida con TVS, SMBJ24CA)                                        |
|    5,0 V    | +5 V                  | Convertidor reductor MPQ4371GVE                                                                                   |
|    3,3 V    | +3,3 V                | 2 convertidores reductores MPQ4371GVE                                                                             |
|    1,8 V    | SOM_VREG_MDPX3_1P8    | Carril de 1,8 V del dominio de aplicación principal del SOM (accesible al usuario a través de JMISC, JCTL)        |
|    1,8 V    | SOM_VREG_S5S_SPX3_1P8 | Exclusivamente para el dominio del subsistema de seguridad del SOM (RTSS); no apto para uso general               |
|    1,8 V    | +1V8                  | Convertidor reductor MPQ2179GQHE (para los circuitos integrados integrados QCA8081, ADV7535, MAX98091)            |
|   1,28 V    | +1,28 V               | LDO MP20312GTF (para el códec de audio MAX98091)                                                                  |
|    1,1 V    | +1,1 V                | Convertidor reductor MPQ2179GQHE (para las placas con circuitos integrados TUSB7340RKMR, QCA8081 y PI7C9X2G304EV) |

>📝 **Nota:** La placa cuenta con tres líneas de alimentación independientes de 1,8 V. `SOM_VREG_MDPX3_1P8` es la línea de alimentación del dominio de aplicación principal del SoM QCS8275 y constituye la referencia recomendada para todas las interfaces de 1,8 V accesibles al usuario, incluidas JMISC y JCTL. `SOM_VREG_S5S_SPX3_1P8` es el raíl del dominio del subsistema de seguridad (RTSS) del SoM y no debe utilizarse como fuente de alimentación o referencia de uso general. `+1V8` es la tensión de 1,8 V a nivel de placa generada por el convertidor reductor MPQ2179GQHE, que alimenta el PHY Ethernet QCA-8081, el display bridge ADV7535 y el códec de audio MAX98091.

>📝 **Nota:** Independientemente de los raíles mencionados anteriormente, el pin 59 del JMISC admite una batería de respaldo del RTC de hasta 3,3 V para mantener los relojes en tiempo real (RTC) del SOM y de la MCU cuando la placa no recibe alimentación por otros medios. `SOM_VCOIN` (RTC del SOM) y `VBAT` (RTC de la MCU) son dos entradas de batería de respaldo para el RTC que están conectadas físicamente entre sí en este único pin, en lugar de a un raíl de alimentación compartido. Cada una se conecta a través de su propia resistencia de 0 Ω a un nodo común, que está protegido por un diodo TVS bidireccional (Vr = 5,5 V) con referencia a tierra. El consumo de corriente previsto es muy bajo, y este pin no suministra alimentación para mantener el resto de la placa encendida.

### Consumo energético típico

Las siguientes mediciones se basan en una temperatura ambiente de 24,4 °C, utilizando un analizador de potencia, con tres métodos de entrada de alimentación: 12 V CC, 24 V CC y USB-C® PD a 20 V. Los ejemplos «Blink» en la MCU, «Hello World» en la MPU, «Edge AI Assistant» y «Detect Objects» en la cámara del smartphone están disponibles como ejemplos integrados en Arduino App Lab. El ejemplo «Smart Mirror» se basa en una nota de aplicación específica.

#### Consumo energético típico: 12 V CC

| **Escenario**                                     | **Potencia media** | **Potencia mínima** | **Potencia máxima** |
| ------------------------------------------------- | -----------------: | ------------------: | ------------------: |
| Booting                                           |             7,07 W |                   – |              17,9 W |
| «Blink» en la MCU                                 |             7,42 W |              5,30 W |              12,6 W |
| «Hello World» en la MPU                           |             7,52 W |              5,32 W |              13,3 W |
| «Edge AI Assistant»                               |             13,5 W |              6,13 W |              24,6 W |
| Ejemplo de «Smart Mirror»¹                        |             14,7 W |              7,65 W |              33,0 W |
| Detección de objetos con la cámara del smartphone |             9,63 W |              5,80 W |              21,2 W |

#### Consumo energético típico - 24 V CC

| **Escenario**                                     | **Potencia media** | **Potencia mínima** | **Potencia máxima** |
| ------------------------------------------------- | -----------------: | ------------------: | ------------------: |
| Booting                                           |             9,71 W |                   – |              23,7 W |
| «Blink» en la MCU                                 |             10,6 W |              7,04 W |              18,9 W |
| «Hello World» en la MPU                           |             10,8 W |              7,09 W |              18,3 W |
| Asistente de IA en el borde                       |             15,5 W |              7,44 W |              28,8 W |
| Ejemplo de «Smart Mirror»¹                        |             17,3 W |              8,47 W |              36,6 W |
| Detección de objetos con la cámara del smartphone |             11,5 W |              7,88 W |              24,7 W |

#### Consumo energético típico - USB-C® PD (20 V)

| **Escenario**                                     | **Potencia media** | **Potencia mínima** | **Potencia máxima** |
| ------------------------------------------------- | -----------------: | ------------------: | ------------------: |
| Booting                                           |             6,56 W |                   – |              20,2 W |
| «Blink» en la MCU                                 |             7,84 W |              6,33 W |              16,1 W |
| «Hello World» en la MPU                           |             9,68 W |              6,42 W |              16,1 W |
| Asistente de IA en el borde                       |             15,3 W |              6,61 W |              25,6 W |
| Ejemplo de «Smart Mirror»¹                        |             15,1 W |              8,05 W |              34,2 W |
| Detección de objetos con la cámara del smartphone |             11,3 W |              7,85 W |              23,1 W |

¹ Configuración de prueba del «Smart Mirror»: cámara USB Logitech BRIO 4K, auriculares USB (micrófono y altavoces) y una pantalla HDMI conectada.

>📝 **Nota:** Las mediciones se realizaron utilizando un analizador de potencia Otii Ace Pro a modo de referencia. El pico máximo registrado en todos los escenarios y fuentes de entrada fue de 36,6 W (ejemplo de Smart Mirror a 24 V CC), dentro de la recomendación de una fuente de alimentación de 60 W o más mencionada anteriormente.

<div style="page-break-after: always;"></div>

## Descripción general del funcionamiento

### Distribución de pines

![](assets/ABX00181_pinout.png)

### Diagrama de bloques

![Descripción general completa del diagrama de bloques](assets/ABX00181_block_diagram.png)

![Diagrama de bloques (página 1/2)](assets/ABX00181_block_diagram_pg1.png)

![Diagrama de bloques (página 2/2)](assets/ABX00181_block_diagram_pg2.png)

### Fuente de alimentación

VENTUNO Q admite dos vías de entrada de alimentación independientes: un puerto USB-C® con negociación de Power Delivery (PD) de hasta 20 V, y una entrada de 7-24 V CC a través del conector cilíndrico de 5,5 × 2,1 mm o del terminal de tornillo. Ambas vías están protegidas por TVS bidireccionales de 24 V y se canalizan a través de un circuito «OR» de potencia formado por interruptores de potencia independientes, protegidos contra polaridad inversa y corriente inversa (KTS1900 + 2x NMOS), antes de llegar a los convertidores reductores.

Un circuito integrado de detección de corriente (INA232AIDDFR) supervisa la corriente de entrada total a lo largo de la vía activa. Dos convertidores reductores multifásicos (MPQ4371GVE-1001-AECC901-Z) generan el raíl principal de `+3,3 V`, que alimenta el SOM (QCS8275) y los periféricos de 3,3 V de la placa. Un tercer convertidor reductor MPQ4371GVE genera el raíl de `+5 V`.

Un convertidor reductor MPQ2179GQHE genera la tensión de `+1V8`, que alimenta el PHY Ethernet QCA-8081, el display bridge ADV7535 y el códec de audio MAX98091. Un convertidor reductor MPQ2179GQHE genera la tensión de `+1,1 V`, que alimenta al TUSB7340RKMR y al conmutador PCIe QCA-8081 y PI7C9X2G304EV.

El SOM proporciona la línea de tensión del dominio de aplicación principal «MDPX3_1P8» (1,8 V) a través de su PMIC interno («SOM_VREG_MDPX3_1P8»), al que el usuario puede acceder mediante JMISC y JCTL. La línea independiente «SOM_VREG_S5S_SPX3_1P8» está dedicada al subsistema de seguridad en tiempo real (RTSS). No debe utilizarse como referencia de uso general. Un LDO MP20312GTF genera la línea de «+1,28 V» para el códec de audio MAX98091.

Los interruptores de carga MP5077GG-Z dedicados controlan de forma independiente la ranura M.2 NVMe, el raíl `+3V3_LIMITED` (para UNO Shield, HAT y Qwiic) y el raíl `+5V_LIMITED` (para shield y HAT). La línea de alimentación VBUS de cada puerto USB tipo A está habilitada y protegida por el TUSB7340RKMR. El resto de interruptores de carga periféricos se controlan mediante líneas de habilitación controladas por los pines GPIO del SOM, lo que permite a la MPU desconectar de la alimentación los subsistemas que no se estén utilizando.

![Descripción general completa del árbol de alimentación del Arduino VENTUNO Q](assets/ABX00181_power_tree.png)

![alimentación del Arduino VENTUNO Q (página 1/3)](assets/ABX00181_power_tree_pg1.png)

![alimentación del Arduino VENTUNO Q (página 2/3)](assets/ABX00181_power_tree_pg2.png)

![alimentación del Arduino VENTUNO Q (página 3/3)](assets/ABX00181_power_tree_pg3.png)

<div style="page-break-after: always;"></div>

## Interfaz de usuario e indicadores

| **Indicador**       | **Tipo**                          | **Controlador**                              | **Notas**                                                     |
| ------------------- | --------------------------------- | -------------------------------------------- | ------------------------------------------------------------- |
| Matriz de LED       | 104 LED azules (LTST-C191TBKT-5A) | MCU a través de GPIO                         | Matriz de pantalla programable                                |
| 4 LED RGB           | LTST-C28NBEGK-2A                  | MCU a través de GPIO                         | Indicadores de estado direccionables por el usuario           |
| LED de alimentación | Verde (LTST-C190KGKT)             | Hardware (+3V3)                              | Indica que el raíl de +3V3 está activo                        |
| LED de fallo        | Rojo (XHY-STB0603SR)              | Controlador USB-C® PD (CYPD6129, GPIO9/P4.1) | Indica una condición de fallo detectada por el controlador PD |

- **4 LED RGB:** Cuatro LED tricolores controlados por el microcontrolador (MCU) STM32H5F5 a través de 12 pines GPIO individuales (3 por LED). Son direccionables por el usuario y pueden utilizarse para indicar el estado de la aplicación, el estado de conectividad o eventos personalizados desde un sketch de Arduino.

| **Designador** | **LED RGB** | **Rojo** | **Verde** | **Azul** |
| -------------- | ----------- | -------- | --------- | -------- |
| DL1_1          | LED RGB 1   | PG3      | PG6       | PK2      |
| DL1_2          | LED RGB 2   | PG4      | PD10      | PK1      |
| DL1_3          | LED RGB 3   | PD11     | PG5       | PK0      |
| DL1_4          | LED RGB 4   | PG2      | PG8       | PC6      |

![](assets/ABX00181_rgb_led.png)

>📝 Los LED RGB son de nivel bajo activo y se encienden cuando se les aplica un nivel lógico «0».

- **Matriz de LED:** Una matriz de LED monocromática azul de 8×13 (104 píxeles) controlada por el microcontrolador STM32H5F5. Muestra la animación de arranque durante aproximadamente 20-30 segundos mientras se inicia Linux. Acceder a la matriz antes de que finalice el arranque puede interferir en el funcionamiento del microcontrolador.

>📝 **Nota:** La animación de arranque solo se reproduce cuando se ha cargado el gestor de arranque de la MCU y se está ejecutando un sketch válido. Si no aparece, consulte el [Manual de usuario de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) para obtener más detalles.

![](assets/ABX00181_matrix.png)

- **LED de alimentación:** Indicador verde (LTST-C190KGKT) conectado al raíl `+3V3`. Se ilumina siempre que la placa recibe alimentación.

- **LED de fallo:** Indicador rojo controlado por el controlador USB-C® PD (CYPD6129, GPIO9/P4.1). Indica una condición de fallo detectada por el controlador PD.

![](assets/ABX00181_status_led.png)

## MPU y MCU

Una MPU (unidad de microprocesador) es un procesador de aplicaciones de alto rendimiento diseñado para ejecutar un sistema operativo completo y software complejo. Una MCU (unidad de microcontrolador) es un controlador pequeño y de bajo consumo diseñado para una sincronización rápida y precisa de las operaciones de E/S y el control. VENTUNO Q combina ambas unidades para aunar la capacidad de cálculo a nivel de sistema operativo con un control ágil y en el que el tiempo es un factor crítico en una única placa, y para comunicarse a través de Bridge, una capa RPC implementada en ambos lados.

### Procesador de aplicaciones (MPU)

El Qualcomm® Dragonwing™ IQ8 (QCS8275) es un procesador Arm® Cortex® de ocho núcleos que ejecuta el sistema operativo Ubuntu Linux (también es compatible con Debian). Sus E/S funcionan a 1,8 V y gestionan interfaces multimedia de alta velocidad e inferencia de IA.

- Dominio de tensión: 1,8 V para el GPIO de la MPU (SoC) y las interfaces de alta velocidad.
- Controla JMEDIA: carriles de cámara MIPI CSI y carriles de pantalla MIPI-DSI.
- Controla los GPIO de la MPU a 1,8 V y los terminales de audio en los conectores «Carrier» (JMEDIA, JMISC).
- USB-C: el cambio de función se gestiona a través del controlador PD CYPD6129, que se encarga de la negociación PD de forma independiente (admite perfiles de hasta 20 V).
- Salida DisplayPort a través del multiplexor USB eDP (TMUXHS4446RETT) en el conector USB-C.
- Ejecuta la NPU Hexagon™ (hasta 40 TOPS densos) y la GPU Adreno™ 623 para tareas de IA en el borde y cargas de trabajo gráficas.

### Microcontrolador (MCU) en tiempo real

El STM32H5F5 de STMicroelectronics® es un Arm® Cortex®-M33 que ejecuta Arduino Core en el sistema operativo Zephyr a 250 MHz. Proporciona una sincronización rápida y determinista para robótica, control de motores y E/S generales.

- Dominio de tensión: 3,3 V para GPIO e interfaces analógicas.
- Gestiona el ADC, el PWM, la matriz de LED, los LED RGB y los temporizadores.
- Gestiona los conectores de 3,3 V: JDIGITAL, JANALOG y JSPI.
- Controla todas las interfaces CAN-FD: PHY en el terminal de tornillo y puertos sin PHY en los conectores JOMEGA y UNO Shield.

JMISC gestiona ambos dominios: las líneas de la MPU a 1,8 V conviven con las señales de la MCU a 3,3 V (PSSI, I²C, GPIO) y el audio analógico. Compruebe siempre los niveles de tensión al conectar carriers o circuitos lógicos externos a JMISC.

>📝 **Nota sobre VDDIO2:** El STM32H5F5 tiene un dominio de alimentación de E/S secundario (VDDIO2) alimentado por `SOM_VREG_MDPX3_1P8` (1,8 V). Esto permite que determinados pines de la MCU se comuniquen directamente con la MPU a 1,8 V sin necesidad de convertidores de nivel externos. Las siguientes interfaces funcionan en el dominio VDDIO2:
>
>- **MCU I2C1** se utiliza para la comunicación directa entre la MCU y la MPU
>- **Los pines GPIO de la MCU PG9, PG10, PG11, PG12, PG13 y PG14** se comunican directamente con la MPU a 1,8 V
>
> No aplique lógica de 3,3 V a estos pines. El resto de señales GPIO de la MCU funcionan a 3,3 V en el dominio VDDIO estándar.

>⚠️ **Advertencia sobre el nivel de tensión:** Las señales GPIO de la MPU funcionan a 1,8 V, mientras que las señales GPIO de la MCU funcionan a 3,3 V. Asegúrese de que cualquier conexión externa a los conectores de expansión sea compatible con el nivel de tensión de su respectivo dominio de procesador para evitar daños en el hardware.

## Comunicación entre procesadores

El Qualcomm® Dragonwing™ IQ8 (QCS8275) (MPU) y el STM32H5F5 (MCU) se comunican a través del Arduino Bridge, una capa de llamada a procedimiento remoto (RPC) basada en software e implementada tanto en el lado de Linux como en el de la MCU. Bridge proporciona una API orientada a servicios que permite a cualquiera de los procesadores exponer servicios para que el otro los invoque, al tiempo que admite notificaciones unidireccionales para eventos asíncronos. Gestiona el enrutamiento de mensajes entre procesadores y admite múltiples medios de transporte físicos.

A través de su API, Bridge permite llamadas a funciones con seguridad de tipos, lo que permite que los sketches del microcontrolador invoquen servicios de Linux y reciban respuestas estructuradas o envíen datos mediante notificaciones.

La capa de transporte físico entre los dos procesadores incluye las siguientes interfaces:

| **Interfaz** | **Dirección**     | **Finalidad**                                                     |
| ------------ | ----------------- | ----------------------------------------------------------------- |
| USB 2.0      | SoC -> MCU (host) | Transporte de datos de gran ancho de banda                        |
| SWD          | SoC -> MCU        | Interfaz de depuración (con conversión de nivel de 1,8 V a 3,3 V) |

Si se requiere un indicador de hardware para una placa carrier o una lógica externa, el firmware puede dedicar un GPIO de la MPU a 1,8 V en JMISC, o un GPIO disponible de JCTL, como salida de «listo» o de «activación». Esta señal puede recibirse en un GPIO de la MCU a través de circuitos compatibles de nivel, como un cambiador de nivel o una configuración de drenaje abierto con una resistencia pull-up.

>📝 Las señales GPIO de la MPU funcionan en el dominio de baja tensión del procesador de aplicaciones (1,8 V). Asegúrese de que cualquier conexión al microcontrolador sea compatible en cuanto a nivel con su rail de tensión de E/S (3,3 V). Por ejemplo, utilice un convertidor de nivel o una configuración de drenaje abierto con una resistencia pull-up conectada al rail de E/S del microcontrolador.

<div style="page-break-after: always;"></div>

## Aceleración por hardware

VENTUNO Q proporciona aceleración por hardware para IA en el borde, gráficos 3D y codificación/decodificación de vídeo a través del procesador de IA Hexagon™ Tensor (NPU), la GPU Adreno™ 623 y la VPU Adreno™ 623 integrados.

### Aceleración de IA (NPU)

El procesador de IA Hexagon™ Tensor integrado ofrece hasta 40 TOPS (teraoperaciones por segundo) densos de cálculo de redes neuronales. Permite a VENTUNO Q ejecutar de forma offline modelos de lenguaje a gran escala (LLM), modelos de visión y lenguaje (VLM) y complejas cadenas de procesamiento de visión artificial.

La NPU está integrada con Qualcomm AI Stack y es compatible de forma nativa con Arduino App Lab. Los desarrolladores pueden implementar modelos optimizados mediante **TensorFlow Lite, ONNX Runtime y PyTorch**. VENTUNO Q también cuenta con integración directa con **Edge Impulse Studio** para el entrenamiento y la implementación rápidos de modelos de IA en el borde personalizados sin necesidad de escribir código repetitivo.

| **Componente**     | **Especificaciones**                                    |
| ------------------ | ------------------------------------------------------- |
| Procesador         | Procesador de IA Hexagon™ Tensor                        |
| Rendimiento máximo | Hasta 40 TOPS densos                                    |
| Arquitectura       | Hexagon DSP + cuatro coprocesadores HVX + dos HMX       |
| Marcos compatibles | TensorFlow Lite, ONNX Runtime, PyTorch                  |
| Integración        | Qualcomm AI Stack, Arduino App Lab, Edge Impulse Studio |

### Aceleración gráfica (GPU)

La GPU Adreno™ 623 proporciona gráficos 3D acelerados por hardware y computación de propósito general (GPGPU) en el SoM QCS8275. En Qualcomm Linux, la aceleración por GPU se proporciona a través de la pila de controladores Adreno, propiedad de Qualcomm, mediante el controlador del núcleo KGSL.

Para consultar las especificaciones completas del hardware de la GPU, remítase a la [Ficha técnica del QCS8275 (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html) y la [Guía de gráficos de Qualcomm Linux](https://docs.qualcomm.com/doc/80-70018-19/topic/).

>📝 **Nota:** Las librerías del controlador Adreno y los archivos de firmware se encuentran en `/lib/firmware/` en el dispositivo. Es posible que no todas las funciones de la GPU que figuran en la documentación del QCS8275 estén disponibles en el software distribuido con VENTUNO Q. Consulte la [Documentación de VENTUNO Q](https://docs.arduino.cc/hardware/ventuno-q/) para ver la lista actualizada de funciones compatibles.

### Aceleración de vídeo (VPU)

La VPU 623 de Adreno™ proporciona procesamiento de vídeo acelerado por hardware en el SoM QCS8275. Los códecs y resoluciones compatibles, así como los detalles de integración, dependen de la pila de software distribuida con la placa. Para consultar las especificaciones completas del hardware, consulte la [Ficha técnica del QCS8275 (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html).

>📝 **Nota:** Es posible que no todos los códecs o marcos de trabajo que figuran en la documentación del QCS8275 estén disponibles en el software distribuido con VENTUNO Q. Consulte la [documentación de VENTUNO Q](https://docs.arduino.cc/hardware/ventuno-q/) para obtener la lista actualizada de funciones compatibles.

>📝 **Nota:** Los complementos de GStreamer específicos de Qualcomm (`gstreamer1.0-plugins-qcom`) no se incluyen de forma predeterminada en la imagen de Ubuntu distribuida con VENTUNO Q. Se pueden instalar manualmente cuando se necesite la captura de cámara con aceleración por hardware o flujos de vídeo. Consulte el [Manual de usuario de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) para obtener detalles sobre la configuración.

<div style="page-break-after: always;"></div>

## Periféricos y conectores

VENTUNO Q pone a su disposición su arquitectura de doble núcleo a través de un completo conjunto de conectores y cabezales. Los conectores controlados por la MCU funcionan con una tensión lógica de **3,3 V**, mientras que los controlados por la MPU lo hacen a **1,8 V**. Compruebe siempre el dominio de tensión de cualquier conector antes de conectar periféricos externos para evitar daños en el hardware.

### JANALOG

El conector JANALOG proporciona entradas analógicas, líneas de alimentación y señales de control de la MCU. Es compatible con la disposición estándar de los conectores analógicos del Arduino UNO. Las entradas analógicas toman como referencia `VREF+` en la línea de 3,3 V y no deben superar `VDD + 0,3 V` (~3,6 V). **No aplique 5 V a los pines analógicos**. `IOREF` es una salida de referencia de 3,3 V, por lo que no debe utilizarse para retroalimentar corriente a través de ella.

| **Pin** | **Designación** | **Red**               | **Dominio**  | **Pin de la MCU** | **Notas**                                        |
| ------: | --------------- | --------------------- | ------------ | ----------------- | ------------------------------------------------ |
|       1 | NC              | JANALOG_BOOT_MCU_3V3  | 3,3 V MCU    | BOOT0             | Circuito de arranque de la MCU                   |
|       2 | IOREF           | +3V3_LIMITED          | Alimentación | -                 | Salida de referencia de tensión de E/S           |
|       3 | Reset           | JANALOG_RESET_MCU_3V3 | MCU de 3,3 V | NRST              | Reset de la MCU                                  |
|       4 | +3V3 OUT        | +3V3_LIMITED          | Alimentación | -                 | Salida de alimentación de 3,3 V                  |
|       5 | +5 V USB        | +5V_LIMITED           | Alimentación | -                 | Salida de alimentación de 5 V (limitada por USB) |
|       6 | GND             | GND                   | Alimentación | -                 | Masa                                             |
|       7 | GND             | GND                   | Alimentación | -                 | Masa                                             |
|       8 | VIN             | 7-24 V                | Alimentación | -                 | Entrada de CC (solo alimentación)                |
|       9 | A0              | JANALOG_A0_MCU_3V3    | Analógico    | PA4               | Entrada del ADC, no tolerante a 5 V              |
|      10 | A1              | JANALOG_A1_MCU_3V3    | Analógico    | PA5               | Entrada del ADC, no tolerante a 5 V              |
|      11 | A2              | JANALOG_A2_MCU_3V3    | Analógica    | PE12              | Entrada del ADC / SPI4_SCK                       |
|      12 | A3              | JANALOG_A3_MCU_3V3    | Analógica    | PE13              | Entrada del ADC / SPI4_MISO                      |
|      13 | A4              | JANALOG_A4_MCU_3V3    | Analógico    | PE14              | Entrada ADC / SPI4_MOSI                          |
|      14 | A5              | JANALOG_A5_MCU_3V3    | Analógico    | PE15              | Entrada ADC                                      |

>📝 **Nota:** A0 y A1 son entradas directas del ADC de la MCU y no admiten 5 V. El rango de entrada válido es de 0 V a `VREF+` (~3,3 V). El pin VIN del pin 8 es una entrada exclusiva para alimentación y no debe utilizarse como GPIO. El pin VIN está protegido por un fusible PTC de 1,1 A, lo que limita su potencia a aproximadamente 26 W a 24 V. No se recomienda alimentar la placa desde este pin a plena carga. Es más adecuado para extraer energía con el fin de alimentar un shield o un periférico que como fuente de alimentación principal de la placa.

>📝 **Nota:** A4 (PE14) y A5 (PE15) son pines exclusivamente analógicos y compatibles con SPI, y no tienen un periférico I2C por hardware. Los shields que requieran I2C en A4 y A5 necesitarán I2C por software (bit-banging). El I2C por hardware está disponible en los pines 17 (SDA, PH12) y 18 (SCL, PH11) de JDIGITAL.

### JDIGITAL

El conector JDIGITAL proporciona señales de E/S digital, UART, SPI, I2C y PWM controladas por la MCU con lógica de 3,3 V. Es compatible con la disposición estándar del conector digital de Arduino UNO.

| **Pin** | **Denominación** | **Net**               | **Dominio**      | **Pin de la MCU** | **Notas**                       |
| ------: | ---------------- | --------------------- | ---------------- | ----------------- | ------------------------------- |
|       1 | D0 / RX          | JDIGITAL_MCU_UART_3V3 | MCU de 3,3 V     | PB11              | UART RX                         |
|       2 | D1 / TX          | JDIGITAL_MCU_UART_3V3 | MCU de 3,3 V MCU | PB10              | UART TX                         |
|       3 | D2               | JDIGITAL_D2_MCU_3V3   | 3,3 V MCU        | PB0               | GPIO                            |
|       4 | D3               | JDIGITAL_D3_MCU_3V3   | 3,3 V MCU        | PB1               | GPIO / PWM                      |
|       5 | D4               | JDIGITAL_D4_MCU_3V3   | MCU de 3,3 V     | PB6               | GPIO / FDCAN2_TX                |
|       6 | D5               | JDIGITAL_D5_MCU_3V3   | MCU de 3,3 V     | PB5               | GPIO / PWM / FDCAN2_RX          |
|       7 | D6               | JDIGITAL_D6_MCU_3V3   | MCU de 3,3 V     | PB2               | GPIO / PWM                      |
|       8 | D7               | JDIGITAL_D7_MCU_3V3   | MCU de 3,3 V MCU | PB3               | GPIO                            |
|       9 | D8               | JDIGITAL_D8_MCU_3V3   | 3,3 V MCU        | PB4               | GPIO                            |
|      10 | D9               | JDIGITAL_D9_MCU_3V3   | 3,3 V MCU        | PB7               | GPIO / PWM                      |
|      11 | D10 / CS         | JDIGITAL_MCU_SPI_3V3  | MCU de 3,3 V     | PB12              | Selección de chip SPI           |
|      12 | D11 / MOSI       | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU        | PB15              | SPI MOSI / PWM                  |
|      13 | D12 / MISO       | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU        | PB14              | SPI MISO                        |
|      14 | D13 / SCK        | JDIGITAL_MCU_SPI_3V3  | 3,3 V MCU        | PB13              | Reloj SPI                       |
|      15 | GND              | GND                   | Alimentación     | -                 | Masa                            |
|      16 | AREF             | JDIGITAL_AREF_MCU_3V3 | Analógico        | -                 | Referencia de tensión analógica |
|      17 | SDA              | JDIGITAL_MCU_I2C_3V3  | MCU de 3,3 V     | PH12              | Datos I2C (I2C4 / I3C1)         |
|      18 | SCL              | JDIGITAL_MCU_I2C_3V3  | MCU de 3,3 V     | PH11              | Reloj I2C (I2C4 / I3C1)         |

>📝 **Nota:** Todas las líneas JDIGITAL son de lógica de MCU a 3,3 V. La mayoría de los pines admiten 5 V como entradas en modo digital. AREF es una entrada de referencia de tensión analógica para el ADC de la MCU. Se canaliza a través de un conmutador analógico integrado (U28, SGM3157YC6/TR) y solo está activa cuando el pin PI8 de la MCU está en estado ALTO.


### JSPI

El conector JSPI ofrece un bus SPI dedicado para conectar periféricos como lectores de tarjetas SD, controladores de pantalla o sensores. También proporciona reset y alimentación. Todas las señales se encuentran en el dominio de 3,3 V de la MCU.

| **Pin** | **Designación** | **Red**          | **Dominio**      | **Pin de la MCU** | **Notas**                     |
| ------: | --------------- | ---------------- | ---------------- | ----------------- | ----------------------------- |
|       1 | MISO            | JSPI_MCU_SPI_3V3 | 3,3 V de la MCU  | PF14              | SPI MISO                      |
|       2 | +5 V            | +5V_LIMITED      | Alimentación     | -                 | Salida de alimentación de 5 V |
|       3 | SCK             | JSPI_MCU_SPI_3V3 | MCU de 3,3 V     | PC10              | Reloj SPI                     |
|       4 | MOSI            | JSPI_MCU_SPI_3V3 | MCU de 3,3 V MCU | PC12              | MOSI SPI                      |
|       5 | Reset           | MCU_NRST         | 3,3 V MCU        | NRST              | Reset de la MCU               |
|       6 | GND             | GND              | Alimentación     | -                 | Masa                          |

>⚠️ **Nota sobre la protección de alimentación:** Los raíles de 3,3 V y 5 V de JSPI y de los conectores del UNO Shield están protegidos por interruptores de carga específicos (MP5077GG-Z), cada uno de ellos con un límite de **2,8 A**. Estos interruptores evitan que los periféricos conectados consuman una corriente excesiva y protegen la placa contra la retroalimentación. No intente puentear ni desactivar estos interruptores.

### Qwiic

El conector Qwiic proporciona un bus I2C de 3,3 V para una conexión «plug-and-play» con nodos Modulino® y sensores de terceros compatibles, sin necesidad de soldaduras. El conector está polarizado, con una única orientación para la conexión.

| **Pin** | **Designación** | **Red**      | **Dominio**  | **Pin de la MCU** | **Notas**                               |
| ------: | --------------- | ------------ | ------------ | ----------------- | --------------------------------------- |
|       1 | GND             | GND          | Alimentación | -                 | Masa                                    |
|       2 | VCC             | +3V3_LIMITED | Alimentación | -                 | Alimentación de 3,3 V para dispositivos |
|       3 | SDA             | I2C3_SDA     | MCU de 3,3 V | PC9               | Datos I2C                               |
|       4 | SCL             | I2C3_SCL     | MCU de 3,3 V | PA8               | Reloj I2C                               |

>📝 **Nota:** Los conectores Qwiic son ampliables mediante conexión en cadena, por lo que se pueden conectar varios módulos en serie en el mismo bus I2C. El bus I2C está conectado a la MCU.

### JCTL (depuración remota de la MPU)

El conector JCTL es un conector de 10 pines (2×5) que proporciona acceso a la consola UART de la MPU, control de anulación del arranque y señales de gestión de alimentación. Arduino Bughopper es la herramienta recomendada para interactuar con este conector. La mayoría de los pines de señal activos están protegidos contra descargas electrostáticas (ESD) mediante diodos TVS (el pin 10 no lo está). Los pines de señal funcionan en dominios de tensión mixtos: 1,8 V, 3,3 V y 7-24 V; consulte la tabla de pines que figura a continuación. El pin 9 expone directamente el raíl `SOM_VREG_MDPX3_1P8`; no aplique ninguna tensión externa a este pin.

| **Pin** | **Designación**        | **Red**            | **Dominio**                    | **Pin de la MPU** | **Notas**                                                                                                                                                                |
| ------: | ---------------------- | ------------------ | ------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|       1 | GND                    | GND                | Alimentación                   | -                 | Masa                                                                                                                                                                     |
|       2 | FORCED_USB_BOOT_N      | FORCE_BOOT_3V3     | 3,3 V                          | -                 | Dominio de 3,3 V. Controla dos NMOS que activan MD_FORCE_USB_BOOT_1V8 y RTSS_FORCE_USB_BOOT_1V8. Póngase en estado BAJO para entrar en modo EDL en el siguiente reinicio |
|       3 | PMIC_POWER_EN          | PMIC_POWER_EN      | 1,8 V MPU                      | -                 | Habilitación de alimentación del PMIC                                                                                                                                    |
|       4 | TX                     | UART_DBG_1V8       | 1,8 V MPU                      | GPIO_43           | Transmisión (TX) del UART de depuración de la MPU                                                                                                                        |
|       5 | GPIO                   | MD_GPIO_103        | 1,8 V MPU                      | GPIO_103          | GPIO de uso general                                                                                                                                                      |
|       6 | RX                     | UART_DBG_1V8       | 1,8 V MPU                      | GPIO_44           | UART de depuración de la MPU (RX)                                                                                                                                        |
|       7 | GND                    | GND                | Alimentación                   | -                 | Masa                                                                                                                                                                     |
|       8 | RESIN_N                | RESIN_N            | 3,3 V                          | -                 | Drenaje abierto, protegido por TVS. Colóquelo en estado BAJO para un reinicio en caliente (los raíles de tensión permanecen activos)                                     |
|       9 | +1V8 OUT               | SOM_VREG_MDPX3_1P8 | Alimentación                   | -                 | Dominio MDPX3 de 1,8 V directo; no aplique tensión externa                                                                                                               |
|      10 | POWER_SWITCH_DISABLE_N | PWR_DISABLE        | 7-24 V (hasta 5 V como máximo) | -                 | Sin protección TVS. Ponga el pin en estado BAJO para un reinicio en frío (controla la alimentación principal)                                                            |

> ⚠️ **Lea esto antes de conectar cualquier cosa al JCTL**
>
> El pin 9 expone directamente `SOM_VREG_MDPX3_1P8` (~1,8 V); no aplique ningún voltaje externo a este pin. Los pines funcionan en dominios de tensión mixtos: los pines 2 y 8 pertenecen al dominio de 3,3 V, los pines 4 y 6 (UART) al de 1,8 V, el pin 10 es la entrada de habilitación para el interruptor de alimentación principal VIN; cuenta con un divisor de tensión interno que permite la conexión directa a VIN; bájelo por debajo de 0,85 V para desactivar la alimentación principal, manténgalo por encima de 1 V para un funcionamiento normal y no supere los 5 V externamente. El pin 10 no cuenta con protección TVS. La aplicación de tensiones incorrectas a cualquier pin activo del JCTL puede dañar de forma permanente el SoM QCS8275.
>
> **Se recomienda encarecidamente el uso del Arduino Bughopper** para la mayoría de los casos de depuración, ya que incluye traductores de nivel y etapas de salida compatibles con drenaje abierto diseñadas específicamente para una interfaz segura con el JCTL.
>
> Si opta por utilizar un adaptador USB a UART diferente o hardware de depuración personalizado, asegúrese de que todas las líneas de señal se alimenten con la tensión correcta para su dominio respectivo, de que el pin 10 nunca supere los 5 V y de que no exista ninguna ruta de retroalimentación de potencia hacia el raíl `SOM_VREG_MDPX3_1P8`.

> 📝 **Resumen del control de arranque:**
> - **Reinicio en caliente** (solo MPU, los raíles de tensión permanecen activos): Ponga el pin 8 (RESIN_N) a NÍVEL BAJO mediante drenaje abierto.
> - **Reinicio en frío** (ciclo completo de alimentación, fuente de alimentación principal desconectada): Ponga el pin 10 (POWER_SWITCH_DISABLE_N) a NÍVEL BAJO mediante un circuito de drenaje abierto.
> - **Modo EDL / Descarga de emergencia**: Ponga el pin 2 (FORCED_USB_BOOT_N) a NÍVEL BAJO mediante un circuito de drenaje abierto y, a continuación, active un reinicio mediante el pin 8 o el pin 10.
>
> Este conector está destinado a fines de desarrollo y depuración.

### JHAT

El conector JHAT es un conector estándar de 40 pines compatible con Raspberry Pi®, controlado por la MPU (QCS8275) con lógica de **3,3 V**. Expone señales I2C, SPI, UART, I2S y GPIO de uso general procedentes de la MPU. Los pines de alimentación suministran 3,3 V y 5 V a los HAT conectados.

Todas las señales GPIO se convierten de nivel desde el dominio de 1,8 V de la MPU al dominio de 3,3 V de los HAT mediante cuatro convertidores de nivel bidireccionales integrados: tres dispositivos TXS0108ERKSR de 8 canales (U33_2, U33_3, U33_4) y un dispositivo TXS0104ERUTR de 4 canales (U21), lo que permite la compatibilidad directa con los diseños estándar de HAT de Raspberry Pi® sin necesidad de cambios de nivel adicionales.

| **Pin** | **Denominación** | **Pin de la MPU** | **Función alternativa** | **Dominio**  | **Notas**                       |
| ------: | ---------------- | ----------------- | ----------------------- | ------------ | ------------------------------- |
|       1 | Salida +3V3      | -                 | -                       | Alimentación | Salida de alimentación de 3,3 V |
|       2 | Salida +5V       | -                 | -                       | Alimentación | Salida de alimentación de 5 V   |
|       3 | GPIO 2 (SDA)     | MD_GPIO_17        | QUP0_SE0_I2C_SDA        | MPU de 3,3 V | Datos I2C1                      |
|       4 | +5V OUT          | -                 | -                       | Alimentación | Salida de alimentación de 5 V   |
|       5 | GPIO 3 (SCL)     | MD_GPIO_18        | QUP0_SE0_I2C_SCL        | 3,3 V MPU    | Reloj I2C1                      |
|       6 | GND              | -                 | -                       | Alimentación | Masa                            |
|       7 | GPIO 4           | MD_GPIO_83        | GPCLK0                  | 3,3 V MPU    | GPIO general                    |
|       8 | GPIO 14 (TX)     | MD_GPIO_86        | QUP1_SE2_UART_TX        | 3,3 V MPU    | UART0 TX                        |
|       9 | GND              | -                 | -                       | Alimentación | Tierra                          |
|      10 | GPIO 15 (RX)     | MD_GPIO_87        | QUP1_SE2_UART_RX        | 3,3 V MPU    | UART0 RX                        |
|      11 | GPIO 17          | MD_GPIO_85        | QUP1_SE2_UART_RFR       | 3,3 V MPU    | UART RFR/RTS                    |
|      12 | GPIO 18 (CLK)    | MD_GPIO_116       | LPI_I2S1_SCK            | 3,3 V MPU    | Reloj PCM                       |
|      13 | GPIO 27          | MD_GPIO_109       | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      14 | GND              | -                 | -                       | Alimentación | Masa                            |
|      15 | GPIO 22          | MD_GPIO_90        | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      16 | GPIO 23          | MD_GPIO_105       | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      17 | Salida +3V3      | -                 | -                       | Alimentación | Salida de alimentación de 3,3 V |
|      18 | GPIO 24          | MD_GPIO_106       | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      19 | GPIO 10 (MOSI)   | MD_GPIO_26        | QUP0_SE3_SPI_MOSI       | 3,3 V MPU    | SPI0 MOSI                       |
|      20 | GND              | -                 | -                       | Alimentación | Masa                            |
|      21 | GPIO 9 (MISO)    | MD_GPIO_25        | QUP0_SE3_SPI_MISO       | 3,3 V MPU    | SPI0 MISO                       |
|      22 | GPIO 25          | MD_GPIO_107       | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      23 | GPIO 11 (SCLK)   | MD_GPIO_27        | QUP0_SE3_SPI_SCK        | 3,3 V MPU    | Reloj SPI0                      |
|      24 | GPIO 8 (CE0)     | MD_GPIO_28        | QUP0_SE3_SPI_CS         | 3,3 V MPU    | CE0 de SPI0                     |
|      25 | GND              | -                 | -                       | Alimentación | Masa                            |
|      26 | GPIO 7 (CE1)     | MD_GPIO_88        | GPIO                    | 3,3 V MPU    | SPI0 CE1                        |
|      27 | GPIO 0 (SDA)     | MD_GPIO_19        | QUP0_SE1_I2C_SDA        | 3,3 V MPU    | I2C0 / EEPROM SDA               |
|      28 | GPIO 1 (SCL)     | MD_GPIO_20        | QUP0_SE1_I2C_SCL        | 3,3 V MPU    | I2C0 / EEPROM SCL               |
|      29 | GPIO 5           | MD_GPIO_89        | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      30 | GND              | -                 | -                       | Alimentación | Masa                            |
|      31 | GPIO 6           | MD_GPIO_80        | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      32 | GPIO 12 (PWM0)   | MD_GPIO_77        | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      33 | GPIO 13 (PWM1)   | MD_GPIO_81        | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      34 | GND              | -                 | -                       | Alimentación | Masa                            |
|      35 | GPIO 19 (FS)     | MD_GPIO_117       | LPI_I2S1_WS             | 3,3 V MPU    | Sincronización de trama PCM     |
|      36 | GPIO 16          | MD_GPIO_84        | QUP1_SE2_UART_CTS       | 3,3 V MPU    | CTS de UART                     |
|      37 | GPIO 26          | MD_GPIO_108       | GPIO                    | 3,3 V MPU    | GPIO general                    |
|      38 | GPIO 20 (DIN)    | MD_GPIO_118       | LPI_I2S1_DATA0          | 3,3 V MPU    | Entrada de datos PCM            |
|      39 | GND              | -                 | -                       | Alimentación | Masa                            |
|      40 | GPIO 21 (DOUT)   | MD_GPIO_119       | LPI_I2S1_DATA1          | 3,3 V MPU    | Salida de datos PCM             |

>📝 **Nota:** Aunque las señales GPIO de la MPU tienen un voltaje interno de 1,8 V, los traductores de nivel integrados TXS0108ERKSR y TXS0104ERUTR las presentan a 3,3 V en el conector JHAT, lo que las hace directamente compatibles con los niveles lógicos estándar de los HAT de Raspberry Pi®. No aplique tensiones superiores a 3,3 V a ningún pin de señal JHAT. Los pines de alimentación (3,3 V y 5 V) son salidas de la placa; por favor, no realice retroalimentación de corriente a través de ellos desde un HAT conectado.

>📝 **Nota:** Los pines 8, 10, 11 y 36 del UART de JHAT (TX, RX, RFR y CTS) comparten el mismo UART QUP1_SE2 que el módulo Wi-Fi®/Bluetooth® LE integrado. Los pines TX, RX y RFR se someten a conversión de nivel a través de U33_4 (TXS0108ERKSR), mientras que el pin CTS se convierte por separado a través de U21 (TXS0104ERUTR) junto con los pines GPIO 26, GPIO 20 (I2S_DATA0) y GPIO 21 (I2S_DATA1) en los pines 37, 38 y 40. Estos pines no están disponibles para el uso de HAT externos siempre que Bluetooth esté activo.

### JMISC

El conector JMISC es un conector de alta densidad de 60 pines que combina el bus paralelo de cámara PSSI de la MCU, los pines GPIO de la MCU, el bus I2C de la MCU, las señales de audio (micrófono, auriculares, salida de altavoz mono y salida de línea), el bus SPI del SoC de la MPU, los pines GPIO de la MPU y las señales I2S de la MPU. Se trata de un conector de voltaje mixto: **las señales de la MCU son de 3,3 V**, **las señales de la MPU son de 1,8 V** y los pines de audio/micrófono son analógicos.

| **Pin** | **Designación**    | **Dominio**     | **Pin de la MCU** | **Pin de la MPU** | **Notas**                                                 |
| ------: | ------------------ | --------------- | ----------------- | ----------------- | --------------------------------------------------------- |
|       1 | MCU_PSSI_D0        | 3,3 V MCU       | PA9               | -                 | Bit de datos PSSI 0                                       |
|       2 | MCU_TRACE_CLK      | 3,3 V MCU       | PE2               | -                 | Reloj de rastreo de la MCU                                |
|       3 | MCU_PSSI_D1        | 3,3 V MCU       | PC7               | -                 | Bit de datos 1 de PSSI                                    |
|       4 | MCU_TRACE_D0       | 3,3 V MCU       | PE3               | -                 | Datos de rastreo 0 de la MCU                              |
|       5 | MCU_PSSI_D2        | 3,3 V MCU       | PC8               | -                 | Bit de datos PSSI 2                                       |
|       6 | MCU_TRACE_D1       | MCU de 3,3 V    | PE4               | -                 | Datos de rastreo de la MCU 1                              |
|       7 | MCU_PSSI_D3        | MCU de 3,3 V    | PE1               | -                 | Bit de datos PSSI 3                                       |
|       8 | MCU_TRACE_D2       | MCU de 3,3 V    | PE5               | -                 | Datos de rastreo de la MCU 2                              |
|       9 | MCU_PSSI_D4        | MCU de 3,3 V    | PC11              | -                 | Bit de datos PSSI 4                                       |
|      10 | MCU_TRACE_D3       | MCU de 3,3 V    | PE6               | -                 | Datos de rastreo de la MCU 3                              |
|      11 | MCU_PSSI_D5        | MCU de 3,3 V    | PD3               | -                 | Bit de datos PSSI n.º 5                                   |
|      12 | MCU_USART2_RX      | MCU de 3,3 V    | PE7               | -                 | Recepción USART2 de la MCU                                |
|      13 | MCU_PSSI_D6        | MCU de 3,3 V    | PF4               | -                 | Bit de datos 6 del PSSI                                   |
|      14 | MCU_USART2_TX      | 3,3 V MCU       | PE8               | -                 | Transmisión (TX) del USART2 de la MCU                     |
|      15 | MCU_PSSI_D7        | 3,3 V MCU       | PI7               | -                 | Bit de datos 7 del PSSI                                   |
|      16 | MCU_I2C_SCL        | 3,3 V MCU       | PF1               | -                 | Reloj I2C2 de la MCU                                      |
|      17 | MCU_PSSI_PDCK      | 3,3 V MCU       | PA6               | -                 | Reloj de píxeles PSSI                                     |
|      18 | MCU_I2C_SDA        | 3,3 V MCU       | PF0               | -                 | Datos I2C2 de la MCU                                      |
|      19 | MCU_PSSI_RDY       | 3,3 V MCU       | PI5               | -                 | PSSI listo                                                |
|      20 | MCU_GPIO_PA0       | 3,3 V MCU       | PA0               | -                 | GPIO de la MCU                                            |
|      21 | MCU_PSSI_DE        | 3,3 V MCU       | PH8               | -                 | Habilitación de datos PSSI                                |
|      22 | MCU_GPIO_PA1       | 3,3 V MCU       | PA1               | -                 | GPIO de la MCU                                            |
|      23 | MCU_UART4_RX       | 3,3 V MCU       | PA11              | -                 | UART4 RX de la MCU                                        |
|      24 | MCU_GPIO_PA2       | 3,3 V MCU       | PA2               | -                 | GPIO de la MCU                                            |
|      25 | MCU_UART4_TX       | 3,3 V MCU       | PA12              | -                 | Salida de transmisión UART4 de la MCU                     |
|      26 | GND                | Alimentación    | -                 | -                 | Masa                                                      |
|      27 | GND                | Alimentación    | -                 | -                 | Masa                                                      |
|      28 | EAR_P              | Analógico       | -                 | -                 | Salida de altavoz P (mono)                                |
|      29 | MIC_INP            | Analógica       | -                 | -                 | Entrada de micrófono+                                     |
|      30 | EAR_M              | Analógica       | -                 | -                 | Salida de altavoz M (mono)                                |
|      31 | MIC_INN            | Analógica       | -                 | -                 | Entrada de micrófono −                                    |
|      32 | LINEOUT_P          | Analógica       | -                 | -                 | Salida de línea P                                         |
|      33 | MIC_BIAS           | Analógica       | -                 | -                 | Polarización del micrófono                                |
|      34 | LINEOUT_M          | Analógica       | -                 | -                 | Salida de línea M                                         |
|      35 | GND                | Alimentación    | -                 | -                 | Masa                                                      |
|      36 | HPH_L              | Analógica       | -                 | -                 | Auriculares izquierdo                                     |
|      37 | SOC_SPI_MISO       | MPU de 1,8 V    | -                 | GPIO_10           | MPU SPI MISO (SE0)                                        |
|      38 | HPH_R              | Analógico       | -                 | -                 | Auricular derecho                                         |
|      39 | SOC_SPI_MOSI       | 1,8 V MPU       | -                 | GPIO_11           | MPU SPI MOSI (SE0)                                        |
|      40 | HPH_REF            | Analógico       | -                 | -                 | Referencia de auriculares                                 |
|      41 | SOC_SPI_SCK        | 1,8 V MPU       | -                 | GPIO_12           | Reloj SPI de la MPU (SE0)                                 |
|      42 | HS_DET             | Analógico       | -                 | -                 | Detección de auriculares                                  |
|      43 | SOC_SPI_CS0        | 1,8 V MPU       | -                 | GPIO_13           | Selección de chip SPI de la MPU 0 (SE0)                   |
|      44 | GND                | Alimentación    | -                 | -                 | Masa                                                      |
|      45 | SOC_SPI_CS2        | 1,8 V MPU       | -                 | GPIO_15           | Selección de chip SPI de la MPU 2 (SE0)                   |
|      46 | SOC_MI2S_SCK       | 1,8 V MPU       | -                 | GPIO_120          | Reloj I2S                                                 |
|      47 | SOC_SPI_CS1        | 1,8 V MPU       | -                 | GPIO_14           | Selección de chip SPI de la MPU 1 (SE0)                   |
|      48 | SOC_MI2S_WS        | 1,8 V MPU       | -                 | GPIO_121          | Selección de palabra I2S                                  |
|      49 | SOC_GPIO_73        | 1,8 V MPU       | -                 | GPIO_73           | GPIO del SoC de la MPU                                    |
|      50 | SOC_MI2S_DATA0     | 1,8 V MPU       | -                 | GPIO_122          | Datos I2S 0                                               |
|      51 | SOC_GPIO_74        | 1,8 V MPU       | -                 | GPIO_74           | GPIO del SoC de la MPU                                    |
|      52 | SOC_MI2S_DATA1     | 1,8 V MPU       | -                 | GPIO_123          | Datos I2S 1                                               |
|      53 | +3V3 OUT           | Alimentación    | -                 | -                 | Salida de alimentación de 3,3 V                           |
|      54 | +5V OUT            | Alimentación    | -                 | -                 | Salida de alimentación de 5 V                             |
|      55 | +3V3 OUT           | Alimentación    | -                 | -                 | Salida de alimentación de 3,3 V                           |
|      56 | +5V OUT            | Alimentación    | -                 | -                 | Salida de alimentación de 5 V                             |
|      57 | SOM_VREG_MDPX3_1P8 | Alimentación    | -                 | -                 | Carril de 1,8 V del SOM                                   |
|      58 | GND                | Alimentación    | -                 | -                 | Masa                                                      |
|      59 | SOM_VCOIN / VBAT   | Reserva del RTC | -                 | -                 | Entrada de la batería de reserva del RTC del SOM y la MCU |
|      60 | SIN CONECTAR       | -               | -                 | -                 | -                                                         |

>📝 **Nota:** Los pines de la MCU son de 3,3 V, los pines del SoC de la MPU son de 1,8 V y los pines de audio/micrófono son analógicos. No mezcle dominios de tensión. Las líneas GPIO del SoC en JMISC están dedicadas a la interfaz y no son GPIO de uso general para creadores.

>📝 **Nota:** El pin 59 de JMISC admite una batería de respaldo del RTC de hasta 3,3 V para mantener los relojes en tiempo real del SOM y de la MCU cuando la placa no recibe alimentación. `SOM_VCOIN` (RTC del SOM) y `VBAT` (RTC de la MCU) son dos entradas de batería de respaldo para el RTC que están conectadas físicamente entre sí en este único pin, en lugar de a un raíl de alimentación compartido. Cada una se conecta a través de su propia resistencia de 0 Ω a un nodo común, que está protegido por un diodo TVS bidireccional (Vr = 5,5 V) con referencia a tierra. El consumo de corriente previsto es muy bajo, y este pin no suministra alimentación para mantener el resto de la placa encendida.

### JMEDIA

El conector JMEDIA es un conector de alta densidad de 60 pines que transmite MIPI DSI (pantalla), MIPI CSI0 y CSI1, señales de reloj de la cámara y buses I2C de control de la cámara. Todas las señales se encuentran en el **dominio de 1,8 V de la MPU**. Los pines de alimentación proporcionan una salida de 3,3 V y admiten una entrada de 7-24 V CC.

| **Pin** | **Denominación** | **Dominio**  | **Pin de la MPU** | **Notas**                                            |
| ------: | ---------------- | ------------ | ----------------- | ---------------------------------------------------- |
|       1 | GND              | Alimentación | -                 | Masa                                                 |
|       2 | GND              | Alimentación | -                 | Masa                                                 |
|       3 | MIPI_DSI0_CLK_M  | MIPI D-PHY   | -                 | Reloj DSI −                                          |
|       4 | MIPI_DSI0_L1_P   | MIPI D-PHY   | -                 | Canal DSI 1 +                                        |
|       5 | MIPI_DSI0_CLK_P  | MIPI D-PHY   | -                 | Reloj DSI +                                          |
|       6 | MIPI_DSI0_L1_M   | MIPI D-PHY   | -                 | Canal 1 de DSI −                                     |
|       7 | GND              | Alimentación | -                 | Masa                                                 |
|       8 | GND              | Alimentación | -                 | Masa                                                 |
|       9 | MIPI_DSI0_L2_M   | MIPI D-PHY   | -                 | Canal DSI 2 −                                        |
|      10 | MIPI_DSI0_L0_P   | MIPI D-PHY   | -                 | Canal DSI 0 +                                        |
|      11 | MIPI_DSI0_L2_P   | MIPI D-PHY   | -                 | Canal DSI 2 +                                        |
|      12 | MIPI_DSI0_L0_M   | MIPI D-PHY   | -                 | Canal DSI 0 −                                        |
|      13 | GND              | Alimentación | -                 | Masa                                                 |
|      14 | GND              | Alimentación | -                 | Masa                                                 |
|      15 | MIPI_DSI0_L3_M   | MIPI D-PHY   | -                 | Canal 3 de DSI −                                     |
|      16 | SOC_CAM_MCLK0    | MPU de 1,8 V | GPIO_67           | Reloj maestro de la cámara 0                         |
|      17 | MIPI_DSI0_L3_P   | MIPI D-PHY   | -                 | Canal DSI 3 +                                        |
|      18 | SOC_CAM_MCLK1    | 1,8 V MPU    | GPIO_68           | Reloj maestro de la cámara 1                         |
|      19 | GND              | Alimentación | -                 | Masa                                                 |
|      20 | GND              | Alimentación | -                 | Masa                                                 |
|      21 | CSI0_LN0_M       | MIPI D-PHY   | -                 | Canal de datos CSI0 0 −                              |
|      22 | CCI_I2C2_SDA     | 1,8 V MPU    | GPIO_59           | Control de cámara I2C2 SDA                           |
|      23 | CSI0_LN0_P       | MIPI D-PHY   | -                 | Canal de datos 0 de CSI0 +                           |
|      24 | CCI_I2C2_SCL     | 1,8 V MPU    | GPIO_60           | Control de la cámara I2C2 SCL                        |
|      25 | GND              | Alimentación | -                 | Masa                                                 |
|      26 | GND              | Alimentación | -                 | Masa                                                 |
|      27 | CSI0_LN1_M       | MIPI D-PHY   | -                 | Canal de datos 1 de CSI0 −                           |
|      28 | CSI1_LN3_P       | MIPI D-PHY   | -                 | Carril de datos CSI1 3 +                             |
|      29 | CSI0_LN1_P       | MIPI D-PHY   | -                 | Carril de datos CSI0 1 +                             |
|      30 | CSI1_LN3_M       | MIPI D-PHY   | -                 | Carril de datos 3 de CSI1 −                          |
|      31 | GND              | Alimentación | -                 | Masa                                                 |
|      32 | GND              | Alimentación | -                 | Masa                                                 |
|      33 | CSI0_CLK_M       | MIPI D-PHY   | -                 | Reloj CSI0 −                                         |
|      34 | CSI1_LN2_P       | MIPI D-PHY   | -                 | Canal de datos CSI1 2 +                              |
|      35 | CSI0_CLK_P       | MIPI D-PHY   | -                 | Reloj CSI0 +                                         |
|      36 | CSI1_LN2_M       | MIPI D-PHY   | -                 | Carril de datos CSI1 n.º 2 −                         |
|      37 | GND              | Alimentación | -                 | Masa                                                 |
|      38 | GND              | Alimentación | -                 | Masa                                                 |
|      39 | CSI0_LN2_M       | MIPI D-PHY   | -                 | Carril de datos 2 de CSI0 −                          |
|      40 | CSI1_CLK_P       | MIPI D-PHY   | -                 | Reloj CSI1 +                                         |
|      41 | CSI0_LN2_P       | MIPI D-PHY   | -                 | Canal de datos CSI0 2 +                              |
|      42 | CSI1_CLK_M       | MIPI D-PHY   | -                 | Reloj CSI1 −                                         |
|      43 | GND              | Alimentación | -                 | Masa                                                 |
|      44 | GND              | Alimentación | -                 | Masa                                                 |
|      45 | CSI0_LN3_M       | MIPI D-PHY   | -                 | Canal de datos CSI0 3 −                              |
|      46 | CSI1_LN1_P       | MIPI D-PHY   | -                 | Canal de datos CSI1 1 +                              |
|      47 | CSI0_LN3_P       | MIPI D-PHY   | -                 | Carril de datos 3 de CSI0 +                          |
|      48 | CSI1_LN1_M       | MIPI D-PHY   | -                 | Carril de datos 1 de CSI1 −                          |
|      49 | GND              | Alimentación | -                 | Masa                                                 |
|      50 | GND              | Alimentación | -                 | Masa                                                 |
|      51 | CCI_I2C0_SCL     | 1,8 V MPU    | GPIO_58           | Control de cámara I2C0 SCL                           |
|      52 | CSI1_LN0_P       | MIPI D-PHY   | -                 | Canal de datos 0 de CSI1 +                           |
|      53 | CCI_I2C0_SDA     | 1,8 V MPU    | GPIO_57           | Control de la cámara I2C0 SDA                        |
|      54 | CSI1_LN0_M       | MIPI D-PHY   | -                 | Canal de datos CSI1 0 −                              |
|      55 | GND              | Alimentación | -                 | Masa                                                 |
|      56 | GND              | Alimentación | -                 | Masa                                                 |
|      57 | VIN IN           | Alimentación | -                 | Entrada de 7-24 V CC (1,5 A máx., protegida por PTC) |
|      58 | +3V3 OUT         | Alimentación | -                 | Salida de alimentación de 3,3 V                      |
|      59 | VIN IN           | Alimentación | -                 | Entrada de 7-24 V CC (máx. 1,5 A, protegida por PTC) |
|      60 | Salida +3V3      | Alimentación | -                 | Salida de alimentación de 3,3 V                      |

>📝 **Nota:** Los pines VIN de JMEDIA (pines 57 y 59) pertenecen a la misma red, protegida por un fusible PTC de 1,5 A (F3, MF-MSMF150/24X) y un diodo TVS de 24 V. Pueden suministrar alimentación a una placa carrier, pero no están pensados para alimentar toda la placa VENTUNO Q desde una fuente externa.

>📝 **Nota:** Los pares diferenciales MIPI CSI/DSI son señales D-PHY y no deben utilizarse como E/S de uso general. Todas las señales de control (CCI_I2C, CAM_MCLK) pertenecen al dominio de 1,8 V de la MPU. El VIN de los pines 57 y 59 corresponde únicamente a la tensión de entrada de CC.

### JOMEGA

El conector JOMEGA es un conector de expansión de alta densidad de 100 pines que proporciona señales USB 3.0, CAN-FD, JTAG, GPIO de la MPU, SPI y UART, así como señales de depuración y gestión de alimentación. Los dominios de tensión son mixtos: el USB y algunas señales de control funcionan a 3,3 V, mientras que las señales de depuración JTAG, SPI y UART funcionan a 1,8 V en el dominio de la MPU.

| **Pin** | **Designación**           | **Dominio**  | **Pin de la MCU** | **Pin de la MPU** | **Notas**                                      |
| ------: | ------------------------- | ------------ | ----------------- | ----------------- | ---------------------------------------------- |
|       1 | VIN                       | Alimentación | -                 | -                 | Entrada de 7-24 V CC                           |
|       2 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|       3 | VIN                       | Alimentación | -                 | -                 | Entrada de 7-24 V CC                           |
|       4 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|       5 | VIN                       | Alimentación | -                 | -                 | Entrada de 7-24 V CC                           |
|       6 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|       7 | VIN                       | Alimentación | -                 | -                 | Entrada de 7-24 V CC                           |
|       8 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|       9 | VIN                       | Alimentación | -                 | -                 | Entrada de 7-24 V CC                           |
|      10 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      11 | VIN                       | Alimentación | -                 | -                 | Entrada de 7-24 V CC                           |
|      12 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      13 | VIN                       | Alimentación | -                 | -                 | Entrada de 7-24 V CC                           |
|      14 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      15 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      16 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      17 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      18 | USB3.0_1_SS_TX_P          | USB 3.0      | -                 | -                 | Puerto USB 1 SuperSpeed TX+                    |
|      19 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      20 | USB3.0_1_SS_TX_N          | USB 3.0      | -                 | -                 | Puerto USB 1 SuperSpeed TX−                    |
|      21 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      22 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      23 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      24 | USB3.0_1_HS_D_P           | USB 3.0      | -                 | -                 | Puerto USB 1 HighSpeed D+                      |
|      25 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      26 | USB3.0_1_HS_D_N           | USB 3.0      | -                 | -                 | Puerto USB 1 de alta velocidad D−              |
|      27 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      28 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      29 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      30 | USB3.0_1_SS_RX_P          | USB 3.0      | -                 | -                 | Puerto USB 1 SuperSpeed RX+                    |
|      31 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      32 | USB3.0_1_SS_RX_N          | USB 3.0      | -                 | -                 | Puerto USB 1 SuperSpeed RX−                    |
|      33 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      34 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      35 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      36 | USB3.0_2_SS_TX_P          | USB 3.0      | -                 | -                 | Puerto USB 2 SuperSpeed TX+                    |
|      37 | GND                       | Alimentación | -                 | -                 | Tierra                                         |
|      38 | USB3.0_2_SS_TX_N          | USB 3.0      | -                 | -                 | Puerto USB 2 SuperSpeed TX−                    |
|      39 | IO0_3V3                   | MCU de 3,3 V | PC0               | -                 | GPIO de la MCU                                 |
|      40 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      41 | IO1_3V3                   | 3,3 V MCU    | PC1               | -                 | GPIO de la MCU                                 |
|      42 | USB3.0_2_HS_D_P           | USB 3.0      | -                 | -                 | Puerto USB 2 HighSpeed D+                      |
|      43 | IO2_3V3                   | 3,3 V MCU    | PC2               | -                 | GPIO de la MCU                                 |
|      44 | USB3.0_2_HS_D_N           | USB 3.0      | -                 | -                 | Puerto USB 2 HighSpeed D−                      |
|      45 | IO3_3V3                   | 3,3 V MCU    | PC3               | -                 | GPIO de la MCU                                 |
|      46 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      47 | IO4_3V3                   | 3,3 V MCU    | PD12              | -                 | GPIO de la MCU                                 |
|      48 | USB3.0_2_SS_RX_P          | USB 3.0      | -                 | -                 | Puerto USB 2 SuperSpeed RX+                    |
|      49 | IO5_3V3                   | MCU de 3,3 V | PD13              | -                 | GPIO de la MCU                                 |
|      50 | USB3.0_2_SS_RX_N          | USB 3.0      | -                 | -                 | Puerto USB 2 SuperSpeed RX−                    |
|      51 | IO6_3V3                   | 3,3 V MCU    | PD14              | -                 | GPIO de la MCU                                 |
|      52 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      53 | IO7_3V3                   | 3,3 V MCU    | PD15              | -                 | GPIO de la MCU                                 |
|      54 | USB3.0_1_PWRON_3V3        | 3,3 V        | -                 | -                 | Activación de alimentación del puerto USB 1    |
|      55 | IO8_3V3                   | 3,3 V MCU    | PI2               | -                 | GPIO de la MCU                                 |
|      56 | USB3.0_1_OVERCUR_3V3      | 3,3 V        | -                 | -                 | Indicador de sobrecorriente del puerto USB 1   |
|      57 | MIC_INP                   | Analógico    | -                 | -                 | Entrada de micrófono+                          |
|      58 | USB3.0_2_PWRON_3V3        | 3,3 V        | -                 | -                 | Activación de alimentación del puerto USB 2    |
|      59 | MIC_INN                   | Analógico    | -                 | -                 | Entrada de micrófono−                          |
|      60 | USB3.0_2_OVERCUR_3V3      | 3,3 V        | -                 | -                 | Indicador de sobrecorriente del puerto USB 2   |
|      61 | MIC_BIAS                  | Analógico    | -                 | -                 | Polarización del micrófono                     |
|      62 | SPI_ICS_MISO              | 1,8 V MPU    | -                 | GPIO_39           | MPU SPI MISO (SPI_ICS_1V8)                     |
|      63 | TMS                       | 1,8 V MPU    | -                 | -                 | TMS JTAG (JTAG_1V8)                            |
|      64 | SPI_ICS_MOSI              | 1,8 V MPU    | -                 | GPIO_40           | MPU SPI MOSI                                   |
|      65 | TDO                       | 1,8 V MPU    | -                 | -                 | JTAG TDO                                       |
|      66 | SPI_ICS_SCK               | 1,8 V MPU    | -                 | GPIO_37           | Reloj SPI de la MPU                            |
|      67 | TDI                       | 1,8 V MPU    | -                 | -                 | TDI de JTAG                                    |
|      68 | SPI_ICS_CS                | 1,8 V MPU    | -                 | GPIO_38           | Selección de chip SPI de la MPU                |
|      69 | TCK                       | 1,8 V MPU    | -                 | -                 | Reloj JTAG                                     |
|      70 | PM_PS_HOLD_1V8            | 1,8 V MPU    | -                 | -                 | Retención del estado de alimentación de la MPU |
|      71 | SRST_N                    | 1,8 V MPU    | -                 | -                 | Reset del sistema JTAG                         |
|      72 | FORCED_USB_BOOT_1V8       | 1,8 V MPU    | -                 | GPIO_52           | Forzar el modo de arranque USB                 |
|      73 | TRST_N                    | 1,8 V MPU    | -                 | -                 | Reset TAP de JTAG                              |
|      74 | PWR_EN_N                  | 1,8 V MPU    | -                 | -                 | Activación de alimentación (activo bajo)       |
|      75 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      76 | USER_BUTTON               | 3,3 V        | -                 | GPIO_79           | Entrada del botón de usuario                   |
|      77 | SOM_VREG_S5S_SPX3_1P8     | Alimentación | -                 | -                 | Carril RTSS de 1,8 V del SOM                   |
|      78 | PM_RESIN_N_3V3            | 3,3 V        | -                 | -                 | Entrada de reset del PMIC de la MPU            |
|      79 | SOM_VREG_MDPX3_1P8        | Alimentación | -                 | -                 | Carril de 1,8 V del SOM                        |
|      80 | RTSS_RESIN_N_1V8          | 1,8 V MPU    | -                 | -                 | Entrada de reset RTSS                          |
|      81 | SOM_VREG_MDPX3_1P8        | Alimentación | -                 | -                 | Carril de 1,8 V del SOM                        |
|      82 | RTSS_PS_HOLD_SPX3_1P8_1V8 | MPU de 1,8 V | -                 | -                 | Retención del estado de alimentación RTSS      |
|      83 | UART_DBG_TX               | 1,8 V MPU    | -                 | GPIO_71           | Transmisión UART de depuración de la MPU       |
|      84 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      85 | UART_DBG_RX               | 1,8 V MPU    | -                 | GPIO_72           | UART de depuración de la MPU (recepción)       |
|      86 | CAN1_TX                   | 3,3 V MCU    | PD5               | -                 | Transmisión del bus CAN-FD 1 (sin PHY)         |
|      87 | PWR_DISABLE_7-24V         | Sistema      | -                 | -                 | Desactiva la ruta de alimentación VIN          |
|      88 | CAN1_RX                   | 3,3 V MCU    | PI9               | -                 | Recepción del bus CAN-FD 1 (sin PHY)           |
|      89 | FORCE_BOOT_3V3            | 3,3 V        | -                 | -                 | Anulación forzada del arranque                 |
|      90 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      91 | +3V3 OUT                  | Alimentación | -                 | -                 | Salida de alimentación de 3,3 V                |
|      92 | CAN2_TX                   | MCU de 3,3 V | PA10              | -                 | Transmisión del bus CAN-FD 2 (sin PHY)         |
|      93 | +3V3 OUT                  | Alimentación | -                 | -                 | Salida de alimentación de 3,3 V                |
|      94 | CAN2_RX                   | 3,3 V MCU    | PD9               | -                 | Recepción del bus CAN-FD 2 (sin PHY)           |
|      95 | +3V3 OUT                  | Alimentación | -                 | -                 | Salida de alimentación de 3,3 V                |
|      96 | GND                       | Alimentación | -                 | -                 | Masa                                           |
|      97 | +5V OUT                   | Alimentación | -                 | -                 | Salida de alimentación de 5 V                  |
|      98 | CAN3_TX                   | MCU de 3,3 V | PF6               | -                 | Bus CAN-FD 3 TX (sin PHY)                      |
|      99 | +5 V OUT                  | Alimentación | -                 | -                 | Salida de alimentación de 5 V                  |
|     100 | CAN3_RX                   | 3,3 V MCU    | PF7               | -                 | Bus CAN-FD 3 RX (sin PHY)                      |

>📝 **Nota:** Las señales JTAG y SPI ICS pertenecen al dominio de 1,8 V de la MPU. No aplique directamente la lógica de 3,3 V. JOMEGA tiene buses CAN FD sin capa física PHY, por lo que se requiere un transceptor CAN externo. Los pines VIN son únicamente de entrada de alimentación.

### Conectores de cámara MIPI CSI (J3_1, J3_2, J3_3)

VENTUNO Q ofrece tres conectores independientes para cámaras MIPI CSI (J3_1, J3_2, J3_3), cada uno de ellos un conector FPC de 22 pines (TF31-22S-0,5SH, paso de 0,5 mm). Cada uno de ellos es compatible con cámaras MIPI CSI-2 de 4 carriles. Las señales de control (I2C, GPIO) funcionan a **3,3 V**, tanto para el GPIO de habilitación del pin 17 como para los buses I2C de los pines 20-21. Las señales I2C se convierten internamente a un nivel de 1,8 V antes de llegar al bus `CCI_I2C` del SoM. Los pares diferenciales MIPI son D-PHY y no deben utilizarse como GPIO.

#### J3_1 - Cámara 2

| **Pin** | **Designación** | **Dominio**  | **Pin de la MPU** | **Notas**                                                          |
| ------: | --------------- | ------------ | ----------------- | ------------------------------------------------------------------ |
|       1 | GND             | Alimentación | -                 | Masa                                                               |
|       2 | LN0_M           | MIPI D-PHY   | -                 | Canal de datos CSI2 0 −                                            |
|       3 | LN0_P           | MIPI D-PHY   | -                 | Canal de datos CSI2 0 +                                            |
|       4 | GND             | Alimentación | -                 | Tierra                                                             |
|       5 | LN1_M           | MIPI D-PHY   | -                 | Canal de datos CSI2 1 −                                            |
|       6 | LN1_P           | MIPI D-PHY   | -                 | Canal de datos CSI2 1 +                                            |
|       7 | GND             | Alimentación | -                 | Masa                                                               |
|       8 | CLK_M           | MIPI D-PHY   | -                 | Canal de reloj CSI2 −                                              |
|       9 | CLK_P           | MIPI D-PHY   | -                 | Canal de reloj CSI2 +                                              |
|      10 | GND             | Alimentación | -                 | Tierra                                                             |
|      11 | LN2_M           | MIPI D-PHY   | -                 | Canal de datos CSI2 2 −                                            |
|      12 | LN2_P           | MIPI D-PHY   | -                 | Canal de datos CSI2 2 +                                            |
|      13 | GND             | Alimentación | -                 | Tierra                                                             |
|      14 | LN3_M           | MIPI D-PHY   | -                 | Canal de datos CSI2 3 −                                            |
|      15 | LN3_P           | MIPI D-PHY   | -                 | Canal de datos CSI2 3 +                                            |
|      16 | GND             | Alimentación | -                 | Tierra                                                             |
|      17 | GPIO_PIN17_3V3  | 3,3 V        | GPIO_82           | GPIO de la cámara                                                  |
|      18 | SIN CONECTAR    | -            | -                 | -                                                                  |
|      19 | GND             | Alimentación | -                 | Masa                                                               |
|      20 | SCL             | 3,3 V        | GPIO_62           | Reloj I2C de la cámara (CCI_I2C4, con conversión de nivel a 1,8 V) |
|      21 | SDA             | 3,3 V        | GPIO_61           | Datos I2C de la cámara (CCI_I2C4, con conversión de nivel a 1,8 V) |
|      22 | +3V3            | Alimentación | -                 | Suministro de 3,3 V para el módulo de la cámara                    |

#### J3_2 - Cámara 0

| **Pin** | **Denominación** | **Dominio**  | **Pin de la MPU** | **Notas**                                                          |
| ------: | ---------------- | ------------ | ----------------- | ------------------------------------------------------------------ |
|       1 | GND              | Alimentación | -                 | Masa                                                               |
|       2 | LN0_M            | MIPI D-PHY   | -                 | Canal de datos CSI0 0 −                                            |
|       3 | LN0_P            | MIPI D-PHY   | -                 | Canal de datos CSI0 0 +                                            |
|       4 | GND              | Alimentación | -                 | Tierra                                                             |
|       5 | LN1_M            | MIPI D-PHY   | -                 | Canal de datos CSI0 1 −                                            |
|       6 | LN1_P            | MIPI D-PHY   | -                 | Canal de datos CSI0 1 +                                            |
|       7 | GND              | Alimentación | -                 | Masa                                                               |
|       8 | CLK_M            | MIPI D-PHY   | -                 | Canal de reloj CSI0 −                                              |
|       9 | CLK_P            | MIPI D-PHY   | -                 | Canal de reloj CSI0 +                                              |
|      10 | GND              | Alimentación | -                 | Tierra                                                             |
|      11 | LN2_M            | MIPI D-PHY   | -                 | Canal de datos CSI0 2 −                                            |
|      12 | LN2_P            | MIPI D-PHY   | -                 | Canal de datos CSI0 2 +                                            |
|      13 | GND              | Alimentación | -                 | Tierra                                                             |
|      14 | LN3_M            | MIPI D-PHY   | -                 | Canal de datos CSI0 3 −                                            |
|      15 | LN3_P            | MIPI D-PHY   | -                 | Canal de datos CSI0 3 +                                            |
|      16 | GND              | Alimentación | -                 | Masa                                                               |
|      17 | GPIO_PIN17_3V3   | 3,3 V        | GPIO_64           | GPIO de la cámara                                                  |
|      18 | SIN CONECTAR     | -            | -                 | -                                                                  |
|      19 | GND              | Alimentación | -                 | Masa                                                               |
|      20 | SCL              | 3,3 V        | GPIO_58           | Reloj I2C de la cámara (CCI_I2C0, con conversión de nivel a 1,8 V) |
|      21 | SDA              | 3,3 V        | GPIO_57           | Datos I2C de la cámara (CCI_I2C0, con conversión de nivel a 1,8 V) |
|      22 | +3V3             | Alimentación | -                 | Suministro de 3,3 V para el módulo de la cámara                    |

#### J3_3 - Cámara 1

| **Pin** | **Denominación** | **Dominio**  | **Pin de la MPU** | **Notas**                                                          |
| ------: | ---------------- | ------------ | ----------------- | ------------------------------------------------------------------ |
|       1 | GND              | Alimentación | -                 | Masa                                                               |
|       2 | LN0_M            | MIPI D-PHY   | -                 | Canal de datos CSI1 0 −                                            |
|       3 | LN0_P            | MIPI D-PHY   | -                 | Canal de datos CSI1 0 +                                            |
|       4 | GND              | Alimentación | -                 | Tierra                                                             |
|       5 | LN1_M            | MIPI D-PHY   | -                 | Canal de datos CSI1 1 −                                            |
|       6 | LN1_P            | MIPI D-PHY   | -                 | Canal de datos CSI1 1 +                                            |
|       7 | GND              | Alimentación | -                 | Masa                                                               |
|       8 | CLK_M            | MIPI D-PHY   | -                 | Canal de reloj CSI1 −                                              |
|       9 | CLK_P            | MIPI D-PHY   | -                 | Canal de reloj CSI1 +                                              |
|      10 | GND              | Alimentación | -                 | Tierra                                                             |
|      11 | LN2_M            | MIPI D-PHY   | -                 | Canal de datos CSI1 2 −                                            |
|      12 | LN2_P            | MIPI D-PHY   | -                 | Canal de datos CSI1 2 +                                            |
|      13 | GND              | Alimentación | -                 | Tierra                                                             |
|      14 | LN3_M            | MIPI D-PHY   | -                 | Canal de datos CSI1 3 −                                            |
|      15 | LN3_P            | MIPI D-PHY   | -                 | Canal de datos CSI1 3 +                                            |
|      16 | GND              | Alimentación | -                 | Tierra                                                             |
|      17 | GPIO_PIN17_3V3   | 3,3 V        | GPIO_75           | GPIO de la cámara                                                  |
|      18 | SIN CONECTAR     | -            | -                 | -                                                                  |
|      19 | GND              | Alimentación | -                 | Masa                                                               |
|      20 | SCL              | 3,3 V        | GPIO_60           | Reloj I2C de la cámara (CCI_I2C2, con conversión de nivel a 1,8 V) |
|      21 | SDA              | 3,3 V        | GPIO_59           | Datos I2C de la cámara (CCI_I2C2, con conversión de nivel a 1,8 V) |
|      22 | +3V3             | Alimentación | -                 | Suministro de 3,3 V para el módulo de la cámara                    |

>📝 **Nota:** Los carriles diferenciales MIPI D-PHY no son E/S de uso general.

## Periféricos de alta velocidad

### Redes

Wi-Fi® 6 tribanda (2,4/5/6 GHz) y Bluetooth® 5.3 a través del módulo integrado NFA725B. Conectividad por cable mediante Ethernet RJ45 de 2,5 Gbps (PHY QCA-8081).

### Almacenamiento

Almacenamiento NVMe Gen 4 ampliable a través del conector M.2 2230 Key M (MDT580M01001), conectado directamente al SOM QCS8275 mediante una interfaz PCIe Gen 4 de 4 carriles. La ranura M.2 no es arrancable, según la especificación del QCS8275. La alimentación de la ranura se activa de forma independiente mediante un interruptor de carga MP5077GG-Z controlado por la MPU.

El conmutador de paquetes PCIe Gen 2 PI7C9X2G304EV de la placa está dedicado al controlador host USB 3.0 xHCI (TUSB7340RKMR) y al módulo Wi-Fi® (NFA725B).

> 📝 **Nota:** La MPU controla la alimentación de la ranura M.2. Si la MPU no tiene completado el arranque o no se ha habilitado el control de alimentación, una unidad NVMe instalada no recibirá alimentación y no se enumerará. Se trata de un comportamiento esperado durante las primeras fases del arranque.

### USB-C

El conector USB-C admite el cambio de rol entre host y dispositivo, el cambio de rol de alimentación, la salida en modo alternativo (Alt-Mode) de DisplayPort y la negociación de USB Power Delivery de hasta 20 V a través del controlador PD CYPD6129-52LQXI. Los pares diferenciales SuperSpeed del conector USB-C se comparten entre los datos SuperSpeed de USB 3.0 y el modo alternativo de DisplayPort a través del multiplexor USB eDP integrado (TMUXHS4446RETT).

**Cuando el modo alternativo de DisplayPort está activo**, los carriles SuperSpeed se reasignan a DisplayPort. Los datos USB quedan entonces limitados a las velocidades de USB 2.0 (HighSpeed, 480 Mbps) únicamente en el par HS_D+/D−. La velocidad completa de datos USB 3.0 SuperSpeed solo está disponible cuando el modo alternativo de DisplayPort no está activo.

El CYPD6129 supervisa tanto el VBUS como el VIN para determinar el estado de alimentación de la placa y negocia los perfiles PD en consecuencia. El LED de fallo (rojo, GPIO9/P4.1 en el CYPD6129) indica condiciones de fallo. A continuación se resumen los principales escenarios de alimentación:

| **Escenario**                                                                        | **Resultado esperado**                                                                  |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| VIN conectado, USB no conectado                                                      | Sistema alimentado por VIN, controlador PD en modo batería                              |
| VIN conectado, USB conectado                                                         | Sistema alimentado por VIN, se permite la negociación PD y el intercambio de datos      |
| VIN no conectado, USB-C a USB-C                                                      | Sistema alimentado por VBUS, se inicia la negociación PD, objetivo: 20 V a 3 A          |
| VIN no conectado, USB-C a USB-A                                                      | PD detecta una fuente no PD, sistema apagado, LED de fallo parpadeando                  |
| VIN no conectado, USB-C a USB-A -> VIN conectado sobre la marcha                     | PD reconoce VIN, desbloquea VIN, mantiene VBUS bloqueado                                |
| VIN no conectado, USB-C a USB-C (potencia negociada) → VIN conectado sobre la marcha | Sistema alimentado por VBUS, VIN bloqueado, el LED de fallo muestra un patrón diferente |

>📝 **Nota:** El CYPD6129 está programado para requerir un perfil de tensión PD superior a 5 V antes de habilitar la ruta de alimentación principal. La conexión mediante un cable estándar de USB-C a USB-A, o a un puerto USB-C que solo suministre 5 V sin negociación PD, no alimentará la placa y provocará que el LED de fallo parpadee. Utilice siempre una fuente de alimentación USB-C compatible con PD que admita 9 V, 15 V o 20 V para garantizar un funcionamiento fiable con alimentación USB-C.
>
> El CYPD6129 permanece siempre alimentado a través de un convertidor reductor dedicado (LMR51440SDRRR, U26) alimentado desde cualquier fuente de alimentación conectada, lo que le permite supervisar y negociar la alimentación de forma independiente antes de habilitar la ruta de alimentación de la placa.

### USB tipo A

Ambos puertos USB 3.0 tipo A están protegidos de forma independiente mediante interruptores de carga dedicados (MP5077GG-Z). El VBUS de cada puerto está limitado de forma fija a 1,71 A mediante la red de resistencias ILIM. La activación de la alimentación de cada puerto se gestiona mediante el TUSB7340RKMR.

| **Parámetro**               | **Valor**                                 |
| --------------------------- | ----------------------------------------- |
| Tensión VBUS                | 5 V                                       |
| Corriente máxima por puerto | 1,71 A (establecida por ILIM, por puerto) |
| Protección                  | Interruptor de carga MP5077GG-Z           |
| Control de habilitación     | TUSB7340RKMR                              |

>📝 **Nota:** El límite de corriente de 1,71 A por puerto está configurado en el hardware y no puede anularse mediante software. No intente eludir el interruptor de carga.

### Display

La placa ofrece las siguientes salidas de pantalla:

- **HDMI** a través del conector HDMI dedicado, controlado por el DSI bridge a HDMI ADV7535 integrado. El ADV7535 utiliza las líneas MIPI DSI del SoM. Cuando el HDMI está activo, las líneas MIPI-DSI del conector JMEDIA no están disponibles.
- **DisplayPort Alt Mode** a través del conector USB-C mediante el multiplexor USB eDP integrado (TMUXHS4446RETT).
- **MIPI DSI en JMEDIA** disponible cuando la salida HDMI no está activa (requiere configuración de superposición DSI).

### Cámara

VENTUNO Q admite la entrada de cámara a través de tres conectores MIPI CSI integrados (J3_1, J3_2, J3_3) y a través del conector Carrier de JMEDIA.

**VENTUNO Q autónomo (por defecto):**

Los tres conectores CSI integrados (J3_1, J3_2, J3_3) están disponibles simultáneamente para la entrada de la cámara. Se trata de una configuración exclusiva para la cámara y MIPI DSI no está activo de forma predeterminada. La salida de pantalla está disponible a través del conector HDMI o USB-C DisplayPort Alt Mode.

>📝 **Nota:** El [módulo de cámara Arducam IMX577 Mini](https://www.arducam.com/arducam-imx577-mini-camera-module-for-qualcomm-rb3g2.html) (SKU B0488) es compatible con VENTUNO Q a través de sus conectores MIPI CSI integrados. Consulte el [Manual de usuario de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) para obtener instrucciones de prueba y configuración.

**VENTUNO Q con una placa carrier compatible:**

Una placa carrier conectada a JMEDIA permite utilizar una pantalla MIPI DSI junto con las cámaras integradas. Si se habilita la superposición DSI de la placa carrier, la cámara 0 (J3_2) no estará disponible, ya que comparte el bus CCI_I2C0 (GPIO_57/58) con el conector JMEDIA. Las cámaras 1 (J3_3) y 2 (J3_1) siguen estando disponibles.

>📝 **Nota:** La disponibilidad de las cámaras cuando se conecta una placa carrier depende de la configuración específica de dicha placa. Consulte la documentación de la propia placa carrier para obtener más detalles.

<div style="page-break-after: always;"></div>

## Funcionamiento del dispositivo

### Primeros pasos: Arduino App Lab

Arduino App Lab [1] es un editor unificado que permite crear y ejecutar proyectos en ambos procesadores de VENTUNO Q. Combina la programación integrada (sketch), el desarrollo en Linux y la IA periférica en un único entorno.

Un proyecto es una **aplicación** que puede incluir:

- Un programa en Python® que se ejecuta en el sistema Linux (Qualcomm Dragonwing™ IQ8)
- Un sketch de Arduino que se ejecuta en el microcontrolador (STM32H5F5)
- **Bricks** opcionales (servicios preconfigurados, como modelos de IA, servidores web o clientes de API) que se implementan junto con la aplicación y se ejecutan en el sistema Linux.

Las aplicaciones utilizan **Bridge** para intercambiar datos entre el lado de Linux y el microcontrolador.

**Tres configuraciones. Una sola experiencia.**

![](assets/ABX00181_modes.png)

- **Modo de ordenador de placa única:** App Lab se ejecuta directamente en VENTUNO Q. Conecte un monitor a través de HDMI (o USB-C), un teclado y un ratón para disponer de un entorno de desarrollo «todo en uno». No se necesita un ordenador.
- **Modo de PC Hoste**: Conecte VENTUNO Q a su ordenador mediante USB-C o red y ejecute App Lab en su PC.
- **Modo en red:** VENTUNO Q funciona sin interfaz gráfica, es decir, sin pantalla, teclado ni ratón. Acceda a la placa de forma remota a través de Wi-Fi® o Ethernet.

>📝 **Nota:** En el modo **alojado en PC**, se requiere una conexión de datos USB para la configuración inicial. Posteriormente, puede utilizar el destino **Red** a través de LAN (SSH).

En el modo **ordenador de placa única**, no se necesita ningún enlace de datos USB; encienda la placa y utilice el destino **Red** una vez que se haya conectado a su red. Los periféricos USB (teclado, ratón, cámara USB, micrófono) pueden conectarse directamente a los puertos USB-A integrados. Cuando el modo alternativo DisplayPort está activo en el puerto USB-C, la velocidad de datos USB se reduce.

Para obtener instrucciones completas de instalación, configuración inicial y orientación para el primer uso, consulte el [Manual de usuario de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Nota:** Si se alimenta a través de USB-C por primera vez, es posible que el LED de fallo parpadee al conectarse a un ordenador o a un puerto USB-C no compatible con PD. La placa requiere una fuente de alimentación compatible con PD de al menos 9 V para arrancar. Para un funcionamiento a pleno rendimiento, incluyendo la inferencia de IA, los periféricos conectados y los HAT acoplados, se recomienda una fuente de alimentación de 12 V o superior a través de USB-C PD (hasta 20 V) o del conector cilíndrico o los terminales de tornillo (7-24 V). Consulte la sección [Alimentación de entrada](#alimentación-de-entrada) para conocer los límites de tensión y corriente por fuente.

>📝 **Nota:** El primer arranque tarda entre 20 y 30 segundos mientras se inicia Linux. La matriz de LED muestra una animación de arranque cuando se carga el gestor de arranque de la MCU y se está ejecutando un sketch válido. Espere a que finalice antes de interactuar con la placa. Si la animación no aparece, consulte el [Manual de usuario de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) para obtener más detalles.

### Bricks

Los «Bricks» son bloques de construcción preconfigurados de Arduino App Lab, que incluyen modelos de IA, servicios web, integraciones de sensores, bases de datos e interfaces de usuario, y que se implementan junto con su aplicación en el entorno Linux sin que sea necesario que usted desarrolle la infraestructura subyacente. Para obtener una guía completa sobre cómo seleccionar y utilizar los «Bricks», consulte el [Manual de usuario de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Nota:** Mientras una aplicación está vinculada y en ejecución, es posible que el sistema ocupe las interfaces USB. Para utilizar herramientas de línea de comandos externas a través de USB, detenga la aplicación o desconecte la placa.

### Botones y modos de arranque

VENTUNO Q incluye dos botones integrados: un **pulsador vertical** y un **botón de usuario**.

![](assets/ABX00181_vertical_button.png)

### Pulsador vertical

El pulsador vertical está conectado al GPIO PK13 de la MCU. Se puede utilizar para interactuar con la placa y apagarla.

- **Pulsación única (modo de ordenador de placa única):** activa un cuadro de diálogo de apagado en pantalla. El usuario puede confirmar para apagar inmediatamente o cancelar para descartarlo y continuar con el funcionamiento normal. Si no se realiza ninguna acción, la placa se apaga automáticamente tras 60 segundos.
- **Pulsación prolongada (más de 10 segundos, modo SSH/ADB):** Apaga el sistema por completo. La placa permanecerá apagada hasta que se desconecte y se vuelva a conectar la alimentación.

>📝 **Nota:** Un apagado mediante pulsación prolongada detiene por completo el entorno Linux e interrumpirá cualquier aplicación en ejecución. Guarde su trabajo y asegúrese de que los procesos externos se detengan de forma segura cuando sea necesario. La placa se inicia automáticamente cuando se le suministra alimentación, y no es necesario pulsar el botón para un arranque normal.

### Botón de usuario

![](assets/ABX00181_user_button.png)

El botón de usuario está conectado a la MPU (GPIO_79) y está disponible como entrada de uso general. Se puede leer desde aplicaciones y scripts de Linux utilizando interfaces GPIO estándar. Para ver ejemplos de uso, consulte el [Manual de usuario de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

<div style="page-break-after: always;"></div>

## Información mecánica

La placa mide 160 mm × 100 mm. La altura total, sin contar el disipador térmico ni el ventilador del SoM, es de 25,8 mm. El conector JHAT de 40 pines cumple con la especificación mecánica estándar de los HAT de Raspberry Pi®, lo que permite la compatibilidad física con los accesorios HAT compatibles.

![](assets/ABX00181_general_dimensions.svg)

Los conectores del UNO Shield mantienen el espaciado estándar de la placa Arduino UNO, lo que permite una compatibilidad mecánica y eléctrica directa con el ecosistema del UNO Shield.

La placa cuenta con tres conjuntos de orificios que cumplen diferentes funciones mecánicas:

- **4 separadores M2,5** (5 mm de altura, soldados a la placa) para el montaje del disipador térmico, situados a 9,78 mm del borde derecho y a 10,02 mm y 42,63 mm del borde superior.
- **4 orificios de montaje en las esquinas de 3,2 mm** para la instalación en cajas, paneles o placas Carrier y accesorios personalizados.
- **2× 3,2 mm** orificios de montaje HAT que cumplen con la especificación mecánica estándar de Raspberry Pi® HAT, compatibles con separadores M3 para fijar accesorios HAT.
- **1× separador M2** (4 mm de altura) para fijar una tarjeta de almacenamiento M.2 2230 NVMe en la ranura M.2.

VENTUNO Q se suministra con 4 separadores hexagonales M3 y 4 tuercas M3, incluidos en una bolsa aparte. En entornos sensibles a descargas electrostáticas (ESD), fije un separador y una tuerca a cada uno de los cuatro orificios de montaje de las esquinas para elevar la placa de la superficie de trabajo y aumentar el espacio libre.

| **Artículo**           | **Dimensiones**                                                              |
| ---------------------- | ---------------------------------------------------------------------------- |
| Separador hexagonal M3 | Longitud hexagonal 20 mm, longitud de rosca 6 mm, diámetro de rosca 3 mm     |
| Tuerca M3              | Altura 2,4 mm, ancho entre caras del hexágono 5,6 mm, diámetro interior 3 mm |

![](assets/ABX00181_esd_standoff.png)

### Disipador térmico y diseño térmico del SoM

El módulo SoM Qualcomm® Dragonwing™ IQ8 (QCS8275) requiere refrigeración activa para un funcionamiento sostenido a pleno rendimiento. La huella del SoM en la placa mide **57,5 mm × 57,5 mm**, centrada a **14,26 mm** del borde izquierdo y a **14,73 mm** del borde inferior, con un desplazamiento horizontal de **8,95 mm** y un desplazamiento vertical de **8,55 mm** respecto al área activa del SoM.

![](assets/ABX00181_active_fan.png)

Los cuatro separadores M2,5 definen el patrón de montaje del conjunto de disipador térmico y ventilador incluido, situado simétricamente alrededor de la huella del SoM para proporcionar una fuerza de sujeción uniforme en toda la tapa del SoM.

En las peores condiciones, con la MPU, la NPU y la GPU funcionando simultáneamente a pleno rendimiento, la placa puede consumir aproximadamente 25 W o más. La solución de refrigeración activa incluida está optimizada para esta carga térmica. Asegúrese de que el ventilador permanezca en funcionamiento durante cargas de trabajo sostenidas de alto rendimiento.

![](assets/ABX00181_som_heatsink.svg)

>📝 **Nota:** El funcionamiento de la placa bajo cargas de trabajo intensivas de IA o de cálculo sin una refrigeración adecuada puede provocar una limitación térmica del SoM QCS8275, lo que reducirá el rendimiento. Compruebe siempre el margen térmico para su caso de uso específico y el entorno de la carcasa.

<div style="page-break-after: always;"></div>

# Safety Information

Maintain a minimum separation distance of 20 cm between the device and the user during operation. The 5 GHz frequency band may be subject to operational restrictions depending on the country of use.

**Bulgarian (BG):**

Поддържайте минимално разстояние от 20 см между устройството и потребителя по време на работа. Честотната лента 5 GHz може да бъде обект на ограничения за използване в зависимост от държавата.

**Croatian (HR):**

Održavajte minimalnu udaljenost od 20 cm između uređaja i korisnika tijekom rada. Frekvencijski pojas od 5 GHz može podlijegati ograničenjima ovisno o zemlji uporabe.

**Czech (CS):**

Udržujte minimální vzdálenost 20 cm mezi zařízením a uživatelem během provozu. Pásmo 5 GHz může podléhat provozním omezením v závislosti na zemi použití.

**Danish (DA):**

Oprethold en minimumsafstand på 20 cm mellem enheden og brugeren under drift. 5 GHz-båndet kan være underlagt driftsmæssige begrænsninger afhængigt af brugslandet.

**Dutch (NL):**

Houd tijdens gebruik een minimale afstand van 20 cm tussen het apparaat en de gebruiker aan. De 5GHz-band kan onderhevig zijn aan gebruiksbeperkingen afhankelijk van het land van gebruik.

**Estonian (ET):**

Hoidke seadme ja kasutaja vahel töötamise ajal vähemalt 20 cm kaugust. 5 GHz sagedusribale võivad kehtida kasutuspiirangud sõltuvalt kasutusriigist.

**Finnish (FI):**

Pidä laitteen ja käyttäjän välillä vähintään 20 cm etäisyys käytön aikana. 5 GHz taajuuskaistaan voi kohdistua käyttörajoituksia käyttömaasta riippuen.

**French (FR):**

Maintenez une distance minimale de 20 cm entre l’appareil et l’utilisateur pendant son fonctionnement. La bande de fréquences 5 GHz peut être soumise à des restrictions d’utilisation selon le pays.

**German (DE):**

Halten Sie während des Betriebs einen Mindestabstand von 20 cm zwischen dem Gerät und dem Benutzer ein. Das 5‑GHz‑Frequenzband kann je nach Einsatzland Nutzungsbeschränkungen unterliegen.

**Greek (EL):**

Διατηρείτε ελάχιστη απόσταση 20 cm μεταξύ της συσκευής και του χρήστη κατά τη λειτουργία. Η ζώνη συχνοτήτων 5 GHz ενδέχεται να υπόκειται σε περιορισμούς ανάλογα με τη χώρα χρήσης.

**Hungarian (HU):**

A működés során tartson legalább 20 cm távolságot az eszköz és a felhasználó között. Az 5 GHz-es frekvenciasáv használata országtól függően korlátozott lehet.

**Irish (GA):**

Coinnigh ar a laghad fad 20 cm idir an gléas agus an t‑úsáideoir le linn úsáide. D’fhéadfadh srianta oibriúcháin a bheith ar an mbanda minicíochta 5 GHz ag brath ar an tír.

**Italian (IT):**

Mantenere una distanza minima di 20 cm tra il dispositivo e l’utente durante il funzionamento. La banda di frequenza a 5 GHz può essere soggetta a restrizioni operative a seconda del paese.

**Latvian (LV):**

Uzturiet vismaz 20 cm attālumu starp ierīci un lietotāju darbības laikā. 5 GHz frekvenču joslai var būt izmantošanas ierobežojumi atkarībā no valsts.

**Lithuanian (LT):**

Naudojimo metu laikykite bent 20 cm atstumą tarp įrenginio ir naudotojo. 5 GHz dažnių juostai gali būti taikomi naudojimo apribojimai priklausomai nuo šalies.

**Maltese (MT):**

Żomm distanza minima ta’ 20 cm bejn l-apparat u l-utent waqt l-użu. Il-medda tal-frekwenza 5 GHz tista’ tkun soġġetta għal restrizzjonijiet skont il-pajjiż.

**Polish (PL):**

Podczas pracy zachowaj minimalną odległość 20 cm między urządzeniem a użytkownikiem. Pasmo częstotliwości 5 GHz może podlegać ograniczeniom w zależności od kraju użytkowania.

**Portuguese (PT):**

Mantenha uma distância mínima de 20 cm entre o dispositivo e o utilizador durante o funcionamento. A banda de frequência de 5 GHz pode estar sujeita a restrições de utilização dependendo do país.

**Romanian (RO):**

Mențineți o distanță minimă de 20 cm între dispozitiv și utilizator în timpul funcționării. Banda de frecvență de 5 GHz poate face obiectul unor restricții în funcție de țara de utilizare.

**Slovak (SK):**

Počas prevádzky dodržiavajte minimálnu vzdialenosť 20 cm medzi zariadením a používateľom. Pásmo 5 GHz môže podliehať prevádzkovým obmedzeniam v závislosti od krajiny použitia.

**Slovenian (SL):**

Med delovanjem ohranjajte najmanj 20 cm razdalje med napravo in uporabnikom. Pas frekvenc 5 GHz je lahko omejen glede na državo uporabe.

**Spanish (ES):**

Mantenga una distancia mínima de 20 cm entre el dispositivo y el usuario durante su funcionamiento. La banda de frecuencia de 5 GHz puede estar sujeta a restricciones según el país de uso.

**Swedish (SV):**

Håll ett minsta avstånd på 20 cm mellan enheten och användaren under drift. 5 GHz-bandet kan vara föremål för driftbegränsningar beroende på användningsland.

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

| **Radio Technology**      | **Frequency Band** | **Maximum Transmit Power** |
| ------------------------- | ------------------ | -------------------------- |
| Bluetooth® EDR            | 2400 - 2483.5 MHz  | 18.31 dBm                  |
| Bluetooth® LE             | 2400 - 2483.5 MHz  | 9.97 dBm                   |
| Wi-Fi® 2.4 GHz            | 2400 - 2483.5 MHz  | 19.91 dBm EIRP             |
| Wi-Fi® 5 GHz              | 5150 - 5350 MHz    | 22.92 dBm EIRP             |
| Wi-Fi® 5 GHz              | 5470 - 5725 MHz    | 22.97 dBm EIRP             |
| Wi-Fi® 5 GHz              | 5725 - 5850 MHz    | 13.84 dBm EIRP             |
| Wi-Fi® 6 GHz (LPI client) | 5945 - 6425 MHz    | 22.83 dBm EIRP             |
| Wi-Fi® 6 GHz (VLP)        | 5945 - 6425 MHz    | 13.77 dBm EIRP             |

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

This device complies with Canadian RSS-247. This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.

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

**Note:** For 5GHz and/or when co-located with 5 GHz transmitters, the following statements should be provided in the user information.

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

```
高增益指向性天線只得應用於固定式點對點系統。
```

## OFCA

5150 ~5350MHz & 6GHz band Wi-Fi (LPI) are also required to be used indoor in HongKong.

## Marcas comerciales

Los términos «HDMI», «HDMI High-Definition Multimedia Interface», la imagen comercial de HDMI y los logotipos de HDMI son marcas comerciales o marcas registradas de HDMI Licensing Administrator, Inc.

# Información de la empresa

| Nombre de la empresa | Arduino S.r.l.                              |
| -------------------- | ------------------------------------------- |
| Dirección            | Via Andrea Appiani 25, 20900 Monza (Italia) |

# Referencia de la documentación

| N.º | Referencia                 | Enlace                                                                                     |
| :-: | -------------------------- | ------------------------------------------------------------------------------------------ |
|  1  | Arduino App Lab            | [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)                   |
|  2  | Documentación de VENTUNO Q | [https://docs.arduino.cc/hardware/ventuno-q/](https://docs.arduino.cc/hardware/ventuno-q/) |
|  3  | Centro de proyectos        | [https://projecthub.arduino.cc/](https://projecthub.arduino.cc/)                           |
|  4  | Referencia de la librería  | [https://docs.arduino.cc/librerías/](https://docs.arduino.cc/librerías/)                   |
|  5  | Tienda de Arduino          | [https://store.arduino.cc/](https://store.arduino.cc/)                                     |

# Historial de revisiones del documento

| **Fecha**  | **Revisión** | **Cambios**         |
| :--------: | :----------: | ------------------- |
| 25/08/2026 |      1       | Primera publicación |
