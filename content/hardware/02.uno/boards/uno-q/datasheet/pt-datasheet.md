---
identifier: ABX00162-ABX00173
title: Arduino® UNO Q
type: maker
---

# Português

![](assets/featured.png)

# Descrição

<p style="text-align: justify;">O Arduino® UNO Q (doravante denominado UNO Q) é um computador de placa única que combina o microprocessador Qualcomm® Dragonwing™ QRB2210 (MPU), um Arm® Cortex®-A53 quad-core com sistema operativo Debian Linux, com o microcontrolador STMicroelectronics STM32U585 (MCU), um Arm® Cortex®-M33 com Arduino Core no sistema operativo Zephyr. O sistema Linux e o microcontrolador comunicam-se através da Bridge, a biblioteca RPC (Remote Procedure Call) da Arduino. Isso permite que os Arduino sketch no microcontrolador acessem os serviços Linux para tarefas de alto nível, enquanto as aplicações Linux podem interagir com os periféricos do microcontrolador para lidar com operações em tempo real dentro do mesmo projeto.
</p>

<p style="text-align: justify;">O UNO Q vem com armazenamento eMMC incorporado (opções de 16 GB, 32 GB) e LPDDR4X SDRAM (opções de 2 GB, 4 GB) para executar o Linux e os seus projetos com facilidade. Possui Wi-Fi® 5 de banda dupla e Bluetooth® 5.1 para conectividade sem fios, um conector USB-C® com entrada de alimentação e saída de vídeo e conectores compatíveis com Arduino para fácil expansão com shields, carriers e acessórios.</p>

<p style="text-align: justify;">O UNO Q integra-se perfeitamente com o Arduino App Lab, permitindo que os programadores combinem Arduino sketch, aplicações Linux e modelos de IA num único ambiente. O App Lab pode ser executado diretamente na placa ou a partir de um PC conectado, oferecendo exemplos prontos a utilizar e a flexibilidade para criar aplicações personalizadas adaptadas aos seus projetos.</p>

# Áreas

Prototipagem, IA e ML de ponta, visão artificial, educação, dispositivos inteligentes, robótica, automação residencial e predial, jogos

<div style="page-break-after: always;"></div>

# ÍNDICE

## Exemplos De Aplicações

<p style="text-align: justify;">O UNO Q combina um processador Linux com capacidade para IA com um microcontrolador em tempo real, oferecendo o melhor da computação de alto nível e do controlo determinístico. Além dessa arquitetura dupla, ele suporta um amplo ecossistema de shields Arduino, carriers, nós Modulino® e acessórios de terceiros, tornando-o uma plataforma flexível para diversas aplicações.
</p>

- **Prototipagem:** provas de conceito rápidas, como ferramentas de inspeção baseadas em visão, quiosques inteligentes ou computadores compactos de ponta com conectividade integrada.

- **Educação:** Ensino de Linux, programação em tempo real, IA e visão computacional por meio de aprendizagem baseada em projetos, desde experiências científicas até robôs educacionais interativos.

- **Robótica:** Robôs de entrega autônomos, companheiros que seguem gestos e braços robóticos com feedback visual, combinando visão Linux com controle de motor acionado por MCU.

- **Dispositivos de consumo inteligentes:** Câmaras inteligentes DIY, ecrãs interativos ou projetos de RA alimentados por câmaras duplas e aceleração GPU.

- **Automação residencial e predial:** Campainhas inteligentes com reconhecimento facial, sistemas controlados por voz e hubs climáticos personalizados.

- **Jogos:** emulação de consolas retrô, gabinetes de arcade personalizados ou jogabilidade aprimorada com controles baseados em gestos, rastreamento facial e feedback em tempo real.

<div style="page-break-after: always;"></div>

## Características

### UNO Q Variantes

O UNO Q está disponível em duas variantes:

- **ABX00162**: 2 GB de RAM, 16 GB de armazenamento integrado
- **ABX00173**: 4 GB de RAM, 32 GB de armazenamento integrado

### Especificações Gerais

#### Processamento & Memória

![](assets/ABX00162-ABX00173-main-components.png)


| **Subsistema** | **Detalhes** |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MPU principal      | - Qualcomm Dragonwing™ QRB2210 - Sistema em chip (SoC) (MPU) (SOC1): 4 × Arm Cortex-A53 a 2,0 GHz, 64 bits <br></br>- GPU Adreno 702 a 845 MHz (gráficos 3D) <br></br>- ISPs duplos: 13 MP + 13 MP ou 25 MP a 30 fps <br></br>- Sistema operativo Debian (suporte upstream) <br></br>- E/S: USB 3.1 com capacidades de troca de funções através do conector USB, SDIO 3.0, MIPI-CSI-2 de 4 vias e MIPI-DSI de 4 vias |
| MCU em tempo real | - ST STM32U585 (MCU) (MCU1), Arm Cortex-M33 até 160 MHz <br></br>- Arduino Core no sistema operativo Zephyr <br></br>- 2 MB de memória Flash, 786 kB de SRAM                                                                                                                                                                                                                                                   |
| Memória do sistema | - Opções eMMC de 16 ou 32 GB (EMMC1) para SO/dados <br></br>- Opções LPDDR4X de 2 GB ou 4 GB (single-rank, 32 bits) (DRAM1)                                                                                                                                                                                                                                                                 |



<p style="text-align: justify;">O Qualcomm Dragonwing™ QRB2210 I/O opera a 1,8 V.
O MPU controla as interfaces da câmara MIPI-CSI-2 e do ecrã MIPI-DSI no JMEDIA, bem como os pontos finais GPIO e áudio do MPU (SoC) de 1,8 V expostos no JMISC.
O JMISC é um conector de tensão mista que também transporta sinais MCU de 3,3 V e áudio analógico juntamente com as linhas MPU de 1,8 V. O vídeo DisplayPort é fornecido pelo ANX7625 integrado, que converte o MIPI-DSI do MPU para DisplayPort Alt-Mode no USB-C.
O STM32U585 gerencia ADC, PWM, CAN, a matriz LED e os conectores de 3,3 V (JDIGITAL, JANALOG, JSPI e Qwiic).</p>

#### Conectividade & Mídia

![](assets/ABX00162-ABX00173-comm-components.png)


| **Subsistema**      | **Detalhes**                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Módulo sem fios    | - WCBN3536A (Qualcomm WCN3980) (U2901) <br></br>- Wi-Fi® 5 802.11a/b/g/n/ac (banda dupla) + Bluetooth® 5.1                                                                                                                                                                                                                                                                                                                                                                         |
| Porta USB-C (JUSB1) | - USB 3.1 com capacidades de troca de funções<br></br>- Modo alternativo DisplayPort através da ponte ANX7625 DSI-para-DP (U3001) (os pares diferenciais SuperSpeed no Tipo C são encaminhados para o modo alternativo DP)<br></br>- Saída de vídeo (modo SBC): suporta monitores Full HD (1920 × 1080p); a resolução ideal é 1280 × 720p<br></br>- A negociação USB Power Delivery solicita apenas um contrato de **5 V / 3 A** (sem perfis de tensão mais elevada)<br></br>- Proteção VBUS load-switch/back-drive (Q2801) |


O módulo sem fios utiliza SDIO para dados Wi-Fi® e um UART para controlo Bluetooth®, com uma antena PCB partilhada.

#### Expansão & Conectores

![](assets/ABX00162-ABX00173-header-expansion.png)

