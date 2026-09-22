---
title: 'Encoder Example With MKR Vidor 4000'
description: 'Manage easily quadrature encoders and never lose an impulse with the MKR Vidor 4000.'
difficulty: 'advanced'
tags: [Quadrature Encoders]
author: Arduino
---

## Hardware Required

- [Arduino MKR Vidor 4000](https://store.arduino.cc/arduino-vidor-4000)
- A quadrature encoder

## Circuit

The encoder is connected as follows:

- ENC_A to A0

- ENC_B to A1

![The circuit for this tutorial.](assets/vidor-circuit.png)

| Pin name | Description | Pin number |
| -------- | ----------- | ---------- |
| AREF     |             | 0          |
| A0       | ENC0_A      | 1          |
| A1       | ENC0_B      | 2          |
| A2       | ENC1_A      | 3          |
| A3       | ENC1_B      | 4          |
| A4       | ENC2_A      | 5          |
| A5       | ENC2_B      | 6          |
| A6       | ENC3_A      | 7          |
| D0       | ENC3_B      | 8          |
| D1       | ENC4_A      | 9          |
| D2       | ENC4_B      | 10         |
| D3       | ENC5_A      | 11         |
| D4       | ENC5_B      | 12         |
| D5       | ENC6_A      | 13         |
| D6       | ENC6_B      | 14         |
| D7       | ENC7_A      | 15         |
| D8       | ENC7_B      | 16         |
| D9       | ENC8_A      | 17         |
| D10      | ENC8_B      | 18         |
| D11      | ENC9_A      | 19         |
| D12      | ENC9_B      | 20         |
| D13      | ENC10_A     | 21         |
| D14      | ENC10_B     | 22         |

## Code

Include the VidorEncoder library, which is part of VidorPeripherals.
`#include "VidorPeripherals.h"`
`#include "VidorEncoder.h"`

You have a number of functions available to manage the encoder:

- `VidorEncoder(int index)` - refer to pinout tab for pinout (index) in this page

- `void write(int32_t p);` - resets the count value to "p"

- `int32_t read();` - returns the actual count

```arduino

/*

   This sketch shows how to use the Encoder IP in MKRVidor 4000

   Quadrature encoders are a very common way to detect position (and speed) of a moving part, like a DC motor.

   Normally, in the microcontroller world, decoding a quadrature encoder has serious limitations since all edges must be counted, otherwise the final number will be wrong. This is usually accomplished using interrupts, but over a certain revolution speed the intinsic overhead of servicing an interrupt destroys the count reliability.

   Using the FPGA to perform decoding allows:

    - not to lose any edge until the revolution speed is less than some million RPM :)

    - we can "read" the encoder at any time, because the FPGA is counting independently

    Circuit:

      connect ENC_A to A0 and ENC_B to A1

*/

#include "VidorGraphics.h"
#include "VidorEncoder.h"

// Initialize Encoder #0 (connected to A0 and A1)
// Refer to the online documentation to find which pins correspond to a given index
// This assignment may change between bitstreams

VidorEncoder encoder(0);

void setup() {

  Serial.begin(9600);

  // wait for the serial monitor to open,

  // if you are powering the board from a USB charger remove the next line

  while (!Serial);

  // Let's start the FPGA

  if (!FPGA.begin()) {

    Serial.println("Initialization failed!");

    while (1) {}

  }
}

void loop() {

  // Read the encoder

  int value = encoder.read();

  Serial.print("Encoder value: ");

  Serial.println(value);

#if 1

  // Wait one second with interrupts disabled

  noInterrupts();

  // We can't call delay() since it uses interrupts, so use busy loops

  for (int i = 0; i < F_CPU / 10; i++) {

    asm ("nop");

  }

  interrupts();

#else

  delay(200);
#endif

  if (value >= 200 || value <= -200) {

    // Reset the count

    encoder.write(0);

  }
}
```


**Last revision 2018/07/22 by SM**
