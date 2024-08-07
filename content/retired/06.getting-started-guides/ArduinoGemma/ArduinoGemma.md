---
title: 'Getting Started with the Arduino Gemma'
description: 'THe first steps to setting up your Arduino Gemma'
---

## Overview

Like the LilyPad Arduino boards, the [Arduino Gemma](https://arduino.cc/en/Main/ArduinoGemma) is designed to be sewn into clothing and other fabric with conductive thread. The Arduino Gemma can be powered either from the USB connection or a 3.7V Li-Ion battery. **The board runs at 3.3V; applying more voltage (e.g. 5V) to its pins may damage it**.

The Arduino Gemma is programmed using the [Arduino Software (IDE)](https://arduino.cc/en/Main/Software), our Integrated Development Environment common to all our boards. For more information on how to get started with the Arduino Software visit the [Getting Started page](https://arduino.cc/en/Guide/HomePage).

### Use your Arduino Gemma on the Arduino Desktop IDE

If you want to program your Arduino Gemma you need to install the [Arduino Desktop IDE](https://arduino.cc/en/Main/Software). This board does not work on [Arduino Cloud Editor](https://create.arduino.cc/editor).

#### Open your first sketch

Open the LED blink example sketch: **File > Examples >01.Basics > Blink**.

#### Select your board type

Select Arduino Gemma from **Tools > Board**

#### Upload the program

Select Arduino Gemma from **Tools > Programmer**. Plug in the Gemma, make sure you see the red LED lit.
Press the reset button on the Gemma - verify you see the red LED pulse. This means it is ready to receive data. Click on **File > Upload Using Programmer** above within 10 seconds.
When the upload is finished, the built-in LED will flash every other second.

#### Learn more on the Desktop IDE

[See this tutorial](https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-the-arduino-software-ide-623be4) for a generic guide on the Arduino IDE with a few more infos on the Preferences, the Board Manager, and the Library Manager.

### Tutorials

Now that you have set up and programmed your Arduino Gemma board, you may find inspiration in our [Project Hub](https://create.arduino.cc/projecthub/products/arduino-gemma) tutorial platform.

<iframe frameborder='0' height='410' scrolling='no' src='https://create.arduino.cc/projecthub/AmieDD/zelda-princess-hilda-led-staff-powered-by-arduino-9a85de/embed?use_route=project' width='354' style='margin-top:30px'></iframe>

### Please Read...

Like the LilyPad Arduino boards, the [Arduino Gemma](https://arduino.cc/en/Main/ArduinoGemma) is designed to be sewn into clothing and other fabric with conductive thread. The Arduino Gemma can be powered either from the USB connection or a 3.7V Li-Ion battery. **The board runs at 3.3V; applying more voltage (e.g. 5V) to its pins may damage it**.

Arduino Gemma uses only a single microcontroller (the Atmel ATtiny85) to run your sketches, but it cannot communicate over USB with the computer. This means that you only need a USB cable to program the Arduino Gemma, but you cannot use the Serial Monitor. This is the reason why you don't have to select a Serial port from the Serial port menu.

#### Serial Debug with Arduino Gemma

The Arduino Gemma doesn't allow you to use the serial monitor on the Arduino IDE, but [Software Serial](http://arduino.cc/en/Reference/softwareSerial) can be used. To see the serial output on a serial monitor you can use the [Arduino USB2Serial](http://arduino.cc/en/Main/USBSerial)

#### Additional Resources

- [Arduino Gemma product page](https://arduino.cc/en/Main/ArduinoGemma): details about the board's hardware and software

The text of the Arduino getting started guide is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). Code samples in the guide are released into the public domain.
