---

featured: micropython-101  
title: '2. Micropython Basics - Analog I/O'  
description: 'Learn the fundamentals of analog I/O with MicroPython for smooth signal interactions.'  
author: 'Pedro Lima'  
hero_image: "./hero-banner.png"  

---

Analog inputs and outputs are essential for handling a range of values rather than simple on/off states, allowing for more nuanced control over devices and inputs in your projects. In this chapter, we’ll cover how to work with analog I/O using MicroPython, focusing on how to:

- Read analog values, such as a light sensor or potentiometer.
- Generate analog outputs, like controlling LED brightness or motor speed.

Analog signals differ from digital signals in that they represent a continuous range of values. This flexibility enables more refined interactions with the physical world, making analog I/O indispensable for many types of sensors and actuators.

## Analog Inputs

To read analog values as microcontrollers work on a binary system, we typically use the `ADC` (Analog-to-Digital Converter) class. Analog inputs measure voltage levels that range continuously between two values, often 0V (LOW) and the board's operating voltage, like 3.3V or 5V.
Analog signals allow you to interact with the world more fluidly by capturing gradual changes rather than absolute states. This flexibility is ideal for applications like environmental sensing, variable speed control, and responsive lighting. 
Analog sensors output a range of voltages to reflect changes in physical conditions. By converting these values into digital numbers, your Arduino board can interpret real-world signals, such as light intensity or temperature.

## PWM - Pulse Width Modulation

In microcontrollers, **Pulse Width Modulation (PWM)** is essential for creating the appearance of analog output. True analog signals involve a continuous voltage range, but since microcontrollers primarily handle digital signals (on or off), PWM bridges the gap by rapidly switching the signal between HIGH and LOW. By adjusting the time the signal remains in the HIGH state (known as the "duty cycle"), PWM simulates varying voltage levels.

PWM is especially useful in applications where true analog output is not possible but smooth transitions are necessary. Common scenarios include:

- **LED Dimming**: PWM allows for adjusting brightness levels by controlling how long the LED is ON versus OFF within a given time frame.
- **Motor Control**: By modifying the duty cycle, PWM can control the speed of motors for robotics or other mechanical devices, as the motor responds to the average power supplied over time.
- **Audio Signals**: Some sound applications also use PWM to generate varying sound frequencies or control speaker volume.

The main advantage of PWM is that it allows you to control analog-like behavior using digital pins, adding versatility to your projects while keeping power consumption efficient.

TODO: ILLUSTRATE THIS PWM MAGIC

### Code Example: Reading a Light Sensor

**Components Needed:**

- Arduino board compatible with MicroPython
- Analog light sensor (e.g., photoresistor)
- Jumper wires

**Circuit Diagram:**

1. Connect one leg of the photoresistor to the analog input pin (e.g., `A0`) and the other leg to `GND`.
2. Optionally, add a pull-up resistor to the sensor if needed.

**MicroPython Code:**

```python
from machine import ADC
import time

# Initialize ADC for the analog pin
light_sensor = ADC(0)  # Replace '0' with the correct ADC channel for your board

while True:
    light_level = light_sensor.read_u16()  # Reads a 16-bit value (0-65535)
    print("Light level:", light_level)
    time.sleep(1)
```

**Explanation:**

- **ADC Initialization**: We initialize the `ADC` class, passing the analog channel as an argument.
- **Reading Values**: `read_u16()` reads a 16-bit integer (0-65535), where `0` represents 0V and `65535` represents the board's maximum operating voltage.
- **Loop**: The sensor reading is printed every second, showing how the value changes based on light intensity.

## Analog Outputs

Unlike analog input, analog output on microcontrollers doesn’t provide a truly continuous range of voltages. Instead, we use **Pulse Width Modulation** (PWM) to simulate varying voltage levels. PWM rapidly switches a digital output between HIGH and LOW at a specified duty cycle, creating the illusion of analog output by controlling the amount of time the signal stays HIGH.

### Code Example: Dimming an LED with PWM

PWM is commonly used for tasks such as dimming LEDs or controlling motor speeds.

**Components Needed:**

- Arduino board compatible with MicroPython
- LED
- Current-limiting resistor (e.g., 220Ω)
- Jumper wires

**Circuit Diagram:**

1. Connect the anode (+) of the LED to the PWM-capable output pin (e.g., `D5`).
2. Connect the cathode (-) through a resistor to `GND`.

**MicroPython Code:**

```python
from machine import Pin, PWM
import time

# Initialize PWM for the LED pin
led_pwm = PWM(Pin(5))  # Replace '5' with the correct pin for your board
led_pwm.freq(1000)     # Set frequency to 1 kHz

# Gradually change the LED brightness
while True:
    for duty in range(0, 65536, 1024):  # 0 to 65535 for 16-bit PWM
        led_pwm.duty_u16(duty)
        time.sleep(0.01)
    for duty in range(65535, -1, -1024):
        led_pwm.duty_u16(duty)
        time.sleep(0.01)
```

**Explanation:**

- **PWM Initialization**: We create a `PWM` object and set the frequency to 1 kHz, which works well for LEDs.
- **Duty Cycle**: `duty_u16()` takes a value between 0 and 65535. The higher the value, the longer the signal stays HIGH, making the LED brighter.
- **Loop**: The brightness gradually increases and decreases by adjusting the duty cycle in small steps, causing the LED to fade in and out.


