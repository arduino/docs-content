---
identifier: ABX00050
title: Arduino® Nicla Sense ME
type: pro
author: Ali Jahangiri
---

![Nicla Sense ME](assets/featured.png)

# 中⽂ (ZH)

# 描述

<p style="text-align: justify;">
Arduino Nicla Sense ME 是我们迄今为止体积最小的产品，将一系列工业级传感器集成于极小巧的机身内。可测量温度、湿度、运动等工艺参数。借助强大的数据融合能力，深入探索边缘计算。通过内置的 Bosch® BHI260AP、BMP390、BMM150 和 BME688 传感器，构建专属的工业级无线传感网络。
</p>

# 目标领域
无线传感器网络、数据融合、人工智能与气体检测

# 目录

## 特点

### Bluetooth® 蓝牙模块

| **特点**                    | **描述**                                               |
| --------------------------- | ------------------------------------------------------ |
| **型号**                    | ANNA-B112 Bluetooth® 蓝牙模块                          |
| **微控制器**                | nRF52832 系统级芯片                                    |
| **CPU 内核**                | 64 MHz Arm® Cortex®-M4F                                |
| **内部SRAM**                | 64 KB                                                  |
| **内部闪存**                | 512 KB                                                 |
| **外部闪存**                | 2 MB                                                   |
| **接口**                    | 2 路 SPI，2 路 I2C（每种接口各通过一个引脚排针可访问） |
| **ADC**                     | 12-bit/200 ksps                                        |
| **Bluetooth® 蓝牙模块频率** | 2400–2483.5 MHz                                        |
| **天线规格**                | 内部                                                   |
| **振荡器**                  | 内部 32 MHz                                            |
| **工作电压**                | 1.8 VDC                                                |

### 集成 IMU 的智能传感器

| **特点**     | **描述**                                               |
| ------------ | ------------------------------------------------------ |
| **型号**     | Bosch® BHI260AP                                        |
| **CPU 内核** | Fuser 2, 32 Bit Synopsys DesignWare ARCTM EM4TM 处理器 |
| **IMU**      | 6 轴：16 位3轴加速度计和陀螺仪                         |
| **高级特点** | 自学习人工智能、游泳分析、行人航迹推算、方向感测       |
| **外部内存** | 通过 QSPI 连接的 2MB 闪存                              |

### 高性能压力传感器

| **特点**        | **描述**                      |
| --------------- | ----------------------------- |
| **型号**        | Bosch® BMP390                 |
| **允许范围**    | 300-1250 hPa                  |
| **绝对精度**    | ± 0.5 hPa                     |
| **相对精度**    | ± 0.03 hPa（相当于 ±25 厘米） |
| **RMS 降噪**    | 0.02 Pa                       |
| **FIFO 缓冲区** | 集成 512 字节                 |
| **最大采样率**  | 200 Hz                        |

### 3轴磁力计

| **特点**       | **描述**                              |
| -------------- | ------------------------------------- |
| **型号**       | Bosch® BMM150                         |
| **磁场范围**   | X, Y axis: ±1300 μT, Z axis: ±2500 μT |
| **分辨率**     | 0.3 μT                                |
| **非线性误差** | <1% FS                                |

### 环境传感器

| **特点**         | **描述**                                                     |
| ---------------- | ------------------------------------------------------------ |
| **型号**         | Bosch® BME688                                                |
| **允许范围**     | 压力：300-1100 hPa，湿度：0-100%，温度：-40 至 - +85°C       |
| **eNose 传感器** | 传感器间偏差（IAQ）：±15% ±15 IAQ                            |
| **传感器输出**   | IAQ、bVOC 和 CO2 等效浓度（ppm）、气体扫描结果（%）、强度等级 |

### 微控制器

| **特点** | **描述**                  |
| -------- | ------------------------- |
| **型号** | ATSAMD11D14A-MUT          |
| **功能** | 串口转USB桥接器，调试接口 |

<div style="page-break-after: always;"></div>

## 电路板简介

### 应用示例
Arduino® Nicla Sense ME 是您开发无线网络解决方案的理想选择，具备快速开发和高可靠性。实时监控您的生产流程的运行特性。利用高质量传感器和网络功能，评估新型无线传感器网络（WSN）架构。超低功耗和集成电池管理功能，支持在各种应用场景中部署。WebBLE 支持固件的远程固件升级（OTA）以及远程监控。

- **仓库和库存管理**：
Arduino® Nicla Sense ME 的环境传感器可检测水果、蔬菜和肉类的成熟状态，与 Arduino Cloud 一起实现易腐资产的智能管理。

- **分布式工业传感**：
即使在难以到达或具有危险性的区域，也可远程识别机器、工厂或温室内的运行状态。借助 **Arduino® Nicla Sense ME** 的 AI 能力，检测天然气、有毒气体或其他危险气体。通过远程分析提升安全等级。Mesh 网络功能使无线传感网络（WSN）的部署更加简便，几乎不需基础设施支持。

