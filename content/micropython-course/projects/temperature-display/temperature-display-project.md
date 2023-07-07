---
author: 'Benjamin Dannegård'
hero_image: "./hero-banner.png"
featured: micropython-101-projects
title: 'Temperature Display'
description: 'Use a temperature sensor together with a NeoPixel stick, giving you visual feedback on the current temperature.'
---

This project will take the temperature reading from a DHT11 sensor and change the color of the LEDs on the NeoPixel accordingly.

## Required Hardware

You will need the following to build this project:

- [Nano ESP32](https://store.arduino.cc/products/nano-esp32)
- [Nano Screw Terminal Adapter](https://store.arduino.cc/products/nano-screw-terminal)
- [NeoPixel light](https://www.seeedstudio.com/Grove-RGB-LED-Stick-10-WS2813-Mini.html)
- [DHT11 temperature sensor](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT11.html)
- [Grove to male cables](https://store.arduino.cc/products/grove-4-pin-male-to-grove-4-pin-cable-5-pcs)

## Circuit

Assemble the components according to the circuit diagram below:

![Circuit for the temperature display](assets/temperature-light.png)

## Code

Feel free to change the temperature thresholds to fit your environment more accurately, the script will print the temperature reading in the terminal so you can easily determine what thresholds to use. Then upload this code to your board.

```python
from machine import Pin
from time import sleep
import neopixel
import dht

PIXEL_NUMBER = 10
np = neopixel.NeoPixel(Pin(10), PIXEL_NUMBER) # Pin D7

SENSOR_PIN = 5 # Pin D2
TEMP_SENSOR = dht.DHT11(Pin(SENSOR_PIN))
sleep(1)

red = (255, 0, 0) # set to red
green = (0, 128, 0) # set to green
blue = (0, 0, 64)  # set to blue

def hotLED():
    for i in range(0, PIXEL_NUMBER):
        np[i] = red
        np.write()

        
def coldLED():
    for i in range(0, PIXEL_NUMBER):
        np[i] = blue
        np.write()
        
def neutralLED():
    for i in range(0, PIXEL_NUMBER):
        np[i] = green
        np.write()

while(1):
    TEMP_SENSOR.measure()
    print(TEMP_SENSOR.temperature())
    temp = TEMP_SENSOR.temperature()

    if(temp >= 28): #Threshold for when the LEDs indicate a hot temperature
        hotLED()
        
    if(temp <= 22): #Threshold for when the LEDs indicate a cold temperature
        coldLED()
        
    if(temp > 22 and temp < 28): #Threshold for when the LEDs indicate a neutral temperature
        neutralLED()

    sleep(1)
```