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

The **Arduino UNO** is our most popular and important line of development boards, and has become a staple in the maker community and education since its release. The **Arduino UNO R4 WiFi** is a new flavour of UNO, and in this cheat sheet you will a collection of links to resources and guides to let you take advantage of all the improvements from the previous revisions of this board. The **UNO R4 WiFi** comes with a large 12x8 LED Matrix that you can create animations and simple graphics with, as well as an onboard ESP32-S3 module giving the board WiFi and Bluetooth functionality.

The ESP32 module and the Renesas RA4M1-chip are part of a sophisticated USB-Serial system that is highly flexible and adaptive to allow for HID features while still keeping the ability to program both the main MCU, and the ESP32, if you so wish (Although this is an advanced option and requires some hacking).

You can also visit the documentation platform for the [Arduino UNO R4 WiFi](/hardware/uno-r4-wifi)  

## Datasheet 
The full datasheet is available as a downloadable PDF from the link below:

- [Download the UNO R4 WiFi datasheet](/resources/datasheets/ABX00087-datasheet.pdf)

## Arduino IoT Cloud
The UNO R4 WiFi is compatible with the [Arduino IoT Cloud](https://create.arduino.cc/iot/things), a cloud service that allows you to create IoT applications in just minutes.

***Visit the [Getting Started with Arduino IoT Cloud](/arduino-cloud/getting-started/iot-cloud-getting-started) guide for more information.***

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

The way this is implemented on the UNO R3 also means that the board is not able to emulate an HID device, such as a keyboard or a mouse. This is, however, not true for the UNO R4.

### USB Bridge
As mentioned, by default the ESP32 is acting as a serial bridge, however if you wish you can change this and get direct access to the serial bus on the RA4M1 MCU either with software or hardware. 

1. Software - By pulling D40 to HIGH you will close the circuit that controls which MCU is connected to USB. While D40 is HIGH, the RA4M1 is connected to the USB Serial port.
  You can do this by including the following code in `void setup()`
  ```arduino
  pinMode(40, OUTPUT);
  digitalWrite(40, HIGH);
  ```
2. On the back of the UNO R4 WiFi you will find solder pads labelled "RA4M1 USB". If you create a short circuit between these pads, by for example creating a bridge across them with solder, the RA4M1 will be connected to the USB Serial port, instead of the ESP32.

![RA4M1 USB solder pads](./assets/RA4M1-usb.png)

### WiFi

### Bluetooth

### Programming the ESP32 (Advanced)
The ESP32 can be programmed individually from the RA4M1, with access to the data lines in the ESP header. By default, the ESP32's is used mainly as a radio module using Wi-Fi and Bluetooth®.

Overwriting the ESP32's firmware disrupts the communication between the two MCUs, but enables them to act independently. 

To reprogram the ESP32 board you can find UART-pads next to the ESP32 Module, that are laid out as shown in the image below:

![Exposed ESP32 pads](./assets/ESP32-pads.png)

## LED Matrix
The LED Matrix on the UNO R4 WiFi is available to use in your program, to display still graphics, animations, or even play games on. Bundled in the core for the UNO R4 is a library for displaying frames on the matrix.

### LED_Matrix
Initialise a LED_matrix by for example adding this code to the start of your sketch:
```arduino
LED_matrix matrix;
```

### LED_Matrix.load()
If you've written your sketch to hold your frames as child-arrays inside of a parent-array, `load()` can be used to load the parent-array, as such:

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

### LED_Matrix.begin()
The `begin()` method starts displaying the frames you have loaded into the matrix buffer one after the other.

### LED_Matrix.autoscroll()
`autoscroll()` lets you set an automatic time interval for the matrix to move to the next frame, and is used as such:

```arduino
  matrix.autoscroll(300);
```

### LED_Matrix.next()
`next()` will manually let you move to the next frame, if the autoscroll is not suitable for your program.

### LED_Matrix.on()
`on()` will manually turn a single pixel on.

### LED_Matrix.off()
`off()` will manually turn a single pixel off. 