---

title: 'Modulino Buzzer'
description: 'Get started with using the Modulino Buzzer'
author: 'Hannes Siebeneicher, Sebastian Romero'
hero_image: "./hero-banner.png"

---

This article will show you how to get started with the Modulino Buzzer, a piezo speaker.

## Goals

The goals of this tutorial are:

- learn how to connect a Modulino to the Arduino Nano ESP32.
- learn how to program the Modulino Buzzer.

## Hardware & Software Needed

- [MicroPython Labs](https://lab-micropython.arduino.cc/)
- [Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32?queryID=undefined)
- [Modulino MicroPython Package](https://github.com/arduino/arduino-modulino-mpy)
- [Modulino Buzzer](https://store.arduino.cc/products/plug-and-make-kit)
- [Arduino Nano to QWIIC Connector Carrier]()

## Connect the Modulino

Before programming it, you need to first connect your Modulino Buzzer to your Arduino Nano ESP32. Follow the diagram below to connect your Modulino Buzzer and Nano ESP32.

![Circuit Diagram]()

## Code

Copy the code below and run it in Arduino MicroPython labs connected to your Arduino Nano ESP32.

```python
from modulino import ModulinoBuzzer
from time import sleep

buzzer = ModulinoBuzzer()

# Super Mario Bros theme intro
melody = [
    (ModulinoBuzzer.NOTES["E5"], 125),
    (ModulinoBuzzer.NOTES["REST"], 25),
    (ModulinoBuzzer.NOTES["E5"], 125),
    (ModulinoBuzzer.NOTES["REST"], 125),
    (ModulinoBuzzer.NOTES["E5"], 125),
    (ModulinoBuzzer.NOTES["REST"], 125),
    (ModulinoBuzzer.NOTES["C5"], 125),
    (ModulinoBuzzer.NOTES["E5"], 125),
    (ModulinoBuzzer.NOTES["REST"], 125),
    (ModulinoBuzzer.NOTES["G5"], 125),
    (ModulinoBuzzer.NOTES["REST"], 375),
    (ModulinoBuzzer.NOTES["G4"], 250)
]

for note, duration in melody:
    buzzer.tone(note, duration, blocking=True)

# Wait 2 seconds before playing the next melody
sleep(2)

# Police siren sound effect
def generate_siren(frequency_start, frequency_end, total_duration, steps, iterations):
    siren = []
    mid_point = steps // 2
    duration_rise = total_duration // 2
    duration_fall = total_duration // 2

    for _ in range(iterations):
        for i in range(steps):
            if i < mid_point:
                # Easing in rising part
                step_duration = duration_rise // mid_point + (duration_rise // mid_point * (mid_point - i) // mid_point)
                frequency = int(frequency_start + (frequency_end - frequency_start) * (i / mid_point))
            else:
                # Easing in falling part
                step_duration = duration_fall // mid_point + (duration_fall // mid_point * (i - mid_point) // mid_point)
                frequency = int(frequency_end - (frequency_end - frequency_start) * ((i - mid_point) / mid_point))

            siren.append((frequency, step_duration))

    return siren

# 4 seconds up and down siren, with 200 steps and 2 iterations
siren_melody = generate_siren(440, 880, 4000, 200, 2)

for note, duration in siren_melody:
    buzzer.tone(note, duration, blocking=True)
````
