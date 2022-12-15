---
author: 'Karl Söderby'
title: 'Nano 33 BLE Sense Python® Guide'
description: 'Discover how to access the features on the Nano 33 BLE Sense using Python® scripts.'
compatible-products: [nano-33-ble-sense]
tags: 
  - MicroPython
  - OpenMV
---

![The Nano 33 BLE Sense](assets/hero.png)

The [Nano 33 BLE Sense board](https://store.arduino.cc/arduino-nano-33-ble-sense) board can be programmed using the popular **Python®** programming language. More specifically, it supports [OpenMV's fork of MicroPython](https://github.com/openmv/micropython), where MicroPython is an implementation of the Python® language, designed to run on microcontrollers. In this article, you will find a lot of sample scripts that will work directly with your Nano 33 BLE Sense, such as general GPIO control, reading onboard sensors and Wi-Fi/BLE communication!

- If you want to read more about Arduino & Python®, you can visit the [Python® with Arduino](/learn/programming/arduino-and-python) article. Here you will find a lot of useful examples, such as how to use delays, interrupts, reading pins and more general functions.

## Hardware & Software Needed

- [Arduino Nano 33 BLE Sense](https://store.arduino.cc/nano-33-ble-sense).
- [OpenMV IDE](https://openmv.io/pages/download)

***This guide does not cover the installation of OpenMV and MicroPython on your board. Please refer to [Getting started with OpenMV and Nano 33 BLE Sense](/tutorials/nano-33-ble-sense/getting-started-omv) for a detailed guide.***   

## API

Below you will find a lot of useful examples that can be loaded to your Nano 33 BLE Sense board. Many of these examples were extracted from the [OpenMV repository](https://github.com/openmv/openmv), where you can find many useful examples for other boards as well.

***In this article, you will only find examples for the Nano 33 BLE Sense board. For more information on how to use delays, read and write to pins, please refer to the [Python® with Arduino](/learn/programming/arduino-and-python) main article.***

## Pin Control

The pinout for the **Nano 33 BLE Sense** and the **NRF52840 microcontroller** varies greatly. For example, if we are to use `D2` according to the Arduino pinout, we would actually need to use **pin 43**.

```python
# Defining "D2" on the Nano 33 BLE Sense
p0 = Pin(43, Pin.OUT)
```

***In the MicroPython port of the Nano 33 BLE Sense board, the pinout is the same as the Nordic NRF52840 (the microcontroller). You will find a pin map below this section that explains how to address the different pins.***

### Pin Map

Before you start using the board's pins, it might be a good idea to check out the table below to understand the relationship between Arduino's pinout and the NRF52840's pinout.

| Arduino | nRF52840 |
| ------- | -------- |
| TX      | 35       |
| RX      | 42       |
| D2      | 43       |
| D3      | 44       |
| D4      | 47       |
| D5      | 45       |
| D6      | 46       |
| D7      | 23       |
| D8      | 21       |
| D9      | 27       |
| D10     | 34       |
| D11     | 33       |
| D12     | 40       |
| D13     | 13       |
| D14/A0  | 4        |
| D15/A1  | 5        |
| D16/A2  | 30       |
| D17/A3  | 29       |
| D18/A4  | 31       |
| D19/A5  | 2        |
| D20/A6  | 28       |
| D21/A7  | 3        |

### Analog Pins

To read the analog pins on the Nano BLE Sense, we can choose from the following pins:

- A0 - `4` 
- A1 - `5` 
- A2 - `30`
- A3 - `29`
- A4 - `31`
- A5 - `2` 
- A6 - `28`
- A7 - `3` 

To define them, we need to import the `machine` module, and define the pin as follows: 

```python
import machine

adc_pin = machine.Pin(29)
adc = machine.ADC(adc_pin)
```

To read the analog pin, simply use:

```python
reading = adc.read_u16() #16-bit resolution (0-65535)
```

The below script will read the `A3` pin on the Arduino Nano BLE Sense and print the value in the terminal.

```python
import machine
import time

adc_pin = machine.Pin(29) # A3
adc = machine.ADC(adc_pin)

while True:
    reading = adc.read_u16()     
    print("ADC: ",reading)
    time.sleep_ms(500)
```

## LED Control

There are 3 different LEDs that can be accessed on the Nano BLE Sense: **RGB, the built-in LED** and the **power LED**.

They can be accessed by importing the `LED` module, where the RGB and built-in LED can be accessed.

```python
from board import LED

led_red = LED(1) # red LED
led_green = LED(2) # green LED
led_blue = LED(3) # blue LED
led_builtin = LED(4) # classic built-in LED (also accessible through pin 13)
```

To access the **power LED** we need to import the `Pin` module.

```python
from machine import Pin

led_pwr = Pin(41, Pin.OUT)
```

### RGB

Blink all RGB lights every 0.25 seconds.  

```python
from board import LED
import time 

led_red = LED(1)
led_green = LED(2)
led_blue = LED(3)

while (True):
   
    # Turn on LEDs
    led_red.on()
    led_green.on()
    led_blue.on()

    # Wait 0.25 seconds
    time.sleep_ms(250)
    
    # Turn off LEDs
    led_red.off()
    led_green.off()
    led_blue.off()

    # Wait 0.25 seconds
    time.sleep_ms(250)
```

### Built-in LED

The classic blink example! Blink the built-in LED every 0.25 seconds.

```python
from board import LED
import time 

led_builtin = LED(4)

while (True):
   
    # Turn on LED
    led_builtin.on()

    # Wait 0.25 seconds
    time.sleep_ms(250)
    
    # Turn off LED
    led_builtin.off()

    # Wait 0.25 seconds
    time.sleep_ms(250)

```

## Sensors

There are several sensors onboard the Nano 33 BLE Sense. The scripts below can be used to access the data from each of them.

### IMU (LSM9DS1)

Access the `accelerometer`, `magnetometer`, and `gyroscope` data from the LSM9DS1 IMU module.

```python
import time
import lsm9ds1
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
lsm = lsm9ds1.LSM9DS1(bus)

while (True):
    #for g,a in lsm.iter_accel_gyro(): print(g,a)    # using fifo
    print('Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*lsm.read_accel()))
    print('Magnetometer:  x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*lsm.read_magnet()))
    print('Gyroscope:     x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*lsm.read_gyro()))
    print("")
    time.sleep_ms(500)
```


### Temperature & Humidity (HTS221)

Access the `temperature` & `humidity` values from the HTS221 sensor.

```python
import time
import hts221
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
hts = hts221.HTS221(bus)

while (True):
    rH   = hts.humidity()
    temp = hts.temperature()
    print ("rH: %.2f%% T: %.2fC" %(rH, temp))
    time.sleep_ms(100)
```

### Pressure (LPS22)

Access the `pressure` values from the LPS22 sensor.

```python
import time
import lps22h
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
lps = lps22h.LPS22H(bus)

while (True):
    pressure = lps.pressure()
    temperature = lps.temperature()
    print("Pressure: %.2f hPa Temperature: %.2f C"%(pressure, temperature))
    time.sleep_ms(100)
```

### Ambient Light (APDS9960)

Access the `Ambient Light` values from the APDS9960 sensor.

```python
from time import sleep_ms
from machine import Pin, I2C
from apds9960.const import *
from apds9960 import uAPDS9960 as APDS9960

bus = I2C(1, sda=Pin(13), scl=Pin(14))
apds = APDS9960(bus)

print("Light Sensor Test")
print("=================")
apds.enableLightSensor()

while True:
    sleep_ms(250)
    val = apds.readAmbientLight()
    print("AmbientLight={}".format(val))
```

### Proximity (APDS9960)

Access the `Proximity values` from the APDS9960 sensor.

```python
from time import sleep_ms
from machine import Pin, I2C

from apds9960.const import *
from apds9960 import uAPDS9960 as APDS9960

bus = I2C(1, sda=Pin(13), scl=Pin(14))
apds = APDS9960(bus)

apds.setProximityIntLowThreshold(50)

print("Proximity Sensor Test")
print("=====================")
apds.enableProximitySensor()

while True:
    sleep_ms(250)
    val = apds.readProximity()
    print("proximity={}".format(val))
```

### Microphone (MP34DT05)

Below example can be used with OpenMV's frame buffer window (top right corner).

```python
import image, audio, time
from ulab import numpy as np
from ulab import scipy as sp

CHANNELS = 1
SIZE = 256//(2*CHANNELS)

raw_buf = None
fb = image.Image(SIZE+50, SIZE, image.RGB565, copy_to_fb=True)
audio.init(channels=CHANNELS, frequency=16000, gain_db=80, highpass=0.9883)

def audio_callback(buf):
    # NOTE: do Not call any function that allocates memory.
    global raw_buf
    if (raw_buf == None):
        raw_buf = buf

# Start audio streaming
audio.start_streaming(audio_callback)

def draw_fft(img, fft_buf):
    fft_buf = (fft_buf / max(fft_buf)) * SIZE
    fft_buf = np.log10(fft_buf + 1) * 20
    color = (0xFF, 0x0F, 0x00)
    for i in range(0, SIZE):
        img.draw_line(i, SIZE, i, SIZE-int(fft_buf[i]), color, 1)

def draw_audio_bar(img, level, offset):
    blk_size = SIZE//10
    color = (0xFF, 0x00, 0xF0)
    blk_space = (blk_size//4)
    for i in range(0, int(round(level/10))):
        fb.draw_rectangle(SIZE+offset, SIZE - ((i+1)*blk_size) + blk_space, 20, blk_size - blk_space, color, 1, True)

while (True):
    if (raw_buf != None):
        pcm_buf = np.frombuffer(raw_buf, dtype=np.int16)
        raw_buf = None

        if CHANNELS == 1:
            fft_buf = sp.signal.spectrogram(pcm_buf)
            l_lvl = int((np.mean(abs(pcm_buf[1::2])) / 32768)*100)
        else:
            fft_buf = sp.signal.spectrogram(pcm_buf[0::2])
            l_lvl = int((np.mean(abs(pcm_buf[1::2])) / 32768)*100)
            r_lvl = int((np.mean(abs(pcm_buf[0::2])) / 32768)*100)

        fb.clear()
        draw_fft(fb, fft_buf)
        draw_audio_bar(fb, l_lvl, 0)
        if CHANNELS == 2:
            draw_audio_bar(fb, r_lvl, 25)
        fb.flush()

# Stop streaming
audio.stop_streaming()
```

## Bluetooth® Low Energy

This example allows us to connect to our board via our phone, and control the built-in LED.  We recommend using the **nRF Connect** applications.

- [nRF desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop)
- [nRF mobile](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-mobile)

***After loading the script below, your board should be listed as "Nano 33 BLE Sense" in the list of available devices. You need to pair in order to control the built-in LED.*** 

```python
# Use nRF Connect from App store, connect to the Nano and write 1/0 to control the LED.

import time
from board import LED
from ubluepy import Service, Characteristic, UUID, Peripheral, constants

def event_handler(id, handle, data):
    global periph
    global service
    if id == constants.EVT_GAP_CONNECTED:
        pass
    elif id == constants.EVT_GAP_DISCONNECTED:
        # restart advertisement
        periph.advertise(device_name="Nano 33 BLE Sense", services=[service])
    elif id == constants.EVT_GATTS_WRITE:
        LED(1).on() if int(data[0]) else LED(1).off()

# start off with LED(1) off
LED(1).off()

notif_enabled = False
uuid_service = UUID("0x1523")
uuid_led     = UUID("0x1525")

service = Service(uuid_service)
char_led = Characteristic(uuid_led, props=Characteristic.PROP_WRITE)
service.addCharacteristic(char_led)

periph = Peripheral()
periph.addService(service)
periph.setConnectionHandler(event_handler)
periph.advertise(device_name="Nano 33 BLE Sense", services=[service])

while (True):
    time.sleep_ms(500)
```

## Summary

In this article we have gone through a selection of scripts that will help you control your Nano BLE Sense board, via the OpenMV IDE. Feel free to check out our [Python® with Arduino boards article](/learn/programming/arduino-and-python), where you can find guides to other boards, useful links to learn Python® and more.
