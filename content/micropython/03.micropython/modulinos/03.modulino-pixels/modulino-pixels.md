---

title: 'Modulino Pixels'
description: 'Get started with using the Modulino Pixels'
author: 'Hannes Siebeneicher, Sebastian Romero'
hero_image: "./hero-banner.png"

---

This article will show you how to get started with the Modulino Pixels and control RGB LEDs.

## Goals

The goals of this tutorial are:

- learn how to connect a Modulino to the Arduino Nano ESP32.
- learn how to program the Modulino Pixels.

## Hardware & Software Needed

- [MicroPython Labs](https://lab-micropython.arduino.cc/)
- [Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32?queryID=undefined)
- [Modulino MicroPython Package](https://github.com/arduino/arduino-modulino-mpy)
- [Modulino Pixels](https://store.arduino.cc/products/plug-and-make-kit)
- [Arduino Nano to QWIIC Connector Carrier]()

## Connect the Modulino

Before programming it, you need to first connect your Modulino Pixels to your Arduino Nano ESP32. Follow the diagram below to connect your Modulino Pixels and Nano ESP32.

![Circuit Diagram]()

## Code

Copy the code below and run it in Arduino MicroPython labs connected to your Arduino Nano ESP32.

```python
from modulino import ModulinoPixels, ModulinoColor
from time import sleep

pixels = ModulinoPixels()

for index in range(0, 8):
    color_wheel_colors = [
        (255, 0, 0),
        (255, 85, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 255, 255),
        (0, 0, 255),
        (255, 0, 255),
        (255, 0, 0)
    ]
    pixels.set_rgb(index, *color_wheel_colors[index], 100)
pixels.show()
sleep(1)

pixels.set_all_rgb(255, 0, 0, 100)
pixels.show()
sleep(1)

pixels.set_all_color(ModulinoColor.GREEN, 100)
pixels.show()
sleep(1)

pixels.set_all_color(ModulinoColor.BLUE, 100)
pixels.show()
sleep(1)


# Night Rider animation

for j in range(0, 3):
    for i in range(0, 8):
        pixels.clear_all()
        pixels.set_rgb(i, 255, 0, 0, 100)
        pixels.show()
        sleep(0.05)

    for i in range(7, -1, -1):
        pixels.clear_all()
        pixels.set_rgb(i, 255, 0, 0, 100)
        pixels.show()
        sleep(0.05)

# Turn off all LEDs
pixels.clear_all()    
pixels.show()
````
