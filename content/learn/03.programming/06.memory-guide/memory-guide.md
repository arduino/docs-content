---
title: 'Arduino Memory Guide'
description: 'Learn about the built-in memory blocks of Arduino® boards in this article.'
tags: 
  - ROM
  - RAM
  - Flash
  - SRAM
  - EEPROM
author: 'Arduino, José Bagur, Taddy Chung'
---

A microcontroller unit (also known as a MCU) is an integrated circuit (IC), typically used to perform specific applications or tasks. Usually, this type of IC gathers information or data from its surroundings, process it, and generates specific outputs according to the gathered data. Microcontrollers today are everywhere; they are an essential part of modern embedded systems that can be found practically everywhere in our world, from smartwatches to electric vehicles; they are even on the Martian surface right now. 

One essential part of a microcontroller is its **memory**; memory stores information temporarily or permanently in microcontrollers, and can be used for several purposes. In this article, we will explore memory organization in microcontrollers, focusing on those present in Arduino® boards. We will also explore several ways to manage, measure, and optimize memory usage in Arduino-based systems are discussed in the article.

## What is Memory?

Memory blocks are essential parts of modern embedded systems, especially microcontroller-based ones. **Memory blocks are semiconductor devices that store and retrieve information or data**; a microcontroller central processing unit (CPU) uses and processes data stored in memory blocks to perform specific tasks.

As shown in the image below, memory blocks in microcontrollers are usually described as **arrays**. Memory arrays are divided into **cells** that can store data and be accessed using a unique identifier representing its **address** or position relative to the memory array. Information in memory cells is stored using binary digits (bits), usually organized in bytes (8-bits); it can also be retrieved later by the MCU or other components of a microcontroller-based system. 

Memory in computing systems can be **volatile** or **non-volatile**. Volatile memory is a **temporary memory**, this means that data is stored while the system is running, but it is lost forever when the system is turned off. Non-volatile memory is **permanent memory**; data is not lost even if the system is turned off. 

## Memory Architectures 101

Computer architecture is a vast topic; we will focus on a general picture that will let us understand how memory is organized in the microcontrollers used in Arduino® boards.

In the early days of computing, two computer architectures, i.e., the organization of the components inside a computing system, emerged: **von Neumann** and **Harvard**. 

### Von Neumann Architecture

The von Neumann architecture, named after the mathematician, physicist, and computer scientist John von Neumann, was first introduced in the mid-'40s; it is also known as the Princeton architecture. This architecture stores program data and instructions in the same memory unit. 

Both are accessed by the CPU using the same communications bus, as shown below. Von Neumann's architecture is fundamental since nearly all digital computers design have been based on this architecture.

### Harvard Architecture

The Harvard architecture, named after the Harvard Mark I relay-based computer, was first introduced in the mid-'40s. This architecture's main characteristic is that it uses **two separate memory units**, one for storing program instructions and one for storing program data. Both memory units in the Harvard architecture are accessed by the CPU using different communication buses. 

### Modern Architectures: Hybrids

Modern computing systems use **hybrid architectures** models that maximize performance using the best of both worlds, the von Neumann and the Harvard models. 

Microcontrollers are usually used in embedded applications. They must perform defined tasks reliably and efficiently, with low or constrained resources; this is why the **Harvard architecture model is mainly used in microcontrollers**: microcontrollers have a small program and data memory that needs to be accessed simultaneously. However, Harvard architecture is not always used in microcontrollers; some microcontroller families use hybrid or Von Neumann architecture models. 

### Arduino® Boards Architectures

Arduino® boards are mainly based on two families of microcontrollers: **AVR®** and **ARM®**. While AVR® family microcontrollers are based on the Harvard architecture model, ARM® family microcontrollers can be based on either von Neuman or Harvard architectures models. The following table summarizes Arduino boards microcontrollers architectures:

