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

## Common Examples

Arduino Runtime was created to simplify the code creation when programming in MicroPython, providing a more user-friendly syntax that allows you to understand the programs you create a bit better.

Now that we have everything installed, and our basic example tested out, let's take a look at some of the more common examples. 

***A list of commands are listed [later in this article](). You can also view the [source code on Github]() for further understanding.***

### Pin Mode

- `pin_mode(pin, mode)`

Configures a pin as an input or an output.

### Analog Read

- `analog_read(pin)`

Analog read is a classic example where you read the voltage from an analog pin.

```python
pin = "A0"

def setup():
  print("Analog Read Example")

def loop():
  value = analog_read(pin)
  print(value)

start(setup, loop)
```

### Analog Write (PWM)

- `analog_write(pin, duty_cycle)`

To write an analog signal (using PWM), we can use the `analog_write()` method. This function takes a `pin` and the `duty_cycle` (0-255) as input.

The example below sets the pin to "half capacity", and if you connect an LED to this pin, it will shine at half brightness.

```python
pin = "D6"
brightness = 127 #half brightness

def setup():
    print("Analog Write Example")

def loop():
    analog_write(pin, brightness)

start(setup, loop)
```

### Digital Read

- `digital_read(pin)`

Reads a digital pin and returns a HIGH (1) or LOW (0) value.

```python
def setup():
    print("Digital Read Example")

def loop():
    value = digital_read("D2")
    print(value)

start(setup, loop)
```

### Digital Write

- `digital_write(pin)`

Writes a HIGH (1) or LOW (0) value to a digital pin.

```python
def setup():
    print("Digital Write Example")

def loop():
    digital_write("D2")
    

start(setup, loop)
```

### Delay

- `delay(time)`

Freezes the program for the duration specified in *microseconds*.

Below is a demonstration of the classic blink example:

```python
led = "D13"

def setup():
    print("Delay Example")
    pin_mode(led, OUTPUT)

def loop():
    digital_write(led, HIGH)
    delay(1000)
    digital_write(led, LOW)
    delay(1000)
    
start(setup, loop)
```

## Runtime Specific Examples

Below are some methods that are introduced with the runtime package.

### Start

- `start(setup, loop, cleanup)`

Starts the program, first by running the `setup()` function, the `loop()` function and finally the `cleanup()` function. 

The `cleanup()` function is optional.

### Cleanup

