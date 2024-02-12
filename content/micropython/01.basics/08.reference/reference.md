---
title: MicroPython Reference
description: A single document reference of the MicroPython API.
authors: Karl Söderby
micropython_type: basics
---

***Please note that some part of this reference is still in progress and will be updated over time. The article is subject to minor changes.***

This reference serves as a "translation" between what is known as the **Arduino API**, which is documented in the [Arduino Language Reference](https://www.arduino.cc/reference/en/), and the **MicroPython API**.

The main goal with this reference is to provide an understanding of how to e.g. use common Arduino concepts such as `digitalWrite()` in a MicroPython script.

For example:
- `digitalWrite(pin, HIGH)` (Arduino/C++)
- `pin.value(1)` (MicroPython)

The entries are named exactly the same as in the language reference, with the MicroPython syntax, description and code example provided for each entry. It is however important to understand that any given board may not be fully compatible with this reference, as some implementations vary between board/architecture. For example, using PWM on a STM32 board will differ from using it on an ESP32 board.

***Note that several entries in the original [Language Reference](https://www.arduino.cc/reference/en/) are directly taken from the C++ reference. In the same fashion, many functions located in this reference are taken from the Python reference, and are not MicroPython specific.***

## Digital I/O

To access digital GPIOs using MicroPython, we use the `Pin` module. To define a pin, we use `Pin(pin,type)`.

### pinMode()

- `output_pin = Pin(pin, Pin.OUT)` (define as output) 
- `input = Pin(pin, Pin.IN)`
- `input_pullup = Pin(pin, Pin.IN, Pin.PULL_UP` (define as input pull up)
- `input_pulldown = Pin(pin, Pin.IN, Pin.PULL_DOWN` (define as input pull down)

**Parameters:**
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

### tone() / noTone()

- `tone(pin,frequency,volume,duration)`
- `noTone(pin,duration)`

To use the popular `tone()` and `noTone()` functions, we need to define them as functions as they currently are not implemented.

**Example:**

```python
from machine import Pin, PWM
import time
    
def tone(pin,frequency,volume,duration=None):
    speaker = PWM(Pin(pin))
    speaker.freq(frequency)
    speaker.duty_u16(volume)
    if duration is not None:
        time.sleep(duration)

def noTone(pin,duration=None):
    speaker = PWM(Pin(pin))
    speaker.deinit()
    if duration is not None:
        time.sleep(duration)

while True:
    tone(5,500,1000,1)
    noTone(5,1)
```

## Math

### abs()

`abs(value)`

Returns the absolute value of a number.

**Example:**

```python
result = abs(-5)
print(result)
```

### constrain()

`constrain(value, min, max)`

Constrains the value to be within a specific range.

**Example:**

```python
def constrain(value, lower, upper):
    return max(min(value, upper), lower)

result = constrain(10, 0, 5)  # Result will be 5
print(result)
```


### map()

`map(value, in_min, in_max, out_min, out_max)`

Maps a value from one range to another.

**Example:**

```python
def map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

result = map(50, 0, 100, 0, 255) # Result is 127.5
print(result)
```


### max()

`max(value1, value2, value3, valueX)`

Returns the highest value among the given parameters. Accepts many arguments separated by comma.

**Example:**

```python
result = max(5, 10, 3)  # Result will be 10
print(result)
```

### min()

`min(value1, value2, value3, valueX)`

Returns the lowest value among the given parameters. Accepts many arguments separated by comma.

**Example:**

```python
result = min(5, 10, 3)  # Result will be 3
print(result)
```

### pow()

`pow(base, exponent)`

Raises a number to the power of another.

**Example:**

```python
result = pow(2, 3)  # Result will be 8
print(result)
```

### sq()

`sq(value)`

Returns the square of a number.

**Example:**

```python
result = sq(4)  # Result will be 16
print(result)
```

### sqrt()

`math.sqrt(value)`

This function returns the square root of a number.

**Example:**

```python
import math

result = math.sqrt(16)  # Result will be 4.0
print(result)
```

## Trigonometry

### cos()

`math.cos(angle_in_radians)`

Calculates the cosine of an angle (in radians). The result will be between -1 and 1.

**Example:**

```python
import math

# Specify the angle in radians
angle_in_radians = math.radians(45)

# Calculate the cosine of the angle
cos_value = math.cos(angle_in_radians)

# Print the result
print(f"The cosine of {angle_in_radians} radians is: {cosine_value}")
```

### sin()

`math.sin(angle_in_radians)`

Calculates the sine of an angle (in radians). The result will be between -1 and 1.

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

`math.tan(angle_in_radians)`

Calculates the tangent of an angle (in radians). The result will be between negative infinity and infinity.

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


### random()

`random.random()`

Produces a random number within the range provided.

**Example:**

```python
import random

random_integer = random.randint(1, 10)
print("Random integer between 1 and 10:", random_integer)
```

### randomSeed()

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

## Serial (USB)

In the Arduino API, we are accustomed to using `Serial.begin()` and `Serial.print()` to send data from a board to a computer.

The same API is used for sending and receiving data over UART, using `Serial1`. For UART, see the [Serial (UART)](#serial-uart) section. 

In MicroPython, to send data over USB, we can use the `print()` function, which prints the content to the REPL. As MicroPython is implemented a bit differently, the REPL also allows you to write commands inside it. The REPL is therefore in many ways, different from the Serial Monitor we are used to in the Arduino IDE.


### Serial.print()

`print(content)`

This function prints the content to the REPL. 

**Example:**

```python
variable = 5

print("I am a string!") # prints a string
print(variable) # prints value of variable
print(58) # prints a numeric value
print(f"The value is {variable}") # prints a string with a value inserted
```

## Serial1 (UART)

UART communication is initialized using the `UART` object from the `machine` module.

***When sending & receiving data on a hardware UART port on an Arduino board, we use the `Serial1` class.***

### Serial1.begin()

`machine.UART(port, baudrate=baud)`

Initialize UART communication on specified port (default is `1`), and specified baud rate.

**Example:**

```python
import machine
import time

uart = machine.UART(1, baudrate=57600)
```

***Baud rate `57600` is used as using the common `115200` and `9600` interfered with the Arduino IDE's Serial Monitor.***

### Serial1.available()

`uart.any()`

Checks if there's any data available on the UART port.

**Example:**

```python
import machine
import time

uart = machine.UART(1, baudrate=57600)

while True:
    if uart.any():
        print("data available")
```


### Serial1.read()

`uart.read(1)`

Reads one byte from the buffer.

**Example:**

This example reads the first byte of data from the buffer, stores it into the `received_data` string. When a new line character (`\n`) is detected, the received message is printed to the REPL.

```python
import machine
import time


uart = machine.UART(1, baudrate=57600) 
received_data = ""

while True:
    if uart.any():
        data = uart.read(1)
        received_data += data
    
    if received_data and received_data[-1] == '\n':
        print("Received:", received_data[:-1])  # Print the accumulated data (excluding the newline character)
        received_data = ""  # Reset the string after printing
    
    time.sleep(0.1) 
```

### Serial1.write()

`uart.write(message)`

Writes / sends data over UART.

**Example:**

```python
import machine
import time


uart = machine.UART(1, baudrate=57600)  

while True:
    data_to_send = "Hello World!\n"
    uart.write(data_to_send)
    
    time.sleep(1)  
```

## SPI

SPI communication is initialized using the `SPI` object from the `machine` module. 

### SPI.begin()

`spi = machine.SPI(port, baudrate, polarity, phase)`

SPI is initialized by importing the `machine` module and specifying a number of parameters, such as baudrate and polarity.

**Example:**

```python
import machine

spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0)
```

### SPI.read()

***Note that `SPI.read()` is not in the Arduino API, as the `SPI.transfer()` handles both outgoing and incoming data.***

`spi.readinto(data_in)`

Reads incoming data and stores it in an array. The size of the array needs to be adjusted to match the size of the incoming data size.

**Example:**

```python
import machine
import time

spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0)
data_in = bytearray(3)

spi.readinto(data_in)

print("Received Data:", data_in)
```

### SPI.write()

***Note that `SPI.write()` is not in the Arduino API, as the `SPI.transfer()` handles both outgoing and incoming data.***

`spi.write(data_out)`

Writes data to the SPI bus.

**Example:**

```python
import machine
import time

spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0) 
data_out = b'\x01\x02\x03'

spi.write(data_out)
```

### SPI.transfer()

`spi.write_readinto(data_out, data_in)`

Reads & writes data simultaneously, where incoming data is stored in a buffer.

**Example:**

```python
import machine
import time

spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0)

data_to_send = b'\x01\x02\x03'

data_received = bytearray(len(data_to_send))

spi.write_readinto(data_to_send, data_received)

print("Received Data:", data_received)

spi.deinit()
```

### Bit Size

`spi.bits = 8`

Sets the number of bits per word. 

**Example:**

```python
spi.bits = 8
```

## Wire / I2C

### Wire.begin()

`i2c = I2C(port, scl, sda, freq)`

Initializes I2C communication on specified port and pins. The `port` and `freq` are optional parameters, if left unspecified, default values will be set. 
```python
from machine import I2C

i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=100000)
```

### Wire.available()

`i2c.in_waiting()`

Checks the number of available bytes to read.

```python
available_bytes = i2c.in_waiting()

print("Available bytes to read: ", available_bytes)
```

### Wire.read()

`i2c.readfrom(address, num_bytes)`

Reads data in specified number of bytes from a device with the specified address.

```python
data_in = i2c.readfrom(address, num_bytes)

print("I2C data: ", data_in)
```

### Wire.write()

`i2c.writeto(address, data_out)`

Writes data to specified address.

**Example:**

```python
from machine import I2C, Pin

# Initialize I2C anc configure device & reg addresses
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)  # Adjust pins and frequency as needed
device_address = 0x68
register_address = 0x00

# The array of bytes to be send out
# This buffer simply stores 1,2,3,4
data_out = bytearray([0x01, 0x02, 0x03, 0x04])

# Send the device address with the write bit to indicate a write operation
i2c.writeto(device_address, bytearray([register_address]))

# Finally, send data to the device
i2c.writeto(device_address, data_out)
```

### Wire.setClock()

The frequency for the clock is set during initialization. See [begin()](#wirebegin) for more info.

### SoftI2C

MicroPython has a built in class called `SoftI2C` (as in software I2C). Software I2C does not use a dedicated hardware I2C peripheral, but instead relies on the CPU to handle the clock signal, communication protocol etc.

`SoftI2C` is available through the `machine` module, and uses the same API as hardware I2C, with a few additional methods.

- `softi2c = machine.SoftI2C(scl,sda,freq,timeout)` - creates the `softi2c` object with specified pins, frequency and timeout.
- `softi2c.start()` - create the start condition for initializing communication over I2C (SDA goes to **LOW** while SCL is **HIGH**).
- `softi2c.stop()` - create the stop condition for ending communication over I2C (SDA goes to **HIGH** while SCL is **HIGH**).

## USB HID

Human Interface Device (HID) is currently **not supported** on any of the Arduino boards. 

To use HID functions on Arduino boards that support it (most modern boards), please refer to the Arduino / C++ reference:
- [Mouse](https://www.arduino.cc/reference/en/language/functions/usb/mouse/)
- [Keyboard](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/)

## Data Types

When declaring variables in MicroPython / Python, you do not need to specify the data type, this is done automatically.

Examples for variable declaration can be seen in the snippet below:

```python
var_array = [1, 2, 3]
var_bool = True/False
var_unsigned_byte = 255
var_signed_byte = -128
var_char = 'A'
var_double = 3.14
var_float = 29.231232
var_int = 2147483647
var_long = 2147483647
var_short = 32767
var_string = "This is a string"
var_unsigned_int = 4294967295
var_unsigned_long = 4294967295
```

### size_t

`len(my_array)`

There is no direct equivalent to `size_t`, but using the `len()` function, you can return the size of an object.

**Example:**

```python
my_array = [1,2,3,4,5]

array_size = len(my_array)

print("Size of array is: ", array_size)
```

### void

`def my_func():`

There is no direct equivalent to `void`, but when defining a function without a return statement, the function is of a "void" type.

**Example:**

```python
def my_function():
    print("Function executed, nothing returned though!")
```

## Conversion

### byte()

`bytes(value)`

Converts a value to a byte.

**Example:**

```python
my_byte = bytes([255])
print(my_byte) # prints \xff which in hex is 255
```

### char()

`chr(value)`

Converts a value to a char


**Example:**

```python
value = 65  # 65 is "A" in ASCII code
char_value = chr(value) # converts a value to char (65 to "A")
print("Char value:", char_value) # prints "A"
```

### float()

`float(value)`

**Example 1:**

Converts an integer to float.

```python
value = 25
float_value = float(value)
print("Float value:", float_value) # prints 25.0
```

**Example 2:**

Converts a string to float.

```python
value = "3.14"
float_value = float(value)
print("Float value:", float_value) #prints 3.14
```

### int()

`int(value)`

Converts a value

**Example 1:**

Converts a float to int. Rounds the number up/down, e.g. `42.232` = `42`.

```python
value = 42.232
int_value = int(value)
print("Int value:", int_value)
```

**Example 2:**

Converts a string to int.

```python
value = "42"
int_value = int(value)
print("Int value:", int_value)
```

## Local / Global Variables

Variables can either be globally or locally declared:

- Global variables can be accessed anywhere in the program.
- Local variables can only be accessed within the function it is declared.

When creating a program, you can decide whether you want certain variables accessible from anywhere, or just within the function. 

The benefit of declaring a local variable is that it uses less memory space (as it is only assigned within the function).

The con of declaring a local variable is that it is not accessible anywhere else in the program.

```python
global_var = 0 #initial value

def my_function():
    local_var = 10 # declare local variable
    print()
    print("(inside function) local_var is: ", local_var)

    global_var = local_var + 25
    print("(inside function) global_var is updated to: ", global_var)

    return global_var

global_var = my_function() + 25
print("(outside function) global_var is finally: ", global_var)

'''
The line below will cause the script to fail
because it is not declared globally.
'''
#print(local_var) 
```

## Sketch

MicroPython uses scripts as opposed to traditional sketches that require the `void loop()` and `void setup()` functions.

A script can be as simple as a single line that prints "Hello World!"

```python
print("Hello World!")
```

### loop()

`while True:`

A loop is not required in a MicroPython script, but is required in order to run a script continuously on the board. To have a loop in a program, we need to use a [while loop]().

**Example:**

The example below runs a loop that increases the `value` variable by `1` each time the loop is run. It then prints the value to the REPL, and waits for a second.

```python
import time
value = 0

while True:
    value += 1
    print(value)
    time.sleep(1)
```

### setup()

In MicroPython, there's no equalivent of the `setup()` function. Configurations that are traditionally done in this function can simply be declared at the top of the program.

**Example:**

This script simply declares a pin's pin mode (see [pinMode()](#pinmode)).

```python
from machine import Pin

output_pin = Pin(5, Pin.OUT)

while True:
    #loops forever
```

## Control Structure

Control structures are used to control the flow of a program, i.e. what code will and won't execute. When a condition is met, the specified code block executes.

### if

The `if` statement checks *if* a condition is met, and executes the following block of code.

**Example:**

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### else

The `else` statement can be used after e.g. an `if` statement. If the previous condition is not met, then it will the block of code following the `else` statement

**Example:**

```python
x = 5
y = 10

if x > y:
    print("x is greater")
else:
    print("y is greater")
```

### for

The `for` loop is used to iterate through a sequence, e.g. a range of numbers, a list, or a string. 

**Example 1: Number Range**

```python
for number in range(5):
    print(number)
```

**Example 2: List**

```python
my_list = [10, 20, 30, 40, 50]
for item in my_list:
    print(item)
```

**Example 3: String**

```python
my_string = "Hello World!"
for char in my_string:
    print(char)
```

### while

The while loop is used to repeatedly execute a block of code as long as the specified condition is `True`. 

**Example 1:**

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

**Example 2: Infinity Loop**

The while loop is critical to MicroPython as it is needed to create the "infinity" loop, i.e. a loop that runs whenever the board is powered. 

```python
while True:
    # your program
```



### break

The `break` statement is used to break out of loops before it ends.

**Example:**

```python
for i in range(5):
    if i == 3:
        break
    print(i)

```

### continue

The `continue` statement is used to skip to the end of the code block, effectively moving on to the next iteration. This is useful to e.g. filter out specific data points.

**Example:**

This example iterates through a list of numbers. If the number is less than `0` (negative), it will skip it.

```python
my_list = [0, -5, -3, 8, 9 , 11]
for num in my_list:
    if num < 0:
        continue
    print(num)
```

### return

Terminates a function and `return` a value from a function to the calling function.

**Example:**

In this example, we call a function named `add_numbers()`, which takes two parameters. It then returns the processed value, using the `return` statement.

```python
def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(5,5))
```

## Operators

### Arithmetic Operators

Arithmetic operators are symbols used in programming and mathematics to perform basic arithmetic operations on numerical values.

To assign a new value to any variable, use an assignment operator (single equal sign `=`).

```python
my_variable = 5 # the value of my_variable is now 5
```

The following arithmetic operators can be used:

- `%` (remainder)
- `*` (multiplication)
- `+` (addition)
- `-` (subtraction)
- `/` (division)
- `**` (exponentiation)


**Example:**

The script below demonstrates 

```python
remainder = 5 % 10 # remainder is 5
multiplication = 10 * 5 # result of multiplication is 50
addition = 10 + 5 # result of addition is 15
subtraction = 10 - 5 # result of subtraction is 5
division = 10 / 5 # result of division is 2
exponentiation = 10 ** 5 # result of exponentiation is 10000 (10*10*10*10*10)

print("remainder:", remainder)
print("multiplication:", multiplication)
print("addition:", addition)
print("subtraction:", subtraction)
print("division:", division)
print("exponentiation:", exponentiation)
```

### Comparison Operators

Comparison operators are used to compare two values or expressions, and returns a boolean result (`True` or `False`)

- `==` (equal to)
- `!=` (not equal to)
- `<` (less than)
- `<=` (less than or equal to)
- `>` (greater than)
- `>=` (greater than or equal to)

The following scripts will compare the `x` with `y` variables and print the result in the REPL.

**Equal to `==`**

```python
x = 10
y = 5

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
```

**Not equal to `!=`**

```python
x = 10
y = 5

if x != y:
    print("x is not equal to y")
else: 
    print("x is equal to y")
```

**Less than `<`**

```python
x = 10
y = 5

if x <  y:
    print("x is smaller than x")
else:
    print("x is not smaller than y")
```

**Less or equal to `<=`**

```python
x = 10
y = 5

if x <= y:
    print("x is smaller or equal to y")
else:    
    print("x is not smaller or equal to y")

```

**Greater than `>`**

```python
x = 10
y = 5

if x >  y:
    print("x is greater than y")
else:
    print("x is not greater than y")
```

**Greater than or equal to `>=`**

```python
x = 10
y = 5

if x >= y:
    print("x is greater than or equal to y")
else:
    print("x is not greater than or equal to y")

```

### Boolean Operators

Boolean operators are used to perform logical operations between Boolean values (`True` or `False`).

Boolean operators are expressed in written format, and not with symbols ( `!`, `&&`, `||`) like other programming frameworks such as Arduino / C++ use. 

- `not` (logical not)
- `and` (logical and)
- `or` (logical or)

The following scripts demonstrates how to use the boolean operators:

**Logical `not`:**

```python
x = True

if not x:
    print("False")
else:
    print("True")
```

**Logical `and`:**

```python
x = 7

if x > 5 and x < 10:
    print("x is greater than 5 AND smaller than 10")
```

**Logical `or`:**

```python
x = 5
y = 10

if x == 3 or y == 10:
    print("One condition matched!") 
```


### Bitwise Operators

Bitwise operators are used to manipulate individual bits at a binary level. For example, an integer variable that holds the value of `15` is in binary `1111`. With bitwise operators, you can for example change `1111` (15) to `1011` (11).

The following bitwise operators are available:

- `&` (bitwise and)
- `<<` (bitshift left)
- `>>` (bitshift right)
- `^` (bitwise xor)
- `|` (bitwise or)
- `~` (bitwise not)

Below are a set of scripts that explains the usage of bitwise operators:

**Bitwise and `&`:**

```python
a = 5   # 101 in binary
b = 3   # 011 in binary

result = a & b
print(result)  # Output: 1 (001 in binary)
```

**Bitshift left `<<`:**

```python
x = 3   # 11 in binary

result = x << 2
print(result)  # Output: 12 (1100 in binary)
```

**Bitshift right `>>`:**

```python
y = 16  # 10000 in binary

result = y >> 2
print(result)  # Output: 4 (100 in binary)
```

**Bitwise xor `^`:**

```python
p = 12  # 1100 in binary
q = 7   # 0111 in binary

result = p ^ q
print(result)  # Output: 11 (1011 in binary)
```

**Bitwise or `|`:**

```python
m = 10  # 1010 in binary
n = 5   # 0101 in binary

result = m | n
print(result)  # Output: 15 (1111 in binary)
```

**Bitwise not `~`:**

```python
z = 7   # 0111 in binary

result = ~z
print(result)  # Output: -8 (1000 in two's complement binary)
```

### Compound Operators

A compound operator combines an arithmetic or bitwise operation with an assignment. For example, instead of writing `x = x +3`, you can write `x += 3`, using the compound addition (+) operator. 

The following compound operators are available:

- `%=` (compound remainder)
- `&=` (compound bitwise and)
- `*=` (compound multiplication)
- `+=` (compound addition)
- `-=` (compound subtraction)
- `/=` (compound division)
- `^=` (compound bitwise xor)
- `|=` (compound bitwise or)

***Please note that increment `++` and decrement `--` are not available in the Python language. The equalivent is `x +=1` and `x -=1`.**

Below are a set of scripts that explains the usage of compound operators:

**Compound remainder `%=`:**

```python
a = 15
b = 7

a %= b
print(a)  # Output: 1 (15 % 7)
```

**Compound bitwise and `&=`:**

```python
x = 5
y = 3

x &= y
print(x)  # Output: 1 (5 & 3)
```

**Compound multiplication `*=`:**

```python
num = 8

num *= 3
print(num)  # Output: 24 (8 * 3)
```

**Compound addition `+=`:**

```python
total = 10

total += 5
print(total)  # Output: 15 (10 + 5)
```

**Compound subtraction `-=`:**

```python
result = 20

result -= 8
print(result)  # Output: 12 (20 - 8)
```

**Compound division `/=`:**

```python
value = 30

value /= 6
print(value)  # Output: 5.0 (30 / 6)
```

**Compound bitwise xor `^=`:**

```python
m = 12
n = 7

m ^= n
print(m)  # Output: 11 (12 ^ 7)
```

**Compound bitwise or `|=`:**

```python
p = 10
q = 5

p |= q
print(p)  # Output: 15 (10 | 5)
```
