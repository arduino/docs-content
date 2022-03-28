---
title: Getting Started with Arduino
description: 'An introduction to hardware, software tools, and the Arduino API.'
tags: [Arduino, API]
---

The Arduino platform has since its start in 2005, grown to become one of the most recognizable brands in the space of electronics and embedded design. 

But what are the cornerstones of Arduino? What is a "board", how do I write code to it, and what are the tools needed to create my own project? The goal with this guide is to provide you with an overview to the Arduino project.

***In this guide, you will find links to articles that goes more in depth on a specific topic.***

## Overview

This guide is divided into three main sections: **hardware**, **software tools**, and **Arduino API**. The sections just below summarizes the learning outcome of this article:

### Hardware

In this section, we will dedicate some time to learn about some fundamentals in electronics, and about a basic operation of an Arduino board.

- The anatomy of an Arduino board.
- The "basic" operation of an Arduino board.
- Fundamental knowledge of microcontrollers, electronic signals, communication protocols, memory management.
- Embedded sensors.
- Creating a circuit with external sensors and actuators.
- Internet of Things (IoT) and different radio modules & wireless protocols.

### Software IDE, Tools & Services

In this section you will how to set up your development environment as well as learning about what options there are.s

- How to set up your development environment.
- Learn about the Arduino IDEs (Integrated Development Environment).
- Learn about the Arduino Cloud Service.
- Intro to the Arduino CLI (Command Line Interface).

### The Arduino API

In this section you will learn what the Arduino API is, and how to create code that can run on your Arduino board.

- What is the "Arduino API".
- How is an Arduino program (sketch) structured.
- How do I upload code to an Arduino board?
- What is a "core/platform"?
- Core specific API.
- Quick reference to the Arduino API.

## Arduino Hardware

Over the years, Arduino has released hundreds of hardware designs in many shapes and forms. 

### Anatomy of an Arduino Board

While all Arduino boards differ from each other, there are several key components that can be found on practically any Arduino. Let's take a look at the image below:

![Key components of an Arduino board.]()

- **1.** Microcontroller - this is the brain of the Arduino, and is the component that we load programs into. Think of it as a very tiny computer, designed to execute a specific number of things.
- **2.** USB port - used to connect a USB cable from your computer.
- **3.** USB to serial chip - the USB to Serial is an important component, as it helps translate data that comes from e.g. a computer to the microcontroller. This is what makes it possible to program it from your computer.
- **4.** Digital pins - pins that uses digital logic (0,1 or LOW/HIGH). Commonly used for switches and to turn on an LED.
- **5.** Analog pins - pins that can read analog values in a 10 bit resolution (0-1023).
- **6.** 5V / 3.3V pins- these pins are used to power external components.
- **7.** GND - also known as `ground`, `negative` or simply `-`, is used to complete a circuit, where the electrical level is at 0 volt.

Generally speaking, all Arduino boards have the above components, but there are of course many more than meets the eye.

### Basic Operation

Most Arduino boards are designed to have a single program running on the microcontroller. This program can be designed to perform one single action, such as blinking an LED. It can also be designed to execute a hundred different actions in a cycle. The scope varies from program to program.

The program that is loaded to the microcontroller will start execution as soon as it is powered. Every program has a function called a "loop". Inside the loop, you can for example:

- Read a sensor.
- Turn on a light.
- Check whether a condition is met.
- All of the above.

The speed of a program is incredibly fast, unless we tell it to slow down. It depends on the size of the program and how long it takes for the microcontroller to execute it, but it is generally in **microseconds(or one millionth of a second)**.  

![The basic operation of an Arduino]()

### Memory

The "standard" Arduino typically has two memories: SRAM and Flash memory. 

The SRAM (Static Random-Access Memory) is used to for example store the value of a variable (such as the state of a boolean). When powered off, this memory resets.

The Flash memory is primarily used to store the main program, or the instructions for the microcontroller. This memory is not erased when powered off so that the instructions for the microcontroller are executed as soon as the board is powered.

![Memory types on an Arduino.]()

### Circuit Basics




### Electronic Signals

![Electronic signals.]()

All communication between any electronic components are done through **electronic signals.** There are two main types of electronic signals: **analog & digital**. 

### Analog Signal

![Basics of an analog signal.]()

An analog signal is generally bound to a range. In an Arduino, that range is typically 0-5V, or 0-3.3V. 

If we for example use a potentiometer (an analog component used to change the resistance of a circuit), we can adjust this range (0-5V). In the program, this is represented in a range of 0-1023, which is a 10-bit resolution. 



### Digital Signal

![Basics of a digital signal.]()

A digital signal works a bit different, and measures only if it is in a high, or low state (0 or 1). This is the most common signal type in modern technology. 

You can easily write and read digital signals on an Arduino, and is very useful to read button states, or to turn something on or off.

Digital signals might seem very basic (just 0 or 1 right), but are actually way more advanced. For example, we can create a sequence by sending a high or low state rapidly a number of times. This is known as a **binary sequence** or a **bitstream**.

Let's take a look at two binary sequences:

```
101101
101110001110011
```

Which in decimal is:

```
45
23667
```

This is a clever way of sending large amounts of data from one point to the other, by rapidly turning ON or OFF something. This particular operation is quite complex, and this is just a basic explanation of how a digital signal works.

