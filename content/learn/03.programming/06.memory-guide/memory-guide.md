---
title: 'Memory Allocation on Arduino Boards'
description: 'Learn how the memory on Arduino boards work.'
tags: [Flash, SRAM, EEPROM, ]
---

There are three potential pools of memory in the microcontrollers used on Arduino boards:

- Flash memory (program space), is where the Arduino sketch is stored.

- SRAM (static random access memory) is where the sketch creates and manipulates variables when it runs.

- EEPROM is memory space that programmers can use to store long-term information.

Flash memory and EEPROM memory are non-volatile (the information persists after the power is turned off). SRAM is volatile and will be lost when the power is cycled.

## Memory on Arduino Nano boards

The nRF52840 ([datasheet](https://content.arduino.cc/assets/Nano_BLE_MCU-nRF52840_PS_v1.1.pdf?_gl=1*x4s7j8*_ga*Mjk5OTAxNjU5LjE2MzkyMTU1MDg.*_ga_NEXN8H46L5*MTYzOTQ5NzYzMS44LjEuMTYzOTQ5ODc4Ny4w)) chip found on the [Nano 33 BLE Sense](https://store.arduino.cc/collections/boards/products/arduino-nano-33-ble-sense) and [Nano 33 BLE](https://store.arduino.cc/collections/boards/products/arduino-nano-33-ble) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|1mb|
|SRAM   |256kb|

  
  
The SAMD21G18A ([datasheet](https://content.arduino.cc/assets/mkr-microchip_samd21_family_full_datasheet-ds40001882d.pdf)) chip found on the [Nano 33 IoT](https://store.arduino.cc/collections/boards/products/arduino-nano-33-iot) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|1mb|
|SRAM   |256kb|

  

The SAMD21G18A ([datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)) chip found on the [Nano RP2040 Connect](https://store.arduino.cc/collections/boards/products/arduino-nano-rp2040-connect) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|16mb|
|SRAM   |264kb|

  

The ATmega4809 ([datasheet](https://content.arduino.cc/assets/Nano-Every_processor-48-pin-Data-Sheet-megaAVR-0-series-DS40002016B.pdf)) chip found on the [Nano Every](https://store.arduino.cc/collections/boards/products/arduino-nano-every) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|48kb|
|SRAM   |6kb|
|EEPROM| 256 bytes|

  

The ATmega328 ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061A.pdf)) chip found on the [Nano](https://store.arduino.cc/collections/boards/products/arduino-nano) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|32kb|
|SRAM   |2kb|
|EEPROM| 1kb|


## Memory on Arduino MKR boards

The SAMD21G18A ([datasheet](https://content.arduino.cc/assets/mkr-microchip_samd21_family_full_datasheet-ds40001882d.pdf)) chip found on the [MKR WiFi 1000](https://store.arduino.cc/collections/boards/products/arduino-mkr1000-wifi), [MKR FOX 1200](https://store.arduino.cc/collections/boards/products/arduino-mkr-fox-1200), [MKR GSM 1400](https://store.arduino.cc/collections/boards/products/arduino-mkr-gsm-1400), [MKR NB 1500](https://store.arduino.cc/collections/boards/products/arduino-mkr-nb-1500), [MKR Vidor 4000](https://store.arduino.cc/collections/boards/products/arduino-mkr-vidor-4000), [MKR WAN 1300](https://store.arduino.cc/products/arduino-mkr-wan-1300-lora-connectivity?pr_prod_strat=description&pr_rec_pid=5517873053847&pr_ref_pid=5517874233495&pr_seq=uniform), [MKR WAN 1310](https://store.arduino.cc/collections/boards/products/arduino-mkr-wan-1310), [MKR WiFi 1010](https://store.arduino.cc/collections/boards/products/arduino-mkr-wifi-1010) and [MKR Zero](https://store.arduino.cc/collections/boards/products/arduino-zero) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|256kb|
|SRAM   |32kb|


## Memory on Arduino Pro boards

The ST STM32H747XI ([datasheet](https://content.arduino.cc/assets/Arduino-Portenta-H7_Datasheet_stm32h747xi.pdf?_gl=1*14nfrmx*_ga*Mjk5OTAxNjU5LjE2MzkyMTU1MDg.*_ga_NEXN8H46L5*MTYzOTQ5NzYzMS44LjEuMTYzOTQ5OTE2NS4w)) chip found on the [Portenta H7](https://store.arduino.cc/collections/boards/products/portenta-h7), [Portenta H7 Lite](https://store.arduino.cc/collections/boards/products/portenta-h7-lite) and [Portenta H7 Lite Connected](https://store.arduino.cc/collections/boards/products/portenta-h7-lite-connected) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|2mb|
|SRAM   |1mb|


## Memory on Arduino Classic boards

The ATmega328P ([datasheet](https://content.arduino.cc/assets/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf?_gl=1*if3eoe*_ga*Mjk5OTAxNjU5LjE2MzkyMTU1MDg.*_ga_NEXN8H46L5*MTYzOTQ5NzYzMS44LjEuMTYzOTQ5OTIyMS4w)) chip found on the [UNO R3](https://store.arduino.cc/collections/boards/products/arduino-uno-rev3) and [UNO Mini](https://store.arduino.cc/collections/boards/products/uno-mini-le) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|32kb|
|SRAM   |2kb|
|EEPROM| 1kb|


The ATmega4809 ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega4808-4809-Data-Sheet-DS40002173A.pdf)) chip found on the [UNO WiFi Rev2](https://store.arduino.cc/collections/boards/products/arduino-uno-wifi-rev2) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|48kb|
|SRAM   |6kb|
|EEPROM| 256 bytes|


The ATmega32U4 ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf)) chip found on the [Yún Rev2](https://store.arduino.cc/collections/boards/products/arduino-yun-rev-2), [Leonardo](https://store.arduino.cc/collections/boards/products/arduino-leonardo-with-headers) and [Micro](https://store.arduino.cc/collections/boards/products/arduino-micro) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|32kb|
|SRAM   |2.5kb|
|EEPROM| 1kb|


The Atmel SAM3X8E ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf)) chip found on the [Due](https://store.arduino.cc/collections/boards/products/arduino-due) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|512kb|
|SRAM   |96kb|


The ATmega2560 ([datasheet](https://content.arduino.cc/assets/ATmega640-1280-1281-2560-2561-Datasheet-DS40002211A.pdf?_gl=1*l6g5au*_ga*Mjk5OTAxNjU5LjE2MzkyMTU1MDg.*_ga_NEXN8H46L5*MTYzOTQ5NzYzMS44LjEuMTYzOTQ5OTMzMy4w)) chip found on the [Mega 2560 Rev3](https://store.arduino.cc/collections/boards/products/arduino-mega-2560-rev3) has the following amounts of memory:

|Memory Type|Size|
|--|--|
|Flash|256kb|
|SRAM   |8kb|
|EEPROM| 4kb|


Notice that with boards that do not have a lot of SRAM available, like the UNO. It's easy to use it all up by having lots of strings in your program.  For example, a declaration like:
```arduino
char message[] = "I support the Cape Wind project.";
```

puts 33 bytes into SRAM (each character takes a byte, plus the '\0' terminator).  This might not seem like a lot, but it doesn't take long to get to 2048, especially if you have a large amount of text to send to a display, or a large lookup table, for example.

If you run out of SRAM, your program may fail in unexpected ways; it will appear to upload successfully, but not run, or run strangely. To check if this is happening, you can try commenting out or shortening the strings or other data structures in your sketch (without changing the code). If it then runs successfully, you're probably running out of SRAM. There are a few things you can do to address this problem:

- If your sketch talks to a program running on a (desktop/laptop) computer, you can try shifting data or calculations to the computer, reducing the load on the Arduino.

- If you have lookup tables or other large arrays, use the smallest data type necessary to store the values you need; for example, an [int](/en/Reference/Int) takes up two bytes, while a [byte](arduino.cc/en/Reference/Byte) uses only one (but can store a smaller range of values).

- If you don't need to modify the strings or data while your sketch is running, you can store them in flash (program) memory instead of SRAM; to do this, use the [PROGMEM](arduino.cc/en/Reference/PROGMEM) keyword.
