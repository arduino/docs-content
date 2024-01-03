---
title: 'Getting Started with the Arduino Pro'
description: 'The first steps to setting up the Arduino Pro'
---

**This is a retired product** 

The [Arduino Pro](https://store.arduino.cc/arduino-pro) is intended for advanced users who require flexibility and low-cost. It comes with the minimum of components (no on-board USB or pin headers) to keep the cost down. It's a good choice for a board you want to leave embedded in a project. Please note that there are multiple variants of the board which operate at different voltages and clock speeds. You need to know if you have the 3.3V / 8 MHz version or the 5V / 16 MHz version.

The Arduino Pro is programmed using the [Arduino Software (IDE)](https://arduino.cc/en/Main/Software), our Integrated Development Environment common to all our boards and running both [online](https://create.arduino.cc/editor) and offline. For more information on how to get started with the Arduino Software visit the [Getting Started page](https://arduino.cc/en/Guide/HomePage).

### Use your Arduino Pro on the Arduino Web IDE



All Arduino boards, including this one, work out-of-the-box on the [Arduino Web Editor](https://create.arduino.cc/editor), you only need to install Arduino Create Agent to get started.

The Arduino Web Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow this [simple guide](https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-4b3e4a) to start coding on the browser and upload your sketches onto your board.





### Use your Arduino Pro on the Arduino Desktop IDE

If you want to program your Arduino Pro while offline you need to install the [Arduino Desktop IDE](https://arduino.cc/en/Main/Software)

The board comes without built-in USB circuitry, so an off-board USB-to-TTL serial converter must be used to upload sketches. For the 3.3V Arduino Pro boards, this can be a [FTDI TTL-232R-3V3 USB - TTL Level Serial Converter Cable](https://ftdichip.com/products/ttl-232r-3v3/) or the SparkFun[FTDI Basic Breakout Board (3.3V)](http://www.sparkfun.com/commerce/product_info.php?products_id=8772). For the 5V Arduino Pro boards, use a [TTL-232R USB - TTL Level Serial Converter](https://ftdichip.com/products/ttl-232r-5v/) or the SparkFun[FTDI Basic Breakout Board (5V)](http://www.sparkfun.com/commerce/product_info.php?products_id=9115). (You can probably also get away with using a 5V USB-to-serial converter with a 3.3V board and vice-versa, but it's not recommended.)

If using the FTDI cable on Windows, you'll need to make one configuration change to enable the auto-reset. With the board connected, open the Device Manager (in Control Panels > System > Hardware), and find the USB Serial Port under Ports. Right-click and select properties, then go to Port Settings > Advanced and check Set RTS on Close under Miscellaneous Options.

#### Open your first sketch

Open the LED blink example sketch: **File > Examples >01.Basics > Blink**.

#### Select your board type and port

For the 3.3V versions of the Arduino Pro, select **Arduino Pro or Pro Mini (3.3V, 8 MHz) w/ ATmega328P** or **Arduino Pro or Pro Mini (3.3V, 8 MHz) w/ ATmega168** from the **Tools > Board** menu (depending on the microcontroller on your board). For the 5V versions of the Arduino Pro, select **Arduino Duemilanove or Nano w/ ATmega328P** or **Arduino Diecimila, Duemilanove, or Nano w/ ATmega168**.

![](./assets/ArduinoProFTDICable.jpg)

_An Arduino Pro connected to (and powered by) an FTDI USB - TTL Level Serial Converter Cable. The green and yellow wires align with the words "green" and "yellow" written underneath the pins._

![](./assets/ArduinoProFTDIBreakout.jpg)

_The Arduino Pro connected to (and powered by) a SparkFun FTDI Basic Breakout Board (prototype version) and USB Mini-B cable._

The external USB-to-TTL serial converter will power the Arduino Pro, regardless of the position of the switch.

#### Upload and Run your first Sketch

To upload the sketch to the Arduino Pro, you need to press the upload button in the Arduino environment.

Click the **Upload** button in the upper left to load and run the sketch on your board:

![](./assets/UNO_Upload.png)

Wait a few seconds - you should see the RX and TX leds on the board flashing. If the upload is successful, the message "Done uploading." will appear in the status bar.

#### Learn more on the Desktop IDE

[See this tutorial](https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-the-arduino-software-ide-623be4) for a generic guide on the Arduino IDE with a few more infos on the Preferences, the Board Manager, and the Library Manager.

### Tutorials

Now that you have set up and programmed your Arduino Pro board, you may find inspiration in our [Project Hub](https://create.arduino.cc/projecthub) tutorial platform.

### Please Read...

#### Standalone usage

To use the board standalone, with no connection to a computer, it can be be powered by a battery or an external power supply (wall wart). You can solder the + and - wires of a battery connector to the corresponding holes on the board. For the 3.3V boards, you can connect a LiPo battery (with JST connector) to the JST jack. Alternatively, solder a DC power jack into the three large holes on the board, and connect a DC power supply (center positive). When the switch is in the "Batt" position, the board will draw power from an attached battery; when it is in the "Ext." position, power comes from an external power supply. In either position, the board can be powered by the 6-pin USB header.

![](./assets/ArduinoProBattery.jpg)

_A 3.3V Arduino Pro powered by a [2000 mAh LiPo battery](https://www.sparkfun.com/commerce/product_info.php?products_id=8483) from SparkFun._

#### Connectors

Any standard 0.1" spaced header can be soldered to the holes on the Arduino Pro. To use every pin requires two 6-pin header and two 8-pin headers. Bare wire can also be soldered directly to the holes. Note that the header spacing is compatible with Arduino shields.

The text of the Arduino getting started guide is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). Code samples in the guide are released into the public domain.
