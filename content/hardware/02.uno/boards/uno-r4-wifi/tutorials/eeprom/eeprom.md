---
title: 'Arduino UNO R4 WiFi EEPROM'
description: 'Learn how to access the EEPROM memory on the UNO R4 WiFi.'
tags:
  - RTC
  - Alarm
author: 'Karl Söderby'
hardware:
  - hardware/02.hero/boards/uno-r4-wifi
---

In this tutorial you will learn how to access the EEPROM (memory) on an **Arduino UNO R4 WiFi** board. The EEPROM is embedded in the UNO R4 WiFi's microcontroller (RA4M1).

## Goals

The goals of this tutorials are:

- Write to the EEPROM memory,
- read from the EEPROM memory.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software))
- [Arduino UNO R4 WiFi](https://store.arduino.cc/uno-r4-wifi)
- [UNO R4 Board Package](/tutorials/uno-r4-wifi/r4-wifi-getting-started)

## EEPROM

Electronically erasable programmable read-only memory (EEPROM) is a memory that can be used to store data that can be retrieved after power loss - it is non-volatile. EEPROM memory can be useful during run-time to log data, or can be used to re-initialize variables whenever a system comes back online.

When writing to the EEPROM memory, we specify two parameters: the **address** and **value**. Each byte can hold a value between 0-255.

```arduino
EEPROM.write(0,15); //writes the value 15 to the first byte
```

We are writing a value of `15` to the first byte available in the memory, `0`.

To read the value of this memory, we simply use:

```arduino
EEPROM.read(0); //reads first byte
```

There are several more methods available when working with EEPROM, and you can read more about this in the [A Guide to EEPROM](https://docs.arduino.cc/learn/programming/eeprom-guide).

***Please note: EEPROM is a type of memory with a limited amount of write cycles. Be cautious when writing to this memory as you may significantly reduce the lifespan of this memory.***

### EEPROM Write 

A minimal example on how to **write** to the EEPROM can be found below:

```arduino
#include <EEPROM.h>

int addr = 0;
byte value = 100; 

void setup() {
  EEPROM.write(addr, value);
}
void loop(){ 
}
```

### EEPROM Read

A minimal example of how to **read** from the EEPROM can be found below:

```arduino
#include <EEPROM.h>

int addr = 0;
byte value;

void setup() {
  Serial.begin(9600);
  value = EEPROM.read(addr);
  while (!Serial) {

  }

  Serial.print("Address 0: ");
  Serial.println(value);
}

void loop() {
}
```

## Summary

In this tutorial, you've learned how to access the EEPROM on the UNO R4 WiFi board. To learn more about EEPROM, visit [A Guide to EEPROM](https://docs.arduino.cc/learn/programming/eeprom-guide).
