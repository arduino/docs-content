---
author: 'Hannes Siebeneicher'
hero_image: "./hero-banner.png"
micropython_type: "101"
featured: micropython-101
title: 'Component Examples'
description: 'Practical examples for Neopixels, sensors, servo motors and more.'
---

Congratulations you have almost reached the end of your MicroPython 101 course. This chapter introduces you to several popular sensors and motors, showing you how to connect them, what code you need, and also what the intended outcome should look like. Try out all examples and feel free to combine them and create new exciting projects as you go.

**Before getting started** we need to make sure we install all necessary modules for the sensors we will be using. If you skipped the chapter where we talk about modules or need a quick refresh you can go back to "[Introduction to MicroPython](../01.introduction-python/02.intro-to-micropython.md)". Copy the script below and paste it into your ``main.py`` file. Don't forget to add your **network credentials** to the scripts otherwise, it won't work.

```python
#import modules
import mip
import network

#connect to network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)

    #enter your network credentials here
    sta_if.connect('<ssid>', '<key>')

    while not sta_if.isconnected():
        pass
    print('network config:', sta_if.ifconfig())
    
#import modules from Github
mip.install("https://raw.githubusercontent.com/Hannes7eicher/MicroPython/main/modules/lis3dh.py")
mip.install("https://raw.githubusercontent.com/Hannes7eicher/MicroPython/main/modules/neopixel.py")
mip.install("https://raw.githubusercontent.com/Hannes7eicher/MicroPython/main/modules/ssd1306_1315.py")
mip.install("https://raw.githubusercontent.com/Hannes7eicher/MicroPython/main/modules/tm1637.py")
```

When you run the code you should see some feedback in the REPL.

If everything worked you should now see a library folder with all the necessary modules on your board memory and you can continue trying out the examples listed below.

## Button

