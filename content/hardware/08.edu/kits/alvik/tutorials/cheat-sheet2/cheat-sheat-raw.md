---
title: 'Cheat Sheet'
description: 'Placeholder'
author: 'Placeholder'
tags:
	- edu
---

## Arduino Alvik Class

```python
    def is_on() -> bool:
        """
        Returns true if robot is on
        :return:
        """
```

    def begin(self) -> int:
        """
        Begins all Alvik operations
        :return:
        """


    def is_target_reached(self) -> bool:
        """
        Returns True if robot has sent an M or R acknowledgment.
        It also responds with an ack received message
        :return:
        """

    def set_behaviour(self, behaviour: int):
        """
        Sets the behaviour of Alvik
        :param behaviour: behaviour code
        :return:
        """


    def rotate(self, angle: float, unit: str = 'deg', blocking: bool = True):
        """
        Rotates the robot by given angle
        :param angle:
        :param blocking:
        :param unit: the angle unit
        :return:
        """


    def move(self, distance: float, unit: str = 'cm', blocking: bool = True):
        """
        Moves the robot by given distance
        :param distance:
        :param blocking:
        :param unit: the distance unit
        :return:
        """


    def stop(self):
        """
        Stops all Alvik operations
        :return:
        """


    def get_wheels_speed(self, unit: str = 'rpm') -> (float | None, float | None):
        """
        Returns the speed of the wheels
        :param unit: the speed unit of measurement (default: 'rpm')
        :return: left_wheel_speed, right_wheel_speed
        """


    def set_wheels_speed(self, left_speed: float, right_speed: float, unit: str = 'rpm'):
        """
        Sets left/right motor speed
        :param left_speed:
        :param right_speed:
        :param unit: the speed unit of measurement (default: 'rpm')
        :return:
        """


    def set_wheels_position(self, left_angle: float, right_angle: float, unit: str = 'deg'):
        """
        Sets left/right motor angle
        :param left_angle:
        :param right_angle:
        :param unit: the speed unit of measurement (default: 'rpm')
        :return:
        """


    def get_wheels_position(self, unit: str = 'deg') -> (float | None, float | None):
        """
        Returns the angle of the wheels
        :param unit: the angle unit of measurement (default: 'deg')
        :return: left_wheel_angle, right_wheel_angle
        """


    def get_orientation(self) -> (float | None, float | None, float | None):
        """
        Returns the orientation of the IMU
        :return: roll, pitch, yaw
        """

    def get_accelerations(self) -> (float | None, float | None, float | None):
        """
        Returns the 3-axial acceleration of the IMU
        :return: ax, ay, az
        """

    def get_gyros(self) -> (float | None, float | None, float | None):
        """
        Returns the 3-axial angular acceleration of the IMU
        :return: gx, gy, gz
        """

    def get_imu(self) -> (float | None, float | None, float | None, float | None, float | None, float | None):
        """
        Returns all the IMUs readouts
        :return: ax, ay, az, gx, gy, gz
        """

    def get_line_sensors(self) -> (int | None, int | None, int | None):
        """
        Returns the line sensors readout
        :return: left_line, center_line, right_line
        """

    def drive(self, linear_velocity: float, angular_velocity: float, linear_unit: str = 'cm/s',
              angular_unit: str = 'deg/s'):
        """
        Drives the robot by linear and angular velocity
        :param linear_velocity:
        :param angular_velocity:
        :param linear_unit: output linear velocity unit of meas
        :param angular_unit: output angular velocity unit of meas
        :return:
        """

    def brake(self):
        """
        Brakes the robot
        :return:
        """

    def get_drive_speed(self, linear_unit: str = 'cm/s', angular_unit: str = 'deg/s') -> (float | None, float | None):
        """
        Returns linear and angular velocity of the robot
        :param linear_unit: output linear velocity unit of meas
        :param angular_unit: output angular velocity unit of meas
        :return: linear_velocity, angular_velocity
        """

    def reset_pose(self, x: float, y: float, theta: float, distance_unit: str = 'cm', angle_unit: str = 'deg'):
        """
        Resets the robot pose
        :param x: x coordinate of the robot
        :param y: y coordinate of the robot
        :param theta: angle of the robot
        :param distance_unit: angle of the robot
        :param angle_unit: angle of the robot
        :return:
        """

    def get_pose(self, distance_unit: str = 'cm', angle_unit: str = 'deg') \
            -> (float | None, float | None, float | None):
        """
        Returns the current pose of the robot
        :param distance_unit: unit of x and y outputs
        :param angle_unit: unit of theta output
        :return: x, y, theta
        """

    def set_servo_positions(self, a_position: int, b_position: int):
        """
        Sets A/B servomotor angle
        :param a_position: position of A servomotor (0-180)
        :param b_position: position of B servomotor (0-180)
        :return:
        """

    def get_ack(self) -> str:
        """
        Returns last acknowledgement
        :return:
        """


    def set_builtin_led(self, value: bool):
        """
        Turns on/off the builtin led
        :param value:
        :return:
        """

    def set_illuminator(self, value: bool):
        """
        Turns on/off the illuminator led
        :param value:
        :return:
        """


    def get_battery_charge(self) -> int | None:
        """
        Returns the battery SOC
        :return:
        """

    def get_touch_any(self) -> bool:
        """
        Returns true if any button is pressed
        :return:
        """

    def get_touch_ok(self) -> bool:
        """
        Returns true if ok button is pressed
        :return:
        """

    def get_touch_cancel(self) -> bool:
        """
        Returns true if cancel button is pressed
        :return:
        """

    def get_touch_center(self) -> bool:
        """
        Returns true if center button is pressed
        :return:
        """

    def get_touch_up(self) -> bool:
        """
        Returns true if up button is pressed
        :return:
        """

    def get_touch_left(self) -> bool:
        """
        Returns true if left button is pressed
        :return:
        """

    def get_touch_down(self) -> bool:
        """
        Returns true if down button is pressed
        :return:
        """

    def get_touch_right(self) -> bool:
        """
        Returns true if right button is pressed
        :return:
        """

    def color_calibration(self, background: str = 'white') -> None:
        """
        Calibrates the color sensor
        :param background: str white or black
        :return:
        """

    def get_color_raw(self) -> (int | None, int | None, int | None):
        """
        Returns the color sensor's raw readout
        :return: red, green, blue
        """

    def rgb2hsv(r: float, g: float, b: float) -> (float, float, float):
        """
        Converts normalized rgb to hsv
        :param r:
        :param g:
        :param b:
        :return:
        """

    def get_color(self, color_format: str = 'rgb') -> (float | None, float | None, float | None):
        """
        Returns the normalized color readout of the color sensor
        :param color_format: rgb or hsv only
        :return:
        """

    def get_color_label(self) -> str:
        """
        Returns the label of the color as recognized by the sensor
        :return:
        """

    def hsv2label(h, s, v) -> str:
        """
        Returns the color label corresponding to the given normalized HSV color input
        :param h:
        :param s:
        :param v:
        :return:
        """

    def get_distance(self, unit: str = 'cm') -> (float | None, float | None, float | None, float | None, float | None):
        """
        Returns the distance readout of the TOF sensor
        :param unit: distance output unit
        :return: left_tof, center_left_tof, center_tof, center_right_tof, right_tof
        """

    def get_distance_top(self, unit: str = 'cm') -> float | None:
        """
        Returns the obstacle top distance readout
        :param unit:
        :return:
        """

    def get_distance_bottom(self, unit: str = 'cm') -> float | None:
        """
        Returns the obstacle bottom distance readout
        :param unit:
        :return:
        """


    def get_version(self) -> str:
        """
        Returns the firmware version of the Alvik
        :return:
        """


    def print_status(self):
        """
        Prints the Alvik status
        :return:
        """

    def on_touch_ok_pressed(self, callback: callable, args: tuple = ()) -> None:
        """
        Register callback when touch button OK is pressed
        :param callback:
        :param args:
        :return:
        """

    def on_touch_cancel_pressed(self, callback: callable, args: tuple = ()) -> None:
        """
        Register callback when touch button CANCEL is pressed
        :param callback:
        :param args:
        :return:
        """

    def on_touch_center_pressed(self, callback: callable, args: tuple = ()) -> None:
        """
        Register callback when touch button CENTER is pressed
        :param callback:
        :param args:
        :return:
        """

    def on_touch_up_pressed(self, callback: callable, args: tuple = ()) -> None:
        """
        Register callback when touch button UP is pressed
        :param callback:
        :param args:
        :return:
        """

    def on_touch_left_pressed(self, callback: callable, args: tuple = ()) -> None:
        """
        Register callback when touch button LEFT is pressed
        :param callback:
        :param args:
        :return:
        """

    def on_touch_down_pressed(self, callback: callable, args: tuple = ()) -> None:
        """
        Register callback when touch button DOWN is pressed
        :param callback:
        :param args:
        :return:
        """

    def on_touch_right_pressed(self, callback: callable, args: tuple = ()) -> None:
        """
        Register callback when touch button RIGHT is pressed
        :param callback:
        :param args:
        :return:
        """

