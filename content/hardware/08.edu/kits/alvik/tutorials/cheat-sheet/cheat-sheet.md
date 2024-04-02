---
title: 'Placeholder'
description: 'Placeholder'
author: 'Placeholder'
tags:
	- edu
---

## List of All Functions Name

### Alvik Class

| **Name**                     | **Description**                                                                                          |
|------------------------------|----------------------------------------------------------------------------------------------------------|
| is_on()                      | Returns true if robot is on                                                                              |
| begin()                      | Begins all Alvik operations                                                                              |
| is_target_reached()          | Returns True if robot has sent an M or R acknowledgment. It also responds with an ack received message |
| set_behaviour(...)           | Sets the behaviour of Alvik                                                                              |
| rotate(...)                  | Rotates the robot by given angle                                                                         |
| move(...)                    | Moves the robot by given distance                                                                        |
| stop()                       | Stops all Alvik operations                                                                               |
| get_wheels_speed(...)        | Returns the speed of the wheels                                                                          |
| set_wheels_speed(...)        | Sets left/right motor speed                                                                              |
| set_wheels_position(...)     | Sets left/right motor angle                                                                              |
| get_wheels_position(...)     | Returns the angle of the wheels                                                                          |
| get_orientation()            | Returns the orientation of the IMU                                                                       |
| get_accelerations()          | Returns the 3-axial acceleration of the IMU                                                              |
| get_gyros()                  | Returns the 3-axial angular acceleration of the IMU                                                      |
| get_imu()                    | Returns all the IMUs readouts                                                                            |
| get_line_sensors()           | Returns the line sensors readout                                                                         |
| drive(...)                   | Drives the robot by linear and angular velocity                                                          |
| brake()                      | Brakes the robot                                                                                         |
| get_drive_speed(...)         | Returns linear and angular velocity of the robot                                                         |
| reset_pose(...)              | Resets the robot pose                                                                                    |
| [get_pose(...)](#get_pose)                | Returns the current pose of the robot                                                                    |
| set_servo_positions(...)     | Sets A/B servomotor angle                                                                                |
| get_ack()                    | Returns last acknowledgement                                                                             |
| set_builtin_led(...)         | Turns on/off the builtin led                                                                             |
| set_illuminator(...)         | Turns on/off the illuminator led                                                                         |
| get_battery_charge()         | Returns the battery SOC                                                                                  |
| get_touch_any()              | Returns true if any button is pressed                                                                    |
| get_touch_ok()               | Returns true if ok button is pressed                                                                     |
| get_touch_cancel()           | Returns true if cancel button is pressed                                                                 |
| get_touch_center()           | Returns true if center button is pressed                                                                 |
| get_touch_up()               | Returns true if up button is pressed                                                                     |
| get_touch_left()             | Returns true if left button is pressed                                                                   |
| get_touch_down()             | Returns true if down button is pressed                                                                   |
| get_touch_right()            | Returns true if right button is pressed                                                                  |
| color_calibration(...)       | Calibrates the color sensor                                                                              |
| get_color_raw()              | Returns the color sensor's raw readout                                                                   |
| rgb2hsv(...)                 | Converts normalized rgb to hsv                                                                           |
| get_color(...)               | Returns the normalized color readout of the color sensor                                                 |
| get_color_label()            | Returns the label of the color as recognized by the sensor                                               |
| hsv2label(...)               | Returns the color label corresponding to the given normalized HSV color input                          |
| get_distance(...)            | Returns the distance readout of the TOF sensor                                                           |
| get_distance_top(...)        | Returns the obstacle top distance readout                                                                |
| get_distance_bottom(...)     | Returns the obstacle bottom distance readout                                                             |
| get_version()                | Returns the firmware version of the Alvik                                                                |
| print_status()               | Prints the Alvik status                                                                                  |
| on_touch_ok_pressed(...)     | Register callback when touch button OK is pressed                                                        |
| on_touch_cancel_pressed(...) | Register callback when touch button CANCEL is pressed                                                    |
| on_touch_center_pressed(...) | Register callback when touch button CENTER is pressed                                                    |
| on_touch_up_pressed(...)     | Register callback when touch button UP is pressed                                                        |
| on_touch_left_pressed(...)   | Register callback when touch button LEFT is pressed                                                      |
| on_touch_down_pressed(...)   | Register callback when touch button DOWN is pressed                                                      |
| on_touch_right_pressed(...)  | Register callback when touch button RIGHT is pressed                                                     |

### Alvik Wheel Class

| **Name**           | **Description**                                                |
|--------------------|----------------------------------------------------------------|
| reset(...)         | Resets the wheel reference position                            |
| set_pid_gains(...) | Set PID gains for Alvik wheels                                 |
| stop()             | Stop Alvik wheel                                               |
| set_speed(...)     | Sets the motor speed                                           |
| get_speed(...)     | Returns the current RPM speed of the wheel                     |
| get_position(...)  | Returns the wheel position angle with respect to the reference |
| set_position(...)  | Sets left/right motor speed                                    |

### Alvik RGB Led Class

| **Name**       | **Description**            |
|----------------|----------------------------|
| set_color(...) | Sets the LED's r,g,b state |

### Alvik Events Class

| **Name**               | **Description**                                               |
|------------------------|---------------------------------------------------------------|
| register_callback(...) | Registers a callback to execute on an event                   |
| has_callbacks()        | True if the _callbacks dictionary has any callback registered |
| execute_callback(...)  | Executes the callback associated to the event_name            |

### Alvik Touch Event Class

| **Name**                | **Description**                                                     |
|-------------------------|---------------------------------------------------------------------|
| update_touch_state(...) | Updates the internal touch state and executes any possible callback |

### Update Firmware

| **Name**             | **Description**     |
|----------------------|---------------------|
| update_firmware(...) | Update the firmware |


## Parameters and Return Values of Each Functions 

### `get_pose`

get_pose(distance_unit: str = 'cm', angle_unit: str = 'deg')           

_Returns the current pose of the robot_

 - inputs:
	- **distance_unit**: unit of x and y outputs
 	- **angle_unit**: unit of theta output

 - outputs:
	- **x**
	- **y**
	- **theta**
