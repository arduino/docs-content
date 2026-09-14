---
title: 'Accessing Accelerometer Data on Nano 33 BLE Rev2'
difficulty: intermediate
compatible-products: [nano-33-ble-rev2]
description: 'Learn how to measure the relative position of the Nano 33 BLE Rev2 through the BMi270 and BMM150 IMU system.'
tags:
  - IMU
  - Accelerometer
author: 'Nefeli Alushi'
libraries: 
  - name:  Arduino BMI270_BMM150
    url: https://www.arduino.cc/reference/en/libraries/arduino_bmi270_bmm150/
hardware:
  - hardware/03.nano/boards/nano-33-ble-rev2
software:
  - cloud-editor
  - ide-v1
  - ide-v2
---

This tutorial will focus on the IMU system with the **BMI270 and BMM150** modules on the Arduino Nano 33 BLE Rev2, to measure the relative position of the board. This will be achieved by utilizing the values of the accelerometer's axes and later printing the return values through the Arduino IDE Serial Monitor.


## Goals

The goals of this project are:
- Understand how the IMU system on the Nano 33 BLE Rev2 works.
- Use the BMI270_BMM150 library.
- Read the raw data of the accelerometer sensor.
- Convert the raw data into board positions.
- Print out live data through the Serial Monitor.


## Hardware & Software Needed
* This project uses no external sensors or components apart from the Arduino Nano 33 BLE Rev2.
* In this tutorial, we will use the Arduino Cloud Editor to program the board.


## The IMU System on Nano 33 BLE Rev2

IMU (Inertial Measurement Unit)  is an electronic device that measures and reports a body's specific force, angular rate and the orientation of the body, using a combination of accelerometers, gyroscopes, and oftentimes magnetometers. In this tutorial, we will learn about the IMU system that is included in the Nano 33 BLE Rev2 Board.

![The Nano 33 BLE Rev2 IMU system.](./assets/Nano33_ble_rev2_imu.png)

The IMU system on the Nano 33 BLE Rev2 is a combination of two modules, the 6-axis BMI270, and the 3-axis BMM150, that together add up to a combined 9-axis IMU system that can measure acceleration, as well as rotation and magnetic fields all in 3D space.


### The BMI270_BMM150 Library
The Arduino BMI270_BMM150 library allows us to use the Nano 33 BLE Rev2 IMU system without having to go into complicated programming. The library takes care of the sensor initialization and sets its values as follows:

- **Accelerometer** range is set at [-4, +4]g -/+0.122 mg.
- **Gyroscope** range is set at [-2000, +2000] dps +/-70 mdps.
- **Magnetometer** range is set at [-400, +400] uT +/-0.014 uT.
- **Accelerometer** Output data rate is fixed at 104 Hz.
- **Gyroscope** Output data rate is fixed at 104 Hz.
- **Magnetometer** Output data rate is fixed at 20 Hz.

