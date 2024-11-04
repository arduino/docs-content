---

title: 'Modulino Movement'
description: 'Get started with using the Modulino Movement'
author: 'Hannes Siebeneicher, Sebastian Romero'
hero_image: "./hero-banner.png"

---

This article will show you how to get started with the Modulino Movement, measuring acceleration and positioning.

## Goals

The goals of this tutorial are:

- learn how to connect a Modulino to the Arduino Nano ESP32.
- learn how to program the Modulino Movement.

## Hardware & Software Needed

- [MicroPython Labs](https://lab-micropython.arduino.cc/)
- [Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32?queryID=undefined)
- [Modulino MicroPython Package](https://github.com/arduino/arduino-modulino-mpy)
- [Modulino Movement](https://store.arduino.cc/products/plug-and-make-kit)
- [Arduino Nano to QWIIC Connector Carrier]()

## Connect the Modulino

Before programming it, you need to first connect your Modulino Movement to your Arduino Nano ESP32. Follow the diagram below to connect your Modulino Movement and Nano ESP32.

![Circuit Diagram]()

## Code

Copy the code below and run it in Arduino MicroPython labs connected to your Arduino Nano ESP32.

```python
from modulino import ModulinoMovement
from time import sleep_ms

movement = ModulinoMovement()

while True:
    print("🏃 Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}".format(*movement.accelerometer))
    print("🌐 Gyroscope:     x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}".format(*movement.gyro))
    print("")
    sleep_ms(100)
````
