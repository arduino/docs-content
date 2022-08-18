---
title: 'Curie IMU Library'
description: 'The Curie IMU library enables an Arduino or Genuino 101 to read the output of the on-board IMU'
author: Arduino
---


***This library is included in the [Arc32 core](https://github.com/arduino/ArduinoCore-arc32/tree/master/libraries). This core can be installed through the Arduino IDEs , where the package is named "Intel Curie Boards".*** 

The Curie IMU library enables an Arduino or Genuino 101 to read the output of the on-board IMU [(Inertial Measurement Unit)](https://en.wikipedia.org/wiki/Inertial_measurement_unit) containing an accelerometer and a gyroscope and elaborate the raw data coming from it.

To use this library:
```
#include <CurieIMU.h>
```


## Examples

- [Curie IMU Orientation Visualizer](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMUOrientationVisualiser)
- [Curie IMU Accelerometer](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMUAccelerometer)
- [Curie IMU Accelerometer Orientation](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMUAccelerometerOrientation)
- [Curie IMU Gyro](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMUGyro)
- [Curie IMU Raw Imu Data Serial](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMURawImuDataSerial)
- [Curie IMU Shock Detect](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMUShockDetect)
- [Curie IMU Step Count](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMUStepCount)
- [Curie IMU Tap Detect](https://www.arduino.cc/en/Tutorial/Genuino101CurieIMUTapDetect)


## Functions 

---

### `begin()`
#### Description
Initializes the Arduino and Genuino 101 IMU. begin() needs to be called before any other CurieIMU library function.

#### Syntax
```
CurieIMU.begin()
```
#### Parameters
none

---

### `getGyroRate()`
#### Description
Return the gyro data rate, that is the frequency at which the gyroscope is read.

#### Syntax
```
CurieIMU.getGyroRate()
```
#### Returns
 The gyro data rate expressed in Hz.
Allowed values are:

25,
50,
100,
200,
400,
800,
1600,
3200

---

### `setGyroRate()`
#### Description
Defines the output data rate of the gyroscope. The data rate is also the sampling frequency and affects the bandwidth of the readings.

#### Syntax
```
CurieIMU.setGyroRate(int rate)
```
#### Parameters
rate: the rate to be set
It can assume one of the following values:

25,
50,
100,
200,
400,
800,
1600,
3200

---

### `setGyroRange()`

#### Description
Sets the gyro angular measurement range.

#### Syntax

```
CurieIMU.setGyroRange()
```

#### Parameters
range: the range to be set.

Allowed values are:

- 2000 (+/-2000°/s)
- 1000 (+/-1000°/s)
- 500 (+/-500°/s)
- 250 (+/-250°/s)
- 125 (+/-125°/s)

---

### `getAccelerometerRate()`
#### Description
Return the accelerometer data rate, that is the frequency - expressed in Hz - at which the accelerometer is read.

#### Syntax
```
CurieIMU.getAccelerometerRate()
```
#### Returns
The accelerometer rate in Hz.
Values returned are:

- 12.5,
- 25,
- 50,
- 100,
- 200,
- 400,
- 800,
- 1600

---

### `setAccelerometerRate()`
#### Description
Defines the output data rate of the accelerometer. The data rate is also the sampling frequency and affects the bandwidth of the readings.

#### Syntax
```
CurieIMU.setAccelerometerRate(float rate)
```
#### Parameters
rate: the rate to be set in Hz.
Allowed values are:

12.5,
25,
50,
100,
200,
400,
800,
1600

---

### `getGyroRange()`
#### Description
Returns the gyro angular measurement range.

#### Syntax
```
CurieIMU.getGyroRange()
```
#### Returns
 The gyro angular range.
Returned values are:

2000 (+/-2000°/s),
1000 (+/-1000°/s),
500 (+/-500°/s),
250 (+/-250°/s),
125 (+/-125°/s)

---

### `getAccelerometerRange()`
#### Description
Returns the accelerometer range.

#### Syntax
```
CurieIMU.getAccelerometerRange()
```
#### Returns
 The accelerometer range expressed as multiples of g.
Returned values are:

2 (+/- 2g),
4 (+/- 4g),
8 (+/- 8g),
16 (+/- 16g)

---

### `setAccelerometerRange()`
#### Description
Sets the accelerometer range as multiples of g.

#### Syntax
```
CurieIMU.setAccelerometerRange(int range)
```
#### Parameters
range: the range to be set expressed as multiples of g.
Allowed values are:

2 (+/- 2g),
4 (+/- 4g),
8 (+/- 8g),
16 (+/- 16g)

---

### `autoCalibrateGyroOffset()`
#### Description
Starts an autocalibration of the gyro's offset. During this procedure the board should stay motionless. When finished, this procedure writes the proper offset value in the IMU register that can be read with getGyroOffset.

#### Syntax
```
CurieIMU.autoCalibrateGyroOffset()
```
#### Parameters
none

---

### `autoCalibrateAccelerometerOffset()`
#### Description
Starts an auto-calibration of the accelerometer's offset for the axis specified as argument. This procedure should be executed while the board is kept laying flat and motionless. The offset is stored in the IMU registers and can be read with getAccelerometerOffset.

#### Syntax
```
CurieIMU.autoCalibrateAccelerometerOffset(int, axis, int target)
```
#### Parameters
axis: the axis to calibrate. It can assume one of these values:
```
X_AXIS 
Y_AXIS
Z_AXIS
```
target: it can be 0 or 1. In particular it has to be used in this way:
```
CurieIMU.autoCalibrateAccelerometerOffset(X_AXIS, 0);
CurieIMU.autoCalibrateAccelerometerOffset(Y_AXIS, 0);
CurieIMU.autoCalibrateAccelerometerOffset(Z_AXIS, 1);
```
The target for Z is 1 because it represents the vertical force of gravity (1g) that should be read when the board is laying flat.

---

### `noGyroOffset()`
#### Description
Disables the gyro offset.

#### Syntax
```
CurieIMU.noGyroOffset()
```
#### Returns
 none

---

### `noAccelerometerOffset()`
#### Description
Disables the accelerometer offset.

#### Syntax
```
CurieIMU.noAccelerometerOffset()
```
#### Returns
 none

---

### `gyroOffsetEnabled()`
#### Description
Returns the enable state of the gyro offset

#### Syntax
```
CurieIMU.gyroOffsetEnabled()
```
#### Returns
 true or false if the feature is enabled or disabled

---

### `accelerometerOffsetEnabled()`
#### Description
Returns the enable state of the accelerometer offset

#### Syntax
```
CurieIMU.accelerometerOffsetEnabled()
```
#### Returns
 true or false if the feature is enabled or disabled

---

### `getGyroOffset()`
#### Description
Returns the value of gyro's offset.

#### Syntax
```
CurieIMU.getGyroOffset(int axis)
```
#### Parameters
axis: the target axis. Can be one of these values:
```
X_AXIS
Y_AXIS
Z_AXIS
```
#### Returns
 The value of the offset for the selected axis. The returned value is from -31.25 °/s to +31.25 °/s in discrete steps of 0.061 °/s.

---

### `getAccelerometerOffset()`
#### Description
Returns the value of accelerometer's offset for the selected axis

#### Syntax
```
CurieIMU.getAccelerometerOffset(int axis)
```
#### Parameters
axis: the axis of which we want to get the offset value. Can be one of these values:
```
X_AXIS
Y_AXIS
Z_AXIS
```
#### Returns
The value of the offset for the selected axis. The value returned varies from -495.3 mg to + 495.3 mg in discrete steps of 3.9mg.

---

### `setGyroOffset()`
#### Description
Sets the value of gyro offset

#### Syntax
```
CurieIMU.setGyroOffset(int axis, int offset)
```
#### Parameters
axis: the target axis. Can be one of these values:
```
X_AXIS
Y_AXIS
Z_AXIS
```
offset: the value of the offset to be set. Valid values are from -31.25 °/s to +31.25 °/s in discrete steps of 0.061 °/s.

---

### `setAccelerometerOffset()`
#### Description
Sets the value of accelerometer offset

#### Syntax
```
CurieIMU.setAccelerometerOffset(int axis, int offset)
```
#### Parameters
axis: the target axis. Can be one of these values:
```
X_AXIS
Y_AXIS
Z_AXIS
```
offset: The value of the offset for the selected axis. The value goes from -495.3 mg to + 495.3 mg independent of the range selected for the accelerometer; it varies in discrete steps of 3.9mg.

---

### `getDetectionThreshold()`
#### Description
Returns the value of the detection threshold

#### Syntax
```
CurieIMU.getDetectionThreshold(int feature)
```
#### Parameters
feature: the requested feature. It can assume one of these values:
```
CURIE_IMU_FREEFALL
CURIE_IMU_SHOCK
CURIE_IMU_MOTION
CURIE_IMU_ZERO_MOTION
CURIE_IMU_TAP
```

---

### `setDetectionThreshold()`
#### Description
Sets the value of the detection threshold.

#### Syntax
```
CurieIMU.getDetectionThreshold(int feature, float value)
```

#### Parameters
feature: the requested feature. It can assume one of these values:

- CURIE_IMU_FREEFALL
- CURIE_IMU_SHOCK
- CURIE_IMU_MOTION
- CURIE_IMU_ZERO_MOTION
- CURIE_IMU_TAP

value: the value to be set, expressed in mg, according to the accelerometer range set, as follows:

#### CURIE_IMU_FREEFALL
3.91 to 1995.46 mg, in steps of 7.81 mg


#### CURIE_IMU_SHOCK
2G: 3.91 to 1995.46 mg, in steps of 7.81 mg
4G: 7.81 to 3993.46 mg, in steps of 15.63 mg
8G: 15.63 to 7984.38 mg, in steps of 31.25 mg
16G: 31.25 to 15968.75 mg, in steps of 62.50 mg

#### CURIE_IMU_MOTION
2G: 0 to 997.05 mg, in steps of 3.91 mg
4G: 0 to 1991.55 mg, in steps of 7.81 mg
8G: 0 to 3985.65 mg, in steps of 15.63 mg
16G: 0 to 7968.75 mg, in steps of 31.25 mg

#### CURIE_IMU_ZERO_MOTION
2G: 0 to 997.05 mg, in steps of 3.91 mg
4G: 0 to 1991.55 mg, in steps of 7.81 mg
8G: 0 to 3985.65 mg, in steps of 15.63 mg
16G: 0 to 7968.75 mg, in steps of 31.25 mg

#### CURIE_IMU_TAP
2G: 31.25 to 7968.75 mg, in steps of 62.5 mg
4G: 62.50 to 31937.50 mg, in steps of 125.0 mg
8G: 125.0 to 63875.00 mg, in steps of 250.0 mg
16G: 250.0 to 127750.00 mg, in steps of 500 mg

#### Returns
The detection threshold of the chosen feature in mg. The range of the returned values is related to the Accelerometer range setting. See setDetectionThreshold for more details.

---

### `setDetectionDuration()`
#### Description
Sets the value of the detection duration or waiting window for the selected feature

#### Syntax
```
CurieIMU.setDetectionDuration(int feature, float value)
```
#### Parameters
feature: the requested feature. It can assume one of these values:
```
CURIE_IMU_FREEFALL
CURIE_IMU_SHOCK
CURIE_IMU_MOTION
CURIE_IMU_ZERO_MOTION
CURIE_IMU_DOUBLE_TAP
CURIE_IMU_TAP_SHOCK
CURIE_IMU_TAP_QUIET
```
value: the value to be set for each of the features. Some features allow a specific set of values as stated below:

CURIE_IMU_FREEFALL – interval of continuous 0g reading to trigger the interrupt
2.5 to 637.5 ms, in steps of 2.5 ms

CURIE_IMU_SHOCK - The duration of the shock (high-g) condition needed to trigger the interrupt; the sign of high-g must not change during the duration.
50, 75 ms

CURIE_IMU_MOTION - The number of consecutive samples where the threshold value must be exceeded to trigger the interrupt. To get the time correspondent to the samples, divide them by the sampling rate. The value calculated is in seconds.
from 1 to 4

CURIE_IMU_ZERO_MOTION - The amount of time where the acceleration read on any of the three axis must stay below the trigger level to activate the interrupt. The value is stored as six bit and is used with a multiplying factor of 1.28, 5.12 or 10.24 seconds.
1.28, 2.56, 3.84, 5.12, 6.40, 7.68, 8.96, 10.24, 11.52, 12.80, 14.08, 15.36, 16.64, 17.92, 19.20, 20.48, 25.60, 30.72, 35.84, 40.96, 46.08, 51.20, 56.32, 61.44, 66.56, 71.68, 76.80, 81.92, 87.04, 92.16, 97.28, 102.40, 112.64, 122.88, 133.12, 143.36, 153.60, 163.84, 174.08, 184.32, 194.56, 204.80, 215.04, 225.28, 235.52, 245.76, 256.00, 266.24, 276.48, 286.72, 296.96, 307.20, 317.44, 327.68, 337.92, 348.16, 358.40, 368.64, 378.88, 389.12, 399.36, 409.60, 419.84, 430.08 S

CURIE_IMU_DOUBLE_TAP – waiting window for the second tap to be read
50, 100, 150, 200, 250, 275, 500, 700 ms

CURIE_IMU_TAP_SHOCK - The time a physical shocking event should happen, exceeding the set threshold, to trigger the interrupt.
50, 75 ms

CURIE_IMU_TAP_QUIET – The time the acceleration reading should stay low to separate two taps.
20, 30 ms


---

### `getDetectionDuration()`

#### Description
Returns the value of the detection duration.

#### Syntax
```
CurieIMU.getDetectionDuration(int feature)
```

#### Parameter
feature: the requested feature. It can assume one of these values:

- CURIE_IMU_TAP
- CURIE_IMU_TAP_QUIET
- CURIE_IMU_DOUBLE_TAP
- CURIE_IMU_ZERO_MOTION

#### Returns
The detection duration of the chosen feature

---

### `interrupts()`
#### Description
Enables interrupt for the selected feature.

#### Syntax
```
CurieIMU.interrupts(int feature)
```
#### Parameters
feature: the feature for which the interrupt has to be enabled. It can assume one of these values:
```
CURIE_IMU_FREEFALL
CURIE_IMU_SHOCK
CURIE_IMU_MOTION
CURIE_IMU_ZERO_MOTION
CURIE_IMU_STEP
CURIE_IMU_TAP
CURIE_IMU_TAP_SHOCK
CURIE_IMU_TAP_QUIET
CURIE_IMU_DOUBLE_TAP
```
---

### `noInterrupts()`
#### Description
Disables interrupt for the selected feature.

#### Syntax
```
CurieIMU.noInterrupts(int feature)
```
#### Parameters
feature: the feature for which the interrupt has to be disabled. It can assume one of these values:

CURIE_IMU_FREEFALL
CURIE_IMU_SHOCK
CURIE_IMU_MOTION
CURIE_IMU_ZERO_MOTION
CURIE_IMU_STEP
CURIE_IMU_TAP
CURIE_IMU_TAP_SHOCK
CURIE_IMU_TAP_QUIET
CURIE_IMU_DOUBLE_TAP
CURIE_IMU_FIFO_FULL
CURIE_IMU_DATA_READY

---

### `interruptEnabled()`
#### Description
Return true or false if the interrupt for the selected feature is enabled or not.

#### Syntax
```
CurieIMU.interruptEnabled(int feature)
```
#### Parameters
feature: the feature for which the interrupt has to be enabled. It can assume one of these values:
```
CURIE_IMU_FREEFALL
CURIE_IMU_SHOCK
CURIE_IMU_MOTION
CURIE_IMU_ZERO_MOTION
CURIE_IMU_STEP
CURIE_IMU_TAP
CURIE_IMU_TAP_SHOCK
CURIE_IMU_TAP_QUIET
CURIE_IMU_DOUBLE_TAP
CURIE_IMU_FIFO_FULL
CURIE_IMU_DATA_READY
```
#### Returns
true or false if the interrupt is enabled or not for the selected feature

---

### `getInterruptStatus()`
#### Description
Returns the status of the interrupt for the selected feature.

#### Syntax
```
CurieIMU.getInterruptStatus(int feature)
```
#### Parameters
feature: the feature for which the interrupt has to be enabled. It can assume one of these values:
```
CURIE_IMU_FREEFALL
CURIE_IMU_SHOCK
CURIE_IMU_MOTION
CURIE_IMU_ZERO_MOTION
CURIE_IMU_STEP
CURIE_IMU_TAP
CURIE_IMU_TAP_SHOCK
CURIE_IMU_TAP_QUIET
CURIE_IMU_DOUBLE_TAP
CURIE_IMU_FIFO_FULL
CURIE_IMU_DATA_READY
```
#### Returns
 true or false if an interrupt has been triggered for the selected feature

---

### `getStepDetectionMode()`
#### Description
Returns the value of the step detection mode.

#### Syntax
```
CurieIMU.getStepDetectionMode()
```
#### Returns
CurieIMUStepMode: the step detection mode. It can assume one of these values:

CURIE_IMU_STEP_MODE_NORMAL
CURIE_IMU_STEP_MODE_SENSITIVE
CURIE_IMU_STEP_MODE_ROBUST
CURIE_IMU_STEP_MODE_UNKNOWN

---

### `setStepDetectionMode()`
#### Description
Sets the value of the step detection mode.

#### Syntax
```
CurieIMU.setStepDetectionMode(in mode)
```
#### Returns
mode: the step detection mode. It can assume one of these values:

CURIE_IMU_STEP_MODE_NORMAL
CURIE_IMU_STEP_MODE_SENSITIVE
CURIE_IMU_STEP_MODE_ROBUST
CURIE_IMU_STEP_MODE_UNKNOWN

---

### `readMotionSensor()`
#### Description
Reads the raw values of the motion sensor (accelerometer + gyro).

#### Syntax
```
CurieIMU.readMotionSensor(int ax, int ay, int az, int gx, int gy, int gz)
```
#### Parameters
- ax: a variable in which the accelerometer's value along x will be stored.
- ay: a variable in which the accelerometer's value along y will be stored.
- az: a variable in which the accelerometer's value along z will be stored.
- gx: a variable in which the gyro's value along x will be stored.
- gy: a variable in which the gyro's value along y will be stored.
- gz: a variable in which the gyro's value along z will be stored.

---

### `readAccelerometer()`
#### Description
Reads the raw value of the accelerometer.

#### Syntax
```
CurieIMU.readAccelerometer(int ax, int ay, int az)
```
#### Parameters
- ax: a variable in which the accelerometer's value along x will be stored.
- ay: a variable in which the accelerometer's value along y will be stored.
- az: a variable in which the accelerometer's value along z will be stored.

To convert the raw value into mg use the following formula:
float g = (gRaw/32768.0)*getAccelerometerRange()
where gRaw is either ax, ay or az.

---

### `readGyro()`
#### Description
Reads the raw value of the gyro.

#### Syntax
```
CurieIMU.readGyro(int gx, int gy, int gz)
```
#### Parameters
- gx: a variable in which the gyro's value along x will be stored.
- gy: a variable in which the gyro's value along y will be stored.
- gz: a variablle in which the gyro's value along z will be stored.

To convert any of the raw values in angular velocity (°/s) use the following formula:
```
float av = ( avRaw/32768.9)*getGyroRange()
```
where avRaw is either gx, gy or gz.
---

### `readTemperature()`
#### Description
Returns the raw value of the temperature value read by the built-in motion sensor

#### Syntax
```
CurieIMU.readTemperature()
```
#### Returns
The value of the read temperature is 16 bit signed. To convert this value you can use the following formula:
```
Celsius=(raw/512.0)+23
```
---

### `shockDetected()`
#### Description
Returns true if a shock is detected.

#### Syntax
```
CurieIMU.shockDetected(int axis, int direction)
```
#### Parameters
axis: the axis to check for shock detection. It must have one of these values:
```
X_AXIS
Y_AXIS
Z_AXIS
```
direction: the direction to check for shock detection. It must have one of these values:

POSITIVE from zero to positive axis values

NEGATIVE from zero to negative axis values
#### Returns
true or false if the shock is detected or not on the axis and direction specified.

---

### `motionDetected()`
#### Description
Returns true if a motion is detected

#### Syntax
```
CurieIMU.motionDetected(int axis, int direction)

```
#### Parameters
axis: the axis to check for motion detection. It must have one of these values:
```
X_AXIS
Y_AXIS
Z_AXIS
```
direction: the direction to check for motion detection. It must have one of these values:

POSITIVE from zero to positive axis values
NEGATIVE from zero to negative axis values
#### Returns
true or false if the motion is detected or not on the axis and direction specified.

---

### `tapDetected()`
#### Description
Returns true if a tap is detected

#### Syntax
```
CurieIMU.tapDetected(int axis, int direction)
```
#### Parameters
axis: the axis to check for tap detection. It must have one of these values:
```
X_AXIS
Y_AXIS
Z_AXIS
```
direction: the direction to check for tap detection. It must have one of these values:

POSITIVE from zero to positive axis values
NEGATIVE from zero to negative axis values
#### Returns
True or false if the tap is detected or not on the axis and direction specified. 

---

### `stepsDetected()`
#### Description
Returns true if a step is detected.

#### Syntax
```
CurieIMU.stepsDetected()
```
#### Returns
true or false if the step is detected or not.

---

### `attachInterrupt()`
#### Description
Attach an interrupt action.

#### Syntax
```
CurieIMU.attachInterrupt(voidFuncPtr callback)
```
#### Parameters
callback: The name of the function to be called on interrupt event

---

### `detachInterrupt()`
#### Description
Removes an interrupt action.

#### Syntax
```
CurieIMU.detachInterrupt()
```
#### Parameters
none