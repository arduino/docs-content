---
title: 'String length() and trim() Commands'
compatible-products: [all-boards]
difficulty: beginner
description: 'Get and trim the length of a string.'
tags: 
  - Strings
  - Code
  - Trimming
---

You can get the length of a [Strings](https://www.arduino.cc/en/Reference/StringObject)  using the `length()` command, or eliminate extra characters using the trim() command.  This example shows you how to use both commands.

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.

![](assets/circuit.png)


### Code

`trim()` is useful for when you know there are extraneous whitespace characters on the beginning or the end of a String and you want to get rid of them. *Whitespace* refers to characters that take space but aren't seen. It includes the single space (ASCII 32), tab (ASCII 9), vertical tab (ASCII 11), form feed (ASCII 12), carriage return (ASCII 13), or newline (ASCII 10). The example below shows a String with whitespace, before and after trimming:

```arduino
/*
  String length() and trim()

  Examples of how to use length() and trim() in a String

  created 27 Jul 2010
  modified 2 Apr 2012
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/StringLengthTrim
*/

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString length() and trim():");
  Serial.println();
}

void loop() {
  // here's a String with empty spaces at the end (called white space):
  String stringOne = "Hello!       ";
  Serial.print(stringOne);
  Serial.print("<--- end of string. Length: ");
  Serial.println(stringOne.length());

  // trim the white space off the string:
  stringOne.trim();
  Serial.print(stringOne);
  Serial.print("<--- end of trimmed string. Length: ");
  Serial.println(stringOne.length());

  // do nothing while true:
  while (true);
}
```

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/08/11 by SM*