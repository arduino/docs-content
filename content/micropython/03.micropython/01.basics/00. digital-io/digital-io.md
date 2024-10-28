---

featured: micropython-101
title: '2. Micropython Basics - Digital I/O'
description: 'Learn the basics for loops on MicroPython.'
author: 'Pedro Lima'
hero_image: "./hero-banner.png"

---

Digital pins are fundamental for interacting with the physical world using your Arduino board. In this chapter, we'll explore how to use digital pins in MicroPython to:

- Control outputs, such as turning an LED on and off.
- Read inputs, like detecting the state of a button.

Digital signals have two distinct values:

- **HIGH (1)**: Represents a voltage level close to the board's operating voltage (e.g., 3.3V or 5V).
- **LOW (0)**: Represents a voltage level close to 0V (ground).

Although they can only represent two states, digital signals are highly useful. Being binary in nature, they directly interface with microcontrollers and processors, making them ideal for tasks requiring fast, on/off communication, such as reading sensors or controlling simple outputs. Their simplicity also gives them a natural resilience to electrical noise, as noise only disrupts digital signals when it is strong enough to cross the threshold between HIGH and LOW states. This makes them reliable for clear, consistent communication in various environments.

## Digital Outputs

To control digital outputs in MicroPython, we use the `Pin` class from the `machine` module. Setting a pin as an output allows you to control devices like LEDs, relays, or other actuators.

### Code Example: Blinking an LED

Let's create the classic "Blink" example, where we turn an LED on and off at regular intervals.

**Components Needed:**

- Arduino board compatible with MicroPython
- LED (optional if using the onboard LED)
- Current-limiting resistor (e.g., 220Ω) if using an external LED
- Jumper wires

**Circuit Diagram:**

- **Onboard LED**: Many Arduino boards have an onboard LED connected to a specific pin.
- **External LED**:
  - Connect the anode (+) of the LED to a digital output pin.
  - Connect the cathode (-) of the LED through a resistor to `GND`.

**MicroPython Code:**

```python
from machine import Pin
import time

# Initialize the LED pin
# Uncomment the line that matches your board
led = Pin(25, Pin.OUT)     # For Arduino Nano RP2040 Connect
# led = Pin(13, Pin.OUT)   # For Arduino Nano 33 BLE / Sense (built-in LED)
# led = Pin(2, Pin.OUT)    # For Arduino Portenta H7

while True:
    led.value(1)  # Turn LED on
    time.sleep(1)  # Wait for 1 second
    led.value(0)  # Turn LED off
    time.sleep(1)  # Wait for 1 second
```

**Explanation:**

- **Import Modules**: We import `Pin` from `machine` and `time` for delays.
- **Initialize LED Pin**: Create a `Pin` object, setting the pin number and direction (`Pin.OUT`).
- **Main Loop**:
  - `led.value(1)`: Sets the pin to HIGH, turning the LED on.
  - `time.sleep(1)`: Pauses the program for 1 second.
  - `led.value(0)`: Sets the pin to LOW, turning the LED off.
  - The loop repeats indefinitely, causing the LED to blink.



## Digital Inputs

Reading digital inputs allows your program to respond to external events, like button presses or sensor signals. In MicroPython, we use the `Pin` class to set up pins as inputs, and we can specify pull modes to stabilize the input readings.

### Understanding Pull Modes

When a digital input pin is not connected to a definite HIGH or LOW voltage, it is said to be "floating," which can result in unreliable readings due to electrical noise. To prevent this, we use internal pull-up or pull-down resistors, activated by specifying the pull mode in the `Pin` constructor.

- **Pull-Up Mode (`Pin.PULL_UP`)**: Connects the input pin internally to a HIGH voltage level, ensuring the pin reads HIGH when not connected to anything else.
- **Pull-Down Mode (`Pin.PULL_DOWN`)**: Connects the input pin internally to GND, ensuring the pin reads LOW when not connected to anything else.

These internal resistors are built into the microcontroller and can be enabled in your code, eliminating the need for external resistors.

![We can create a image here to explain that]()



### Pull-Up Mode

In pull-up mode, the input pin is internally connected to a HIGH voltage level. When the input device (like a button) is activated and connects the pin to GND, the pin reads LOW (`0`).

**Circuit Diagram for Pull-Up Mode:**

- Connect one side of the button to **GND**.
- Connect the other side to a digital input pin.

![Demo]() TODO: Show Schematic

### Pull-Down Mode

In pull-down mode, the input pin is internally connected to GND. When the input device is activated and connects the pin to a HIGH voltage level (e.g., 3.3V), the pin reads HIGH (`1`).

**Circuit Diagram for Pull-Down Mode:**

- Connect one side of the button to **3.3V** (or **5V**, depending on your board's logic level).
- Connect the other side to a digital input pin.

![Demo]() TODO: Show Schematic


### Code Example: Reading a Button with Pull-Up Mode

**Components Needed:**

- Arduino board compatible with MicroPython
- Push-button switch
- Jumper wires

**MicroPython Code:**

```python
from machine import Pin
import time

# Initialize the button pin with internal pull-up resistor
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Replace 14 with your input pin number

while True:
    button_state = button.value()
    if button_state == 0:
        print("Button Pressed")
    else:
        print("Button Released")
    time.sleep(0.1)
```

**Explanation:**

- **Initialize Button Pin**:
  - We set up the pin as an input with a pull-up mode (`Pin.PULL_UP`), enabling the internal pull-up resistor.
  - This means the pin reads HIGH (`1`) when the button is not pressed.
- **Reading the Pin**:
  - When the button is **not pressed**, the pin is pulled HIGH internally (`button.value()` returns `1`).
  - When the button is **pressed**, it connects the pin to GND, making `button.value()` return `0`.
- **Main Loop**:
  - Reads the button state and prints a message accordingly.
  - A short delay helps debounce the button.



### Code Example: Reading a Button with Pull-Down Mode

**Components Needed:**

- Arduino board compatible with MicroPython
- Push-button switch
- Jumper wires

**MicroPython Code:**

```python
from machine import Pin
import time

# Initialize the button pin with internal pull-down resistor
button = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Replace 14 with your input pin number

while True:
    button_state = button.value()
    if button_state == 1:
        print("Button Pressed")
    else:
        print("Button Released")
    time.sleep(0.1)
```

**Explanation:**

- **Initialize Button Pin**:
  - We set up the pin as an input with a pull-down mode (`Pin.PULL_DOWN`), enabling the internal pull-down resistor.
  - This means the pin reads LOW (`0`) when the button is not pressed.
- **Reading the Pin**:
  - When the button is **not pressed**, the pin is pulled LOW internally (`button.value()` returns `0`).
  - When the button is **pressed**, it connects the pin to HIGH voltage, making `button.value()` return `1`.
- **Main Loop**:
  - Reads the button state and prints a message accordingly.
  - A short delay helps debounce the button.

