---
title: bitRead()
categories: "Functions"
subCategories: "Bits and Bytes"
---

**Description**

Reads a bit of a variable, e.g. `bool`, `int`. Note that `float` &
`double` are not supported. You can read the bit of variables up to an
`unsigned long long` (64 bits / 8 bytes).

**Syntax**

`bitRead(x, n)`

**Parameters**

`x`: the number from which to read.
`n`: which bit to read, starting at 0 for the least-significant
(rightmost) bit.

**Returns**

The value of the bit (0 or 1).

**Example Code**

This example code demonstrates how to read two variables, one increasing
counter, one decreasing counter, and print out both the binary and
decimal values of the variables.

The `readBit()` function loops through each bit of the variable
(starting from the rightmost bit), and prints it out.

    long negative_var = -0;  //
    unsigned long long positive_var = 0;

    //predefined sizes when looping through bits
    //e.g. long_size is 32 bit (which is 0-31). Therefore, we subtract "1".
    const int bool_size = (1 - 1);
    const int int_size = (8 - 1);
    const int long_size = (32 - 1);

    void setup() {
      Serial.begin(9600);
    }

    void loop() {
      //run readBit function, passing the pos/neg variables
      readBit("Positive ", positive_var);
      readBit("Negative ", negative_var);
      Serial.println();

      //increase and decrease the variables
      negative_var--;
      positive_var++;

      delay(1000);
    }

    /*this function takes a variable, prints it out bit by bit (starting from the right)
    then prints the decimal number for comparison.*/
    void readBit(String direction, long counter) {
      Serial.print(direction + "Binary Number: ");
      //loop through each bit
      for (int b = long_size; b >= 0; b--) {
        byte bit = bitRead(counter, b);
        Serial.print(bit);
      }
      Serial.print(" Decimal Number: ");
      Serial.println(counter);
    }

**See also**

