---
title: "Getting Started with Alvik"
difficulty: beginner
description: "Discover how to use and program Alvik's robot"
tags:
  - Robot
author: "Paolo Cavagnolo"
---

Arduino® Alvik is a powerful and versatile robot specifically designed for programming and STEAM education.

![Alvik's Robot](assets/alvik_main.jpg)

Powered by the Arduino® Nano ESP32, Alvik offers diverse learning paths through different programming languages including MicroPython, Arduino C, and block-based coding; enabling different possibilities to explore Robotics, IoT and Artificial Intelligence.

In this tutorial you will find useful information to get started, test and maintain Alvik.

## Alvik's First Use

![Selecting one of the ready-to-go examples](assets/select-examples.gif)

Your Alvik robot is equipped with three ready-to-go examples. To choose one of the examples, just turn your Alvik ON, wait until the LEDs turn blue and use the Up and Down buttons to pick one color, then hit the "tick" confirmation button. It's that easy!

* **Red Program (Touch Mode):** Use the arrows to tell your robot what to do: up and down for moving forward and backward by 10 cm, and left and right for turning 90 degrees in each of the directions. The robot will collect instructions until you press the "tick" confirmation button. Once you press it, the robot will execute all the actions in order.

* **Green Program (Hand Follower):** Your robot will keep a steady 10 cm distance from your hand or any object you put in front of it. Press the "tick" confirmation button again to make the robot start following your hand.

* **Blue Program (Line Follower):** Your robot will glide along a black line on a white surface. Press the "tick" confirmation button again to make the robot follow the line. You can stop the robot at any moment by pressing the "X" cancel button. __The recommended size for the "black line" to follow is between 2-3 cm wide.__

***The product is sensitive to electrostatic discharge, observe ESD-safe handling procedures when working with it***

Now that you have played with Alvik and have seen it moving, it is time to know more in-depth how it is built and how to get much more than the out-of-the-box experience from it.

## Alvik in Detail

![Unboxing Alvik](assets/unboxing.jpg)

To get started to play with Alvik you will need the following hardware and software:

### Hardware Requirements

- Alvik (x1)
- USB-C® to USB-C® cable (x1)
- Phillips Screwdriver (cross head) (x1)
- Computer (X1)

***Make sure the UCB-C® cable you are using works with data lines, not only power lines***

### Software Requirements

- Operating Systems: All the major Operating Systems are supported
- [Arduino Lab for Micropython](https://labs.arduino.cc/en/labs/micropython)

## Alvik Overview

![Alvik exploded view](assets/main-components.png)

***When the PCB is out of the chassis and the battery is in place there is the risk of short-circuiting the 18650 Li-Ion battery. If you remove the hardware from the chassis make sure you do it on a __non-conductive surface clean__ of materials or tools that can short-circuit the battery***

### Main Components

Alvik is a robot with two controllers and tons of useful sensors and actuators. The main controller is the Arduino Nano ESP32 attached at the top of the robot while there is an STM32 controller integrated into the robot that takes care of the low-level commands like reading the sensors and moving the motors.

![Alvik top components](assets/up-components.png)

![Alvik bottom components](assets/down-components.png)

#### Nano ESP32

The [Nano ESP32](https://store.arduino.cc/products/nano-esp32) is the board used to control Alvik, it has a quick processor, large flash memory and Wi-Fi® enabled chip packed into a tiny circuit board.

***You can find out more about this board in the [Nano ESP32 documentation](/hardware/nano-esp32).***

Please note that when using MicroPython the pin number reflects the GPIO on the ESP32-S3, not the Nano board. Use the **green labeled number** in the following image. You can read more about this [here](https://docs.arduino.cc/micropython/micropython-course/course/introduction-python#nano-esp32--micropython-pinout).

![Nano ESP32 pinout](assets/esp-pinout.png)

#### STM32

The main core of the robot is the STM32 ARM Cortex-M4 32 Bit, you can access it through a set of dedicated APIs from the Nano ESP32.

You can learn more about the available functions for Alvik in the following [ Alvik's API Documentation](/tutorials/alvik/api-overview/).

The latest firmware of the STM32 can be found at [this link](https://github.com/arduino-libraries/Arduino_AlvikCarrier/releases), and [here](#how-to-upload-firmware) is the guide to flash it.


#### ON/OFF Switch

![Switch on](assets/robot-on.png)

At the back-right side of Alvik there is the main switch of the robot. When ON the robot will power up and it will execute the already loaded program.

***While programming the terminal of the Arduino Lab for MicroPython will notify you if you forgot to switch on the robot. Keep the robot off while programming to avoid undesired movements and remember to turn it on when you are ready to execute your program***

![Notification to switch on](assets/message-switch-on.png)

#### Battery

The battery is a rechargeable Li-ion 18650. It is located in the bottom part of Alvik, to access it you need to remove one Phillip's screw and take out the plastic holder.

![Charging blink](assets/battery_holder.jpg)

The Nano ESP32 can report the status of the battery through the terminal of the Arduino Lab for MicroPython and with its RGB status LED. To do that you need to call the `Alvik.begin()` function in any program or directly at the command line area.

When the battery is charging the status LED will blink RED for one second.

![Charging blink](assets/charging.gif)

![Terminal notification](assets/ide-charging.png)

When fully charged it will stay GREEN.

![Alvik fully charged - Green LED](assets/charged.png)

***Don't confuse the RGB status LED with the power ON LED of the Nano ESP32, which is always green.***

#### Sensors

Alvik has five different sensors, all connected to the STM32 and accessible through the [APIs](/tutorials/alvik/api-overview/). For each sensor there is a test example program that you can find in the _examples_ folder in [this repository](https://github.com/arduino/arduino-alvik-mpy/tree/main/examples).

| **Sensor name**              | **Part name** | **Test program name** |
|------------------------------|---------------|-----------------------|
| RGB Color detection          | APDS 9660     | read_color_sensor.py  |
| ToF 8x8 Array - up to 350 cm | LSM6DSOX      | read_tof.py           |
| IMU - 6 degree               | VL53L7CX      | read_imu.py           |
| 3x Line follower             | custom made   | line_follower.py      |
| 7x Touch sensor              | AT42QT2120    | read_touch.py         |

***Before using the ToF sensor check if it has a yellow protective film, if present, remove it from the sensor to ensure it works properly***

#### Actuators

Alvik has two high-precision geared motors and two RGB LEDs. The test programs are located in the same folder as the [sensor examples](#sensors).

| **Actuator name**        | **Part name**           | **Test program name** |
|--------------------------|-------------------------|-----------------------|
| Geared motors w/ encoder | GM12-N20VA-08255-150-EN | wheels_positions.py   |
| RGB LEDs                 | RGB LEDs                | leds_settings.py      |

#### Connectors

The connectors are placed in the back of the robot, the pinout is shown in the following image:

![Connectors Pinout](assets/datasheet_connectors.png)

## Coding Alvik

![Alvik USB Connection](assets/connecting-final.gif)

In order for Alvik to work properly three things have to be set correctly:

1. The Nano ESP32 needs the [MicroPython firmware](https://labs.arduino.cc/en/labs/micropython) on it.
2. The [latest libraries](https://github.com/arduino/arduino-alvik-mpy/releases) have to be placed in the Nano ESP32.
3. The [latest firmware](https://github.com/arduino-libraries/Arduino_AlvikCarrier/releases) has to be uploaded to the STM32 microcontroller.

Alvik comes with a preinstalled version of libraries and firmware, but in case you want to upgrade it or if something happens and you mess things up, here is the guide to reinstall both libraries and firmware.

### MicroPython Firmware on the Nano ESP32

Download and install the [Arduino Lab for MicroPython](https://labs.arduino.cc/en/labs/micropython), if you are able to connect the Arduino Nano ESP32 it means that you're board is ready. You have to see the **CONNECTED** yellow label at the bottom.

![Connection Succeeded](assets/connection_succeeded.png)

If something goes wrong it means you need to upload the MicroPython firmware on the Nano ESP32.

Follow [this guide](https://docs.arduino.cc/micropython/basics/board-installation/).

### How to Upload Libraries

You will find the latest instructions directly in the [repository](https://github.com/arduino/arduino-alvik-mpy/releases). Here are the main steps:

1. Prepare file

Download the repository and extract all the files in a specific folder that will become the main Alvik folder.

2. Remove old files

Open **Arduino Lab for MicroPython** and **connect** Alvik. Then:

- Click on the `files` icon

- Click on a `files name` in the bottom left explorer windows.

- Click on the `bin` icon to delete it

- Repeat for all the files, from all folders

![Delete all files](assets/delete_files.png)

3. Install mpremote

[mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html) is a Python module needed to upload files on the Nano ESP32. The minimum suggested mpremote release is 1.22.0. Be sure to have Python installed before proceeding!

```
(venv)$ pip install mpremote
```

or

```
(venv)$ python3 -m pip install mpremote
```

Depending on how you configure Python on your machine.

4. Install library

Run the following line to upload all files and download the dependencies needed to run the Arduino Alvik MicroPython library.

Linux
```
$ ./install.sh -p <device port>
```

Windows
```
> install.bat -p <device port>
```

The `install.*` script will copy all the needed files into your Alvik.

The `<device port>` is the name of the USB port that your computer assigned to the Nano ESP32. There are several ways to find it, depending on your OS, for example:

- You can use the Arduino IDE to discover the port, [follow this guide to know more.](https://support.arduino.cc/hc/en-us/articles/4406856349970-Select-board-and-port-in-Arduino-IDE)
- You can check it by using the Arduino Lab for MicroPython by clicking `Connect` after connecting Alvik with the USB cable.
- You can check the list of the USB devices attached to your PC.

### How to Upload Firmware

1. Download the latest [pre-compiled firmware](https://github.com/arduino-libraries/Arduino_AlvikCarrier/releases/latest) and place it inside Alvik's project folder

2. Go into `utilities` folder and run the `flash_firmware` script:


Linux
```
$ ./flash_firmware.sh -p <device port> <path-to-your-firmware>
```

Windows
```
> flash_firmware.bat -p <device port> <path-to-your-firmware>
```
Answer `y` to flash firmware.

### Test

There are several examples to test all the features of your Alvik placed inside the `examples` folder.

Open **Arduino Lab for MicroPython** and **connect** Alvik. Then:

1. Click on the `files` icon
2. Click on the `path string` in the bottom right explorer windows.
3. Click on the `file name` of the example you choose
4. Click on the `play button`

![Test examples files](assets/test_files.png)

## Maintenance

### Check Wheels Alignment

The motion calculations performed by Alvik are based on the precise position of both wheels. You can check this position and correct it in case you think your robot is not moving as expected:

1. Place your Alvik on a side on a flat surface
2. Check that the exterior part of the wheel is in contact with the flat surface and aligned with the plastic chassis
3. Repeat with the other wheel

![Check wheel alignment](assets/wheels_alignment.png)

### Calibrate Color Sensors

To calibrate the color sensor, placed in the bottom PCB under the Nano ESP32, you'll need a white surface and a black surface. Follow these steps:

1. Open the Arduino Lab for MicroPython
2. Connect Alvik
3. Open the REPL terminal (just click on the Terminal Icon on top)

Now you're ready to send commands directly to Alvik. Every time you click enter the command will be executed in real time.

```bash
 from arduino_alvik import ArduinoAl

 alvik = ArduinoAlvi

 alvik.begin()
```

Now place your robot on the white surface and type:

```bash
alvik.color_calibration('white')
```

Now place your robot on the black surface and type:

```bash
alvik.color_calibration('black')
```

Press reset on Lab for MicroPython.

You can now test using read_color_sensor.py in the examples folder. Refer to the [test chapter](#test) if you have any problems.

***Colors are tested on paper painted using acrylic marker pens, such as UNIPOSCA, or paper printed with an inkjet printer.***

## Extensions

***When adding extensions to the robot, never use screws longer than 10 mm or the device could be damaged.***

### Add LEGO® Addons

On both sides of Alvik there are different housings that let you add:

- 4x M3 screws per side
- 2x LEGO® Technic™ Connector per side

The dimensions are:

![Addons dimensions](assets/holes_dimensions.png)

As reference you can take a look at the following images:

![Alvik screws compatibility connectors](assets/screw_lego.png)

![Alvik LEGO® compatibility connectors](assets/lego.png)

### Add Servo Motors

The servo motors connectors are placed at the back of Alvik, in this tutorial we'll attach a servo motor to the port A. You can take a look at the pinout image in the [pinout](#3.2.7-connectors) chapter](#connectors).

***The port provides 5 Volt to the motor, so be sure to connect a servo that runs with 5V.***

1. Connect the servo motor to the upper port

    ![Servo connected](assets/servo_connection.png)

2. Open the Arduino Lab for MicroPython

3. Connect Alvik with a USB cable and click CONNECT

4. Copy and paste the following test code

```arduino
from arduino_alvik import ArduinoAlvik

import time

alvik = ArduinoAlvik()

alvik.begin()

while True:
    alvik.set_servo_positions(0,0)
    time.sleep(2)
    alvik.set_servo_positions(90,0)
    time.sleep(2)
    alvik.set_servo_positions(180,0)
    time.sleep(2)
    alvik.set_servo_positions(90,0)
    time.sleep(2)
```

5. Click on the PLAY button to run the test code

6. The motor should move as in the gif below

    ![Servo movement](assets/servo_move.gif)

If you want to understand how the command `alvik.set_servo_positions` works, you can have a look in the [API overview](/tutorials/alvik/api-overview/).

### Add I2C Grove

The I2C Grove connectors are placed at the back of Alvik, in this tutorial we'll see how to scan a generic I2C device connected to it. You can take a look at the pinout image at [Arvik's Product Page](/hardware/alvik/).

1. Connect the I2C Groove device to one of the two ports.

2. Open the Arduino Lab for MicroPython

3. Connect Alvik with a USB cable and click CONNECT

4. Turn ON Alvik

5. Copy and paste the following test code

```arduino
from machine import I2C
from machine import Pin

i2c = I2C(0, scl=Pin(12, Pin.OUT), sda=Pin(11, Pin.OUT))

print()
print('Scan i2c bus...')
print()

devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))
print()

for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device))

print()
```

5. Click on the PLAY button to run the test code

6. Look at the terminal to see the list of the I2C devices

### Add Qwiic

The Qwiic connectors are placed at the back of Alvik, for this example we'll be using the Qwiic OLED display from SparkFun. You can take a look at the pinout image in the [pinout](#3.2.7-connectors) chapter](#connectors).

![Qwiic OLED display](assets/qwiic_oled.png)

1. Connect the OLED display to one of the Qwiic connectors, you can use either the left one or the right one.

![Qwiic OLED display](assets/qwiic_connection.png)

2. We've prepared the example code and the libraries in [this](assets/qwiic_display.zip) zip file.

3. Extract the files and open the folder

4. Install mpremote

[mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html) is a Python module needed to upload files on the Nano ESP32. The minimum suggested mpremote release is 1.22.0. Be sure to have Python installed before proceeding!

```
(venv)$ pip install mpremote
```

or

```
(venv)$ python3 -m pip install mpremote
```

Depending on how you configure Python on your machine.

5. Install library

Run the following line to upload all files and download the dependencies needed to run the Arduino Alvik MicroPython library.


Linux
```
$ ./install_oled_lib.sh -p <device port>
```
Windows
```
> install_oled_lib.bat -p <device port>
```

The `<device port>` is the name of the USB port that your computer assigned to the Nano ESP32. There are several ways to find it, depending on your Operating System, for example:

- You can use the Arduino IDE to know the port by [following this guide](https://support.arduino.cc/hc/en-us/articles/4406856349970-Select-board-and-port-in-Arduino-IDE).
- You can look it using the Arduino Lab for MicroPython by clicking `Connect` after have connected the Alvik with the USB cable.
- You can look at the list of the USB devices attached to the PC

6. Test `Hello World!`

Now you can open the Arduino Lab for MicroPython, connect Alvik and open the example called `hello_world.py` in the `examples` folder. If everything works as expected you'll see something like the following image:

![Hello World OLED](assets/hello.png)

7. Test `bender.py`

Open the example called `bender.py`, launch it and see on your display the image of Bender's robot.
