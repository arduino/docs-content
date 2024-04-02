# Alvik API cheat sheet

## Arduino Alvik Class

### is_on()
        """
        Returns true if robot is on
        :return:
        """


### begin()
        """
        Begins all Alvik operations
        :return:
        """


### is_target_reached()
        """
        Returns True if robot has sent an M or R acknowledgment.
        It also responds with an ack received message
        :return:
        """

### set_behaviour(behaviour: int)
        """
        Sets the behaviour of Alvik
        :param behaviour: behaviour code
        :return:
        """


### rotate(angle: float, unit: str = 'deg', blocking: bool = True)
        """
        Rotates the robot by given angle
        :param angle:
        :param blocking:
        :param unit: the angle unit
        :return:
        """


### move(distance: float, unit: str = 'cm', blocking: bool = True)
        """
        Moves the robot by given distance
        :param distance:
        :param blocking:
        :param unit: the distance unit
        :return:
        """


### stop()
        """
        Stops all Alvik operations
        :return:
        """


### get_wheels_speed(unit: str = 'rpm')
        """
        Returns the speed of the wheels
        :param unit: the speed unit of measurement (default: 'rpm')
        :return: left_wheel_speed, right_wheel_speed
        """


### set_wheels_speed(left_speed: float, right_speed: float, unit: str = 'rpm')
        """
        Sets left/right motor speed
        :param left_speed:
        :param right_speed:
        :param unit: the speed unit of measurement (default: 'rpm')
        :return:
        """


### set_wheels_position(left_angle: float, right_angle: float, unit: str = 'deg')
        """
        Sets left/right motor angle
        :param left_angle:
        :param right_angle:
        :param unit: the speed unit of measurement (default: 'rpm')
        :return:
        """


### get_wheels_position(unit: str = 'deg')
        """
        Returns the angle of the wheels
        :param unit: the angle unit of measurement (default: 'deg')
        :return: left_wheel_angle, right_wheel_angle
        """


### get_orientation()
        """
        Returns the orientation of the IMU
        :return: roll, pitch, yaw
        """

### get_accelerations()
        """
        Returns the 3-axial acceleration of the IMU
        :return: ax, ay, az
        """

### get_gyros()
        """
        Returns the 3-axial angular acceleration of the IMU
        :return: gx, gy, gz
        """

### get_imu()
        """
        Returns all the IMUs readouts
        :return: ax, ay, az, gx, gy, gz
        """

### get_line_sensors()
        """
        Returns the line sensors readout
        :return: left_line, center_line, right_line
        """

### drive(linear_velocity: float, angular_velocity: float, linear_unit: str = 'cm/s',angular_unit: str = 'deg/s')
        """
        Drives the robot by linear and angular velocity
        :param linear_velocity:
        :param angular_velocity:
        :param linear_unit: output linear velocity unit of meas
        :param angular_unit: output angular velocity unit of meas
        :return:
        """

### brake()
        """
        Brakes the robot
        :return:
        """

### get_drive_speed(linear_unit: str = 'cm/s', angular_unit: str = 'deg/s')
        """
        Returns linear and angular velocity of the robot
        :param linear_unit: output linear velocity unit of meas
        :param angular_unit: output angular velocity unit of meas
        :return: linear_velocity, angular_velocity
        """

### reset_pose(x: float, y: float, theta: float, distance_unit: str = 'cm', angle_unit: str = 'deg')
        """
        Resets the robot pose
        :param x: x coordinate of the robot
        :param y: y coordinate of the robot
        :param theta: angle of the robot
        :param distance_unit: angle of the robot
        :param angle_unit: angle of the robot
        :return:
        """

### get_pose(distance_unit: str = 'cm', angle_unit: str = 'deg')
           
        """
        Returns the current pose of the robot
        :param distance_unit: unit of x and y outputs
        :param angle_unit: unit of theta output
        :return: x, y, theta
        """

### set_servo_positions(a_position: int, b_position: int)
        """
        Sets A/B servomotor angle
        :param a_position: position of A servomotor (0-180)
        :param b_position: position of B servomotor (0-180)
        :return:
        """

### get_ack()
        """
        Returns last acknowledgement
        :return:
        """


### set_builtin_led(value: bool)
        """
        Turns on/off the builtin led
        :param value:
        :return:
        """

### set_illuminator(value: bool)
        """
        Turns on/off the illuminator led
        :param value:
        :return:
        """


### get_battery_charge()
        """
        Returns the battery SOC
        :return:
        """

### get_touch_any()
        """
        Returns true if any button is pressed
        :return:
        """

### get_touch_ok()
        """
        Returns true if ok button is pressed
        :return:
        """

### get_touch_cancel()
        """
        Returns true if cancel button is pressed
        :return:
        """

### get_touch_center()
        """
        Returns true if center button is pressed
        :return:
        """

### get_touch_up()
        """
        Returns true if up button is pressed
        :return:
        """

### get_touch_left()
        """
        Returns true if left button is pressed
        :return:
        """

### get_touch_down()
        """
        Returns true if down button is pressed
        :return:
        """

