---
title: 'Arduino UNO R4 WiFi Cheat Sheet'
description: 'Learn how to set up the Arduino UNO R4 WiFi, the fourth revision of our most popular and important development board.'
tags:
  - Installation
  - I2C
  - SPI
  - UART
  - WiFi
  - Bluetooth
author: 'Jacob Hylén'
hardware:
  - hardware/02.hero/boards/uno-r4-wifi
software:
  - ide-v1
  - ide-v2
  - web-editor
---


The **Arduino UNO** is our most popular and globally recognized development board, and has become a staple in the maker community and education since its release. The **Arduino UNO R4 WiFi** board is part of the 4th revision of UNO boards, and the first to feature a 32-bit MCU (RA4M1 series from Renesas).

The **UNO R4 WiFi** features a large 12x8 LED Matrix that you can create animations and simple graphics with, as well as an onboard ESP32-S3 module giving the board Wi-Fi and Bluetooth® functionality. It also features a DAC and an Op-Amp.

This document serves as a technical overview for the UNO R4 WiFi, where you will a collection of links to resources and guides to help you get get started with your next project. 

The ESP32 module and the Renesas RA4M1-chip are part of a sophisticated USB-Serial system that is highly flexible and adaptive to allow for HID features while still keeping the ability to program both the main MCU, and the ESP32, if you so wish (Although this is an advanced option and requires some hacking).

You can also visit the documentation platform for the [Arduino UNO R4 WiFi](/hardware/uno-r4-wifi)  

## Datasheet 
The full datasheet is available as a downloadable PDF from the link below:

- [Download the UNO R4 WiFi datasheet](/resources/datasheets/ABX00087-datasheet.pdf)

## Power Supply

To power the UNO R4 WiFi you may either use a USB-C® cable, or the VIN pin.

If you’re using the USB-C® connector you must power it with 5V.

The board can be powered via the VIN pin, supporting a range between 6-24V.

## Installation

***For detailed instructions on how to install the UNO R4 WiFi core, please refer to the [Getting Started with the UNO R4 WiFi]() guide.***

The **UNO R4 WiFi** can be programmed through:

- the **IDE 1**, 
- the **IDE 2**, 
- and the **Web-Editor**. 

## Core

