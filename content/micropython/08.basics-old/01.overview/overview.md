---
title: Overview
description: An introduction to Arduino and MicroPython
author: Francesca Sanfilippo
micropython_type: basics
---

MicroPython is an implementation of the Python programming language, and includes some of the standard Python libraries. It is designed to run on microcontrollers with constrained environments.
 
In this sequence of guides, you will among other things, learn how to:
- Install MicroPython on your Arduino board,
- Install an editor with support for MicroPython,
- How to make basic scripts that can for example blink an LED, read an analog pin and print things to the terminal (REPL).

You do not need any prior knowledge in either programming with Arduino or MicroPython, but it is recommended to know the basics of Python.

What you need to do it is have a Compatible Board and a Code Editor. You can choose between two alternatives:
- **Arduino Lab for MicroPython:** an experimental editor from Arduino, designed for simpler projects.
- **OpenMV:** an editor for  more complex projects, such as computer vision.

## Python vs C/C++.

If you are experienced with Arduino programming in C and C++ a lot of the presented topics will look familiar to you.
There's a big difference between how we program an Arduino board with the Arduino IDE, using the Arduino programming language (based on C++), and how we program it using MicroPython. 
- The “Arduino way” requires compiling the sketch before uploading it to your board. The previous code running is replaced by the new one.
- The “MicroPython way” does not require compiling, as you will have MicroPython installed on the actual board. Code is instead run through an interpreter, line by line.

## Python vs MicroPython

MicroPython was created to work under constrained conditions, like a small environment. The main difference between Python and MicroPython is that MicroPython does not have the full standard Python language, it is only a subset of it.