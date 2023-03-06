---
author: 'Karl Söderby'
title: 'Nano 33 BLE Python® Guide'
description: 'Discover how to access the features on the Nano 33 BLE using Python® scripts.'
compatible-products: [nano-33-ble]
tags: 
  - MicroPython
  - OpenMV
featuredImage: 'board'
---

![The Nano 33 BLE](assets/hero.png)

The [Nano 33 BLE](https://store.arduino.cc/arduino-nano-33-ble-sense) board can be programmed using the popular **Python®** programming language. More specifically, it supports [OpenMV's fork of MicroPython](https://github.com/openmv/micropython), where MicroPython is an implementation of the Python® language, designed to run on microcontrollers. In this article, you will find a lot of sample scripts that will work directly with your Nano 33 BLE, such as general GPIO control, reading data from the IMU module and testing Bluetooth® Low Energy connection.

- If you want to read more about Arduino & Python®, you can visit the [Python® with Arduino](/learn/programming/arduino-and-python) article. Here you will find a lot of useful examples, such as how to use delays, interrupts, reading pins and more general functions.

***If you are looking for information related to the similar Nano 33 BLE Sense board, you can refer to the [Nano 33 BLE Sense Python® Guide](/tutorials/nano-33-ble-sense/ble-sense-python-api).***

## Hardware & Software Needed

- [Arduino Nano 33 BLE](https://store.arduino.cc/nano-33-ble).
- [OpenMV IDE](https://openmv.io/pages/download)

***This guide does not cover the installation of OpenMV and MicroPython on your board. Please refer to [Getting started with OpenMV and Nano 33 BLE](/tutorials/nano-33-ble/getting-started-omv) for a detailed guide.***   

## API

Below you will find a lot of useful examples that can be loaded to your Nano 33 BLE board. Many of these examples were extracted from the [OpenMV repository](https://github.com/openmv/openmv), where you can find many useful examples for other boards as well.

***In this article, you will only find examples for the Nano 33 BLE board. For more information on how to use delays, read and write to pins, please refer to the [Python® with Arduino](/learn/programming/arduino-and-python) main article.***

## Pin Control

The pinout for the **Nano 33 BLE** and the **NRF52840 microcontroller** varies greatly. For example, if we are to use `D2` according to the Arduino pinout, we would actually need to use **pin 43**.

```python
# Defining "D2" on the Nano 33 BLE
p0 = Pin(43, Pin.OUT)
```

***In the MicroPython port of the Nano 33 BLE board, the pinout is the same as the Nordic NRF52840 (the microcontroller). You will find a GPIO Map below this section that explains how to address the different pins.***

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

To read the analog pins on the Nano BLE , we can choose from the following pins:

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

The below script will read the `A3` pin on the board and print the value in the terminal.

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

There are 3 different LEDs that can be accessed on the Nano BLE: **RGB, the built-in LED** and the **power LED**.

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

## IMU (LSM9DS1)

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



## Bluetooth® Low Energy

This example allows us to connect to our board via our phone, and control the built-in LED.  We recommend using the **nRF Connect** applications.

- [nRF desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop)
- [nRF mobile](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-mobile)

***After loading the script below, your board should be listed as "Nano 33 BLE" in the list of available devices. You need to pair in order to control the built-in LED.*** 

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
        periph.advertise(device_name="Nano 33 BLE", services=[service])
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
periph.advertise(device_name="Nano 33 BLE", services=[service])

while (True):
    time.sleep_ms(500)
```

## Summary

In this article we have gone through a selection of scripts that will help you control your Nano BLE board, via the OpenMV IDE. Feel free to check out our [Python® with Arduino boards article](/learn/programming/arduino-and-python), where you can find guides to other boards, useful links to learn Python® and more.