| **Interface (Conector)** | **Tensão & Número pin**       | **Detalhes**                                                                                                                                                                                                                                                                                                                                            |
|---------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JMEDIA (JMEDIA1)          | Sinais de 1,8 V, 60 pinos         | - Linhas de alta velocidade para câmera/monitor (MIPI DSI, CSI) <br></br>- Barramento de controle da câmera (CCI I²C) - dedicado, não GPIO de uso geral <br></br>- Relógios de câmara (SOC_CAM_MCLK0/1) <br></br>- Também transporta trilhos de alimentação (+3V3 OUT, VIN IN) e GND |
| JMISC (JMISC1)            | Misto 1,8 V / 3,3 V, 60 pinos   | - GPIO e SDIO mistos <br></br>- Periféricos MCU: SDMMC1, TRACE, PSSI (câmara paralela), I²C4, pinos MCO/CRS_SYNC, OPAMP1 <br></br>- Terminais de áudio: Mic2 INP/INM/BIAS, Auscultadores L/R + REF, LineOut P/M, Auricular P/R, HS_DET <br></br>- Bancos GPIO MPU (SoC) (SE0) a 1,8 V <br></br>- Também transporta trilhos de alimentação (+5V USB OUT, +3V3 OUT, +1V8 OUT, VBAT OUT, VCOIN IN) e GND |
| JCTL (JCTL1)              | 1,8 V, 10 pinos                 | - Consola SE4 UART <br></br>- Entrada de arranque USB forçada <br></br>- Entrada de reinicialização PMIC <br></br>- Desativação do interruptor de alimentação VBUS <br></br>- Trilho de 1,8 V e GND |
| JDIGITAL (JDIGITAL1)      | 3,3 V, 18 pinos                 | - E/S digital para SPI, I²C, UART, PWM, CAN |
| JANALOG (JANALOG1)        | 3,3 V, 14 pinos | - E/S analógica - Canais ADC e referências |
| JSPI (JSPI1)              | Lógica de 3,3 V, 6 pinos + 5 V VBUS | - SPI dedicado: MOSI, MISO, SCLK <br></br>- Reinicialização do MCU (NRST) <br></br>- Terra <br></br>- 5 V VBUS (alimentação USB)                                                                                                                                                                                                                                                                |
| Qwiic (QWIIC1)            | 3,3 V, 4 pinos | - I²C (ecossistema Qwiic) |

### Produtos Relacionados

- Shields Arduino UNO via JDIGITAL e JANALOG
- Placas carrier compatíveis com UNO Q
- Cabo USB-C completo de 24 pin
- Dongle USB-C com capacidade de fornecimento de energia externa

<div style="page-break-after: always;"></div>

## Características elétricas

### Potência De Entrada

![Métodos de entrada UNO Q](assets/ABX00162-ABX00173-power-supply.png)

| **Fonte**  | **Intervalo de Tensão** | **Corrente Máxima** | **Conector**         |
|-------------|------------------:|--------------------:|-----------------------|
| USB-C VBUS  |               5 V |           até 3 A | Conector USB-C       |
| VIN (DC IN) |            7-24 V |                   - | JMEDIA, JANALOG (VIN) |
| Pino 5 V     |               5 V |           até 3 A | JANALOG               |


<p style="text-align: justify;">O UNO Q suporta duas entradas de alimentação: uma porta USB-C e uma entrada de 7-24 V CC. Através da USB Power Delivery, solicita apenas o contrato de 5 V / 3 A e não solicita perfis PD de tensão mais elevada. Utilize uma fonte e um cabo com classificação para 5 V a 3 A para evitar subtensão durante picos de atividade curtos, como rajadas sem fios ou inicialização do ecrã. Uma fonte externa regulada de 5 V DC também pode ser utilizada para fornecer energia à placa através do pino de 5 V no conector JANALOG.
</p>

<p style="text-align: justify;">O <em>USB-C VBUS</em> e a saída de 5 V do buck de 7-24 V são combinados por <em>diodo OR</em> no barramento de 5 V do sistema (<code>5V_SYS</code>). A partir de <code>5V_SYS</code>, o projeto deriva o nó pré-regulador de 3,8 V e, subsequentemente, o de 3,3 V.
O PMIC, alimentado por 5V_SYS, deriva o trilho de 1,8 V.
</p>

<p style="text-align: justify;"><strong>Proteção contra polaridade inversa:</strong> Verificado com -24 V aplicados à entrada DC IN. A operação é especificada apenas com a polaridade correta. Não aplique tensão inversa durante o uso normal.
</p>

<p style="text-align: justify;"><strong>Caminho OR Schottky:</strong> A queda de tensão direta da saída buck para <code>5V_SYS</code> foi medida da seguinte forma (injeção JANALOG VIN, alimentação Rigol DP832 em série, medição Keithley DMM6500, carga ativa 8542B). A dissipação de energia é calculada como <code>P = I × Vf</code>.
</p>

| **Corrente de carga** | **Queda direta (`Vf`)** | **Dissipação do díodo** |
|-----------------:|------------------------:|----------------------:|
|            1,0 A |                  0,35 V |                0,35 W |
|            1,5 A |                  0,37 V |                0,56 W |
|            2,0 A |                  0,39 V |                0,78 W |



### Condições Operacionais Recomendadas

Utilize os limites abaixo para dimensionar fontes de alimentação, definir tolerâncias de trilhos e planejar margem térmica:


| **Parâmetro**         | **Símbolo**  | **Mínimo** | **Típico** | **Máximo** | **Unidade** |
|-----------------------|-------------|:-----------:|:-----------:|:-----------:|:--------:|
| Entrada USB-C           | `VBUS_USBC` |     4,5     |     5,0     |     5,5     |    V     |
| Entrada CC              | `DC_IN`     |     7,0     |      -      |    24,0     |    V     |
| Trilho do sistema de 3,3 V     | `PWR_3P3V`  |     3,1     |     3,3     |     3,5     |    V     |
| Temperatura de funcionamento | `T_OP`      |     -10     |      -      |     60      |    °C    |


<p style="text-align: justify;"><em>Mínimo</em> indica o valor contínuo mais baixo para operação regular; quedas breves podem causar reinicializações ou quedas de ligação. <em>Típico</em> é o ponto nominal de projeto. <em>Máximo</em> não deve ser excedido. Para <code>DC_IN</code> (7-24 V), selecione uma fonte que cubra confortavelmente a carga de 5 V e utilize cabos curtos para reduzir a queda de tensão. A faixa <code>PWR_3P3V</code> reflete a tolerância do regulador e a carga. A faixa de temperatura refere-se ao ar ambiente próximo à placa, e operar perto dos limites pode reduzir a corrente de saída disponível.
</p>

### Tensão De Alimentação Integrada


| **Tensão** | **Rail**         | **Origem / Regulador**                                                       |
|------------:|------------------|------------------------------------------------------------------------------|
|       5,0 V | `5V_SYS`         | Diodo OR de USB-C VBUS e saída buck de 7-24 V (ambos através de retificadores Schottky) |
|       3,8 V | `PWR_3P8V`       | Redução (buck) de `5V_SYS`                                               |
|       3,3 V | `PWR_3P3V`       | Redução (buck) de `PWR_3P8V`                                             |
|       1,8 V | `VREG_L15A_1P8V` | PM4125 LDO L15A  de `5V_SYS`                                               |


<div style="page-break-after: always;"></div>

## Funções Gerais

### Pinout

![](assets/ABX00162-ABX00173_pinout.png)

### Diagrama De Blocos

![](assets/ABX00162-ABX00173_block_diagram.png)

### Fonte De Alimentação

<p style="text-align: justify;">O UNO Q suporta duas entradas de alimentação: uma porta USB-C e uma entrada de 7-24 V CC. 
O <em>USB-C VBUS</em> e a saída de 5 V do buck de 7-24 V são combinados por <em>diodo OR</em> no barramento de 5 V do sistema (5V_SYS).</p>

<p style="text-align: justify;"><code>5V_SYS</code> fornece o <strong>PM4125 PMIC (PMIC1)</strong> em <code>USB_IN</code>.
O LDO L15A do PMIC fornece o trilho de 1,8 V (<code>VREG_L15A_1P8V</code>) e alimenta os bancos de E/S do SoC, ANX7625 <code>DVDD18</code>, lógica digital Wi-Fi® e os shifters de nível integrados. O trilho de 1,8 V também está disponível em <code>JMISC</code>.
A partir de <code>5V_SYS</code>, um buck gera o <code>PWR_3P8V (3,8 V)</code> reservado para o design do sistema e recursos futuros.
Um segundo regulador buck gera <code>PWR_3P3V</code> para o STM32U585, o ANX7625 (trilhos de 3,3 V), o domínio Wi-Fi® de 3,3 V e os pinos do conector de 3,3 V.</p>
<p style="text-align: justify;">Um <em>MOSFET de canal P protegido</em> (<code>Q2801</code>) pode fornecer USB <code>VBUS</code> a partir de <code>5V_SYS</code> quando a placa funciona como um host USB/OTG. O <code>VCOIN</code> alimenta apenas o relógio em tempo real do PMIC e não alimenta os domínios Linux ou MCU.O <code>VBAT</code> liga-se ao <code>PWR_3P8V</code> e está reservado para o design do sistema e funcionalidades futuras. </p>

