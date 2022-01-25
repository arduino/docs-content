---
title: 'Burning sketches to the Arduino board with an external programmer'
description: 'How to use the Arduino software with a hardware programmer (eliminating the need for the bootloader and saving program space on the chip).'
tags: 
  - Bootloader
  - ISP
---
If you have an external programmer (e.g. an AVR-ISP, STK500, or [parallel programmer](/hacking/hardware/ParallelProgrammer)), you can burn sketches to the Arduino board without using the bootloader. This allows you to use the full program space (flash) of the chip on the Arduino board. So with an ATmega168, you'll get 16 KB instead of 14 (on an ATmega8 you'll get 8 KB instead of 7). It also avoids the bootloader delay when you power or reset your board. However you must have in mind that the Upload Using Programmer procedure doesn't burn fuses so, if you have a fresh factory micro-controller you have to burn the boot-loader first in order to have a properly working device.

This can be easily done in this way:

- **Tools->Boards->Your Board**
- **Tools->Programmer->Your Programmer**
- **Sketch->Upload Using a Programmer**
## Note
In order to come back to the default way to program your Arduino you have to rewrite the bootloader. To do this:

- **Tools->Boards->Your Board**
- **Tools->Programmer->Your Programmer**
- **Tools->Burn Bootloader**