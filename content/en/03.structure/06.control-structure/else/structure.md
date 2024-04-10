---
title: else
categories: "Structure"
subCategories: "Control Structure"
---

**Description**

The `if...else` allows greater control over the flow of code than the
basic `link:../if[if]` statement, by allowing multiple tests to be
grouped. An `else` clause (if at all exists) will be executed if the
condition in the `if` statement results in `false`. The `else` can
proceed another `if` test, so that multiple, mutually exclusive tests
can be run at the same time.

Each test will proceed to the next one until a true test is encountered.
When a true test is found, its associated block of code is run, and the
program then skips to the line following the entire if/else
construction. If no test proves to be true, the default `else` block is
executed, if one is present, and sets the default behavior.

Note that an `else if` block may be used with or without a terminating
`else` block and vice versa. An unlimited number of such `else if`
branches are allowed.

**Syntax**

    if (condition1) {
      // do Thing A
    }
    else if (condition2) {
      // do Thing B
    }
    else {
      // do Thing C
    }

**Example Code**

Below is an extract from a code for temperature sensor system

    if (temperature >= 70) {
      // Danger! Shut down the system.
    }
    else if (temperature >= 60) { // 60 <= temperature < 70
      // Warning! User attention required.
    }
    else { // temperature < 60
      // Safe! Continue usual tasks.
    }

**See also**

