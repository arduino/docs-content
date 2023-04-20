---
title: "LilyPad Arduino SimpleSnap"
description: "The LilyPad SimpleSnap is a new, easy way to create e-textiles projects with LilyPad that are modular and can be disassembled or broken down. The SimpleSnap includes a built-in rechargeable Lithium Polymer battery and female snap connectors."
url_guide: "https://www.arduino.cc/en/Guide/ArduinoLilyPad"
coverImage: "assets/store_e000059-featured_1.jpg"
sku: "E000059"
source: "https://store.arduino.cc/lilypad-arduino-simplesnap"
---

***Note: This page refers to a product that is retired.***

![The LilyPad Arduino SimpleSnap board](./assets/store_e000059-featured_1.jpg)

The **LilyPad Arduino SimpleSnap** is a microcontroller board designed for wearables and e-textiles. It is similar to the [LilyPad Arduino Simple](https://www.arduino.cc/en/Main/ArduinoBoardLilyPadSimple), except that it has a built in lithium polymer battery, and instead of through-holes, it has conductive snaps. By using matching snaps in your project, you can affix the LilyPad securely but remove it to wash your project or move it to another project. The LilyPad SimpleSnap has 9 pins for input/output. Additionally, it has a built in charging circuit for the battery. The board is based on the [ATmega328](http://www.atmel.com/assets/Atmel-8271-8-bit-AVR-Microcontroller-ATmega48A-48PA-88A-88PA-168A-168PA-328-328P_datasheet_Complete.pdf).  
  
The LilyPad Arduino SimpleSnap was designed and developed by Leah Buechley and SparkFun Electronics.

You can find your board warranty information [here](https://www.arduino.cc/en/Main/warranty).

## Getting Started

In the [Getting Started section](https://www.arduino.cc/en/Guide/ArduinoLilyPad), you can find all the information you need to configure your board, use the [Arduino Software (IDE)](https://www.arduino.cc/en/Main/Software), and start to tinker with coding and electronics. SparkFun Electronics has a [range of accessories](http://www.sparkfun.com/commerce/categories.php?c=135) for use with the LilyPad Arduinos.

### Need Help?

* On the board on the [LilyPad Arduino SimpleSnap Page](http://lilypadarduino.org/?p=289)
* On Projects [on the Arduino Forum](https://forum.arduino.cc/index.php?board=3.0)
* On the Product itself through [our Customer Support](https://support.arduino.cc/hc)

## Documentation

### OSH: Schematics

LilyPad Arduino SimpleSnap is open-source hardware! You can build your own board using the following files:

[EAGLE FILES IN .ZIP](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/E-Textiles/Lilypad/LilyPad-SimpleSnap-v13.zip) 

[SCHEMATICS IN .PDF](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/E-Textiles/Lilypad/LilyPad-SimpleSnap-v13.pdf)

### Power

The board can be turned on and off with the on-board switch. When the board is unplugged from an FTDI adapter and powered via its on-board battery, the switch turns the board on and off; with the switch in the ON position, the microcontroller receives power and the board runs and with the switch in the OFF position, the microcontroller doesn't receive power. When the board is powered via an FTDI adapter, the board remains on all of the time; with the switch in the ON position, the microcontroller receives power from the battery and with the switch in the OFF position, the microcontroller receives power from the FTDI adapter.

The Lilypad SimpleSnap's built in lithium polymer battery is the primary power source for the board. The board contains a MCP73831 LiPo battery charging chip. If the board is connected to an FTDI connection, the FTDI power will charge the battery. This is true regardless of the position of the power switch. The LED adjacent to the switch lights up while the battery is being charged. The charging will stop automatically when the battery is fully charged.

Because of the battery charging circuit, it is not possible to power components like a Bluetooth® modem via the FTDI connector.

### Programming

The LilyPad SimpleSnap can be programmed with the Arduino [Arduino Software](https://www.arduino.cc/en/Main/Software) (IDE). Select "LilyPad Arduino" from the **Tools > Board** menu. For details, see the [LilyPad Arduino Getting Started Guide](https://www.arduino.cc/en/Guide/ArduinoLilyPad).

The ATmega328 on the LilyPad Arduino SimpleSnap comes preburned with [bootloader](https://www.arduino.cc/en/Hacking/Bootloader?from=Tutorial.Bootloader) that allows you to upload new code to it with the Arduino software.

The LilyPad SimpleSnap does not have an onboard USBSerial adapter or USB connector. To program the board, you will need to use a FTDI compatible adapter like the [USBSerial Light Adapter](https://docs.arduino.cc/retired/boards/arduino-usb-2-serial-micro).

### Inputs and Outputs

The LilyPad SimpleSnap has fewer inputs and outputs than the [LilyPad Arduino Main Board](https://www.arduino.cc/en/Main/ArduinoBoardLilyPad). There are a total of 9 I/O pins on the SimpleSnap board, one exposed pin for +5VDC, and one pin for ground.

Each of the 9 digital I/O pins on the LilyPad Arduino SimpleSnap can be used as an input or output, using [pinMode()](https://www.arduino.cc/reference/en/language/functions/digital-io/pinmode/), [digitalWrite()](https://www.arduino.cc/en/Reference/DigitalWrite), and [digitalRead()](https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/) functions. They operate at 3.3V volts. Each pin can provide or receive a maximum of 40 mA and has an internal pull-up resistor (disconnected by default) of 20 kOhms. In addition, some pins have specialized functions:

* **PWM: 5, 6, 9, 10, 11** Provide 8-bit PWM output with the [analogWrite()](https://www.arduino.cc/en/Reference/AnalogWrite) function.
* **Analog Inputs: A2-A5**. The LilyPad Arduino SimpleSnap has 4 analog inputs, labeled A2 through A5, all of which can also be used as digital I/O. Each analog input provide 10 bits of resolution (i.e. 1024 different values). By default the analog inputs measure from ground to 5 volts, though is it possible to change the upper end of their range using the [analogReference()](https://www.arduino.cc/reference/en/language/functions/analog-io/analogreference/)function.

### Automatic (Software) Reset and Bootloader Initiation

Rather than requiring a physical press of the reset button before an upload, the LilyPad SimpleSnap Arduino is designed in a way that allows it to be reset by software running on a connected computer. The bootloader can also be initiated by pressing the reset button on the LilyPad Arduino SimpleSnap.

Because of the way the LilyPad Arduino SimpleSnap handles reset it's best to let the Arduino software try to initiate the reset before uploading. If the software can't reset the board you can always start the bootloader by pressing the reset button.

### Physical Characteristics

The LilyPad Arduino SimpleSnap is a circle, approximately 50mm (2") in diameter. The PCB is .8mm (1/32") thick (approximately 3mm (1/8") where electronics are attached).

### Washability

Because of the built in battery, you cannot wash the LilyPad Arduino SimpleSnap. It will ruin the board and battery if you do. Instead, you should detach the LilyPad before carefully hand-washing the rest of your project.


