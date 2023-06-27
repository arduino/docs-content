---
author: 'Hannes Siebeneicher'
hero_image: "./hero-banner.png"
micropython_type: "101"
featured: micropython-101
title: 'Component Examples'
description: 'Practical examples for Neopixels, sensors, servo motors and more.'
---

## Button

This example shows how to use a pushbutton with MicroPython.

| Arduino        | Button        |
| -------------- | ------------- |
| Signal         | Pin 5 (D2)    |
| 3.3 V / 5 V    | +             |
| GND            | -             |

```python
from machine import Pin
from time import sleep

button = Pin(5, Pin.IN, Pin.PULL_UP)

while True:
    button_state = button.value()
    if button_state == 0:
        print("Button not pressed")
    else:
        print("Button pressed")
    sleep(0.5)
```

## LED

This example shows how to create the classic blink example using MicroPython.

| Arduino        | Button        |
| -------------- | ------------- |
| LED            | Pin 5 (D2)    |
| GND            | -             |

```python
from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)

while(True):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

## Servo

This code controls a servo motor connected to Pin 5 (D2) using PWM. As with any motor if the current being drawn due to the motor needing too much power the board resets.

| Arduino        | Line Finder   |
| -------------- | ------------- |
| Signal         | Pin 5 (D2)    |
| 3.3 V / 5 V    | +             |
| GND            | -             |

```python
from machine import Pin,PWM
import time

servo = PWM(Pin(5, mode=Pin.OUT))
servo.freq(50)

while True:
    servo.duty(26)
    time.sleep(1)
    servo.duty(123)
    time.sleep(1)
```

## Neopixel

This example shows how to use a Neopixel strip with 10 RGB leds.

| Arduino        | RGB Strip     |
| -------------- | ------------- |
| Signal         | Pin 5 (D2)    |
| 3.3 V / 5 V    | +             |
| GND            | -             |


```python
# NeoPixel driver for MicroPython
# MIT license; Copyright (c) 2016 Damien P. George, 2021 Jim Mussared

from machine import bitstream
class NeoPixel:
    # G R B W
    ORDER = (1, 0, 2, 3)

    def __init__(self, pin, n, bpp=3, timing=1):
        self.pin = pin
        self.n = n
        self.bpp = bpp
        self.buf = bytearray(n * bpp)
        self.pin.init(pin.OUT)
        # Timing arg can either be 1 for 800kHz or 0 for 400kHz,
        # or a user-specified timing ns tuple (high_0, low_0, high_1, low_1).
        self.timing = (
            ((400, 850, 800, 450) if timing else (800, 1700, 1600, 900))
            if isinstance(timing, int)
            else timing
        )

    def __len__(self):
        return self.n

    def __setitem__(self, i, v):
        offset = i * self.bpp
        for i in range(self.bpp):
            self.buf[offset + self.ORDER[i]] = v[i]

    def __getitem__(self, i):
        offset = i * self.bpp
        return tuple(self.buf[offset + self.ORDER[i]] for i in range(self.bpp))

    def fill(self, v):
        b = self.buf
        l = len(self.buf)
        bpp = self.bpp
        for i in range(bpp):
            c = v[i]
            j = self.ORDER[i]
            while j < l:
                b[j] = c
                j += bpp

    def write(self):
        # BITSTREAM_TYPE_HIGH_LOW = 0
        bitstream(self.pin, 0, self.timing, self.buf)
```

## DHT11

This example shows how to use a DHT11 with an Arduino Nano ESP32.

| Arduino        | DHT11         |
| -------------- | ------------- |
| Signal         | Pin 5 (D2)    |
| 3.3 V / 5 V    | +             |
| GND            | -             |

```python
import dht
from machine import Pin
from time import sleep_ms

SENSOR_PIN = 5

TEMP_SENSOR = dht.DHT11(Pin(SENSOR_PIN))
sleep_ms(500)

while(1):
    TEMP_SENSOR.measure()
    print(TEMP_SENSOR.temperature())
    print(TEMP_SENSOR.humidity())
    sleep_ms(1000)

```

## OLED Screen

This example shows how to use an OLED screen via I2C.

| Arduino        | Oled_Button               |
| -------------- | ------------------------- |
| Oled           | SDA=8(D5), SCL=9(D6)      |
| 3.3 V / 5 V    | +                         |
| GND            | -                         |

```python
from machine import SoftI2C, Pin
import ssd1306_1315 as ssd1306
import gc
from random import randint
from time import sleep_ms
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coords(coords):
        return
old_coords = Point(64, 32)
new_coords = Point(64, 32)
# old_coords = ["x": 0, "y":0]
# new_coords = ["x": 0, "y": 0]
i2cbus = SoftI2C(scl = Pin(9), sda = Pin(8), freq = 100000)
print(i2cbus)
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2cbus)
# oled.fill(0)
oled.show()
oled.text('Arduino', 40, 12)
oled.text('vs', 60, 26)
oled.text('MicroPython', 23, 45)
oled.show()

