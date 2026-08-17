---
identifier: ABX00162-ABX00173
title: Arduino® UNO Q
type: maker
---

# 中文

![](assets/featured.png)

# 描述

<p style="text-align: justify;">Arduino® UNO Q（以下简称UNO Q）是一款单板计算机，Qualcomm® Dragonwing™ QRB2210 微处理器（MPU）、 四核Arm® Cortex®-A53处理器 运行Debian Linux操作系统，以及意法半导体STM32U585微控制器（MCU）——该MCU基于Arm® Cortex®-M33架构，运行Zephyr OS上的Arduino核心。Linux系统与微控制器通过Arduino的RPC（远程过程调用）库Bridge进行通信。这使得微控制器上的Arduino程序能够调用Linux服务完成高级任务，同时Linux应用程序可与微控制器外设交互，在同一项目中处理实时操作。</p>

<p style="text-align: justify;">UNO Q 配备嵌入式 eMMC 存储（可选 16 GB 或 32 GB）和 LPDDR4X SDRAM（可选 2 GB 或 4 GB），可流畅运行 Linux 系统及您的项目。该开发板支持双频Wi-Fi® 5和Bluetooth® 5.1蓝牙模块实现无线连接，配备支持电源输入与视频输出的USB-C®接口，并提供兼容Arduino的扩展接口，便于通过扩展板、载体板及配件进行功能扩展。</p>

<p style="text-align: justify;">UNO Q与Arduino App Lab无缝集成，使开发者能够在一个环境中同时运行Arduino程序、Linux应用程序和AI模型。App Lab既可直接在开发板上运行，也可通过连接的电脑运行，提供现成的示例程序，并支持灵活创建定制应用程序以满足项目需求。
</p>

# 目标领域

原型设计、边缘人工智能与机器学习、机器视觉、教育、智能设备、机器人技术、家庭与建筑自动化、游戏

<div style="page-break-after: always;"></div>

# 目录

## 应用示例

<p style="text-align: justify;">UNO Q融合了具备AI能力的Linux处理器与实时微控制器，实现了高级计算与确定性控制的完美结合。凭借这种双架构设计，它兼容广泛的生态系统，包括Arduino扩展板、载体板、Modulino®节点及第三方配件，成为适用于多样化应用的灵活平台。
</p>

- **原型设计:** 快速实现概念验证，例如基于视觉的检测工具、智能自助终端或内置连接功能的紧凑型边缘计算机。

- **教育应用:** 通过项目式学习教授Linux、实时编程、人工智能及计算机视觉，涵盖科学实验到交互式教育机器人等领域。

- **机器人技术:** 融合Linux视觉与MCU驱动电机控制的自主配送机器人、手势跟随伴侣机器人及具备视觉反馈的机械臂。

- **智能消费设备:** 搭载双摄像头与GPU加速的DIY智能相机、交互式显示屏或AR项目。

- **家居与建筑自动化:** 配备人脸识别功能的智能门铃、语音控制系统及个性化气候控制中心。

- **游戏领域:** 复古主机模拟器、定制街机柜，或通过手势控制、面部追踪及实时反馈增强游戏体验。

<div style="page-break-after: always;"></div>

## 特点

### UNO Q 型号

UNO Q 提供两种型号：

- **ABX00162**：2 GB 内存，16 GB 板载存储
- **ABX00173**：4 GB 内存，32 GB 板载存储

### 一般规格概述

#### 处理器与内存

![](assets/ABX00162-ABX00173-main-components.png)

| **子系统**   | **详细信息**                                                 |
| ------------ | ------------------------------------------------------------ |
| 主MPU        | - Qualcomm Dragonwing™ QRB2210 - 系统级芯片 (SoC) (MPU) (SOC1): 4 × Arm Cortex-A53 @ 2.0 GHz, 64位<br></br>- Adreno 702 GPU @ 845 MHz 3D图形处理 <br></br>- Dual ISPs: 13 MP + 13 MP 或 25 MP @ 30 fps <br></br>- Debian操作系统（上游支持）<br></br>- I/O：USB 3.1接口支持USB连接器角色切换功能，SDIO 3.0，4通道MIPI-CSI-2及4通道MIPI-DSI |
| 实时时钟 MCU | - ST STM32U585 (MCU) (MCU1)，Arm Cortex-M33 最高160 MHz <br></br>- Zephyr OS上的Arduino核心 <br></br>- 2 MB闪存，786 kB SRAM |
| 系统内存     | - eMMC 16或32 GB选项（EMMC1）用于操作系统/数据存储 <br></br>- LPDDR4X 2GB或4 GB选项（单通道，32位）（DRAM1） |

<p style="text-align: justify;">Qualcomm Dragonwing™ QRB2210 I/O工作电压为1.8V。该MPU驱动JMEDIA上的MIPI-CSI-2摄像头接口与MIPI-DSI显示接口，同时通过JMISC引出1.8V MPU（SoC）GPIO及音频端点。JMISC为混合电压接口，除1.8V MPU线路外，同时承载3.3V MCU信号及模拟音频。显示端口视频由板载ANX7625提供，该芯片将MPU的MIPI-DSI信号转换为USB-C接口的DisplayPort替代模式。STM32U585芯片管理ADC、PWM、CAN、LED矩阵及3.3V接口（JDIGITAL、JANALOG、JSPI和Qwiic）。</p>


#### 连接性与媒体

![](assets/ABX00162-ABX00173-comm-components.png)

<<<<<<< PXCT-1634-UNO-Q-Zh+PT
| **子系统**                                                   | **详细信息**                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 无线模块                                                     | - WCBN3536A（Qualcomm WCN3980）（U2901）<br></br>- Wi-Fi® 5 802.11a/b/g/n/ac（双频）+ Bluetooth® 5.1 |
| USB-C 接口 (JUSB1)                                           | - 具备角色切换功能的USB 3.1 <br></br>- 通过ANX7625 DSI转DP桥接器实现DisplayPort替代模式（U3001） |
| (Type-C接口的超高速差分对专用于DP替代模式)<br></br> - USB电源传输协议仅支持**5V/3A**供电协议（不支持更高电压配置文件）<br></br>- VBUS负载开关/背驱动保护（Q2801） |                                                              |


无线模块采用SDIO传输Wi-Fi®数据，通过UART控制Bluetooth®蓝牙模块功能，并共享PCB天线。

#### 扩展与头

![](assets/ABX00162-ABX00173-header-expansion.png)