|      **Board**      | **Microcontroller** |    **Family**    | **Architecture** |
|:-------------------:|:-------------------:|:----------------:|:----------------:|
|       UNO Mini      |      ATmega328P     |        AVR       |      Harvard     |
|       UNO Rev3      |      ATmega328P     |        AVR       |      Harvard     |
|    UNO WiFi Rev2    |      ATmega4809     |        AVR       |      Harvard     |
|     UNO Rev3 SMD    |      ATmega328P     |        AVR       |      Harvard     |
|       Leonardo      |      ATmega32u4     |        AVR       |      Harvard     |
|    Mega 2560 Rev3   |      ATmega2560     |        AVR       |      Harvard     |
|        Micro        |      ATmega32u4     |        AVR       |      Harvard     |
|         Zero        |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|     Portenta H7     |      STM32H747      | ARM Cortex M4/M7 |      Harvard     |
|    Nicla Sense ME   |       nRF52832      |   ARM Cortex M4  |      Harvard     |
| Nano RP2040 Connect |        RP2040       |  ARM Cortex M0+  |    Von Neumann   |
|     MKR FOX 1200    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|     MKR NB 1500     |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|    MKR Vidor 4000   |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|    MKR WiFi 1010    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|       MKR Zero      |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|     MKR1000 WIFI    |     ATSAMW25H18     |  ARM Cortex M0+  |    Von Neumann   |
|     MKR WAN 1300    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|     MKR WAN 1310    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|         Nano        |      ATmega328P     |        AVR       |      Harvard     |
|      Nano Every     |      ATmega4809     |        AVR       |      Harvard     |
|     Nano 33 IoT     |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |
|     Nano 33 BLE     |       nRF52840      |   ARM Cortex M4  |      Harvard     |
|  Nano 33 BLE Sense  |       nRF52840      |   ARM Cortex M4  |      Harvard     |

## Memory Types

Now, let us talk about the different memory units present on microcontrollers. All the different memory units inside a microcontroller can be divided into two main types: **RAM** and **ROM**. RAM (from Random-Access Memory) in microcontroller-based systems is a volatile memory used to store temporary data such as the system's firmware variables. ROM (from Read-Only Memory) in microcontroller-based systems is non-volatile memory used to store permanent data such as the system's firmware.

RAM and ROM in microcontroller-based systems are organized into three main categories:

- Flash
- RAM
- EEPROM

Let us talk more about these types of memories.

### Flash

Flash memory in microcontroller-based systems is part of its ROM. The **Flash memory is where the system's firmware is stored to be executed**. For example, think of the famous `Blink.ino` example sketch, when we compile this sketch, we create a binary file that is later stored into the Flash memory of an Arduino board and executed when power on.

### RAM

**RAM** in microcontroller-based systems **is where the system's temporary data or run-time data is stored**. A microcontroller's RAM usually is SRAM; this is a type of RAM that uses a flip-flop to store one bit of data. For example, the variables created by functions. 

### EEPROM

In microcontroller-based systems, Erasable Programmable Read-Only Memory, or EEPROM, is also part of its ROM; actually, Flash memory is a type of EEPROM. **The main difference between Flash memory and EEPROM is how they are managed**; EEPROM can be managed at the byte level (write or erased) while Flash can be managed at the block level.

## Arduino® Boards Memory Allocation

As stated before, Arduino® boards are mainly based on two families of microcontrollers, AVR® and ARM®; it is important to know that **memory allocation differs in both architectures**. In Harvard-based AVR architecture, memory is organized as shown in the image below:

Something important to mention about AVR-based Arduino boards is how their SRAM is organized into different sections:

- `Text`
- `Data`
- `BSS`
- `Stack`
- `Heap`
  
The `text` section contains instructions loaded into the flash memory; `data` section contains variables initialized in the sketch, `BSS` section contains uninitialized data, `stack` section stores data of functions and interrupts, and `heap` section stores variables created during run time.

In hybrid ARM architectures, so called **Memory map** is implemented, with different address map configuration of 32-bit, 36-bit, and 40-bit that depends on the requirement of System On a Chip (SoC) address space with extra DRAM. The Memory Map grants interface with SoC design, while having most system control on a high level coding. Memory access instructions can be used on high level code to manage interrupt modules and built-in peripherals. All of this controlled by Memory Management Unit (MMU).

The memory resource is handled by the **Memory Management Unit** (MMU). The main role of the MMU is to enable the processor to run multiple tasks independently in its own virtual memory space; the MMU then uses translation tables to establish a bridge between the virtual and the physical memory addresses. Virtual Address is managed via software with memory instructions, and Physical address is the memory system that is controlled depending on the Translation Table input given by the Virtual Address.
An example of how memory is organized in ARM-based microcontrollers, virtually and physically, is shown in the image below:

