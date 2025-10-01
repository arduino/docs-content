---
title: 'Bootloader'
description: 'The bootloader is a small piece of software that allows uploading of sketches onto the Arduino board. It comes preprogrammed on the microcontrollers on Arduino boards.'
tags: 
  - Bootloader
---

 ## What's a Bootloader?
Microcontrollers are usually programmed through a [programmer](/hacking/software/Programmer) unless you have a piece of firmware in your microcontroller that allows installing new firmware without the need of an external programmer. This is called a bootloader.

## Not Using a Bootloader
If you want to use the full program space (flash) of the chip or avoid the bootloader delay, you can burn your sketches using an external [programmer](/hacking/software/Programmer).

## Burning the Bootloader
To burn the bootloader, you'll need to buy an [AVR-ISP](http://www.atmel.com/dyn/products/tools_card.asp?tool_id=2726) (in-system programmer), [USBtinyISP](http://www.ladyada.net/make/usbtinyisp/) or build a [ParallelProgrammer](/hacking/hardware/ParallelProgrammer). The programmer should be connected to the ICSP pins (the 2 by 3 pin header) - make sure you plug it in the right way. The board must be powered by an external power supply or the USB port.

Make sure you have the right item selected in the **Tools | Board** menu. Then, just launch the appropriate command from the Tools > Burn Bootloader menu of the Arduino environment. Burning the bootloader may take 15 seconds or more, so be patient.

## Bootloading an Arduino Mini
Here are some instructions on [bootloading the Mini](/hacking/software/MiniBootloader), thanks to Gian Pablo Vilamil.

## It Still Doesn't Work! (Parallel Programmer on Windows XP)
Windows XP may be polling your parallel port and disrupting the bootloader burning process. You'll need this [registry patch](http://www.melabs.com/downloads/XP_stop_polling.reg):

 ```
[HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Parport\Parameters]
"DisableWarmPoll"=dword:00000001
```

## Versions of the Bootloader
There are different versions of the bootloader - both in order to work on different hardware and because it has changed over time.

The current bootloaders (i.e. the ones included in Arduino 0009) are almost identical for the Diecimila and NG (with ATmega168). They both run at 19200 baud and take up 2 KB of flash memory on the ATmega168. The only differences is the time the bootloader waits for a new program to arrive and the number of times it flashes the pin 13 LED when it starts. Because of the automatic reset on the Diecimila, its bootloader only waits a very short amount of time (less than a second) - to save time, it also flashes the pin 13 LED once. The NG bootloader waits about 6-8 seconds and flashes the LED three times.

The bootloader that actually shipped on the Arduino NG is slightly different. It enables the internal pullup resistor on pin 6, and doesn't enable the internal pullup on the RX pin. Nor does it timeout upon receiving invalid data, so if you send data to it immediately after it resets, your sketch will never start.

The Arduino BT bootloader does some initial configuration of the Bluetooth® module.

The ATmega8 bootloader only takes up 1 KB of flash. It does not timeout when it receives invalid data, you need to make sure that no data is sent to the board during the 6-8 seconds when the bootloader is running.

Some ancient versions of the bootloader run at 9600 baud (instead of 19200). In order to successfully upload sketches to boards with this bootloader, you'll need to change the serial.download_rate in your [preferences file](/hacking/software/Preferences) to 9600.

Third parties have also worked on the bootloader. This page is link to some other [bootloader development](http://www.arduino.cc/playground/Code/BootloaderDevelopment)

## How Does it Work?
The "Burn Bootloader" commands in the Arduino environment use an open-source tool, avrdude. There are four steps: unlocking the bootloader section of the chip, setting the fuses on the chip, uploading the bootloader code to the chip, and locking the bootloader section of the chip. These are controlled by a number of preferences in the Arduino [preferences file](/hacking/software/Preferences).

For the ATmega8 bootloader, these are:

- bootloader.atmega8.programmer (default value: stk500) is the protocol used by the bootloader.
- bootloader.atmega8.unlock_bits (default value: 0xFF) is the value to write to the ATmega8 lock byte to unlock the bootloader section.
- bootloader.atmega8.high_fuses (default value: 0xca) is the value to write to the high byte of the ATmega8 fuses.
- bootloader.atmega8.low_fuses (default value: 0xdf) is the value to write to the low byte of the ATmega8 fuses.
- bootloader.atmega8.path (default value: bootloader) is the path (relative to the Arduino application directory) containing the precompiled bootloader.
- bootloader.atmega8.file (default value: ATmegaBOOT.hex) is the name of the file containing the precompiled bootloader code (in bootloader.path).
- bootloader.atmega8.lock_bits (default value: 0x0F) is the value to write to the ATmega8 lock byte to lock the bootloader section (so it doesn't get accidentally overwritten when you upload a sketch).

For the ATmega168, these are (where `<BOARD>` is either "diecimila" or "ng"):

- bootloader.atmega168-`<BOARD>`.programmer (default value: avrispmkii) is the protocol used by the bootloader.
- bootloader.atmega168-`<BOARD>`.unlock_bits (default value: 0x3F) is the value to write to the ATmega168 lock byte to unlock the bootloader section.
- bootloader.atmega168-`<BOARD>`.extended_fuses (default value: 0x00) is the value to write to the high byte of the ATmega168 fuses.
- bootloader.atmega168-`<BOARD>`.high_fuses (default value: 0xdd) is the value to write to the high byte of the ATmega168 fuses.
- bootloader.atmega168-`<BOARD>`.low_fuses (default value: 0xff) is the value to write to the low byte of the ATmega168 fuses.
- bootloader.atmega168-`<BOARD>`.path (default value: bootloader168) is the path (relative to the Arduino application directory) containing the precompiled bootloader.
- bootloader.atmega168-`<BOARD>`.file (default value: ATmegaBOOT_168_`<BOARD>`.hex) is the name of the file containing the precompiled bootloader code (in bootloader.path).
- bootloader.atmega168-`<BOARD>`.lock_bits (default value: 0x0F) is the value to write to the ATmega168 lock byte to lock the bootloader section (so it doesn't get accidentally overwritten when you upload a sketch).
## Source Code
The [AVR bootloader source code](https://github.com/arduino/ArduinoCore-avr/tree/master/bootloaders) and [SAMD bootloader source code](https://github.com/arduino/ArduinoCore-samd/tree/master/bootloaders/zero) are available.