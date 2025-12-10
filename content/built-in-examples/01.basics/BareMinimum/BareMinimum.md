---
title: 'Bare Minimum code needed'
compatible-products: [all-boards]
difficulty: beginner
description: 'The bare minimum of code needed to start an Arduino sketch.'
tags: 
  - Basics
  - Code
---

This example contains the bare minimum of code you need for a sketch to compile properly on Arduino Software (IDE): the `setup()` method and the `loop()` method.

### Hardware Required

- [Arduino Board](https://store.arduino.cc/collections/boards-modules)

### Circuit

Only your Arduino Board is needed for this example.

![](assets/circuit.png)


### Code

The `setup()` function is called when a sketch starts. Use it to initialize variables, pin modes, start using libraries, etc. The setup function will only run once, after each powerup or reset of the board.

After creating a `setup()` function, the `loop()` function does precisely what its name suggests, and loops consecutively, allowing your program to change and respond as it runs. Code in the `loop()` section of your sketch is used to actively control the board.

The code below won't actually do anything, but it's structure is useful for copying and pasting to get you started on any sketch of your own. It also shows you how to make comments in your code.

Any line that starts with two slashes (//) will not be read by the compiler, so you can write anything you want after it. The two slashes may be put after functional code to keep comments on the same line. Commenting your code like this can be particularly helpful in explaining, both to yourself and others, how your program functions step by step.

<iframe src='https://create.arduino.cc/example/builtin/01.Basics%5CBareMinimum/BareMinimum/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/07/28 by SM*