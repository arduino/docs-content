---
title: 'Arduino Memory Guide'
description: 'Learn about the built-in memory blocks of Arduino® boards in this article.'
tags: 
  - ROM
  - RAM
  - Flash
  - SRAM
  - EEPROM
author: 'José Bagur, Taddy Chung, Luca Osti'
---

A microcontroller unit (also known as MCU) is an integrated circuit (IC) typically used to perform specific applications or tasks. Usually, this type of IC gathers information or data from its surroundings, process it, and generates specific outputs according to the gathered data. Microcontrollers today are everywhere; they are an essential part of modern embedded systems that can be found practically everywhere in our world, from smartwatches to electric vehicles; they are even on the Martian surface right now. 

One essential part of a microcontroller is its **memory**; memory stores information temporarily or permanently in microcontrollers and can be used for several purposes. This article talks about memory organization in microcontrollers, focusing on those present in Arduino® boards. Also, several ways to manage, measure, and optimize memory usage in Arduino-based systems are discussed in the article.

## What is Memory?

Memory blocks are essential parts of modern embedded systems, especially microcontroller-based ones. **Memory blocks are semiconductor devices that store and retrieve information or data**; a microcontroller central processing unit (CPU) uses and processes data stored in memory blocks to perform specific tasks.

As shown in the image below, memory blocks in microcontrollers are usually described as **arrays**. Memory arrays are divided into **cells** that can store data and be accessed using a unique identifier representing its **address** or position relative to the memory array. Information in memory cells is stored using binary digits (bits), usually organized in bytes (8-bits); it can also be retrieved later by the MCU or other components of a microcontroller-based system. 

Memory in computing systems can be **volatile** or **non-volatile**. **Volatile memory is a temporary memory**, this means that data is stored while the system is running, but it is lost forever when the system is turned off. **Non-volatile memory is permanent memory**; data is not lost even if the system is turned off. 

## Memory Architectures 101

Computer architecture is a vast topic; we will focus on a general picture that will let us understand how memory is organized in the microcontrollers used in Arduino® boards.

In the early days of computing, two computer architectures, i.e., the organization of the components inside a computing system, emerged: **von Neumann** and **Harvard**. 

### Von Neumann Architecture

The von Neumann architecture, named after the mathematician, physicist, and computer scientist John von Neumann, was first introduced in the mid-'40s; it is also known as the Princeton architecture. This architecture stores program data and instructions in the same memory unit; both are accessed by the CPU using the same communications bus, as shown below. Von Neumann's architecture is fundamental since nearly all digital computers design have been based on this architecture.

### Harvard Architecture

The Harvard architecture, named after the Harvard Mark I relay-based computer, was first introduced in the mid-'40s. This architecture's main characteristic is that it uses two separate memory units, one for storing program instructions and one for storing program data. Both memory units in the Harvard architecture are accessed by the CPU using different communication buses. 

## Types of Memories 

There are three potential pools of memory in the microcontrollers used on Arduino boards:

- Flash memory (program space), is where the Arduino sketch is stored.

- SRAM (static random access memory) is where the sketch creates and manipulates variables when it runs.

- EEPROM is memory space that programmers can use to store long-term information.

Flash memory and EEPROM memory are non-volatile (the information persists after the power is turned off). SRAM is volatile and will be lost when the power is cycled.