| **接口 (连接器)**    | **电压与引脚数量**                        | **详细信息**                                                 |
| -------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| JMEDIA (JMEDIA1)     | 1.8 V 信号, 60 引脚                       | - 高速摄像头/显示通道（MIPI DSI、CSI）<br></br>- 摄像头控制总线（CCI I2C）-<br></br> 专用接口，非通用GPIO- 摄像头时钟（SOC_CAM_MCLK0/1）<br></br>- 同时承载电源轨（+3V3 OUT、VIN IN）及地线（GND） |
| JMISC (JMISC1)       | 混合 1.8 V / 3.3 V, 60 引脚               | - 混合GPIO和SDIO <br></br>- MCU外设：SDMMC1、TRACE、PSSI（并行摄像头）、I2C4、MCO/CRS_SYNC、运算放大器1引脚 <br></br>- 音频端点： 麦克风2输入/负反馈/偏置、耳机L/R+参考、线路输出P/M、听筒P/R、耳机检测器 HS_DET<br></br>- MPU（SoC）GPIO银行（SE0）工作于1.8V <br></br>- 同时承载电源轨（+5V USB输出、+3.3V输出、+1.8V输出、电池电压输出、硬币电压输入）及地线 (GND) |
| JCTL (JCTL1)         | 1.8 V, 10 引脚                            | - SE4 UART控制台 <br></br>- 强制USB启动输入<br></br> - PMIC复位输入 <br></br>- VBUS电源开关禁用<br></br> - 1.8V电源轨及接地 |
| JDIGITAL (JDIGITAL1) | 3.3 V, 18 引脚                            | - 用于SPI、I2C、UART、PWM、CAN的数字I/O                      |
| JANALOG (JANALOG1)   | 3.3 V, 14 引脚                            | - 模拟I/O<br></br> - ADC通道及基准电压                       |
| JSPI (JSPI1)         | 3.3 V 数字逻辑电压参考, 6 引脚 + 5 V VBUS | - 专用SPI：MOSI、MISO、SCLK- MCU复位（NRST）- 接地- 5V VBUS（USB供电） |
| Qwiic (QWIIC1)       | 3.3 V, 4 引脚                             | - I2C（Qwiic生态系统）                                       |

### 相关产品

- 通过JDIGITAL和JANALOG实现的Arduino UNO扩展板
- 兼容UNO Q的载体板
- 全规格24针USB-C线缆
- 具备外接电源传输功能的USB-C转接头

<div style="page-break-after: always;"></div>

## 额定值

### 输入电源

![UNO Q Input Methods](assets/ABX00162-ABX00173-power-supply.png)

| **源电流**  | **工作电压** | **最大限值** | **连接器**            |
| ----------- | -----------: | -----------: | --------------------- |
| USB-C VBUS  |          5 V |   高达3 A 位 | USB-C  连接器         |
| VIN (DC IN) |       7-24 V |            - | JMEDIA, JANALOG (VIN) |
| 5 V 引脚    |          5 V |   高达3 A 位 | JANALOG               |

<p style="text-align: justify;">UNO Q支持双电源输入：USB-C接口和7-24V直流输入。通过USB电源传输协议时，仅请求5V/3A供电协议，不请求更高电压的PD配置文件。请使用额定5V/3A的电源线和线缆，以避免在无线传输突发或显示初始化等短时活动高峰期间出现欠压情况。也可通过JANALOG接头上的5V引脚，使用稳压外部5V直流电源为电路板供电。
</p>

<p style="text-align: justify;"><em>USB-C VBUS</em>与7-24V降压稳压器的5V输出经<em>二极管</em>或门组合接入系统5V总线（<code>5V_SYS</code>）。设计从<code>5V_SYS</code>衍生出3.8V预稳压节点，进而生成3.3V电源。由5V_SYS供电的PMIC则衍生出1.8V电源轨。</p>

<p style="text-align: justify;"><strong>反极性保护：</strong>经直流输入端施加-24V电压验证。本器件仅在正确极性条件下保证工作特性。正常使用时请勿施加反向电压。
</p>

<p style="text-align: justify;"><strong>肖特基或路径</strong>：从降压输出到<code>5V_SYS</code>的正向电压降测量如下（JANALOG VIN注入，Rigol DP832电源串联，Keithley DMM6500测量，8542B有源负载）。功耗按<code>P = I × Vf</code>计算。</p>

| **负载电流** | **正向压降 (`Vf`)** | **二极管功耗** |
| -----------: | ------------------: | -------------: |
|        1.0 A |              0.35 V |         0.35 W |
|        1.5 A |              0.37 V |         0.56 W |
|        2.0 A |              0.39 V |         0.78 W |

### 建议运行条件

使用以下限制来确定电源规格、定义电源轨容差并规划热余量：

| **参数**     | **符号**    | **最小值** | **输出功率典型值** | **最大限值** | **单位** |
| ------------ | ----------- | :--------: | :----------------: | :----------: | :------: |
| USB-C 输入   | `VBUS_USBC` |    4.5     |        5.0         |     5.5      |    V     |
| DC 输入      | `DC_IN`     |    7.0     |         -          |     24.0     |    V     |
| 3.3 V 电源轨 | `PWR_3P3V`  |    3.1     |        3.3         |     3.5      |    V     |
| 工作温度     | `T_OP`      |    -10     |         -          |      60      |    °C    |

<p style="text-align: justify;"><em>2最小值</em>表示常规操作的最低持续值；短暂跌压可能导致重置或链路中断。<em>典型值</em>为设计标称点。<em>最大值</em>不可逾越。对于<code>DC_IN</code>（7-24 V），应选用能轻松满足5 V负载需求的电源，并使用短电缆以减少压降。<code>PWR_3P3V</code>范围反映稳压器容差与负载特性。温度范围指电路板附近环境空气温度，在临界值附近运行可能降低可用输出电流。</p>

### 板载电压轨

| **工作电压** | **电源轨**       | **原点 / 调节器**                                            |
| -----------: | ---------------- | ------------------------------------------------------------ |
|        5.0 V | `5V_SYS`         | USB-C VBUS与7-24V降压输出（均通过肖特基整流器）的二极管或门电路 |
|        3.8 V | `PWR_3P8V`       | 降压电路（降压型）从`5V_SYS`供电                             |
|        3.3 V | `PWR_3P3V`       | 降压电路（降压型）从`PWR_3P8V`供电                           |
|        1.8 V | `VREG_L15A_1P8V` | PM4125 LDO L15A 从`5V_SYS`供电                               |

<div style="page-break-after: always;"></div>

## 功能概述

### 引脚布局

![](assets/ABX00162-ABX00173_pinout.png)

### 方框图

![](assets/ABX00162-ABX00173_block_diagram.png)

### 电源

<p style="text-align: justify;">UNO Q支持双电源输入：USB-C端口和7-24V直流输入。
<em>USB-C VBUS</em>与7-24V降压稳压器的5V输出通过<em>二极管</em>或门组合接入系统5V总线（5V_SYS）。</p>


<p style="text-align: justify;"><code>5V_SYS</code>通过<code>USB_IN</code>接口为<strong>PM4125</strong>电源管理集成电路(PMIC1)供电。
该PMIC的L15A低压差稳压器提供1.8V电源轨（<code>VREG_L15A_1P8V</code>），为SoC I/O总线、ANX7625的<code>DVDD18</code>引脚、Wi-Fi®数字逻辑电路及板载电平转换器供电。1.8 V电源轨也可通过<code>JMISC</code>接口获取。
由<code>5V_SYS</code>供电的降压电路生成<code>PWR_3P8V (3.8 V)</code>电源，该电源专用于系统设计及未来功能扩展。
第二个降压电路生成<code>PWR_3P3V</code>，为STM32U585、ANX7625（3.3V电源轨）、Wi-Fi® 3.3V域及3.3V接头引脚供电。</p>


<p style="text-align: justify;">当板卡作为USB主机/OTG运行时，<em>受保护的P沟道MOSFET</em>（<code>Q2801</code>）可从<code>5V_SYS</code>为USB <code>VBUS</code>供电。<code>VCOIN</code>仅为PMIC的实时时钟供电，不为Linux或MCU域供电。<code>VBAT</code> 连接到 <code>PWR_3P8V</code>，该引脚保留用于系统设计和未来功能扩展。</p>

