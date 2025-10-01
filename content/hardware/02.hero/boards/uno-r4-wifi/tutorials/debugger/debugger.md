---
title: 'Debugging the Arduino UNO R4 WiFi'
description: 'Learn how to debug the UNO R4 WiFi with the Arduino IDE.'
tags:
  - Debugger
  - IDE
author: 'Hannes Siebeneicher'
---

Debugging is the process of identifying and fixing errors in your code. It’s a vital skill for anyone writing code especially when dealing with microcontrollers like those on your Arduino.

In this article, we will focus on using the Arduino IDE's built-in debugger, which can be used to debug the UNO R4 WiFi over USB. We will go through how to:
- Enable debugging mode in the Arduino IDE
- Create breakpoints for where we want to inspect the code
- Monitor the value of a variable at a specific point in the program 

Note that you **do not** need an external debugger to follow this tutorial.

***To learn more about general debugging principles, you can read up on the topic [here](/learn/microcontrollers/debugging).***

## Goals

The goals of this tutorial are:

- learn about the basics of debugging.
- learn how to set up the Arduino IDE to debug an Arduino sketch.

## Hardware & Software Needed

- [Arduino IDE](https://www.arduino.cc/en/main/software)
- [Arduino UNO R4 WiFi](https://store.arduino.cc/uno-r4-wifi)
- [UNO R4 Board Package](/tutorials/uno-r4-minima/minima-getting-started)

## Debugging

Debugging your Arduino project allows you to dive deep into your code and troubleshoot as well as analyze the code execution. You can gain full access to the microcontroller's internal registers, memory, and variables. This is especially helpful when working on more complex projects where understanding the code execution flow is crucial. With the Arduino IDE you can step through the code line by line, allowing you to analyze why your code might break at a specific point.

## Connection

The only thing you need to do is to connect your UNO R4 WiFi to your computer using a USB-Cable.

## Software 

### Setting up the Arduino IDE

First, if you haven't done it yet, install the [Arduino IDE](https://www.arduino.cc/en/software). It's a good idea to verify that everything is working as it should by uploading the Blink example.

![Blink Example](./assets/blink_example.png)

## Set Correct Programmer

To access and debug the Arduino's MCU it's important that we set the correct programmer. Select **Tools** > **Programmer** > **ARM CMSIS-DAP compatible**.

![Set Programmer](./assets/set_programmer.png)

## Setting Breakpoints

A breakpoint is an intentional stopping or pausing place at a specific point in the code. You can add them by clicking the sidebar next to your sketch, and you should see a red dot appear. You have now set a breakpoint.

![Setting a breakpoint](./assets/set_breakpoints.png)

## Start Debugging

Now you are ready to start debugging. Press "**Start Debugging**" next to the "Upload button" or click the icon in the left sidebar.

![Start Debugging](./assets/start_debugger.png)

You will see how your code is executed and **stopped** at the line you set the breakpoint. You can set as many breakpoints as you want, depending on where you want to stop your code.

To resume the code press the "**Continue**" in the top left corner and you will see how the code runs until the it reaches the next breakpoint.

![Resume Code](./assets/resume_code.png)