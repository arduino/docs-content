---
title: 'String replace Function'
compatible-products: [all-boards]
difficulty: beginner
description: 'The replace() function allows you to replace all instances of a given character in a string with another character.'
tags: 
  - Strings
  - Search and replace
  - Serial monitor
  - Code
---

The [**String**](https://www.arduino.cc/en/Reference/StringObject)`replace()` function allows you to replace all instances of a given character with another character. You can also use `replace` to replace substrings of a String with a different substring.

### Hardware Required

- Arduino Board

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.

![](assets/circuit.png)


### Code

**Caution:**
If you try to replace a substring that's more than the whole String itself, nothing will be replaced.  For example:

```arduino
String stringOne = "<html><head><body>";
stringOne.replace("<html><head></head><body></body></html>", "Blah");
```

In this case, the code will compile, but `stringOne` will remain unchanged, since the replacement substring is more than the String itself.

<iframe src='https://create.arduino.cc/example/builtin/08.Strings%5CStringReplace/StringReplace/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last Revision 2018/03/27 by SM*
