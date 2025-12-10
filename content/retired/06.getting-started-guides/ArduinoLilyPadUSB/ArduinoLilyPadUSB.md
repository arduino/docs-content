---
title: 'Getting Started with the LilyPad Arduino USB'
description: 'The first steps to setting up the LilyPad Arduino USB'
---

Like the other LilyPad Arduino boards, the [LilyPad Arduino USB](https://arduino.cc/en/Main/ArduinoBoardLilyPadUSB) is designed to be sewn into clothing and other fabric with conductive thread. The LilyPad Arduino can be powered either from the USB connection or a 3.7V LiPo battery. **The board runs at 3.3V; applying more voltage (e.g. 5V) to its pins may damage it.** If you connect a USB cable from a computer and a LiPo battery to the LilyPad, it will charge the battery. The switch on the LilyPad allows you to turn the board on or off (use the "CHG" position to turn the board off).

Similar to the Arduino Leonardo and Micro, the LilyPad Arduino uses only a single microcontroller (the Atmel ATmega32U4) to both run your sketches and communicate over USB with the computer. This means that you only need a USB cable to program the LilyPad Arduino USB (as opposed to an FTDI USB-serial adaptor as with other LilyPads) but it also means that there are some differences in the way that the USB communication works.

The LilyPad Arduino USB is programmed using the [Arduino Software (IDE)](https://arduino.cc/en/Main/Software), our Integrated Development Environment common to all our boards and running both [online](https://create.arduino.cc/editor) and offline. For more information on how to get started with the Arduino Software visit the [Getting Started page](https://arduino.cc/en/Guide/HomePage).

### Use your LilyPad Arduino USB on the Arduino Web IDE



All Arduino boards, including this one, work out-of-the-box on the [Arduino Cloud Editor](https://create.arduino.cc/editor), you only need to install Arduino Create Agent to get started.

The Arduino Cloud Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow this [simple guide](https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-4b3e4a) to start coding on the browser and upload your sketches onto your board.





### Use your LilyPad Arduino USB on the Arduino Desktop IDE

If you want to program your LilyPad Arduino USB while offline you need to install the [Arduino Desktop IDE](https://arduino.cc/en/Main/Software).

#### Connect the board

Connect the Arduino board to your computer using the USB 2 Serial adapter and a USB cable.

#### Open your first sketch

Open the LED blink example sketch: **File > Examples >01.Basics > Blink**.

#### Select your board type and port

You'll need to select the entry in the **Tools > Board** menu that corresponds to your Arduino board.

#### Upload the program

Now, simply click the "Upload" button in the environment. Wait a few seconds. If the upload is successful, the message "Done uploading." will appear in the status bar.

#### Learn more on the Desktop IDE

[See this tutorial](https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-the-arduino-software-ide-623be4) for a generic guide on the Arduino IDE with a few more infos on the Preferences, the Board Manager, and the Library Manager.

### Tutorials

Now that you have set up and programmed your LilyPad Arduino USB board, you may find inspiration in our [Project Hub](https://create.arduino.cc/projecthub/products/arduino-lilypad-usb) tutorial platform.

<iframe frameborder='0' height='410' scrolling='no' src='https://create.arduino.cc/projecthub/Arduino_Scuola/a-cool-scale-512c2f/embed?use_route=project' width='354' style='margin-top:30px'></iframe>

### Please Read...

#### Differences from Other LilyPad Arduino Boards

The LilyPad Arduino USB uses a single processor (the ATmega32U4) to both run your sketches and communicate over USB with the computer. This provides more flexibility - for example, the board can emulate a keyboard or mouse - but it also means that the USB connection resets whenever the processor does (e.g. when you upload a new sketch).

For details on these differences, see the [guide to the Arduino Leonardo and Micro](https://arduino.cc/en/Guide/ArduinoLeonardoMicro). In addition, see the following section for a few differences between the LilyPad USB and the Leonardo or Micro.

#### Differences from the Leonardo and Micro

Because it operates at 3.3V, the LilyPad Arduino USB is limited to an 8 MHz clock speed vs. 16 MHz for the Leonardo and Micro. Your sketches should behave the same on either board (e.g. delay(1000) will pause for 1 second), but it's important to correctly select the appropriate board in the boards menu. Uploading to a LilyPad Arduino USB with the board set to "Arduino Leonardo" or "Arduino Micro" will mean that your sketch won't be able to communicate over USB (and the timing of other things will be off). If this does happen, you'll need to recover using the method described in the next section.

#### About Uploading Sketches to the LilyPad USB

Typically, you'll upload to the LilyPad Arduino USB as you do with other Arduino boards: select "LilyPad Arduino USB" from the Tools > Board menu and the appropriate serial port from the Tools > Serial Port menu and press the upload button. This will reset the LilyPad, launching the bootloader, which receives the new sketch from the computer and stores it on the board. The bootloader then automatically launches the new sketch. You can tell when the bootloader is running because the on-board (pin 13) LED will fade in and out (breathe).

Sometimes, however, this automatic reset fails. This can happen, for example, if you upload a sketch to the LilyPad with a different board (e.g. the Leonardo or Micro) selected in the Tools menu. If this does happen, there's an easy fix: you can press the reset button on the LilyPad twice in quick succession to initiate the bootloader. To upload with this technique, first press the upload button in the Arduino software; then, when you see the status message "Uploading..." press the reset button twice. This should initiate the bootloader, and the Arduino software will upload your sketch. You might have to play a bit with the relative timing of pressing the upload button in the software vs. the double-press of the reset button on the board.

#### Additional Resources

[LilyPad Arduino USB product page](https://arduino.cc/en/Main/ArduinoBoardLilyPadUSB): details about the board's hardware and software
[LilyPad Category on SparkFun](https://www.sparkfun.com/categories/135): sensors, actuators, and other boards for use with the LilyPad Arduino

The text of the Arduino getting started guide is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). Code samples in the guide are released into the public domain.
