---
featured: micropython-101
title: '1. Introduction to Arduino'
description: 'Learn about the Arduino platform'
author: 'Karl Söderby'
hero_image: "./hero-banner.png"
---

***This page is an introduction to the Arduino platform. If you are already familiar with Arduino, we recommend skipping to the next page.***

Arduino is a platform that enables students, teachers, hobbyists & professionals all over the world to build projects & applications that run on tiny computers.

The Arduino ecosystem is comprised of the hardware (a physical board with a tiny computer), software tools & services (Arduino IDE, Arduino Cloud), and the Arduino programming language, or "Arduino API".

## The Arduino Board

![The Arduino Nano ESP32.](assets/nano-esp32.png)

An Arduino development board is centered around a tiny computer that you program yourself to behave in specific ways. You can, for example, program a board to control a light, a motor, or to read the values of a temperature sensor.

The Arduino board is the connection with the physical world and can be used to control many different electronic circuits and devices. To name a few examples, an Arduino can be used to:
- Create a light show with an LED strip,
- Automatically open a door when you walk up to it,
- A robotic arm that is controlled with a joystick,
- A weather station recording data and posting it online.

## Hardware Required

This course is designed around two main components:
- [Nano ESP32](https://store.arduino.cc/products/nano-esp32) - an Arduino board with a Wi-Fi® chip and antenna. 
- [Nano Screw Terminal Adapter](https://store.arduino.cc/products/nano-screw-terminal) - a carrier with screw terminal connections.

Additionally, as we progress in the course, we introduce the option of using third party components from [Seeed](https://www.seeedstudio.com/), which uses the **Grove connector standard**. These components can easily be connected to the Nano Screw Terminal Adapter via a [grove-to-male cable](https://store.arduino.cc/products/grove-4-pin-male-to-grove-4-pin-cable-5-pcs).

![Mount the Nano ESP32 on the Nano Screw terminal.](assets/esp32-terminal.png)

### Nano ESP32

The [Nano ESP32](https://store.arduino.cc/products/nano-esp32) is the board used in this course, which is very suitable for MicroPython due to its quick processor, large flash memory and Wi-Fi® enabled chip packed into a tiny circuit board.

***You can find out more about this board in the [Nano ESP32 documentation](/hardware/nano-esp32).***

### Nano Screw Terminal

The [Nano Screw Terminal Adapter](https://store.arduino.cc/products/nano-screw-terminal) is a carrier that you insert your Nano board into. With the carrier, you can very easily connect cables and secure them tightly with a screwdriver. This makes it easy to maintain and your circuits more robust.

***You can find out more about this board in the [Nano Screw Terminal Adapter documentation](/hardware/nano-screw-terminal-adapter).***


## Microcontroller Basics

The tiny computer on the board, also known as the **microcontroller**, can be programmed and communicated with over USB. This microcontroller has very limited memory compared to the computers you are used to. For example, the board used in this course has about **30 000 times less RAM memory** than a modern computer, such as a Mac.

A microcontroller is designed to run the instructions it is programmed with, as soon as the board has power. These instructions happen very quickly, with thousands of instructions executed every second. How often they are executed can be altered in your program. You can for example pause the program for a second, and resume it again.

## Programming Basics

So how do we actually get the board to do what we want?

There are two ways of programming an Arduino board, either using the Arduino programming language (a subset of C/C++) or with MicroPython, an implementation of Python® specifically for microcontrollers. In this course, we will be using **MicroPython**. 

### Arduino Programming Language

With the **Arduino programming language**, you write your program in what we call "sketches". A sketch is a file with the `.ino` extension, that you can edit inside the Arduino IDE. When you are happy with your sketch, you need to compile this file. A compiler checks for errors, and if successful, the sketch can be uploaded to your board. Once uploaded you replace the current program on your board.

The compiler is very strict and will point out where in your code you have a problem. If you are using a function from the Arduino language called `digitalWrite()`, but you write `digitalwrite()`, the code will not compile and you will get an error.

### MicroPython

Programming an Arduino using MicroPython is a slightly different experience. In this scenario, you install a version of Python on your board permanently, and then you send instructions to it. This means you can change the code for your board and load it in real time. MicroPython also implements a file system on your board.

## Summary

Over the years Arduino has released over a hundred different development boards, each different from the other. You choose the board depending on what you want to achieve, e.g. some boards have a Wi-Fi® module allowing you to connect to the Internet, and some have onboard sensors that allow you to record sensor data.

- [Next chapter: Introduction to MicroPython](/micropython-course/course/introduction-python)