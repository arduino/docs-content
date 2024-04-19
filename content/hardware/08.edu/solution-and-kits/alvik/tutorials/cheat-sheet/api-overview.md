---
title: 'Arduino Alvik Cheat Sheet'
description: 'A technical summary of the APIs used to control the Alvik Robot.'
tags:
  - Alvik
  - API
  - MicroPython
author: 'Paolo Cavagnolo'
hardware:
  - hardware/08.edu/solution-and-kits/alvik
---

## API List

To access to any of these functions you need first to initialize an instance of the class **ArduinoAlvik()**.


```arduino
alvik = ArduinoAlvik()
```

Then you can use the following functions as methods of the instance you've created, for example:

```arduino
alvik.begin()
```

### `is_on`

is_on()

_Returns true if robot is on_

**Outputs**

- boolean: Returns true if robot is on, false if is off.

### `begin`

begin()

_Begins all Alvik operations_


### `is_target_reached`

is_target_reached()

_Returns True if robot has sent an M or R acknowledgment. It also responds with an ack received message_

**Outputs**

- boolean: Returns True if robot has arrived to target, False otherwise.

### `stop`

stop()

_Stops all Alvik operations_


### `get_orientation`

get_orientation()

_Returns the orientation of the IMU_

**Outputs**

- **r**: roll value
- **p**: pitch value
- **y**: yaw value

### `get_accelerations`

get_accelerations()

_Returns the 3-axial acceleration of the IMU_

**Outputs**

- **ax**: acceleration on x 
- **ay**: acceleration on y 
- **az**: acceleration on z 

### `get_gyros`

get_gyros()

_Returns the 3-axial angular acceleration of the IMU_

**Outputs**

- **gx**: angular acceleration on x 
- **gy**: angular acceleration on y 
- **gz**: angular acceleration on z 

### `get_imu`

get_imu()

_Returns all the IMUs readouts_

**Outputs**

- **ax**: acceleration on x 
- **ay**: acceleration on y 
- **az**: acceleration on z 
- **gx**: angular acceleration on x 
- **gy**: angular acceleration on y 
- **gz**: angular acceleration on z 

### `get_line_sensors`

get_line_sensors()

_Returns the line follower sensors readout_

**Outputs**

- **left**: left sensor readout
- **center**: center sensor readout
- **right**: right sensor readout

### `brake`

brake()

_Brakes the robot_

### `get_ack`

get_ack()

_Returns last acknowledgement_

**Outputs**

- **last_ack**: last acknowledgement value

### `get_battery_charge`

get_battery_charge()

_Returns the battery SOC_

**Outputs**

- **battery_soc**: percentage of charge

### `get_touch_any`

get_touch_any()

_Returns true if any button is pressed_

**Outputs**

- **touch_any**: true if any button is pressed, false otherwise.

### `get_touch_ok`

get_touch_ok()

_Returns true if ok button is pressed_

**Outputs**

- **touch_ok**: true if ok button is pressed, false otherwise.

### `get_touch_cancel`

get_touch_cancel()

_Returns true if cancel button is pressed_

**Outputs**

- **touch_cancel**: true if cancel button is pressed, false otherwise.

### `get_touch_center`

get_touch_center()

_Returns true if center button is pressed_

**Outputs**

- **touch_center**: true if center button is pressed, false otherwise.

### `get_touch_up`

get_touch_up()

_Returns true if up button is pressed_

**Outputs**

- **touch_up**: true if up button is pressed, false otherwise.

### `get_touch_left`

get_touch_left()

_Returns true if left button is pressed_

**Outputs**

- **touch_left**: true if left button is pressed, false otherwise.

### `get_touch_down`

get_touch_down()

_Returns true if down button is pressed_

**Outputs**

- **touch_down**: true if down button is pressed, false otherwise.

### `get_touch_right`

get_touch_right()

_Returns true if right button is pressed_

**Outputs**

- **touch_right**: true if right button is pressed, false otherwise.

### `get_color_raw`

get_color_raw()

_Returns the color sensor's raw readout_

**Outputs**

- **color**: the color sensor's raw readout

### `get_color_label`

get_color_label()

_Returns the label of the color as recognized by the sensor_

**Outputs**

- **color**: the label of the color as recognized by the sensor

### `get_version`

get_version()

_Returns the firmware version of the Alvik_

**Outputs**

- **version**: Returns the firmware version of the Alvik

### `print_status`

print_status()

_Prints the Alvik status_

**Outputs**

- **status**: Prints the Alvik status

### `set_behaviour`

set_behaviour(behaviour: int)

