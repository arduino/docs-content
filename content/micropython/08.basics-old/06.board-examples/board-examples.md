---
title: Examples by Board
description: Find examples that work only with specific boards, such as reading built-in sensors.
author: Karl Söderby
micropython_type: basics
featured: micropython
hero_image: "./hero-banner.png"
---

In this article, you will find examples that works only with specific boards. Each board also has a GPIO map that explains how each pin can be addressed.

## Nano RP2040 Connect

![Nano RP2040 Connect.](assets/nano-rp2040.png)

### GPIO Map

The pinout for the **Nano RP2040 Connect** and the **RP2040 microcontroller** varies greatly. For example, if we are to use `D2` according to the Arduino pinout, we would actually need to use **pin 25**.

```python
# Defining "D2" on the Arduino Nano RP2040 Connect
p0 = Pin(25, Pin.OUT)
```

Before you start using the board's pins, it might be a good idea to check out the table below to understand the relationship between Arduino's pinout and the RP2040's pinout.

| Arduino | RP2040 | Usage         |
| ------- | ------ | ------------- |
| TX      | GPIO0  | UART/TX       |
| RX      | GPIO1  | UART/RX       |
| D2      | GPIO25 | GPIO          |
| D3      | GPIO15 | GPIO          |
| D4      | GPIO16 | GPIO          |
| D5      | GPIO17 | GPIO          |
| D6      | GPIO18 | GPIO          |
| D7      | GPIO19 | GPIO          |
| D8      | GPIO20 | GPIO          |
| D9      | GPIO21 | GPIO          |
| D10     | GPIO5  | GPIO          |
| D11     | GPIO7  | SPI/COPI      |
| D12     | GPIO4  | SPI/CIPO      |
| D13     | GPIO6  | SPI/SCK       |
| D14/A0  | GPIO26 | ADC/RP2040    |
| D15/A1  | GPIO27 | ADC/RP2040    |
| D16/A2  | GPIO28 | ADC/RP2040    |
| D17/A3  | GPIO29 | ADC/RP2040    |
| D18/A4  | GPIO12 | I2C           |
| D19/A5  | GPIO13 | I2C           |
| D20/A6  | GPIO36 | ADC/NINA-W102 |
| D21/A7  | GPIO35 | ADC/NINA-W102 |

### Analog Read

