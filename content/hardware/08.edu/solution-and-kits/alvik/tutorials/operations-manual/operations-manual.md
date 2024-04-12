title: 'Getting Started with Alvik'
difficulty: beginner
description: 'This short guide helps you to get started with Avlik, you'll also find useful information to maintain your Alvik.'
tags: [Robot]
hardware: - Arduino® Alvik



![](assets/title.png)

## 1. Requirements
In this manual you'll find useful information to test and maintain your Alvik. But before proceeding let's check to have all the essential tools, hardware and sotware. 

### 1.1 Hardware requirements

 - One Alvik, of course.
 - One USB-C® type cable, working and with data lines, not only power lines.
 - One screw driver, cross head
 - One computer

### 1.2 Software requirements

 - OS: all the major os are supported.
 - [Arduino Lab for Micropython](https://labs.arduino.cc/en/labs/micropython)

## 2. Alvik Overview
![](assets/main-components.png)
### 2.1 Warning notes
Please read carefully the following notes:

***When the PCB is out of the chassis and the battery is in place there is the risk of short-circuiting the 18650 Li-Ion battery***

***The product is sensible to electrostatic discharge***

***When adding extension in the side, never use screws longer then 15mm, overall never use objects longer then 15mm in the holes because the device can be damaged***

***If present, remove the yellow protective film on the frontal sensor***

### 2.2 Main components
![Alvik top components](assets/up-components.png)
![Alvik bottom components](assets/down-components.png)
#### 2.2.1 Nano ESP32
The [Nano ESP32](https://store.arduino.cc/products/nano-esp32) is the board used to control Alvik, it has a quick processor, large flash memory and Wi-Fi® enabled chip packed into a tiny circuit board.

***You can find out more about this board in the [Nano ESP32 documentation](/hardware/nano-esp32).***

Please note that when using MicroPython the pin number reflects the GPIO on the ESP32-S3, not the Nano board. Use the **green labeled number** in the following image. You can read more about this [here](https://docs.arduino.cc/micropython/micropython-course/course/introduction-python#nano-esp32--micropython-pinout).
![Nano ESP32 pinout](assets/esp-pinout.png)

#### 2.2.2 STM32

The main core of the robot is the STM32 ARM Cortex-M4 32 Bit, you can access it through a set of dedicated APIs from the Nano ESP32.

[Here](/tutorials/cheat-sheet/cheat-sheet.md) is the list of APIs.

The latest firmware of the STM32 can be found at [this link](https://github.com/arduino/arduino-alvik-mpy/releases), and [here](#how-to-upload-firmware) there is the guide to flash it.


#### 2.2.3 ON/OFF switch
![switch on](assets/robot-on.png)
On the back side of the robot, on the right, there is the main switch of the robot. When ON the robot will power up and it will execute the "main.py" routine, if present; also with USB cable disconnected.


During operation the terminal of the Arduino Lab for MicroPython will notify you if you forgot to switch on the robot.
![notification to switch on](assets/message-switch-on.png)

#### 2.2.4 Battery

The battery is a rechargeable Li-ion 18650. It is located in the bottom part of the Alvik, to access it you need to remove one screw and take out the plastic holder.

The Nano ESP32 can report the status of the battery through the terminal of the Arduino Lab for MicroPython and with its RGB status LED. To do that you need to call the `Alvik.begin()` function, in any program.

When the battery is charging the status LED will blink RED for 1 second.
![charging blink](assets/charging.gif)
![terminal notification](assets/ide-charging.png)

When fully charged it will stay GREEN.
![](assets/charged.png)

***Don't confuse the RGB status LED with the power ON LED of the Nano ESP32, that is always green.***

#### 2.2.5 Inputs

Alvik has five inputs, all linked to the STM32 and accessible through the [APIs](/tutorials/cheat-sheet/cheat-sheet.md). For every input there is a test example program that you can find in the _examples_ folder in [this](https://github.com/arduino/arduino-alvik-mpy/tree/main/examples) repository. 

| **Sensor name**              | **Part name** | **Test program name** |
|------------------------------|---------------|-----------------------|
| RGB Color detection          | APDS 9660     | read_color_sensor.py  |
| ToF 8x8 Array - up to 350 cm | LSM6DSOX      | read_tof.py           |
| IMU - 6 degree               | VL53L7CX      | read_imu.py           |
| 3x Line follower             | custom made   | line_follower.py      |
| 7x Touch sensor              | AT42QT2120    | read_touch.py         |

#### 2.2.6 Outputs

Alvik has 2 high precision geared motors and 2 RGB leds.

| **Actuator name**        | **Part name**           | **Test program name** |
|--------------------------|-------------------------|-----------------------|
| Geared motors w/ encoder | GM12-N20VA-08255-150-EN | wheels_positions.py   |
| RGB LEDs                 | RGB LEDs                | leds_settings.py      |

#### 2.2.7 Connectors

The connectors are placed in the back of the robot, the pinout is shown in the following image:

![connectors pinout](assets/datasheet_connectors.png)

## 3. Alvik code
![alvik usb connection](assets/connecting-final.gif)

In order to Alvik to work properly three things has to be set correctly:

 1. the Nano ESP32 needs the MicroPython firmware on it
 2. the last libraries have to be placed in the Nano ESP32
 3. the last firmware have to be uploaded to the STM32 microcontroller

Alvik comes with a preinstalled version of libraries and firmware, but in case you want to upgrade it or if something happened and you mess things up, heres is the guide to reinstall both libraries and firmware.

### 3.1 MicroPython firmware on the Nano ESP32

Download and install the [Arduino Lab for Micropython](https://labs.arduino.cc/en/labs/micropython), if you are able to connect the Arduino Nano ESP32 it means that you're board is ready. You have to see the **CONNECTED** yellow label at the bottom.

![connection succeeded](assets/connection_succeeded.png)

If something goes wrong it means you need to upload the MicroPython firmware on the Nano ESP32.
Follow [this guide](https://docs.arduino.cc/micropython/basics/board-installation/).

### 3.2 How to upload libraries



### 3.3 How to upload firmware
### 3.4 Test APIs

## 4. Maintenance
### 4.1 Check wheels alignment
### 4.2 Check / calibrate sensors (here color calibrate procedure)

## 5. Extensions
### 5.1 Repeat warning about 15mm screws
### 5.2 Add servo
### 5.3 Add i2c grove
### 5.4 Add qwiic