The ARM-based microcontroller's memory department is organized into the following sections respectively within the address type mentioned previously:

- **Virtual Address**
  - `Kernel Code & Data`
  - `Application Code & Data`

- **Physical Address**
  - `ROM`
  - `RAM`
  - `Flash`
  - `Peripherals`

The following table summarizes the Arduino® board's memory allocation:

|      **Board**      | **Microcontroller** |    **Family**    | **Architecture** | **Flash** | **SRAM** | **EEPROM** |
|:-------------------:|:-------------------:|:----------------:|:----------------:|:---------:|:--------:|:----------:|
|       UNO Mini      |      ATmega328P     |        AVR       |      Harvard     |    32kB   |    2kB   |     1kB    |
|       UNO Rev3      |      ATmega328P     |        AVR       |      Harvard     |    32kB   |    2kB   |     1kB    |
|    UNO WiFi Rev2    |      ATmega4809     |        AVR       |      Harvard     |    48kB   |    6kB   |    256B    |
|     UNO Rev3 SMD    |      ATmega328P     |        AVR       |      Harvard     |    32kB   |    2kB   |     1kB    |
|       Leonardo      |      ATmega32u4     |        AVR       |      Harvard     |    32kB   |   2.5kB  |     1kB    |
|    Mega 2560 Rev3   |      ATmega2560     |        AVR       |      Harvard     |   256kB   |    8kB   |     4kB    |
|        Micro        |      ATmega32u4     |        AVR       |      Harvard     |    32kB   |   2.5kB  |     1kB    |
|         Zero        |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|    Porten ta H7*     |      STM32H747      | ARM Cortex M4/M7 |      Harvard     |    16MB   |    8MB   |      -     |
|    Nicla Sense ME   |       nRF52832      |   ARM Cortex M4  |      Harvard     |   512kB   |   64kB   |      -     |
| Nano RP2040 Connect |        RP2040       |  ARM Cortex M0+  |    Von Neumann   |     -     |   264kB  |      -     |
|     MKR FOX 1200    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|     MKR NB 1500     |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|    MKR Vidor 4000   |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|    MKR WiFi 1010    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|       MKR Zero      |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|     MKR1000 WIFI    |     ATSAMW25H18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|     MKR WAN 1300    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|     MKR WAN 1310    |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|         Nano        |      ATmega328P     |        AVR       |      Harvard     |    32kB   |    2kB   |     1kB    |
|      Nano Every     |      ATmega4809     |        AVR       |      Harvard     |    48kB   |    6kB   |    256B    |
|     Nano 33 IoT     |     ATSAMD21G18     |  ARM Cortex M0+  |    Von Neumann   |   256kB   |   32kB   |      -     |
|     Nano 33 BLE     |       nRF52840      |   ARM Cortex M4  |      Harvard     |    1MB    |   256kB  |      -     |
|  Nano 33 BLE Sense  |       nRF52840      |   ARM Cortex M4  |      Harvard     |    1MB    |   256kB  |      -     |

## Measuring Memory Usage in Arduino Boards

Memory usage statistics help comprehend the insight of resource management affected by the designed code structure. Memory load demand is one statistic that will give you an insight into how efficient the code is design|ed. It is a crucial development consideration element because the resources are finite inside a microcontroller-based system; **software should always perform without reaching maximum load capacity to avoid problems or issues**. Memory load could be observed either as **available RAM** at disposal for specific tasks or **Flash storage remaining capacity** for required headroom.

Let us talk more about memory usage measurement in Arduino boards.
​
### SRAM & DRAM: Quick Differentiation Specification

Embedded devices compose of **Static Random Access Memory (SRAM)** and **Dynamic Random Access Memory (DRAM)**. These are 2 different derivatives that shapes the Random Access Memory (RAM). Both RAM types has trade-off in between them, and it is based on speed, physical size and manufacturing cost. 

- SRAM performs much faster than DRAM has to propose. In Read, Write and Access speed. 
- SRAM is much more expensive in terms of manufacturing cost than DRAM.
- DRAM offers more friendly physical size, in terms of storage capacity, than SRAM. 