![Arduino UNO Q Power Tree](assets/ABX00162-ABX00173_power_tree.png)

<div style="page-break-after: always;"></div>

## IU & Indicadores

![](assets/ABX00162-ABX00173-leds.png)

- **LEDs RGB (controlados por Linux):** Dois LEDs tricolores são acionados pelo processador de aplicativos Qualcomm Dragonwing™ QRB2210 e expostos via `/sys/class/leds/`.

  - **LED RGB 1 (D27301):** canais: `vermelho:usuário` → **GPIO_41**, `verde:usuário` → **GPIO_42**, `azul:usuário` → **GPIO_60**.
  - **LED RGB 2 (D27302):** canais: `vermelho:pânico` → **GPIO_39**, `verde:wlan` → **GPIO_40**, `azul:bt` → **GPIO_47**.
    
    Por predefinição, o LED RGB 2 indica o estado do sistema, `PANIC`, `WLAN` e `BT`, mas também pode ser controlado pelo utilizador. A frequência PWM é de aproximadamente 2 kHz para transições de cor suaves.

- **LEDs RGB (controlados por MCU):** Dois LEDs tricolores são acionados pelo STM32U585.

  - **LED RGB 3 (D27401):** `LED3_R` → **PH10**, `LED3_G` → **PH11**, `LED3_B` → **PH12**.
  - **LED RGB 4 (D27402):** `LED4_R` → **PH13**, `LED4_G` → **PH14**, `LED4_B` → **PH15**.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
Os LEDs RGB são ativos baixos, o que significa que se acendem quando acionados para a lógica `0`.
</div>

- **Matriz LED (D27001..D27104):** Matriz LED monocromática azul 8 × 13 (104 pixels) acionada pelo STM32U585. Exibe o logótipo de inicialização por aproximadamente 20 a 30 segundos durante a inicialização do Linux. O acesso à matriz antes da conclusão da inicialização pode interferir na operação do MCU.

- **LED de alimentação (D27201):** Indicador verde ligado ao trilho de 3,3 V e aceso sempre que a placa é alimentada.

## MPU & MCU

<p style="text-align: justify;">
Uma MPU (unidade de microprocessador) é um processador de aplicativos de alto desempenho projetado para executar um sistema operacional completo e software complexos. Uma MCU (unidade de microcontrolador) é um controlador pequeno e com baixo consumo de energia, focado em temporização rápida e precisa para E/S e controle. O UNO Q combina ambos para emparelhar a computação ao nível do sistema operativo com um controlo responsivo e crítico em termos de tempo numa placa única e comunicar através do Bridge, uma camada RPC implementada em ambos os lados.</p>

### Processador De Aplicações (MPU)
<p style="text-align: justify;">
O Qualcomm® Dragonwing™ QRB2210 é um Arm® Cortex®-A53 quad-core que executa o sistema operativo Debian Linux. A sua E/S opera a 1,8 V e lida com mídia de alta velocidade e política Type-C/PD.
</p>

<ul>
  <li>Domínio de tensão: 1,8 V para MPU (SoC) GPIO e interfaces de alta velocidade</li>
  <li>Comanda JMEDIA: câmera MIPI-CSI-2 e pistas de exibição MIPI-DSI</li>
  <li>Comanda 1,8 V MPU GPIO e terminais de áudio em JMISC (conector de tensão mista)</li>
  <li>USB-C: troca de funções e negociação PD (solicita 5 V / 3 A)</li>
  <li>Saída DisplayPort via ANX7625 integrado (converte MIPI-DSI para DP Alt-Mode)</li>
</ul>

### Microcontrolador Em Tempo Real (MCU)

<p style="text-align: justify;">
O STMicroelectronics® STM32U585 é um Arm® Cortex®-M33 que executa o Arduino Core no Zephyr OS. Ele fornece temporização rápida e precisa para tarefas de controlo e conectores de E/S de 3,3 V.
</p>

<ul>
  <li>Domínio de tensão: 3,3 V para GPIO e analógico (VREF+ ≈ 3,3 V)</li>
  <li>Gerencia ADC, PWM, CAN, matriz LED, temporizadores</li>
  <li>Lida com conectores de 3,3 V: JDIGITAL, JANALOG, JSPI, Qwiic</li>
</ul>
<p style="text-align: justify;">
O JMISC lida com ambos os domínios: linhas MPU de 1,8 V ficam ao lado de sinais MCU de 3,3 V (por exemplo, PSSI, SDMMC1, TRACE, I²C4) e analógico/áudio. Verifique os níveis de tensão ao conectar carrier ou lógica externa.
</p>

## Comunicação Entre Processadores

<p style="text-align: justify;">O Qualcomm® Dragonwing™ QRB2210 (MPU) e o STM32U585 (MCU) comunicam através da Arduino Bridge, uma camada de Chamada de Procedimento Remoto (RPC) baseada em software implementada tanto no lado Linux como no lado MCU. A Bridge fornece uma API orientada a serviços que permite que qualquer um dos processadores exponha serviços para o outro chamar, ao mesmo tempo que suporta notificações unidirecionais para eventos assíncronos. Ela gerencia o encaminhamento de mensagens entre processadores e acomoda vários transportes físicos. Através da sua API, a Bridge permite chamadas de função seguras, permitindo que sketches de microcontroladores invoquem serviços Linux e recebam respostas estruturadas, ou enviem dados através de notificações.</p>

<p style="text-align: justify;">Se for necessário um indicador de hardware para uma placa carrier ou lógica externa, o firmware pode dedicar um GPIO MPU de 1,8 V no JMISC ou um GPIO JCTL disponível como saída pronta ou de ativação. Este sinal pode ser recebido num GPIO MCU através de circuitos compatíveis com o nível, tais como um deslocador de nível ou uma configuração de dreno aberto com um resistor pull-up. O firmware define a função exata deste sinal. Alternativamente, a atividade no transporte selecionado (USB CDC, UART ou SPI) pode servir como fonte de ativação quando o MCU está no modo de suspensão</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Os sinais GPIO do MPU operam no domínio de baixa tensão do processador da aplicação (1,8 V). Certifique-se de que qualquer ligação ao microcontrolador seja compatível com o nível da sua tensão de E/S (3,3 V). Por exemplo, utilize um nivelador ou uma configuração de dreno aberto com um pull-up para a tensão de E/S do microcontrolador.
</div>

<div style="page-break-after: always;"></div>

## Aceleração Hardware

<p style="text-align: justify;">O UNO Q fornece aceleração de hardware para gráficos 3D e codificação/decodificação de vídeo através da GPU Adreno 702 integrada, operando a 845 MHz.</p>

### Aceleração Gráfica

<p style="text-align: justify;">A GPU Adreno 702 fornece renderização de gráficos 3D acelerada por hardware através de controladores Mesa de código aberto. As aplicações podem aceder à aceleração da GPU através de APIs gráficas padrão, incluindo OpenGL, OpenGL ES, Vulkan e OpenCL.</p>


| **API gráfica** | **Controlador** | **Suporte de hardware** | **Versão atual do controlador** | **Nome do dispositivo**        |
|------------------|------------|----------------------|----------------------------|------------------------|
| Desktop OpenGL   | freedreno  | -                    | 3.1                        | FD702                  |
| OpenGL ES        | freedreno  | 3.1                  | 3.1                        | FD702                  |
| Vulkan           | turnip     | 1.1                  | 1.0.318                    | Turnip Adreno (TM) 702 |
| OpenCL           | Mesa       | 2.0                  | 2.0                        | -                      |



<p style="text-align: justify;">A GPU Adreno 702 apresenta uma arquitetura de memória unificada, partilhando a RAM do sistema com a CPU para transferência de dados. Suporta endereçamento de memória de 64 bits e oferece recursos de renderização direta para um desempenho gráfico ideal.</p>



