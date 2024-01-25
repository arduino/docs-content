---
title: 'Power Consumption on Arduino Boards'
description: 'Learn about measuring power consumption on an Arduino board.'
tags: [Power Consumption]
author: 'Karl Söderby'
---

All electronic devices, including Arduino boards, consume power. The power consumption is measured in ampere hours (Ah), and with low voltage devices, it is typically measured in mAh.

When creating projects that run on a battery or is power-constrained, taking power consumption into account can be critical. It will among other things help you decide which kind of battery you need to use.

In this article, we will demonstrate how you can perform power consumption tests, using a **power profiler**. A power profiler is used to measure consumption over a specific time period, where we record several thousands samples. You will find instructions for both the hardware setup, the software setup, and the actual power consumption tests in this article.

***Note that in this article, third party products are being used.***

## Hardware & Software Needed

For power consumption tests in this article, we used the following hardware & software. Note that there are many alternatives on the market.

- [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-Desktop/Download)
- [Power Profiler Kit II](https://www.nordicsemi.com/Products/Development-hardware/Power-Profiler-Kit-2)
- [Arduino board (link to store)](https://store.arduino.cc/)
- Jumper wires

## Measuring Power Consumption

Power consumption measurements are done by connecting a power profiler between your Arduino and computer. The power profiler is connected to the computer via USB, and then to the Arduino via jumper wires. For power consumption measurements, we simply use two wires: **power** and **ground**. The power cable is connected to your Arduino's power pins, and ground goes to one of the GND pins on the board.

When it is connected, the power profiler can measure the power consumption of your board with a high accuracy. Any power that your board consumes can now be detected, and with a software tool (such as the [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-Desktop/Download)), we can record power consumption over time.

So what is it that we are measuring? In very simple terms, all electronic devices draw current, whether it is small or big. A small LED can for example draw 10 mA (0.01 A), while a servo motor can draw up towards 1000 mA (1 A). If you have an LED on for an hour that draws 10 mA, we can express it as **mAh**, which means **milli-ampers consumed per hour**.

### Power Consumption Example

To provide a practical example, let's take the [Nano ESP32](). We ran a simple sketch on the board, which continuously runs the `analogRead()` function. The test ran for 60 seconds, and recorded 100'000 samples. The result was an average of **31.05 mA**. 

Now, if we wanted to power this application using a battery, we know that the power consumption is 31.05 mA. If we intend to run the application with a fully re-charged 300 mAh battery, we would be able to run for approximately 9 hours, as we would be consuming **31.05 * 9 = 279.45**, according to the formula below:

- **milli-ampere hours (mAh) = power consumption * hours**

With that information, we can make an educated guess of what type of battery we should get. For example, a battery with more capacity, let's say 600 mAh, would in theory last for twice the period.

***Note that there are other factors at play, such as the battery's discharge rate and the general quality of the battery. The above formulas and measurements are to be considered guidelines.***


## Software Setup

The software setup involves two steps: **upload a sketch** and **insatlling nRF Connect for Desktop**. 

### Upload Sketch

This step is rather straightforward. Upload the sketch that you want to measure the power consumption of. Below is a minimal sketch that reads an analog pin continuously. 

```arduino

```

### Install Desktop App

To measure the power consumption, we are going to use the [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-Desktop/Download) tool. This is a program that you install on your computer.

## Hardware Setup

The profiler we used is the [Power Profiler Kit II](https://www.nordicsemi.com/Products/Development-hardware/Power-Profiler-Kit-2).

1. First disconnect the USB cable from your board. You will be powering the board directly from the power profiler, so there's no need for the USB cable at this point.
2. Use the provided cable from the kit, and connect it to your board's GND and power pin, following the illustration below:

![Connect the power profiler to the board.]()

***Important note! In the software setup you enable the "Power Output" of the power profiler. Make sure that the voltage (3.3 V or 5 V) matches the voltage on the power pin of the board. Applying 5 V to a 3.3 V pin will damage your board.***

## Power Consumption Test

With the hardware and software set up, let's take a look at how to record the power consumption of your device.