## Arduino AlvikWheel Class


    def reset(self, initial_position: float = 0.0, unit: str = 'deg'):
        """
        Resets the wheel reference position
        :param initial_position:
        :param unit: reference position unit (defaults to deg)
        :return:
        """

    def set_pid_gains(self, kp: float = MOTOR_KP_DEFAULT, ki: float = MOTOR_KI_DEFAULT, kd: float = MOTOR_KD_DEFAULT):
        """
        Set PID gains for Alvik wheels
        :param kp: proportional gain
        :param ki: integration gain
        :param kd: derivative gain
        :return:
        """


    def stop(self):
        """
        Stop Alvik wheel
        :return:
        """

    def set_speed(self, velocity: float, unit: str = 'rpm'):
        """
        Sets the motor speed
        :param velocity: the speed of the motor
        :param unit: the unit of measurement
        :return:
        """

    def get_speed(self, unit: str = 'rpm') -> float | None:
        """
        Returns the current RPM speed of the wheel
        :param unit: the unit of the output speed
        :return:
        """

    def get_position(self, unit: str = 'deg') -> float | None:
        """
        Returns the wheel position (angle with respect to the reference)
        :param unit: the unit of the output position
        :return:
        """


    def set_position(self, position: float, unit: str = 'deg'):
        """
        Sets left/right motor speed
        :param position: the speed of the motor
        :param unit: the unit of measurement
        :return:
        """

## Arduino AlvikRgbLed Class

    def set_color(self, red: bool, green: bool, blue: bool):
        """
        Sets the LED's r,g,b state
        :param red:
        :param green:
        :param blue:
        :return:
        """

## Arduino AlvikEvents Class

    def register_callback(self, event_name: str, callback: callable, args: tuple = None):
        """
        Registers a callback to execute on an event
        :param event_name:
        :param callback: the callable
        :param args: arguments tuple to pass to the callable. remember the comma! (value,)
        :return:
        """

    def has_callbacks(self) -> bool:
        """
        True if the _callbacks dictionary has any callback registered
        :return:
        """

    def execute_callback(self, event_name: str):
        """
        Executes the callback associated to the event_name
        :param event_name:
        :return:
        """

## Arduino AlvikTouchEvents Class

    def update_touch_state(self, touch_state: int):
        """
        Updates the internal touch state and executes any possible callback
        :param touch_state:
        :return:
        """


## UPDATE FIRMWARE METHOD

    def update_firmware(file_path: str):
        """
        :param file_path: path of your FW bin
        :return:
        """
