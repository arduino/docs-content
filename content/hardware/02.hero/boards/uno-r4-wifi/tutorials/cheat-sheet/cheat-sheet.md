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
The Arduino UNO R4 WiFi is compatible with the [Arduino IoT Cloud](https://create.arduino.cc/iot/things), a cloud service that allows you to create IoT applications in just minutes.

***Visit the [Getting Started with Arduino IoT Cloud](/arduino-cloud/getting-started/iot-cloud-getting-started) guide for more information.***

## ESP32
By default, the ESP32-S3 module onboard the UNO R4 WiFi is acting as a Serial bridge, handling the connection to your computer as well as rebooting the main MCU, the Renesas RA4M1 when it is needed, for example when receiving a new sketch and resetting. On the UNO R3, there is an ATMEGA16U2 serving this exact purpose. The difference here is that the ESP32-S3 is much more capable, and the UNO R4 WiFi takes advantage of those capabilities by using its connectivity features, as well as  exposing the ESP32s data lines to make it programmable by itself.

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

### Programmable (Advanced)
A more advanced user will be able to program the ESP32 individually from the RA4M1, and even integrate them with each other to create what is essentially a multi-core development board. You could for example use the RA4M1 chip to read sensordata with high speed and send it to the ESP32 where it gets processed and then sent to a webserver, or logged in a spreadsheet, all without adding any extra hardware to your board apart from the sensors. 

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