- **无线传感网络参考设计:**
Nicla 封装规格是 Arduino® 专为无线传感网络开发的一种标准，可由合作伙伴适配用于定制化工业解决方案。通过开发包括连接云端的电池供电 IoT 设备和自主机器人在内的定制终端用户解决方案，让您的项目领先一步。研究人员和教育工作者也可利用该平台，在一个获得工业认可的无线传感器研究开发标准上开展工作，从而缩短从概念到市场的时间。

### 配件（不包含在内）
- 单节锂离子/锂聚合物电池

### 相关产品
- ESLOV 连接器
- Arduino® Portenta H7 (SKU: ABX00042)

### 功能概述
![远程环境监测的典型解决方案示例，包括Arduino® Nicla Sense ME、Portenta H7和电池。请注意电池电缆在电路板连接器中的方向。 ](assets/niclaSenseMEBattery.png)

**注意:** 电池连接器上的 NTC 引脚为可选项。此特点有助于更安全地使用，并支持过热保护功能。


## 额定值
### 建议运行条件
| 符号                 | 描述                      | 最小值                              | 典型值 | 最大值                              | 单位 |
| -------------------- | ------------------------- | ----------------------------------- | ------ | ----------------------------------- | ---- |
| V<sub>IN</sub>       | 来自 VIN 焊盘的输入电压   | 3.5                                 | 5.0    | 5.5                                 | V    |
| V<sub>USB</sub>      | 来自 USB 连接器的输入电压 | 4.8                                 | 5.0    | 5.5                                 | V    |
| V<sub>DDIO_EXT</sub> | 电平转换电压              | 1.8                                 | 3.3    | 3.3                                 | V    |
| V<sub>IH</sub>       | 输入高电平电压            | 0.7V<sub>DDIO_EXT</sub><sup>1</sup> |        | V<sub>DDIO_EXT</sub>                | V    |
| V<sub>IL</sub>       | 输入低电平电压            | 0                                   |        | 0.3V<sub>DDIO_EXT</sub><sup>2</sup> | V    |
| T<sub>OP</sub>       | 工作温度                  | -40                                 | 25     | 85                                  | °C   |

**注意**：V<sub>DDIO_EXT</sub> 可通过软件编程。虽然 ADC 输入可接受高达 3.3V 的电压，但最大值取决于 ANNA B112 的工作电压。

**<sup>1</sup>**：除以下引脚外，所有 I/O 引脚均工作在 V<sub>DDIO_EXT</sub> 电压下：
- ADC1 和 ADC2 - 1V8
- JTAG_SAMD11 - 3V3
- JTAG_ANNA - 1V8
- JTAG_BHI - 1V8

**<sup>2</sup>**：如果内部 V<sub>DDIO_EXT</sub> 被禁用，则可以通过外部供电。

<div style="break-after:page"></div>

## 功能概述

### 方框图
![Nicla Sense ME Block Diagram](assets/niclaSenseMEBlockDiagram.png)

<div style="page-break-after:always;"></div>

### 电路板拓扑结构
**俯视图**

![Nicla Sense ME Top View](assets/niclaSenseMETopTopology.svg)


| **编号** | **描述**                                 | **编号** | **描述**                      |
| -------- | ---------------------------------------- | -------- | ----------------------------- |
| MD1      | ANNA B112 Bluetooth® 蓝牙模块            | U2, U7   | MX25R1635FZUIH0 2MB 闪存芯片  |
| U3       | BMP390 压力传感器芯片                    | U4       | BMM150 3轴磁传感器芯片        |
| U5       | BHI260AP  六轴 IMU 与 AI 核心芯片        | U6       | BME688 环境传感器芯片         |
| U8       | IS31FL3194-CLS2-TR 三通道 LED 驱动芯片   | U9       | BQ25120AYFPR 电池充电管理芯片 |
| U10      | SN74LVC1T45 1通道电压电平转换器集成电路  | U11      | TXB0108YZPR 双向集成电路      |
| U12      | NTS0304EUKZ 4位转换收发器                | J1       | ADC、SPI和LPIO引脚接头        |
| J2       | I2C, JTAG, 电源, LPIO引脚接头            | J3       | 电池引脚接头                  |
| Y1       | SIT1532AI-J4-DCC MEMS 32.7680 kHz 振荡器 | DL1      | SMLP34RGB2W3 RGB SMD LED      |
| PB1      | 复位按钮                                 |          |                               |

<div style="page-break-after:always;"></div>

**电路板背面视图**
![Nicla Sense ME Back View](assets/niclaSenseMEBackTopology.png)

| **编号** | **描述**                                 | **编号** | **描述**                                        |
| -------- | ---------------------------------------- | -------- | ----------------------------------------------- |
| U1       | ATSAMD11D14A-MUT USB桥接器               | U13      | NTS0304EUKZ 4位转换收发器 IC                    |
| U14      | AP2112K-3.3TRG1 0.6 A 3.3 V LDO IC       | J4       | 3针 1.2mm ACH 电池连接器 （BM03B-ACHSS-GAN-TF） |
| J5       | SM05B-SRSS-TB（LF)（SN) 5针 Eslov 连接器 | J7       | microUSB 连接器                                 |

