---

title: 'Modulino Buttons'
description: 'Get started with using the Modulino Buttons'
author: 'Hannes Siebeneicher, Sebastian Romero'
hero_image: "./hero-banner.png"

---

This article will show you how to get started with the Modulino Buttons, a three-button Modulino.

## Goals

The goals of this tutorial are:

- learn how to connect a Modulino to the Arduino Nano ESP32.
- learn how to program the Modulino Buttons.

## Hardware & Software Needed

- [MicroPython Labs](https://lab-micropython.arduino.cc/)
- [Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32?queryID=undefined)
- [Modulino MicroPython Package](https://github.com/arduino/arduino-modulino-mpy)
- [Modulino Buttons](https://store.arduino.cc/products/plug-and-make-kit)
- [Arduino Nano to QWIIC Connector Carrier]()

## Connect the Modulino

Before programming it, you need to first connect your Modulino Buttons to your Arduino Nano ESP32. Follow the diagram below to connect your Modulino Buttons and Nano ESP32.

![Circuit Diagram]()

## Code

Copy the code below and run it in Arduino MicroPython labs connected to your Arduino Nano ESP32.

```python
from modulino import ModulinoButtons

buttons = ModulinoButtons()

buttons.on_button_a_press = lambda : print("Button A pressed")
buttons.on_button_a_long_press = lambda : print("Button A long press")
buttons.on_button_a_release = lambda : print("Button A released")

buttons.on_button_b_press = lambda : print("Button B pressed")
buttons.on_button_b_long_press = lambda : print("Button B long press")
buttons.on_button_b_release = lambda : print("Button B released")

buttons.on_button_c_press = lambda : print("Button C pressed")
buttons.on_button_c_long_press = lambda : print("Button C long press")
buttons.on_button_c_release = lambda : print("Button C released")


while True:
    buttons_state_changed = buttons.update()
    
    if(buttons_state_changed):    
      led_a_status = buttons.is_pressed(0) # Turn LED A on if button A is pressed
      led_b_status = buttons.is_pressed(1) # Turn LED B on if button B is pressed
      led_c_status = buttons.is_pressed(2) # Turn LED C on if button C is pressed
      buttons.set_led_status(led_a_status, led_b_status, led_c_status)
````