| **Parâmetro** | **Especificação** |
|--------------------------------|----------------------------------|
| Frequência do relógio                | 845 MHz                          |
| Arquitetura de memória            | Unificada (partilhada com a RAM do sistema) |
| Memória de vídeo disponível         | 1740 MB                          |
| Endereçamento de memória              | 64 bits                           |
| Renderização direta               | Sim                              |
| Tamanho máximo da textura 2D        | 16384 × 16384 pixels             |
| Tamanho máximo da textura 3D        | 2048³ voxels                     |
| Tamanho máximo do mapa cúbico          | 16384 × 16384 pixels             |
| Linguagem de sombreamento OpenGL (GLSL) | 1.40                             |
| Linguagem de sombreamento OpenGL ES     | 3.10 ES                          |


<p style="text-align: justify;">A pilha gráfica Mesa oferece suporte para extensões e recursos OpenGL padrão. Aplicações que utilizam OpenGL, OpenGL ES ou Vulkan utilizarão automaticamente a aceleração de hardware sem configuração adicional. Utilitários gráficos padrão, como mesa-utils e vulkan-tools, funcionam imediatamente no UNO Q.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Observação:</strong> Os controladores OpenGL e Vulkan estão disponíveis através dos controladores Mesa de código aberto <strong>freedreno (OpenGL/OpenGL ES)</strong> e <strong>turnip (Vulkan)</strong>, proporcionando transparência e suporte da comunidade. Embora o hardware Adreno 702 seja compatível com Vulkan 1.1, a implementação atual do controlador oferece Vulkan 1.0.318. <strong>Não há exemplos específicos do UNO Q para OpenGL ou Vulkan. No entanto, os utilitários padrão do Mesa e os exemplos do projeto Mesa podem ser usados como referência.</strong>
</div>

### Aceleração Vídeo

<p style="text-align: justify;">A GPU Adreno 702 inclui codificadores e descodificadores de vídeo de hardware dedicados acessíveis através da API <code>V4L2 (Video4Linux2)</code> através dos dispositivos <code>/dev/video0</code> e <code>/dev/video1</code>. A aceleração de hardware está disponível para os seguintes codecs de vídeo:</p>


| **Codec**    | **Codificação** | **Decodificação** | **Elemento GStreamer**     |
|--------------|--------------|--------------|---------------------------|
| H.264 (AVC)  | Sim          | Sim          | v4l2h264enc / v4l2h264dec |
| H.265 (HEVC) | Sim          | Sim          | v4l2h265enc / v4l2h265dec |
| VP9          | Não           | Sim          | v4l2vp9dec                |



<p style="text-align: justify;">O codificador e descodificador de vídeo de hardware descarregam as tarefas de compressão e descompressão da CPU para hardware dedicado, permitindo um processamento de vídeo em tempo real eficiente. Isto reduz o consumo de energia do sistema e permite que a CPU se concentre na lógica da aplicação. A aceleração de hardware está disponível para resoluções de até 1920×1080 (Full HD), incluindo formatos comuns como 720p (1280×720).</p>

#### Integração GStreamer

<p style="text-align: justify;">A abordagem recomendada para aceder à aceleração de vídeo por hardware é através do GStreamer, que fornece uma interface de pipeline de alto nível para os dispositivos V4L2. Os seguintes elementos do GStreamer fornecem processamento de vídeo acelerado por hardware:</p>

Para decodificação H.264, o seguinte pipeline pode ser utilizado:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h264parse ! v4l2h264dec \
  ! videoconvert ! autovideosink
```

Para a descodificação H.265, pode ser utilizado o seguinte pipeline:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h265parse ! v4l2h265dec \
  ! videoconvert ! autovideosink
```

Para decodificação VP9, o seguinte pipeline pode ser utilizado:

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.webm \
  ! matroskademux ! queue ! v4l2vp9dec \
  ! videoconvert ! autovideosink
```

Para codificação H.264, pode-se utilizar o seguinte pipeline:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc ! h264parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Para codificação H.265, pode-se utilizar o seguinte pipeline:

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1920,height=1080,framerate=30/1 \
  ! v4l2h265enc ! h265parse ! mp4mux ! filesink location=/tmp/output.mp4
```

Para codificação e descodificação simultâneas, pode ser utilizado o seguinte pipeline:

```bash
gst-launch-1.0 -v videotestsrc num-buffers=1000 \
  ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc capture-io-mode=4 output-io-mode=2 ! h264parse \
  ! v4l2h264dec capture-io-mode=4 output-io-mode=2 ! videoconvert \
  ! autovideosink
```

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
 <strong>Acesso para desenvolvedores:</strong> Os dispositivos de vídeo V4L2 são acessíveis por meio de APIs padrão do Linux, permitindo a integração direta em aplicações C/C++ usando libv4l2 ou por meio de frameworks de nível superior, como GStreamer, FFmpeg ou OpenCV com suporte de backend V4L2.
</div>

### Suporte a OpenCL

<p style="text-align: justify;">O suporte a OpenCL 2.0 está disponível por meio da implementação Mesa, permitindo computação GPU de uso geral (GPGPU) para tarefas de processamento paralelo, computação científica e operações computacionais intensivas. Os recursos OpenCL do Adreno 702 permitem transferir cargas de trabalho computacionais intensivas da CPU para a GPU, melhorando o desempenho.</p>

<div style="page-break-after: always;"></div>

## Periféricos

![Periféricos UNO Q](assets/ABX00162-ABX00173_headers.png)

- **JDIGITAL (A2) (JDIGITAL1) / JANALOG (A3) (JANALOG1):** GPIO de 3,3 V com suporte para entradas SPI, UART, CAN, PWM e ADC. As entradas analógicas são referenciadas a `VREF+` no trilho de 3,3 V. A faixa de entrada válida é de 0 V a `VREF+`. Alguns pinos do STM32U585 toleram 5 V no modo digital; no entanto, quando configurados como ADC ou qualquer função analógica (como *A0* a *A5*), eles não toleram 5 V e não devem exceder `VDD + 0,3 V`. Use condicionamento externo, como um divisor de tensão ou buffer, para tensões mais altas. Para *A4/A5* quando usados como I2C3 (PC1/PC0), use pull-ups apenas para 3,3 V. Além disso, **~D3 (PB0)** usa uma estrutura de E/S do tipo TT e é tolerante a 3,6 V; não é tolerante a 5 V em nenhum modo, incluindo o digital.

- **Conector QWIIC (A4) (QWIIC1):** Barramento I²C adicional (lógica de 3,3 V). Mapeia como **PD13 (I2C4_SDA)** e **PD12 (I2C4_SCL)**. Garante compatibilidade plug-and-play com nós Modulino® e sensores e atuadores de terceiros.

- **JSPI (A5) (JSPI1):** Conector SPI de 3,3 V para periféricos que fornece sinais MOSI, MISO e SCLK, com seleção de chip disponível através de um pino GPIO em JDIGITAL/JMISC. Os pinos utilizam configuração do tipo STM32U585 FT com MISO em PC2, MOSI em PC3 e SCK em PD1. São tolerantes a 5 V como entradas ou em dreno aberto, enquanto as saídas conduzem 3,3 V. Adicione mudança de nível se for necessário um limiar de entrada de 5 V ou sinalização bidirecional de 5 V. Inclui um pino de alimentação `5V_SYS`.

- **JMEDIA (B2) (JMEDIA1):** Sinais de câmara e ecrã de quatro vias no domínio de 1,8 V (MIPI-CSI-2 e MIPI-DSI).

- **JMISC (B1) (JMISC):** Conector de função mista que combina sinais MCU de 3,3 V e sinais MPU de 1,8 V. Fornece barramento MCU PSSI (câmara paralela), pinos de teste SDMMC1, TRACE, I2C4, MCO/CRS_SYNC e pinos analógicos OPAMP1. Além disso, ele divide o áudio (Mic2, Headphone L/R+REF, LineOut P/M, Earpiece P/R, HS_DET) e os trilhos de alimentação (+3V3, +5V_USB, +1V8, VBAT e VCOIN para uso do sistema). Observe os domínios de tensão: **os pinos MCU são 3,3 V, os GPIO MPU são 1,8 V**.

