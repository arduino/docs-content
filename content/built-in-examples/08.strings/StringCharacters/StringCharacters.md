---
title: 'String Character Functions'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Get/set the value of a specific character in a string.'
tags: 
  - Strings
  - Serial monitor
  - Get character
  - Set character
  - Code
---

The [String](https://www.arduino.cc/en/Reference/StringObject) functions `charAt()` and `setCharAt()` are used to get or set the value of a character at a given position in a String.

At their simplest, these functions help you search and replace a given character.  For example, the following replaces the colon in a given String with an equals sign:

```arduino
String reportString = "SensorReading: 456";
int colonPosition = reportString.indexOf(':');
reportString.setCharAt(colonPosition, '=');
```

Here's an example that checks to see if the first letter of the second word is 'B':

```arduino
String reportString = "Franklin, Benjamin";
int spacePosition = reportString.indexOf(' ');
if (reportString.charAt(spacePosition + 1) == 'B') {
Serial.println("You might have found the Benjamins.")
}
```

**Caution:**
If you try to get the `charAt` or try to `setCharAt()` a value that's longer than the String's length, you'll get unexpected results. If you're not sure, check to see that the position you want to set or get is less than the string's length using the `length()` function.

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