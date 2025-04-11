---
title: 'Arduino Style MicroPython'
description: 'Learn how to use the runtime package, which allows you to write MicroPython code, Arduino style.'
author: 'Karl Söderby'
tags: [MicroPython, Runtime]
micropython_type: test
---

The [Arduino Runtime Package]() is a MicroPython package that allows you to write and program your board using the classic `setup()` and `loop()` constructs.

The package was designed to make it easier to create programs, particularly for those familiar with the Arduino C++ environment.

In this tutorial, you will learn how the package works, along with a set of examples that will get you started.

## Requirements

To follow this tutorial, you will need to have the following requirements ticked:

### Hardware Requirements

- [A MicroPython compatible board](/micropython/first-steps/install-guide/#micropython-compatible-arduino-boards) (in this tutorial, we will be using an [Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32))
- MicroPython installed on your board (see [installation instructions for MicroPython](/micropython/first-steps/install-guide/)).

### Software Requirements

- [Arduino Lab for Micropython](https://labs.arduino.cc/en/labs/micropython) - an editor where we can create and run MicroPython scripts on an Arduino board.
- [Arduino MicroPython Package Installer](https://labs.arduino.cc/en/labs/micropython-package-installer) - for installing **MicroPython packages** on an Arduino board.

## Installation

To use the runtime library, we will need to install it first.

1. Download and install the [Arduino MicroPython Package Installer](https://labs.arduino.cc/en/labs/micropython-package-installer). 
2. Connect your board to your computer.
3. Run the tool. In the tool, you should now see your board connected.

    ![Board connected.]()

4. After verifying that your board is connected, click on the search field, and search for **runtime**. Install the package.

    ![Install the package.]()

5. When the installation is complete, we are ready to use the library.

## Basic Example

We will begin by one of the most known example: blinking an LED. Let's take a look at the code example below:

```python
from arduino import *

led = 'LED_BUILTIN'
def setup():
  print('starting my program')

def loop():
  print('loopy loop')
  digital_write(led, HIGH)
  delay(500)
  digital_write(led, LOW)
  delay(500)

start(setup, loop)
```

This program has two main functions: `setup()` and `loop()`. If you are unfamiliar with this concept, here's how it works:
- `setup()` - this function will run just once, at the start of a program. Like in this example, we use `print('starting my program')`.
- `loop()` - this function will continue to run, until you disrupt the program by disconnecting the board or stopping the script.

Inside of the functions, you can see that we are using `digital_write(led, HIGH)`. This is a function that will enable a pin on the board, and write it high (or low). Since we configured it at the top as `'LED_BUILTIN'`, we will control that LED on the board.

At the bottom of the program, we have something called `start()`. This function will launch the program and concurrently run the `loop()` function.