- **JCTL (A1) (JCTL1):** Pinos do modo de inicialização, reinicialização e sinais de ativação de baixa potência (lógica de 1,8 V).

<p style="text-align: justify;"><strong>SE4 UART</strong> é a consola do sistema (<code>shell UART</code>). É separada dos UARTs da aplicação e não deve ser reutilizada para E/S do utilizador. Opera no domínio de E/S de <strong>1,8 V</strong> da MPU.</p>

<p style="text-align: justify;">Não utilize as linhas Qualcomm Dragonwing™ QRB2210 reservadas para <strong>I²C</strong>, <strong>JMEDIA CCI</strong> (Camera Control Interface) ou <strong>MI2S0</strong> (barramento de áudio I²S) como E/S de uso geral. Estes sinais são dedicados à interface, operam a <strong>1,8 V</strong> e estão reservados na árvore de dispositivos Linux. Os conectores expõem-nos apenas para essas funções.</p>

### JMISC (B1) (JMISC1) - Mapa De Pin

| **Pin** | **Designação** | **Pino MCU/SoC** | **Domínio** | **Notas**                 |
|--------:|-----------------|-----------------|------------|---------------------------|
|       1 | MCU_PSSI_D0     | PC6             | 3,3 V MCU   | PSSI D0                   |
|       2 | MCU_SDMMC1_CMD  | PD2             | 3,3 V MCU   | SDMMC1 CMD / teste         |
|       3 | MCU_PSSI_D1     | PC7             | 3,3 V MCU   | PSSI D1                   |
|       4 | MCU_TRACE_CLK   | PE2             | 3,3 V MCU   | Relógio de rastreamento               |
|       5 | MCU_PSSI_D2     | PC8             | 3,3 V MCU   | PSSI D2                   |
|       6 | MCU_TRACE_D0    | PE3             | 3,3 V MCU   | Dados de rastreamento 0              |
|       7 | MCU_PSSI_D3     | PC9             | 3,3 V MCU   | PSSI D3                   |
|       8 | MCU_TRACE_D2    | PE5             | 3,3 V MCU   | Dados de rastreamento 2              |
|       9 | MCU_PSSI_D4     | PE4             | 3,3 V MCU   | PSSI D4                   |
|      10 | MCU_TRACE_D3    | PE6             | 3,3 V MCU   | Dados de rastreamento 3              |
|      11 | MCU_PSSI_D5     | PI4             | 3,3 V MCU   | PSSI D5                   |
|      12 | MCU_PE7         | PE7             | 3,3 V MCU   | GPIO                      |
|      13 | MCU_PSSI_D6     | PI6             | 3,3 V MCU   | PSSI D6                   |
|      14 | MCU_PE8         | PE8             | 3,3 V MCU   | GPIO                      |
|      15 | MCU_PSSI_D7     | PI7             | 3,3 V MCU   | PSSI D7                   |
|      16 | MCU_I2C4_SCL    | PF14            | 3,3 V MCU   | I²C4 SCL                  |
|      17 | MCU_PSSI_PDCK   | PD9             | 3,3 V MCU   | Relógio PSSI                |
|      18 | MCU_I2C4_SDA    | PF15            | 3,3 V MCU   | I²C4 SDA                  |
|      19 | MCU_PSSI_RDY    | PI5             | 3,3 V MCU   | PSSI pronto                |
|      20 | MCU_OPAMP1_VOUT | PA3             | Analógico     | OpAmp1 VOUT               |
|      21 | MCU_PSSI_DE     | PD8             | 3,3 V MCU   | PSSI dados ativados          |
|      22 | MCU_OPAMP1_VINP | PA0             | Analógico     | OpAmp1 VINP               |
|      23 | MCU_MCO         | PA8             | 3,3 V MCU   | Saída do relógio MCU             |
|      24 | MCU_OPAMP1_VINM | PA1             | Analógico     | OpAmp1 VINM               |
|      25 | MCU_CRS_SYNC    | PA10            | 3,3 V MCU   | Sincronização CRS                  |
|      26 | GND             | -               | Alimentação      | Terra                    |
|      27 | GND             | -               | Alimentação      | Terra                    |
|      28 | EAR_P_R         | -               | Analógico     | Áudio auricular P_R             |
|      29 | MIC2_INP        | -               | Analógico     | Mic2 IN+                  |
|      30 | EAR_M_R         | -               | Analógico     | Áudio M_R             |
|      31 | MIC2_INM        | -               | Analógico     | Mic2 IN−                  |
|      32 | LINEOUT_P       | -               | Analógico     | Saída de linha P                |
|      33 | MIC2_BIAS       | -               | Analógico     | Polarização do microfone 2                 |
|      34 | LINEOUT_M       | -               | Analógico     | Saída de linha M                |
|      35 | GND             | -               | Alimentação      | Terra                    |
|      36 | HPH_L           | -               | Analógico     | Auscultadores L               |
|      37 | SOC_GPIO_0_SE0  | -               | 1,8 V MPU   | SoC GPIO 0 (SE0)          |
|      38 | HPH_R           | -               | Analógico     | Auscultadores R               |
|      39 | SOC_GPIO_1_SE0  | - | 1,8 V MPU | SoC GPIO 1 (SE0) |
| 40 | HPH_REF | - | Analógico | REF dos auscultadores |
| 41 | SOC_GPIO_2_SE0 | - | 1,8 V MPU | SoC GPIO 2 (SE0) |
|      42 | HS_DET          | -               | Analógico     | Detecção de auscultadores            |
|      43 | SOC_GPIO_3_SE0  | -               | 1,8 V MPU   | SoC GPIO 3 (SE0)          |
|      44 | GND             | -               | Alimentação      | Terra                    |
|      45 | SOC_GPIO_86_SE0 | -               | 1,8 V MPU   | SoC GPIO 86 (SE0)         |
|      46 | SOC_GPIO_98     | -               | 1,8 V MPU   | SoC GPIO 98               |
|      47 | SOC_GPIO_82_SE0 | -               | 1,8 V MPU   | SoC GPIO 82 (SE0)         |
|      48 | SOC_GPIO_99     | -               | 1,8 V MPU   | SoC GPIO 99               |
|      49 | SOC_GPIO_18     | -               | 1,8 V MPU   | SoC GPIO 18               |
|      50 | SOC_GPIO_100    | -               | 1,8 V MPU   | SoC GPIO 100              |
|      51 | SOC_GPIO_28     | -               | 1,8 V MPU   | SoC GPIO 28               |
|      52 | SOC_GPIO_101    | -               | 1,8 V MPU   | SoC GPIO 101              |
|      53 | +3V3 (OUT)      | -               | Alimentação      | Saída de alimentação de 3,3 V           |
|      54 | +5V_USB (OUT)   | -               | Alimentação      | Saída de alimentação de 5 V             |
|      55 | +3V3 (OUT)      | -               | Alimentação      | Saída de alimentação de 3,3 V           |
|      56 | +5V_USB (OUT)   | -               | Alimentação      | Saída de alimentação de 5 V             |
|      57 | +1V8 (ENTRADA)       | -               | Alimentação      | Entrada de 1,8 V             |
|      58 | GND             | -               | Alimentação      | Terra                    |
|      59 | VCOIN (ENTRADA)      | -               | Alimentação      | Tensão do sistema (PMIC RTC) |
|      60 | VBAT (OUT)     | -               | Alimentação      | Tensão do sistema (reservada para o design do sistema e funcionalidades futuras) |



<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Nota: As linhas GPIO SoC no JMISC são dedicadas à interface (não são GPIO do fabricante). As MCU têm lógica de 3,3 V, as MPU têm lógica de 1,8 V e o áudio/microfone são analógicos.
</div>

<div style="page-break-after: always;"></div>

### JMEDIA (B2) (JMEDIA1) - Mapa De Pin