### 微控制器
Arduino® Nicla Sense ME 由 ANNA-B112 模块（MD1）内的 nRF52832 SoC 提供动力。nRF52832 SoC 基于 Arm® Cortex®-M4 微控制器构建，配备浮点运算单元，运行频率为 64 MHz。草图程序存储在 nRF52832 的内部 512 KB 闪存中（与引导程序共享）。用户可使用 64 KB 的 SRAM。ANNA-B112 模块作为数据记录用的 2MB 闪存（U7）和 BHI260 六轴 IMU（U5）的 SPI 主机。同时，它也是 BHI260（U5）I2C 和 SPI 连接的从设备。虽然该模块本身运行在 1.8V 电压下，但可通过电平转换器根据 BQ25120（U9）中设置的 LDO，在 1.8V 和 3.3V 之间调整逻辑电平。一个外部振荡器（Y1）提供 32 KHz 信号。

### Bosch® BHI260 内置六轴 IMU 的智能传感器系统
Bosch® BHI260 是一款超低功耗可编程传感器，集成了 Fuser2 核心处理器、六轴 IMU（陀螺仪和加速度计）以及传感器融合软件框架。BHI260 是一个智能传感器核心（可运行可编程识别系统），负责通过 I2C 和 SPI 接口与 **Arduino Nicla Sense ME** 上的其他传感器进行通信。芯片还配备一个专用的 2MB 闪存（U2），用于存储可直接执行的代码（XiP）以及数据，如 Bosch® 传感器融合算法（BSX）的校准数据。BHI260 支持加载在 PC 上训练好的自定义算法，生成的智能算法可直接在芯片上运行。

### Bosch® BME688 环境传感器
**Arduino Nicla Sense ME** 能够通过 Bosch® BME688 传感器（U6）进行环境监测。该传感器具备检测气压、湿度、温度以及挥发性有机化合物（VOC）的功能。Bosch® BME688 通过 eNose 金属氧化物半导体阵列进行气体检测，典型气体扫描周期为 10.8 秒。 

### Bosch® BMP390 压力传感器
在气压测量方面，BMP390（U3）提供工业级的精度与稳定性，适用于长期使用，在高分辨率模式下具有 ±0.03 hPa 的相对精度和 0.02 Pa 的 RMS 噪声。Bosch® BMP390 既适用于 200 Hz 采样率的快速测量，也可在 1 Hz 低功耗模式下运行，电流消耗低于 3.2 μA。U3 通过 SPI 接口由 BHI260（U2）控制，与 BME688（U6）共用同一总线。

### Bosch® BMM150 3轴磁力计
Bosch® BMM150（U4）可实现对磁场的高精度3轴测量，具备指南针级别的准确性。与 BHI260 IMU（U2）结合后，可通过 Bosch® 传感器融合算法获得高精度的空间姿态和运动矢量，用于自主机器人中的航向检测以及预测性维护。该传感器通过专用 I2C 接口与 BHI260（U2）相连，BHI260 作为主机。
### RGB LED

一个 I2C 接口的 LED 驱动芯片（U8）驱动 RGB LED（DL1），其最大输出电流为 40 mA，由微控制器 ANN-B112（U5）控制。

### USB 转接桥
SAMD11 微控制器（U1）专用于作为 USB 转接桥和 ANNA-B112 的 JTAG 控制器。逻辑电平转换器（U13）用于将 3.3V 逻辑电平转换为 ANNA-B112 所需的 1.8V 电平。3.3V 电压由 LDO 稳压器（U14）通过 USB 电压生成。

### 电源树
![Nicla Sense ME Back View](assets/niclaSenseMEPowerTree.svg)

**Arduino Nicla Sense ME** 可通过 Micro USB（J7）、ESLOV（J5）或 VIN 接口供电。这些输入电压通过 BQ2512BAYFPR 芯片（U9）转换为各个所需电压。一个肖特基二极管为 USB 和 ESLOV 电压提供反向极性保护。当通过 Micro USB 供电时，一个线性 3.3V 稳压器为用于编程、JTAG 和 SWD 的 SAMD11 微控制器供电。LED 驱动芯片（U8）及 RGB LED（DL1）则由 5V 升压电压驱动。其余所有组件均由降压稳压器提供的 1.8V 电压轨供电。PMID 引脚作为 VIN 和 BATT 之间的“或门”开关，用于驱动 LED 驱动器。所有引出至引脚的 I/O 信号均通过工作在 V <sub>DDIO_EXT</sub> 电压下的双向电平转换器处理。

此外，BQ25120AYFPR（U9）还支持通过 J4 接口连接单节 3.7V 锂聚合物（LiPo）/锂离子（Li-ion）电池组，使该板卡能够作为无线传感网络使用。电池充电电流设定为 40mA，终止电流为 4mA（10%）。

