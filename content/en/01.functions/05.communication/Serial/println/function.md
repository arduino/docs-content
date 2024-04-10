---
title: Serial.println()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Prints data to the serial port as human-readable ASCII text followed by
a carriage return character (ASCII 13, or *\r*) and a newline character
(ASCII 10, or *\n*). This command takes the same forms as
[Serial.print()](../print).

**Syntax**

`_Serial_.println(val)`
`_Serial_.println(val, format)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`val`: the value to print. Allowed data types: any data type.
`format`: specifies the number base (for integral data types) or number
of decimal places (for floating point types).

**Returns**

`println()` returns the number of bytes written, though reading that
number is optional. Data type: `size_t`.

**Example Code**

    /*
     Analog input reads an analog input on analog in 0, prints the value out.
     created 24 March 2006
     by Tom Igoe
     */

    int analogValue = 0;    // variable to hold the analog value

    void setup() {
      // open the serial port at 9600 bps:
      Serial.begin(9600);
    }

    void loop() {
      // read the analog input on pin 0:
      analogValue = analogRead(0);

      // print it out in many formats:
      Serial.println(analogValue);       // print as an ASCII-encoded decimal
      Serial.println(analogValue, DEC);  // print as an ASCII-encoded decimal
      Serial.println(analogValue, HEX);  // print as an ASCII-encoded hexadecimal
      Serial.println(analogValue, OCT);  // print as an ASCII-encoded octal
      Serial.println(analogValue, BIN);  // print as an ASCII-encoded binary

      // delay 10 milliseconds before the next reading:
      delay(10);
    }

**Notes and Warnings**

For information on the asyncronicity of `Serial.println()`, see the
Notes and Warnings section of the [Serial.write() reference
page](../write#howtouse).