While these are 2 types of RAM that are found within embedded devices, optimization process that will be stated in the following are applicable as a whole. No matter which type of RAM is on-board, it can be controlled to achieve efficient memory management with careful design factors in mind. 

Ultimately, it should not be abused whatsoever, because even if the code might produce results, the system may be filled with a lot of memory handling flaws causing unstable on-the-edge software. The fix or patch that are applied later, might cost entire code architecture re-design.  

### Flash Memory Measurement 

The Flash memory on Arduino boards can be measured with the help of the Arduino IDE. As the Flash memory is where the Application code is stored, the Arduino IDE will report through output log to let the developer know how much resource is being used. 

This is the output log format for Arduino Nano.

![Flash Memory Usage - Arduino Nano [AVR]](assets/avr_nano.png)

This is the output log format for Arduino MKR WAN 1310.

![Flash Memory Usage - Arduino MKR WAN 1310 [ARM]](assets/arm_mkrwan1310.png)

This is the output log format for Arduino Portenta H7.

![Flash Memory Usage - Arduino Portenta H7 (ABX00042) [ARM]](assets/arm_portentah7.png)

Each image of Arduino IDE is based of selected three different Arduino boards, in which one is based on AVR and the other two is based of ARM architecture. The compiler will output a log where how much Flash resource is used when uploading the code. 

The purpose of these three images for different boards is to show that for each Arduino board family, the output log format is little different from one another; but it will show you the memory consumption information regarding the uploaded code. 