| **Pin** | **Designação**         | **Domínio** | **Notas**               |
|--------:|-------------------------|------------|-------------------------|
|       1 | GND                     | Alimentação      | Terra                  |
|       2 | GND                     | Alimentação      | Terra                  |
|       3 | MIPI_DSI0_CLK_M         | MIPI D-PHY | Relógio DSI −             |
|       4 | MIPI_DSI0_L1_P          | MIPI D-PHY | DSI lane1 +             |
|       5 | MIPI_DSI0_CLK_P         | MIPI D-PHY | Relógio DSI +             |
|       6 | MIPI_DSI0_L1_M          | MIPI D-PHY | Pista DSI1 −             |
|       7 | GND                     | Alimentação      | Terra                  |
|       8 | GND                     | Alimentação      | Terra                  |
|       9 | MIPI_DSI0_L2_M          | MIPI D-PHY | DSI lane2 −             |
|      10 | MIPI_DSI0_L0_P          | MIPI D-PHY | DSI lane0 +             |
|      11 | MIPI_DSI0_L2_P          | MIPI D-PHY | DSI lane2 +             |
|      12 | MIPI_DSI0_L0_M          | MIPI D-PHY | DSI lane0 −             |
|      13 | GND                     | Alimentação      | Terra                  |
|      14 | GND                     | Alimentação      | Terra                  |
|      15 | MIPI_DSI0_L3_M          | MIPI D-PHY | DSI lane3 −             |
|      16 | SOC_CAM_MCLK0 (GPIO_20) | 1,8 V MPU   | Relógio mestre da câmara 0   |
|      17 | MIPI_DSI0_L3_P          | MIPI D-PHY | DSI lane3 +             |
|      18 | SOC_CAM_MCLK1 (GPIO_21) | 1,8 V MPU   | Relógio mestre da câmara 1   |
|      19 | GND                     | Alimentação      | Terra                  |
|      20 | GND                     | Alimentação      | Terra                  |
|      21 | CSI0_C0_LN0_M           | MIPI D-PHY | CSI0 dados0 −            |
|      22 | CCI_I2C_SDA1 (GPIO_29)  | 1,8 V MPU   | Controlo da câmara I²C SDA1 |
|      23 | CSI0_B0_LN0_P           | MIPI D-PHY | Dados CSI00 +            |
|      24 | CCI_I2C_SCL1 (GPIO_30)  | 1,8 V MPU   | Controlo da câmara I²C SCL1 |
|      25 | GND                     | Alimentação      | Terra                  |
|      26 | GND                     | Alimentação      | Terra                  |
|      27 | CSI0_B1_LN1_M           | MIPI D-PHY | Dados CSI01 −            |
|      28 | CSI1_B2_LN3_P           | MIPI D-PHY | Dados CSI13 +            |
|      29 | CSI0_A1_LN1_P           | MIPI D-PHY | Dados CSI01 +            |
|      30 | CSI1_C2_LN3_M           | MIPI D-PHY | Dados CSI13 −            |
|      31 | GND                     | Alimentação      | Terra                  |
|      32 | GND                     | Alimentação      | Terra                  |
|      33 | CSI0_A0_CLK_M           | MIPI D-PHY | CSI0 clock −            |
|      34 | CSI1_C1_LN2_P           | MIPI D-PHY | CSI1 data2 +            |
|      35 | CSI0_NC_CLK_P           | MIPI D-PHY | Relógio CSI0 +            |
|      36 | CSI1_A2_LN2_M           | MIPI D-PHY | Dados CSI12 −            |
|      37 | GND                     | Alimentação      | Terra                  |
|      38 | GND                     | Alimentação      | Terra                  |
|      39 | CSI0_A2_LN2_M           | MIPI D-PHY | CSI0 dados2 −            |
|      40 | CSI1_NC_CLK_P           | MIPI D-PHY | CSI1 relógio +            |
|      41 | CSI0_C1_LN2_P           | MIPI D-PHY | Dados CSI02 +            |
|      42 | CSI1_A0_CLK_M           | MIPI D-PHY | Relógio CSI1 −            |
|      43 | GND                     | Alimentação      | Terra                  |
|      44 | GND                     | Alimentação      | Terra                  |
|      45 | CSI0_C2_LN3_M           | MIPI D-PHY | CSI0 dados3 −            |
|      46 | CSI1_A1_LN1_P           | MIPI D-PHY | CSI1 dados1 +            |
|      47 | CSI0_B2_LN3_P           | MIPI D-PHY | Dados CSI0 3 +            |
|      48 | CSI1_B1_LN1_M           | MIPI D-PHY | Dados CSI1 1 −            |
|      49 | GND                     | Alimentação      | Terra                  |
|      50 | GND                     | Alimentação      | Terra                  |
|      51 | CCI_I2C_SCL0 (GPIO_23)  | 1,8 V MPU   | Controlo da câmara I²C SCL0 |
|      52 | CSI1_B0_LN0_P           | MIPI D-PHY | Dados CSI10 +            |
|      53 | CCI_I2C_SDA0 (GPIO_22)  | 1,8 V MPU   | Controlo da câmara I²C SDA0 |
|      54 | CSI1_C0_LN0_M           | MIPI D-PHY | Dados CSI10 −            |
|      55 | GND                     | Alimentação      | Terra                  |
|      56 | GND                     | Alimentação      | Terra                  |
|      57 | VIN (IN)                | Alimentação      | Entrada 7-24 V            |
|      58 | +3V3 (OUT)              | Alimentação      | Saída de alimentação de 3,3 V         |
|      59 | VIN (IN)                | Alimentação      | Entrada de 7-24 V            |
|      60 | +3V3 (OUT)              | Alimentação      | Saída de alimentação de 3,3 V         |



<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Observação: as pistas MIPI CSI/DSI são pares diferenciais D-PHY e não E/S de uso geral. As linhas de controle (CCI_I2C_*, SOC_CAM_MCLK*) são do domínio MPU de 1,8 V. VIN no JMEDIA é a entrada bruta de 7-24 V (apenas alimentação).
</div>

<div style="page-break-after: always;"></div>

### Qwiic (A4) (QWIIC1) - Mapa De Pin


| **Pin** | **Designação** | **Rede/Função** | **Domínio** | **Notas**                |
|--------:|-----------------|--------------------|------------|--------------------------|
|       1 | GND             | Terra             | Alimentação      | -                        |
|       2 | +3V3 OUT        | PWR_3P3V           | Alimentação      | Alimentação para dispositivos Qwiic |
|       3 | SDA             | PD13 (I2C4_SDA)    | 3,3 V      | -                        |
|       4 | SCL             | PD12 (I2C4_SCL)    | 3,3 V      | -                        |



### JSPI (A5) (JSPI1) - Mapa De Pin

| **Pin** | **Designação** | **Rede/Função** | **Domínio** | **Notas**  |
|--------:|-----------------|--------------------|------------|------------|
|       1 | MISO            | PC2 (SPI2_MISO)    | 3,3 V      | -          |
|       2 | +5V             | 5V_USB_VBUS        | Alimentação      | Apenas alimentação |
|       3 | SCK             | PD1 (SPI2_SCK)     | 3,3 V      | -          |
|       4 | MOSI            | PC3 (SPI2_MOSI)    | 3,3 V      | -          |
|       5 | RESET           | MCU_NRST           | 3,3 V      | -          |
|       6 | GND             | Terra             | Alimentação      | -          |


### JCTL (A1) (JCTL1) - Mapa De Pin


| **Pin** | **Designação** | **Rede/Função**        | **Domínio** | **Observações**          |
|--------:|-----------------|---------------------------|------------|--------------------|
|       1 | GND             | Terra                    | Alimentação      | -                  |
|       2 | USB_BOOT        | Bootstrap                | 1,8 V      | -                  |
|       3 | VOL_DOWN        | GPIO_36                   | 1,8 V      | GPIO               |
|       4 | SOC_SE4_TX      | Console UART TX (SE4)     | 1,8 V      | Console do sistema     |
|       5 | VOL_UP          | GPIO_96                   | 1,8 V      | GPIO               |
|       6 | SOC_SE4_RX      | Console UART RX (SE4)     | 1,8 V      | Console do sistema     |
|       7 | GND             | Terra                    | Alimentação      | -                  |
|       8 | PMIC_RESET      | Reinicialização PM4125              | 1,8 V      | -                  |
|       9 | +1V8 OUT        | VREG_L15A_1P8V            | Alimentação      | Referência de 1,8 V    |
|      10 | VBUS_DISABLE    | Desativação do interruptor de alimentação VBUS | 1,8 V      | Controla o caminho VBUS |

