---
title: 'Portenta C33'
description: 'Learn how to use specific features on the Portenta C33 using MicroPython'  
author: 'Karl Söderby'  
---

In this guide, you will information related only to the [Arduino® Portenta C33](https://store.arduino.cc/products/portenta-c33) and MicroPython.

## Pinout Mapping

The Portenta C33 has two ways its pins are physically available: through its MKR-styled connectors and its High-Density connectors. Most pins are referred to via their port name or function. In the image below, the Portenta C33 MKR-styled connectors pinout is shown. 

![Portenta C33 MKR-styled connectors pinout](assets/portenta33_MKR_pinout.png)

The MKR-styled connectors pinout is mapped in MicroPython as follows:

| **Arduino Pin Mapping** | **MicroPython Pin Mapping** |
|:-----------------------:|:---------------------------:|
|       `P006`/`A0`       |            `P006`           |
|       `P005`/`A1`       |            `P005`           |
|       `P004`/`A2`       |            `P004`           |
|       `P002`/`A3`       |            `P002`           |
|       `P001`/`A4`       |            `P001`           |
|       `P015`/`A5`       |            `P015`           |
|       `P014`/`A6`       |            `P014`           |
|       `P105`/`D0`       |            `P105`           |
|       `P106`/`D1`       |            `P106`           |
|       `P111`/`D2`       |            `P111`           |
|       `P303`/`D3`       |            `P303`           |
|       `P401`/`D4`       |            `P401`           |
|       `P210`/`D5`       |            `P210`           |
|          `P602`         |            `P602`           |
|          `P110`         |            `P110`           |
|          `P408`         |            `P408`           |
|          `P407`         |            `P407`           |
|          `P315`         |            `P315`           |
|          `P204`         |            `P204`           |
|          `P900`         |            `P900`           |
|          `P402`         |            `P402`           |
|          `P601`         |            `P601`           |

The complete MicroPython pinout is available [here](https://github.com/micropython/micropython/blob/master/ports/renesas-ra/boards/ARDUINO_PORTENTA_C33/pins.csv).

## Input/Output Pins

The `Pin` class in the `machine` module is essential for controlling Input/Output (I/O) pins of the Portenta C33 board.  These pins are crucial for a wide range of applications, including reading sensor data, controlling actuators, and interfacing with other hardware components.

### Pin Initialization

To begin using an I/O pin of the Portenta C33 board with MicroPython, you need to initialize it using the `Pin` class from the `machine` module. This involves specifying the pin identifier and its mode (input, output, etc.).

```python
from machine import Pin

# Initializing pin P107 as an output
p107 = Pin('P107', Pin.OUT)
```

### Configuring Pin Modes

You can configure a pin as an input or output. For input pins, it's often useful to activate an internal pull-up or pull-down resistor. This helps to stabilize the input signal, especially in cases where the pin is reading a mechanical switch or a button.

```python
# Configuring pin P105 as an input with its pull-up resistor enabled
p105 = Pin('P105', Pin.IN, Pin.PULL_UP)
```

### Reading from and Writing to Pins

To read a digital value from a pin, use the `.value()` method without any arguments. This is particularly useful for input pins. Conversely, to write a digital value, use the `.value()` method with an argument. Passing `1` sets the pin to `HIGH`, while `0` sets it to `LOW`. This is applicable to output pins.

```python
# Reading from P105
pin_value = p105.value()

# Writing to P107
p107.value(1)  # Set p2 to high
```

### Advanced Pin Configuration

The Pin class allows dynamic reconfiguration of pins and setting up interrupt callbacks. This feature is essential for creating responsive and interactive applications.

```python
# Reconfiguring P105 as an input with a pull-down resistor
p105.init(Pin.IN, Pin.PULL_DOWN)

# Setting up an interrupt on P105
p105.irq(lambda p: print("- IRQ triggered!", p))
```

### Practical Example

In this example, we will configure one pin as an input to read the state of a button and another pin as an output to control an LED. The LED will turn on when the button is pressed and off when it's released.

```python
from machine import Pin
import time

# Configure pin P107 as an output (for the LED)
led = Pin('P107', Pin.OUT_PP)

# Configure pin P105 as input with pull-up resistor enabled (for the button)
button = Pin('P105', Pin.IN, Pin.PULL_UP)

while True:
    # Read the state of the button
    button_state = button.value()  
    if button_state == 0:
        # Turn on LED if button is pressed (button_state is LOW)
        led.value(1)  
    else:
        # Turn off LED if button is not pressed (button_state is HIGH)
        led.value(0) 

    # Short delay to debounce the button 
    time.sleep(0.1)
```

This practical example demonstrates controlling an LED based on a button's state. The LED, connected to pin `P107` (configured as an output), is turned on or off depending on the button's input read from pin `P105` (set as an input with a pull-up resistor). The main loop continually checks the button's state; pressing the button fixes the LED on while releasing it turns the LED off. A brief delay is included for debouncing, ensuring stable operation without false triggers from the button.

## Analog to Digital Converter

The `ADC` class in MicroPython provides an interface for the Analog-to-Digital (ADC) converter of the Portenta C33 board, enabling the measurement of continuous voltages and their conversion into discrete digital values. This functionality is crucial for applications that, for example, require reading from analog sensors. The `ADC` class represents a single endpoint for sampling voltage from an analog pin and converting it to a digital value. 

The available ADC pins of the Portenta C33 board in MicroPython are the following:

| **Available ADC Pins** |
|:----------------------:|
|         `P006`         |
|         `P005`         |
|         `P004`         |
|         `P002`         |
|         `P001`         |
|         `P015`         |
|         `P014`         |
|         `P000`         |

### Initializing the ADC

First, to use an ADC of the Portenta C33 board, create an ADC object associated with a specific pin. This pin will be used to read analog values.

```python
from machine import ADC

# Create an ADC object on a specific pin
adc = ADC(pin)
```

### Reading Analog Values

You can read analog values as raw values using the `read_u16()` method. This method returns a raw integer from 0-65535, representing the analog reading.

```python
# Reading a raw analog value
val = adc.read_u16()
```

### Practical Example

This example demonstrates the use of the `ADC` class to read values from a potentiometer on the Portenta C33 board. First, connect your potentiometer to the Portenta C33 board. One outer pin goes to `GND`, the other to `3V3`, and the middle pin to an analog-capable I/O pin, such as `P006`. This setup creates a variable voltage divider, with the voltage at the center pin changing as you adjust the potentiometer.

```python
from machine import ADC, Pin
import time

# Initialize the ADC on the potentiometer-connected pin
pot_pin = Pin('P006')
pot_adc = ADC(pot_pin)

while True:
    # Read the raw analog value
    raw_value = pot_adc.read_u16()
    print("- Potentiometer raw value:", raw_value)

    # Delay for readability
    time.sleep(0.1)
```
The example starts by importing the necessary modules and setting up the ADC on a pin connected to a potentiometer (`P006`). The ADC object (`pot_adc`) is used to interface with the potentiometer. Inside the loop, the analog value from the potentiometer is continuously read using the `read_u16()` method that provides a raw integer value scaled between `0` and `65535`, reflecting the potentiometer's position. The analog value value is printed to the console, and a short delay is included in the loop to ensure the output is readable.

## Pulse Width Modulation

Pulse Width Modulation (PWM) is a method to emulate an analog output using a digital pin. It does this by rapidly toggling the pin between low and high states. Two primary aspects define PWM behavior:

- **Frequency**: This is the speed at which the pin toggles between low and high states. A higher frequency means the pin toggles faster.
- **Duty cycle**: This refers to the ratio of the high state duration to the total cycle duration. A 100% duty cycle means the pin remains high all the time, while a 0% duty cycle means it stays low.

The available PWM pins of the Portenta C33 board in MicroPython are the following:

| **Available PWM Pins** |
|:----------------------:|
|         `P105`         |
|         `P106`         |
|         `P111`         |
|         `P303`         |
|         `P401`         |
|         `P601`         |

### Setting Up PWM

To use PWM, start by initializing a pin and then creating a PWM object associated with that pin.

```python
import machine

# Initialize a pin for PWM (e.g., pin P105)
p105 = machine.Pin('P105')
pwm1 = machine.PWM(p105)
```

### Configuring PWM Parameters

The frequency and duty cycle of the PWM signal are set based on the specific needs of your application:

```python
# Set the frequency to 500 Hz
pwm1.freq(500)

# Adjusting the duty cycle to 50 for 50% duty
pwm1.duty(50)
```

### Checking PWM Configuration

You can check the current configuration of the PWM object by printing it:

```python
# Will show the current frequency and duty cycle
print(pwm1)
```

Retrieve the frequency and duty cycle values:

```python
current_freq = pwm1.freq()
current_duty = pwm1.duty()
```

### Deinitializing PWM

When PWM is no longer needed, the pin can be deinitialized:

```python
pwm1.deinit()
```

### Practical Example

In this example, we will use PWM to control the brightness of an LED connected to pin `P105` of the Portenta C33 board.

```python
import machine
import time

# Configure the LED pin and PWM
led_pin = machine.Pin('P105')
led_pwm = machine.PWM(led_pin)
led_pwm.freq(500)

# Loop to vary brightness
while True:
    # Increase brightness
    for duty in range(100):
        led_pwm.duty(duty)
        time.sleep(0.001)

    # Decrease brightness
    for duty in range(100, -1, -1):
        led_pwm.duty(duty)
        time.sleep(0.001)
```

## Real-Time Clock

The `RTC` class in MicroPython provides a way to manage and utilize the Real-Time Clock (RTC) of the Portenta C33 board. This feature is essential for applications that require accurate timekeeping, even when the main processor is not active. The RTC maintains accurate time and date, functioning independently from the main system. It continues to keep track of the time even when the board is powered off, as long as it's connected to a power source like a battery.

### Initializing the RTC

To use the RTC, first create an RTC object. This object is then used to set or read the current date and time.


```python
import machine

# Create an RTC object
rtc = machine.RTC()
```

### Setting and Getting Date and Time

The RTC allows you to set and retrieve the current date and time. The date and time are represented as an 8-tuple format.

```python
# Setting the RTC date and time
rtc.datetime((2024, 1, 4, 4, 20, 0, 0, 0))

# Getting the current date and time
current_datetime = rtc.datetime()
print("- Current date and time:", current_datetime)
```

The 8-tuple for the date and time follows the format `(year, month, day, weekday, hours, minutes, seconds, subseconds)`.

### Practical Example

A practical use case for the RTC is to add timestamps to sensor data readings. By setting the current time on the RTC, you can then append an accurate timestamp each time a sensor value is logged.

```python
import machine

# Initialize the RTC and set the current datetime
rtc.datetime((2024, 1, 4, 4, 20, 0, 0, 0))

# Function to read a sensor value (placeholder)
def read_sensor():
    # Replace with actual sensor reading logic
    return 42  

# Read sensor value and get the current time
sensor_value = read_sensor()
timestamp = rtc.datetime()

# Output the sensor value with its timestamp
print("- Sensor value at ", timestamp, ":", sensor_value)
```

In this example, every sensor reading is accompanied by a timestamp, which can be crucial for data analysis or logging purposes. The RTC's ability to maintain time independently of the main system's power status makes it reliable for time-sensitive applications.
