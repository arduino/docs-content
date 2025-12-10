---
title: 'Character Analysis'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Use the operators to recognise the type of character we are dealing with.'
tags: 
  - Strings
  - Input
  - Serial monitor
  - Code
---

In this example we use the operators that allow us to recognise the type of character we are dealing with. It is useful to check if a character is  ASCII, or is upper case, or numeric, or it is a punctuation mark and so forth. The options available cover a variety of situations and this is demonstrated in the sketch below. Every character sent to the board through the serial monitor of the Arduino Software (IDE) is analysed by the sketch that returns all the information it was able to find.  A single character may trigger more than one condition and therefore you may get multiple answers for a single entry.

The available operators are:

- *isAlphaNumeric()*
 it's alphanumeric

- *isAlpha()*
 it's alphabetic

- *isAscii()*
 it's ASCII

- *isWhitespace()*
 it's whitespace

- *isControl()*
 it's a control character

- *isDigit()*
 it's a numeric digit

- *isGraph()*
 it's a printable character that's not whitespace

- *isLowerCase()*
 it's lower case

- *isPrintable()*
 it's printable

- *isPunct()*
 it's punctuation

- *isSpace()*
 it's a space character

- *isUpperCase()*
 it's upper case

- *isHexadecimalDigit()*
 it's a valid hexadecimaldigit (i.e. 0 - 9, a - F, or A - F)

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.

![](assets/circuit.png)


### Code

Open the serial monitor window of the Arduino Software (IDE) and type in a single character at a time, then press Send to get a report about that specific character.

```arduino

/*

  Character analysis operators

  Examples using the character analysis operators.

  Send any byte and the sketch will tell you about it.

  created 29 Nov 2010

  modified 2 Apr 2012

  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/CharacterAnalysis

*/

void setup() {

  // Open serial communications and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  }

  // send an intro:

  Serial.println("send any byte and I'll tell you everything I can about it");

  Serial.println();
}

void loop() {

  // get any incoming bytes:

  if (Serial.available() > 0) {

    int thisChar = Serial.read();

    // say what was sent:

    Serial.print("You sent me: \'");

    Serial.write(thisChar);

    Serial.print("\'  ASCII Value: ");

    Serial.println(thisChar);

    // analyze what was sent:

    if (isAlphaNumeric(thisChar)) {

      Serial.println("it's alphanumeric");

    }

    if (isAlpha(thisChar)) {

      Serial.println("it's alphabetic");

    }

    if (isAscii(thisChar)) {

      Serial.println("it's ASCII");

    }

    if (isWhitespace(thisChar)) {

      Serial.println("it's whitespace");

    }

    if (isControl(thisChar)) {

      Serial.println("it's a control character");

    }

    if (isDigit(thisChar)) {

      Serial.println("it's a numeric digit");

    }

    if (isGraph(thisChar)) {

      Serial.println("it's a printable character that's not whitespace");

    }

    if (isLowerCase(thisChar)) {

      Serial.println("it's lower case");

    }

    if (isPrintable(thisChar)) {

      Serial.println("it's printable");

    }

    if (isPunct(thisChar)) {

      Serial.println("it's punctuation");

    }

    if (isSpace(thisChar)) {

      Serial.println("it's a space character");

    }

    if (isUpperCase(thisChar)) {

      Serial.println("it's upper case");

    }

    if (isHexadecimalDigit(thisChar)) {

      Serial.println("it's a valid hexadecimaldigit (i.e. 0 - 9, a - F, or A - F)");

    }

    // add some space and ask for another byte:

    Serial.println();

    Serial.println("Give me another byte:");

    Serial.println();

  }
}
```

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/08/11 by SM*