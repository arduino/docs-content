---
title: 'String startsWith and endsWith Functions'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Check which characters/substrings a given string starts or ends with.'
tags: 
  - Strings
  - Serial monitor
  - Code
---

The [**String**](https://www.arduino.cc/en/Reference/StringObject) functions `startsWith()` and `endsWith()` allow you to check what character or substring a given String starts or ends with. They're basically special cases of `substring`.

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open..

![](assets/circuit.png)


### Code

`startsWith()` and `endsWith()` can be used to look for a particular message header, or for a single character at the end of a String. They can also be used with an offset to look for a substring starting at a particular position.  For example:

```arduino
stringOne = "HTTP/1.1 200 OK";
if (stringOne.startsWith("200 OK", 9)) {
Serial.println("Got an OK from the server");
}
```

This is functionally the same as this:

```arduino
stringOne = "HTTP/1.1 200 OK";
if (stringOne.substring(9) == "200 OK") {
Serial.println("Got an OK from the server");
}
```

**Caution:**
If you look for a position that's outside the range of the string,you'll get unpredictable results.  For example, in the example above stringOne.startsWith("200 OK", 16) wouldn't check against the String itself, but whatever is in memory just beyond it. For best results, make sure the index values you use for `startsWith` and `endsWith` are between 0 and the String's `length()`.

```arduino
/*
  String startWith() and endsWith()

  Examples of how to use startsWith() and endsWith() in a String

  created 27 Jul 2010
  modified 2 Apr 2012
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/StringStartsWithEndsWith
*/

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString startsWith() and endsWith():");
  Serial.println();
}

void loop() {
  // startsWith() checks to see if a String starts with a particular substring:
  String stringOne = "HTTP/1.1 200 OK";
  Serial.println(stringOne);
  if (stringOne.startsWith("HTTP/1.1")) {
    Serial.println("Server's using http version 1.1");
  }

  // you can also look for startsWith() at an offset position in the string:
  stringOne = "HTTP/1.1 200 OK";
  if (stringOne.startsWith("200 OK", 9)) {
    Serial.println("Got an OK from the server");
  }

  // endsWith() checks to see if a String ends with a particular character:
  String sensorReading = "sensor = ";
  sensorReading += analogRead(A0);
  Serial.print(sensorReading);
  if (sensorReading.endsWith("0")) {
    Serial.println(". This reading is divisible by ten");
  } else {
    Serial.println(". This reading is not divisible by ten");
  }

  // do nothing while true:
  while (true);
}
```

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/08/11 by SM*