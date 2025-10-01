---
title: 'SerialEvent'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Demonstrates the use of serialEvent() function.'
tags: 
  - Communication
  - Serial monitor
  - Code
---

This example demonstrates use of the serialEvent() function.  This function is automatically called at the end of `loop()` when there is serial data available in the buffer. In this case, each character found is added to a string until a newline is found. Then the string is printed and set back to null.

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

![](assets/circuit.png)


None, but the board has to be connected to the computer; the Arduino Software (IDE) serial monitor may be used to communicate the single or multiple characters and receive the string back.

### Code

<iframe src='https://create.arduino.cc/example/builtin/04.Communication%5CSerialEvent/SerialEvent/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/07/29 by SM*