<div style="page-break-after: always;"></div>

### JDIGITAL (A2) (JDIGITAL1) - Mapa De Pin

| **Pino** | **Designação** | **Pino MCU** | **Funções**                                     | **Domínio** | **Notas**                                    |
| -------: | -------------- | ------------ | ----------------------------------------------- | ----------- | -------------------------------------------- |
|        1 | D0             | PB7          | - USART1_RX <br></br>- TIM4_CH2                 | 3,3 V       | UART                                         |
|        2 | D1             | PB6          | - USART1_TX <br></br>- TIM4_CH1                 | 3,3 V       | UART                                         |
|        3 | D2             | PB3          | - TIM2_CH2                                      | 3,3 V       | -                                            |
|        4 | ~D3            | PB0          | - OPAMP2_OUTPUT <br></br>- TIM3_CH3             | 3.3 V       | PWM / não é tolerante a 5 V                  |
|        5 | D4             | PA12         | - FDCAN1_TX <br></br>- TIM1_ETR                 | 3,3 V       | -                                            |
|        6 | ~D5            | PA11         | - FDCAN1_RX <br></br>- TIM1_CH4                 | 3,3 V       | PWM                                          |
|        7 | ~D6            | PB1          | - TIM3_CH4                                      | 3,3 V       | PWM                                          |
|        8 | D7             | PB2          | - TIM8_CH4N                                     | 3,3 V       | -                                            |
|        9 | D8             | PB4          | - TIM3_CH1                                      | 3,3 V       | -                                            |
|       10 | ~D9            | PB8          | - TIM4_CH3                                      | 3,3 V       | PWM                                          |
|       11 | ~D10           | PB9          | - SPI2_SS (Seleção de Chip) <br></br>- TIM4_CH4 | 3,3 V       | PWM                                          |
|       12 | ~D11           | PB15         | - SPI2_MOSI <br></br>- TIM1_CH3N                | 3,3 V       | PWM                                          |
|       13 | D12            | PB14         | - SPI2_MISO <br></br>- TIM1_CH2N                | 3,3 V       | -                                            |
|       14 | D13            | PB13         | - SPI2_SCK <br></br>- TIM1_CH1N                 | 3,3 V       | -                                            |
|       15 | GND            | -            | - Terra                                         | Alimentação | -                                            |
|       16 | AREF           | -            | - Referência analógica                          | -           | Pino de referência analógica (não é um GPIO) |
|       17 | D20            | PB11         | - I2C2_SDA <br></br>- TIM2_CH4                  | 3,3 V       | -                                            |
|       18 | D21            | PB10         | - I2C2_SCL <br></br>- TIM2_CH3                  | 3,3 V       | -                                            |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
Todas as linhas do JDIGITAL operam com lógica de 3,3 V. A maioria dos pinos usa uma estrutura de E/S do tipo FT e tolera 5 V como entrada. O D3 (PB0) usa uma estrutura de E/S do tipo TT e tolera apenas 3,6 V; não apliques 5 V a este pino em nenhum modo.
</div>

### JANALOG (A3) (JANALOG1) - Mapa De Pin


| **Pin** | **Designação** | **Pin de rede/MCU** | **Funções**                                            | **Domínio**     | **Notas**                     |
|--------:|-----------------|-------------------|----------------------------------------------------------|----------------|-------------------------------|
|       1 | BOOT            | MCU_BOOT0         | - Bootstrap                                             | 3,3 V          | -                             |
|       2 | IOREF           | PWR_3P3V          | - Referência de tensão de E/S (espelha o trilho de 3,3 V)             | Alimentação          | Apenas saída; não retroalimentar |
|       3 | RESET           | MCU_NRST          | - Reinicialização da MCU                                              | 3,3 V          | -                             |
|       4 | +3V3 OUT        | PWR_3P3V          | - Alimentação de 3,3 V                                           | Alimentação          | -                             |
|       5 | +5V USB VBUS    | 5V_USB_VBUS       | - Alimentação de 5 V (passagem)                              | Alimentação          | Apenas alimentação                    |
|       6 | GND             | GND               | - Terra                                                 | Alimentação          | -                             |
|       7 | GND             | GND               | - Terra                                                 | Alimentação          | -                             |
|       8 | VIN IN          | DC_IN             | - Entrada de 7-24 V                                           | Alimentação          | Apenas alimentação                    |
|       9 | A0 / D14        | PA4               | - Entrada ADC <br></br>- DAC0 <br></br>- TIM2_CH1          | Analógico / 3,3 V | ADC direto / não tolerante a 5 V |
|      10 | A1 /  D15       | PA5               | - Entrada ADC <br></br>- DAC1 <br></br>- TIM3_CH1          | Analógico / 3,3 V | ADC direto / não tolerante a 5 V |
|      11 | A2 /  D16       | PA6               | - Entrada ADC <br></br>- OPAMP2_INPUT+ <br></br>- TIM3_CH2 | Analógico / 3,3 V |                               |
|      12 | A3 /  D17       | PA7               | - Entrada ADC <br></br>- OPAMP2_INPUT−                     | Analógico / 3,3 V | -                             |
|      13 | A4 /  D18       | PC1               | - Entrada ADC <br></br>- I2C3_SDA <br></br>- LPTIM1_CH1    | Analógico / 3,3 V | -                             |
|      14 | A5 /  D19       | PC0               | - Entrada ADC <br></br>- I2C3_SCL <br></br>- LPTIM1_IN1    | Analógico / 3,3 V | -                             |


<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  A0 (PA4) e A1 (PA5) são entradas ADC diretas do STM32U585 referenciadas a <code>VREF+</code>. Elas não são tolerantes a 5 V. A faixa de entrada válida é <code>0-VREF+</code> (≈3,3 V). O máximo absoluto no pino é <code>VDD + 0,3 V</code>, aproximadamente 3,6 V. Acima deste nível, os díodos de proteção internos do MCU começam a conduzir. O conector também fornece pinos de alimentação <code>5V_SYS</code> e <code>PWR_3P3V</code>, que se destinam apenas à alimentação. Não aplique 5 V a <strong>A0</strong> ou <strong>A1</strong>. O IOREF está ligado ao trilho de 3,3 V (<code>PWR_3P3V</code>) e é fornecido como referência/saída para blindagens. Não deve ser utilizado para alimentar energia de volta à placa.
</div>

## Periféricos Alta Velocidade

- **USB-C:** USB 3.1 com capacidades de troca de funções. Modo alternativo DisplayPort através da ponte ANX7625 DSI-para-DP. Os pares diferenciais SuperSpeed do conector são partilhados entre o modo alternativo DP e os dados USB 3.1. Quando o modo alternativo DisplayPort está ativo, a velocidade dos dados USB é reduzida.

- **Câmara:** Quatro vias **MIPI-CSI-2** (1,8 V I/O).

- **Ecrã:** **MIPI-DSI** de quatro vias para **ANX7625** para DisplayPort Alt-Mode em USB-C. Ao operar no modo Single-Board Computer (SBC), a placa suporta ecrãs Full HD (1920 × 1080p) com resolução ideal de 1280 × 720p.

- **Wireless:** Wi-Fi® de banda dupla (802.11a/b/g/n/ac) e Bluetooth® 5.1 num módulo partilhado.

<div style="page-break-after: always;"></div>

## Operação Do Dispositivo

### Introdução - Arduino App Lab

O Arduino App Lab [1] é um editor unificado que cria e executa projetos em ambos os processadores da placa. Um projeto é um **App** que pode incluir: 

- Um programa Python® que é executado no sistema Linux (Qualcomm Dragonwing™ QRB2210)
- Um sketch Arduino que é executado no microcontrolador (MCU) (STM32U585)
- **Brick** opcional (serviços pré-empacotados, como modelos de IA, servidores web ou clientes API) que são implementados juntamente com a App (também executados no sistema Linux).

Os aplicativos utilizam o **Bridge** para trocar dados entre o lado Linux e o microcontrolador.

