---
title: MicroPython Reference
description: A reference of the MicroPython API
authors: Karl Söderby
micropython_type: basics
---

***Note that this article is a work in progress and is subject to major changes.***

This reference acts as a "translation" between what is known as the "Arduino API", which is documented in the [Arduino Language Reference](), and the MicroPython API.

Please note that implementations may vary from board to board, such as how you configure pins, and how to use PWM.

The main goal with this reference is to provide an understanding of how to e.g. use common Arduino concepts such as `digitalWrite()` in a MicroPython script.

For example:
- `digitalWrite(pin, HIGH)` (Arduino/C++)
- `pin.value(1)` (MicroPython)

## Index

- [Index](#index)
- [Digital I/O](#digital-io)
  - [pinMode()](#pinmode)
  - [digitalRead()](#digitalread)
  - [digitalWrite()](#digitalwrite)
- [Analog I/O](#analog-io)
  - [Configure Input (ADC)](#configure-input-adc)
  - [Configure Output (PWM)](#configure-output-pwm)
  - [analogRead()](#analogread)
  - [analogWrite()](#analogwrite)
  - [analogWrite() (STM32)](#analogwrite-stm32)
- [Time](#time)
  - [delay()](#delay)
  - [millis()](#millis)
- [Bits and Bytes](#bits-and-bytes)
  - [bitRead()](#bitread)
  - [bitSet()](#bitset)
  - [highByte()](#highbyte)
  - [lowByte()](#lowbyte)
- [Advanced I/O](#advanced-io)
  - [noTone()](#notone)
  - [pulseIn()](#pulsein)
  - [shiftIn()](#shiftin)
  - [shiftOut()](#shiftout)
  - [tone()](#tone)
- [Math](#math)
  - [abs()](#abs)
  - [constrain()](#constrain)
  - [map()](#map)
  - [max()](#max)
  - [min()](#min)
  - [pow()](#pow)
  - [sq()](#sq)
  - [sqrt()](#sqrt)
  - [cos()](#cos)
  - [sin()](#sin)
  - [tan()](#tan)
- [Characters](#characters)
  - [isAlpha()](#isalpha)
  - [isAlphaNumeric()](#isalphanumeric)
  - [isAscii()](#isascii)
  - [isControl()](#iscontrol)
  - [isDigit()](#isdigit)
  - [isGraph()](#isgraph)
  - [isLowerCase()](#islowercase)
  - [isPrintable()](#isprintable)
  - [isPunct()](#ispunct)
  - [isSpace()](#isspace)
  - [isUpperCase()](#isuppercase)
- [Random Numbers](#random-numbers)
- [random()](#random)
- [randomSeed()](#randomseed)
- [External Interrupts](#external-interrupts)
  - [attachInterrupt()](#attachinterrupt)
- [Attaches an interrupt to a pin with specified mode.](#attaches-an-interrupt-to-a-pin-with-specified-mode)
  - [detachInterrupt()](#detachinterrupt)
  - [digitalPinToInterrupt()](#digitalpintointerrupt)
- [Interrupts](#interrupts)
  - [interrupts()](#interrupts-1)
  - [noInterrupts()](#nointerrupts)
- [Communication](#communication)
  - [Print](#print)
  - [Serial](#serial)
  - [SPI](#spi)
  - [Stream](#stream)
  - [Wire](#wire)
- [USB](#usb)
  - [Keyboard](#keyboard)
  - [Mouse](#mouse)

## Digital I/O

To access digital GPIOs using MicroPython, we use the `Pin` module. To define a pin, we use `Pin(pin,type)`.

### pinMode()

- `output_pin = Pin(pin, Pin.OUT)` (define as output) 
- `input = Pin(pin, Pin.IN)`
- `input_pullup = Pin(pin, Pin.IN, Pin.PULL_UP` (define as input pull up)
- `input_pulldown = Pin(pin, Pin.IN, Pin.PULL_DOWN` (define as input pull down)

Parameters:
- `pin` - pin we want to set
- `type` - define as input or output
- `pullmode` - define as pull up or pull down mode (optional). 

**Example:**

```python
from machine import Pin

output_pin = Pin(5, Pin.OUT) #define pin
input_pin = Pin(6, Pin.IN, Pin.PULL_UP) #define pin as an input pullup
```

### digitalRead()

`pin.value()`

Reads the state of a digital pin defined as input.
- **Parameters:** none.
- **Returns:** the value of the digital pin (0 or 1).

```python
from machine import Pin

pin = Pin(5, Pin.PULL_UP) #define pin
reading = pin.value() #read pin

print(reading) #print state of pin to REPL
```

### digitalWrite()

`pin.value(state)`

Writes a state to a digital pin defined as an output.
- **Parameters:** none.
- **Returns:** the value of the digital pin (0 or 1).


```python
from machine import Pin

pin = Pin(5, Pin.PULL_UP) #define pin
pin.value(1) #set pin to high state
```

## Analog I/O

### Configure Input (ADC)

To read an analog input pin, we need to attach a pin to the ADC.

- `adc_pin = machine.Pin(pin)` - create the pin.
- `adc = machine.ADC(adc_pin)` - attach it to the ADC.

### Configure Output (PWM)

To write analog values using PWM, we need to define the pin and set the frequency.

- `pwm = PWM(Pin(15))`
- `pwm.freq(1000)`

On STM32 boards (GIGA R1, Portenta H7 etc.), we need to define at as follows:

- `pin1 = Pin("PC6", Pin.OUT_PP, Pin.PULL_NONE)`
- `timer1 = Timer(3, freq=1000)`
- `channel1 = timer1.channel(1, Timer.PWM, pin=pin1, pulse_width=0)`

### analogRead()

`adc.read_u16()`

Attach a pin to an ADC, and read the raw value. 

- **Returns:** - the raw analog value in a 16-bit format (0-65535).
- **Parameters:** none.

**Example:**

```python
import machine
import time

adc_pin = machine.Pin("PC4") 
adc = machine.ADC(adc_pin)

while True:
    reading = adc.read_u16()    
    print("ADC: ",reading)

    time.sleep_ms(1000)
```

**Note:** to convert the 16-bit value to a 10-bit value, you can use the following formula:

```python
# right-shifts the bits and discards the 6 most significant bits
# effectively changing the value range from 0-65535 to 0-1023
result = (reading >> 6) & 0x3FF
```

### analogWrite()

`pwm.duty_u16(duty)`

Writes the duty cycle (0-65535) to a PWM pin. 

- **Parameters:** duty cycle (0-65535).
- **Returns:** None.

**Example:**

```python
from machine import Pin, PWM, ADC

pwm = PWM(Pin(15))
duty = 30000 #between 0-65535

pwm.freq(1000)

while True:
    pwm.duty_u16(duty)
```

### analogWrite() (STM32)

`channel1.pulse_width(duty)`

Writes the duty cycle in percentage (0-100) to a PWM pin. 

- **Parameters:** duty cycle in percentage (0-100).
- **Returns:** None.

**Example:**

```python
import pyb
import time
from pyb import Pin, Timer

pin1 = Pin("PC6", Pin.OUT_PP, Pin.PULL_NONE)
timer1 = Timer(3, freq=1000)
channel1 = timer1.channel(1, Timer.PWM, pin=pin1, pulse_width=0)

channel1.pulse_width(50) #duty cycle at 50%
```

## Time

To introduce timings & delays, use the `time` module.

### delay()

`time.sleep(seconds)`

Creates a delay for the number of specified seconds.

- **Parameters:** seconds.
- **Returns:** nothing.

**Example:**
```python
import time

time.sleep(1) #freeze program for 1 seconds
```

### millis()

`time.time()`

Returns the number of seconds elapsed since the start of the script.

- **Returns:** seconds (float).
- **Parameters:** none.

**Example:**

```python
'''
"Blink Without Delay" script.
Blinks an LED attached to pin 5 every second,
without freezing the program.
'''

import time
from machine import Pin

ledPin = Pin(5, Pin.OUT) 

interval = 1
previousTime = 0
switch = False

while True:
    currentTime = time.time()
    
    if currentTime - previousTime >= interval:
        previousTime = currentTime
        
        switch = not switch
        ledPin.value(switch)
```

## Bits and Bytes

### bitRead()

`bit_value = (variable >> bit_index) & 1`

Reads a specific bit of an integer variable.

**Parameters:**
- `variable` - an integer variable with numeric value, e.g. `12345`
- `bit_index` - the specific bit we want to read (e.g. `5`)

**Returns:**
- The value of the specific bit.

**Example:**

```python
'''
This example prints out each bit of an 8-bit variable
It stops after 255 (the max value an 8-bit variable can hold)
'''
import time
counter = 0

bit_length = 8 # 8 bits
while True:
    bits = []
    for bit_index in range(bit_length - 1, -1, -1):
        bit_value = (counter >> bit_index) & 1
        bits.append(bit_value)
    print("Binary: ", bits, " DEC: ", counter)

    counter += 1
    time.sleep(0.01)
    if counter > 255:
        break
```

### bitSet()

`variable = variable | (1 << bit_index)`

Sets a specific bit of an integer variable.

**Parameters:**
- `variable` - an integer variable with numeric value, e.g. `12345`
- `bit_index` - the specific bit we want to read (e.g. `5`)

**Returns:**
- Nothing.

**Example:**

```python
# Example variable
variable = 12345

# Set the third bit
bit_index = 2

print()
print("Before setting a bit: ",bin(variable))
print("Before setting a bit: ",variable)
variable = variable | (1 << bit_index)

# Print the result
print("After setting a bit: ",bin(variable))
print("After setting a bit: ",variable)
```

### highByte()

`leftmost_bit = (variable >> leftmost_bit_index) & 1`

Reads the high-order (leftmost) bit of a variable.

**Parameters**
- `variable` - an integer variable with numeric value, e.g. `255`
- `leftmost_bit_index` - the leftmost bit, e.g. `7` in an 8-bit variable.

**Returns**
- `leftmost_bit` - the value of the leftmost bit.

**Example:**

```python
# Example variable
variable = 255

bit_length = 8
# Extract the leftmost bit
leftmost_bit_index = bit_length - 1
leftmost_bit = (variable >> leftmost_bit_index) & 1

# Print the result
print("Leftmost bit: ", leftmost_bit)
```

### lowByte()

`rightmost_bit = variable & 1`

Reads the low-order (rightmost) bit of a variable.

**Parameters**
- `variable` - an integer variable with numeric value, e.g. `255`
- `rightmost_bit` - the rightmost bit, `0` in an 8-bit variable.

**Returns**
- `rightmost_bit` - the value of the rightmost bit, e.g. `1` if `variable` is 255 (255 is 11111111 in binary).

**Example:**

```python
# Example variable
variable = 255

# Extract the rightmost bit
rightmost_bit = variable & 1

# Print the result
print("Rigthmost bit: ", rightmost_bit)
```


## Advanced I/O

### noTone()

Stops generating a tone on a specified pin by deinitializing the PWM (Pulse Width Modulation) associated with the given pin.

**Parameters:**
- `pin`: The pin number to stop generating the tone.

**Returns:**
- Nothing

**Example:**

```python
import machine

def noTone(pin):
    pwm = machine.PWM(machine.Pin(pin))
    pwm.deinit()
```

### pulseIn()

**Example:**

```python
import machine

def pulseIn(pin, level, timeout=1000000):
    pulse_start = machine.time_pulse_us(machine.Pin(pin), level, timeout)
    pulse_end = machine.time_pulse_us(machine.Pin(pin), not level, timeout)
    return pulse_end - pulse_start
```

### shiftIn()

**Example:**

```python
import machine

def shiftIn(dataPin, clockPin, bitOrder=machine.MSBFIRST):
    value = 0
    for i in range(8):
        value |= machine.Pin(dataPin).value() << (7 - i)
        machine.Pin(clockPin).value(1)
        machine.Pin(clockPin).value(0)
    return value
```

### shiftOut()

**Example:**

```python
import machine

def shiftOut(dataPin, clockPin, bitOrder=machine.MSBFIRST, value):
    for i in range(8):
        mask = 1 << i if bitOrder == machine.LSBFIRST else 1 << (7 - i)
        machine.Pin(dataPin).value(bool(value & mask))
        machine.Pin(clockPin).value(1)
        machine.Pin(clockPin).value(0)
```

### tone()

**Example:**

```python
import machine

def tone(pin, frequency, duration=None):
    pwm = machine.PWM(machine.Pin(pin))
    pwm.freq(frequency)
    if duration is not None:
        machine.sleep(duration)
        pwm.deinit()
```

## Math

### abs()

**Example:**

```python
result = abs(-5)
```

### constrain()

**Example:**

```python
def constrain(value, lower, upper):
    return max(min(value, upper), lower)

result = constrain(10, 0, 5)  # Result will be 5
```


### map()

**Example:**

```python
def map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

result = map(50, 0, 100, 0, 255)
```


### max()

**Example:**

```python
result = max(5, 10, 3)  # Result will be 10
```

### min()

**Example:**

```python
result = min(5, 10, 3)  # Result will be 3
```

### pow()

**Example:**

```python
result = pow(2, 3)  # Result will be 8
```

### sq()

**Example:**

```python
result = sq(4)  # Result will be 16
```

### sqrt()

**Example:**

```python
import math

result = math.sqrt(16)  # Result will be 4.0
```




Trigonometry

### cos()


### sin()

**Example:**

```python
import math

# Specify the angle in radians
angle_in_radians = math.radians(30)

# Calculate the sine of the angle
sine_value = math.sin(angle_in_radians)

# Print the result
print(f"The sine of {angle_in_radians} radians is: {sine_value}")

```

### tan()

**Example:**

```python
import math

# Specify the angle in radians
angle_in_radians = math.radians(60)

# Calculate the tangent of the angle
tangent_value = math.tan(angle_in_radians)

# Print the result
print(f"The tangent of {angle_in_radians} radians is: {tangent_value}")
```

## Characters

### isAlpha()

`char.isalpha()`

Analyse if a single character is alphabetic.

```python
char = 'a'
if char.isalpha():
    print(f"{char} is alphabetic.")
else:
    print(f"{char} is not alphabetic.")
```

### isAlphaNumeric()

`char.isDigit()` and `char.isAlpha()`

Checks if char is a number **or** an alphabetic character.  

**Example:**

```python
# Function to check if a character is alphanumeric
def is_alphanumeric(char):
    return char.isalpha() or char.isdigit()

# Example usage
test_char = 'a'

if is_alphanumeric(test_char):
    print(f"{test_char} is alphanumeric.")
else:
    print(f"{test_char} is not alphanumeric.")

```

### isAscii()

`ord(char) < 128`

Checks if character is an ASCII character by checking if the decimal number of the character presented is over 128. If it is over, it is not an ASCII character.

```python
char = 'Ö'

if 0 <= ord(char) < 128:
    print(f"{char} is an ASCII character.")
else:
    print(f"{char} is not an ASCII character.")
```

### isControl()

`ord(char) < 32 or ord(char) == 127`

Checks whether character presented is less than 32 or 127, which represents control characters.

```python
char = '\t'  # Example: Tab character

if 0 <= ord(char) < 32 or ord(char) == 127:
    print(f"{char} is a control character.")
else:
    print(f"{char} is not a control character.")
```

### isDigit()

`char.isDigit()`


```python
char = '5'
if char.isdigit():
    print(f"{char} is a digit.")
else:
    print(f"{char} is not a digit.")
```

### isGraph()

**Example:**

```python
char = 'A'

if char.isprintable() and not char.isspace():
    print(f"{char} is a graph character.")
else:
    print(f"{char} is not a graph character.")
```

### isLowerCase()

**Example:**

`islower()`

```python
char = 'a'

if char.islower():
    print("Is lower case.")
else:
    print("Is not lower case.")
```

### isPrintable()

`isprintable()`

Checks if a character is printable, e.g. any character, including blank space, but not control characters.

**Example:**

```python
char = '\t'

if char.isprintable():
    print("Is printable.")
else:
    print("Is not printable.")
```

### isPunct()

There is no built-in function for checking punctuation in Python. Instead, we can define a variable containing all punctioation characters, and a function that compares the provided value with it.

**Example:**

```python
def isPunct(char):
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return char in punctuation_chars

print(isPunct("."))
```

### isSpace()

`char.isspace()`

**Example:**

```python
char = ' '

if char.isspace():
    print(f"{char} is a space character.")
else:
    print(f"{char} is not a space character.")
```

### isUpperCase()

`char.isupper()`

**Example:**

```python
char = 'A'

if char.isupper():
    print(f"{char} is an uppercase letter.")
else:
    print(f"{char} is not an uppercase letter.")
```


## Random Numbers


## random()

`random.random()`

Produces a random number within the range provided.

**Example:**

```python
import random

random_integer = random.randint(1, 10)
print("Random integer between 1 and 10:", random_integer)
```

## randomSeed()

`seed_value = int(time.time())` and `random.seed()`

To generate a random seed value, we first use the `time()` module to generate a unique value, and feed it to the `random.seed()` generator. The result is that you will always get a unique random number.

**Example:**

```python
import random
import time

# Seed the random number generator with the current time
seed_value = int(time.time())
random.seed(seed_value)

# Generate random numbers using the seeded generator
random_number = random.randint(1,100)
print(random_number)
```

***Note that `time.time()` generates a new value every second. E.g. running `random.seed()` twice within a second will generate the same value. `random.seed()` should not be used repetitively.***

## External Interrupts

### attachInterrupt()

`interrupt_pin.irq(trigger=mode, handler=function)`

Attaches an interrupt to a pin with specified mode.
- 

```python
from machine import Pin
import time

# Define a callback function to be called when the interrupt occurs
def interrupt_callback(pin):
    print("Interrupt occurred on pin", pin_name)

# Pin name
pin_name = "PA3"

# Define the pin to which you want to attach the interrupt
interrupt_pin = Pin(pin_name, Pin.IN, Pin.PULL_UP)  # Replace 2 with the actual pin number you are using

# Attach the interrupt to the pin, specifying the callback function and trigger type
interrupt_pin.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_callback)

while True:
    print("hello world")
    time.sleep(1)
```

### detachInterrupt()

`interrupt_pin.irq(handler=None)`

Detaches the active interrupt from specified pin.

**Example:**

```python
from machine import Pin
import time

# Define a callback function to be called when the interrupt occurs
def interrupt_callback(pin):
    print("Interrupt occurred on pin", pin_name)
    # Detaches the interrupt from the pin
    interrupt_pin.irq(handler=None) 

# Pin name
pin_name = "PA3"

# Define the pin to which you want to attach the interrupt
interrupt_pin = Pin(pin_name, Pin.IN, Pin.PULL_UP)  # Replace 2 with the actual pin number you are using

# Attach the interrupt to the pin, specifying the callback function and trigger type
interrupt_pin.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_callback)

while True:
    print("hello world")
    time.sleep(1)
```

### digitalPinToInterrupt()
<!-- TODO -->
## Interrupts


### interrupts()
<!-- TODO -->
### noInterrupts()
<!-- TODO -->
## Communication


### Print
<!-- TODO -->
### Serial
<!-- TODO -->
### SPI
<!-- TODO -->
### Stream
<!-- TODO -->
### Wire
<!-- TODO -->
## USB


### Keyboard
<!-- TODO -->
### Mouse
<!-- TODO -->