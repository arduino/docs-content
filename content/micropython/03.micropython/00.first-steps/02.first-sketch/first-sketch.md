---
title: 'My First Script'
description: 'Learn how to write a basic MicroPython script to blink an LED.'
author: 'Pedro Lima'
hero_image: "./hero-banner.png"
---

In this tutorial, we'll guide create our very first MicroPython script that will run on an Arduino board. We'll make an LED blink, a classic beginner project that introduces you to basic MicroPython programming concepts.

## Hardware & Software Needed

For this tutorial, you will need a MicroPython compatible Arduino Board:

  - [Arduino Nano 33 BLE]()
  - [Arduino Nano ESP32]()
  - [Arduino Nano RP2040 Connect]()
  - [Arduino GIGA R1 WiFi]()
  - [Arduino Portenta H7]()
  - [Arduino Nicla Vision]()

You will also need the following software installed:

  - [Arduino Lab for MicroPython](https://labs.arduino.cc/en/labs/micropython).

## Board and Editor Setup

Blinking an LED is a simple yet effective way to get started with MicroPython while still understanding how to control hardware using code.

1. Connect your Arduino board to your computer via USB.
2. Open the Arduino Lab for MicroPython application.
3. Click on the **Connect** button, and select the board from the list.

***Need help installing MicroPython on your board? Visit the [MicroPython installation guide]().***

## First Script (LED Blink)

Once your board is connected, we can start writing code! Below you will find a basic example, that will flash the built in LED on your board every second. 

1. First, open the `main.py` file on your board. We write in this file, because once saved, the code will run even if you reset the board.
   ![Open main.py file.]()

2. Copy and paste the following code into your editor:
  ```python
  import machine
  import time

  led = machine.Pin(25, machine.Pin.OUT)

  while True:
      led.value(1)
      time.sleep(1)
      led.value(0)
      time.sleep(1)
  ```

  ***Note: On some boards, the built-in LED might be on a different pin. For example, on the Arduino Nano RP2040 Connect, the built-in LED is on pin `25`. Check your board's documentation to confirm the correct pin number.***

3. Click the **Run** or **Upload** button in your editor to transfer the script to your board.

Once the script is running, the LED on your board should start blinking at one-second intervals. This means your MicroPython script has loaded successfully.

![LED blinking on your board.]()

## Programming Concepts Explained

Let's break down the key programming concepts used in this script:

### `machine` Module

The machine module is a built-in MicroPython library that provides direct access to your board's hardware components. It allows you to control and interact with the microcontroller's features, such as:

-**Pins:** Configure and control digital and analog pins.
-**Timers:** Set up timers for scheduling tasks.
-**Communication Interfaces:** Use protocols like I2C, SPI, and UART.
-**Hardware-Specific Functions:** Access features unique to your microcontroller.

In our script, we use the machine.Pin class to interact with a specific pin on the board. By creating a Pin object, we can control the voltage level of that pin, which in turn controls the LED.

### `time` Module

The time module provides functions for managing time-related tasks. It allows you to add delays, measure time intervals, and schedule events. Key functions include:

-**time.sleep(seconds):** Pauses the execution of your script for the specified number of seconds. It accepts floating-point numbers for sub-second delays.
-t**ime.ticks_ms():** Returns the number of milliseconds(ms) since the board was last reset.
-**time.ticks_us()**: Returns the number of microseconds(us) since the board was last reset.
-In our script, ``time.sleep(1)`` pauses the program for one second. This creates a delay between turning the LED on and off, controlling the blink rate.

### `while True` Loop

A `while True` loop creates an infinite loop, allowing the code inside it to run repeatedly. This is essential for tasks that need to run continuously, like blinking an LED.

### Code Breakdown

- **Import Modules**:

  ```python
  import machine
  import time
  ```

  We import the `machine` and `time` modules to access hardware functions and time delays.

- **Initialize the LED Pin**:

  ```python
  led = machine.Pin(25, machine.Pin.OUT)
  ```

  We create a `Pin` object named `led`, set to pin number `25`, and configure it as an output.

- **Infinite Loop**:

  ```python
  while True:
      led.value(1)
      time.sleep(1)
      led.value(0)
      time.sleep(1)
  ```

  Inside the loop, we:

  - Turn the LED on by setting its value to `1`.
  - Wait for 1 second.
  - Turn the LED off by setting its value to `0`.
  - Wait for another second.
  - Repeat the cycle.

## Modification: Make the LED Blink Faster

Let's modify the script to make the LED blink faster. We'll change the delay from 1 second to 0.2 seconds.

### Modified Code

```python
import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(2)
```

### Steps

1. Change the `time.sleep(1)` lines to `time.sleep(2)`.
2. Upload the modified script to your board.
3. Observe that the LED now blinks faster, turning on and off every 2 seconds.

## Conclusion

Congratulations! You've written and modified your first MicroPython script on an Arduino board. This exercise introduced you to:

- Importing modules (`machine`, `time`)
- Initializing hardware components (LED)
- Using loops (`while`)
- Controlling time delays (`time.sleep()`)

These concepts are key for a vast majoraty of the operations you will be performing when writing your own programs and are present in the industry at large.