### Serial Communication Protocols

![Serial communication protocols.]()

There are several serial communication protocols that uses the aforementioned digital signals to send data. The most common are **UART, SPI & I²C**. The UART protocol is used to send data between a computer and Arduino board, such as uploading a new program, or reading data directly from an Arduino.

The SPI and I²C protocols are used for communication between both internal and external components. The communication is handled by something called a **serial bus**, which is attached to a specific pin on the Arduino. 

Using the I²C protocol, we can connect several sensors on the same pin, and retrieve the data accurately. A device an address that we need to specify, where we can request this device to send back data. 

### Embedded Components

An **embedded component** is a tiny component that is found on your board. As electronics are getting smaller and smaller, more and more can be fitted to smaller circuit boards.

Many new Arduino boards have sensors embedded directly, making them very compact. For example, the [Nano BLE Sense]() has 7 embedded sensors, but is only **45x18mm** (the size of a thumb). These are all connected via the I²C protocol as mentioned above, and has a unique address.

![Embedded sensors.]()

### Internet of Things (IoT)

Most modern Arduino boards now come equipped with a radio module, designed to communicate wirelessly. There are several different ones: Wi-Fi, Bluetooth, LoRa, GSM, NB-IoT and more. Each are designed to communicate using the various technologies available on the market.

The most popular and inexpensive modules are the Wi-Fi & Bluetooth modules. The Wi-Fi modules allow your board to connect to routers, and to request and send data over the Internet. In a way, it works the same as your computer when requesting various types of data over the Internet, just in a smaller scale. 

Bluetooth is used to communicate with nearby devices, and is really useful for maintaining a fast and reliable connection. For example, in real-life applications, Bluetooth is used for wireless headphones & speakers.

Similarly to serial protocols, radio modules use their own set of protocols to communicate, such as HTTP, MQTT and UPD.

![Wireless communication]().

## Arduino Software Tools

***The Arduino IDEs are available for download for free in the [Software downloads page]().***

Now that we have a bit of background on Arduino hardware, let us move on to another fundamental: the Arduino Software tools.

The Arduino IDE, as it is commonly referred to, is an **integrated development environment.** But what does that mean exactly?

In order to program your board, you need to write a program, compile that program into machine code, and finally: send over the new program to your board.

The Arduino IDE facilitates all this, from the first line of code written, to have it executed on the Arduino board's microcontroller. It is a program, or application, that you can download (or use an online version), to manage all of your code development. Back in the day, this was a complicated process, that required a good set of knowledge in electronics & computer science. Now, **anyone** can learn how to do it, with the help of the Arduino IDE.

Today, there are three Arduino IDEs available:

- Arduino IDE 1.8.x (classic)
- Arduino IDE 2.0.x (new)
- Arduino Web Editor (online)

### A Typical Workflow

To upload code to an Arduino board using the IDE, one typically does the following:

**1. Install your board** - this means installing the right "package" for your board. Without the package, you can simply not use your board. Installing is done directly in the IDE, and is a quick and easy operation.

**2. Create a new sketch** - a sketch is your main program file. Here we write a set of instructions we want to execute on the microcontroller.

**3. Compile your sketch** - the code we write is not exactly how it looks like when uploaded to our Arduino: compiling code means that we check it for errors, and convert it into a binary file (1s and 0s). If something fails, you will get this in the error console.

**4. Upload your sketch** - once the compilation is successful, the code can be uploaded to your board. In this step, we connect the board to the computer physically, and select the right serial port. 

**5. Serial Monitor (optional)** - for most Arduino projects, it is important to know what's going on on your board. The Serial Monitor tool available in all IDEs allow for data to be sent from your board to your computer. 

### Arduino IDE 1.8.x

![The classic Arduino IDE.]()

For what is now considered the "legacy" editor, the Arduino IDE 1.8.X, or "Java IDE", is the editor that was first released back when Arduino started.

***Learn more by visiting the [Arduino IDE 1 documentation]().***

### Arduino IDE 2.0.x

![The new Arduino IDE.]()

In 2021, the Arduino IDE 2.0 was released. The new IDE has the same functionality, but also supports features such as auto-completion and debugging. 

***Learn more by visiting the [Arduino IDE 2 documentation]().***

### Web Editor (Arduino Cloud)

![The Web Editor.]()

The Web Editor is an online IDE, part of the Arduino Cloud suite. Similar in function, this editor is completely web based, with online storage among other features.

***Learn more by visiting the [Web Editor documentation]().***

### Library Manager

![The Library Manager.]()

Every version of the IDE has a library manager for installing Arduino software libraries. Thousands of libraries, both official and contributed libraries, are available for direct download. Code examples for each library is made available on download.

We will go through what a library is and how to use them, further down in the [Arduino API section]() of this article.

### Arduino CLI

![The CLI (Command Line Interface).]()

The Arduino CLI is a command line tool that can be used to compile and upload code to your board. It has no visual UI, but is very useful for automation. It is designed for more advanced users.

A proper use of the CLI can speed up your development time by far, as any operation is executed much faster than in the regular IDE.

## Arduino API

***Visit the [Arduino Language Reference] to learn more about the standard Arduino API.***

The Arduino API, aka the "Arduino Programming Language", consists of several functions, variables and structures based on the C/C++ language. 

