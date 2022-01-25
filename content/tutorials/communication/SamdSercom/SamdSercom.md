---
author: 'Arduino'
description: 'In this tutorial we explain how to add further serial interfaces to your SAMD based board.'
title: 'Adding more Serial Interfaces to SAMD microcontrollers (SERCOM)'
tags: [Serial]
---

In this tutorial we explain how to add further serial interfaces to your SAMD based board. These interfaces are hardware based and can be of I2C, UART, or SPI type. This is possible because the SAMD microcontroller has six internal serial modules that can be configured individually and just four of them are already configured. The other two are available for mapping onto specific pins. In this tutorial we explain how you can do that.

## Hardware Required

- [Arduino Zero](https://www.arduino.cc/en/Main/ArduinoBoardZero), [MKRZero](https://www.arduino.cc/en/Main/ArduinoBoardMKRZero) or [MKR1000](https://www.arduino.cc/en/Main/ArduinoMKR1000) Board

## Circuit

Only your Arduino Board is needed for this example.

![](assets/ArduinoZero_bb.jpg)

## Pin functions

One of the advantages of the Arduino platform is the simplification of the hardware, assigning to each microcontroller pin one of the many possible functions. You can find the various functions assigned to each pin in the variant.cpp file of each board. Let's see, for example, the variant.cpp for the [MKR1000](https://raw.githubusercontent.com/arduino/ArduinoCore-samd/master/variants/mkr1000/variant.cpp).

Focusing our attention on the SERCOM related pins, we can extract the following information:

```arduino
/*

 +------------+------------------+---------+---------+----------+

 | Pin number |  MKR  Board pin  | Perip.C | Perip.D | Periph.G |

 |            |                  | SERCOMx | SERCOMx |    COM   |

 |            |                  | (x/PAD) | (x/PAD) |          |

 +------------+------------------+---------+---------+----------+

 | 00         | D0               |   3/00  |   5/00  |          |

 | 01         | D1               |   3/01  |   5/01  | USB/SOF  |

 | 02         | D2               |   0/02  |   2/02  | I2S/SCK0 |

 | 03         | D3               |   0/03  |   2/03  | I2S/FS0  |

 | 04         | D4               |         |   4/02  | I2S/MCK1 |

 | 05         | D5               |         |   4/03  | I2S/SCK1 |

 | 06         | D6               |   5/02  |   3/02  | I2S/SCK0 |

 | 07         | D7               |   5/03  |   3/03  | I2S/FS0  |

 +------------+------------------+---------+---------+----------+

 |            |       SPI        |         |         |          |

 | 08         | MOSI             |  *1/00  |   3/00  |          |

 | 09         | SCK              |  *1/01  |   3/01  |          |

 | 10         | MISO             |  *1/03  |   3/03  | I2S/SD0  |

 +------------+------------------+---------+---------+----------+

 |            |       Wire       |         |         |          |

 | 11         | SDA              |  *0/00  |   2/00  | I2S/SD1  |

 | 12         | SCL              |  *0/01  |   2/01  | I2S/MCK0 |

 +------------+------------------+---------+---------+----------+

 |            |      Serial1     |         |         |          |

 | 13         | RX               |         |  *5/03  |          |

 | 14         | TX               |         |  *5/02  |          |

 +------------+------------------+---------+---------+----------+

 | 16         | A1               |         |   5/00  |          |

 | 17         | A2               |         |   5/01  |          |

 | 18         | A3               |         |   0/00  |          |

 | 19         | A4               |         |   0/01  |          |

 | 20         | A5               |         |   0/02  |          |

 | 21         | A6               |         |   0/03  | I2S/SD0  |

 +------------+------------------+---------+---------+----------+

 |            | ATWINC1501B SPI  |         |         |          |

 | 26         | WINC MOSI        |  *2/00  |   4/00  |          |

 | 27         | WINC SCK         |  *2/01  |   4/01  |          |

 | 28         | WINC SSN         |   2/02  |   4/02  |          |

 | 29         | WINC MISO        |  *2/03  |   4/03  |          |

 +------------+------------------+---------+---------+----------+

 |            | ATWINC1501B PINS |         |         |          |

 | 32         | WINC WAKE        |         |   4/00  |          |

 | 33         | WINC IRQN        |         |   4/01  |          |

 +------------+------------------+---------+---------+----------+

 */
```

As you can see, SERCOMs can be routed almost everywhere, having more than one SERCOM routable on more than one pin.

## Default assigned SERCOMs

On the header of the MKR1000 boards, you can find an SPI, I2C and UART interface positioned as follows:

- SPI / *SERCOM 1*:

- MOSI on pin 8;

- SCK on pin 9;

- MISO on pin 10;

- I2C / *SERCOM 0*:

- SDA on pin 11;

- SCL on pin 12;

- UART / *SERCOM 5*:

- RX on pin 13;

- TX on pin 14;

Additionally there is another SPI interface internally connected to the WINC1500 module, wired as follows:

- WINC1500 SPI / *SERCOM 2*:

- MOSI on pin 26;

- SCK on pin 27;

- MISO on pin 29;

So removing from our table the pre-existing interfaces, since our aim is to add new interfaces instead of changing the pre-defined ones, we obtain what follows:

```arduino
/*

 +------------+------------------+---------+---------+----------+

 | Pin number |  MKR  Board pin  | Perip.C | Perip.D | Periph.G |

 |            |                  | SERCOMx | SERCOMx |    COM   |

 |            |                  | (x/PAD) | (x/PAD) |          |

 +------------+------------------+---------+---------+----------+

 | 00         | D0               |   3/00  |   5/00  |          |

 | 01         | D1               |   3/01  |   5/01  | USB/SOF  |

 | 02         | D2               |   0/02  |   2/02  | I2S/SCK0 |

 | 03         | D3               |   0/03  |   2/03  | I2S/FS0  |

 | 04         | D4               |         |   4/02  | I2S/MCK1 |

 | 05         | D5               |         |   4/03  | I2S/SCK1 |

 | 06         | D6               |   5/02  |   3/02  | I2S/SCK0 |

 | 07         | D7               |   5/03  |   3/03  | I2S/FS0  |

 +------------+------------------+---------+---------+----------+

 | 16         | A1               |         |   5/00  |          |

 | 17         | A2               |         |   5/01  |          |

 | 18         | A3               |         |   0/00  |          |

 | 19         | A4               |         |   0/01  |          |

 | 20         | A5               |         |   0/02  |          |

 | 21         | A6               |         |   0/03  | I2S/SD0  |

 +------------+------------------+---------+---------+----------+

 */
```

## Adding a new communication interface

Let's now try to use the table above to add a new interface to our MKR1000 board.

### Create a new Wire instance

As we can see, pin 0 and pin 1 can be driven by two SERCOMs. In particular by SERCOM3 and SERCOM5. Looking at the SAMD21 datasheet, we can figure out that the SERCOM PAD0 can be used as SDA and the SERCOM PAD1 as SCL. So we can do this using the example below.

```arduino
/* Wire Slave Sender on pins 0 and 1 on MKR1000

 Demonstrates use of the Wire library and how to instantiate another Wire

 Sends data as an I2C/TWI slave device

 Refer to the "Wire Master Reader" example for use with this

 Created 20 Jun 2016

 by

 Arturo Guadalupi <a.guadalupi@arduino.cc>

 Sandeep Mistry <s.mistry@arduino.cc>

*/

#include <Wire.h>
#include "wiring_private.h"

TwoWire myWire(&sercom3, 0, 1);   // Create the new wire instance assigning it to pin 0 and 1

void setup()
{

  myWire.begin(2);                // join i2c bus with address #2

  pinPeripheral(0, PIO_SERCOM);   //Assign SDA function to pin 0

  pinPeripheral(1, PIO_SERCOM);   //Assign SCL function to pin 1

  myWire.onRequest(requestEvent); // register event
}

void loop()
{

  delay(100);
}

// function that executes whenever data is requested by master
// this function is registered as an event, see setup()
void requestEvent()
{

  myWire.write("hello "); // respond with message of 6 bytes

                          // as expected by master
}

// Attach the interrupt handler to the SERCOM

extern "C" {

  void SERCOM3_Handler(void);

  void SERCOM3_Handler(void) {

    myWire.onService();

  }
}


```

the two instructions use the internal function `pinPeripheral (pinnumber, function)` that reassigns the pins

```arduino
pinPeripheral(0, PIO_SERCOM);   //Assign SDA function to pin 0

pinPeripheral(1, PIO_SERCOM);   //Assign SCL function to pin 1
```

must be put in the `setup()` in order to override the standard Arduino pin assignment for this board (digital I/O) and to allow the SERCOM to drive them.

The callback

```arduino
void SERCOM3_Handler(void) {

  myWire.onService();
}
```

is used to allow the real I2C communication, since the Wire library relies on interrupts.

### Create a new Serial instance

```arduino
/*

  AnalogReadSerial on new UART placed on pins 1 and 0

  Reads an analog input on pin A0, prints the result to the serial monitor.

  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)

  Attach the center pin of a potentiometer to pin A0, and the outside pins to +3.3V and ground.

  Short together pin 1 and pin 0 with a wire jumper

 Created 20 Jun 2016

 by

 Arturo Guadalupi <a.guadalupi@arduino.cc>

  This example code is in the public domain.

*/

#include <Arduino.h>
#include "wiring_private.h"

Uart mySerial (&sercom3, 1, 0, SERCOM_RX_PAD_1, UART_TX_PAD_0); // Create the new UART instance assigning it to pin 1 and 0

// the setup routine runs once when you press reset:
void setup() {

  // initialize serial communication at 9600 bits per second:

  Serial.begin(9600);

  mySerial.begin(9600);

  pinPeripheral(1, PIO_SERCOM); //Assign RX function to pin 1

  pinPeripheral(0, PIO_SERCOM); //Assign TX function to pin 0
}

// the loop routine runs over and over again forever:
void loop() {

  // read the input on analog pin 0:

  int sensorValue = analogRead(A0);

  // print out the value you read on mySerial wired in loopback:

  mySerial.write(sensorValue);

  while (mySerial.available()) {

    Serial.print(mySerial.read());

  }

  Serial.println();

  delay(1);        // delay in between reads for stability
}

// Attach the interrupt handler to the SERCOM
void SERCOM3_Handler()
{

  mySerial.IrqHandler();
}
```

as we did for Wire, the two instructions

```arduino
pinPeripheral(1, PIO_SERCOM); //Assign RX function to pin 1

pinPeripheral(0, PIO_SERCOM); //Assign TX function to pin 0
```

must be placed in order to override the standard Arduino pin assignment for this board (digital I/O) and to allow the SERCOM to drive them.

The callback

```arduino
void SERCOM3_Handler()
{

  mySerial.IrqHandler();
}
```

is used to allow the real Serial communication, since the Serial library relies on interrupts too.