### get_touch_right()
        """
        Returns true if right button is pressed
        :return:
        """

### color_calibration(background: str = 'white')
        """
        Calibrates the color sensor
        :param background: str white or black
        :return:
        """

### get_color_raw()
        """
        Returns the color sensor's raw readout
        :return: red, green, blue
        """

### rgb2hsv(r: float, g: float, b: float)
        """
        Converts normalized rgb to hsv
        :param r:
        :param g:
        :param b:
        :return:
        """

### get_color(color_format: str = 'rgb')
        """
        Returns the normalized color readout of the color sensor
        :param color_format: rgb or hsv only
        :return:
        """

### get_color_label()
        """
        Returns the label of the color as recognized by the sensor
        :return:
        """

### hsv2label(h, s, v)
        """
        Returns the color label corresponding to the given normalized HSV color input
        :param h:
        :param s:
        :param v:
        :return:
        """

### get_distance(unit: str = 'cm')
        """
        Returns the distance readout of the TOF sensor
        :param unit: distance output unit
        :return: left_tof, center_left_tof, center_tof, center_right_tof, right_tof
        """

### get_distance_top(unit: str = 'cm')
        """
        Returns the obstacle top distance readout
        :param unit:
        :return:
        """

### get_distance_bottom(unit: str = 'cm')
        """
        Returns the obstacle bottom distance readout
        :param unit:
        :return:
        """


### get_version()
        """
        Returns the firmware version of the Alvik
        :return:
        """


### print_status()
        """
        Prints the Alvik status
        :return:
        """

### on_touch_ok_pressed(callback: callable, args: tuple = ())
        """
        Register callback when touch button OK is pressed
        :param callback:
        :param args:
        :return:
        """

### on_touch_cancel_pressed(callback: callable, args: tuple = ())
        """
        Register callback when touch button CANCEL is pressed
        :param callback:
        :param args:
        :return:
        """

### on_touch_center_pressed(callback: callable, args: tuple = ())
        """
        Register callback when touch button CENTER is pressed
        :param callback:
        :param args:
        :return:
        """

### on_touch_up_pressed(callback: callable, args: tuple = ())
        """
        Register callback when touch button UP is pressed
        :param callback:
        :param args:
        :return:
        """

### on_touch_left_pressed(callback: callable, args: tuple = ())
        """
        Register callback when touch button LEFT is pressed
        :param callback:
        :param args:
        :return:
        """

### on_touch_down_pressed(callback: callable, args: tuple = ())
        """
        Register callback when touch button DOWN is pressed
        :param callback:
        :param args:
        :return:
        """

### on_touch_right_pressed(callback: callable, args: tuple = ())
        """
        Register callback when touch button RIGHT is pressed
        :param callback:
        :param args:
        :return:
        """

## Arduino AlvikWheel Class


### reset(initial_position: float = 0.0, unit: str = 'deg')
        """
        Resets the wheel reference position
        :param initial_position:
        :param unit: reference position unit (defaults to deg)
        :return:
        """

### set_pid_gains(kp: float = MOTOR_KP_DEFAULT, ki: float = MOTOR_KI_DEFAULT, kd: float = MOTOR_KD_DEFAULT)
        """
        Set PID gains for Alvik wheels
        :param kp: proportional gain
        :param ki: integration gain
        :param kd: derivative gain
        :return:
        """


### stop()
        """
        Stop Alvik wheel
        :return:
        """

### set_speed(velocity: float, unit: str = 'rpm')
        """
        Sets the motor speed
        :param velocity: the speed of the motor
        :param unit: the unit of measurement
        :return:
        """

### get_speed(unit: str = 'rpm')
        """
        Returns the current RPM speed of the wheel
        :param unit: the unit of the output speed
        :return:
        """

### get_position(unit: str = 'deg')
        """
        Returns the wheel position (angle with respect to the reference)
        :param unit: the unit of the output position
        :return:
        """


### set_position(position: float, unit: str = 'deg')
        """
        Sets left/right motor speed
        :param position: the speed of the motor
        :param unit: the unit of measurement
        :return:
        """

## Arduino AlvikRgbLed Class

### set_color(red: bool, green: bool, blue: bool)
        """
        Sets the LED's r,g,b state
        :param red:
        :param green:
        :param blue:
        :return:
        """

## Arduino AlvikEvents Class

### register_callback(event_name: str, callback: callable, args: tuple = None)
        """
        Registers a callback to execute on an event
        :param event_name:
        :param callback: the callable
        :param args: arguments tuple to pass to the callable. remember the comma! (value,)
        :return:
        """

### has_callbacks()
        """
        True if the _callbacks dictionary has any callback registered
        :return:
        """

### execute_callback(event_name: str)
        """
        Executes the callback associated to the event_name
        :param event_name:
        :return:
        """

## Arduino AlvikTouchEvents Class

### update_touch_state(touch_state: int)
        """
        Updates the internal touch state and executes any possible callback
        :param touch_state:
        :return:
        """


## UPDATE FIRMWARE METHOD

### update_firmware(file_path: str)
        """
        Update the firmware
        :param file_path: path of your FW bin
        :return:
        """