## 电路板操作
### 入门指南 - IDE
如果您希望在离线状态下为 Arduino® Nicla Sense ME 编程，您需要安装 Arduino® 桌面版 IDE **[1]**。要将 Arduino® Nicla Sense ME 连接至计算机，您需要一根 Micro USB 数据线。该数据线也为开发板供电，供电状态通过 LED 指示灯显示。Arduino 核心运行在 ANNA-B112 上，而 Bosch® 智能传感器框架则运行在 BHI260 上。

### 入门指南 - Arduino Cloud Editor
包括本电路板在内的所有 Arduino®  电路板，都可以在 Arduino® Cloud Editor **[2]**上开箱即用，只需安装一个简单的插件即可。

Arduino® Cloud Editor 是在线托管的，因此它将始终提供最新功能并支持所有电路板。接下来**[3]**开始在浏览器上编码并将程序上传到您的电路板上。

### 入门指南 - Arduino Cloud
Arduino®  Cloud 支持所有 Arduino®  支持 IoT 功能的产品，让您可以记录、绘制和分析传感器数据，触发事件，实现家庭或企业自动化。

### 入门指南 - WebBLE
Arduino Nicla Sense ME 支持使用 WebBLE 对 NINA-B112 和 BHI260 固件进行 OTA 更新。

### 入门指南 - ESLOV
该开发板可以作为 ESLOV 控制器的从设备，并可通过该方式更新固件。
### 示例程序
Arduino® Nicla Sense ME 的示例程序可以在 Arduino IDE 的“示例”菜单或 Arduino® Pro  网站 **[4]** 的“文档”部分找到。

### 在线资源
现在，您已经了解该电路板的基本功能，就可以通过查看 Project Hub **[5]**、Arduino® Library Reference **[6]** 和在线商店 **[7]** 上的精彩项目来探索它所提供的无限可能性；在这些项目中，您可以为电路板配备传感器、执行器等。

### 电路板恢复
所有 Arduino®  电路板都配置有内置的引导加载程序，可以通过 USB 对电路板进行刷新。如果某一程序锁定了处理器，且无法通过 USB 再次访问电路板，则可以在上电后立即双击复位按钮进入引导加载程序模式。

## 连接器引脚布局
**注意:** J1 和 J2 上的所有引脚（不包括散热片）均参考 V <sub>DDIO_EXT</sub> 电压，该电压可以由内部生成或由外部供电。

### J1 Nicla 头A

| 引脚 | **功能**  | **类型** | **描述**               |
| ---- | --------- | -------- | ---------------------- |
| 1    | LPIO0_EXT | 数字     | 低功耗 IO 引脚 0       |
| 2    | NC        | N/A      | N/A                    |
| 3    | CS        | 数字     | SPI 电缆选择           |
| 4    | COPI      | 数字     | SPI 控制器输出外设输入 |
| 5    | CIPO      | 数字     | SPI 控制器输入外设输出 |
| 6    | SCLK      | 数字     | SPI 时钟               |
| 7    | ADC2      | 模拟     | 模拟输入 2             |
| 8    | ADC1      | 模拟     | 模拟输入 1             |

### J2 Nicla 头B

| 引脚 | **功能**  | **类型** | **描述**         |
| ---- | --------- | -------- | ---------------- |
| 1    | SDA       | 数字     | I2C 数据线       |
| 2    | SCL       | 数字     | I2C 时钟         |
| 3    | LPIO1_EXT | 数字     | 低功耗 IO 引脚 1 |
| 4    | LPIO2_EXT | 数字     | 低功耗 IO 引脚 2 |
| 5    | LPIO3_EXT | 数字     | 低功耗 IO 引脚 3 |
| 6    | GND       | 电源     | 接地             |
| 7    | VDDIO_EXT | 数字     | 逻辑电平参考值   |
| 8    | N/C       | N/A      | N/A              |
| 9    | VIN       | 数字     | 输入电压         |

