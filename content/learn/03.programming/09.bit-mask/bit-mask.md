---
author: Arduino
title: "Bit Masks with Arduino"
description: 'Bit masks are used to access specific bits in a byte of data.'
tags: [Bitwise Operations, Bit Masks]
---

Bit masks are used to access specific bits in a byte of data. This is often useful as a method of iteration, for example when sending a byte of data serially out a single pin. In this example the pin needs to change it's state from high to low for each bit in the byte to be transmitted. This is accomplished using what are known as bitwise operations and a bit mask.

Bitwise operations perform logical functions that take affect on the bit level. Standard bitwise operations include  AND (&) OR (|) Left Shift (`<<`) and Right Shift (`>>`).

The AND (&) operator will result in a 1 at each bit position where both input values were 1.
For example:

```arduino
    x:  10001101

    y:  01010111

x & y:  00000101
```

The OR (|) operator (also known as Inclusive Or) will result in a 1 at each bit position where either input values were 1.
For example:

```arduino
    x:  10001101

    y:  01010111

x | y:  11011111
```

The Left Shift (`<<`) operator will shift a value to the left the specified number of times.
For example:

```arduino
        y = 1010

        x = y << 1

yields: x = 10100
```

All the bits in the byte get shifted one position to the left and the bit on the left end drops off.

The Right Shift (>>) operator works identically to left shift except that it shifts the value to the right the specified number of times
For example:

```arduino
        y = 1010

        x = y >> 1

yields: x = 0101
```

All the bits in the byte get shifted one position to the right and the bit on the right end drops off.

For a practical example, let's take the value 170, binary 10101010. To pulse this value out of pin 7 the code might look as follows:

```arduino
byte transmit = 7; //define our transmit pin
byte data = 170; //value to transmit, binary 10101010
byte mask = 1; //our bitmask
byte bitDelay = 100;

void setup()
{

   pinMode(transmit,OUTPUT);
}

void loop()
{

  for (mask = 00000001; mask>0; mask <<= 1) { //iterate through bit mask

    if (data & mask){ // if bitwise AND resolves to true

      digitalWrite(transmit,HIGH); // send 1

    }

    else{ //if bitwise and resolves to false

      digitalWrite(transmit,LOW); // send 0

    }

    delayMicroseconds(bitDelay); //delay

  }
}
```

Here we use a FOR loop to iterate through a bit mask value, shifting the value one position left each time through the loop. In this example we use the `<<=` operator which is exactly like the `<<` operator except that it compacts the statement

```arduino
  00000001
& 10101010

  ________

  00000000
```

And our output pin gets set to 0.
Second time through the loop the mask = 00000010, so our operation looks like:

```arduino
  00000010
& 10101010

  ________

  00000010
```

And our output pin gets set to 1. The loop will continue to iterate through each bit in the mask until the 1 gets shifted left off the end of the 8 bits and our mask =0. Then all 8 bits have been sent and our loop exits.