If you want to read more about the sensor modules that make up the IMU system, find the datasheet for the [BMI270](https://download.mikroe.com/documents/datasheets/bst-bmi270-ds000-2_datasheet.pdf) and the [BMM150](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmm150-ds001.pdf) here.


### Accelerometer

An accelerometer is an electromechanical device used to measure acceleration forces. Such forces may be static, like the continuous force of gravity or, as is the case with many mobile devices, dynamic to movement or vibrations.

![How the accelerometer works.](./assets/nano33B_02_acceleration.png)

In this example, we will use the accelerometer as a "level" that will provide information about the position of the board. With this application, we will be able to read the relative position of the board as well as the degrees, by tilting the board up, down, left or right.



## Creating the Program

**1. Setting up**

Let's start by opening the Arduino Cloud Editor, clicking on the **Libraries** tab, and searching for the **Arduino_BMI270_BMM150** library. Then, in **Examples**, open the **SimpleAccelerometer** sketch and once it opens, rename it as **Accelerometer**.

![Finding the library in the Cloud Editor.](./assets/nano33B_02_include_library.png)

**2. Connecting the board**

Now, connect the Arduino Nano 33 BLE Sense Rev2 to the computer and make sure that the Cloud Editor recognizes it. If so, the board and port should appear as shown in the image below. If they don't appear, follow the [instructions](https://create.arduino.cc/getting-started/plugin/welcome) to install the plugin that will allow the editor to recognize your board.

![Selecting the board.](assets/nano33B_02_board_port.png)

**3. Printing the relative position**

Now we will need to modify the code in the example to print the relative position of the board as we move it at different angles.

First, include the BMI270_BMM150 library at the top of your sketch:

```arduino
#include "Arduino_BMI270_BMM150.h"
```

Then, initialize variables before the `setup()` function:

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
  Serial.println("Hz");
}
```

In the `loop()` function, we will read the accelerometer data and calculate the tilt angles:

```arduino
void loop() {
  if (IMU.accelerationAvailable() && millis() - previousMillis >= WAIT_TIME) {
    previousMillis = millis();
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

    if (angleY > MINIMUM_TILT) {  // Tilting right
      Serial.print("Tilting right ");
      Serial.print(angleY);
      Serial.println(" degrees");
    } else if (angleY < -MINIMUM_TILT) {  // Tilting left
      Serial.print("Tilting left ");
      Serial.print(-angleY);
      Serial.println(" degrees");
    }
  }
}
```

> **Note:** For the following code to work properly, the board's facing direction and inclination during the initialization of the code need to be specific. More information will be shared in the "Testing It Out" section.

**4. Complete code**

If you choose to skip the code-building section, the complete code can be found below:

```arduino
/*
  Arduino BMI270_BMM150 - Accelerometer Application

  This example reads the acceleration values as relative direction and degrees,
  from the BMI270 sensor and prints them to the Serial Monitor.

  The circuit:
  - Arduino Nano 33 BLE Sense Rev2

  Created by Pedro Lima

  This example code is in the public domain.
*/

#include "Arduino_BMI270_BMM150.h"

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
  Serial.println("Hz");
}

void loop() {
  if (IMU.accelerationAvailable() && millis() - previousMillis >= WAIT_TIME) {
    previousMillis = millis();
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

    if (angleY > MINIMUM_TILT) {  // Tilting right
      Serial.print("Tilting right ");
      Serial.print(angleY);
      Serial.println(" degrees");
    } else if (angleY < -MINIMUM_TILT) {  // Tilting left
      Serial.print("Tilting left ");
      Serial.print(-angleY);
      Serial.println(" degrees");
    }
  }
}
```


## Testing It Out

To get a correct reading of the board data, before uploading the sketch to the board hold the board in your hand, from the side of the USB port. The board should be facing up and "pointing" away from you. The image below illustrates the board's position and how it works:

![Interacting with the X and Y axes.](./assets/nano33B_02_illustration.png)

Now, you can verify and upload the sketch to the board and open the Monitor from the menu on the left.  

If you tilt the board upwards, downwards, right or left, you will see the results printing every second according to the direction of your movement!


Here is a screenshot of the sketch returning these values:

![Printing out the "tilt condition" of the board.](./assets/nano33B_02_printing_values.png)


### Troubleshoot

Sometimes errors occur, if the code is not working there are some common issues we can troubleshoot:
- Missing a bracket or a semicolon.
- The Arduino board is connected to the wrong port.
- Accidental interruption of cable connection.
- The initial position of the board is not as instructed. In this case, you can refresh the page and try again.



## Conclusion

In this simple tutorial, we learned what an IMU sensor module is, how to use the **BMI270_BMM150** library, and how to use an Arduino Nano 33 BLE Rev2 to get data. Furthermore, we utilized the 3-axis accelerometer sensor, in order to measure and print out the degrees and relative position of the board.
