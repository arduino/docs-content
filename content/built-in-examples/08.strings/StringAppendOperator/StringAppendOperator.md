---
title: 'String Appending Operators'
compatible-products: [all-boards]
difficulty: intermediate
description: 'Use the += operator and the concat() method to append things to Strings.'
tags: 
  - Strings
  - Append
  - Operators
  - Code
---

Just as you can concatenate Strings with other data objects using the [StringAdditionOperator](/built-in-examples/strings/StringAdditionOperator), you can also use the `+=` operator and the `concat()` method to append things to Strings. The `+=` operator and the `concat()` method work the same way, it's just a matter of which style you prefer.  The two examples below illustrate both, and result in the same String:

```arduino
String stringOne = "A long integer: ";
// using += to add a long variable to a string:
stringOne += 123456789;
```

or

```arduino
String stringTwo = "A long integer: ";
// using concat() to add a long variable to a string:
stringTwo.concat(123456789);
```

In both cases, `stringOne` equals "A long integer: 123456789". Like the `+` operator, these operators are handy for assembling longer strings from a combination of data objects.

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.

![](assets/circuit.png)


### Code

<iframe src='https://create.arduino.cc/example/builtin/08.Strings%5CStringAppendOperator/StringAppendOperator/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/08/11 by SM*