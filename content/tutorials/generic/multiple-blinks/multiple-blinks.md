---
title: 'Multiple Blinks'
description: 'Run multiple functions simultaneously with the Scheduler Library.'
tags: 
  - Scheduler
  - LED
difficulty: beginner
libraries:
  - name: Scheduler 
    url: https://www.arduino.cc/reference/en/libraries/scheduler/
hardware:
  - hardware/02.hero/boards/due
  - hardware/02.hero/boards/zero
  - hardware/01.mkr/01.boards/mkr-1000-wifi
  - hardware/01.mkr/01.boards/mkr-zero
software:
  - ide-v1
  - ide-v2
  - web-editor
author: "Arduino"
contributeURL: content/tutorials/generic
---


## Introduction

Arduino boards based on SAM and SAMD architectures (i.e Arduino Zero, MKR ZERO, MKR1000 WiFi and Due) to run multiple functions at the same time.  By setting up a number of other functions that run the same way `loop()` does, it's possible to have separate looping functions without a dedicated timer.

## Goals

- How to use the Scheduler library.
- To run multiple functions simultaneously. 

## Hardware & Software Needed

- Arduino Zero, MKR ZERO, MKR1000 WiFi Board. [(Link to store)]()
- Three LEDs
- Three 220 Ω resistors
- Jumper Wires
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [Scheduler library](https://www.arduino.cc/reference/en/libraries/scheduler/)

### The Circuit

The anode of the LEDs are connected in series with a 220-ohm resistor to pins 11, 12, and 13. Their cathodes connect to ground.


### Programming the Board

**1.** First, let's make sure we have correct the drivers installed. If we are using the Cloud Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAM boards (32-bits ARM Cortex-M3)** and install it. 

**2.** Now, we need to install the libraries needed. Simply go to **Tools > Manage libraries...** and search for **Scheduler** and install it.




### Code
Before we begin, let's take a look at some of the core functions of the library:

- `Scheduler.startLoop()` - Adds a function to the scheduler that will run concurrently with `loop()`.

- `yield()` - Passes control to other tasks when called. Ideally `yield()` should be used in functions that will take a while to complete.




```arduino
// Include Scheduler since we want to manage multiple tasks.
#include <Scheduler.h>

int led1 = 13;
int led2 = 12;
int led3 = 11;

void setup() {

  Serial.begin(9600);

  // Setup the 3 pins as OUTPUT

  pinMode(led1, OUTPUT);

  pinMode(led2, OUTPUT);

  pinMode(led3, OUTPUT);

  // Add "loop2" and "loop3" to scheduling.

  // "loop" is always started by default.

  Scheduler.startLoop(loop2);

  Scheduler.startLoop(loop3);
}

// Task no.1: blink LED with 1 second delay.
void loop() {

  digitalWrite(led1, HIGH);

  // IMPORTANT:

  // When multiple tasks are running 'delay' passes control to

  // other tasks while waiting and guarantees they get executed.

  delay(1000);

  digitalWrite(led1, LOW);

  delay(1000);
}

// Task no.2: blink LED with 0.1 second delay.
void loop2() {

  digitalWrite(led2, HIGH);

  delay(100);

  digitalWrite(led2, LOW);

  delay(100);
}

// Task no.3: accept commands from Serial port
// '0' turns off LED
// '1' turns on LED
void loop3() {

  if (Serial.available()) {

    char c = Serial.read();

    if (c=='0') {

      digitalWrite(led3, LOW);

      Serial.println("Led turned off!");

    }

    if (c=='1') {

      digitalWrite(led3, HIGH);

      Serial.println("Led turned on!");

    }

  }

  // IMPORTANT:

  // We must call 'yield' at a regular basis to pass

  // control to other tasks.

  yield();
}
```


## Testing It Out
After you have uploaded the code, two of the LEDs should now light up. One should blink with a 1 second delay and the other should blink with a 0.1 second delay. The third and final LED can be turned on and off using the Serial Monitor. To open the Serial Monitor go to **Tools >Serial Monitor**. Inputting a `0` will turn the LED of whilst a `1` will turn it on.

### Troubleshoot
If the code is not working, there are some common issues we can troubleshoot:

- LEDs / resistors are not wired correctly.
- You have not installed the [Scheduler library](https://www.arduino.cc/reference/en/libraries/scheduler/).


## Conclusion
In this example, we built a project and learned about the Scheduler library that allows Arduino boards based on SAM and SAMD architectures to run multiple functions at the same time.