![Arduino UNO Q Power Tree](assets/ABX00162-ABX00173_power_tree.png)

<div style="page-break-after: always;"></div>

## 用户界面与指示器

![](assets/ABX00162-ABX00173-leds.png)

- **RGB LED(Linux控制):** 两颗三色LED由Qualcomm Dragonwing™ QRB2210应用处理器驱动，并通过`/sys/class/leds/`路径暴露。

  - **RGB LED 1 (D27301):** 通道配置：`red:user` → **GPIO_41**，`green:user` → **GPIO_42**，`blue:use` → **GPIO_60**。

  - **RGB LED 2 (D27302):** 通道配置：`red:panic` → **GPIO_39**，`green:wlan` → **GPIO_40**，`blue:bt` → **GPIO_47**。

    默认情况下，RGB LED 2 指示系统状态、`PANIC`、`WLAN` 和 `BT`，但也可由用户控制。PWM 频率约为 2 kHz，以实现平滑的色彩过渡。

- **RGB LED (MCU控制):** 两个三色LED由STM32U585驱动。

  - **RGB LED 3 (D27401):** `LED3_R` → **PH10**, `LED3_G` → **PH11**, `LED3_B` → **PH12**。
  - **RGB LED 4 (D27402):** `LED4_R` → **PH13**, `LED4_G` → **PH14**, `LED4_B` → **PH15**。

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  RGB LED为低电平有效，即逻辑`0`时点亮。
</div>

- **LED矩阵 (D27001..D27104):** 由STM32U585驱动的8×13单色蓝色LED矩阵（104像素）。在Linux启动过程中，该矩阵会显示启动徽标约20–30秒。启动完成前访问该矩阵可能干扰MCU运行。

- **电源指示灯 (D27201):** 绿色指示灯连接至3.3V电源轨，当电路板通电时始终亮起。

## MPU & MCU

<p style="text-align: justify;">
MPU（微处理器单元）是一种高性能应用处理器，专为运行完整操作系统和复杂软件而设计。MCU（微控制器单元）则是小型节能控制器，专注于实现I/O与控制的快速精准时序。UNO Q将二者融合，在单板上实现操作系统级计算与响应迅速的时序控制，并通过双向实现的RPC层Bridge进行通信。</p>

### 应用处理器（MPU）

<p style="text-align: justify;">Qualcomm® Dragonwing™ QRB2210是一款搭载Debian Linux操作系统的四核Arm® Cortex®-A53处理器。其I/O接口工作电压为1.8V，可处理高速媒体传输及Type-C/PD电源管理策略。
</p>

<ul>
  <li>电压域：1.8 V 供电（用于 SoC 的 MPU GPIO 及高速接口）</li> <li>驱动 JMEDIA：MIPI-CSI-2 相机通道与 MIPI-DSI 显示通道</li><li>驱动 1.8 V MPU GPIO 及 JMISC（混合电压接口）上的音频端点</li><li>USB-C：角色切换与 PD 协商（请求 5 V / 3 A）</li> <li>通过板载ANX7625实现DisplayPort输出（将MIPI-DSI转换为DP替代模式）</li>
</ul>

### 实时微控制器（MCU）

<p style="text-align: justify;">
意法半导体® STM32U585是一款基于Arm® Cortex®-M33架构的微控制器，在Zephyr OS系统上运行Arduino核心。它为控制任务提供快速精准的定时功能，并配备3.3 V I/O接口。
</p>


<ul>
  <li>电压域：GPIO和模拟信号为3.3 V (VREF+ ≈ 3.3 V)</li>
  <li>管理ADC、PWM、CAN、LED矩阵、定时器</li>
  <li>支持3.3 V接口：JDIGITAL、JANALOG、JSPI、Qwiic</li>
</ul>


<p style="text-align: justify;">
JMISC同时处理两个电压域：1.8 V MPU线路与3.3 V MCU信号（如PSSI、SDMMC1、TRACE、I2C4）及模拟/音频信号并行。连接载板或外部逻辑电路时，请务必核查电压等级。
</p>


## 处理器间通信

<p style="text-align: justify;">Qualcomm® Dragonwing™ QRB2210（MPU）与 STM32U585（MCU）通过 Arduino Bridge 进行通信，该软件层在 Linux 和 MCU 两端均实现了基于软件的远程过程调用（RPC）。该桥接器提供面向服务的API，使任一处理器都能为另一处理器暴露可调用的服务，同时支持异步事件的单向通知。它管理处理器间的消息路由，并兼容多种物理传输方式。通过其API，桥接器实现类型安全的函数调用，允许微控制器程序调用Linux服务并接收结构化响应，或通过通知推送数据。</p>

<p style="text-align: justify;">若载板或外部逻辑需要硬件指示器，固件可将JMISC上的1.8V MPU GPIO或JCTL的可用GPIO指定为就绪/唤醒输出。该信号可通过电平兼容电路（如电平转换器或带上拉电阻的开漏配置）接收到MCU GPIO端口。固件将定义该信号的具体功能。另一方案是：当MCU处于睡眠模式时，选定传输通道（USB CDC、UART或SPI）的活动状态可作为唤醒源。</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  MPU GPIO信号在应用处理器的低电压域（1.8 V）内工作。确保与微控制器之间的任何连接均与其I/O电压轨（3.3 V）电平兼容。例如，可采用电平转换器或开漏配置，并通过上拉电阻连接至微控制器的I/O电压轨。
</div>
<div style="page-break-after: always;"></div>

## 硬件加速

<p style="text-align: justify;">UNO Q通过集成Adreno 702 GPU（运行频率845 MHz）为3D图形和视频编解码提供硬件加速。</p>

### 图形加速

Adreno 702 GPU通过开源Mesa驱动程序提供硬件加速的3D图形渲染。应用程序可通过标准图形API（包括OpenGL、OpenGL ES、Vulkan和OpenCL）访问GPU加速功能。

| **图形API**    | **驱动程序** | **硬件支持** | **当前驱动程序版本** | **设备名称**           |
| -------------- | ------------ | ------------ | -------------------- | ---------------------- |
| Desktop OpenGL | freedreno    | -            | 3.1                  | FD702                  |
| OpenGL ES      | freedreno    | 3.1          | 3.1                  | FD702                  |
| Vulkan         | turnip       | 1.1          | 1.0.318              | Turnip Adreno (TM) 702 |
| OpenCL         | Mesa         | 2.0          | 2.0                  | -                      |

<p style="text-align: justify;">Adreno 702 GPU采用统一内存架构，与CPU共享系统RAM进行数据传输。它支持64位内存寻址，并提供直接渲染能力以实现最佳图形性能。</p>

| **参数**               | **规格**                  |
| ---------------------- | ------------------------- |
| **时钟频率**           | 845 MHz                   |
| 内存架构               | 统一内存（与系统RAM共享） |
| 可用显存               | 1740 MB                   |
| 内存寻址               | 64-bit                    |
| 直接渲染               | 是                        |
| 最大2D纹理尺寸         | 16384 × 16384 像素        |
| 最大3D纹理尺寸         | 20483 体素                |
| 最大立方体贴图尺寸     | 16384 × 16384 像素        |
| OpenGL着色语言（GLSL） | 1.40                      |
| OpenGL ES着色语言      | 3.10 ES                   |

