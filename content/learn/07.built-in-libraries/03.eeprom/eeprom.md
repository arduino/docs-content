---
title: EEPROM Library
description: Documentation for usage of the EEPROM library. EEPROM is a memory whose values are kept when the board is powered off.
author: 'Arduino'
tags: [EEPROM]
---

The microcontroller on the Arduino and Genuino AVR based board has EEPROM: memory whose values are kept when the board is turned off (like a tiny hard drive). This library enables you to read and write those bytes.

The supported micro-controllers on the various Arduino and Genuino boards have different amounts of EEPROM: 1024 bytes on the ATmega328P, 512 bytes on the ATmega168 and ATmega8, 4 KB (4096 bytes) on the ATmega1280 and ATmega2560. The Arduino and Genuino 101 boards have an emulated EEPROM space of 1024 bytes.

To use this library

```
#include <EEPROM.h>
```

## Examples

To see a list of examples for the EEPROM library, click the link below:

- [A Guide to EEPROM](/learn/programming/eeprom-guide)

## Functions

### `read()`

#### Description
Reads a byte from the EEPROM. Locations that have never been written to have the value of 255.

#### Syntax

```
EEPROM.read(address)
```

#### Parameters
address: the location to read from, starting from 0 (int)

#### Returns
the value stored in that location (byte)

#### Example

```
#include <EEPROM.h>

int a = 0;
int value;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  value = EEPROM.read(a);

  Serial.print(a);
  Serial.print("\t");
  Serial.print(value);
  Serial.println();

  a = a + 1;

  if (a == 512)
    a = 0;

  delay(500);
}
```

### `write()`

#### Description
Write a byte to the EEPROM.

#### Syntax

```
EEPROM.write(address, value)
```

#### Parameters
address: the location to write to, starting from 0 (int)

value: the value to write, from 0 to 255 (byte)

#### Returns
none

Note: An EEPROM write takes 3.3 ms to complete. The EEPROM memory has a specified life of 100,000 write/erase cycles, so you may need to be careful about how often you write to it.

#### Example

```

#include <EEPROM.h>

void setup()
{
  for (int i = 0; i < 255; i++)
    EEPROM.write(i, i);
}

void loop()
{
}
 
```

### `update()`

#### Description
Write a byte to the EEPROM. The value is written only if differs from the one already saved at the same address.

#### Syntax

```
EEPROM.update(address, value)

```

#### Parameters
address: the location to write to, starting from 0 (int)

value: the value to write, from 0 to 255 (byte)

#### Returns
none

>Note: An EEPROM write takes 3.3 ms to complete. The EEPROM memory has a specified life of 100,000 write/erase cycles, so using this function instead of write() can save cycles if the written data does not change often

#### Example

```

#include <EEPROM.h>

void setup()
{
  for (int i = 0; i < 255; i++) {
    // this performs as EEPROM.write(i, i)
    EEPROM.update(i, i);
  }
  for (int i = 0; i < 255; i++) {
    // write value "12" to cell 3 only the first time
    // will not write the cell the remaining 254 times
    EEPROM.update(3, 12);
  }
}

void loop()
{
}
 
```

### `get()`

#### Description
Read any data type or object from the EEPROM.

#### Syntax

```
EEPROM.get(address, data)

```

#### Parameters
address: the location to read from, starting from 0 (int)

data: the data to read, can be a primitive type (eg. float) or a custom struct

#### Returns
A reference to the data passed in

#### Example

```

#include <EEPROM.h>

struct MyObject{
  float field1;
  byte field2;
  char name[10];
};

void setup(){

  float f = 0.00f;   //Variable to store data read from EEPROM.
  int eeAddress = 0; //EEPROM address to start reading from

  Serial.begin( 9600 );
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  Serial.print( "Read float from EEPROM: " );

  //Get the float data from the EEPROM at position 'eeAddress'
  EEPROM.get( eeAddress, f );
  Serial.println( f, 3 );  //This may print 'ovf, nan' if the data inside the EEPROM is not a valid float.

  // get() can be used with custom structures too.
  eeAddress = sizeof(float); //Move address to the next byte after float 'f'.
  MyObject customVar; //Variable to store custom object read from EEPROM.
  EEPROM.get( eeAddress, customVar );

  Serial.println( "Read custom object from EEPROM: " );
  Serial.println( customVar.field1 );
  Serial.println( customVar.field2 );
  Serial.println( customVar.name );
}

void loop(){ /* Empty loop */ }
 
```

### `put()`

#### Description
Write any data type or object to the EEPROM.

#### Syntax

```
EEPROM.put(address, data)

```

#### Parameters
address: the location to write to, starting from 0 (int)

data: the data to write, can be a primitive type (eg. float) or a custom struct

#### Returns
A reference to the data passed in

>Note: This function uses EEPROM.update() to perform the write, so does not rewrites the value if it didn't change.

#### Example

```

#include <EEPROM.h>

struct MyObject {
  float field1;
  byte field2;
  char name[10];
};

void setup() {

  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  float f = 123.456f;  //Variable to store in EEPROM.
  int eeAddress = 0;   //Location we want the data to be put.


  //One simple call, with the address first and the object second.
  EEPROM.put(eeAddress, f);

  Serial.println("Written float data type!");

  /** Put is designed for use with custom structures also. **/

  //Data to store.
  MyObject customVar = {
    3.14f,
    65,
    "Working!"
  };

  eeAddress += sizeof(float); //Move address to the next byte after float 'f'.

  EEPROM.put(eeAddress, customVar);
  Serial.print("Written custom data type! \n\nView the example sketch eeprom_get to see how you can retrieve the values!");
}

void loop() {   /* Empty loop */ }
 
```

### `EEPROM[]`

#### Description
This operator allows using the identifier `EEPROM` like an array. EEPROM cells can be read and written directly using this method.

#### Syntax

```
EEPROM[address]

```

#### Parameters
address: the location to read/write from, starting from 0 (int)

#### Returns
A reference to the EEPROM cell

#### Example

```

#include <EEPROM.h>

void setup(){

  unsigned char val;

  //Read first EEPROM cell.
  val = EEPROM[ 0 ];

  //Write first EEPROM cell.
  EEPROM[ 0 ] = val;

  //Compare contents
  if( val == EEPROM[ 0 ] ){
    //Do something...
  }
}

void loop(){ /* Empty loop */ }
 
```

### `length()`

This function returns an unsigned int containing the number of cells in the EEPROM.

#### Description

This function returns an `unsigned int` containing the number of cells in the EEPROM.

#### Syntax

```
EEPROM.length()
```

#### Returns

Number of cells in the EEPROM as an `unsigned int`.


