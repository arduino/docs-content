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

Here the full list of the methods of the **ArduinoAlvik()** class.

| **Name**                     | **Description**                                                                                          |
|------------------------------|----------------------------------------------------------------------------------------------------------|
| is_on()                      | Returns true if robot is on                                                                              |
| begin()                      | Begins all Alvik operations                                                                              |
| is_target_reached()          | Returns True if robot has sent an M or R acknowledgment. It also responds with an ack received message |
| [set_behaviour(...)](#set_behaviour)           | Sets the behaviour of Alvik                                                                              |
| [rotate(...)](#rotate)                  | Rotates the robot by given angle                                                                         |
| [move(...)](#move)                    | Moves the robot by given distance                                                                        |
| stop()                       | Stops all Alvik operations                                                                               |
| [get_wheels_speed(...)](#get_wheels_speed)        | Returns the speed of the wheels                                                                          |
| [set_wheels_speed(...)](#set_wheels_speed)        | Sets left/right motor speed                                                                              |
| [set_wheels_position(...)](#set_wheels_position)     | Sets left/right motor angle                                                                              |
| [get_wheels_position(...)](#get_wheels_position)     | Returns the angle of the wheels                                                                          |
| get_orientation()            | Returns the orientation of the IMU                                                                       |
| get_accelerations()          | Returns the 3-axial acceleration of the IMU                                                              |
| get_gyros()                  | Returns the 3-axial angular acceleration of the IMU                                                      |
| get_imu()                    | Returns all the IMUs readouts                                                                            |
| get_line_sensors()           | Returns the line sensors readout                                                                         |
| [drive(...)](#drive)                   | Drives the robot by linear and angular velocity                                                          |
| brake()                      | Brakes the robot                                                                                         |
| [get_drive_speed(...)](#get_drive_speed)         | Returns linear and angular velocity of the robot                                                         |
| [reset_pose(...)](#reset_pose)              | Resets the robot pose                                                                                    |
| [get_pose(...)](#get_pose)                | Returns the current pose of the robot                                                                    |
| [set_servo_positions(...)](#set_servo_positions)     | Sets A/B servomotor angle                                                                                |
| get_ack()                    | Returns last acknowledgement                                                                             |
| [set_builtin_led(...)](#set_builtin_led)         | Turns on/off the builtin led                                                                             |
| [set_illuminator(...)](#set_illuminator)         | Turns on/off the illuminator led                                                                         |
| get_battery_charge()         | Returns the battery SOC                                                                                  |
| get_touch_any()              | Returns true if any button is pressed                                                                    |
| get_touch_ok()               | Returns true if ok button is pressed                                                                     |
| get_touch_cancel()           | Returns true if cancel button is pressed                                                                 |
| get_touch_center()           | Returns true if center button is pressed                                                                 |
| get_touch_up()               | Returns true if up button is pressed                                                                     |
| get_touch_left()             | Returns true if left button is pressed                                                                   |
| get_touch_down()             | Returns true if down button is pressed                                                                   |
| get_touch_right()            | Returns true if right button is pressed                                                                  |
| [color_calibration(...)](#color_calibration)       | Calibrates the color sensor                                                                              |
| get_color_raw()              | Returns the color sensor's raw readout                                                                   |
| [rgb2hsv(...)](#rgb2hsv)                 | Converts normalized rgb to hsv                                                                           |
| [get_color(...)](#get_color)               | Returns the normalized color readout of the color sensor                                                 |
| get_color_label()            | Returns the label of the color as recognized by the sensor                                               |
| [hsv2label(...)](#hsv2label)               | Returns the color label corresponding to the given normalized HSV color input                          |
| [get_distance(...)](#get_distance)            | Returns the distance readout of the TOF sensor                                                           |
| [get_distance_top(...)](#get_distance_top)        | Returns the obstacle top distance readout                                                                |
| [get_distance_bottom(...)](#get_distance_bottom)     | Returns the obstacle bottom distance readout                                                             |
| get_version()                | Returns the firmware version of the Alvik                                                                |
| print_status()               | Prints the Alvik status                                                                                  |
| [on_touch_ok_pressed(...)](#on_touch_ok_pressed)     | Register callback when touch button OK is pressed                                                        |
| [on_touch_cancel_pressed(...)](#on_touch_cancel_pressed) | Register callback when touch button CANCEL is pressed                                                    |
| [on_touch_center_pressed(...)](#on_touch_center_pressed) | Register callback when touch button CENTER is pressed                                                    |
| [on_touch_up_pressed(...)](#on_touch_up_pressed)     | Register callback when touch button UP is pressed                                                        |
| [on_touch_left_pressed(...)](#on_touch_left_pressed)   | Register callback when touch button LEFT is pressed                                                      |
| [on_touch_down_pressed(...)](#on_touch_down_pressed)   | Register callback when touch button DOWN is pressed                                                      |
| [on_touch_right_pressed(...)](#on_touch_right_pressed)  | Register callback when touch button RIGHT is pressed                                                     |

## Parameters and return values of each function
### set_behaviour 

set_behaviour(behaviour: int)

_Sets the behaviour of Alvik_

- inputs:
	- **behaviour**: behaviour code

### rotate

rotate(angle: float, unit: str = 'deg', blocking: bool = True)

_Rotates the robot by given angle_

- inputs:
	- **angle**: the angle value
	- **unit**: the angle unit, [?](#the-angle-unit)
	- **blocking**: _True_ or _False_, [?](#blocking-or-non-blocking)
### move

move(distance: float, unit: str = 'cm', blocking: bool = True)

_Moves the robot by given distance_

- inputs:
	- **distance**: the distance value
	- **unit**: the distance unit. [?](#the-distance-unit)
	- **blocking**: _True_ or _False_, [?](#blocking-or-non-blocking)

### get_wheels_speed

get_wheels_speed(unit: str = 'rpm')

- inputs:
	- **unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)
- outputs:
	- **left_wheel_speed**: the speed value
	- **right_wheel_speed**: the speed value

_Returns the speed of the wheels_

### set_wheels_speed

set_wheels_speed(left_speed: float, right_speed: float, unit: str = 'rpm')

_Sets left/right motor speed_

- inputs:
	- **left_speed**: the speed value
	- **right_speed**: the speed value
	- **unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)

### set_wheels_position

set_wheels_position(left_angle: float, right_angle: float, unit: str = 'deg')

_Sets left/right motor angle_

- inputs:
	- **left_angle**: the angle value
	- **right_angle**: the angle value
	- **unit**: the angle unit, [?](#the-angle-unit)


### get_wheels_position

get_wheels_position(unit: str = 'deg')

_Returns the angle of the wheels_

- inputs:
 	- **angular_unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)
- outputs:
	- **angular_velocity**:	speed of the wheels.

### drive

drive(linear_velocity: float, angular_velocity: float, linear_unit: str = 'cm/
s',angular_unit: str = 'deg/s')

_Drives the robot by linear and angular velocity_

- inputs:
	- **linear_velocity**: speed of the robot.
	- **angular_velocity**:	speed of the wheels.
	- **linear_unit**: unit of linear velocity. [?](#the-linear-speed-unit)
 	- **angular_unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)

### get_drive_speed

get_drive_speed(linear_unit: str = 'cm/s', angular_unit: str = 'deg/s')

_Returns linear and angular velocity of the robot_

- inputs:
	- **linear_unit**: unit of linear velocity. [?](#the-linear-speed-unit)
 	- **angular_unit**: unit of rotational speed of the wheels. [?](#the-rotational-speed-unit)
- outputs:
	- **linear_velocity**: speed of the robot.
	- **angular_velocity**:	speed of the wheels.


### reset_pose

reset_pose(x: float, y: float, theta: float, distance_unit: str = 'cm', angle_unit: 
str = 'deg')

_Resets the robot pose_

- inputs:
	- **x**
	- **y**
	- **theta**
	- **distance_unit**: unit of x and y outputs, [?](#the-distance-unit)
 	- **angle_unit**: unit of theta output, [?](#the-angle-unit)


### get_pose

get_pose(distance_unit: str = 'cm', angle_unit: str = 'deg')           

_Returns the current pose of the robot_

 - inputs:
	- **distance_unit**: unit of x and y outputs, [?](#the-distance-unit)
 	- **angle_unit**: unit of theta output, [?](#the-angle-unit)

 - outputs:
	- **x**
	- **y**
	- **theta**

### set_servo_positions

set_servo_positions(a_position: int, b_position: int)

_Sets A/B servomotor angle_

 - inputs:
	- **a_position**: position of A servomotor (0-180)
	- **b_position**: position of B servomotor (0-180)

### set_builtin_led

set_builtin_led(value: bool)

_Turns on/off the builtin led_

 - inputs:
	- **value**: True = ON, False = OFF

### set_illuminator

set_illuminator(value: bool)

_Turns on/off the illuminator led_

 - inputs:
	- **value**: True = ON, False = OFF

### color_calibration

color_calibration(background: str = 'white')

_Calibrates the color sensor_

 - inputs:
 	- **background**: string "white" or "black"

### rgb2hsv

rgb2hsv(r: float, g: float, b: float)

_Converts normalized rgb to hsv_

 - inputs:
 	- **r**: red value
 	- **g**: green value
 	- **b**: blue value
 - outputs:
 	- **h**: hue value
 	- **s**: saturation value
 	- **v**: brightness value

### get_color

get_color(color_format: str = 'rgb')

_Returns the normalized color readout of the color sensor_

 - inputs:
 	- **color_format**: rgb or hsv only
 - outputs:
 	- **r** or **h**
 	- **g** or **s**
 	- **b** or **v**

### hsv2label

hsv2label(h, s, v)

_Returns the color label corresponding to the given normalized HSV color input_

 - inputs:
 	- **h**: hue value
 	- **s**: saturation value
 	- **v**: brightness value
 - outputs:
 	- **color label**: like "BLACK" or "GREEN", if possible, otherwise return "UNDEFINED"

### get_distance

get_distance(unit: str = 'cm')

_Returns the distance readout of the TOF sensor_

 - inputs:
 	- **unit**: distance output unit
 - outputs:
 	- **left_tof**: 45° to the left object distance
 	- **center_left_tof**: 22° to the left object distance
 	- **center_tof**: center object distance
 	- **center_right_tof**: 22° to the right object distance
 	- **right_tof**: 45° to the right object distance

### get_distance_top

get_distance_top(unit: str = 'cm')

_Returns the obstacle top distance readout_

 - inputs:
 	- **unit**: distance output unit
 - outputs:
 	- **top_tof**: 45° to the top object distance

### get_distance_bottom

get_distance_bottom(unit: str = 'cm')

_Returns the obstacle bottom distance readout_

 - inputs:
 	- **unit**: distance output unit
 - outputs:
 	- **bottom_tof**: 45° to the bottom object distance

### on_touch_ok_pressed

on_touch_ok_pressed(callback: callable, args: tuple = ())

_Register callback when touch button OK is pressed_

 - inputs:
 	- **callback**: the name of the function to recall
 	- **args**: optional arguments of the function

### on_touch_cancel_pressed

on_touch_cancel_pressed(callback: callable, args: tuple = ())

_Register callback when touch button CANCEL is pressed_

 - inputs:
 	- **callback**: the name of the function to recall
 	- **args**: optional arguments of the function

### on_touch_center_pressed

on_touch_center_pressed(callback: callable, args: tuple = ())

_Register callback when touch button CENTER is pressed_

 - inputs:
 	- **callback**: the name of the function to recall
 	- **args**: optional arguments of the function

### on_touch_up_pressed

on_touch_up_pressed(callback: callable, args: tuple = ())

_Register callback when touch button UP is pressed_

 - inputs:
 	- **callback**: the name of the function to recall
 	- **args**: optional arguments of the function

### on_touch_left_pressed

on_touch_left_pressed(callback: callable, args: tuple = ())

_Register callback when touch button LEFT is pressed_

 - inputs:
 	- **callback**: the name of the function to recall
 	- **args**: optional arguments of the function

### on_touch_down_pressed

on_touch_down_pressed(callback: callable, args: tuple = ())

_Register callback when touch button DOWN is pressed_

 - inputs:
 	- **callback**: the name of the function to recall
 	- **args**: optional arguments of the function

### on_touch_right_pressed

on_touch_right_pressed(callback: callable, args: tuple = ())

_Register callback when touch button RIGHT is pressed_

 - inputs:
 	- **callback**: the name of the function to recall
 	- **args**: optional arguments of the function



## Extras

### The distance unit

Distance unit of measurement used in the APIs:

 - _cm_: centimeters
 - _mm_: millimeters
 - _m_: meters
 - _inch_: inch, 2.54 cm
 - _in_: inch, 2.54 cm

### The angle unit

Angle unit of measurement used in the APIs:

 - _deg_: degrees, example: 1.0 as reference for the other unit. 1 degree is 1/360 of a circle.
 - _rad_: radiant, example: 1 radiant is 180/pi deg.
 - _rev_: revolution, example: 1 rev is 360 deg.
 - _revolution_: same as rev
 - _perc_: percentage, example 1 perc is 3.6 deg.
 - _%_: same as perc

### The linear speed unit

Speed unit of measurement used in the APIs:

 - 'cm/s': centimeters per second
 - 'mm/s': millimeters per second
 - 'm/s': meters per second
 - 'inch/s': inch per second
 - 'in/s': inch per second

### The rotational speed unit

Rotational speed unit of measurement used in the APIs: 

 - 'rpm': revolutions per minute, example: 1.0 as reference for the other unit.
 - 'deg/s': degrees per second, example: 1.0 deg/s is 60.0 deg/min that is 1/6 rpm. 
 - 'rad/s': radiant per second, example: 1.0 rad/s is 60.0 rad/min that is 9.55 rpm.
 - 'rev/s': revolution per second, example: 1.0 rev/s is 60.0 rev/min that is 60.0 rpm.

### Blocking or non blocking

While programming a microcontroller, the terms "blocking" means that **all the resources are used only in performing a specific action, and no other things can happen at the same time**. Usually this is used when you want to be precise or you don't want anything else that could interact with the action you are performing.

On the other hand, "Non blocking", means that the microcontroller is free to do other thing while the action is been performed.