<p style="text-align: justify;">Mesa图形栈支持标准的OpenGL扩展功能。使用OpenGL、OpenGL ES或Vulkan的应用程序将自动启用硬件加速，无需额外配置。标准图形工具如<code>mesa-utils</code>和<code>vulkan-tools</code>在UNO Q上开箱即用。</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>注:</strong>OpenGL 和 Vulkan 驱动程序可通过开源 Mesa 驱动程序 <strong>freedreno (支持 OpenGL/OpenGL ES)</strong> 和 <strong>turnip (支持 Vulkan)</strong> 获取，这些驱动程序具有透明性并获得社区支持。尽管 Adreno 702 硬件支持 Vulkan 1.1，但当前驱动程序实现仅提供 Vulkan 1.0.318 版本。<strong>目前尚无针对 UNO Q 平台的 OpenGL 或 Vulkan 示例代码。但可参考 Mesa 项目提供的标准 Mesa 工具及示例代码</strong>。
</div>

### 视频加速

<p style="text-align: justify;">Adreno 702 GPU 包含专用硬件视频编解码器，可通过 <code>V4L2 (Video4Linux2)</code>API 经由 <code>/dev/video0</code> 和 <code>/dev/video1</code> 设备访问。以下视频编解码器支持硬件加速：</p>

| **编解码器** | **编码** | **解码** | **GStreamer元素**         |
| ------------ | -------- | -------- | ------------------------- |
| H.264 (AVC)  | 是       | 是       | v4l2h264enc / v4l2h264dec |
| H.265 (HEVC) | 是       | 是       | v4l2h265enc / v4l2h265dec |
| VP9          | 没有     | 是       | v4l2vp9dec                |

<p style="text-align: justify;">硬件视频编解码器将压缩与解压缩任务从CPU卸载至专用硬件，从而实现高效的实时视频处理。这既降低了系统功耗，又使CPU能够专注于应用逻辑。硬件加速支持最高1920×1080（全高清）分辨率，涵盖720p（1280×720）等常见格式。</p>

#### GStreamer集成

<p style="text-align: justify;">访问硬件视频加速的推荐方案是通过<strong>GStreamer</strong>实现，该框架为V4L2设备提供了高级管道接口。以下GStreamer组件支持硬件加速视频处理：</p>

H.264解码可采用以下管道：

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h264parse ! v4l2h264dec \
  ! videoconvert ! autovideosink
```

H.265解码可采用以下管道：

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.mp4 \
  ! qtdemux name=demux demux.video_0 ! queue ! h265parse ! v4l2h265dec \
  ! videoconvert ! autovideosink
```

VP9解码可采用以下管道：

```bash
gst-launch-1.0 filesrc location=videos/xxxxx.webm \
  ! matroskademux ! queue ! v4l2vp9dec \
  ! videoconvert ! autovideosink
```

对于H.264编码，可使用以下处理流程：

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc ! h264parse ! mp4mux ! filesink location=/tmp/output.mp4
```

对于H.265编码，可使用以下处理流程：

```bash
gst-launch-1.0 videotestsrc num-buffers=30 \
  ! video/x-raw,width=1920,height=1080,framerate=30/1 \
  ! v4l2h265enc ! h265parse ! mp4mux ! filesink location=/tmp/output.mp4
```

对于并发编码与解码，可以采用以下管道：

```bash
gst-launch-1.0 -v videotestsrc num-buffers=1000 \
  ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 \
  ! v4l2h264enc capture-io-mode=4 output-io-mode=2 ! h264parse \
  ! v4l2h264dec capture-io-mode=4 output-io-mode=2 ! videoconvert \
  ! autovideosink
