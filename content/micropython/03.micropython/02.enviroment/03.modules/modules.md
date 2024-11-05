---
title: 'Modules'
description: 'Understanding Modules and how to use them.'
author: 'Pedro Lima'
tags: [MicroPython, Modules]
---


In this article, we’ll cover how modules work in MicroPython, explore a few built-in modules, and demonstrate how to install an external package like Modulino to extend our MicroPython project’s functionality.

## What Are Modules?

Modules are collections of functions, classes, and variables organized into separate files, which we can import and use in our main program. Modules allow us to:

- **Reuse Code**: We can import useful functionality instead of writing everything from scratch.
- **Organize Code**: Breaking code into modules makes projects more readable and maintainable.
- **Access Special Functionality**: Some tasks require advanced functions (e.g., time delays or hardware communication) that are available only through modules.

## Built-in Modules

MicroPython comes with a set of built-in modules that provide essential functions for programming tasks. For instance:

- **`time`**: This module allows us to add time delays, get timestamps, and measure durations in code.
- **`os`**: Provides functions to manage the file system, such as creating files or listing directories.
- **`machine`**: A module designed for hardware interaction, allowing us to control pins, I2C, and more.

We can access built-in modules directly without any installation. Here’s a quick example using the `time` module to add a delay:

```python
import time

print("Starting countdown...")
time.sleep(3)  # Pauses the program for 3 seconds
print("Countdown complete!")
```

In this example, `time.sleep()` introduces a delay. Built-in modules like `time` are pre-installed with MicroPython, so we don’t need to install anything extra to use them.

## External Modules

Some modules aren’t included with the default MicroPython installation and need to be installed separately. External modules, often provided by the community or specific hardware packages, extend MicroPython’s functionality. For example, the **Modulino** library is an external module that provides tools for working with Arduino Modulinos.

To demonstrate how to use external modules, we’ll go through the steps to install the Modulino package on an Arduino board.

### Step 1: Install MicroPython on Your Board

Before we can install external modules, we need to have MicroPython running on our board. Use the [MicroPython Installer](https://labs.arduino.cc/en/labs/micropython-installer) to install it:

- Open the installer.
- Connect the board to your computer.
- Press the "Refresh" button if the board does not appear.
- Click "**Install MicroPython**" and wait for the installation to complete.

### Step 2: Install the Modulino Package

To install the Modulino package, we’ll use `mpremote`, a tool that allows us to install MicroPython packages directly onto our board from the command line.

1. **Install `mpremote`**: Make sure Python is installed on your computer, then open a terminal and type:

   ```bash
   pip install mpremote 
   ```

2. **Connect to Your Board**: Find your board’s serial port by running:

   ```bash
   mpremote connect list
   ```

   This command should return something like:

   ```bash
   /dev/cu.usbmodem101 ecda3b60a4dccb3f 2341:056b Arduino Nano ESP32
   ```

   - Copy the port, e.g., `/dev/cu.usbmodem101`.

3. **Install the Modulino Package**: Use the following command to install the Modulino package, replacing `<PORT>` with your board’s port:

   ```bash
   mpremote connect <PORT> mip install github:arduino/arduino-modulino-mpy
   ```

4. **Verify Installation**: After installation, check Arduino Labs for MicroPython. You should see a `/lib` folder with the Modulino library inside, indicating a successful installation.

   ![MicroPython Lab Files](./assets/microPythonLabsFiles.png)

## Organizing and Using Modules

With the Modulino package installed, we’ll see a `/lib` folder in Arduino Labs, where MicroPython automatically stores external modules. This directory structure is commonly used for organizing additional libraries, making it easy to import and use custom functions in our main program.

### Using an External Module

To use a function from the Modulino library, simply import it in `main.py`:

```python
from modulino import distance_sensor  # Example function

# Example usage
distance = distance_sensor.read_distance()
print("Distance:", distance)
```

This setup keeps `main.py` clean and makes it easy to incorporate external functionality without crowding the main script.

## Conclusion

MicroPython modules—whether built-in or external—allow us to keep our code organized, reduce duplication, and add powerful functionality to our projects. Some modules, like `time`, are included by default, while others, like the Modulino library, require installation.

- **Built-in Modules**: Modules like `time` and `machine` are part of MicroPython and need no installation.
- **External Modules**: Packages like Modulino must be installed separately, typically into the `/lib` folder.
- **Using Modules**: Once installed, we can import modules into our main program to extend functionality and keep our code modular.