The UNO R4 WiFi is based on the [Arduino Core for Renesas devices](https://github.com/arduino/ArduinoCore-renesas).

## Renesas RA4M1

The UNO R4 WiFi features the powerful and very robust renesas microcontroller also found on the UNO R4 Minima. Renesas microcontrollers are known for their high performance and robustness, including their built in peripheral set. 

These peripherals include analog-to-digital converters, timers, pulse width modulation (PWM) units, communication interfaces (such as UART, SPI, and I2C) and more.

![Microcontroller on the UNO R4 WiFi](assets/R7FA4M1AB3CFM.png)

## Memory

### RAM

The **UNO R4 WiFi** comes equipped with 32 KB of RAM memory.

### Flash

The flash memory comes in 256 KB code and 8 KB data.

## Arduino IoT Cloud
The UNO R4 WiFi is compatible with the [Arduino IoT Cloud](https://create.arduino.cc/iot/things), a cloud service that allows you to create IoT applications in just minutes.

***Visit the [Getting Started with Arduino IoT Cloud](/arduino-cloud/getting-started/iot-cloud-getting-started) guide for more information.***

## SPI

![SPI Pins](assets/spipins.png)

The **UNO R4 WiFi** features a Serial Peripheral Interface (SPI) bus. The bus (connector), ‘SPI’ uses the following pins:


- (COPI) - D11
- (CIPO) - D12
- (SCK) - D13
- (CS) - D10

The following example shows how to use SPI:


```arduino
#include <SPI.h>

const int CS = 10;


void setup() {
  pinMode(CS, OUTPUT);

  SPI.begin();

  digitalWrite(CS, LOW);

  SPI.transfer(0x00);
  
  digitalWrite(CS, HIGH);
}

void loop() {
}
```

## I2C

I2C lets you connect multiple I2C compatible devices in series using only two pins. The controller will send out information through the I2C bus to a 7 bit address, meaning that the technical limit of I2C devices on a single line is 128. Practically, you're never gonna reach 128 devices before other limitations kick in.

The **UNO R4 WiFi** has one I2C bus which is marked with SCL and SDA. They are shared with A4 (SDA) and A5 (SCL) which owners of previous UNO's are familiar with. The pullups are not mounted on the PCB but there are footprints to do so if needed.

The pins used for I2C on the **UNO R4 WiFi** are the following:
- SDA - D14
- SCL - D15

![I2C Pins](assets/i2cpins.png)

To connect I2C devices you will need to include the [Wire](https://www.arduino.cc/reference/en/language/functions/communication/wire/) library at the top of your sketch.

```arduino
#include <Wire.h>
```

Inside `void setup()` you need to initialize the library, and initialize the I2C port you want to use.

```arduino
Wire.begin() //SDA & SDL
Wire1.begin(); //SDA1 & SDL1
Wire2.begin(); //SDA2 & SDL2
```

And to write something to a device connected via I2C, we can use the following commands:

```arduino
Wire.beginTransmission(1); //begin transmit to device 1
Wire.write(byte(0x00)); //send instruction byte 
Wire.write(val); //send a value
Wire.endTransmission(); //stop transmit
```

## Serial Ports


The **UNO R4 WiFi** supports, like every other Arduino board, serial communication with UART (Universal Asynchronous, Receiver-Transmitter). However, the **Uno R4 WiFi** board features 2 separate serial ports. 

This not only means that you may print different values to different ports and monitor them separately, which is useful enough in and of itself, but that you may also communicate with **2 different serial enabled devices** simultaneously.

The pins used for UART on the **UNO R4 WiFi** are the following:

- RX0 - D0
- TX0 - D1

Each Serial port works in the same way as the one you're used to, but you use different functions to target them:

```arduino
Serial.begin(9600);
Serial1.begin(9600);
```

To send and receive data through UART, we will first need to set the baud rate inside `void setup()`.

```arduino
Serial1.begin(9600);
```

To read incoming data, we can use a while loop() to read each individual character and add it to a string.

```arduino
  while(Serial1.available()){
    delay(2);
    char c = Serial1.read();
    incoming += c;
  }
```

And to write something, we can use the following command:

```arduino
Serial1.write("Hello world!");
```

## Pins

The **UNO R4 WiFi** gives you access to many different pins and many of them have special features that will be accounted for in the upcoming sections of this article. Keep reading to learn what you can do with them. 

If you just need a quick overview of the pins functionality, this is a full table of all the IO pins on the **UNO R4 WiFi** 

| Pin | Function  | Notes                      |
| --- | --------- | --------------------       |
| 0   | RX        | Serial communication       |
| 1   | TX        | Serial communication       |
| 2   | GPIO      | Digital IO pin             |
| 3   | PWM       | Digital IO pin, PWM        |
| 4   | GPIO      | Digital IO pin             |
| 5   | PWM       | Digital IO pin, PWM        |
| 6   | PWM       | Digital IO pin, PWM        |
| 7   | GPIO      | Digital IO pin             |
| 8   | GPIO      | Digital IO pin             |
| 9   | PWM       | Digital IO pin, PWM        |
| 10  | PWM       | Digital IO pin, PWM        |
| 11  | PWM       | Digital IO pin, PWM        |
| 12  | GPIO      | Digital IO pin             |
| 13  | GPIO      | Digital IO pin             |
| 14  | SDA       | Serial communication       |
| 15  | SCL       | Serial communication       |
| 16  | DAC       | Analog In, DAC             |
| 17  | OPAMP+    | Analog In, OPAMP+          |
| 18  | OPAMP-    | Analog In, OPAMP-          |
| 19  | OPAMP OUT | Analog In, OPAMP OUT       |
| 20  | GPIO      | Analog in, Digital IO pin  |
| 21  | GPIO      | Analog in, Digital IO pin  |
| A0  | DAC       | Analog In, DAC             |
| A1  | Analog in | Analog In                  |
| A2  | Analog in | Analog In                  |
| A3  | Analog in | Analog In                  |
| A4  | Analog in | Analog In                  |
| A5  | Analog in | Analog In                  |

### Analog Pins

The **UNO R4 WiFi** has 6 analog input pins (A0-A5) that can be read by using the `analogRead()` function.

```arduino
value = analogRead(pin, value);
```

The reference voltage of these pins is 3.3V. 


### PWM

PWM (Pulse Width Modulation) capability allows a digital pin to emulate analog output by flickering on and off very fast letting you, among other things, dim LEDs connected to digital pins. 

The **UNO R4 WiFi** has 6 PWM capable pins which are marked with ~ on the headers. The PWM capable pins are:

- D3~
- D5~
- D6~
- D9~
- D10~
- D11~

You may use them as analog output pins with the function: 

```arduino
analogWrite(pin, value);
```
The **RA4M1** has an internal OPAMP that is exposed on the **UNO R4 WiFi** as follows:

| Pin | OPAMP             |
| --- | ------------------|
| A1  | OPAMP +           |
| A2  | OPAMP -           |
| A3  | OPAMP OUT         |

### Digital Pins

The **UNO R4 WiFi** features a total of digital 14 pins. Though some of them serve another purpose and shouldn't be used for GPIO if you have other pins available.


| Pin | Function  | Notes                      |
| --- | --------- | --------------------       |
| 0   | RX        | Serial communication       |
| 1   | TX        | Serial communication       |
| 2   | GPIO      | Digital IO pin             |
| 3   | PWM       | Digital IO pin, PWM        |
| 4   | GPIO      | Digital IO pin             |
| 5   | PWM       | Digital IO pin, PWM        |
| 6   | PWM       | Digital IO pin, PWM        |
| 7   | GPIO      | Digital IO pin             |
| 8   | GPIO      | Digital IO pin             |
| 9   | PWM       | Digital IO pin, PWM        |
| 10  | PWM       | Digital IO pin, PWM        |
| 11  | PWM       | Digital IO pin, PWM        |
| 12  | GPIO      | Digital IO pin             |
| 13  | GPIO      | Digital IO pin             |
| 14  | SDA       | Serial communication       |
| 15  | SCL       | Serial communication       |

The reference voltage of all digital pins is 5V.

### DAC Pin

The **UNO R4 WiFi** also has a DAC pin (A0) that can act as genuine analog output pin which means it's even more capable than PWM pins.

```arduino
analogWrite(pin, value);
```

![DAC Pin](assets/dacpin.png)

This DAC pin has a default write resolution of 8-bits. This means that values that are written to the pin should be between 0-255.

However you may change this write resolution if you need to, to up to 12-bits, and in this case the values you write to the pin should be between 0-4096.

```arduino
analogWriteResolution(12);
```


## QWIIC Connector

The UNO R4 WiFi features a QWIIC/STEMMA connector that you can use to connect modules, often allowing you to daisy chain several modules and control all of them through a single connector.

QWIIC or STEMMA are both names for a type of connector developed by SparkFun and Adafruit respectively, that bundles the I2C pins of a development board and breakout modules. What this means is that if you have a development board (such as for example the Arduino UNO R4 WiFi) and a breakout module, and both have a QWIIC or STEMMA connector, you can hook them up together and with absolutely minimal wiring you can quickly create multi-faceted projects. 

If your breakout board features more than one of these connector, which many do, you can use the second one to daisychain *another* QWIIC module to add another interactive node to your project.

The UNO R4 WiFi features two I2C buses, and the QWIIC connector is connected to the secondary one. What this means is that if you are using the [Wire](https://reference.arduino.cc/reference/en/language/functions/communication/wire/) library, you will need to use the `Wire1` object rather than the `Wire` object, like the following example:

```arduino
#include <Wire.h>

void setup(){
  Wire1.begin();
  Wire1.beginTransmission(1);   //begin transmit to device 1
  Wire1.write(byte(0x00));      //send instruction byte 
  Wire1.write(val);             //send a value
  Wire1.endTransmission();      //stop transmit
}
```


## ESP32-S3-MINI-1-N8
By default, the ESP32-S3 module onboard the UNO R4 WiFi acts as a Serial bridge, handling the connection to your computer. It also handles the rebooting of the main MCU, the Renesas RA4M1 when it is needed, for example when receiving a new sketch and resetting.

On the UNO R3, the ATMEGA16U2 serves the same purpose. The onboard ESP32 module is a more advanced SoC, adding Wi-Fi® & Bluetooth® connectivity to the board.

The ESP32 also exposes the ESP32's data lines, so that you can program the ESP32 directly. These data lines are exposed by 3x2 header at the top of the board, or through pads on the bottom side.

***Please note that the ESP32 has a default firmware installed, which is set to communicate with the RA4M1 chip. Any direct programming of the ESP32 will override that firmware and the communication between the chips may be disrupted until the default firmware is restored ***

![UNO R4 & UNO R3](./assets/UNO-serial.png)

### USB Bridge
By default the ESP32 acts as a serial bridge between a computer and the RA4M1 MCU. The USB data lines are routed through switches, and by default, these switches are set for communication to go via the ESP32 module.

![Switches for Serial Communication.](./assets/RA4M1-usb-switches.png)

If you wish you can change this and get direct access to the serial bus on the RA4M1 MCU either with software or hardware. See the instructions below:

1. Software - By pulling D40 to HIGH you will close the circuit that controls which MCU is connected to USB. While D40 is HIGH, the RA4M1 is connected to the USB Serial port, and while D40 is LOW the ESP32 is connected, like the default configuration.
  You can do this by including the following code in `void setup()`
  ```arduino
  pinMode(40, OUTPUT);
  digitalWrite(40, HIGH);
  ```
2. On the back of the UNO R4 WiFi you will find solder pads labelled "RA4M1 USB". If you create a short circuit between these pads, by for example creating a bridge across them with solder, the RA4M1 will be connected to the USB Serial port, instead of the ESP32.

![RA4M1 USB solder pads](./assets/RA4M1-usb.png)

### Wi-Fi®

The ESP32 onboard the UNO R4 WiFi is used to give the board Wi-Fi® capabilities. The Wi-Fi module has a bitrate of up to 150 Mbps. The ESP32 module has a built in trace-antenna, meaning that you do not need an external one to use the connectivity features of the board. However, this trace antenna is shared with the Bluetooth® module, which means that you cannot use Bluetooth® and Wi-Fi® at the same time.

### Bluetooth®

Thanks to the ESP32 module, the UNO R4 WiFi has Bluetooth® LE and Bluetooth® 5 capabilities, at a speed of up to 2 Mbps. The ESP32 module has a built in trace-antenna, meaning that you do not need an external one to use the connectivity features of the board. However, this trace antenna is shared with the Bluetooth® module, which means that you cannot use Bluetooth® and Wi-Fi® at the same time.

### Programming the ESP32 (Advanced)

The ESP32 module and the Renesas RA4M1-chip are part of a sophisticated USB-Serial system that is highly flexible and adaptive to allow for HID features while still keeping the ability to program both the main MCU, and the ESP32, if you so wish. By default, the ESP32's is used mainly as a radio module using Wi-Fi and Bluetooth®.

Overwriting the ESP32's firmware disrupts the communication between the two MCUs, but enables them to act independently. 

To reprogram the ESP32 board you can either find UART-pads next to the ESP32 Module, that are laid out as shown in the image below:

![Exposed ESP32 pads](./assets/ESP32-pads.png)

or you can use the pins exposed directly on the ESP32 header, shown here:

![ESP-header](./assets/ESP32-header.png)

## LED Matrix
The LED Matrix on the UNO R4 WiFi is available to use in your program, to display still graphics, animations, or even play games on. Bundled in the core for the UNO R4 is a library for displaying frames on the matrix.

To learn about the LED matrix in depth, check out the [LED Matrix Guide](/tutorials/uno-r4-wifi/led-matrix/).

-  `Arduino_LED_Matrix matrix` - Initialises a LED matrix. 
-  `Arduino_LED_Matrix.load()` - Loads a frame into the frame buffer.
Here's a basic example:

```arduino
// creates an array of two frames
const uint32_t frames[][4] = {
  {
    0x0,
    0x0,
    0xc00c0000,
    150
  },
  {
    0x0,
    0x1e01,
    0x201201e0,
    150
  }
}

  // loads the frames into the matrix buffer
  matrix.load(frames);

  ```

- `Arduino_LED_Matrix.begin()` - Initialises the LED matrix itself, making it ready to display frames.
- `Arduino_LED_Matrix.autoscroll()` - Sets an automatic time interval in ms for the matrix to scroll through the frames.
- `Arduino_LED_Matrix.next()` -  Manually moves to the next frame.
- `Arduino_LED_Matrix.on()` -  Manually turn a single pixel on.
- `Arduino_LED_Matrix.off()` -  Manually turn a single pixel off.