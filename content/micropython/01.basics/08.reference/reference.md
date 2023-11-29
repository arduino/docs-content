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

<!-- Section not started yet
## Advanced I/O

### noTone()
### pulseIn()
### pulseInLong()
### shiftIn()
### shiftOut()
### tone()

## Math

### abs()
### constrain()
### map()
### max()
### min()
### pow()
### sq()
### sqrt()

Trigonometry

### cos()
### sin()
### tan()

Characters

### isAlpha()
### isAlphaNumeric()
### isAscii()
### isControl()
### isDigit()
### isGraph()
### isHexadecimalDigit()
### isLowerCase()
### isPrintable()
### isPunct()
### isSpace()
### isUpperCase()
### isWhitespace()

Random Numbers

## random()
## randomSeed()


External Interrupts

### attachInterrupt()
### detachInterrupt()
### digitalPinToInterrupt()

Interrupts

### interrupts()
### noInterrupts()

Communication

### Print
### Serial
### SPI
### Stream
### Wire

USB

### Keyboard
### Mouse

-->