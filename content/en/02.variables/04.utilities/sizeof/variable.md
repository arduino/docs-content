---
title: sizeof()
categories: "Variables"
subCategories: "Utilities"
---

**Description**

The `sizeof` operator returns the number of bytes in a variable type, or
the number of bytes occupied by an array.

**Syntax**

`sizeof(variable)`

**Parameters**

`variable`: The thing to get the size of. Allowed data types: any
variable type or array (e.g. `link:../../data-types/int[int]`,
`link:../../data-types/float[float]`,
`link:../../data-types/byte[byte]`).

**Returns**

The number of bytes in a variable or bytes occupied in an array. Data
type: `link:../../data-types/size_t[size_t]`.

**Example Code**

The `sizeof` operator is useful for dealing with arrays (such as
strings) where it is convenient to be able to change the size of the
array without breaking other parts of the program.

This program prints out a text string one character at a time. Try
changing the text phrase.

    char myStr[] = "this is a test";

    void setup() {
      Serial.begin(9600);
    }

    void loop() {
      for (byte i = 0; i < sizeof(myStr) - 1; i++) {
        Serial.print(i, DEC);
        Serial.print(" = ");
        Serial.write(myStr[i]);
        Serial.println();
      }
      delay(5000);  // slow down the program
    }

**Notes and Warnings**

Note that `sizeof` returns the total number of bytes. So for arrays of
larger variable types such as [`int`](../../data-types/int)s, the for
loop would look something like this.

    int myValues[] = {123, 456, 789};

    // this for loop works correctly with an array of any type or size
    for (byte i = 0; i < (sizeof(myValues) / sizeof(myValues[0])); i++) {
      // do something with myValues[i]
    }

Note that a properly formatted string ends with the NULL symbol, which
has ASCII value 0.

**See also**
