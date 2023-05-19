---
title: "Arduino Pro Mini"
description: "This board was developed for applications and installations where space is premium and projects are made as permanent set ups. Small, available in 3.3 V and 5 V versions, powered by ATmega328P."
url_guide: "https://www.arduino.cc/en/Guide/ArduinoProMini"
coverImage: "assets/e000025_featured.jpg"
sku: "E000025"
source: "https://store.arduino.cc/arduino-pro-mini"
---

***Note: This page refers to a product that is retired.***

![The Arduino Pro Mini board](./assets/e000025_featured.jpg)

The **Arduino Pro Mini** is a microcontroller board based on the [ATmega328P](http://www.atmel.com/Images/Atmel-8271-8-bit-AVR-Microcontroller-ATmega48A-48PA-88A-88PA-168A-168PA-328-328P_datasheet.pdf).  

It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, an on-board resonator, a reset button, and holes for mounting pin headers. A six pin header can be connected to an FTDI cable or Sparkfun breakout board to provide USB power and communication to the board.  
The Arduino Pro Mini is intended for semi-permanent installation in objects or exhibitions. The board comes without pre-mounted headers, allowing the use of various types of connectors or direct soldering of wires. The pin layout is compatible with the Arduino Mini.   

There are two version of the Pro Mini. One runs at 3.3V and 8 MHz, the other at 5V and 16 MHz.   

The Arduino Pro Mini was designed and is manufactured by SparkFun Electronics.

You can find [here](https://www.arduino.cc/en/Main/warranty) your board warranty information.

## Getting Started

You can find in the [Getting Started section](https://www.arduino.cc/en/Guide/ArduinoProMini) all the information you need to configure your board, use the [Arduino Software (IDE)](https://www.arduino.cc/en/Main/Software), and start tinker with coding and electronics.

### Need Help?

* On the Software [on the Arduino Forum](https://forum.arduino.cc/index.php?board=63.0)
* On Projects [on the Arduino Forum](https://forum.arduino.cc/index.php?board=3.0)
* On the Product itself through [our Customer Support](https://support.arduino.cc/hc)

## Documentation 

### OSH: Schematics

Arduino Pro Mini is open-source hardware! You can build your own board using the following files:

[EAGLE FILES IN .ZIP](https://www.arduino.cc/en/uploads/Main/arduino-pro-mini-reference-design.zip) 

[SCHEMATICS IN .PDF](https://www.arduino.cc/en/uploads/Main/Arduino-Pro-Mini-schematic.pdf)

### Power

The Arduino Pro Mini can be powered with an FTDI cable or breakout board connected to its six pin header, or with a regulated 3.3V or 5V supply (depending on the model) on the Vcc pin. There is a voltage regulator on board so it can accept voltage up to 12VDC. If you're supplying unregulated power to the board, be sure to connect to the "RAW" pin on not VCC.  
The power pins are as follows: 

**RAW** For supplying a raw voltage to the board.  
**VCC** The regulated 3.3 or 5 volt supply.  
**GND** Ground pins. 

### Memory

The ATmega328P has 32 kB of flash memory for storing code (of which 0.5kB is used for the bootloader). It has 2 kB of SRAM and 1kBs of EEPROM (which can be read and written with the [EEPROM library](http://www.arduino.cc/en/Reference/EEPROM). 

### Input and Output

Each of the 14 digital pins on the Pro Mini can be used as an input or output, using [pinMode](https://www.arduino.cc/reference/en/language/functions/digital-io/pinmode/),[digitalWrite](https://www.arduino.cc/reference/en/language/functions/digital-io/digitalwrite/), and [digitalRead](https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/) functions. They operate at 3.3 or 5 volts (depending on the model). Each pin can provide or receive a maximum of 40 mA and has an internal pull-up resistor (disconnected by default) of 20-50 kOhms. In addition, some pins have specialized functions:

* **Serial: 0 (RX) and 1 (TX).** Used to receive (RX) and transmit (TX) TTL serial data. These pins are connected to the TX-0 and RX-1 pins of the six pin header.
* **External Interrupts: 2 and 3.** These pins can be configured to trigger an interrupt on a low value, a rising or falling edge, or a change in value. See the [attachInterrupt](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/) function for details.
* **PWM: 3, 5, 6, 9, 10, and 11.** Provide 8-bit PWM output with the [analogWrite](https://www.arduino.cc/reference/en/language/functions/analog-io/analogwrite/) function.
* **SPI: 10 (SS), 11 (MOSI), 12 (MISO), 13 (SCK).** These pins support SPI communication, which, although provided by the underlying hardware, is not currently included in the Arduino language.
* **LED: 13.** There is a built-in LED connected to digital pin 13\. When the pin is HIGH value, the LED is on, when the pin is LOW, it's off.
  
The Pro Mini has 8 analog inputs, each of which provide 10 bits of resolution (i.e. 1024 different values). Four of them are on the headers on the edge of the board; two (inputs 4 and 5) on holes in the interior of the board. The analog inputs measure from ground to VCC. Additionally, some pins have specialized functionality:

* **I2C: A4 (SDA) and A5 (SCL).** Support I2C (TWI) communication using the [Wire library](https://www.arduino.cc/reference/en/language/functions/communication/wire/).

There is another pin on the board:

* **Reset.** Bring this line LOW to reset the microcontroller. Typically used to add a reset button to shields which block the one on the board.

### Communication

The Arduino Pro Mini has a number of facilities for communicating with a computer, another Arduino, or other microcontrollers. The ATmega328P provides UART TTL serial communication, which is available on digital pins 0 (RX) and 1 (TX). The Arduino software includes a serial monitor which allows simple textual data to be sent to and from the Arduino board via a USB connection.  

A [SoftwareSerial library](http://www.arduino.cc/en/Reference/SoftwareSerial) allows for serial communication on any of the Pro Mini's digital pins.   

The ATmega328P also supports I2C (TWI) and SPI communication. The Arduino software includes a Wire library to simplify use of the I2C bus; see the [reference](https://www.arduino.cc/reference/en/language/functions/communication/wire/) for details. To use the SPI communication, please see the ATmega328P datasheet.

### Programming

The Arduino Pro Mini can be programmed with the Arduino software [download](https://www.arduino.cc/en/software). For details, see the [reference](https://www.arduino.cc/reference/en/) and [tutorials](https://docs.arduino.cc/tutorials/).   

The ATmega328P on the Arduino Pro Mini comes preburned with a [bootloader](https://docs.arduino.cc/hacking/software/Bootloader) that allows you to upload new code to it without the use of an external hardware programmer. It communicates using the original STK500 protocol [reference ](http://www.atmel.com/dyn/resources/prod_documents/doc2525.pdf), [C header files](http://www.atmel.com/dyn/resources/prod_documents/avr061.zip).   

You can also bypass the bootloader and program the ATmega328P with an external programmer; see [these instructions](https://docs.arduino.cc/hacking/software/Programmer) for details. 

### Automatic (Software) Reset

Rather then requiring a physical press of the reset button before an upload, the Arduino Pro Mini is designed in a way that allows it to be reset by software running on a connected computer. One of the pins on the six-pin header is connected to the reset line of the ATmega328P via a 100 nF capacitor. This pin connects to one of the hardware flow control lines of the USB-to-serial converter connected to the header: RTS when using an FTDI cable, DTR when using the Sparkfun breakout board. When this line is asserted (taken low), the reset line drops long enough to reset the chip. The Arduino software uses this capability to allow you to upload code by simply pressing the upload button in the Arduino environment. This means that the bootloader can have a shorter timeout, as the lowering of the reset line can be well-coordinated with the start of the upload.   

This setup has other implications. When the Pro Mini is connected to either a computer running Mac OS X or Linux, it resets each time a connection is made to it from software (via USB). For the following half-second or so, the bootloader is running on the Pro. While it is programmed to ignore malformed data (i.e. anything besides an upload of new code), it will intercept the first few bytes of data sent to the board after a connection is opened. If a sketch running on the board receives one-time configuration or other data when it first starts, make sure that the software with which it communicates waits a second after opening the connection and before sending this data. 

### Physical Characteristics

The dimensions of the Pro Mini PCB are approximately 0.7" x 1.3".

## Tech Specs

|                           |                                                |
| ------------------------- | ---------------------------------------------- |
| Microcontroller           | ATmega328P \*                                  |
| Board Power Supply        | 3.35 -12 V (3.3V model) or 5 - 12 V (5V model) |
| Circuit Operating Voltage | 3.3V or 5V (depending on model)                |
| Digital I/O Pins          | 14                                             |
| PWM Pins                  | 6                                              |
| UART                      | 1                                              |
| SPI                       | 1                                              |
| I2C                       | 1                                              |
| Analog Input Pins         | 6                                              |
| External Interrupts       | 2                                              |
| DC Current per I/O Pin    | 40 mA                                          |
| Flash Memory              | 32KB of which 2 KB used by bootloader \*       |
| SRAM                      | 2 KB \*                                        |
| EEPROM                    | 1 KB \*                                        |
| Clock Speed               | 8 MHz (3.3V versions) or 16 MHz (5V versions)  |

**Older boards were equipped with ATmega 168 with this specs:**   

- Flash memory: 16 KB  
- SRAM: 1 KB   
- EEPROM: 512 bytes