```

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
 <strong>开发者访问</strong>：V4L2视频设备可通过标准Linux API访问，支持直接集成至使用libv4l2的C/C++应用程序，或通过具备V4L2后端支持的高级框架（如GStreamer、FFmpeg或OpenCV）进行集成。
</div>


### OpenCL支持

<p style="text-align: justify;">通过Mesa实现支持OpenCL 2.0，可为并行处理任务、科学计算及计算密集型操作提供通用GPU（GPGPU）计算能力。Adreno 702的OpenCL功能可将计算密集型工作负载从CPU卸载至GPU，从而提升性能表现。</p>

<div style="page-break-after: always;"></div>

## 外设

![UNO Q Peripherals](assets/ABX00162-ABX00173_headers.png)

- **JDIGITAL (A2) (JDIGITAL1) / JANALOG (A3) (JANALOG1)：** 3.3 V GPIO，支持 SPI、UART、CAN、PWM 和 ADC 输入。模拟输入以 3.3 V 电源轨上的 `VREF+` 为基准。有效输入范围为 0 V 至 `VREF+`。部分 STM32U585 引脚在数字模式下可耐受 5 V 电压，但当配置为 ADC 或任何模拟功能（如 *A0* 至 *A5*）时，则不耐受 5 V 电压，且电压不得超过 `VDD + 0.3 V`。若需处理更高电压，请使用分压器或缓冲器等外部调理电路。当 *A4/A5* 用作 I2C3（PC1/PC0）时，仅可使用上拉至 3.3 V。此外，**~D3 (PB0)** 采用 TT 型 I/O 结构且耐受 3.6 V，但在任何模式下（包括数字模式）均不耐受 5 V。

- **QWIIC连接器（A4）(QWIIC1):** 额外的I2C总线（3.3V逻辑）。其映射为**PD13（I2C4_SDA** 和 **PD12(I2C4_SCL)**。确保与Modulino®节点及第三方传感器和执行器的即插即用兼容性。

- **JSPI (A5) (JSPI1):** 3.3 V SPI外设接口，提供MOSI、MISO和SCLK信号，芯片选通信号通过JDIGITAL/JMISC上的GPIO引脚实现。引脚采用 STM32U585 FT 型配置：MISO 在 PC2，MOSI 在 PC3，SCK 在 PD1。输入模式或开漏状态下可耐受 5 V 电压，输出驱动 3.3 V。若需 5 V 输入阈值或 5 V 双向信号传输，请添加电平转换器。包含 `5V_SYS` 电源引脚。

- **JMEDIA (B2) (JMEDIA1):** 四通道摄像头与显示信号，工作于1.8V电压域（MIPI-CSI-2和MIPI-DSI）。

- **JMISC (B1) (JMISC):** 混合功能接口，整合3.3V MCU信号与1.8V MPU信号。提供MCU PSSI（并行摄像头）总线、SDMMC1测试引脚、TRACE、I2C4、MCO/CRS_SYNC及OPAMP1模拟引脚。同时引出音频接口（麦克风2、耳机L/R+参考电平、线路输出P/M、听筒P/R、耳机检测HS_DET）及电源轨（+3V3、+5V_USB、+1V8、系统用VBAT和VCOIN）。注意电压域：**MCU引脚为3.3V，MPU通用输入输出为1.8V**。

- **JCTL (A1) (JCTL1):** 启动模式引脚、复位信号及低功耗唤醒信号（1.8V逻辑电平）。

<p style="text-align: justify;"><strong>SE4 UART</strong>是系统控制台（<code>shell UART</code>）。它与应用程序UART独立，不应用于用户I/O。该接口运行于MPU的<strong>1.8V</strong> I/O域。</p>

<p style="text-align: justify;">请勿将 Qualcomm Dragonwing™ QRB2210专用于<strong>I2C</strong>、<strong>JMEDIA CCI</strong>（相机控制接口）或<strong>MI2S0</strong>（I2S音频总线）的线路用作通用输入输出。这些信号为专用接口，工作电压为<strong>1.8V</strong>，并在Linux设备树中被保留。接头仅为实现上述功能而暴露这些信号。</p>

### JMISC (B1) (JMISC1) - 引脚功能概述

| **引脚** | **名称**        | **MCU/SoC 引脚** | **域名** | **注释**                               |
| -------: | --------------- | ---------------- | -------- | -------------------------------------- |
|        1 | MCU_PSSI_D0     | PC6              | 3.3V MCU | PSSI D0                                |
|        2 | MCU_SDMMC1_CMD  | PD2              | 3.3V MCU | SDMMC1 CMD / 测试                      |
|        3 | MCU_PSSI_D1     | PC7              | 3.3V MCU | PSSI D1                                |
|        4 | MCU_TRACE_CLK   | PE2              | 3.3V MCU | 跟踪时钟                               |
|        5 | MCU_PSSI_D2     | PC8              | 3.3V MCU | PSSI D2                                |
|        6 | MCU_TRACE_D0    | PE3              | 3.3V MCU | 跟踪数据 0                             |
|        7 | MCU_PSSI_D3     | PC9              | 3.3V MCU | PSSI D3                                |
|        8 | MCU_TRACE_D2    | PE5              | 3.3V MCU | 跟踪数据 2                             |
|        9 | MCU_PSSI_D4     | PE4              | 3.3V MCU | PSSI D4                                |
|       10 | MCU_TRACE_D3    | PE6              | 3.3V MCU | 跟踪数据 3                             |
|       11 | MCU_PSSI_D5     | PI4              | 3.3V MCU | PSSI D5                                |
|       12 | MCU_PE7         | PE7              | 3.3V MCU | GPIO                                   |
|       13 | MCU_PSSI_D6     | PI6              | 3.3V MCU | PSSI D6                                |
|       14 | MCU_PE8         | PE8              | 3.3V MCU | GPIO                                   |
|       15 | MCU_PSSI_D7     | PI7              | 3.3V MCU | PSSI D7                                |
|       16 | MCU_I2C4_SCL    | PF14             | 3.3V MCU | I2C4 SCL                               |
|       17 | MCU_PSSI_PDCK   | PD9              | 3.3V MCU | PSSI 时钟                              |
|       18 | MCU_I2C4_SDA    | PF15             | 3.3V MCU | I2C4 SDA                               |
|       19 | MCU_PSSI_RDY    | PI5              | 3.3V MCU | PSSI 就绪                              |
|       20 | MCU_OPAMP1_VOUT | PA3              | 模拟     | OpAmp1 VOUT                            |
|       21 | MCU_PSSI_DE     | PD8              | 3.3V MCU | PSSI数据启用                           |
|       22 | MCU_OPAMP1_VINP | PA0              | 模拟     | OpAmp1 VINP                            |
|       23 | MCU_MCO         | PA8              | 3.3V MCU | MCU时钟输出                            |
|       24 | MCU_OPAMP1_VINM | PA1              | 模拟     | OpAmp1 VINM                            |
|       25 | MCU_CRS_SYNC    | PA10             | 3.3V MCU | CRS同步                                |
|       26 | GND             | -                | 电源     | 接地                                   |
|       27 | GND             | -                | 电源     | 接地                                   |
|       28 | EAR_P_R         | -                | 模拟     | 音频耳机P_R                            |
|       29 | MIC2_INP        | -                | 模拟     | Mic2 IN+                               |
|       30 | EAR_M_R         | -                | 模拟     | Audio ear M_R                          |
|       31 | MIC2_INM        | -                | 模拟     | Mic2 IN−                               |
|       32 | LINEOUT_P       | -                | 模拟     | 线路输出P                              |
|       33 | MIC2_BIAS       | -                | 模拟     | 麦克风2偏置                            |
|       34 | LINEOUT_M       | -                | 模拟     | 线路输出M                              |
|       35 | GND             | -                | 电源     | 接地                                   |
|       36 | HPH_L           | -                | 模拟     | 耳机L                                  |
|       37 | SOC_GPIO_0_SE0  | -                | 1.8V MPU | SoC GPIO 0 (SE0)                       |
|       38 | HPH_R           | -                | 模拟     | 耳机R                                  |
|       39 | SOC_GPIO_1_SE0  | -                | 1.8V MPU | SoC GPIO 1 (SE0)                       |
|       40 | HPH_REF         | -                | 模拟     | 耳机REF                                |
|       41 | SOC_GPIO_2_SE0  | -                | 1.8V MPU | SoC GPIO 2 (SE0)                       |
|       42 | HS_DET          | -                | 模拟     | 耳机检测                               |
|       43 | SOC_GPIO_3_SE0  | -                | 1.8V MPU | SoC GPIO 3 (SE0)                       |
|       44 | GND             | -                | 电源     | 接地                                   |
|       45 | SOC_GPIO_86_SE0 | -                | 1.8V MPU | SoC GPIO 86 (SE0)                      |
|       46 | SOC_GPIO_98     | -                | 1.8V MPU | SoC GPIO 98                            |
|       47 | SOC_GPIO_82_SE0 | -                | 1.8V MPU | SoC GPIO 82 (SE0)                      |
|       48 | SOC_GPIO_99     | -                | 1.8V MPU | SoC GPIO 99                            |
|       49 | SOC_GPIO_18     | -                | 1.8V MPU | SoC GPIO 18                            |
|       50 | SOC_GPIO_100    | -                | 1.8V MPU | SoC GPIO 100                           |
|       51 | SOC_GPIO_28     | -                | 1.8V MPU | SoC GPIO 28                            |
|       52 | SOC_GPIO_101    | -                | 1.8V MPU | SoC GPIO 101                           |
|       53 | +3V3 (输出)     | -                | 电源     | 3.3V电源输出                           |
|       54 | +5V_USB (输出)  | -                | 电源     | 5 V 电源输出                           |
|       55 | +3V3 (输出)     | -                | 电源     | 3.3V电源输出                           |
|       56 | +5V_USB (输出)  | -                | 电源     | 5 V 电源输出                           |
|       57 | +1V8 (IN)       | -                | 电源     | 1.8 V 电源轨                           |
|       58 | GND             | -                | 电源     | 接地                                   |
|       59 | VCOIN (IN)      | -                | 电源     | 系统电压（PMIC RTC）                   |
|       60 | VBAT (OUT)      | -                | 电源     | 系统电压（保留用于系统设计和未来功能） |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  注：JMISC上的SoC GPIO引脚为专用接口 (非创客GPIO)。MCU采用3.3V逻辑电平，MPU采用1.8V逻辑电平，音频/麦克风为模拟信号。
</div>


<div style="page-break-after: always;"></div>

### JMEDIA (B2) (JMEDIA1) - 引脚功能概述

| **引脚** | **名称**                | **域名**   | **注释**          |
| -------: | ----------------------- | ---------- | ----------------- |
|        1 | GND                     | 电源       | 接地              |
|        2 | GND                     | 电源       | 接地              |
|        3 | MIPI_DSI0_CLK_M         | MIPI D-PHY | DSI 时钟 −        |
|        4 | MIPI_DSI0_L1_P          | MIPI D-PHY | DSI 通道1 +       |
|        5 | MIPI_DSI0_CLK_P         | MIPI D-PHY | DSI 时钟 +        |
|        6 | MIPI_DSI0_L1_M          | MIPI D-PHY | DSI 通道1 −       |
|        7 | GND                     | 电源       | 接地              |
|        8 | GND                     | 电源       | 接地              |
|        9 | MIPI_DSI0_L2_M          | MIPI D-PHY | DSI lane2 −       |
|       10 | MIPI_DSI0_L0_P          | MIPI D-PHY | DSI lane0 +       |
|       11 | MIPI_DSI0_L2_P          | MIPI D-PHY | DSI lane2 +       |
|       12 | MIPI_DSI0_L0_M          | MIPI D-PHY | DSI lane0 −       |
|       13 | GND                     | 电源       | 接地              |
|       14 | GND                     | 电源       | 接地              |
|       15 | MIPI_DSI0_L3_M          | MIPI D-PHY | DSI lane3 −       |
|       16 | SOC_CAM_MCLK0 (GPIO_20) | 1.8V MPU   | 摄像机主时钟 0    |
|       17 | MIPI_DSI0_L3_P          | MIPI D-PHY | DSI lane3 +       |
|       18 | SOC_CAM_MCLK1 (GPIO_21) | 1.8V MPU   | 摄像机主时钟 1    |
|       19 | GND                     | 电源       | 接地              |
|       20 | GND                     | 电源       | 接地              |
|       21 | CSI0_C0_LN0_M           | MIPI D-PHY | CSI0 data0 −      |
|       22 | CCI_I2C_SDA1 (GPIO_29)  | 1.8V MPU   | 相机控制 I2C SDA1 |
|       23 | CSI0_B0_LN0_P           | MIPI D-PHY | CSI0 data0 +      |
|       24 | CCI_I2C_SCL1 (GPIO_30)  | 1.8V MPU   | 相机控制 I2C SCL1 |
|       25 | GND                     | 电源       | 接地              |
|       26 | GND                     | 电源       | 接地              |
|       27 | CSI0_B1_LN1_M           | MIPI D-PHY | CSI0 data1 −      |
|       28 | CSI1_B2_LN3_P           | MIPI D-PHY | CSI1 data3 +      |
|       29 | CSI0_A1_LN1_P           | MIPI D-PHY | CSI0 data1 +      |
|       30 | CSI1_C2_LN3_M           | MIPI D-PHY | CSI1 data3 −      |
|       31 | GND                     | 电源       | 接地              |
|       32 | GND                     | 电源       | 接地              |
|       33 | CSI0_A0_CLK_M           | MIPI D-PHY | CSI0 时钟 −       |
|       34 | CSI1_C1_LN2_P           | MIPI D-PHY | CSI1 data2 +      |
|       35 | CSI0_NC_CLK_P           | MIPI D-PHY | CSI0 时钟 +       |
|       36 | CSI1_A2_LN2_M           | MIPI D-PHY | CSI1 data2 −      |
|       37 | GND                     | 电源       | 接地              |
|       38 | GND                     | 电源       | 接地              |
|       39 | CSI0_A2_LN2_M           | MIPI D-PHY | CSI0 data2 −      |
|       40 | CSI1_NC_CLK_P           | MIPI D-PHY | CSI1 时钟 +       |
|       41 | CSI0_C1_LN2_P           | MIPI D-PHY | CSI0 data2 +      |
|       42 | CSI1_A0_CLK_M           | MIPI D-PHY | CSI1 时钟 −       |
|       43 | GND                     | 电源       | 接地              |
|       44 | GND                     | 电源       | 接地              |
|       45 | CSI0_C2_LN3_M           | MIPI D-PHY | CSI0 data3 −      |
|       46 | CSI1_A1_LN1_P           | MIPI D-PHY | CSI1 data1 +      |
|       47 | CSI0_B2_LN3_P           | MIPI D-PHY | CSI0 data3 +      |
|       48 | CSI1_B1_LN1_M           | MIPI D-PHY | CSI1 data1 −      |
|       49 | GND                     | 电源       | 接地              |
|       50 | GND                     | 电源       | 接地              |
|       51 | CCI_I2C_SCL0 (GPIO_23)  | 1.8V MPU   | 相机控制 I2C SCL0 |
|       52 | CSI1_B0_LN0_P           | MIPI D-PHY | CSI1 data0 +      |
|       53 | CCI_I2C_SDA0 (GPIO_22)  | 1.8V MPU   | 相机控制 I2C SDA0 |
|       54 | CSI1_C0_LN0_M           | MIPI D-PHY | CSI1 data0 −      |
|       55 | GND                     | 电源       | 接地              |
|       56 | GND                     | 电源       | 接地              |
|       57 | VIN (IN)                | 电源       | 7-24 V 输入       |
|       58 | +3V3 (输出)             | 电源       | 3.3V电源输出      |
|       59 | VIN (IN)                | 电源       | 7-24 V 输入       |
|       60 | +3V3 (输出)             | 电源       | 3.3V电源输出      |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  注：MIPI CSI/DSI通道为D-PHY差分对，而非通用I/O。控制线（CCI_I2C_*、SOC_CAM_MCLK*）属于1.8V MPU域。JMEDIA接口上的VIN为原始7-24V输入（仅供电）。
</div>
<div style="page-break-after: always;"></div>

### Qwiic (A4) (QWIIC1) - 引脚功能概述

| **引脚** | **名称** | **网络 / 功能** | **域名** | **注释**        |
| -------: | -------- | --------------- | -------- | --------------- |
|        1 | GND      | 接地            | 电源     | -               |
|        2 | +3V3 OUT | PWR_3P3V        | 电源     | Qwiic设备的供货 |
|        3 | SDA      | PD13 (I2C4_SDA) | 3.3 V    | -               |
|        4 | SCL      | PD12 (I2C4_SCL) | 3.3 V    | -               |

### JSPI (A5) (JSPI1) - 引脚功能概述

| **引脚** | **名称** | **网络 / 功能** | **域名** | **注释** |
| -------: | -------- | --------------- | -------- | -------- |
|        1 | MISO     | PC2 (SPI2_MISO) | 3.3 V    | -        |
|        2 | +5V      | 5V_USB_VBUS     | 电源     | 仅供电力 |
|        3 | SCK      | PD1 (SPI2_SCK)  | 3.3 V    | -        |
|        4 | MOSI     | PC3 (SPI2_MOSI) | 3.3 V    | -        |
|        5 | RESET    | MCU_NRST        | 3.3 V    | -        |
|        6 | GND      | 接地            | 电源     | -        |

### JCTL (A1) (JCTL1) - 引脚功能概述

| **引脚** | **名称**     | **网络 / 功能**      | **域名** | **注释**       |
| -------: | ------------ | -------------------- | -------- | -------------- |
|        1 | GND          | 接地                 | 电源     | -              |
|        2 | USB_BOOT     | 自举电路             | 1.8 V    | -              |
|        3 | VOL_DOWN     | GPIO_36              | 1.8 V    | GPIO           |
|        4 | SOC_SE4_TX   | UART TX (SE4) 控制台 | 1.8 V    | 系统控制台     |
|        5 | VOL_UP       | GPIO_96              | 1.8 V    | GPIO           |
|        6 | SOC_SE4_RX   | UART RX (SE4) 控制台 | 1.8 V    | 系统控制台     |
|        7 | GND          | 接地                 | 电源     | -              |
|        8 | PMIC_RESET   | PM4125 复位          | 1.8 V    | -              |
|        9 | +1V8 OUT     | VREG_L15A_1P8V       | 电源     | 1.8 V 参考资料 |
|       10 | VBUS_DISABLE | VBUS电源开关禁用     | 1.8 V    | 控制VBUS路径   |

<div style="page-break-after: always;"></div>

### JDIGITAL (A2) (JDIGITAL1) - 引脚功能概述

| **引脚** | **名称** | **MCU 引脚** | **功能**                                 | **域名** | **注释**                 |
|---------:|----------|--------------|------------------------------------------|----------|--------------------------|
|        1 | D0       | PB7          | - USART1_RX <br></br>- TIM4_CH2          | 3.3 V    | UART                     |
|        2 | D1       | PB6          | - USART1_TX <br></br>- TIM4_CH1          | 3.3 V    | UART                     |
|        3 | D2       | PB3          | - TIM2_CH2                               | 3.3 V    | -                        |
|        4 | ~D3      | PB0          | - OPAMP2_OUTPUT <br></br>- TIM3_CH3      | 3.3 V    | PWM / / 不支持 5 V 电压 |
|        5 | D4       | PA12         | - FDCAN1_TX <br></br>- TIM1_ETR          | 3.3 V    | -                        |
|        6 | ~D5      | PA11         | - FDCAN1_RX <br></br>- TIM1_CH4          | 3.3 V    | PWM                      |
|        7 | ~D6      | PB1          | - TIM3_CH4                               | 3.3 V    | PWM                      |
|        8 | D7       | PB2          | - TIM8_CH4N                              | 3.3 V    | -                        |
|        9 | D8       | PB4          | - TIM3_CH1                               | 3.3 V    | -                        |
|       10 | ~D9      | PB8          | - TIM4_CH3                               | 3.3 V    | PWM                      |
|       11 | ~D10     | PB9          | - SPI2_SS (芯片选择) <br></br>- TIM4_CH4 | 3.3 V    | PWM                      |
|       12 | ~D11     | PB15         | - SPI2_MOSI <br></br>- TIM1_CH3N         | 3.3 V    | PWM                      |
|       13 | D12      | PB14         | - SPI2_MISO <br></br>- TIM1_CH2N         | 3.3 V    | -                        |
|       14 | D13      | PB13         | - SPI2_SCK <br></br>- TIM1_CH1N          | 3.3 V    | -                        |
|       15 | GND      | -            | - 接地                                   | 电源     | -                        |
|       16 | AREF     | -            | - 模拟参考                               | -        | 模拟基准引脚（非GPIO引脚） |
|       17 | D20      | PB11         | - I2C2_SDA <br></br>- TIM2_CH4           | 3.3 V    | -                        |
|       18 | D21      | PB10         | - I2C2_SCL <br></br>- TIM2_CH3           | 3.3 V    | -                        |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
   所有 JDIGITAL 线路均采用 3.3 V 逻辑电平。大多数引脚采用 FT 型 I/O 结构，作为输入时可耐受 5 V 电压。D3（PB0）采用 TT 型 I/O 结构，仅可耐受 3.6 V 电压，在任何模式下均不得向该引脚施加 5 V 电压。
</div>


### JANALOG (A3) (JANALOG1) - 引脚功能概述

| **引脚** | **名称**     | **网络 / MCU 引脚** | **功能**                                               | **域名**     | **注释**             |
| -------: | ------------ | ------------------- | ------------------------------------------------------ | ------------ | -------------------- |
|        1 | BOOT         | MCU_BOOT0           | - 自举电路                                             | 3.3 V        | -                    |
|        2 | IOREF        | PWR_3P3V            | - I/O电压基准（镜像3.3V电源轨）                        | 电源         | 仅输出；禁止反向馈入 |
|        3 | RESET        | MCU_NRST            | - MCU 复位                                             | 3.3 V        | -                    |
|        4 | +3V3 OUT     | PWR_3P3V            | - 3.3 V 电源                                           | 电源         | -                    |
|        5 | +5V USB VBUS | 5V_USB_VBUS         | - 5V电源（直通）                                       | 电源         | 仅供电力             |
|        6 | GND          | GND                 | - 接地                                                 | 电源         | -                    |
|        7 | GND          | GND                 | - 接地                                                 | 电源         | -                    |
|        8 | VIN IN       | DC_IN               | - 7-24 V 输入                                          | 电源         | 仅供电力             |
|        9 | A0 / D14     | PA4                 | - ADC 输入<br></br>- DAC0 <br></br>- TIM2_CH1          | 模拟 / 3.3 V | 直接ADC / 不耐5V     |
|       10 | A1 /  D15    | PA5                 | - ADC 输入<br></br>- DAC1 <br></br>- TIM3_CH1          | 模拟 / 3.3 V | 直接ADC / 不耐5V     |
|       11 | A2 /  D16    | PA6                 | - ADC 输入<br></br>- OPAMP2_INPUT+ <br></br>- TIM3_CH2 | 模拟 / 3.3 V |                      |
|       12 | A3 /  D17    | PA7                 | - ADC 输入<br></br>- OPAMP2_INPUT−                     | 模拟 / 3.3 V | -                    |
|       13 | A4 /  D18    | PC1                 | - ADC 输入<br></br>- I2C3_SDA <br></br>- LPTIM1_CH1    | 模拟 / 3.3 V | -                    |
|       14 | A5 /  D19    | PC0                 | - ADC 输入<br></br>- I2C3_SCL <br></br>- LPTIM1_IN1    | 模拟 / 3.3 V | -                    |

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  A0（PA4）和A1（PA5）是直接参考<code>VREF+</code>的STM32U585 ADC输入引脚。它们不耐受5V电压，有效输入范围为<code>0-VREF+</code>（≈3.3V）。引脚绝对最大电压为<code>VDD + 0.3 V</code>（约3.6 V）。超过此电压时，MCU内部保护二极管将开始导通。该接口还提供<code>5V_SYS</code>和<code>PWR_3P3V</code>电源引脚，仅用于电源供应。切勿向<strong>A0</strong>或<strong>A1</strong>引脚施加5V电压。IOREF引脚连接至3.3V电源轨（<code>PWR_3P3V</code>），作为扩展板的参考/输出端口，严禁将其用于向主板回馈电源。
</div>

## 高速外围设备

- **USB-C:** 支持角色切换功能的USB 3.1接口。通过ANX7625 DSI转DP桥接器实现DisplayPort替代模式。该连接器的超高速差分线对同时服务于DP替代模式和USB 3.1数据传输。当DisplayPort替代模式激活时，USB数据传输速率将降低。

- **摄像头:** 四通道**MIPI-CSI-2**（1.8V I/O）。

- **显示:** 四通道**MIPI-DSI**接口接入**ANX7625**芯片，实现USB-C端口的DisplayPort替代模式。

- **无线:** 双频Wi-Fi®（802.11a/b/g/n/ac）与Bluetooth®5.1集成于共享模块。

<div style="page-break-after: always;"></div>

## 电路板操作

### 入门指南 - Arduino App Lab

Arduino App Lab [1] 是一个统一编辑器，可在开发板的两个处理器上构建并运行项目。项目即为**App**，可包含：

- 在Linux系统（Qualcomm Dragonwing™ QRB2210）上运行的Python®程序
- 在微控制器（MCU）（STM32U585）上运行的Arduino程序
- 可选的**Bricks**（预打包服务，如AI模型、Web服务器或API客户端）与应用程序并行部署（同样在Linux系统上运行）。

App通过**Bridge**在Linux侧与微控制器之间交换数据。

Arduino App Lab 可安装在您的电脑上，或直接在单板计算机模式的 UNO Q 上运行。此配置推荐使用 UNO Q 的 4GB LPDDR4X 版本，以确保有足够内存支持稳定运行和资源密集型应用。使用该开发板的方法：

- 在Arduino App Lab中启动现成示例，根据需求进行定制，或使用集成编辑器从零构建新应用。
- 点击Arduino App Lab中的**Run**按钮[1]。
- 编辑器将构建Linux组件、烧录MCU程序、部署所选Bricks，并启动板载所有组件。
- 编辑器中可同时查看双方日志，无需离开Arduino App Lab即可进行迭代开发。

首次设置时：
=======
1. 安装Arduino App Lab [1]并启动，连接UNO Q开发板：采用**USB-C数据线**进入PC主机模式，或直接供电进入单板计算机模式。
2. 该开发板将自动检查更新。若有可用更新，系统将提示您安装。更新完成后，需重新启动Arduino App Lab[1]。
3. 初始设置将要求您为设备设置名称和密码，同时需提供本地网络的Wi-Fi®凭证。
4. 测试开发板时，请在Arduino App Lab[1]的**“Examples”**(示例) 部分选择一个示例应用程序，点击右上角的“运行”按钮。您也可在**“App”**板块创建新应用。
5. App的状态可在App控制台选项卡中监控。

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;"> <p style="text-align: justify;">
  <strong>注意:</strong>在<strong>PC-hosted</strong>模式下，首次设置需要<em>USB数据</em>连接。之后可通过局域网（SSH）使用<strong>网络</strong>目标。在单板计算机 (SBC)模式下，设置无需USB数据连接，只需为板卡供电，待其加入<strong>网络</strong>后即可使<strong>用网</strong>络目标。SBC模式下外设（键盘、鼠标、USB摄像头、麦克风）需使用具备外接电源传输功能的USB-C转接头。当DisplayPort替代模式激活时，USB数据传输速率将降低。.</p>
</div>

使用5V/3A的USB-C电源适配器及数据线供电，或参照[输入电源部分](#input-power)说明通过5V或VIN引脚供电（USB-C仅支持5V / VIN支持7-24V）。

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  首次启动通常需20-30秒完成Linux系统初始化。请等待启动LED序列或LED矩阵动画结束再与开发板交互。
</div>

### Bricks

<p style="text-align: justify;">在Arduino应用实验室中，<strong>Bricks</strong>是模块化构建块，可让您无需编写底层基础设施即可扩展应用程序。每个Brick封装了现成的功能，例如传感器集成、AI模型、数据库或用户界面，您可将其直接拖入项目中使用。典型Bricks提供：</p>

<ul>
  <li>一个AI模型 (例如物体分类或关键词检测)</li>
  <li>一个Web UI或REST API服务</li>
  <li>与外部数据源的集成</li>
</ul>

<p style="text-align: justify;">Bricks与App并行部署，并由Linux侧管理。典型工作流如下：</p>

<ol>
  <li>在Arduino App Lab中创建<strong>应用</strong>程序。</li>
  <li>选择应用程序应使用的任意<strong>Brick</strong>。</li>
  <li>添加您的Python®代码（Linux）和/或Arduino草图（MCU）。</li>
  <li>需将Brick导入`main.py`文件，并按Brick的API进行初始化。</li>
  <li>点击“<strong>Run</strong>”部署Linux应用程序，烧录MCU，并启动应用程序及其Bricks组件。</li>
<li><strong>Bridge</strong>工具负责处理Linux与MCU之间的数据交换。</li>
</ol>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  当应用程序处于绑定运行状态时，USB接口可能被系统占用。请使用Arduino App Lab [1]进行部署和监控。若需通过USB使用外部命令行工具，请停止应用程序或断开开发板连接。
</div>

### Hello World

<p style="text-align: justify;">让我们用经典的Arduino“Hello World”——<em>闪烁LED</em>示例来编程UNO Q。这有助于验证该板是否已正确连接至Arduino App Lab。</p>

<ol>
  <li>打开Arduino App实验室。它从“<strong>Examples</strong>”部分开始。</li>
  <li>若未使用单板计算机模式，<strong>请将UNO Q</strong>连接至电脑。</li>
  <li>打开“<em>Blink LED</em>”示例。阅读示例说明以了解App工作原理。</li>
  <li>点击“<strong>Run</strong>”并等待上传完成。</li>
</ol>

<p style="text-align: justify;">此时您应能看到内置RGB LED的红色通道以一秒亮起、一秒熄灭的节奏循环闪烁。该LED通过Arduino程序由STM32U585微控制器驱动。</p>

<p style="text-align: justify;">您可以从空白 App 开始，或使用现有示例。首次使用时，建议通过“Hello World”示例学习基本结构。</p>

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  每次运行App时，微控制器程序都会被编译，同时Python®应用程序会在Linux系统上启动。根据复杂程度，此过程可能需要长达一分钟。
</div>

### 如何检查应用程序是否正在运行

<p style="text-align: justify;">在 App Lab 中打开<strong>控制台</strong>。共有三个选项卡：</p>

<ul>
  <li><strong>Start-up</strong>：启动序列日志，包括MCU编译和Linux部署</li>
  <li><strong>Main (Python®)</strong>: Python®应用程序输出 (<code>print()</code>)</li>
  <li><strong>Sketch (微控制器)</strong>：Arduino程序串行输出 (<code>Serial.println()</code>)</li>
</ul>


<p style="text-align: justify;">应用程序可能启动成功，但仍存在运行时问题。请检查Python®日志中的错误信息。若发生草图编译错误，启动过程将被中止。</p>

<div style="page-break-after: always;"></div>

### 电源按钮

<p style="text-align: justify;">UNO Q 包含一<strong>个电源按钮</strong>（JBTN1），可用于重启开发板。</p>

![UNO Q Power Button](assets/ABX00162-ABX00173-power-button.png)

<strong>长按 (≥5秒):</strong>重启Linux系统（MPU）。此操作不会切断电路板电源。

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>注:</strong> 长按重启按钮将重启Linux环境，可能中断正在运行的应用程序。请保存工作内容，并在适用情况下确保外部进程安全关闭。供电后主板将自动启动，正常启动时无需按压按钮。
</div>


### 在线资源

<p style="text-align: justify;">在Project Hub[3]探索社区项目，浏览Library Reference[4]了解支持的API，并在Arduino Store [5]选购配件，例如Qwiic传感器、UNO扩展板和载体板。</p>

## 机械层信息

<p style="text-align: justify;">电路板尺寸为68.58毫米×53.34毫米，底部元件高度控制在2毫米以下，以便堆叠至载体基座上。其轮廓与孔位布局遵循UNO规格，兼容该标准。</p>


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
