---
title: 'Runtime'
description: 'Learn about the MicroPython runtime environment and how it handles code execution on microcontrollers.'
author: 'Pedro Lima'
tags: [MicroPython, Modules]
---

MicroPython is a lean and efficient implementation of Python designed to run on microcontrollers and embedded systems. One of the key concepts to understand when working with MicroPython is its **runtime environment**—how it handles code execution, manages resources, and interacts with hardware.

We’ll demystify the MicroPython runtime, explore how it differs from other environments like standard Python, and discuss best practices for working within its constraints.

## What is a Runtime Environment?

A **runtime environment** is the infrastructure that allows code to execute on a given platform. It provides the necessary resources, such as memory management, libraries, and system interfaces, for the code to run properly. 

For MicroPython, the runtime is a lightweight version of the Python runtime, optimized to work with the limited resources of microcontrollers. This means it has to manage memory efficiently, provide quick access to hardware components, and interpret Python code in real-time.

### MicroPython's Runtime

MicroPython's runtime environment consists of several key components:

1. **Interpreter**: MicroPython interprets Python code line by line. This is different from compiled languages (like C or C++ on traditional Arduino) that need to be fully compiled before running. MicroPython’s interpreter is built to be efficient, ensuring quick code execution even on constrained hardware.

2. **Memory Management**: Since microcontrollers have limited RAM, the MicroPython runtime includes a garbage collector to manage memory automatically. The [garbage collector](https://docs.micropython.org/en/latest/library/gc.html) frees up unused memory to prevent the system from running out of resources.

3. **Built-in Libraries and Modules**: MicroPython comes with a set of built-in libraries that provide access to hardware interfaces like pins, I2C, SPI, and UART. These libraries are tightly integrated into the runtime to allow seamless interaction with the hardware.

4. **File System**: The runtime includes a file system, typically mounted on the microcontroller’s flash storage. This allows MicroPython to load and execute scripts, save configuration files, or store data persistently.

### MicroPython Runtime Features

1. **REPL (Read-Eval-Print Loop)**: One of the standout features of MicroPython's runtime is the REPL. The REPL is an interactive shell where we can type and execute Python code line by line, get immediate feedback, and test ideas quickly. It’s especially useful for debugging and learning how the hardware responds to different commands.

2. **Boot and Main Scripts**: When the microcontroller starts up, the MicroPython runtime automatically looks for two scripts:
   
   - **`boot.py`**: This script is executed first and is typically used for system configuration, such as setting up Wi-Fi or initializing hardware settings.
   - **`main.py`**: After `boot.py` runs, `main.py` is executed. This is where we typically put our main application logic.

3. **Concurrency with `uasyncio`**: MicroPython provides support for asynchronous programming using the `uasyncio` module. This allows us to handle multiple tasks concurrently, such as reading a sensor while controlling an LED, without blocking the main program.

### MicroPython vs Python

While MicroPython aims to be as compatible as possible with standard Python, there are some important differences due to the limited resources available on microcontrollers:

- **Memory Constraints**: Standard Python runs on desktops or servers with abundant RAM, but MicroPython runs on devices with as little as 16KB to 512KB of RAM. The runtime is optimized to be efficient, but we must be mindful of memory usage.
- **Limited Libraries**: Many of Python’s standard libraries are unavailable in MicroPython because they are too large or not relevant for embedded systems. However, MicroPython provides specialized libraries for hardware interaction.
- **Performance**: MicroPython is generally slower than compiled languages, but it’s fast enough for most embedded applications thanks to its lightweight runtime and efficient interpreter.

## Code Execution Works in MicroPython

When we upload a MicroPython script to our microcontroller, the runtime handles code execution as follows:

1. **Interpreter Reads Code**: The interpreter reads each line of Python code and executes it immediately. If there are syntax errors, they are reported right away.
2. **Memory Allocation**: Variables, objects, and data structures are allocated in the microcontroller’s RAM. The garbage collector runs periodically to free up memory that’s no longer needed.
3. **Hardware Interaction**: The runtime communicates with the microcontroller’s hardware through built-in libraries. For example, we can control GPIO pins, read sensor data, or send data over I2C using simple Python commands.
4. **Error Handling**: MicroPython includes mechanisms for error handling and debugging. If the script encounters an error, the runtime will stop execution and display an error message in the REPL or console.

## Best Practices
1. **Manage Memory Wisely**: Be mindful of memory usage, especially when working with large data structures or performing frequent allocations. Use the garbage collector [(`gc`)](https://docs.micropython.org/en/latest/library/gc.html) if you need to manually free up memory.
2. **Use REPL for Testing**: Take advantage of the REPL to experiment and debug code interactively. This can save time and help you understand how your code interacts with the hardware.
3. **Optimize Code for Speed and Efficiency**: Use efficient data structures and algorithms to keep your code fast and responsive. Avoid blocking operations when possible, and consider using `uasyncio` for concurrency.
4. **Organize Code with Modules**: Break your code into reusable modules to keep `main.py` clean and organized. This can make your project easier to maintain and extend.

## Conclusion

The MicroPython runtime is a powerful yet lightweight environment that brings the flexibility of Python to embedded systems. By understanding how the runtime handles code execution, memory management, and hardware interaction, we can write efficient and effective MicroPython programs.