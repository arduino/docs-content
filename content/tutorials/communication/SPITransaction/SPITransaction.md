---
author: 'Arduino'
description: 'In this tutorial you will learn how to use the SPI transaction methods.'
title: 'SPITransaction Method'
tags: [SPI]
---

## SPI transaction example

In this tutorial you will learn how to use the SPI transaction methods. For an explanation of SPI see the [SPI EEPROM tutorial](https://www.arduino.cc/en/Tutorial/SPIEEPROM).

A common problem used to be that different SPI devices needed different, incompatible settings. Your sketch had to take care of saving and restoring the SPI settings before communicating with each SPI device. If any SPI device was accessed from an interrupt, this could result in data corruption if another SPI device was communicating at the time.

With the new SPI library, configure each SPI device once as an SPISettings object. Also, if that device will be called from an interrupt, say so with SPI.usingInterrupt(interruptNumber). To communicate with a specific SPI device, use SPI.beginTransaction which automatically uses the settings you declared for that device. In addition, it will disable any interrupts that use SPI for the duration of the transaction. Once you are finished, use SPI.endTransaction() which re-enables any SPI-using interrupts.

## Code

```arduino
#include <SPI.h>

// using two incompatible SPI devices, A and B. Incompatible means that they need different SPI_MODE

const int slaveAPin = 20;

const int slaveBPin = 21;

// set up the speed, data order and data mode

SPISettings settingsA(2000000, MSBFIRST, SPI_MODE1);

SPISettings settingsB(16000000, LSBFIRST, SPI_MODE3);

void setup() {

  // set the Slave Select Pins as outputs:

  pinMode (slaveAPin, OUTPUT);

  pinMode (slaveBPin, OUTPUT);

  // initialize SPI:

  SPI.begin();
}

uint8_t stat, val1, val2, result;

void loop() {

  // read three bytes from device A

  SPI.beginTransaction(settingsA);

  digitalWrite (slaveAPin, LOW);

  // reading only, so data sent does not matter

  stat = SPI.transfer(0);

  val1 = SPI.transfer(0);

  val2 = SPI.transfer(0);

  digitalWrite (slaveAPin, HIGH);

  SPI.endTransaction();

  // if stat is 1 or 2, send val1 or val2 else zero

  if (stat == 1) {

   result = val1;

  } else if (stat == 2) {

   result = val2;

  } else {

   result = 0;

  }

  // send result to device B

  SPI.beginTransaction(settingsB);

  digitalWrite (slaveBPin, LOW);

  SPI.transfer(result);

  digitalWrite (slaveBPin, HIGH);

  SPI.endTransaction();
}
```