## Arduino Board Memory Allocation
Arduino boards processor vary by family, depending on the necessity of the user. Arduino has two big roots that can be differed by processor architecture. The boards are either powered by **AVR** or **ARM** architecture. The Arduino boards such as MKR WAN 1310, Nano 33 BLE Sense, and Portenta H7 are powered by ARM architecture using Cortex-M family. The Arduino Nano is for example powered by AVR architecture using Atmega328.
​
### AVR-based Boards
​
AVR architecture microcontrollers has the Flash Program Memory and Static Random Access Memory 
on a separate bus. There are 2 existing bus in which handles all the data and the other line handling Input and Output with limited access. The memory architecture is allocated briefly in following manner:
​
- Program Memory (Flash)
- EEPROM Memory (Data)
- SRAM Memory (Data)
- I/O Memory 
​
Each memory type serves different role that handles the function of the AVR architecture microcontrollers. It is good to know what does each memory class manages, to comprehend what is about to be detailed in the continuing section.
​
#### Program Memory
​
The Program Memory is the reprogrammable memory found on the system. This is the Flash memory that serves as a storage, and the memory divides into two different section due to security measure. A Boot-loader section is where all the crucial code is stored to initialize peripherals and essential components. While the application section is where the composed code is uploaded.
​
#### EEPROM Memory
​
This type of memory is Read-Only memory that is electrically eraseable and reprogrammable. The memory module is designed usually with minimal resource available on the table. Commonly the memory is used to save small amounts of data and store even if when the device powers down. EEPROM registers are to access this memory department and during rewrite process, the memory removes everything in order to reprogram.  
​
#### SRAM Memory
​
The Static Random Access Memory is accessed via standard data bus, and the data is retained while it has power feed. This data memory stores different memory units that are from registers, Input/Output memory, and its internal SRAM. All this is to have general purpose 8-Bit registers, control registers to address peripheral components, and volatile storage location to temporarily manage the data generated from the code. 
​
### ARM-based Boards
​
ARM architecture implements **Memory Organization** or **Memory Map**, built depending on the width of the address map that goes from 32-Bit to 40-Bit structure. It uses Virtual and Physical addresses while the Memory Management Unit (MMU) interfaces in between to correct operation of memory system. 
​
The **Translation Tables** are injected by virtual addresses, composed of Kernel and application in blocks of data and code; then translated into physical addresses composed by peripherals, Flash, SRAM, and ROM. The present architecture uses its Memory Map, predefined accordingly depending on the ARM chip family, to ease the access.
​
## Heap & Stack
STAND_BY
​
## Measuring Memory Usage in Arduino Boards
Memory usage stadistics will help you understand the resource management affected by the designed code. It is an important factor to consider, as the resources are finite. In fact, it should run without always reaching maximum load capacity. This is one stadistic that will tell you how efficient the code is designed. 
​
### SRAM & DRAM: Quick Differentiation Specification
STAND_BY

### Flash Memory Measurement 

The Flash memory on Arduino boards can be measured with the help of the Arduino IDE. As the Flash memory is where the Application code will be stored, the Arduino IDE will report through output log to let the developer know how much resource is being used. 

This is the output log format for Arduino Nano.

![Flash Memory Usage - Arduino Nano [AVR]](assets/avr_nano.png)

This is the output log format for Arduino MKR WAN 1310.

![Flash Memory Usage - Arduino MKR WAN 1310 [ARM]](assets/arm_mkrwan1310.png)

This is the output log format for Arduino Portenta H7.

![Flash Memory Usage - Arduino Portenta H7 (ABX00042) [ARM]](assets/arm_portentah7.png)

Each image of Arduino IDE is based of three different Arduino boards, one based on AVR and the other two based of ARM architecture. The compiler will output a log where how much Flash resource is used when uploading the code. 

The purpose of three images for different boards is to how that for each Arduino board family, the output log format is little different from one another; but it will show you the required information regarding the code that is to be uploaded to the board. 

