---
title: 'String Object Constructors'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Initialize string objects.'
tags: 
  - Strings
  - String objects
  - Code
---

The [String object](https://www.arduino.cc/en/Reference/StringObject) allows you to manipulate strings of text in a variety of useful ways. You can append characters to Strings, combine Strings through concatenation, get the length of a String, search and replace substrings, and more.  This tutorial shows you how to initialize String objects.

```arduino
String stringOne = "Hello String";                      // using a constant String
String stringOne =  String('a');                        // converting a constant char into a String
String stringTwo =  String("This is a string");         // converting a constant string into a String object
String stringOne =  String(stringTwo + " with more");   // concatenating two strings
String stringOne =  String(13);                         // using a constant integer
String stringOne =  String(analogRead(0), DEC);         // using an int and a base
String stringOne =  String(45, HEX);                    // using an int and a base (hexadecimal)
String stringOne =  String(255, BIN);                   // using an int and a base (binary)
String stringOne =  String(millis(), DEC);              // using a long and a base
String stringOne =  String(5.698, 3);                   // using a float and the decimal places
```

All of these methods are valid ways to declare a String object.  They all result in an object containing a string of characters that can be manipulated using any of the String methods. To see them in action, upload the code below onto an Arduino board and open the Arduino IDE serial monitor.  You'll see the results of each declaration. Compare what's printed by each println() to the declaration above it.

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.

![](assets/circuit.png)


### Code

<iframe src='https://create.arduino.cc/example/builtin/08.Strings%5CStringConstructors/StringConstructors/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/08/11 by SM*