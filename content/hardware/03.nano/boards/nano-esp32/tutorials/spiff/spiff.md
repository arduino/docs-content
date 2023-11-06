---
title: SPIFFS Partition on Nano ESP32
description: Get started with the SPIFFS partition scheme on the Nano ESP32.
author: Hannes Siebeneicher
hardware:
  - hardware/03.nano/boards/nano-esp32
tags: [ESP32, SPIFFS, IDE]
---

The SPIFFS (Serial Peripheral Interface Flash File System) is a file system designed to be used with NOR flash memory devices and microcontrollers that support the Serial Peripheral Interface (SPI) protocol such as the ESP32 found on the [Nano ESP32](https://store.arduino.cc/products/nano-esp32?queryID=undefined).

***Before proceeding with the SPIFFS file system setup on Nano ESP, please be aware that the mounting instructions mentioned in a comment on the code from the packaged built-in example are tailored for specific older IDE versions such as IDE 1.8. These instructions might not be relevant to IDE 2.0, as it does not support the utilization of custom tools, which are unnecessary in this case.***

## Software & Hardware Needed

- [Arduino Nano ESP32](https://store.arduino.cc/nano-esp32)
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Arduino ESP32 Core](https://github.com/arduino/arduino-esp32)

## Set Up SPIFFS File System

Start by opening the **SPIFFS_Test example** by going to:

- File > Examples > SPIFFS > SPIFFS_Test

![Open Example](./assets/openExample.png)

Select the correct **Partition Scheme** by clicking: 

- Tools > Partition Scheme > With SPIFFS partition (advanced)

![Select SPIFFS](./assets/selectSPIFFS.png)

Prepare your following these steps:

- Take your **unplugged** board connect a jumper cable between the **GND** and **B1** pins. 

- **Plug it in** and the RGB LED will turn on with a green or blue color.

- While the **GND** and **B1** pins are shorted, press the white **RST** button on the top of the board to reset the board.

- **Remove** the jumper cable. The RGB LED should stay on, in a purple or yellow color.

Select the correct port:

![Select Port](./assets/selectBoard.png)

***If your board shows up as a generic ESP32 device go to Tools > Board and select "Arduino Nano ESP32" as well as the correct port under Tools > Port.***

Select the **Esptool as Programmer** by going to:

- Tools > Programmer > Esptool

![Select Programmer](./assets/selectProgrammer.png)

**Burn the bootloader** by clicking:

- Tools > Burn Bootloader

![Burn Bootloader](./assets/burnBootloader.png)

We have now successfully changed the partition scheme and the final step is to upload a sketch using programmer and reset the board.

Upload the sketch via **Using Programmer** by going to:

- Sketch > Upload Using Programmer

![Upload Using Programmer](./assets/uploadProgrammer.png)

After the successful upload press the white **RST** button on the top of the board. You should see two ports in the drop-down menu, one showing a USB symbol and another one showing a cube.

Select the port next to the USB symbol. 

![Select the Correct Port](./assets/twoPorts.png)

Open the serial monitor and you should see the following output:

![Serial Output](./assets/serialOutput.png)

***Note: It might take a short while for the messages to be printed. If you don't see any messages after one minute repeat the process.***