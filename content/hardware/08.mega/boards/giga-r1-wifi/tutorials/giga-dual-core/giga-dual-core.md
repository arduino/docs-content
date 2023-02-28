---
title: Guide to GIGA R1 Dual Cores
description: Learn how to access and control the M4 and M7 cores on the GIGA R1
author: Karl Söderby
tags: [Dual Core, M4, M7]
---

The GIGA R1's [STM32H747XI](static/resources/datasheets/stm32h747xi.pdf) has two cores, the M4 and the M7. Each core can be programmed individually, with M7 acting as the main processor, and the M4 as a co-processor.

These two cores can run applications in parallel to each other. For example, running a servo motor on one core, and a display on another, both being blocking operations. In a single core, such operations would slow down the program, resulting in lesser performance.

The M4 and M7 cores are programmed with separate sketches, using the same serial port. In the Arduino IDE, you can select the core you want to program, and then upload the sketch you want to run on that specific core. 

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1-wifi)
- [Arduino IDE](https://www.arduino.cc/en/software)
- Arduino GIGA Core installed.\*

***\*For instructions on how to install the GIGA Core, follow the [Getting Started with GIGA R1 guide](/tutorials/giga-r1-wifi/giga-getting-started).***

## Programming M4/M7

Programming the cores is done via the Arduino IDE, in a special interface that appears only when you **select the Arduino GIGA R1 board** from the board menu. 

### Partioning The Flash Memory

The flash memory can be partionioned into separate by using navigating to **Tools > Flash Split** directly in the IDE.

![Flash partioning in the IDE.](assets/flash-split.png)

- **2MB M7 + M4 in SDRAM (default)** - this option is the default configuration, which is for programming the M7 only. This allocates no memory to the M4.
- **1.5MB M7 + 0.5MB M4** - useful when larger amount of memory is required on the M7.
- **1MB M7 + 1MB M4** - useful when you need to balance the memory equally between the M4 and M7 cores.

***It is required to use option 2 or 3 if you intend to program the M4 via the IDE, as the default option provides no memory allocation for the M4.***

### Target Core

To select the core you want to program, navigate to **Tools > Target Core** in the IDE. 

![Flash partioning in the IDE.](assets/target-core.png)

Here you can choose between:
- **Main Core** - this is the M7 core, the main processor on the board.
- **M4 Co-processor** - this is the M4 core, the co-processor on the board.

### Uploading 

As both cores share the same serial port, choosing the Flash Split + Target Core is required so that the program is uploaded to the correct core.

Uploading is no different to any other Arduino board: simply click the upload button and wait for it to finish.

### Booting M4 Core

The M4 core does not boot by itself; it requires interaction from the M7 core. This function is built into the `RPC` library, and needs to be included in the sketch uploaded to the M7:

```arduino
#include <RPC.h>

void setup() {
  RPC.begin(); //boots M4
}
void loop(){
}
```

Once the M4 is booted from the M7, both cores will run in parallel, much like two Arduinos sharing the same board.

## Limitations

The M7 and M4 cores are two separate cores, and when initialized, they will continue to execute their corresponding program.

In this section you will find some known limitations of using the two parallel cores. 

### Booting M4

As mentioned in the previous section, the M4 requires to be booted from the M7, by using the `RPC.begin()` method.

### Serial Communication

Serial communication is not available by default on the M4 core. A work around for this is by sending data using the `RPC` library, and printing it from the M7 core. To achieve this, see the following examples:

**M4 Sketch**

```arduino
#include <RPC.h>

void setup() {
  RPC.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  RPC.println("Hello World!");
}
```

**M7 Sketch**

```arduino
#include <RPC.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  RPC.begin();
}

void loop() {
  String buffer = "";
    while (RPC.available()) {
      buffer += (char)RPC.read();
    }

    if (buffer.length() > 0) {
      Serial.print(buffer);
    }
}
```

***Note that both of these sketches needs to be uploaded to their corresponding cores.***

## Methods of Programming

Programming the M4 and M7 cores is straightforward, but can be complicated to track. Having a strategy for how you want to build your dual core applications is key. 

In this section we introduce the "single" and "multiple" sketch approach, and the pros and cons of each method.

### Single Sketch Approach

The single sketch approach means writing a single sketch that is uploaded to both cores each time changes are made. In the sketch, we can keep track of what each core does by using simply by querying the core used with a simple function:

```arduino
String currentCPU() {
  if (HAL_GetCurrentCPUID() == CM7_CPUID) {
    return "M7";
  } else {
    return "M4";
  }
}
```

Then, if we are 

### Multiple Sketch Approach

## Use Cases

There are a number of cases where running two cores in parallel brings an advantage. Mainly, it allows one to develop code to run simultaneously, each performing their own individual tasks.

In all modern computers, including yours, you have several cores each occupied with a number of task, in order to speed things up. This is particularly useful in blocking operations such as:
- Controlling a servo motor, 
- Loading a display,
- Connecting to a network.

### Choosing Core

Simply speaking, the M7 should always run your main program, or the most intensive program. It is overall a faster processor that reads memory and executes instructions faster.

For example, you should be running network applications on the M7, while you do sensor readings on the M4. 

***To get a more detailed view on the differences between M4 and M7, see [Arm Cortex-M Processor Comparison Table](https://developer.arm.com/documentation/102787/latest).***

### Wi-Fi / Bluetooth®

Wi-Fi and Bluetooth® applications are best run on the M7, as they are more demanding. Lower level tasks, such as controlling relays, reading sensor data and so forth, can be distributed to the M4 core instead.

### Displays

As the M7 is faster, it is best to run display sketches on the M7 core. Displays have a lot of blocking operations, and it is a good idea to separate the display's functionalities and other operations we want to perform.

### Robotics

For robotics projects, separating the motor control **between the cores** can be beneficial. For example, servo control is a blocking operation, so if you are running several servos at the same time, performance can be reduced.

It can also be distributed so that one core handles servo motors, and one handles stepper motors, if you are using multiple types of motors.

### Sensors

Sensor readings in itself does not matter much which core you use. If you are simply running some tests, it is good to run it on the M7, as you are able to print the results using `Serial.print()` (not available on M4, only through RPC).

When used in relation to a e.g. a display, it is good practice to read sensors on the M4 core and on the M7, fetch the result and display it. 


- “in the IDE you’ll find a submenu that lets you select which core you want to program” **Fixed**
- “the main one is M7, while M4 is a coprocessor” - what does this mean in pratice? what happens if I program one and not the other one? what happens if I want to clear one core and only work with the other one?
- what is a partitioning scheme? what options are there? how do I choose among them?
- if I want to use WiFi/BLE/Cloud, should I use a specific processor?
- if I want to use other hardware pins/peripherals, should I use a specific processor? does the coprocessor have any limitation?
- can both cores write to Serial?
- use cases (parallelization, separation of lower-level operations like motor/GPIO control and higher-level logic like networking, separation of display/UI from other blocking operations for smoother interaction)
- API reference: how do I detect which core I’m running on? (hint -> this can be useful in case you want to put everything a single sketch instead of maintaining two different sketches)