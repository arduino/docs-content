---
title: while
categories: "Structure"
subCategories: "Control Structure"
---

**Description**

A `while` loop will loop continuously, and infinitely, until the
expression inside the parenthesis, () becomes false. Something must
change the tested variable, or the while loop will never exit. This
could be in your code, such as an incremented variable, or an external
condition, such as testing a sensor.

**Syntax**

    while (condition) {
      // statement(s)
    }

**Parameters**

`condition`: a boolean expression that evaluates to `true` or `false`.

**Example Code**

    var = 0;
    while (var < 200) {
      // do something repetitive 200 times
      var++;
    }

**See also**

-   EXAMPLE [While
    Loop^](https://www.arduino.cc/en/Tutorial/BuiltInExamples/WhileStatementConditional)