This example shows how to use a [pushbutton](https://store.arduino.cc/products/grove-button-p?queryID=3db0c95a3af43412f59d48a243453a53) with MicroPython. Connect the button as shown below. Even though the Grove cable has four cables we only need three (Power, GND, Signal). Copy the code to ``main.py``, and press play.

![Button Circuit](./assets/circuitButton.png)

```python
# Import the Pin class from the machine module
from machine import Pin
# Import the sleep function from the time module
from time import sleep     

# Create a Pin object for pin 5 as an input with a pull-up resistor
button = Pin(5, Pin.IN, Pin.PULL_UP)   

# Start an infinite loop
while True:
    # Read the current state of the button    
    button_state = button.value()    
    # Check if the button state is LOW (0)
    if button_state == 0:    
        # If the button is not pressed, print a message
        print("Button not pressed")    
    else:
        # If the button is pressed, print a message
        print("Button pressed")    
    # Pause the program for 0.5 seconds
    sleep(0.5)    
```

Now whenever you press the button you should see ``Button pressed`` being printed in the REPL. 

<video width="100%" loop autoplay>
<source src="assets/Button.mp4" type="video/mp4" />
</video>

## LED

This example shows how to create the classic blink example using MicroPython and a [Grove LED](https://www.seeedstudio.com/Grove-Red-LED.html). Connect the LED according to the circuit shown below, copy the code to ``main.py``, and press play to see it in action.

![LED Circuit](./assets/circuitLED.png)

```python
# Import the Pin class from the machine module
from machine import Pin   
# Import the sleep function from the time module 
from time import sleep     

# Create a Pin object for pin 5 as an output
led = Pin(5, Pin.OUT)    

# Start an infinite loop
while True:    
    # Turn on the LED
    led.on()  
    # Pause the program for 1 second  
    sleep(1)   
    # Turn off the LED 
    led.off()  
    # Pause the program for 1 second 
    sleep(1)    
```

You should now see the led blinking. Change the code to make it speed up or slow down. 

<video width="100%" loop autoplay>
<source src="assets/led.mp4" type="video/mp4" />
</video>

## Servo

This code controls a [servo motor](https://store.arduino.cc/products/grove-servo?queryID=5a2a481038aab78eec2ab1d0b51687a0) connected to Pin 5 (D2) using PWM. As with any motor if the current is being drawn due to the motor needing too much power the board resets. Copy the code to ``main.py`` and press play.

![Servo Motor Circuit](./assets/circuitServo.png)

```python
# Import the Pin and PWM classes from the machine module
from machine import Pin, PWM   
# Import the time module
import time                    

# Create a PWM object named 'servo' on pin 5 configured as an output
servo = PWM(Pin(5, mode=Pin.OUT))    
# Set the frequency of the PWM signal to 50Hz
servo.freq(50)                      

# Start an infinite loop
while True:    
    # Set the duty cycle of the PWM signal to 26 (position 1 of the servo)
    servo.duty(26)  
    # Pause the program for 1 second  
    time.sleep(1)     
    # Set the duty cycle of the PWM signal to 123 (position 2 of the servo)
    servo.duty(123)  
    # Pause the program for 1 second 
    time.sleep(1)     
```

You should now see the servo moving back and forth in an endless loop.

<video width="100%" loop autoplay>
<source src="assets/servoMotor.mp4" type="video/mp4" />
</video>

## Neopixel

This example shows how to use a [Neopixel](https://www.seeedstudio.com/Grove-RGB-LED-Stick-10-WS2813-Mini.html) strip with 10 RGB LEDs. Although we are addressing 10 LEDs at once we luckily still only need one signal pin making our setup super easy. Connect the RGB strip as seen in the circuit below, copy the code to ``main.py`` and press play.

![Neopixel Circuit](./assets/circuitNeopixel.png)

```python
# Import the Pin class from the machine module
from machine import Pin
# Import the sleep class from the time module
from time import sleep
#Import the neopixel module
import neopixel

# Set the number of pixel on the RGB strip
PIXEL_NUMBER = 10
# Create a NeoPixel object with 24 pixels connected to pin 21
np = neopixel.NeoPixel(Pin(21), PIXEL_NUMBER)   

# Define colors
purple = (200, 0, 200)
black = (0, 0, 0)

# Fill the entire strip with black color (turn off all pixels)
np.fill(black)   
# Update the NeoPixel strip to reflect the changes
np.write()       

# Function for turning on all pixels on after the other
def ringUp():
    #loop through all pixels
    for i in range(0, PIXEL_NUMBER):
        # Set the i-th pixel to purple color
        np[i] = purple   
        # Update the NeoPixel strip to reflect the changes
        np.write()   
        # Pause for 0.1 seconds    
        sleep(0.1)       
        
# Function for turning on all pixels off after the other
def ringDown():
    for i in range(0, PIXEL_NUMBER):
        np[i] = black  
        np.write()     
        sleep(0.1)     
        
# Function for turning on all pixels off
def ringOff():
    for i in range(0, PIXEL_NUMBER):
        np[i] = black  
    np.write()         
    
# Function looping through ringUp() and ringDown()
def runPixelRun():
    while(1):             
        ringUp()        
        ringDown()      
    
# Start running the pixel animation
runPixelRun()             
```

You should now see a nice animation lighting up your LED RGB strip.

<video width="100%" loop autoplay>
<source src="assets/neopixel.mp4" type="video/mp4" />
</video>

## DHT11

This example shows how to use a [DHT11](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT11.html?queryID=feac683b68679492e4f168b43f6a6bdd&objectID=1826&indexName=bazaar_retailer_products) with an Arduino Nano ESP32. DHT sensors are temperature and humidity sensors and make use of the built-in ``dht`` module. Connect the sensors as shown below, copy the code to ``main.py``, and press play.


![DHT11 Circuit](./assets/circuitDHT11.png)

```python
#import dht module
import dht
#import Pin class from machine module
from machine import Pin
# Import sleep_ms class from time module
from time import sleep_ms

# Define sensor pin
SENSOR_PIN = 5

# Create a DHT11 object with the specified pin number
TEMP_SENSOR = dht.DHT11(Pin(SENSOR_PIN))  
# Pause for 500 milliseconds to allow the sensor to stabilize 
sleep_ms(500)                             

# Loop indefinitely
while(1):   
    # Trigger a measurement from the DHT11 sensor                              
    TEMP_SENSOR.measure()               
    # Print the measured temperature   
    print(TEMP_SENSOR.temperature())  
    # Uncomment the line below if you want to measure humidity    
    # print(TEMP_SENSOR.humidity())          
    # Pause for 1 second before taking the next measurement
    sleep_ms(1000)                         

```

You should now see the moisture being printed in the REPL.

<video width="100%" loop autoplay>
<source src="assets/DHT11.mp4" type="video/mp4" />
</video>

## OLED Screen

This example shows how to use an [OLED](https://store.arduino.cc/products/grove-oled-display-0-96?queryID=e9abc3d3ad2ef916bd26c57c9b311ce9) screen via I2C. If you are using a different OLED screen make sure to adjust the screen size in the code to display the content properly. Copy the code to ``main.py`` and press play to see it in action.

![OLED Circuit](./assets/circuitOled.png)

```python
# Import the Pin class and SoftI2C class (for using I2C) form the machine module
from machine import SoftI2C, Pin
# Import Oled module
import ssd1306_1315 as ssd1306
# Import the sleep_ms class from the time module
from time import sleep_ms

# Set the display width to 128 pixels
DISPLAY_WIDTH = 128   
# Set the display height to 64 pixels
DISPLAY_HEIGHT = 64   

class Point():
    def __init__(self, x, y):
        # Initialize the x-coordinate of the point
        self.x = x   
        # Initialize the y-coordinate of the point
        self.y = y   

# Create a Point object with initial coordinates (64, 32)
old_coords = Point(64, 32)   
# Create a Point object with initial coordinates (64, 32)
new_coords = Point(64, 32)  

# Create a SoftI2C object for I2C communication with the specified pins and frequency
i2cbus = SoftI2C(scl=Pin(12), sda=Pin(11), freq=100000)   
print(i2cbus)

# Create an SSD1306 OLED object with the specified width, height, and I2C bus
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2cbus)   
# oled.fill(0)
oled.show()

# Display the text "Arduino" at the specified coordinates
oled.text('Arduino', 40, 12)      
# Display the text "vs" at the specified coordinates   
oled.text('+', 60, 26)      
# Display the text "MicroPython" at the specified coordinates        
oled.text('MicroPython', 23, 45)     

# Update the OLED display to reflect the changes
oled.show()                          
```

You should now see Arduino + MicroPython being printed on the screen.

![OLED screen output](./assets/Oled.png)

## Buzzer

This example shows how to use a [Grove Buzzer](https://store.arduino.cc/products/grove-buzzer-piezo?queryID=9655030cc2165861ec71fa900ef46f8b). Following the same principle connect the button as shown in the circuit below, copy the code to ``main.py``, and press play to see it in action.

![Buzzer Circuit](./assets/circuitBuzzer.png)

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

Now your buzzer should be buzzing away. Change the code and play with the intensity and duration.

## Accelerometer

This example shows how to use a [Grove Accelerometer](https://store.arduino.cc/products/grove-3-axis-digital-accelerometer-16g?queryID=cf10960cf012640816efcf27f84dc92c) using I2C. This particular sensor can measure acceleration and its position in space. Because it's using I2C it needs all four wires as shown in the circuit below.

![Accelerometer](./assets/circuitAccelerometer.png)

```python
# Import lis3dh, time, and math classes
import lis3dh, time, math
# Import Pin and SoftI2C class from the machine module
from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(11), scl=Pin(12)) # I2C
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
Move around your sensor to see the numbers in the REPL change. Maybe try to connect the led and turn it on when you move the Accelerometer in a certain way.

<video width="100%" loop autoplay>
<source src="assets/Accelerometer.mp4" type="video/mp4" />
</video>

## Sound Sensor

This example shows how to use a [sound sensor](https://store.arduino.cc/products/grove-sound-sensor?queryID=undefined). It's used to measure sound and display it to the REPL. Connect it as shown below, copy the code to ``main.py``, and press play to try it out.

![Sound Sensor Circuit](./assets/circuitSoundSensor.png)

```python
# Import Pin and ADC class from the machine module
from machine import Pin, ADC
# Import the time module
import time

# Create an ADC object and associate it with pin 5
pin_adc = ADC(Pin(5))      
# Set the attenuation level to 11dB, which allows for a wider input voltage range
pin_adc.atten(ADC.ATTN_11DB)   

while True:
    sum_value = 0

    for i in range(32):
        # Read the ADC value and add it to the sum
        sum_value += pin_adc.read()   

    # Right shift the sum by 5 bits (equivalent to dividing by 32) to get the average value
    sum_value >>= 5   

    # Print the average value   
    print(sum_value)   
    # Pause for 100 milliseconds
    time.sleep_ms(100)   
```

If you make a sound you should see the output change in the REPL.

<video width="100%" loop autoplay>
<source src="assets/SoundSensor.mp4" type="video/mp4" />
</video>

## 4 Digit Display

This example shows how to use a [Grove 4-digit display](https://store.arduino.cc/products/grove-4-digit-display?queryID=a24e1359995118c4ec489ddc59e622c4). 4 digit displays are very basic types of displays that are often seen in alarm clocks as they can display any number between 0 - 9. This sensors also uses I2C which is why we need all four wires as shown below. Copy the code to ``main.py``, and press play to see it in action.

![4 Digit Display Circuit](./assets/circuit4DigitDisplay.png)

```python
from machine import Pin
from time import sleep
import tm1637

tm = tm1637.TM1637(clk=Pin(10), dio=Pin(11))

tm.write([63, 191, 63, 63])  # Write a specific pattern of segments to the TM1637 display
sleep(1)

tm.numbers(17, 23)  # Display the numbers 17 and 23 on the TM1637 display
sleep(1)
tm.show('abcd')  # Display the characters 'abcd' on the TM1637 display
sleep(1)
tm.show('bcde')  # Display the characters 'bcde' on the TM1637 display
sleep(1)
tm.show('cdef')  # Display the characters 'cdef' on the TM1637 display
sleep(1)

tm.temperature(20)  # Display the temperature value 20 on the TM1637 display

```

You should now see the display showing different numbers.

![4 digit display](./assets/4DigitDisplay.png)

## Moisture Sensor

This example shows how to use a [moisture sensor](https://store.arduino.cc/products/grove-moisture-sensor?queryID=undefined). As the name suggests this sensor is used to measure moisture by measuring the resistance between the two probes. Dry soil has less conductivity than wet soil and the difference in resistance and the resulting drop/increase in voltage can be measured by the Arduino. Copy the code to ``main.py``, press play, and ideally try it out on a plant nearby. Otherwise just put your hand around the sensor and you should already see a slight change in values.

![Moisture Sensor Circuit](./assets/circuitMoisture.png)

```python
# Import machine module
import machine
# Import time module
import time

# Define sensor pin
adc_pin = machine.Pin(4)
# Create ADC object and associate it with sensor pin
adc = machine.ADC(adc_pin)

#function mapping sensor values from 0 to 100.
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Infinite loop
while True:
    # Read sensor values
    reading = adc.read_u16()
    # Map sensor readings from 0 - 100 for improved user experience
    mapped_reading = map_value(reading, 0, 65535, 0, 100)
    # Print values in REPL
    print("Moisture: ", reading, " Mapped Moisture: ", mapped_reading)
    # Add short sleep timer for improved readability
    time.sleep_ms(500)
```

<video width="100%" loop autoplay>
<source src="assets/Moisture.mp4" type="video/mp4" />
</video>