***Note: This is currently only available on the nightly build. Follow [this link](https://docs.arduino.cc/micropython/#firmware) to download it.***

To read an analog pin, we can use the `ADC.read_u16` command. This reads the specified analog pin and returns an integer in the range 0 - 65535. For this, we need to import `ADC` from the `machine` module.

```python
from machine import ADC

while True:
    adc = ADC("A4")
    adc.read_u16()
```

### Sensors

#### IMU (LSM6DSOX)

Prints the accelerometer and gyroscope values in the Serial Monitor.

```python
import time
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C

# Initialize the LSM6DSOX sensor with I2C interface
lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))

while True:
    # Read accelerometer values
    accel_values = lsm.accel()
    print('Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*accel_values))
    
    # Read gyroscope values
    gyro_values = lsm.gyro()
    print('Gyroscope:     x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*gyro_values))
    
    print("")
    time.sleep_ms(100)
```

### Microphone (MP34DT05)

Below example can be used with OpenMV's frame buffer window (top right corner).

```python
import image, audio, time
from ulab import numpy as np
from ulab import scipy as sp

CHANNELS = 1
FREQUENCY = 32000
N_SAMPLES = 32 if FREQUENCY == 16000 else 64
SCALE = 2
SIZE = (N_SAMPLES * SCALE) // CHANNELS

raw_buf = None
fb = image.Image(SIZE+(50*SCALE), SIZE, image.RGB565, copy_to_fb=True)
audio.init(channels=CHANNELS, frequency=FREQUENCY, gain_db=16)

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
    for i in range(0, len(fft_buf)):
        img.draw_line(i*SCALE, SIZE, i*SCALE, SIZE-int(fft_buf[i]) * SCALE, color, SCALE)

def draw_audio_bar(img, level, offset):
    blk_size = (SIZE//10)
    color = (0xFF, 0x00, 0xF0)
    blk_space = (blk_size//4)
    for i in range(0, int(round(level/10))):
        fb.draw_rectangle(SIZE+offset, SIZE - ((i+1)*blk_size) + blk_space, 20 * SCALE, blk_size - blk_space, color, 1, True)

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
        draw_audio_bar(fb, l_lvl, 25*SCALE)
        if CHANNELS == 2:
            draw_audio_bar(fb, r_lvl, 25 * SCALE)
        fb.flush()

# Stop streaming
audio.stop_streaming()
```

### Communication

#### I2C

Scans for devices connected to the I2C buses:

```python
import time
from machine import Pin, I2C

i2c_list    = [None, None]
i2c_list[0] = I2C(0, scl=Pin(13), sda=Pin(12), freq=100_000)
i2c_list[1] = I2C(1, scl=Pin(7), sda=Pin(6), freq=100_000)

for bus in range(0, 2):
    print("\nScanning bus %d..."%(bus))
    for addr in i2c_list[bus].scan():
        print("Found device at address %d:0x%x" %(bus, addr))
```

#### UART

To read data and write data through TX and RX pins, you can use `uart.write()` and `uart.read()`.

```python
from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
   uart.write('hello') # writes 5 bytes
   val = uart.read(5)  # reads up to 5 bytes
   print(val) # prints data
   time.sleep(1)
```

### Wireless

Below are examples on wireless connectivity, using the NINA-W102 module onboard the Nano RP2040 Connect. 

***In order to use these examples, you may have to upgrade your firmware. You can find instructions on how to in [Upgrading Nano RP2040 Connect NINA firmware](/tutorials/nano-rp2040-connect/rp2040-upgrading-nina-firmware).***

#### Wi-Fi AP Mode

Turn your board into an access point:

```python
# Wi-Fi AP Mode Example
#
# This example shows how to use Wi-Fi in Access Point mode.
import network, socket, sys, time, gc

SSID ='My_Nano_RP2040_Connect'   # Network SSID
KEY  ='1234567890'  # Network key (must be 10 chars)
HOST = ''           # Use first available interface
PORT = 8080         # Arbitrary non-privileged port

# Init wlan module and connect to network
wlan = network.WLAN(network.AP_IF)
wlan.active(True)
wlan.config(essid=SSID, key=KEY, security=wlan.WEP, channel=2)
print("AP mode started. SSID: {} IP: {}".format(SSID, wlan.ifconfig()[0]))

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            raise OSError("Timeout")
        data.extend(packet)
    return data

def start_streaming(server):
    print ('Waiting for connections..')
    client, addr = server.accept()

    # set client socket timeout to 5s
    client.settimeout(5.0)
    print ('Connected to ' + addr[0] + ':' + str(addr[1]))

    # FPS clock
    clock = time.clock()
    while (True):
        try:
            # Read data from client
            data = recvall(client, 1024)
            # Send it back
            client.send(data)
        except OSError as e:
            print("start_streaming(): socket error: ", e)
            client.close()
            break

while (True):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind and listen
        server.bind([HOST, PORT])
        server.listen(1)

        # Set server socket to blocking
        server.setblocking(True)
        while (True):
            start_streaming(server)
    except OSError as e:
        server.close()
        print("Server socket error: ", e)
```

#### Wi-Fi® Scan

To scan available networks:

```python
# Scan Example

# This example shows how to scan for Wi-Fi networks.

import time, network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Scanning...")
while (True):
    scan_result = wlan.scan()
    for ap in scan_result:
        print("Channel:%d RSSI:%d Auth:%d BSSID:%s SSID:%s"%(ap))
    print()
    time.sleep_ms(1000)
```

#### HTTP Request

Making an HTTP request (in this case to google):

***Remember to enter your network name and password inside the SSID and KEY variables.***

```python
import network, socket

# AP info
SSID='' # Network SSID
KEY=''  # Network key

PORT = 80
HOST = "www.google.com"

# Init wlan module and connect to network
print("Trying to connect. Note this may take a while...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, KEY)

# We should have a valid IP now via DHCP
print("Wi-Fi Connected ", wlan.ifconfig())

# Get addr info via DNS
addr = socket.getaddrinfo(HOST, PORT)[0][4]
print(addr)

# Create a new socket and connect to addr
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

# Set timeout
client.settimeout(3.0)

# Send HTTP request and recv response
client.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%(HOST))
print(client.recv(1024))

# Close socket
client.close()
```

#### NTP (Network Time Protocol)

***Remember to enter your network name and password inside the SSID and KEY variables.***

Obtain accurate time and date from the Internet:

```python
# NTP Example
#
# This example shows how to get the current time using NTP

import network, usocket, ustruct, utime

# AP info
SSID='' # Network SSID
KEY=''  # Network key

TIMESTAMP = 2208988800

# Init wlan module and connect to network
print("Trying to connect... (may take a while)...")

wlan = network.WLAN()
wlan.active(True)
wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)

# We should have a valid IP now via DHCP
print(wlan.ifconfig())

# Create new socket
client = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
client.bind(("", 8080))
#client.settimeout(3.0)

# Get addr info via DNS
addr = usocket.getaddrinfo("pool.ntp.org", 123)[0][4]

# Send query
client.sendto('\x1b' + 47 * '\0', addr)
data, address = client.recvfrom(1024)

# Print time
t = ustruct.unpack(">IIIIIIIIIIII", data)[10] - TIMESTAMP
print ("Year:%d Month:%d Day:%d Time: %d:%d:%d" % (utime.localtime(t)[0:6]))
```

In the terminal, we should see it in this format:

```
Year:2021 Month:8 Day:10 Time: 7:56:30
```

#### Bluetooth® Low Energy

This example allows us to connect to our board via our phone, and control the built-in LED.  We recommend using the **nRF Connect** applications.

- [nRF desktop](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop)
- [nRF mobile](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-mobile)

***After loading the script below, your board should be listed as "Nano RP2040 Connect" in the list of available devices. You need to pair in order to control the built-in LED.*** 

```python
import bluetooth
import random
import struct
import time
from ble_advertising import advertising_payload
from machine import Pin
from micropython import const

LED_PIN = 6

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

_FLAG_READ = const(0x0002)
_FLAG_WRITE = const(0x0008)
_FLAG_NOTIFY = const(0x0010)
_FLAG_INDICATE = const(0x0020)

_SERVICE_UUID = bluetooth.UUID(0x1523)
_LED_CHAR_UUID = (bluetooth.UUID(0x1525), _FLAG_WRITE)
_LED_SERVICE = (_SERVICE_UUID, (_LED_CHAR_UUID,),)

class BLETemperature:
    def __init__(self, ble, name="NANO RP2040"):
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._handle,),) = self._ble.gatts_register_services((_LED_SERVICE,))
        self._connections = set()
        self._payload = advertising_payload(name=name, services=[_SERVICE_UUID])
        self._advertise()

    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            self._connections.remove(conn_handle)
            # Start advertising again to allow a new connection.
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            Pin(LED_PIN, Pin.OUT).value(int(self._ble.gatts_read(data[-1])[0]))
            
    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)

if __name__ == "__main__":
    ble = bluetooth.BLE()
    temp = BLETemperature(ble)
    
    while True:
        time.sleep_ms(1000)
```

## Nano 33 BLE

![Nano 33 BLE.](assets/ble.png)

### GPIO Map

The pinout for the **Nano 33 BLE** and the **NRF52840 microcontroller** varies greatly. For example, if we are to use `D2` according to the Arduino pinout, we would actually need to use **pin 43**.

```python
# Defining "D2" on the Nano 33 BLE
p0 = Pin(43, Pin.OUT)
```

In the MicroPython port of the Nano 33 BLE board, the pinout is the same as the Nordic NRF52840 (the microcontroller). You will find a GPIO Map below that explains how to address the different pins.

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

### Analog Read

***The following example is currently only possible with the nightly build***

### LED Control

There are 3 different LEDs that can be accessed on the Nano 33 BLE: **RGB, the built-in LED** and the **power LED**.

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

#### RGB

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

#### Built-in LED

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

### Sensors

#### IMU (LSM9DS1, BMI270 + BMM150)

Access the `accelerometer`, `magnetometer`, and `gyroscope` data from the IMU module.

```python
import time
import imu
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
imu = imu.IMU(bus)

while (True):
    print('Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*imu.accel()))
    print('Gyroscope:     x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*imu.gyro()))
    print('Magnetometer:  x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*imu.magnet()))
    print("")
    time.sleep_ms(100)
```

### Wireless

#### Bluetooth® Low Energy

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

## Nano 33 BLE Sense

![Nano 33 BLE Sense.](assets/ble-sense.png)

### Pin Map

The pinout for the **Nano 33 BLE Sense** and the **NRF52840 microcontroller** varies greatly. For example, if we are to use `D2` according to the Arduino pinout, we would actually need to use **pin 43**.

```python
# Defining "D2" on the Nano 33 BLE Sense
p0 = Pin(43, Pin.OUT)
```

In the MicroPython port of the Nano 33 BLE Sense board, the pinout is the same as the Nordic NRF52840 (the microcontroller). You will find a pin map below this section that explains how to address the different pins.

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


### LED Control

There are 3 different LEDs that can be accessed on the Nano 33 BLE Sense: **RGB, the built-in LED** and the **power LED**.

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

#### RGB

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

#### Built-in LED

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

### Sensors

There are several sensors onboard the Nano 33 BLE Sense. The scripts below can be used to access the data from each of them.

#### IMU (LSM9DS1, BMI270 + BMM150)

Access the `accelerometer`, `magnetometer`, and `gyroscope` data from the IMU module.

```python
import time
import imu
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
imu = imu.IMU(bus)

while (True):
    print('Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*imu.accel()))
    print('Gyroscope:     x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*imu.gyro()))
    print('Magnetometer:  x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*imu.magnet()))
    print("")
    time.sleep_ms(100)
```


#### Temperature & Humidity (HTS221)

Access the `temperature` & `humidity` values from the HTS221 sensor (Nano 33 BLE Sense).

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

#### Temperature & Humidity (HS3003)

Access the `temperature` & `humidity` values from the HTS221 sensor (Nano 33 BLE Sense Rev2).

```python
import time
from hs3003 import HS3003
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
hts = HS3003(bus)

while True:
    rH   = hts.humidity()
    temp = hts.temperature()
    print ("rH: %.2f%% T: %.2fC" %(rH, temp))
    time.sleep_ms(100)
```

#### Pressure (LPS22)

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

#### Ambient Light (APDS9960)

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

#### Proximity (APDS9960)

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

#### Microphone (MP34DT05)

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

### Wireless

#### Bluetooth® Low Energy

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

## Portenta H7

![Portenta H7.](assets/portenta.png)

***Note that the [Portenta H7 Lite](/hardware/portenta-h7-lite) and [Portenta H7 Lite Connected](/hardware/portenta-h7-lite-connected) boards are compatible with most examples listed here, as they are variations of the Portenta H7.***

### GPIO Map

Most of the pins are referred to via their port name or their function. Please refer to the list below to see which function corresponds to which port on the Portenta H7.

| Arduino          | STM32H747 |
| ---------------- | --------- |
| PA0              | PA0       |
| PA1              | PA1       |
| PA2              | PA2       |
| PA3              | PA3       |
| PA4              | PA4       |
| PA5              | PA5       |
| PA6              | PA6       |
| PA7              | PA7       |
| PA8              | PA8       |
| PA9              | PA9       |
| PA10             | PA10      |
| PA11             | PA11      |
| PA12             | PA12      |
| PA13             | PA13      |
| PA14             | PA14      |
| PA15             | PA15      |
| PB0              | PB0       |
| PB1              | PB1       |
| PB2              | PB2       |
| PB3              | PB3       |
| PB4              | PB4       |
| PB5              | PB5       |
| PB6              | PB6       |
| PB7              | PB7       |
| PB8              | PB8       |
| PB9              | PB9       |
| PB10             | PB10      |
| PB11             | PB11      |
| PB12             | PB12      |
| PB13             | PB13      |
| PB14             | PB14      |
| PB15             | PB15      |
| PC0              | PC0       |
| PC1              | PC1       |
| PC2              | PC2       |
| PC3              | PC3       |
| PC4              | PC4       |
| PC5              | PC5       |
| PC6              | PC6       |
| PC7              | PC7       |
| PC8              | PC8       |
| PC9              | PC9       |
| PC10             | PC10      |
| PC11             | PC11      |
| PC12             | PC12      |
| PC13             | PC13      |
| PC14             | PC14      |
| PC15             | PC15      |
| PD0              | PD0       |
| PD1              | PD1       |
| PD2              | PD2       |
| PD3              | PD3       |
| PD4              | PD4       |
| PD5              | PD5       |
| PD6              | PD6       |
| PD7              | PD7       |
| PD8              | PD8       |
| PD9              | PD9       |
| PD10             | PD10      |
| PD11             | PD11      |
| PD12             | PD12      |
| PD13             | PD13      |
| PD14             | PD14      |
| PD15             | PD15      |
| PE0              | PE0       |
| PE1              | PE1       |
| PE2              | PE2       |
| PE3              | PE3       |
| PE4              | PE4       |
| PE5              | PE5       |
| PE6              | PE6       |
| PE7              | PE7       |
| PE8              | PE8       |
| PE9              | PE9       |
| PE10             | PE10      |
| PE11             | PE11      |
| PE12             | PE12      |
| PE13             | PE13      |
| PE14             | PE14      |
| PE15             | PE15      |
| PF0              | PF0       |
| PF1              | PF1       |
| PF2              | PF2       |
| PF3              | PF3       |
| PF4              | PF4       |
| PF5              | PF5       |
| PF6              | PF6       |
| PF7              | PF7       |
| PF8              | PF8       |
| PF9              | PF9       |
| PF10             | PF10      |
| PF11             | PF11      |
| PF12             | PF12      |
| PF13             | PF13      |
| PF14             | PF14      |
| PF15             | PF15      |
| PG0              | PG0       |
| PG1              | PG1       |
| PG2              | PG2       |
| PG3              | PG3       |
| PG4              | PG4       |
| PG5              | PG5       |
| PG6              | PG6       |
| PG7              | PG7       |
| PG8              | PG8       |
| PG9              | PG9       |
| PG10             | PG10      |
| PG11             | PG11      |
| PG12             | PG12      |
| PG13             | PG13      |
| PG14             | PG14      |
| PG15             | PG15      |
| PH0              | PH0       |
| PH1              | PH1       |
| PH2              | PH2       |
| PH3              | PH3       |
| PH4              | PH4       |
| PH5              | PH5       |
| PH6              | PH6       |
| PH7              | PH7       |
| PH8              | PH8       |
| PH9              | PH9       |
| PH10             | PH10      |
| PH11             | PH11      |
| PH12             | PH12      |
| PH13             | PH13      |
| PH14             | PH14      |
| PH15             | PH15      |
| PI0              | PI0       |
| PI1              | PI1       |
| PI2              | PI2       |
| PI3              | PI3       |
| PI4              | PI4       |
| PI5              | PI5       |
| PI6              | PI6       |
| PI7              | PI7       |
| PI8              | PI8       |
| PI9              | PI9       |
| PI10             | PI10      |
| PI11             | PI11      |
| PI12             | PI12      |
| PI13             | PI13      |
| PI14             | PI14      |
| PI15             | PI15      |
| PJ0              | PJ0       |
| PJ1              | PJ1       |
| PJ2              | PJ2       |
| PJ3              | PJ3       |
| PJ4              | PJ4       |
| PJ5              | PJ5       |
| PJ6              | PJ6       |
| PJ7              | PJ7       |
| PJ8              | PJ8       |
| PJ9              | PJ9       |
| PJ10             | PJ10      |
| PJ11             | PJ11      |
| PJ12             | PJ12      |
| PJ13             | PJ13      |
| PJ14             | PJ14      |
| PJ15             | PJ15      |
| PK0              | PK0       |
| PK1              | PK1       |
| PK2              | PK2       |
| PK3              | PK3       |
| PK4              | PK4       |
| PK5              | PK5       |
| PK6              | PK6       |
| PK7              | PK7       |
| UART1_TX         | PA9       |
| UART1_RX         | PA10      |
| UART4_TX         | PA0       |
| UART4_RX         | PI9       |
| UART6_TX         | PG14      |
| UART6_RX         | PG9       |
| UART8_TX         | PJ8       |
| UART8_RX         | PJ9       |
| ETH_RMII_REF_CLK | PA1       |
| ETH_MDIO         | PA2       |
| ETH_RMII_CRS_DV  | PA7       |
| ETH_MDC          | PC1       |
| ETH_RMII_RXD0    | PC4       |
| ETH_RMII_RXD1    | PC5       |
| ETH_RMII_TX_EN   | PG11      |
| ETH_RMII_TXD0    | PG13      |
| ETH_RMII_TXD1    | PG12      |
| USB_HS_CLK       | PA5       |
| USB_HS_STP       | PC0       |
| USB_HS_NXT       | PH4       |
| USB_HS_DIR       | PI11      |
| USB_HS_D0        | PA3       |
| USB_HS_D1        | PB0       |
| USB_HS_D2        | PB1       |
| USB_HS_D3        | PB10      |
| USB_HS_D4        | PB11      |
| USB_HS_D5        | PB12      |
| USB_HS_D6        | PB13      |
| USB_HS_D7        | PB5       |
| USB_HS_RST       | PJ4       |
| USB_DM           | PA11      |
| USB_DP           | PA12      |
| BOOT0            | BOOT0     |
| DAC1             | PA4       |
| DAC2             | PA5       |
| LEDR             | PK5       |
| LEDG             | PK6       |
| LEDB             | PK7       |
| I2C1_SDA         | PB7       |
| I2C1_SCL         | PB6       |
| I2C3_SDA         | PH8       |
| I2C3_SCL         | PH7       |
| -WL_REG_ON       | PJ1       |
| -WL_HOST_WAKE    | PJ5       |
| -WL_SDIO_0       | PC8       |
| -WL_SDIO_1       | PC9       |
| -WL_SDIO_2       | PC10      |
| -WL_SDIO_3       | PC11      |
| -WL_SDIO_CMD     | PD2       |
| -WL_SDIO_CLK     | PC12      |
| -BT_RXD          | PF6       |
| -BT_TXD          | PA15      |
| -BT_CTS          | PF9       |
| -BT_RTS          | PF8       |
| -BT_REG_ON       | PJ12      |
| -BT_HOST_WAKE    | PJ13      |
| -BT_DEV_WAKE     | PJ14      |
| -QSPI2_CS        | PG6       |
| -QSPI2_CLK       | PF10      |
| -QSPI2_D0        | PD11      |
| -QSPI2_D1        | PD12      |
| -QSPI2_D2        | PF7       |
| -QSPI2_D3        | PD13      |


### I/O Pins

To access the I/O pins, you can use the `Pin` module from the `pyb` library.

```python
from pyb import Pin
```

To reference a pin on the Portenta, you can use the `Pin()` constructor. The first argument you have to provide is the pin you want to use. The second parameter, `mode`, can be set as: `Pin.IN`, `Pin.OUT_PP`, `Pin.OUT_OD`, `Pin.AF_PP`, `Pin.AF_OD` or `Pin.ANALOG`. An explanation of the pin modes can be found [here](https://docs.openmv.io/library/pyb.Pin.html#methods). The third parameter, `pull`,  represents the pull mode. It can be set to: `Pin.PULL_NONE`, `Pin.PULL_UP` or `Pin.PULL_DOWN`. E.g.:

```python
pin0 = Pin('P0', mode, pull)
```

To get the logic level of a pin, call `.value()`. It will return a 0 or a 1. This corresponds to `LOW` and `HIGH` in Arduino terminology.

```python
pin0.value()
```

### PWM

To use PWM, you import the `pyb`, `time`, `Pin`, `Timer` modules.

```python
import pyb
import time
from pyb import Pin, Timer
```

First you need to choose the pin you want to use PWM with.

```python
pin1 = Pin("PC6", Pin.OUT_PP, Pin.PULL_NONE)
```

Create a timer for the PWM, where you set the ID and the frequency.

```python
timer1 = Timer(3, freq=1000)
```

Then you need to start a PWM channel with the timer object. 

```python
channel1 = timer1.channel(1, Timer.PWM, pin=pin1, pulse_width=0)
```

Get or set the pulse width value on a channel. To get, pass no arguments. To set, give a value as an argument.

```python
channel1.pulse_width(Width)
```

### RGB LED

The Portenta H7 has built-in RGB that can be used as feedback for applications. Using the `pyb` library, you can easily define the different LED colors on the Portenta.

For this you will use the `pyb` library.

```python
import pyb
```

Now you can easily define the different colors of the built in LED.

```python
redLED = pyb.LED(1)
greenLED = pyb.LED(2)
blueLED = pyb.LED(3)
```

And then control them in our script.

```python
redLED.on()
redLED.off()

greenLED.on()
greenLED.off()

blueLED.on()
blueLED.off()
```

You could also set a custom intensity for our LED lights. This ranges between the values 0 (off) and 255 (full on). Below you can see an example of how to set the intensity on our different LED lights.

```python
redLED.intensity(128)
greenLED.intensity(64)
blueLED.intensity(50)
```

If no argument is given in the `.intensity()` function, it will return the LED intensity.

### Communication

Like other Arduino® products, the Portenta H7 features dedicated pins for different protocols.

#### SPI

The pins used for SPI on the Portenta H7 are the following:


|  Pin  | Function |
| :---: | :------: |
|  PI0  |    CS    |
|  PC3  |   COPI   |
|  PI1  |    CK    |
|  PC2  |   CIPO   |

You can refer to the [pinout](#gpio-map-2) above to find them on the board.

First, you have to import the relevant module from `pyb`.

```python
from pyb import SPI
```

When you initialize SPI, the only thing you need to state is the bus, which will always be `2` on the Portenta H7; this is the only available bus. The rest of the arguments are optional. But if it is needed, you can state the mode of the SPI device as either `SPI.MASTER` or `SPI.SLAVE`, you can also manually set the `baudrate` of the device. `Polarity` can be set to 0 or 1, and is the logic level the idle clock line sits at (HIGH or LOW). `Phase` can be 0 or 1 to sample data on the first (0) or second (1) clock edge.

```python
spi = SPI(2, SPI.MASTER, baudrate=100000, polarity=0, phase=0)
```

Now, if you want to send data over SPI, you simply call `.send()` inside the arguments you want to send. `data` is the data to send, which could be an integer (dataInt) or a buffer object (dataBuffer). It is optional to set the `timeout`, it indicates the timeout in milliseconds to wait for the send.

```python
dataInt = 21
dataBuffer = bytearray(4)
spi.send(data, timeout=5000)
```

Similarly, if you want to receive data over SPI, you call `.recv()`. `data` indicates the number of bytes to receive, this can be an integer (dataInt) or a buffer (dataBuffer), which will be filled with received bytes.  It is optional to set the `timeout`, which is the time in milliseconds to wait for the receive.

```python
dataInt = 0
dataBuffer = bytearray(4)
SPI.recv(data, timeout=5000)
```

#### I2C

The pins used for I2C (Inter-Integrated Circuit) on the Portenta H7 are the following:

|  Pin  | Function |
| :---: | :------: |
|  PH8  |   SDA    |
|  PH7  |   SCL    |

You can refer to the [pinout](##gpio-map-2) above to find them on the board.

To use the I2C, you import the relevant module.

```python
from pyb import I2C
```

You can now create the I2C object. To create an I2C object you need to state the bus, this indicates what pins you will use for I2C. Giving bus a value of `3` starts I2C on the SCL and SDA pins on the Portenta H7. There are 4 I2C buses on the Portenta H7.

```python
i2c = I2C(3)
```

Now that the object is created, you can initialize it. You need to decide if your device is going to be a controller (I2C.MASTER) or a reader (I2C.SLAVE). If it is a reader device, you also need to set the `address`. You can then set a baudrate if you need to.

```python
i2c.init(I2C.MASTER, addr=address, baudrate=100000)
```

To receive data on the bus, you call the `.recv()` function. In the functions arguments `data` is the number of bytes to receive, it can be an integer (dataInt) or a buffer (dataBuffer), which will be filled with received bytes. `addr` is the address to receive from, this is only required in controller mode. `timeout` indicates how many milliseconds to wait for the receive. The code below shows how to receive and print your data in the OpenMV serial terminal.

```python
dataInt = 0
dataBuffer = bytearray(4)
receivedData = i2c.recv(data, addr=0, timeout=5000)
Print(receivedData)
```

To send data on the bus, you can call the `.send()` function. In the functions arguments `data` is the data to send, an integer (dataInt) or a buffer object (dataBuffer). `addr` is the address to send to, this is only required in controller mode. `timeout` indicates how many milliseconds to wait for the send.

```python
dataInt = 412
dataBuffer = bytearray(4)
i2c.send(data, addr=0, timeout=5000)
```

If you need to make sure that devices are connected to the I2C bus, you can use the `.scan()` function. It will scan all I2C addresses from 0x01 to 0x7f and return a list of those that respond. It only works when in controller mode.

```python
i2c.scan()
```

#### UART

The pins used for UART on the Portenta H7 are the following:

|  Pin  | Function |
| :---: | :------: |
| PA10  |    RX    |
|  PA9  |    TX    |

You can refer to the [pinout](#gpio-map-2) above to find them on the board.

To use the UART, you need to import the relevant module.

```python
from pyb import UART
```

To create the UART object, you need to indicate the UART bus, the Portenta has 3 UART buses, but there is only on UART bus available to use with OpenMV through the boards pins.

```python
uart = UART(1)
```

With the object created, you can initialize it with `init`. When initilazing, you can set the `baudrate`. `bits` is the number of bits per character (7, 8 or 9). `parity` can be set to `None`, `0` (even) or `1` (odd). `stop` is the number of stop bits, 1 or 2. `flow` sets the flow control type, can be 0, UART.RTS, UART.CTS or UART.RTS | UART.CTS. More information on this can be found [here](https://docs.openmv.io/library/pyb.UART.html#flow-control). `timeout` is the time in milliseconds to wait for writing/reading the first character. `timeout_char` is the timeout in milliseconds to wait between characters while writing or reading. `read_buf_len` is the character length of the read buffer (0 to disable).

```python
uart.init(baudrate, bits=8, parity=None, stop=1, timeout=0, flow=0, timeout_char=0, read_buf_len=64)
```

To read from UART, you can call `.read()`. If `bytes` is specified then read at most that many bytes. If `bytes` is not given then the method reads as much data as possible. It returns after the timeout has elapsed. The example code below will read bytes received through uart into an array and then print it in the serial terminal.

```python
array = bytearray(5)
uart.read(array)
print(array)
```

If you intend to write over UART, you can call `.write()`. The function writes `buffer` of bytes to the bus. If characters are 7 or 8 bits wide then each byte is one character. If characters are 9 bits wide then two bytes are used for each character and `buffer` must contain an even number of bytes.

```python
uart.write(buffer)
```

#### Wi-Fi®

To use Wi-Fi® you first need to import the relevant library.

```python
import network
```

Then you need to define the Wi-Fi® networks SSID and put that in a variable. You must do the same for the networks password.

```python
SSID=''
PASSWORD=''
```

Next, you can create a WLAN network interface object. In the argument you can enter `network.STA_IF`, which indicates that your device will be a client and connect to a Wi-Fi® access point.

```python
wlan = network.WLAN(network.STA_IF)
```

To activate the network interface, you can simply call `.activate` with the argument `True`.

```python
wlan.active(True)
```

Now you can decide which network to connect to. Here  it is where the `SSID` and `PASSWORD` variables come in handy.

```python
wlan.connect(SSID, PASSWORD, timeout=30000)
```

If you need to troubleshoot, the connection `.status()` can be used. This function will return a value that describes the connection status. It will also let you know what went wrong with the connection in case it failed.

```python
wlan.status()
```

### Audio

If you want to use audio with the Portenta H7, you first need to include the `audio` module. Another helpful module is `micro_speech`, this runs Google's TensorFlow Lite for Microcontrollers Micro Speech framework for voice recognition.

```python
import audio, micro_speech
```

Next you need to initialize the audio object. In the initialization you can decide how many `channels` to use, it is possible to use either 1 or 2 channels. Frequency decides the sample frequency. Using a higher sample frequency results in a higher noise flow, meaning less effective bits per sample. By default audio samples are 8-bits with 7-bits of effective dynamic range. `gain_db` sets the microphone gain to use. `highpass` is the high pass filter cut off given the target sample frequency.

```python
audio.init(channels=2, frequency=16000, gain_db=24, highpass=0.9883)
```

If you need to deinitialize the audio object, you can simply call `deint()`.

```python
audio.deint()
```

To use micro_speech, you first need to create a micro_speech object. You can create this object in the variable `speech`.

```python
speech = micro_speech.MicroSpeech()
```

Next you can start streaming audio into the `micro_speech` object, to do this you can call `audio.start_streaming()`. Here you can pass the `micro_speech` object as the argument, this will fill the object with audio samples. The MicroSpeech module will compute the FFT of the audio samples and keep a sliding window internally of the FFT the last 100ms or so of audio samples received as features for voice recognition. 

```python
audio.start_streaming(speech.audio_callback)
```

If you need to stop the audio streaming, you can call `.stop_streaming()`.

```python
audio.stop_streaming()
```

## Portenta C33

### Pinout Mapping

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

### Input/Output Pins

The `Pin` class in the `machine` module is essential for controlling Input/Output (I/O) pins of the Portenta C33 board.  These pins are crucial for a wide range of applications, including reading sensor data, controlling actuators, and interfacing with other hardware components.

#### Pin Initialization

To begin using an I/O pin of the Portenta C33 board with MicroPython, you need to initialize it using the `Pin` class from the `machine` module. This involves specifying the pin identifier and its mode (input, output, etc.).

```python
from machine import Pin

# Initializing pin P107 as an output
p107 = Pin('P107', Pin.OUT)
```

#### Configuring Pin Modes

You can configure a pin as an input or output. For input pins, it's often useful to activate an internal pull-up or pull-down resistor. This helps to stabilize the input signal, especially in cases where the pin is reading a mechanical switch or a button.

```python
# Configuring pin P105 as an input with its pull-up resistor enabled
p105 = Pin('P105', Pin.IN, Pin.PULL_UP)
```

#### Reading from and Writing to Pins

To read a digital value from a pin, use the `.value()` method without any arguments. This is particularly useful for input pins. Conversely, to write a digital value, use the `.value()` method with an argument. Passing `1` sets the pin to `HIGH`, while `0` sets it to `LOW`. This is applicable to output pins.

```python
# Reading from P105
pin_value = p105.value()

# Writing to P107
p107.value(1)  # Set p2 to high
```

#### Advanced Pin Configuration

The Pin class allows dynamic reconfiguration of pins and setting up interrupt callbacks. This feature is essential for creating responsive and interactive applications.

```python
# Reconfiguring P105 as an input with a pull-down resistor
p105.init(Pin.IN, Pin.PULL_DOWN)

# Setting up an interrupt on P105
p105.irq(lambda p: print("- IRQ triggered!", p))
```

#### Practical Example

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

### Analog to Digital Converter

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

#### Initializing the ADC

First, to use an ADC of the Portenta C33 board, create an ADC object associated with a specific pin. This pin will be used to read analog values.

```python
from machine import ADC

# Create an ADC object on a specific pin
adc = ADC(pin)
```

#### Reading Analog Values

You can read analog values as raw values using the `read_u16()` method. This method returns a raw integer from 0-65535, representing the analog reading.

```python
# Reading a raw analog value
val = adc.read_u16()
```

#### Practical Example

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

### Pulse Width Modulation

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

#### Setting Up PWM

To use PWM, start by initializing a pin and then creating a PWM object associated with that pin.

```python
import machine

# Initialize a pin for PWM (e.g., pin P105)
p105 = machine.Pin('P105')
pwm1 = machine.PWM(p105)
```

#### Configuring PWM Parameters

The frequency and duty cycle of the PWM signal are set based on the specific needs of your application:

```python
# Set the frequency to 500 Hz
pwm1.freq(500)

# Adjusting the duty cycle to 50 for 50% duty
pwm1.duty(50)
```

#### Checking PWM Configuration

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

#### Deinitializing PWM

When PWM is no longer needed, the pin can be deinitialized:

```python
pwm1.deinit()
```

#### Practical Example

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

### Real-Time Clock

The `RTC` class in MicroPython provides a way to manage and utilize the Real-Time Clock (RTC) of the Portenta C33 board. This feature is essential for applications that require accurate timekeeping, even when the main processor is not active. The RTC maintains accurate time and date, functioning independently from the main system. It continues to keep track of the time even when the board is powered off, as long as it's connected to a power source like a battery.

#### Initializing the RTC

To use the RTC, first create an RTC object. This object is then used to set or read the current date and time.


```python
import machine

# Create an RTC object
rtc = machine.RTC()
```

#### Setting and Getting Date and Time

The RTC allows you to set and retrieve the current date and time. The date and time are represented as an 8-tuple format.

```python
# Setting the RTC date and time
rtc.datetime((2024, 1, 4, 4, 20, 0, 0, 0))

# Getting the current date and time
current_datetime = rtc.datetime()
print("- Current date and time:", current_datetime)
```

The 8-tuple for the date and time follows the format `(year, month, day, weekday, hours, minutes, seconds, subseconds)`.

#### Practical Example

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
