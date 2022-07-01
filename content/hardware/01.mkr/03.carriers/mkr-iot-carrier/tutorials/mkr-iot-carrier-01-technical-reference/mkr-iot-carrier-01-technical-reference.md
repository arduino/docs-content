---
title: 'MKR IoT Carrier Cheat Sheet'
description: 'Learn how to set up the MKR IoT Carrier, get a quick overview of the compatible boards, components, and the library.'
author: 'Liam Aljundi'
tags: 
  - API
  - Installation
  - Sensors
libraries:
  - name: Arduino MKRIoTCarrier
    url: https://www.arduino.cc/reference/en/libraries/arduino_mkriotcarrier/
hardware:
  - hardware/01.mkr/03.carriers/mkr-iot-carrier
---

![The Arduino MKR IoT Carrier](assets/mkrIotCarrier-overview.png)

The Arduino® MKR IoT Carrier is equipped with different sensors, actuators and with a display to leave you free to focus on prototyping and programming your next IoT projects. The carrier does not come equipped with a microcontroller, meaning it only works in combination with an Arduino board. The MKR IoT Carrier comes equipped with 5 RGB LEDs, 5 capacitive touch buttons, a colored display, IMU and a variety of quality sensors. It also features a battery holder for a 18650 Li-Ion battery, SD card holder and Grove connectors.

## Compatible Boards

The MKR family of boards share a common pinout, meaning that they can all be easily connected to the MKR IoT Carrier. Here is a list of the MKR boards:

- [MKR 1000 WiFi](https://docs.arduino.cc/hardware/mkr-1000-wifi)
- [MKR FOX 1200](https://docs.arduino.cc/hardware/mkr-fox-1200)
- [MKR GSM 1400](https://docs.arduino.cc/hardware/mkr-gsm-1400)
- [MKR NB 1500](https://docs.arduino.cc/hardware/mkr-nb-1500)
- [MKR Vidor 4000](https://docs.arduino.cc/hardware/mkr-vidor-4000)
- [MKR WAN 1300](https://docs.arduino.cc/hardware/mkr-wan-1300)
- [MKR WAN 1310](https://docs.arduino.cc/hardware/mkr-wan-1310)
- [MKR WiFi 1010](https://docs.arduino.cc/hardware/mkr-wifi-1010)
- [MKR Zero](https://docs.arduino.cc/hardware/mkr-zero)

The MKR family boards offer different features that can be useful for your projects. You can [browse through the boards](https://store.arduino.cc/collections/mkr-family) and pick the one that is most compatible for your project.

### Assembly

The chosen Arduino MKR board needs to be mounted on top of the MKR IoT Carrier and connected to a computer. The board can be connected as shown in the image below, matching the pin numbers on the board to the ones on the carrier.

![Mounting board on the MKR IoT Carrier](assets/mkrIotCarrier-mounting-board.png)

## Datasheet

The full datasheet is available as a downloadable PDF from the link below:

- [Download the Arduino MKR IoT Carrier datasheet](https://content.arduino.cc/assets/MKR%20IoT%20Carrier%20-%20Datasheet.pdf?_gl=1*13zil78*_ga*MTgzMTI1MTI1Mi4xNjE3ODc1MzM2*_ga_NEXN8H46L5*MTYzMDQwMTY0OS4xMzAuMS4xNjMwNDA2MTcwLjA.)

## Arduino IoT Cloud

The MKR IoT Carrier can be controlled through the [Arduino IoT Cloud](https://create.arduino.cc/iot/things), a cloud service that allows us to create IoT applications in just minutes, if combined with an Arduino IoT Cloud compatible board. Here's a list of the Arduino MKR family boards that are compatible with the Arduino IoT Cloud:

- [MKR 1000 WiFi](https://docs.arduino.cc/hardware/mkr-1000-wifi)
- [MKR GSM 1400](https://docs.arduino.cc/hardware/mkr-gsm-1400)
- [MKR NB 1500](https://docs.arduino.cc/hardware/mkr-nb-1500)
- [MKR WAN 1300](https://docs.arduino.cc/hardware/mkr-wan-1300)
- [MKR WAN 1310](https://docs.arduino.cc/hardware/mkr-wan-1310)
- [MKR WiFi 1010](https://docs.arduino.cc/hardware/mkr-wifi-1010)

***Note: The MKR GSM 1400 and MKR NB 1500 require a SIM card to connect to the Cloud, as they communicate over the mobile networks. The MKR WAN 1300 and 1310 board requires a Arduino PRO Gateway LoRa® to connect to the cloud.***

If you need help to get started, you can go through the [Arduino IoT Cloud tutorial](https://docs.arduino.cc/cloud/iot-cloud/tutorials/iot-cloud-getting-started).

## Pinout

![The pinout for MKR IoT Carrier](assets/mkrIoTCarrier-pinout.png)

To see the full pinout, you can download the PDF from the link below.

- [The MKR IoT Carrier full pinout (PDF)](https://content.arduino.cc/assets/Pinout-MKRIOTCARRIER_latest.pdf)

## Grove Connectors

![Grove connectors on the MKR IoT Carrier](assets/mkriotcarrier-grove-connectors.png)

The MKR IoT Carrier comes with **three grove connectors** (2 analog and 1 I2C) that enables us to easily connect external sensors. The type of the connector is labeled clearly on the back of the carrier.

## Carrier Library

To program the MKR IoT Carrier, the **Arduino_MKRIoTCarrier** library needs to be included. This library allows us to control and read all the components of the MKR IoT Carrier. Setting up the MKRIoTCarrier library requires an addition of few code lines in the **initialization** and **setup**. Practically speaking, the code used in the initialization and setup is rarely changed, and it is required in every sketch.

### Initialization

In the initialization (the very top) of every sketch, the **MKRIoTCarrier** library needs to be included, which includes the individual libraries of the components mounted onto the carrier.

Next, an object, which is always named `carrier` needs to be added.

```arduino
#include <Arduino_MKRIoTCarrier.h>
MKRIoTCarrier carrier;
```

### Setup

Inside the `setup()` of every sketch that created, 2 lines of code needs to added:

The boolean `CARRIER_CASE` refers to the **plastic casing** in the kit, and the capacitive buttons on the carrier. It is set to `true` when the plastic casing is used, and to `false` when not. This is not mandatory, as it is set to `false` by default.

The `carrier.begin();` command is essential to initializing the carrier and must be added.

```arduino
  CARRIER_CASE = false;
  carrier.begin();
```

## Humidity & Temperature Sensor

![The HTS221 Humidity Sensor on the MKR IoT Carrier](assets/mkrIotCarrier-sensor-temp&humi.png)

The **HTS221 Humidity Sensor** is mounted on the top side of the carrier under the display, marked with a drop icon. The sensor uses capacitive sensing with a **humidity sensing range** of **0-100%** and **accuracy** of **± 3.5% rH (20 to +80% rH)**, and a **temperature sensing range** of **-40 to 120° C**, with an **accuracy** of **± 0.5 °C,15 to +40 °C**. The sensor uses a low power consumption (2μA at 1 Hz sampling rate) and connects to the mounted Arduino MKR board through a I2C interface.

### Code

The **ArduinoHTS221** library is included in the **MKRIoTCarrier**, meaning that it does not need to include it separately. The values from the **temperature** and **humidity** sensors can be stored in **float** variables as shown below.

```arduino
float temperature = carrier.Env.readTemperature();
float humidity = carrier.Env.readHumidity();
```

The following methods can be used to get the temperature and humidity values:

```arduino
carrier.Env.readTemperature();
```

Returns temperature value in Celsius.

```arduino
carrier.Env.readHumidity();
```

Returns relative humidity (rH) in percentage.

## Pressure Sensor

![The LPS22HBTR Pressure Sensor on the MKR IoT Carrier](assets/mkrIotCarrier-sensor-pressure.png)

The **LPS22HBTR Pressure Sensor** is mounted on the top side of the carrier under the display, marked with a meter icon. The sensor measures **absolute pressure range** of **260 to 1260 hPa (0.25 to 1.24 atm)** and connects to the mounted Arduino MKR board through a I2C interface.

### Code

The **ArduinoLPS22HB** library is included in the **MKRIoTCarrier**, meaning that it does not need to include it separately. The values from the **pressure** sensor can be stored in **float** variables as shown below.

```arduino
float pressure = carrier.Pressure.readPressure();
```

The following methods can be used to get the pressure values:

```arduino
carrier.Pressure.readPressure();
```

Returns pressure value in Kilopascal (kPa).

## IMU Accelerometer & Gyroscope Sensors

![The IMU on the MKR IoT Carrier](assets/mkrIotCarrier-sensor-imu.png)

The **LSM6DSOXTR** from STM is an IMU (Inertial Measurement Unit) that features a 3D digital accelerometer and a 3D digital gyroscope. It features among many other things, a machine learning core, which is useful for any motion detection projects, such as free fall, step detector, step counter, pedometer. The unit is placed underneath the MKR IoT Carrier's display, connects to the mounted Arduino MKR board through an I2C interface, and acquires Low power consumption (0.55mA max).

### Code

To access the data from the **LSM6DSOX module**, the **MKRIoTCarrier** library needs to be included. The carrier's library includes the **Arduino_LSM6DS3** and functions similarly. The 3-axis values from the **accelerometer** and **gyroscope** sensors can be stored in **float** variables as shown below:

```arduino
float x, y, z;

void loop(){
  if (carrier.IMUmodule.accelerationAvailable())
    {
      carrier.IMUmodule.readAcceleration(x, y, z);
      Serial.println(x);
    }
}

```

The following methods can be used to detect movement:

```arduino
carrier.IMUmodule.accelerationAvailable();
```

Returns 0 if no new acceleration data sample is available, 1 if new acceleration data sample is available.

```arduino
carrier.IMUmodule.readAcceleration(x, y, z);
```

Allows as to access the acceleration data on the three axis (x, y & z).

## RGB and Gesture Sensor

![The APDS-9660 sensor on the MKR IoT Carrier](assets/mkrIotCarrier-sensor-rgb.png)

The MKR IoT Carrier contains a Broadcom **APDS-9660 RGB and Gesture sensors**, situated under the display and marked with a bulb icon. The sensor is useful for **ambient light** and **RGB** color sensing, **proximity** sensing, and **gesture** detection.

### Code

The **ArduinoAPDS9960** library is included in the **MKRIoTCarrier**, meaning that it does not need to include it separately. The color values from the **RGB** sensor can be stored in **int** variables as shown below.

The `carrier.Light.readColor(r, g, b);` method can be used to detect colors.

The if statement `if (r >= 135 && g >= 135 && b >= 135)` in the code below checks if the color detected ranges from light gray to white, but the numbers assigned to red (r), green (g) and blue (b) can be customized to any desired color.

```arduino
  int r, g, b;

  void loop(){

    if (carrier.Light.colorAvailable()){
     carrier.Light.readColor(r, g, b); //read rgb color values

      // check if color/light is bright enough
      if (r >= 135 && g >= 135 && b >= 135){
        Serial.print("White color detected");
      }
    }
  }

```

The following methods can be used to detect gesture:

```arduino
carrier.Light.gestureAvailable();
```

Checks the availability of the **gesture** sensor.

```arduino
carrier.Light.readGesture();
```

Confirms which gesture is being detected, and **returns** UP, DOWN, RIGHT or LEFT.

The code example below shows the gesture value in a fixed width integer `uint8_t` variable, and the if statement checks `if (gesture == UP)`. To detect movements in other directions, UP can be replaced with DOWN, RIGHT or LEFT.

```arduino

  void loop(){

    if (carrier.Light.gestureAvailable())
    {
      uint8_t gesture = carrier.Light.readGesture(); // a variable to store the type of gesture read by the light sensor
      Serial.print("Gesture: ");

      // when gesture is UP
      if (gesture == UP)
      {
        Serial.println("UP");
      }
  }

```

## Relays

![The relays on the MKR IoT Carrier](assets/mkrIotCarrier-relays-01.png)

The MKR IoT Carrier is equipped with two 5V Coil voltage **KEMET EE2-5NU-L relays**, located on the back side of the carrier. The relays are non-latching with a **COM** (common), **NO** (Normally open) and **NC** (normally closed) contacts, and can take up a max of **2A** Current and **24 V** of input each.

The connections between a high power circuit and the relays will be done through these connectors.

![The relays connectors](assets/mkrIotCarrier-relays-02.png)

Once the cables are introduced inside the connectors, they will automatically be locked inside. To unlock a cable and remove it from the connector, a tool is needed to be inserted through the top square hole (it can be a flat screwdriver, a hard piece of plastic, etc.).

![The L1 and L2 LEDs indicators](assets/mkrIotCarrier-relays-lights.png)

The **L1 and L2 LEDs** on the carrier are visual indicators of the state of the relays. If the LED is ON, it means that the **COM** and the **NO** terminal of the relay are **connected**, and if the LED is OFF it means that **COM** and **NC** are **connected**.

### Code

The `carrier.RelayX.open();` and `carrier.RelayX.close();` methods can be used to control the relays, and `carrier.RelayX.getStatus();` to read the status of the relays.

Swap to the Normally Open (NO) circuit of relay 1 (turns it on):

```arduino
carrier.Relay1.open();
```

Swap to the Normally Closed (NC) circuit of relay 2 (turns it off), default mode on power off:

```arduino
carrier.Relay2.close();
```


Bool, returns the status LOW means NC and HIGH means NO:

```arduino
carrier.Relay2.getStatus();
```

## Peripherals

### Display

![The MKR IoT Carrier's display](assets/mkrIotCarrier-display.png)

The screen on the MKR IoT Carrier is a **rounded 1.3” TFT display**, with a 240 x 240 resolution and a diameter of 36 x 40 mm.

#### Code

The display is controlled through the Adafruit-ST7735-Library, which is included in the carrier's library, meaning that it does not need to be added it separately.

Below are some methods to configure the MKR IoT Carrier's display, these include basic configurations, background and text colors, font size, position of the cursor and a loading animation.

```arduino
carrier.display.fillScreen(color);
```

This method sets the color of the background of the display using hex codes.

```arduino
carrier.display.setRotation(0);
```

This method sets the angle of the screen, 0 is the starting position with no rotation.The screen can only be rotated 90, 180 or 270 degrees by replacing the 0 with 1, 2 or 3.

```arduino
display.print("text");
```

This method will print the text inside the string at the current cursor position.

```arduino
carrier.display.drawBitmap(x, y, bitmap_visual, w, h, color);
```

This method displays a bitmap visual on the carrier's screen. The values x & y values are the top left coordinates where the visual is drawn, w & h are the width and height of the visual. The data for the bitmap_visual graphic can be stored as a byte array and used as the `bitmap_visual`.

```arduino
carrier.display.setTextColor(color);
```

This method sets the color of the text using hex codes.

```arduino
carrier.display.setTextSize(number);
```

This method sets the text size. 2 is an average text size since it is visible, but not too small, 3 is a bit larger.

```arduino
carrier.display.setCursor(x, y);
```

This method is very important, as it indicates where on the printing starts on the display. It is indicated by pixels, so, if **0, 0** are used for example, it will start printing in the top left corner.

### Buttons

![The MKR IoT Carrier's buttons](assets/mkrIotCarrier-buttons.png)

The carrier has five **capacitive qTouch buttons** on its top side, numbered from 00 to 04. The buttons are sensitive to direct touch and detect wireless touch.

#### Code

The **Button class** can be controlled using the following methods:

```arduino
Buttons.update();
```

Reads the state of the pads and save them to be used in the different types of touch events.

```arduino
Buttons.getTouch(TOUCHX);
```

Get if the pad is getting touched, true until it gets released.

```arduino
Buttons.onTouchDown(TOUCHX);
```

Get when have been a touch down.

```arduino
Buttons.onTouchUp(TOUCHX);
```

Get when the button has been released.

```arduino
Buttons.onTouchChange(TOUCHX);
```

Get both, touched and released.

`TOUCH0`, `TOUCH1`, `TOUCH2`, `TOUCH3`, `TOUCH4` can be used to access each individual button. The code example below shows how the status of a button can be checked.

```arduino

  void loop(){
    // updates buttons status
    carrier.Buttons.update();

    // Checks if button 00 is touched
    if (carrier.Buttons.onTouchDown(TOUCH0))
    {
      Serial.print("Button 0 pressed down");
    }
  }

```

### LEDs

![The LEDs on the MKR IoT Carrier](assets/mkrIotCarrier-leds.png)

The MKR IoT Carrier comes with 5 **digital RGB LEDs** placed on the top side of the carrier in front of the buttons.

#### Code

The LEDs are controlled with the Adafruit’s DotStar library, which is included in the `MKRIoTCarrier` library.

The `carrier.leds.show();` method is necessary for updating the new state of the LEDs and needs to be called after any change of the state of the LEDs (turning on & off or change of color).

Here are some of the useful methods used to control the LEDs on the MKR IoT Carrier:

```arduino
carrier.leds.setPixelColor(index, green, red, blue);
```

Sets the color of the index’s LED.

```arduino
carrier.leds.setBrightness(0-255)
```

Set the overall brightness, from 0 (no brightness) to 255 (maximum brightness).

```arduino
carrier.leds.clear()
```

Clear the buffer of the LEDs.

```arduino
carrier.leds.fill(color, firstLedToCount, count);
```

Fill X amount of the LEDs with the same color.

```arduino
uint32_t myColor = carrier.leds.Color(green, red, blue)
```

Saves a custom color.

The code example below shows how to light up all 5 LEDs with our customized color.

```arduino

#include <Arduino_MKRIoTCarrier.h>
MKRIoTCarrier carrier;

uint32_t myCustomColor = carrier.leds.Color(255,100,50);

void setup(){
   CARRIER_CASE = false;
   carrier.begin();
   carrier.leds.fill(myCustomColor, 0, 5);
   carrier.leds.show();
}

```

### Buzzer

![The buzzer on the MKR IoT Carrier](assets/mkriotcarrier-buzzer.png)

The MKR IoT Carrier is equipped with a **sound buzzer** on the bottom side of the carrier, under the MKR board.

#### Code

The buzzer can be controlled with the following methods:

```arduino
carrier.Buzzer.sound(freq)
```

Equivalent to tone(), it will make the tone with the selected frequency.

```arduino
carrier.Buzzer.noSound()
```

Equivalent to noTone(), it will stop the tone signal.

## Memory

The MKR IoT Carrier contains a **SD Card slot** that accepts a Micro SD, which allows for three times the amount of data storage locally.

### Code

The memory can be used with the SD library commands that is already included in the `MKRIoTCarrier` library

The SD class initialized in the main `carrier.begin()`. In order to save our data on a specific file, the method `SD.open("file-name", FILE_WRITE))` can be used. The code below demonstrates how to save data on a file on a SD card.

```arduino
#include <Arduino_MKRIoTCarrier.h>
MKRIoTCarrier carrier;

File myFile;

setup(){
   CARRIER_CASE = false;
   carrier.begin();  //SD card initialized here

   myFile = SD.open("test.txt", FILE_WRITE);
}
```

## Power

![JST battery connector on the MKR IoT Carrier.](assets/mkriotcarrier-battery.png)

The MKR IoT Carrier can be either powered through a USB cable connected to the mounted MKR board, or through a battery. The battery used should be a LI-ION 18650 3.7 v battery, which can be mounted to the carrier via the battery holder on the bottom side. 

A cable with JST connectors on both ends are needed to connect the MKR IoT Carrier and the MKR board. The Battery can then be recharged via a USB connection through the MKR Board (Runs up to 48h with a 3.7v 2500mAh).

<video width="100%" controls="true">
<source src="assets/mkrIoTCarrier-battery-assembly.mp4" type="video/mp4"/>
</video>