**注意:** 有关低功耗 I/O 工作原理的更多信息，请查阅 [Nicla 系列封装规格文档](https://docs.arduino.cc/learn/hardware/nicla-form-factor)。

### J2 Fins

| 引脚 | **功能**      | **类型** | **描述**                   |
| ---- | ------------- | -------- | -------------------------- |
| P1   | BHI_SWDIO     | 数字     | BHI260 JTAG 串行线调试数据 |
| P2   | BHI_SWDCLK    | 数字     | BHI260 JTAG 串行线调试时钟 |
| P3   | ANNA_SWDIO    | 数字     | ANNA JTAG 串行线调试数据   |
| P4   | ANNA_SWDCLK   | 数字     | ANNA JTAG 串行线调试时钟   |
| P5   | RESET         | 数字     | 复位引脚                   |
| P6   | SAMD11_SWDIO  | 数字     | SAMD11 JTAG 串行线调试数据 |
| P7   | +1V8          | 电源     | +1.8V 电压轨               |
| P8   | SAMD11_SWDCLK | 数字     | SAMD11 JTAG 串行线调试时钟 |

**注意:** 这些测试点可以通过将板子插入双排 1.27 mm / 50 mil 间距的排针轻松访问。
**注意 2:** 除 SAMD11 引脚（P6 和 P8）为 3.3V 外，所有 JTAG 逻辑电平均为 1.8V。这些 JTAG 引脚仅支持 1.8V，不会随 VDDIO 电压变化而调整。

### J3 电池焊盘

| 引脚 | **功能** | **类型** | **描述**     |
| ---- | -------- | -------- | ------------ |
| 1    | VBAT     | 电源     | 电池输入     |
| 2    | NTC      | 模拟     | NTC 热敏电阻 |

### J4 电池连接器

| 引脚 | **功能** | **类型** | **描述**     |
| ---- | -------- | -------- | ------------ |
| 1    | VBAT     | 电源     | 电池输入     |
| 2    | NTC      | 模拟     | NTC 热敏电阻 |
| 3    | GND      | 电源     | 接地         |

### J5 ESLOV

| 引脚 | **功能** | **类型** | **描述**   |
| ---- | -------- | -------- | ---------- |
| 1    | 5V       | 电源     | 5V 电源轨  |
| 2    | INT      | 数字     | 数字 IO    |
| 3    | SCL      | 数字     | I2C 时钟线 |
| 4    | SDA      | 数字     | I2C 数据线 |
| 5    | GND      | 电源     | 接地       |

## 机械层信息
![](assets/niclaSenseMEMech.png)

### 功耗
| 描述                              | 最小值 | 典型值 | 最大值 | 单位 |
| --------------------------------- | ------ | ------ | ------ | ---- |
| 待机功耗                          |        | 460    |        | uA   |
| 运行 Blink 程序时的电源功耗       |        | 960    |        | uA   |
| 以 1Hz 频率轮询传感器时的广播功耗 |        | 2.5    |        | mA   |
| 每小时轮询一次传感器时的广播功耗  |        | 1.15   |        | mA   |

**注意:** 测量是在启用温度传感器、加速度计和陀螺仪的前提下进行的，这些传感器配置为 1Hz 采样率和 1ms 延迟。

## Certifications

### Certifications Summary

<table>
   <thead>
      <tr>
         <th style="width: 16%;vertical-align: middle;text-align: center;"><strong>Certification</strong></th>
         <th style="width: 28%;vertical-align: middle;text-align: center;"><strong>Status</strong></th>
      </tr>
      <tr></tr>
   </thead>
   <tbody>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>CE (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>EN IEC 62311:2020</p>
            <p>EN 62368-1:2014+A11+2017</p>
            <p>ETSI EN 301 489-1 V2.2.3 (2019-11)</p>
            <p>ETSI EN 301 489-17 V3.2.4 (2020-09)</p>
            <p>ETSI EN 300 328 V2.2.2: 2019-07</p>
        </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>RoHS (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">
              <p>IEC 62321-3-1-2013</p>
              <p>IEC 62321-5-2013</p>
              <p>IEC 62321-7-1-2015</p>
              <p>IEC 62321-7-2-2017</p>
              <p>IEC 62321-6-2015</p>
              <p>IEC 62321-8-2017</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>REACH (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>WEEE (EU)</strong></td>
         <td style="vertical-align: middle;text-align: center;">Yes</td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>UKCA (UK)</strong></td>
         <td style="vertical-align: middle;text-align: center;">
                <p>EN IEC 62311:2020</p>
                <p>EN 62368-1-2014+A11+2017</p>
                <p>ETSI EN 301 489-1 V2.2.3 (2019-11)</p>
                <p>ETSI EN 301 489-17 V3.2.4 (2020-09)</p>
                <p>ETSI EN 300 328 V2.2.2: 2019-07</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>FCC (US)</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>IC (CA)</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>RSS-247 Issue 2</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>MIC</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>SRRC</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>CCC</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
      </tr>
      <tr>
         <td style="vertical-align: middle;text-align: center;"><strong>GB4943</strong></td>
         <td style="vertical-align: middle;text-align: center;">
            <p>Yes</p>
         </td>
      </tr>
   </tbody>
</table>

### Declaration of Conformity CE DoC (EU)
We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA). 

### Declaration of Conformity to EU RoHS & REACH 211 01/19/2021
Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment. 

| Substance                              | **Maximum limit (ppm)** |
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

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907 /2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907 /2006/EC.

### Conflict Minerals Declaration 

As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas. 

## FCC Caution
Any Changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: 

(1) This device may not cause harmful interference

(2) this device must accept any interference received, including interference that may cause undesired operation.

**FCC RF Radiation Exposure Statement:**

1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.

2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.

3. This equipment should be installed and operated with a minimum distance of 20cm between the radiator & your body.

English: 
User manuals for license-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual or alternatively on the device or both. This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions:

(1) this device may not cause interference

(2) this device must accept any interference, including interference that may cause undesired operation of the device.

French: 
Le présent appareil est conforme aux CNR d’Industrie Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes:

(1) l’appareil nedoit pas produire de brouillage

(2) l’utilisateur de l’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

**IC SAR Warning:**

English 
This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.  

French: 
Lors de l’ installation et de l’ exploitation de ce dispositif, la distance entre le radiateur et le corps est d ’au moins 20 cm.

**Important:** The operating temperature of the EUT can’t exceed 85℃ and shouldn’t be lower than -40℃.

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 201453/EU. This product is allowed to be used in all EU member states. 

| Frequency bands             | Typical Output Power |
| --------------------------- | -------------------- |
| 2.402-2480 MHz, 40 channels | +6dBm                |

## NCC Low Power Warning

**警語:**

取得審驗證明之低功率射頻器材，非經核准，公司、商號或使用者均不得擅自變更頻率、加大功率或變更原設計之特性及功能。

低功率射頻器材之使用不得影響飛航安全及干擾合法通信；經發現有干擾現象時，應立即停用，並改善至無干擾時方得繼續使用。

前述合法通信，指依電信管理法規定作業之無線電通信。

低功率射頻器材須忍受合法通信或工業、科學及醫療用電波輻射性電機設備之干擾。

## SRRC

This equipment contains a radio transmitter module with model approval code: CMIIT ID: 25J996Q00001.

## Company Information

| Company name    | Arduino SRL                                  |
|-----------------|----------------------------------------------|
| Company Address | Via Andrea Appiani, 25 - 20900 MONZA (Italy) |

## Reference Documentation

| Ref                                | Link                                                                                                |
|------------------------------------|-----------------------------------------------------------------------------------------------------|
| Arduino® IDE (Desktop)             | https://www.arduino.cc/en/Main/Software                                                             |
| Arduino® IDE (Cloud)               | https://create.arduino.cc/editor                                                                    |
| Arduino® Cloud IDE Getting Started | https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-4b3e4a |
| Arduino® Pro Website               | https://www.arduino.cc/pro                                                                          |
| Project Hub                        | https://create.arduino.cc/projecthub?by=part&part_id=11332&sort=trending                            |
| Library Reference                  | https://github.com/bcmi-labs/Arduino_EdgeControl/tree/4dad0d95e93327841046c1ef80bd8b882614eac8      |
| Online Store                       | https://store.arduino.cc/                                                                           |

## Revision History

| **Date**   | **Revision** | **Changes**                                          |
| ---------- | ------------ | ---------------------------------------------------- |
| 27/05/2021 | 1            | Initial Version                                      |
| 20/07/2021 | 2            | Technical Revisions                                  |
| 13/12/2022 | 3            | Change Solution Overview Image                       |
| 22/12/2022 | 4            | Add NTC Image & addition pins info                   |
| 03/07/2023 | 5            | Certification Summary Table Updated                  |
| 09/01/2024 | 6            | High-Performance Pressure Sensor information updated |
| 03/09/2024 | 7            | Cloud Editor updated from Web Editor                 |
| 05/02/2025 | 8            | Description updates                                  |
| 12/10/2026 |       9      | Added note for Intended Use |


## Product Warnings and Disclaimers

THESE PRODUCTS ARE INTENDED FOR SALE TO AND INSTALLATION BY QUALIFIED PROFESSIONALS. ARDUINO CANNOT PROVIDE ANY ASSURANCE THAT ANY PERSON OR ENTITY BUYING ITS PRODUCTS, INCLUDING ANY “AUTHORIZED DEALER” OR “AUTHORIZED RESELLER”, IS PROPERLY TRAINED OR EXPERIENCED TO CORRECTLY INSTALL RELATED PRODUCTS.

A PROPERLY INSTALLED AND MAINTAINED SYSTEM MAY ONLY REDUCE THE RISK OF EVENTS SUCH AS LOSS OF FUNCTIONALITY; IT IS NOT INSURANCE OR A GUARANTEE THAT SUCH EVENTS WILL NOT OCCUR, THAT ADEQUATE WARNING OR PROTECTION WILL BE PROVIDED, OR THAT THERE WILL BE NO DEATH, PERSONAL INJURY, AND/OR PROPERTY DAMAGE AS A RESULT.

BEFORE INSTALLING THE PRODUCTS, ENSURE THAT ITS FIRMWARE IS UPGRADED TO THE LATEST VERSION, AVAILABLE FOR DOWNLOAD FROM OUR WEBSITE. DURING THE LIFESPAN OF PRODUCTS, IT IS IMPORTANT TO CHECK ABOUT THE APPLICABILITY OF FIRMWARE UPDATES.

USERS SHOULD, WHERE APPLICABLE, CHANGE PASSWORDS FREQUENTLY AND ENSURE A HIGH-QUALITY PASSWORD (PASSWORDS SHOULD BE LONG AND COMPLEX ENOUGH, NEVER SHARED, AND ALWAYS UNIQUE). FURTHERMORE, IT IS THE USERS’ RESPONSIBILITY TO KEEP ITS ANTI-VIRUS SYSTEM UP TO DATE.

WHILE ARDUINO MAKES REASONABLE EFFORTS TO REDUCE THE PROBABILITY THAT A THIRD PARTY MAY HACK, COMPROMISE OR CIRCUMVENT ITS SECURITY PRODUCTS, RELATED SOFTWARE OR CLOUD SERVERS, ANY SECURITY PRODUCT, SOFTWARE OR CLOUD SERVER MANUFACTURED, SOLD AND/OR LICENSED BY ARDUINO, MAY STILL BE HACKED, COMPROMISED AND/OR CIRCUMVENTED.

CERTAIN PRODUCTS OR SOFTWARE MANUFACTURED, SOLD OR LICENSED BY ARDUINO CONNECT TO THE INTERNET TO SEND AND/OR RECEIVE DATA (“INTERNET OF THINGS” OR “IOT” PRODUCTS). ANY CONTINUED USE OF AN IOT PRODUCT AFTER ARDUINO HAS CEASED SUPPORTING THAT IOT PRODUCT (E.G., THROUGH NOTICE THAT ARDUINO NO LONGER PROVIDES FIRMWARE UPDATES OR BUG FIXES) MAY RESULT IN REDUCED PERFORMANCE, MALFUNCTION, AND/OR INCREASED VULNERABILITY TO HACKING, COMPROMISE AND/OR CIRCUMVENTION.

ARDUINO DOES NOT ALWAYS ENCRYPT COMMUNICATIONS BETWEEN PRODUCTS AND THEIR PERIPHERAL DEVICES INCLUDING, BUT NOT LIMITED TO, SENSORS OR DETECTORS UNLESS REQUIRED BY APPLICABLE LAW. AS A RESULT THESE COMMUNICATIONS MAY BE INTERCEPTED AND COULD BE USED TO CIRCUMVENT YOUR SYSTEM.

THE ABILITY OF ARDUINO PRODUCTS AND SOFTWARE TO WORK PROPERLY DEPENDS ON A NUMBER OF PRODUCTS AND SERVICES MADE AVAILABLE BY THIRD PARTIES OVER WHICH ARDUINO HAS NO CONTROL INCLUDING, BUT NOT LIMITED TO, INTERNET, CELLULAR AND LANDLINE CONNECTIVITY; MOBILE DEVICE AND OPERATING SYSTEM COMPATIBILITY; AND PROPER INSTALLATION AND MAINTENANCE. ARDUINO SHALL NOT BE LIABLE FOR ANY DAMAGES CAUSED BY ACTIONS OR OMISSIONS OF THIRD PARTIES.

BATTERY OPERATED SENSORS, DETECTORS, KEYFOBS, DEVICES AND OTHER PANEL ACCESSORIES HAVE A LIMITED BATTERY LIFE.  WHILE THESE PRODUCTS MAY BE DESIGNED TO PROVIDE SOME WARNING OF IMMINENT BATTERY DEPLETION, THE ABILITY TO DELIVER SUCH WARNINGS IS LIMITED AND SUCH WARNINGS MAY NOT BE PROVIDED IN ALL CIRCUMSTANCES.  PERIODIC TESTING OF THE SYSTEM IN ACCORDANCE WITH PRODUCT DOCUMENTATION IS THE ONLY WAY TO DETERMINE IF ALL SENSORS, DETECTORS, KEYFOBS, DEVICES AND OTHER PANEL ACCESSORIES ARE FUNCTIONING PROPERLY.

CERTAIN SENSORS, DEVICES AND OTHER PANEL ACCESSORIES MAY BE PROGRAMMED INTO PANEL AS “SUPERVISORY” SO THAT THE PANEL WILL INDICATE IF IT DOES NOT RECEIVE A REGULAR SIGNAL FROM THE DEVICE WITHIN A CERTAIN PERIOD OF TIME.  CERTAIN DEVICES CANNOT BE PROGRAMMED AS SUPERVISORY. DEVICES CAPABLE OF BEING PROGRAMMED AS SUPERVISORY MAY NOT BE PROPERLY PROGRAMMED AT INSTALLATION, RESULTING IN A FAILURE TO REPORT TROUBLE WHICH COULD RESULT IN DEATH, SERIOUS INJURY AND/OR PROPERTY DAMAGE.

PURCHASED PRODUCTS CONTAIN SMALL PARTS THAT COULD BE A CHOKING HAZARD TO CHILDREN OR PETS. KEEP ALL SMALL PARTS AWAY FROM CHILDREN AND PETS.

BUYER SHALL PASS ON THE FOREGOING INFORMATION ON PRODUCT RISKS, WARNINGS AND DISCLAIMERS TO ITS CUSTOMERS AND END USERS.

**WARRANTY DISCLAIMERS AND OTHER DISCLAIMERS**

ARDUINO HEREBY DISCLAIMS ALL WARRANTIES AND REPRESENTATIONS, WHETHER EXPRESS, IMPLIED, STATUTORY OR OTHERWISE INCLUDING (BUT NOT LIMITED TO) ANY WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE WITH RESPECT TO ITS PRODUCTS AND RELATED SOFTWARE.

ARDUINO MAKES NO REPRESENTATION, WARRANTY, COVENANT OR PROMISE THAT  ITS PRODUCTS AND/OR RELATED SOFTWARE (I) WILL NOT BE HACKED, COMPROMISED AND/OR CIRCUMVENTED; (II) WILL PREVENT, OR PROVIDE ADEQUATE WARNING OR PROTECTION FROM, BREAK-INS, BURGLARY, ROBBERY, FIRE; OR (III) WILL WORK PROPERLY IN ALL ENVIRONMENTS AND APPLICATIONS.

ARDUINO WILL NOT BE LIABLE FOR UNAUTHORIZED ACCESS (I.E. HACKING) INTO THE CLOUD SERVERS OR TRANSMISSION FACILITIES, PREMISES OR EQUIPMENT, OR FOR UNAUTHORIZED ACCESS TO DATA FILES, PROGRAMS, PROCEDURES OR INFORMATION THEREON, UNLESS AND ONLY TO THE EXTENT THAT THIS DISCLAIMER IS PROHIBITED BY APPLICABLE LAW.

SYSTEMS SHOULD BE CHECKED BY A QUALIFIED TECHNICIAN AT LEAST EVERY TWO YEARS UNLESS OTHERWISE INSTRUCTED IN THE PRODUCT DOCUMENTATION AND, IF APPLICABLE, THE BACKUP BATTERY REPLACED AS REQUIRED.

ARDUINO MAY MAKE CERTAIN BIOMETRIC CAPABILITIES (E.G., FINGERPRINT, VOICE PRINT, FACIAL RECOGNITION, ETC.) AND/OR DATA RECORDING CAPABILITIES (E.G., VOICE RECORDING), AND/OR DATA/INFORMATION RECOGNITION AND/OR TRANSLATION CAPABILITIES AVAILABLE IN PRODUCTS ARDUINO MANUFACTURES AND/OR RESELLS. ARDUINO DOES NOT CONTROL THE CONDITIONS AND METHODS OF USE OF PRODUCTS IT MANUFACTURES AND/OR RESELLS. THE END-USER AND/OR INSTALLER AND/OR DISTRIBUTOR ACT AS CONTROLLER OF THE DATA RESULTING FROM USE OF THESE PRODUCTS, INCLUDING ANY RESULTING PERSONALLY IDENTIFIABLE INFORMATION OR PRIVATE DATA, AND ARE SOLELY RESPONSIBLE TO ENSURE THAT ANY PARTICULAR INSTALLATION AND USE OF ARDUINO’S PRODUCTS COMPLY WITH ALL APPLICABLE PRIVACY AND OTHER LAWS, INCLUDING ANY REQUIREMENT TO OBTAIN CONSENT FROM OR PROVIDE NOTICE TO INDIVIDUALS AND ANY OTHER OBLIGATIONS END-USER AND/OR INSTALLER MAY HAVE AS CONTROLLERS OR OTHERWISE UNDER LAW. THE CAPABILITY OR USE OF ANY PRODUCTS MANUFACTURED OR SOLD BY ARDUINO TO RECORD CONSENT SHALL NOT BE SUBSTITUTED FOR THE CONTROLLER’S OBLIGATION TO INDEPENDENTLY DETERMINE WHETHER CONSENT OR NOTICE IS REQUIRED, NOR SHALL SUCH CAPABILITY OR USE SHIFT ANY OBLIGATION TO OBTAIN ANY REQUIRED CONSENT OR NOTICE TO ARDUINO.

THE INFORMATION IN THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. UPDATED INFORMATION CAN BE FOUND ON OUR WEB PRODUCT PAGE. ARDUINO ASSUMES NO RESPONSIBILITY FOR INACCURACIES OR OMISSIONS AND SPECIFICALLY DISCLAIMS ANY LIABILITIES, LOSSES, OR RISKS, PERSONAL OR OTHERWISE, INCURRED AS A CONSEQUENCE, DIRECTLY OR INDIRECTLY, OF THE USE OR APPLICATION OF ANY OF THE CONTENTS OF THIS DOCUMENT.

THIS PUBLICATION MAY CONTAIN EXAMPLES OF SCREEN CAPTURES AND REPORTS USED IN DAILY OPERATIONS. EXAMPLES MAY INCLUDE FICTITIOUS NAMES OF INDIVIDUALS AND COMPANIES. ANY SIMILARITY TO NAMES AND ADDRESSES OF ACTUAL BUSINESSES OR PERSONS IS ENTIRELY COINCIDENTAL.

REFER TO THE DATA SHEET AND USER DOCUMENTATION FOR INFORMATION ON USE. FOR THE LATEST PRODUCT INFORMATION, CONTACT YOUR SUPPLIER OR VISIT THE PRODUCT PAGES ON THIS SITE.