_Sets the behaviour of Alvik_

**Inputs**

- **behaviour**: behaviour code

### `rotate`

rotate(angle: float, unit: str = 'deg', blocking: bool = True)

_Rotates the robot by given angle_

**Inputs**

- **angle**: the angle value
- **unit**: [angle unit](#the-angle-unit)
- **blocking**:[_True_ or _False_](#blocking-or-non-blocking)

### `move`

move(distance: float, unit: str = 'cm', blocking: bool = True)

_Moves the robot by given distance_

**Inputs**

- **distance**: the distance value
- **unit**: the distance unit. [?](#the-distance-unit)
- **blocking**: _True_ or _False_, [?](#blocking-or-non-blocking)

### `get_wheels_speed`

get_wheels_speed(unit: str = 'rpm')

**Inputs**

- **unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)

**Outputs**

- **left_wheel_speed**: the speed value
- **right_wheel_speed**: the speed value

_Returns the speed of the wheels_

### `set_wheels_speed`

set_wheels_speed(left_speed: float, right_speed: float, unit: str = 'rpm')

_Sets left/right motor speed_

**Inputs**

- **left_speed**: the speed value
- **right_speed**: the speed value
- **unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)

### `set_wheels_position`

set_wheels_position(left_angle: float, right_angle: float, unit: str = 'deg')

_Sets left/right motor angle_

**Inputs**

- **left_angle**: the angle value
- **right_angle**: the angle value
- **unit**: the angle unit, [?](#the-angle-unit)


### `get_wheels_position`

get_wheels_position(unit: str = 'deg')

_Returns the angle of the wheels_

**Inputs**

- **angular_unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)

**Outputs**

- **angular_velocity**:	speed of the wheels.

### `drive`

drive(linear_velocity: float, angular_velocity: float, linear_unit: str = 'cm/s',angular_unit: str = 'deg/s')

_Drives the robot by linear and angular velocity_

**Inputs**

- **linear_velocity**: speed of the robot.
- **angular_velocity**:	speed of the wheels.
- **linear_unit**: unit of linear velocity. [?](#the-linear-speed-unit)
- **angular_unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)

### `get_drive_speed`

get_drive_speed(linear_unit: str = 'cm/s', angular_unit: str = 'deg/s')

_Returns linear and angular velocity of the robot_

**Inputs**

- **linear_unit**: unit of linear velocity. [?](#the-linear-speed-unit)
- **angular_unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)

**Outputs**

- **linear_velocity**: speed of the robot.
- **angular_velocity**:	speed of the wheels.


### `reset_pose`

reset_pose(x: float, y: float, theta: float, distance_unit: str = 'cm', angle_unit:
str = 'deg')

_Resets the robot pose_

**Inputs**

- **x**
- **y**
- **theta**
- **distance_unit**: unit of x and y outputs, [?](#the-distance-unit)
- **angle_unit**: unit of theta output, [?](#the-angle-unit)


### `get_pose`

get_pose(distance_unit: str = 'cm', angle_unit: str = 'deg')           

_Returns the current pose of the robot_

**Inputs**

- **distance_unit**: unit of x and y outputs, [?](#the-distance-unit)
- **angle_unit**: unit of theta output, [?](#the-angle-unit)

**Outputs**

- **x**
- **y**
- **theta**

### `set_servo_positions`

set_servo_positions(a_position: int, b_position: int)

_Sets A/B servomotor angle_

**Inputs**

- **a_position**: position of A servomotor (0-180)
- **b_position**: position of B servomotor (0-180)

### `set_builtin_led`

set_builtin_led(value: bool)

_Turns on/off the builtin led_

**Inputs**

- **value**: True = ON, False = OFF

### `set_illuminator`

set_illuminator(value: bool)

_Turns on/off the illuminator led_

**Inputs**

- **value**: True = ON, False = OFF

### `color_calibration`

color_calibration(background: str = 'white')

_Calibrates the color sensor_

**Inputs**

- **background**: string "white" or "black"

### `rgb2hsv`

rgb2hsv(r: float, g: float, b: float)

_Converts normalized rgb to hsv_

**Inputs**

- **r**: red value
- **g**: green value
- **b**: blue value

**Outputs**

- **h**: hue value
- **s**: saturation value
- **v**: brightness value

### `get_color`

get_color(color_format: str = 'rgb')

_Returns the normalized color readout of the color sensor_

**Inputs**

- **color_format**: rgb or hsv only

**Outputs**

- **r** or **h**
- **g** or **s**
- **b** or **v**

### `hsv2label`

hsv2label(h, s, v)

_Returns the color label corresponding to the given normalized HSV color input_

**Inputs**

- **h**: hue value
- **s**: saturation value
- **v**: brightness value

**Outputs**

- **color label**: like "BLACK" or "GREEN", if possible, otherwise return "UNDEFINED"

### `get_distance`

get_distance(unit: str = 'cm')

_Returns the distance readout of the TOF sensor_

**Inputs**

- **unit**: distance output unit

**Outputs**

- **left_tof**: 45° to the left object distance
- **center_left_tof**: 22° to the left object distance
- **center_tof**: center object distance
- **center_right_tof**: 22° to the right object distance
-  **right_tof**: 45° to the right object distance

### `get_distance_top`

get_distance_top(unit: str = 'cm')

_Returns the obstacle top distance readout_

**Inputs**

- **unit**: distance output unit

**Outputs**

- **top_tof**: 45° to the top object distance

### `get_distance_bottom`

get_distance_bottom(unit: str = 'cm')

_Returns the obstacle bottom distance readout_

**Inputs**

- **unit**: distance output unit

**Outputs**

- **bottom_tof**: 45° to the bottom object distance

### `on_touch_ok_pressed`

on_touch_ok_pressed(callback: callable, args: tuple = ())

_Register callback when touch button OK is pressed_

**Inputs**

- **callback**: the name of the function to recall
- **args**: optional arguments of the function

### `on_touch_cancel_pressed`

on_touch_cancel_pressed(callback: callable, args: tuple = ())

_Register callback when touch button CANCEL is pressed_

**Inputs**

- **callback**: the name of the function to recall
- **args**: optional arguments of the function

### `on_touch_center_pressed`

on_touch_center_pressed(callback: callable, args: tuple = ())

_Register callback when touch button CENTER is pressed_

**Inputs**

- **callback**: the name of the function to recall
- **args**: optional arguments of the function

### `on_touch_up_pressed`

on_touch_up_pressed(callback: callable, args: tuple = ())

_Register callback when touch button UP is pressed_

**Inputs**

- **callback**: the name of the function to recall
- **args**: optional arguments of the function

### `on_touch_left_pressed`

on_touch_left_pressed(callback: callable, args: tuple = ())

_Register callback when touch button LEFT is pressed_

**Inputs**

- **callback**: the name of the function to recall
- **args**: optional arguments of the function

### `on_touch_down_pressed`

on_touch_down_pressed(callback: callable, args: tuple = ())

_Register callback when touch button DOWN is pressed_

**Inputs**

- **callback**: the name of the function to recall
- **args**: optional arguments of the function

### `on_touch_right_pressed`

on_touch_right_pressed(callback: callable, args: tuple = ())

_Register callback when touch button RIGHT is pressed_

**Inputs**

- **callback**: the name of the function to recall
- **args**: optional arguments of the function

## Extras

### The Distance Unit

Distance unit of measurement used in the APIs:

- _cm_: centimeters
- _mm_: millimeters
- _m_: meters
- _inch_: inch, 2.54 cm
- _in_: inch, 2.54 cm

### The Angle Unit

Angle unit of measurement used in the APIs:

- _deg_: degrees, example: 1.0 as reference for the other unit. 1 degree is 1/360 of a circle.
- _rad_: radiant, example: 1 radiant is 180/pi deg.
- _rev_: revolution, example: 1 rev is 360 deg.
- _revolution_: same as rev
- _perc_: percentage, example 1 perc is 3.6 deg.
- _%_: same as perc

### The Linear Speed Unit

Speed unit of measurement used in the APIs:

- 'cm/s': centimeters per second
- 'mm/s': millimeters per second
- 'm/s': meters per second
- 'inch/s': inch per second
- 'in/s': inch per second

### The Rotational Speed Unit

Rotational speed unit of measurement used in the APIs:

- 'rpm': revolutions per minute, example: 1.0 as reference for the other unit.
- 'deg/s': degrees per second, example: 1.0 deg/s is 60.0 deg/min that is 1/6 rpm.
- 'rad/s': radiant per second, example: 1.0 rad/s is 60.0 rad/min that is 9.55 rpm.
- 'rev/s': revolution per second, example: 1.0 rev/s is 60.0 rev/min that is 60.0 rpm.

### `"blocking" or "non blocking"`

While programming a microcontroller, the terms "blocking" means that **all the resources are used only in performing a specific action, and no other things can happen at the same time**. Usually this is used when you want to be precise or you don't want anything else that could interact with the action you are performing.

On the other hand, "Non blocking", means that the microcontroller is free to do other thing while the action is been performed.