O Arduino App Lab pode ser instalado no seu PC ou executado diretamente no UNO Q no modo Computador de Placa Única. Para esta configuração, recomenda-se a variante LPDDR4X de 4 GB do UNO Q para garantir memória suficiente para uma operação estável e aplicações que exigem muitos recursos. Para utilizar a placa: 

- Inicie um exemplo pronto a utilizar no Arduino App Lab, personalize-o de acordo com as suas necessidades ou crie uma nova App  a partir do zero utilizando o editor integrado.
- Pressione o botão **Run** no Arduino App Lab [1].
- O editor cria o componente Linux, grava o sketch da MCU, implementa qualquer Brick selecionado e inicia tudo na placa.
- Os registos de ambos os lados estão disponíveis no editor e pode iterar sem sair do Arduino App Lab.

Para a primeira configuração:

1. Instale o Arduino App Lab [1], inicie-o e conecte o UNO Q, utilize um cabo de dados USB-C para o modo hospedado no PC ou simplesmente ligue a placa para o modo SBC.
2. A placa verificará automaticamente se há atualizações. Se houver atualizações disponíveis, será solicitado que as instale. Quando a atualização estiver concluída, o Arduino App Lab [1] precisará ser reiniciado.
3. Durante a primeira configuração, será solicitado que forneça um nome e uma palavra-passe para o dispositivo. Também será solicitado que forneça as credenciais Wi-Fi® da sua rede local.
4. Para testar a placa, navegue até um aplicativo de exemplo na seção **"Examples"** do Arduino App Lab[1] e clique no botão "Run" no canto superior direito. Você também pode criar um novo aplicativo na seção **"App"**.
5. O status do App pode ser monitorado na guia do console do App.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;"> <p style="text-align: justify;">
  <strong>Observação:</strong> No modo <strong>Hospedado no PC</strong>, é necessária uma conexão <em>de dados USB</em> para a configuração inicial. Posteriormente, é possível utilizar o destino <strong>Rede</strong> através da LAN (SSH). No modo <strong>Computador de placa única (SBC)</strong>, não é necessário um link de dados USB para a configuração, basta ligar a placa e utilizar o destino <strong>Rede</strong> assim que ela se juntar à sua rede. Para periféricos no modo SBC (teclado, rato, câmara USB, microfone), utilize um dongle USB-C com capacidade de fornecimento de energia externa. Quando o DisplayPort Alt-Mode está ativo, a velocidade dos dados USB é reduzida.
  </p>
</div>

Utilize uma fonte e um cabo USB-C de 5 V / 3 A ou alimente a partir dos pinos de 5 V ou VIN, conforme especificado na [secção de alimentação de entrada](#input-power) (USB-C é apenas 5 V / VIN é 7-24 V).

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  A primeira inicialização normalmente leva de 20 a 30 segundos enquanto o Linux é iniciado. Aguarde a sequência do LED de inicialização ou a animação da matriz de LED terminar antes de interagir com a placa.
</div>

### Bricks

<p style="text-align: justify;"><strong>Bricks</strong> são blocos de construção modulares no Arduino App Lab que permitem ampliar a sua App sem precisar escrever toda a infraestrutura subjacente. Cada Brick encapsula funcionalidades prontas, como integração de sensores, modelos de IA, bases de dados ou interfaces de utilizador, que podem ser inseridas em um projeto. Os Bricks típicos fornecem:</p>

<ul>
  <li>Um modelo de IA (por exemplo, classificação de objetos ou deteção de palavras-chave)</li>
  <li>Uma interface de utilizador web ou serviço REST API</li>
  <li>Uma integração com uma fonte de dados externa</li>
</ul>

<p style="text-align: justify;">Os Bricks são implementados juntamente com a App e geridos pelo lado Linux. O fluxo de trabalho típico é:</p>

<ol>
  <li>Crie um <strong>App</strong> no Arduino App Lab.</li>
  <li>Selecione qualquer <strong>Brick</strong> que o App deva utilizar.</li>
  <li>Adicione o seu código Python® (Linux) e/ou o seu sketch Arduino (MCU).</li>
  <li>O Brick precisa ser importado para o seu ficheiro `main.py` e inicializado seguindo a API do Brick.</li>
  <li>Pressione <strong>Run</strong> para implementar a aplicação Linux, atualizar a MCU e iniciar a sua aplicação juntamente com os seus Brick.</li>
  <li>A ferramenta <strong>Bridge</strong> lida com a troca de dados entre o Linux e o MCU.</li>
</ol>


<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Enquanto uma aplicação está vinculada e em execução, as interfaces USB podem estar ocupadas pelo sistema. Utilize o Arduino App Lab [1] para implementar e monitorizar. Para utilizar ferramentas CLI externas via USB, interrompa a aplicação ou desconecte a placa.
</div>

### Hello World

<p style="text-align: justify;">Vamos programar o UNO Q com o clássico "Hello World" do Arduino - o exemplo <em>Blink LED</em>. Isso ajuda a verificar se a placa está conectada corretamente ao Arduino App Lab.</p>

<ol>
  <li>Abra o Arduino App Lab. Ele inicia na secção <strong>Examples</strong>.</li>
  <li>Se não estiver a utilizar o modo de computador de placa única, <strong>conecte o UNO Q</strong> ao seu PC.</li>
  <li>Abra <em>Blink LED</em>. Reveja as notas do exemplo para ver como o App  funciona.</li>
  <li>Clique em <strong>Run</strong> e aguarde a conclusão do upload.</li>
</ol>
<p style="text-align: justify;">Agora deve ver o canal vermelho do LED RGB integrado acender por um segundo e, em seguida, apagar por um segundo, repetidamente. O LED é acionado pelo microcontrolador STM32U585 através do Arduino sketch.</p>

<p style="text-align: justify;">Pode começar com um App  em branco ou utilizar um exemplo existente. Para o primeiro uso, recomenda-se o exemplo Hello World para aprender a estrutura básica.</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  Sempre que executa uma aplicação, o sketch do microcontrolador é compilado e a aplicação Python® é iniciada no sistema Linux. Dependendo da complexidade, isso pode demorar até um minuto.
</div>

### Como Verificar Se O App Está Em Execução

<p style="text-align: justify;">Abra o <strong>Console</strong> no App Lab. Existem três guias:</p>

<ul>
  <li><strong>Inicialização</strong>: registos da sequência de inicialização, incluindo compilação do MCU e implementação do Linux</li>
  <li><strong>Principal (Python®)</strong>: saída do aplicativo Python® (<code>print()</code>)</li>
  <li><strong>Sketch (Microcontrolador)</strong>: saída serial do Arduino sketch(<code>Serial.println()</code>)</li>
</ul>

<p style="text-align: justify;">Uma aplicação pode ser iniciada com sucesso, mas ainda assim apresentar problemas de tempo de execução. Verifique se há erros no log do Python®. Se ocorrer um erro de compilação do sketch, o início será abortado.</p>

<div style="page-break-after: always;"></div>

### Botão De Alimentação

<p style="text-align: justify;">O UNO Q inclui um <strong>botão liga/desliga (JBTN1)</strong> que pode ser utilizado para reiniciar a placa. </p>

![Botão de alimentação do UNO Q](assets/ABX00162-ABX00173-power-button.png)

<strong>Pressione longamente (≥ 5 s):</strong> reinicia o sistema Linux (MPU). Isso não corta a energia da placa.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Observação:</strong> uma reinicialização com pressão longa reinicia o ambiente Linux e pode interromper os App em execução. Salve o trabalho e garanta o encerramento seguro dos processos externos, quando aplicável. A placa inicializa automaticamente quando a energia é fornecida. Não é necessário pressionar o botão para uma inicialização normal.
</div>

### Recursos Online

<p style="text-align: justify;">Explore projetos da comunidade no Project Hub [3], navegue pela Biblioteca de Referência [4] para APIs suportadas e encontre acessórios como sensores Qwiic, UNO Shield e placas carrier na Arduino Store [5].</p>

## Informações Mecânicas

<p style="text-align: justify;">A placa mede 68,58 mm × 53,34 mm, com as partes inferiores mantidas abaixo de 2 mm para que a placa possa ser empilhada em bases de carrier. O contorno e o padrão de orifícios seguem e são compatíveis com o formato UNO.</p>

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