***If it is required to handle the Flash memory within the code, please read more about in [this](https://docs.arduino.cc/tutorials/portenta-h7-lite/por-ard-flash) using Arduino Portenta H7***

### SRAM Memory Measurement

The code may upload and run. However, there may be situations in which the program will suffer from sudden operation halt. Moments like this can be due to memory resource hogging. To solve this, it will require to understand in which sector of the code, the memory demand is going beyond the available resources. Following code fragment will help you measure the SRAM usage while the code is running.

```cpp
void display_freeram(){
  Serial.print(F("SRAM left"));
  Serial.println(freeRam());
}

int freeRam() {
  extern int __heap_start,*__brkval;
  int v;
  return (int)&v - (__brkval == 0  
    ? (int)&__heap_start : (int) __brkval);  
}
```

In the code, `__heap_start` and `__brkval` are as following:
- **`__heap_start`**: Refers to beginning of the Heap.
- **`__brkval`**: Last memory address pointer used by Heap. It is pointing towards the Stack. 

### EEPROM Memory Measurement

To be able to use EEPROM features, it is already included with the Arduino IDE platform so it does not require additional step to install any library. 

EEPROM memory measurement can be done through use of the following simple code fragment. The code is simplified to write a byte to know exactly which address it is reading from. It can be modified to read everything from every possible address. 

```cpp
#include <EEPROM.h>

EEPROM.write(address, value);
EEPROM.read(address);
```

On the other hand, it is possible to clear the entire EEPROM memory to set it to 0. 

```cpp
#include <EEPROM.h>

...

for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
}

...
```

The complete example codes can be found in our guide to EEPROM found below the following code. 

***For more information on how to manage the EEPROM memory, please read [here](https://docs.arduino.cc/learn/programming/eeprom-guide)***

## Optimizing Memory Usage in Arduino-based Systems
To know how the code utilizes the memory resources is one matter, but to optimize the memory is a whole different task. As the term development may infer, the requirements may change or be adjusted depending on external factors such as reduced device capacity due to inavailability of the components. Thus the code architecture may require optimization to be able to run on the reduced limited memory resources.

The optimization process also implies reduced computational complexities, trimming down extra time required to process the tasks. The memory optimization process may help the overall optimization process, as it will handle how the memory is managed in a more suitable manner. 

### Flash Memory Optimization 

One of the memory sources to begin optimization with is the Flash memory. As the Flash memory is where the size itself of the code can be reduced greatly by considering some details. 

1. **Detach Unused Sources**
Detaching unused sources include unused libraries, and code residues. Code residues can be composed of functions that are no longer used and floating variables that takes up the unnecessary space in memory. This will vastly improve the compiled code size and make more clear compilation process. 

2. **Modular Tasks**
Modular tasks mean functions that wraps the code which will be used in a repetitive or continuous manner by receiving different parameters. It is a great way to maintain clean code structure and performance, while reducing the memory space required for additional tasks that might need to be implemented.     

This leads to compact code structure, that is much easier to understand when debugging process is required, and demand developer to considerate compute complexity while designing the code structure. 

### SRAM Memory Optimization

1. **String Wrapper - F()**
It is convenient to use `Serial.println("Something");` to display the literals. This is used usally to understand where the code is going and to observe certain conditionals. However, doing this so will hog up the Static Random Access Memory (SRAM) space, which is something not desirable as the content is a simple literal string that is not used under the hood. 

The ideal way to use the Print Line command is to use the `F()` String Wrapper around the literals. This will lead us to following piece of code. 

```cpp
Serial.println(F("Something"));
```

By wrapping the String with `F()`, will move the Strings to Flash memory only rather than to use SRAM space also. It can be observed as offloading such data to Flash memory instead of SRAM. 

Flash memory is much more spacious than SRAM size, so it is possible to use the Flash space than using SRAM which will use Heap. This does not mean, the memory space will always be available as Flash memory does too have limited space. It is not recommendable to spam the code structure with Print Line, but to use them where they most matter for such applications with minimized implementation. 

2. **PROGMEM**
It is not always with the literal String that occupies the SRAM space, but also using Global Variables which also takes up quite good amount of SRAM. As Global and Static variables are streamed to SRAM space, and pushes the Heap towards the Stack. The space occupied by this variables streamed to SRAM space will be saved at its location and will not be changing, meaning more of these variables are created, they will use more space and consequently, system failure due to low and poor memory management. 

PROGMEM stands simply for Program Memory. We will use Program memory to store variable data offloading to Flash Memory space. As it goes same as to String Wrapper F(), PROGMEM uses Flash Memory space for its usage. The only disadvantage presented using PROGMEM is the Read Speed. Using RAM will provide much faster Read Speed, but PROGMEM, as it uses Flash Memory, it will be slower than RAM, given the same data size read. Thus, it is important to design the software knowing which variables are crucial and others has lower priority. It is one of the many factors that needs to be considered when developing the software, but this will lead to have nicely designed code architecture.

To use the PROGMEM, it can begin with following code fragment. 

```cpp
#include <avr/pgmspace.h>

// Basic PROGMEM Define Structure 
const PROGMEM DataType Variable_Name[] = {var0, var1, var2 ...};

// Unsigned 16 Bit int
const PROGMEM uint16_t NumSet[] = {0, 1, 1, 2, 3, 5, 8 ...};

// Storing Char
const char greetMessage[] PROGMEM = {"Hello There"};
```

***For In-Depth detail about PROGMEM, please read [here](https://www.arduino.cc/reference/en/language/variables/utilities/progmem/)***

3. **RESERVE()**
STAND_BY

4. **Buffer Size Control**
STAND_BY

5. **Non Dynamic Memory Allocation** 
Dynamic Memory Allocation usually is a good method if the given RAM size is big enough to get around with, from MegaBytes and so on. However, for embedded devices counting every Byte of the RAM, the process becomes hostile for RAM.

Dynamic Memory Allocations cause Heap fragmentation. With heap fragmentation, many areas of the RAM affected by it cannot reused again, leaving dead Byte that can be taken as an advantage for other tasks. On top of it, when dynamic allocation proceeds to de-allocate to free up the space, it does not necessarily reduce the Heap Size. So to avoid Heap or RAM fragmentation as much as possible, you can follow following rules to apply into code architecture design. 

- Prioritize using **Stack** than **Heap** if possible to do so.
  - Stack memory is fragmentation free and can be freed up completely when the function returns. Heap in contrast ma not free up the space even though it was instructed to do so. Using Local Variables will help to do this and try not to use dynamic memory allocation, composed of different calls: `malloc, calloc, realloc`.

- Reduced Global and Static Data if possible to do so.
  - Meantime the code is running, memory area occupied by these data will not be freed up. Meaning the data won't be modified as it is constant data taking up the precious space.

- Short Strings / Literals
  - It is good practice to keep the literal Strings as short as possible. Single char takes **One** Byte of RAM, so shorter the better memory space usage. This does not mean, keeping it short and using it in several different areas of the code is possible. Use it when it is absolutely required and keep as short as possible to spare RAM space for other task functions. 

  Arrays are also recommended to be at a minimum size. If it requires to resize the array, you can always re-set the array size in the code. 

6. **Corrective Data Type Usage** 
Implementation of adequate data type leads to a good overall code architecture. It may be desirable for the developer to use easiest or the most accessible data type to handle the data stream. However, it is important to consider the amount of memory space that it takes up when using certain data types.

The Data Types exist to ease data stream format and to be handled without making illegal access. The illegal access in terms of data types are meant when the data is handled in the code with incompatible format. So it is a good practice to not to abuse the the data type and use only convenient types for every data bits. Rather, design and allocate memory carefully according to the requirements, which will help to reserve some memory space if further designed tasks needs extra space.

Following table shows some of the existing data types to opt out for more options. 

| Data Type              | Byte Size   | Range                                 | Format Specifier    | 
| :--------------------: | :---------: | :-----------------------------------: | :-----------------: |
| **char, signed char**  | 1           | -128 ~ 127                            | %c                  | 
| **unsigned char**      | 1           | 0 ~ 255                               | %c                  |
| **int, signed int**    | 2 , 4       | -32,768 ~ 32,767                      | %d, %i              | 
| **unsigned int**       | 2 , 4       | 0 ~ 65,535                            | %u                  |
| **signed short int**   | 2           | -32,768 ~ 32,767                      | %hd                 | 
| **unsigned short int** | 2           | 0 ~ 65,535                            | %hu                 |
| **long int**           | 4           | -2,147,483,648 ~ 2,147,483,647        | %ld, %li            |
| **long long int**      | 8           | -(2^63-1) ~ 2^63-1 (C99 Standard)     | %lld, %lli          |
| **unsigned long int**  | 4           | 0 to 4,294,967,295                    | %lu                 |
| **unsigned long long int**  | 8           | 2^64-1 (C99 standard)            | %llu                |
| **float**              | 4           | 1E-37 ~ 1E+37 + 6 Digit Precision     | %f                  |
| **double**             | 8           | 1E-37 ~ 1E+37 + 10 Digit Precision    | %lf                 |
| **long double**        | 10          | 1E-37 ~ 1E+37 + 10 Digit Precision    | %Lf                 |
​
### EEPROM Memory Optimization

TDB!

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

puts 33 bytes into SRAM (each character ta|kes a byte, plus the '\0' terminator).  This might not seem like a lot, but it doesn't take long to get to 2048, especially if you have a large amount of text to send to a display, or a large lookup table, for example.

If you run out of SRAM, your program may fail in unexpected ways; it will appear to upload successfully, but not run, or run strangely. To check if this is happening, you can try commenting out or shortening the strings or other data structures in your sketch (without changing the code). If it then runs successfully, you're probably running out of SRAM. There are a few things you can do to address this problem:

- If your sketch talks to a program running on a (desktop/laptop) computer, you can try shifting data or calculations to the computer, reducing the load on the Arduino.

- If you have lookup tables or other large arrays, use the smallest data type necessary to store the values you need; for example, an [int](/en/Reference/Int) takes up two bytes, while a [byte](arduino.cc/en/Reference/Byte) uses only one (but can store a smaller range of values).

- If you don't need to modify the strings or data while your sketch is running, you can store them in flash (program) memory instead of SRAM; to do this, use the [PROGMEM](arduino.cc/en/Reference/PROGMEM) keyword.