---
title: 'Esplora Library'
description: 'A library for using the Esplora board.'
author: 'Arduino'
---

## Overview

***This library is archived and is no longer being maintained. It can be still be downloaded and used, but is read-only and cannot be contributed to. For more information, you can view this repository on [GitHub](https://github.com/arduino-libraries/Esplora).***

The Arduino [Esplora](https://www.arduino.cc/en/Main/ArduinoBoardEsplora) has a set of functions for easily interfacing with the sensors and actuators mounted on the board. The functions are accessible through the Esplora class.

The library offers easy access to the data from the onboard sensors, and provides the ability to change the state of the outputs.

The sensors available on the board are:

- 2-Axis analog joystick
- center push-button of the joystick
- 4 push-buttons
- microphone
- light sensor
- temperature sensor
- 3-axis accelerometer
- 2 TinkerKit input connectors

The actuators available on the board are:

- bright RGB (Red-Green-Blue) LED
- piezo buzzer
- 2 TinkerKit output connectors

For more information about the Esplora, visit the [Esplora documentation](/retired/boards/arduino-esplora).

**NOTE: If you're using the Arduino IDE version 1.0.3 or earlier** , you will need to download the [latest version](http://arduino.cc/en/uploads/Guide/Esplora.zip) of this library, or get it from the [Arduino GitHub repository](https://github.com/arduino).

To use this library
```
#include <Esplora.h>
```

## Examples
The Esplora Beginners examples show the functionality of the inputs and outputs of the board. They are a good place to start experimenting with the Esplora's capabilities. The Expert examples are more detailed sketches that illustrate project ideas that utilize the board features in novel ways.

## Beginners
- [EsploraBlink](https://www.arduino.cc/en/Tutorial/EsploraBlink) : Blink the Esplora's RGB LED
- [EsploraAccelerometer](https://www.arduino.cc/en/Tutorial/EsploraAccelerometer) : Read the values from the accelerometer
- [EsploraJoystickMouse](https://www.arduino.cc/en/Tutorial/EsploraJoystickMouse) : Use the Esplora's joystick to control the cursor on your computer
- [EsploraLedShow](https://www.arduino.cc/en/Tutorial/EsploraLedShow) : Use the Joystick and slider to create a light show with the LED
- [EsploraLedShow2](https://www.arduino.cc/en/Tutorial/EsploraLedShow2) : Use the Esplora's microphone, linear potentiometer, and light sensor to change the color of the onboard LED.
- [EsploraLightCalibrator](https://www.arduino.cc/en/Tutorial/EsploraLightCalibrator) : Read the values from the light sensor
-  [EsploraMusic](https://www.arduino.cc/en/Tutorial/EsploraMusic) : Make some music with the Esplora
- [EsploraSoundSensor](https://www.arduino.cc/en/Tutorial/EsploraSoundSensor) : Read the values from the Esplora's microphone
- [EsploraTemperatureSensor](https://www.arduino.cc/en/Tutorial/EsploraTemperatureSensor) : Read the temperature sensor and get the temperature in in Farhenheit or Celsius.

## Experts
- [EsploraKart](https://www.arduino.cc/en/Tutorial/EsploraKart) : Use the Esplora as a controller to play a kart racing game.
- [EsploraTable](https://www.arduino.cc/en/Tutorial/EsploraTable) : Print the Esplora sensor information to a table format.
- [EsploraRemote](https://www.arduino.cc/en/Tutorial/EsploraRemote) : Connect the Esplora to Processing and control the outputs.
- [EsploraPong](https://www.arduino.cc/en/Tutorial/EsploraPong) : Play Pong with the Esplora using Processing.

## Functions
---

### `Esplora constructor`
#### Description

Esplora is the base class for all methods used by the board. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `readSlider()`
#### Description

Reads the value from the linear potentiometer as a 10-bit number. This means that it will map input voltages between 0 and 5 volts into integer values between 0 and 1023. This yields a resolution between readings of: 5 volts / 1024 units or, .0049 volts (4.9 mV) per unit.

#### Syntax
```
Esplora.readSlider()
```
#### Parameters
none

#### Returns
int : The linear potentiometer's position, mapped to a value between 0 and 1023.

#### Example
```
#include <Esplora.h>

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int value = Esplora.readSlider();
  Serial.println(value);

  delay(1000);
}
 
```

---

### `readLightSensor()`
#### Description

Reads the intensity of light hitting the light sensor as a 10-bit number. This means that it will map input voltages between 0 and 5 volts into integer values between 0 and 1023. This yields a resolution between readings of: 5 volts / 1024 units or, .0049 volts (4.9 mV) per unit.

#### Syntax
```
Esplora.readLightSensor()
```
#### Parameters
none

#### Returns
int : The amount of light hitting the sensor, mapped to a value between 0 and 1023.

#### Example
```
#include <Esplora.h>

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int value = Esplora.readLightSensor();
  Serial.println(value);

  delay(1000);
}
 
```

---

### `readTemperature()`
#### Description

Reads the ambient temperature of the temperature sensor and returns a reading in either the Celsius or Fahrenheit scale, depending on the parameter passed.

#### Syntax
```
readTemperature(scale)
```
#### Parameters
scale: the scale of the output, valid arguments are: DEGREES_C and DEGREES_F

#### Returns
int : The temperature reading in Celsius or Fahrenheit. The Celsius range is from -40°C to 150°C, the Fahrenheit range is from -40°F to 302°F.

#### Example
```
#include <Esplora.h>

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int celsius = Esplora.readTemperature(DEGREES_C);
  int fahrenheit = Esplora.readTemperature(DEGREES_F);
  Serial.print(celsius);
  Serial.print("\t");
  Serial.print(fahrenheit);

  delay(1000);
}
 
```

---

### `readMicrophone()`
#### Description

Read the amplitude from the microphone. It returns a valure between 0 and 1023.

#### Syntax
```
readMicrophone()
```
#### Parameters
none

#### Returns
int : The amplitude mapped to a range of 0 to 1023.

#### Example
```
#include <Esplora.h>

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int value = Esplora.readMicrophone();
  Serial.println(value);

  delay(1000);
}
 
```

---

### `readJoystickSwitch()`
#### Description

Reads the joystick's button and returns if its state is 0 or 1023. If you prefer something more consistent with the readButton() function, you may want to use readJoystickButton() instead. That function does the same as this, but returns LOW when the joystick button is pressed, and HIGH when not pressed.

#### Syntax
```
Esplora.readJoystickSwitch()
```
#### Parameters
none

#### Returns
0 when pressed, 1023 when not pressed.

#### Example
```
#include <Esplora.h>


void setup(){
  // nothing in setup
}

void loop()
{
  int button = Esplora.readJoystickSwitch();

  if(button == 0)
  {
    Esplora.writeRed(255);
  }
  else {
    Esplora.writeRed(0);
  }
}
```

---

### `readJoystickButton()`
#### Description

Reads the joystick's button and returns if its state is LOW or HIGH. This function does basically the same thing as readJoystickSwitch(), but it returns values consistent with the readButton() function.

#### Syntax
```
Esplora.readJoystickButton()
```
#### Parameters
none

#### Returns
LOW when pressed, HIGH when not pressed.

#### Example
```
#include <Esplora.h>


void setup(){
  // nothing in setup
}

void loop()
{
  int button = Esplora.readJoystickButton();

  if(button == LOW)
  {
    Esplora.writeRed(255);
  }
  else {
    Esplora.writeRed(0);
  }
}
```

---

### `readAccelerometer()`
#### Description

Reads values from the Esplora's accelerometer. Each of the three axes are accessed independently.

#### Syntax
```
Esplora.readAccelerometer(axis)
```
#### Parameters
axis : char, determines what axis to read.

- X_AXIS	to read the X-axis value
- Y_AXIS	to read the Y-axis value
- Z_AXIS	to read the Z-axis value
#### Returns
int : the value of the readings on the chosen axis. The accelerometer returns zero when it is perpendicular to the direction of gravity. Positive or negative values result when it is accelerates in one of the two directions of the axis.

#### Example
```
#include <Esplora.h>

void setup()
{
 Serial.begin(9600);
}

void loop()
{
 int x_axis = Esplora.readAccelerometer(X_AXIS);
 int y_axis = Esplora.readAccelerometer(Y_AXIS);
 int z_axis = Esplora.readAccelerometer(Z_AXIS);

 Serial.print("x: ");
 Serial.print(x_axis);
 Serial.print("\ty: ");
 Serial.print(y_axis);
 Serial.print("\tz: ");
 Serial.println(z_axis);

 delay(500);
}
```

---

### `readButton()`
#### Description

Reads a button's state and returns if it is HIGH or LOW.

#### Syntax
```
Esplora.readButton(button)
```
#### Parameters
button: the associated button that you wanto read. Valid argument are:

- SWITCH_1 or SWITCH_DOWN
- SWITCH_2 or SWITCH_LEFT
- SWITCH_3 or SWITCH_UP
- SWITCH_4 or SWITCH_RIGHT
 
- JOYSTICK_DOWN = JOYSTICK_BASE
- JOYSTICK_LEFT = JOYSTICK_BASE+1
- JOYSTICK_UP = JOYSTICK_BASE+2
- JOYSTICK_RIGHT = JOYSTICK_BASE+3
#### Returns
LOW when pressed, HIGH when not pressed.

#### Example
```
#include <Esplora.h>

void setup(){}

void loop()
{
int button = Esplora.readButton(SWITCH_DOWN);

if(button == LOW)
  {
    Esplora.writeRed(255);
  }
else {
    Esplora.writeRed(0);
  }
}
```

---

### `readJoystickX()`
#### Description

Read the position of the X-axis of the joystick. When the joystick is in the center, it returns zero. Positive values indicate the joystick has moved to the right and negative values when moved to the left.

#### Syntax
```
Esplora.readJoystickX()
```
#### Parameters
none

#### Returns
int : 0 when the joystick is in the middle of the x-axis; 1 to 512 when the joystick is moved to the right; -1 to -512 when the joystick is moved to the left.

#### Example
```
#include <Esplora.h>

void setup()
{
Serial.begin(9600);
}

void loop()
{
int value = Esplora.readJoystickX();
Serial.println(value);

delay(1000);
}
```

---

### `readJoystickY()`
#### Description

Read the position of the Y-axis of the joystick. When the joystick is in the center, it returns zero. Positive values indicate the joystick has moved up and negative values when moved down.

#### Syntax
```
Esplora.readJoystickY()
```
#### Parameters
none

#### Returns
int : 0 when the joystick is in the middle of the y-axis; 1 to 512 when the joystick is moved up; -1 to -512 when the joystick is moved down.

#### Example
```
#include <Esplora.h>

void setup()
{
Serial.begin(9600);
}

void loop()
{
int value = Esplora.readJoystickY();
Serial.println(value);

delay(1000);
}
```

---

### `writeRGB()`
#### Description

Write values representing brightness to the RGB LED. By mixing different values, it's possible to create different color combinations.

#### Syntax
```
Esplora.writeRGB(red, green, blue)
```
#### Parameters
- red: int, value is to set the red LED brightness. Range 0 to 255
- green: int, value is to set the green LED brightness. Range 0 to 255
- blue: int, value is to set the blue LED brightness. Range 0 to 255
#### Returns
nothing

#### Example
```
#include <Esplora.h>

void setup() {}

void loop()
{
 Esplora.writeRGB(0, 128, 255);
 delay(1000);
 Esplora.writeRGB(255, 0, 128);
 delay(1000);
 Esplora.writeRGB(128, 255, 0);
 delay(1000);
}
```

---

### `writeRed()`
#### Description

Write values to the red LED that correspond to the brightness.

#### Syntax
```
Esplora.writeRed(value)
```
#### Parameters
value: int, value to set the red LED brightness. Range 0 to 255

#### Returns
nothing

#### Example
```
#include <Esplora.h>

void setup() {}

void loop()
{
 for(int i=0; i<256; i++)
 {
  Esplora.writeRed(i);
  delay(100);
 }
}
```

---

### `writeGreen()`
#### Description

Write values to the green LED that correspond to the brightness.

#### Syntax
```
Esplora.writeGreen(value)
```
#### Parameters
value: int, value to set the green LED brightness. Range 0 to 255

#### Returns
nothing

#### Example
```
#include <Esplora.h>

void setup() {}

void loop()
{
 for(int i=0; i<256; i++)
 {
  Esplora.writeGreen(i);
  delay(100);
 }
}
```

---

### `writeBlue()`
#### Description

Write values to the blue LED that correspond to the brightness.

#### Syntax
```
Esplora.writeBlue(value)
```
#### Parameters
value: int, value to set the blue LED brightness. Range 0 to 255

#### Returns
nothing

#### Example
```
#include <Esplora.h>

void setup() {}

void loop()
{
 for(int i=0; i<256; i++)
 {
  Esplora.writeBlue(i);
  delay(100);
 }
}
```

---

### `readRed()`
#### Description

Read the brightness value of the red LED.

#### Syntax
```
Esplora.readRed()
```
#### Parameters
none

#### Returns
int : the brightness of the red LED between 0 and 255.

#### Example
```
#include <Esplora.h>

void setup()
{
 Serial.begin(9600);
}

void loop()
{
 int dimmerValue = Esplora.readSlider();
 Esplora.writeRed(dimmerValue);
 Serial.println(Esplora.readRed());

 delay(500);
}
```

---

### `readGreen()`
#### Description

Read the brightness value of the green LED.

#### Syntax
```
Esplora.readGreen()
```
#### Parameters
none

#### Returns
int : the brightness of the green LED between 0 and 255.

#### Example
```
#include <Esplora.h>

void setup()
{
 Serial.begin(9600);
}

void loop()
{
 int dimmerValue = Esplora.readSlider();
 Esplora.writeGreen(dimmerValue);
 Serial.println(Esplora.readGreen());

 delay(500);
}
```

---

### `readBlue()`
#### Description

Read the brightness value of the blue LED.

#### Syntax
```
Esplora.readBlue()
```
#### Parameters
none

#### Returns
int : the brightness of the blue LED between 0 and 255.

#### Example
```
#include <Esplora.h>

void setup()
{
 Serial.begin(9600);
}

void loop()
{
 int dimmerValue = Esplora.readSlider();
 Esplora.writeBlue(dimmerValue);
 Serial.println(Esplora.readBlue());

 delay(500);
}
```

---

### `tone()`
#### Description

Generates a square wave of the specified frequency from the Esplora's onboard buzzer. A duration can be specified in milliseconds, otherwise the wave continues until a call to Esplora.noTone().

Only one tone can be generated at a time. If a tone is already playing, the call will set its frequency.

Use of the tone() function will interfere with fading the red LED.

#### Syntax
```
Esplora.tone(frequency, duration)
```
#### Parameters
frequency: the frequency of the tone in hertz - unsigned int

duration: the duration of the tone in milliseconds (optional) - unsigned long

#### Returns
nothing

---

### `noTone()`
#### Description

Stops the generation of a square wave triggered by Esplora.tone(). Has no effect if no tone is being generated.

#### Syntax
```
Esplora.noTone()
```
#### Parameters
none

#### Returns
nothing