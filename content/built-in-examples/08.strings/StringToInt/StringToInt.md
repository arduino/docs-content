---
title: 'String to Int Function'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Allows you to convert a String to an integer number.'
tags: 
  - Strings
  - Number
  - Serial monitor
  - Code
---

The [toInt()](https://www.arduino.cc/en/Reference/StringToInt) function allows you to convert a String to an integer number.

In this example, the board reads a serial input string until it sees a newline, then converts the string to a number if the characters are digits. Once you've uploaded the code to your board, open the Arduino IDE serial monitor, enter some numbers, and press send. The board will repeat these numbers back to you. Observe what happens when a non-numeric character is sent.

### Hardware Required:

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.

![](assets/circuit.png)


### Code

<iframe src='https://create.arduino.cc/example/builtin/08.Strings%5CStringToInt/StringToInt/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### See Also

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/08/27 by SM*