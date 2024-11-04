---

title: 'Modulino Knob'
description: 'Get started with using the Modulino Knob'
author: 'Hannes Siebeneicher, Sebastian Romero'
hero_image: "./hero-banner.png"

---

This article will show you how to get started with the Modulino Knob, a rotating knob with a button.

## Goals

The goals of this tutorial are:

- learn how to connect a Modulino to the Arduino Nano ESP32.
- learn how to program the Modulino Knob.

## Hardware & Software Needed

- [MicroPython Labs](https://lab-micropython.arduino.cc/)
- [Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32?queryID=undefined)
- [Modulino MicroPython Package](https://github.com/arduino/arduino-modulino-mpy)
- [Modulino Knob](https://store.arduino.cc/products/plug-and-make-kit)
- [Arduino Nano to QWIIC Connector Carrier]()

## Connect the Modulino

Before programming it, you need to first connect your Modulino Knob to your Arduino Nano ESP32. Follow the diagram below to connect your Modulino Knob and Nano ESP32.

![Circuit Diagram]()

## Code

Copy the code below and run it in Arduino MicroPython labs connected to your Arduino Nano ESP32.

```python
from modulino import ModulinoKnob
from time import sleep

knob = ModulinoKnob()
knob.value = 5 # (Optional) Set an initial value
knob.range = (-10, 10) # (Optional) Set a value range

knob.on_press = lambda: print("🔘 Pressed!")
knob.on_release = lambda: (knob.reset(), print("🔘 Released!")) 
knob.on_rotate_clockwise = lambda steps, value: print(f"🎛️ Rotated {steps} steps clockwise! Value: {value}")
knob.on_rotate_counter_clockwise = lambda steps, value: print(f"🎛️ Rotated {steps} steps counter clockwise! Value: {value}")

while True:
    if(knob.update()):
        print("👀 Knob value or state changed!")

    sleep(0.1)
````
