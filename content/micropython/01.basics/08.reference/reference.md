---
title: MicroPython Reference
description: A reference of the MicroPython API
authors: Karl Söderby
---


--- 

### Template

``

- **Parameters:**
- **Returns:**

---

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
output_pin = Pin(5, Pin.OUT) #define pin
input_pin = Pin(6, Pin.IN, Pin.PULL_UP) #define pin as an input pullup
```

### digitalRead()

`pin.value()`

Reads the state of a digital pin defined as input.
- **Parameters:** none.
- **Returns:** the value of the digital pin (0 or 1).

```python
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
pin = Pin(5, Pin.PULL_UP) #define pin
pin.value(1) #set pin to high state
```

## Analog I/O


### analogRead()

`adc.read_u16()`

To read an analog pin, we first need to attach a pin to the ADC.

- `adc_pin = machine.Pin(pin)` - create the pin.
- `adc = machine.ADC(adc_pin)` - attach it to the ADC.

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

To write analog values using PWM, we need to define the pin and set the frequency.




### analogReadResolution()
### analogWriteResolution()

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

time.sleep(5) #freeze program for 5 seconds
```

### millis()

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

Bits and Bytes

### bit()
### bitClear()
### bitRead()
### bitSet()
### bitWrite()
### highByte()
### lowByte()

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