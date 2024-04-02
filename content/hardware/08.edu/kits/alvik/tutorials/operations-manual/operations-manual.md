---
title: 'Operations Manual'
description: 'Placeholder'
author: 'Placeholder'
tags:
	- edu
---

![](assets/title.png)

## 1. HW and SW Requirements
### 1.1 HW Req
### 1.2 SW Req

## 2. Alvik Overview
![](assets/main-components.png)
### 2.1 Warning Notes
Please read carefully the following notes:

***Disclaimer about the risk of short-circuiting the battery when the PCB is out of the chassis. Since it is Li-Ion battery if ti is shortcircuited it can burn***

***Information about the ESD logo we need to put on the HW announcing the product is sensible to electrostatic discharge***

***Information about the screws to use next to the LEGO compatibility holes***

***If present, remove the yellow protective film on the frontal sensor***

### 2.2 Main Components
![](assets/up-components.png)
![](assets/down-components.png)
#### 2.2.1 NANO ESP32
The [Nano ESP32](https://store.arduino.cc/products/nano-esp32) is the board used to control Alvik, it has a quick processor, large flash memory and Wi-Fi® enabled chip packed into a tiny circuit board.

***You can find out more about this board in the [Nano ESP32 documentation](/hardware/nano-esp32).***

Please note that when using MicroPython the pin number reflects the GPIO on the ESP32-S3, not the Nano board. Use the **green labeled number** in the following image. You can read more about this [here](https://docs.arduino.cc/micropython/micropython-course/course/introduction-python#nano-esp32--micropython-pinout).
![](assets/esp-pinout.png)
#### 2.2.2 STM32

#### 2.2.3 ON/OFF SWITCH (Focus On The Importance and Position)
![](assets/robot-on.png)

#### 2.2.4 BATTERY (Here How To Charge Battery And Check Status)

![](assets/charging.gif)
![](assets/ide-charging.png)
![](assets/charged.png)


#### 2.2.5 Inputs (Touch / Line Follow / ToF / Color / IMU)
#### 2.2.6 Outputs (LEDs / Motor + Movement Infos Like Max Speed)
#### 2.2.7 Connectors

## 3. Alvik Firmware
![](assets/connecting-final.gif)
### 3.1 How To Upload Last Firmware
### 3.2 API (Brief + Link To Cheat-Sheet)
### 3.3 Test (Simple)

## 4. Maintenance
### 4.1 Replace Battery
### 4.2 Check Wheels Alignment
### 4.3 Check / Calibrate Sensors (Here Color Calibrate Procedure)

## 5. Extensions
### 5.1 Repeat Warning About 15mm Screws
### 5.2 Add Servo
### 5.3 Add I2C Grove
### 5.4 Add Qwiic


