---
title: 'String indexOf() and lastIndexOf() Method'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Look for the first/last instance of a character in a string.'
tags: 
  - Strings
  - Code 
---

The [String object](https://www.arduino.cc/en/Reference/StringObject) indexOf() method gives you the ability to search for the first instance of a particular character value in a String.  You can also look for the first instance of the character after a given offset. The lastIndexOf() method lets you do the same things from the end of a String.

```arduino
String stringOne = "<HTML><HEAD><BODY>";
int firstClosingBracket = stringOne.indexOf('>');
```

In this case, `firstClosingBracket` equals 5, because the first `>` character is at position 5 in the String (counting the first character as 0). If you want to get the second closing bracket, you can use the fact that you know the position of the first one, and search from `firstClosingBracket + 1` as the offset, like so:

```arduino
stringOne = "<HTML><HEAD><BODY>";
int secondClosingBracket = stringOne.indexOf('>', firstClosingBracket + 1 );
```

The result would be 11, the position of the closing bracket for the HEAD tag.

If you want to search from the end of the String, you can use the `lastIndexOf()` method instead. This function returns the position of the last occurrence of a given character.

```arduino
stringOne = "<HTML><HEAD><BODY>";
int lastOpeningBracket = stringOne.lastIndexOf('<');
```

In this case, `lastOpeningBracket` equals 12, the position of the `<` for the BODY tag. If you want the opening bracket for the HEAD tag, it would be at `stringOne.lastIndexOf('<', lastOpeningBracket -1)`, or 6.

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.

![](assets/circuit.png)


### Code

<iframe src='https://create.arduino.cc/example/builtin/08.Strings%5CStringIndexOf/StringIndexOf/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/08/11 by SM*