---

title: 'Modulino Distance'
description: 'Get started with using the Modulino Distance'
author: 'Hannes Siebeneicher, Sebastian Romero'
hero_image: "./hero-banner.png"

---

This article will show you how to get started with the Modulino Distance and measure the distance to an object.

## Goals

The goals of this tutorial are:

- learn how to connect a Modulino to the Arduino Nano ESP32.
- learn how to program the Modulino Distance.

## Hardware & Software Needed

- [MicroPython Labs](https://lab-micropython.arduino.cc/)
- [Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32?queryID=undefined)
- [Modulino MicroPython Package](https://github.com/arduino/arduino-modulino-mpy)
- [Modulino Distance](https://store.arduino.cc/products/plug-and-make-kit)
- [Arduino Nano to QWIIC Connector Carrier]()

## Connect the Modulino

Before programming it, you need to first connect your Modulino Distance to your Arduino Nano ESP32. Follow the diagram below to connect your Modulino Distance and Nano ESP32.

![Circuit Diagram]()

## Code

Copy the code below and run it in Arduino MicroPython labs connected to your Arduino Nano ESP32.

```python
from modulino import ModulinoDistance
from time import sleep_ms

distance = ModulinoDistance()

while True:
    print(f"📏 Distance: {distance.distance} cm")
    sleep_ms(50)
````
