---
title: 'Accessing Accelerometer Data on Nano 33 BLE'
difficulty: intermediate
compatible-products: [nano-33-ble]
description: 'Learn how to measure the relative position of the Nano 33 BLE through the LSM9DS1 IMU sensor.'
tags:
  - IMU
  - Accelerometer
author: 'Nefeli Alushi'
libraries: 
  - name:  Arduino LSM9DS1
    url: https://www.arduino.cc/en/Reference/ArduinoLSM9DS1
hardware:
  - hardware/03.nano/boards/nano-33-ble
software:
  - web-editor
featuredImage: 'chip'
---

This tutorial will focus on the 3-axis accelerometer sensor of the **LSM9DS1** module on the Arduino Nano 33 BLE, in order to measure the relative position of the board. This will be achieved by utilizing the values of the accelerometer's axes and later print the return values through the Arduino IDE Serial Monitor.


## Goals

The goals of this project are:

- Understand what an LSM9DS1 module is.
- Use the LSM9DS1 library.
- Read the raw data of the accelerometer sensor.
- Convert the raw data into board positions.
- Print out live data through the Serial Monitor.


## Hardware & Software Needed

- This project uses no external sensors or components.
- In this tutorial we will use the Arduino Create Cloud Editor to program the board.


## The LSM9DS1 Inertial Module

IMU stands for: inertial measurement unit. It is an electronic device that measures and reports a body's specific force, angular rate and the orientation of the body, using a combination of accelerometers, gyroscopes, and oftentimes magnetometers. In this tutorial we will learn about the LSM9DS1 IMU module, which is included in the Arduino Nano 33 BLE Board.

![The LSM9DS1 sensor.](./assets/nano33BLE_01_IMU.png)

The LSM9DS1 is a system-in-package featuring a 3D digital linear acceleration sensor, a 3D digital angular rate sensor, and a 3D digital magnetic sensor.


### The LSM9DS1 Library
The Arduino LSM9DS1 library allows us to use the Arduino Nano 33 BLE IMU module without having to go into complicated programming. The library takes care of the sensor initialization and sets its values as follows:

- **Accelerometer** range is set at [-4, +4]g -/+0.122 mg.
- **Gyroscope** range is set at [-2000, +2000] dps +/-70 mdps.
- **Magnetometer** range is set at [-400, +400] uT +/-0.014 uT.
- **Accelerometer** output data rate is fixed at 104 Hz.
- **Gyroscope** output data rate is fixed at 104 Hz.
- **Magnetometer** output data rate is fixed at 20 Hz.

If you want to read more about the LSM9DS1 sensor module see <a href="https://www.st.com/resource/en/datasheet/lsm9ds1.pdf" target="_blank">here</a>.


### Accelerometer

An accelerometer is an electromechanical device used to measure acceleration forces. Such forces may be static, like the continuous force of gravity or, as is the case with many mobile devices, dynamic to sense movement or vibrations.

![How the accelerometer works.](./assets/nano33BLE_01_acceleration.png)

In this example, we will use the accelerometer as a "level" that will provide information about the position of the board. With this application we will be able to read what the relative position of the board is as well as the degrees, by tilting the board up, down, left or right.


## Creating the Program

**1. Setting up**


Let's start by opening the Arduino Cloud Editor, click on the **Libraries** tab and search for the **LSM9DS1** library. Then in **Examples**, open the **SimpleAccelerometer** sketch and once it opens, rename it as **Accelerometer**.

![Finding the library in the Cloud Editor.](./assets/nano33BLE_01_include_library.png)

**2. Connecting the board**

Now, connect the Arduino Nano 33 BLE to the computer and make sure that the Cloud Editor recognizes it, if so, the board and port should appear as shown in the image below. If they don't appear, follow the [instructions](https://create.arduino.cc/getting-started/plugin/welcome) to install the plugin that will allow the Editor to recognize your board.

Now, connect the Arduino Nano 33 BLE to the computer and make sure that the Cloud Editor recognizes it. If so, the board and port should appear as shown in the image below. If they don't appear, follow the [instructions](https://create.arduino.cc/getting-started/plugin/welcome) to install the plugin that will allow the Editor to recognize your board.

![Selecting the board.](assets/nano33BLE_01_board_port.png)

### 3. Writing the Code

Now we will write the code to read the accelerometer data, calculate the tilt angles, and print the relative position of the board as we move it at different angles.

Include the LSM9DS1 library at the top of your sketch:

```arduino
#include <Arduino_LSM9DS1.h>
```

Initialize variables before the `setup()` function:

```arduino
#define MINIMUM_TILT 5    // Threshold for tilt detection in degrees
#define WAIT_TIME 500     // How often to run the code (in milliseconds)

float x, y, z;
int angleX = 0;
int angleY = 0;
unsigned long previousMillis = 0;
```

In the `setup()`, initialize the IMU and start serial communication:

```arduino
void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
}
```

**Write the `loop()` function to read accelerometer data and calculate tilt angles:**

```arduino
void loop() {
  unsigned long currentMillis = millis();

  if (IMU.accelerationAvailable() && (currentMillis - previousMillis >= WAIT_TIME)) {
    previousMillis = currentMillis;

    IMU.readAcceleration(x, y, z);

    // Calculate tilt angles in degrees
    angleX = atan2(x, sqrt(y * y + z * z)) * 180 / PI;
    angleY = atan2(y, sqrt(x * x + z * z)) * 180 / PI;

    // Determine the tilting direction based on angleX and angleY
    if (angleX > MINIMUM_TILT) {  // Tilting up
      Serial.print("Tilting up ");
      Serial.print(angleX);
      Serial.println(" degrees");
    } else if (angleX < -MINIMUM_TILT) {  // Tilting down
      Serial.print("Tilting down ");
      Serial.print(-angleX);
      Serial.println(" degrees");
    }

    if (angleY > MINIMUM_TILT) {  // Tilting left
      Serial.print("Tilting left ");
      Serial.print(angleY);
      Serial.println(" degrees");
    } else if (angleY < -MINIMUM_TILT) {  // Tilting right
      Serial.print("Tilting right ");
      Serial.print(-angleY);
      Serial.println(" degrees");
    }
  }
}
```

In this code, we use trigonometric functions to calculate the tilt angles from the accelerometer data. The `MINIMUM_TILT` variable is used to ignore small movements below a certain threshold.

> **Note:** For the following code to work properly, the board's facing direction and inclination during the initialization of the code need to be specific. More information will be shared in the "Testing It Out" section.

**Complete Code**

If you choose to skip the code-building section, the complete code can be found below:

```arduino
/*
  Arduino LSM9DS1 - Accelerometer Application

  This example reads the acceleration values as relative direction and degrees,
  from the LSM9DS1 sensor and prints them to the Serial Monitor.

  The circuit:
  - Arduino Nano 33 BLE

  Created by Pedro Lima

  This example code is in the public domain.
*/

#include <Arduino_LSM9DS1.h>

#define MINIMUM_TILT 5    // Threshold for tilt detection in degrees
#define WAIT_TIME 500     // How often to run the code (in milliseconds)

float x, y, z;
int angleX = 0;
int angleY = 0;
unsigned long previousMillis = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
}

void loop() {
  unsigned long currentMillis = millis();

  if (IMU.accelerationAvailable() && (currentMillis - previousMillis >= WAIT_TIME)) {
    previousMillis = currentMillis;

    IMU.readAcceleration(x, y, z);

    // Calculate tilt angles in degrees
    angleX = atan2(x, sqrt(y * y + z * z)) * 180 / PI;
    angleY = atan2(y, sqrt(x * x + z * z)) * 180 / PI;

    // Determine the tilting direction based on angleX and angleY
    if (angleX > MINIMUM_TILT) {  // Tilting up
      Serial.print("Tilting up ");
      Serial.print(angleX);
      Serial.println(" degrees");
    } else if (angleX < -MINIMUM_TILT) {  // Tilting down
      Serial.print("Tilting down ");
      Serial.print(-angleX);
      Serial.println(" degrees");
    }

    if (angleY > MINIMUM_TILT) {  // Tilting left
      Serial.print("Tilting left ");
      Serial.print(angleY);
      Serial.println(" degrees");
    } else if (angleY < -MINIMUM_TILT) {  // Tilting right
      Serial.print("Tilting right ");
      Serial.print(-angleY);
      Serial.println(" degrees");
    }
  }
}
```


## Testing It Out
In order to get a correct reading of the board data, before uploading the sketch to the board hold the board in your hand, from the side of the USB port. The board should be facing up and "pointing" away from you. The image below illustrates the board's position and how it works:

![Interacting with the X and Y axes.](./assets/nano33BLE_01_illustration.png)

Now, you can verify and upload the sketch to the board and open the Monitor from the menu on the left.  

If you tilt the board upwards, downwards, right or left, you will see the results printing every second according to the direction of your movement!


Here is a screenshot of the sketch returning these values:

![Printing out the "tilt condition" of the board.](./assets/nano33BLE_01_printing_values.png)



### Troubleshoot

Sometimes errors occur, if the code is not working there are some common issues we can troubleshoot:
- Missing a bracket or a semicolon.

- Arduino board connected to the wrong port.
- Accidental interruption of cable connection.
- The initial position of the board is not as instructed. In this case you can refresh the page and try again.



## Conclusion

In this simple tutorial we learned what an IMU sensor module is, how to use the **LSM9DS1** library, and how to use an Arduino Nano 33 BLE to get data. Furthermore, we utilized the 3-axis accelerometer sensor, in order to measure and print out the degrees and relative position of the board.