```

## Buzzer

This example shows how to use a Grove Buzzer.

| Arduino        | Buzzer        |
| -------------- | ------------- |
| Signal         | Pin 5 (D2)    |
| 3.3 V / 5 V    | +             |
| GND            | -             |

```python
from machine import Pin, PWM
import time

# Pin connected to the Grove Speaker
SPEAKER_PIN = 5

# Frequency and duration of the sound
FREQUENCY = 220  # Hz
DURATION = 2  # seconds

# Create a controllable Pin for the speaker
speaker = PWM(Pin(SPEAKER_PIN))

# Function to play a sound
def play_sound(frequency, duration):
    speaker.freq(frequency)
    speaker.duty(512)
    time.sleep(duration)
    speaker.duty(0)

# Play the sound
play_sound(FREQUENCY, DURATION)
```

## Accelerometer

This example shows how to use a Grove Accelerometer using I2C.

| Arduino        | Accelerometer              |
| -------------- | -------------------------- |
| Signal         |sda=8 (D5), scl=9 (D6)      |
| 3.3 V / 5 V    | +                          |
| GND            | -                          |

```python
import lis3dh, time, math
from machine import Pin, I2C

i2c = I2C(sda=Pin(8), scl=Pin(9)) # Correct I2C pins for TinyPICO
imu = lis3dh.LIS3DH_I2C(i2c, address=0x19)

last_convert_time = 0
convert_interval = 100 #ms
pitch = 0
roll = 0


# Convert acceleration to Pitch and Roll
def convert_accell_rotation( vec ):
    x_Buff = vec[0] # x
    y_Buff = vec[1] # y
    z_Buff = vec[2] # z

    global last_convert_time, convert_interval, roll, pitch

    # We only want to re-process the values every 100 ms
    if last_convert_time < time.ticks_ms():
        last_convert_time = time.ticks_ms() + convert_interval

        roll = math.atan2(y_Buff , z_Buff) * 57.3
        pitch = math.atan2((- x_Buff) , math.sqrt(y_Buff * y_Buff + z_Buff * z_Buff)) * 57.3

    # Return the current values in roll and pitch
    return ( roll, pitch )

# If we have found the LIS3DH
if imu.device_check():
    # Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
    imu.range = lis3dh.RANGE_2_G

    # Loop forever printing values
    while True:
        # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
        # z axis values.  Divide them by 9.806 to convert to Gs.
        x, y, z = [value / lis3dh.STANDARD_GRAVITY for value in imu.acceleration]
        print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))

        # Convert acceleration to Pitch and Roll and print values
        p, r = convert_accell_rotation( imu.acceleration )
        print("pitch = %0.2f, roll = %0.2f" % (p,r))

        # Small delay to keep things responsive but give time for interrupt processing.
        time.sleep(0.1)
```

## Sound Sensor

This example shows how to use a sound sensor.

| Arduino        | Sound Sensor  |
| -------------- | ------------- |
| Signal         | Pin 5 (D2)    |
| 3.3 V / 5 V    | +             |
| GND            | -             |

```python
from machine import Pin, ADC
import time

pin_adc = ADC(Pin(5))
pin_adc.atten(ADC.ATTN_11DB)

while True:
    sum_value = 0
    for i in range(32):
        sum_value += pin_adc.read()

    sum_value >>= 5

    print(sum_value)
    time.sleep_ms(100)

```

## 4 Digit Display

This example shows how to use a Grove 4-digit display.

| Arduino        | Display                    |
| -------------- | -------------------------- |
| Signal         |clk=12 (A5), dio=11 (A4)    |
| 3.3 V / 5 V    | +                          |
| GND            | -                          |

```python
from machine import Pin
from time import sleep
import tm1637

tm = tm1637.TM1637(clk=Pin(10), dio=Pin(11))

tm.write([63, 191, 63, 63])
sleep(1)

tm.numbers(17,23)
sleep(1)
tm.show('abcd')
sleep(1)
tm.show('bcde')
sleep(1)
tm.show('cdef')
sleep(1)

tm.temperature(20)
```

## Moisture Sensor

This example shows how to use a moisture sensor.

| Arduino        | Moisture Sensor  |
| -------------- | ---------------- |
| Signal         | Pin 5 (D2)       |
| 3.3 V / 5 V    | +                |
| GND            | -                |

```python
import machine
import time

adc_pin = machine.Pin(4)
adc = machine.ADC(adc_pin)

#function mapping sensor values from 0 to 100.
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    reading = adc.read_u16()
    mapped_reading = map_value(reading, 0, 65535, 0, 100)  # Mapping the reading to the range 0-100
    print("Moisture: ", reading, " Mapped Moisture: ", mapped_reading)
    time.sleep_ms(500)
```