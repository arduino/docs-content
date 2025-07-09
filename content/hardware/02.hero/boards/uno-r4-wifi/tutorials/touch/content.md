---
title: Uno R4 Capacitor Tutorial
description: Learn to use the built-in capacitive sensing capabilities of the Arduino® Uno R4.
tags: [Arduino, Capacitive Sensing, Uno R4]
author: Pedro Lima
---

Capacitive sensing is a technology that detects changes in capacitance to determine the presence or absence of a conductive object, such as a human finger. This principle is widely used in touch-sensitive devices. The Arduino® Uno R4, both the [WiFi](https://store.arduino.cc/products/arduino-uno-r4-wifi) and [Minima](https://store.arduino.cc/products/arduino-uno-r4-minima) versions, come equipped with built-in capacitive sensing capabilities, making it easier to integrate touch inputs into your projects.

![Sensor Example](assets/Touch_Cover_001.gif)

## How Capacitive Sensing Works

Imagine the sensor as creating an invisible electric field around itself. When a conductive object (like your finger) approaches, it's like dropping a stone into a calm pond - the field gets disturbed. The sensor detects this disturbance as a change in capacitance, which is essentially how much electrical charge the system can store.
Here's the process:

1. The sensor generates a small electric field
2. When you touch or approach the sensor, your body acts like a conductor
3. This changes the capacitance of the system
4. The microcontroller measures this change and determines if it's significant enough to register as a "touch"



## Using Capacitive Sensing on the Uno R4

The Uno R4 features a Capacitive Touch Sensing Unit (CTSU) that allows you to use certain pins as capacitive touch inputs. To utilize these capabilities, you can use the [Arduino_CapacitiveTouch library](https://github.com/arduino-libraries/Arduino_CapacitiveTouch).

### Compatible Pins

For both the Uno R4 WiFi and Minima, the compatible pins for capacitive touch are listed in the [Arduino_CapacitiveTouch library documentation](https://github.com/arduino-libraries/Arduino_CapacitiveTouch?tab=readme-ov-file#compatible-pins).

**Arduino® UNO-R4 Minima:**
| Arduino Pin  | Touch Sensor Channel (TS#) | Channel Control Index (CHAC idx) | Channel Control Bit Mask (CHAC val) |
|--------------|----------------------------|----------------------------------|-------------------------------------|
| D0           | 9                          | 1                                | (1 << 1)                           |
| D1           | 8                          | 1                                | (1 << 0)                           |
| D2           | 34                         | 4                                | (1 << 2)                           |
| D3           | 13                         | 1                                | (1 << 5)                           |
| D8           | 11                         | 1                                | (1 << 3)                           |
| D9           | 2                          | 0                                | (1 << 2)                           |
| D11          | 10                         | 1                                | (1 << 2)                           |
| D13          | 12                         | 1                                | (1 << 4)                           |
| A1 (D15)     | 21                         | 2                                | (1 << 5)                           |
| A2 (D16)     | 22                         | 2                                | (1 << 6)                           |
| LOVE_BUTTON  | 0                          | 0                                | (1 << 0)                           |

**Arduino® UNO-R4 WiFi:**
| Arduino Pin  | Touch Sensor Channel (TS#) | Channel Control Index (CHAC idx) | Channel Control Bit Mask (CHAC val) |
|--------------|----------------------------|----------------------------------|-------------------------------------|
| D0           | 9                          | 1                                | (1 << 1)                           |
| D1           | 8                          | 1                                | (1 << 0)                           |
| D2           | 13                         | 1                                | (1 << 5)                           |
| D3           | 34                         | 4                                | (1 << 2)                           |
| D6           | 12                         | 1                                | (1 << 4)                           |
| D8           | 11                         | 1                                | (1 << 3)                           |
| D9           | 2                          | 0                                | (1 << 2)                           |
| D11          | 7                          | 0                                | (1 << 7)                           |
| D12          | 6                          | 0                                | (1 << 6)                           |
| A1 (D15)     | 21                         | 2                                | (1 << 5)                           |
| A2 (D16)     | 22                         | 2                                | (1 << 6)                           |
| LOVE_BUTTON  | 27                         | 3                                | (1 << 3)                           |


### Library Functions

The Arduino_CapacitiveTouch library provides several functions to work with capacitive touch inputs:

- **```CapacitiveTouch(uint8_t pin)```** Constructs a capacitive touch sensor for the given pin.
- **```bool begin()```** Initializes the sensor and configures the pin and hardware.
- **```int read()```** Reads the raw sensor value and returns it.
- **```bool isTouched()```** Checks if the sensor is touched based on the threshold.
- **```void setThreshold(int threshold)```** Sets the detection threshold for touch sensitivity.
- **```int getThreshold()```** Retrieves the current detection threshold.

For more detailed usage and examples, refer to the [CapacitiveSensor library documentation](https://docs.arduino.cc/libraries/capacitivesensor/).

## Example Code

Here's a simple example to get you started with capacitive sensing on the Uno R4.
For this example we are connecting a single piece of any conductive material to the pin ```D0``` on the Board.

![How to connect](assets/HoockupGuideExample.png)

**Note:**
You will first need to install the library [Arduino_CapacitiveTouch](https://docs.arduino.cc/libraries/capacitivesensor/):
```Arduino IDE: Library Manager → Search "Arduino_CapacitiveTouch" → Install```

```ARDUINO
#include "Arduino_CapacitiveTouch.h"

CapacitiveTouch touchButton = CapacitiveTouch(D0);

void setup() {
  Serial.begin(9600);
  
  if(touchButton.begin()){
    Serial.println("Capacitive touch sensor initialized.");
  } else {
    Serial.println("Failed to initialize capacitive touch sensor. Please use a supported pin.");
    while(true);
  }

  touchButton.setThreshold(2000);
}

void loop() {
  int sensorValue = touchButton.read();
  Serial.print("Raw value: ");
  Serial.println(sensorValue);

  if (touchButton.isTouched()) {
    Serial.println("Button touched!");
  }
  
  delay(100);
}
```

## Creative Project Ideas
Now that you understand the basics, here are some project ideas:

**Touch-Controlled Night Light -** Create a lamp that turns on/off with a touch
**Capacitive Touch Piano -** Use multiple pins to create touch-sensitive keys
**Smart Home Controller -** Touch different areas to control various devices
**Interactive Art Installation -** Create touch-responsive visual or audio effects

## Conclusion

The built-in capacitive sensing capabilities of the Arduino® Uno R4 provide an excellent way to add touch inputs to your projects. By leveraging the Arduino_CapacitiveTouch library, you can easily integrate touch-sensitive features, enhancing the interactivity and functionality of your designs. Whether you're building a simple touch interface or a more complex interactive system, the Uno R4's capacitive sensing features offer a versatile and user-friendly solution.
Remember to experiment with threshold values and consider the environment where your project will be used, as factors like humidity and nearby electronics can affect sensitivity. With practice, you'll develop an intuitive understanding of how to tune these sensors for optimal performance in your specific applications.