***If it is required to handle the Flash memory within high level code, please read more about in [this](https://docs.arduino.cc/tutorials/portenta-h7-lite/por-ard-flash) using Arduino Portenta H7***

### SRAM Memory Measurement

The code may compile, upload and run. However, there may be situations in which the program will suffer from sudden operation halt. Thys type of issues are likely due to memory resource hogging or not enough memory to allocate. To solve this, it will require to understand in which sector of the code, the memory demand is going beyond the available resources. Following code fragment will help you measure the SRAM usage at a high level code.

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

EEPROM features are already included with the Arduino IDE platform so it does not require additional step to install any library to use its features. 

EEPROM memory measurement can be done through use of the following simple code fragment. The code is simplified to write a byte to know exactly which address it is reading from. It can be modified to read everything from every available possible address. 

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
Knowing how the code utilizes the memory resources is one matter, but to optimize the memory is a whole different task. As the term development may infer, the requirements may change or be adjusted depending on external factors such as reduced device capacity due to inavailability of the components. Thus the code architecture may require optimization to be able to run on the reduced limited memory resources.

The optimization process also implies reduced computational complexities, trimming down extra time required to process the tasks while using less memory resource to do the same task. The memory optimization process may help the overall code optimization process, as it will handle how the memory is managed in a more suitable manner by requiring smart algorithm development. 

### Flash Memory Optimization 

Flash memory optimization is the most likely the straightforward optimization possible source to begin with. The Flash memory is where the capacity used by compiled code can be reduced greatly by considering some details. 

#### Detach Unused Sources
Detaching unused sources include unused libraries, and code residues. Code residues can be composed of functions that are no longer used and floating variables that takes up the unnecessary space in memory. This will vastly improve the compiled code size and make more clear compilation process. 

#### Modular Tasks
Modular tasks mean functions that wraps the code which will be used in a repetitive or continuous manner by receiving different parameters. It is a great way to maintain clean code structure and performance, while reducing the memory space required for additional tasks that might need to be implemented.     

This leads to compact code structure, that is much easier to understand when debugging process is required, and demand developer to considerate compute complexity when designing the code structure or such specific algorithm. 

### SRAM Memory Optimization

#### String Wrapper - F()
It is convenient to use `Serial.println("Something");` to display the literals. This is used usually to understand where the code is going and to observe certain conditionals. However, doing this so will hog up the Static Random Access Memory (SRAM) space, which is something not desirable as the content is a simple literal string that is not used under the hood. 

The ideal way to use the Print Line command is to use the `F()` String Wrapper around the literals. This will lead us to following piece of code. 

```cpp
Serial.println(F("Something"));
```

By wrapping the String with `F()`, will move the Strings to Flash memory only rather than to use SRAM space also. It can be observed as offloading such data to Flash memory instead of SRAM. 

Flash memory is much more spacious than SRAM size, so it is better to use the Flash space than using SRAM which will use Heap. This does not mean the memory space will always be available, as Flash memory does have limited space too. It is not recommendable to cloag the code structure with Print Line, but to use them where they most matter for such applications with minimized implementation. 

#### PROGMEM
It is not always with the literal String that occupies the SRAM space, but also using Global Variables which also takes up quite good amount of SRAM. As Global and Static variables are streamed to SRAM space, and pushes the Heap towards the Stack. The space occupied by this variables streamed to SRAM space will be saved at its location and will not be changing, meaning more of these variables are created, they will use more space and consequently, system failure due to low and poor memory management. 

PROGMEM stands simply for **Program Memory**. We will use Program memory to store variable data offloading to Flash Memory space. As it goes same as to String Wrapper F(), PROGMEM uses Flash Memory space for its implementation. The only disadvantage presented using PROGMEM is the Read Speed. Using RAM will provide much faster Read Speed, but PROGMEM, as it uses Flash Memory, it will be slower than RAM, given the same data size. Thus, it is important to design the software knowing which variables are crucial and which has lower priority. It is one of the many factors that needs to be considered when developing the software, but this will lead to have nicely designed code architecture.

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

#### Non Dynamic Memory Allocation 
Dynamic Memory Allocation usually is a good method if the given RAM size is big enough to get around with, from MegaBytes and so on. However, for embedded devices counting every Byte of the RAM, the process becomes hostile for RAM.

Dynamic Memory Allocations cause **Heap fragmentation**. With heap fragmentation, many areas of the RAM affected by it cannot reused again, leaving dead Byte that can be taken as an advantage for other tasks. On top of it, when dynamic allocation proceeds to de-allocate to free up the space, it does not necessarily reduce the Heap Size. So to avoid Heap or RAM fragmentation as much as possible, you can follow following rules to apply into code architecture design. 

- Prioritize using **Stack** than **Heap** if possible to do so.
  - Stack memory is fragmentation free and can be freed up completely when the function returns. Heap in contrast ma not free up the space even though it was instructed to do so. Using Local Variables will help to do this and try not to use dynamic memory allocation, composed of different calls: `malloc, calloc, realloc`.

- Reduced Global and Static Data if possible to do so.
  - Meantime the code is running, memory area occupied by these data will not be freed up. Meaning the data won't be modified as it is constant data taking up the precious space.

- Short Strings / Literals
  - It is good practice to keep the literal Strings as short as possible. Single char takes **One** Byte of RAM, so shorter the better memory space usage. This does not mean, keeping it short and using it in several different areas of the code is possible. Use it when it is absolutely required and keep as short as possible to spare RAM space for other task functions. 

  - Arrays are also recommended to be at a minimum size. If it requires to resize the array, you can always re-set the array size in the code. It may be a tedious, also non-efficient method to hard-code the array sizes. But if the code utilizes small array sizes and less than 3 arrays, it may be suffice via manual resizing, knowing the requirements. A smart way to do this is resizeable array with limited size. In which the tasks will use the array without going over the size boundary, thus it is suitable for extensive code size. Although, the limit of the array size must be analyzed and kept as small as possible. 

#### RESERVE()
If the tasks work with the Strings, that changes in its size depending on the operation outcome, `RESERVE()` is way to go. This function will help to reserve buffer space and pre-allocate for String variable, which changes in its size, and avoid fragmentation. String variable that changes in its size could be a result of `int` type variable wrapped to be used as a `String` for example.

To use the `RESERVE()` function, it is possible to begin usage with following code piece.

```cpp
// String_Variable is variable of String type
// Alloc_Size is memory to be pre-allocated in number of Bytes with unsigned int type
String_Variable.reserve(Alloc_Size);
```

***For more information about the `RESERVE()` function, please check out [here](https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/reserve/)***

#### Buffer Size Control
Backend processes also requires memory pool for its processing purpose. It is something in which the machine will work on according to the size of the memory pool defined. This Buffer size can be user defined, meaning it can be can reduced to allocate lower memory size. It is similar to defining Array size, in which it is important not to allocate excessive size when it will use only third portion of the defined size. 

In between backend services, Serial communication defines the needed memory pool as Serial Buffer Size. Bigger serial buffer assists in establishing high speed communication, relative to the device that is interchanging data stream. If high speed communication is not part of the requiremente, the buffer size can be redefined to save some memory consumption. This is possible to do so by modifying the `HardwareSerial.h` that comes with Arduino IDE compiler, searching the following line. 

```cpp
#define SERIAL_TX_BUFFER_SIZE 64

#define SERIAL_RX_BUFFER_SIZE 64
```

Libraries, or external modules that involve in code architecture development, also uses Buffer pool for better computing performance. Although, depending on the requirement, smooth performance might be cherry on top for the code architecture that is being developed. It is feasible to modify the buffer size that is designated in the library code.

#### Corrective Data Type Usage
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

EEPROM memory optimization usually is not required, as it will be used mainly to store external module tuning constant. The data which are to be used by EEPROM space are the ones does not really need Flash memory as storage source. On top of it, it is not a good practice to offload SRAM data on EEPROM space. SRAM data are placed within volatility in mind, so offloading to EERPOM space, which is non-volatile memory, will mean the offloaded data will be engraved into EEPROM space. As result, the it is impractical use of storage and the variable will change in its value, making the old data unusable. 

One thing to consider with EEPROM is the read and write operation cycles. With EEPROM, it is crucial to know that write operation is limited. The read operation is unlimited for EEPROM. However, the write operation is finite and capped to 100,000 cycles of operation usually. Thus, it is important to save only parameters that are absolutely important for sensors or modules to work with mostly unchanging data. Additionally avoid implementing in a loop code, to avoid constant write operation, as it will wipe out, most likely in instant. 

### EEPROM Emulation with Flash Memory.

As EEPROM is limited with write operatin cycle, it also applies same to Flash memory. Both of them are subjected to loss of data retention after the manufacturer's defined life cycle. EEPROM is based of NOR type memory, while the Flash memory is NAND type, making the EEPROM more costly than Flash memory. EEPROM works by accessing the data byte-wise, whereas Flash memory accesses block by block. 

Sometimes the developer would have to use the EEPROM as an alternative storage for task operations, but we clearly know that it will be impractical coding due to its size and behaviour properties. To solve this, it is possible to use Flash memory to emulate the EEPROM. Thanks to `FlashStorage` library created by Chrisitan Maglie, it is possible to emulate the EEPROM by using Flash memory. 

***`FlashStorage` library by Christian Maglie can be accessed by [here](https://github.com/cmaglie/FlashStorage)***

Above library will help you to use the Flash memory to emulate the EEPROM, but of course, please remember the EEPROM's properties when using the library. As it is for EEPROM, the Flash memory is also limited in write operation cycle. With two new additional functions stated in the library, one of them being `EEPROM.commit()` should not be called inside a loop function. Otherwise, it will wipe out the Flash memory's write operation cycles, thus loss of data retention ability. 

## Tips & Troubleshooting

Notice that with boards that do not have a lot of SRAM available, like the UNO. It's easy to use it all up by having lots of strings in your program.  For example, a declaration like:
```arduino
char message[] = "I support the Cape Wind project.";
```

puts 33 bytes into SRAM (each character ta|kes a byte, plus the '\0' terminator).  This might not seem like a lot, but it doesn't take long to get to 2048, especially if you have a large amount of text to send to a display, or a large lookup table, for example.

If you run out of SRAM, your program may fail in unexpected ways; it will appear to upload successfully, but not run, or run strangely. To check if this is happening, you can try commenting out or shortening the strings or other data structures in your sketch (without changing the code). If it then runs successfully, you're probably running out of SRAM. There are a few things you can do to address this problem:

- If your sketch talks to a program running on a (desktop/laptop) computer, you can try shifting data or calculations to the computer, reducing the load on the Arduino.

- If you have lookup tables or other large arrays, use the smallest data type necessary to store the values you need; for example, an [int](/en/Reference/Int) takes up two bytes, while a [byte](arduino.cc/en/Reference/Byte) uses only one (but can store a smaller range of values).

- If you don't need to modify the strings or data while your sketch is running, you can store them in flash (program) memory instead of SRAM; to do this, use the [PROGMEM](arduino.cc/en/Reference/PROGMEM) keyword.