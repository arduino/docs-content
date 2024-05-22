---
title: "Getting Started with Alvik"
difficulty: beginner
description: "Take your first steps with Alvik"
tags:
  - Robot
author: "Jose Garcia"
---
# Getting Started With Alvik

Arduino® Alvik is a powerful and versatile robot specifically designed for programming and STEAM education.
![Alvik's Robot](assets/alvik_main.jpg)

Powered by the Arduino® Nano ESP32, Alvik offers diverse learning paths through different programming languages including MicroPython, the Arduino language, and block-based coding; enabling different possibilities to explore Robotics, IoT and Artificial Intelligence.


## Unboxing Alvik

![Selecting one of the ready-to-go examples](assets/select-examples.gif)

Your Alvik robot is equipped with three ready-to-go examples. To choose one of the examples, just turn your Alvik ON, wait until the LEDs turn blue and use the Up and Down buttons to pick one color, then hit the "tick" confirmation button. It's that easy!

- **Red Program (Touch Mode):** Use the arrows to tell your robot what to do: up and down for moving forward and backward by 10 cm, and left and right for turning 90 degrees in each of the directions. The robot will collect instructions until you press the "tick" confirmation button. Once you press it, the robot will execute all the actions in order.

- **Green Program (Hand Follower):** Your robot will keep a steady 10 cm distance from your hand or any object you put in front of it. Press the "tick" confirmation button again to make the robot start following your hand.

- **Blue Program (Line Follower):** Your robot will glide along a black line on a white surface. Press the "tick" confirmation button again to make the robot follow the line. You can stop the robot at any moment by pressing the "X" cancel button. **The recommended size for the "black line" to follow is between 2-3 cm wide.**

Now that you have played with Alvik and have seen it moving, it is time to know more in-depth how it is built and how to get much more than the out-of-the-box experience from it.

## Let's Start Coding Alvik

Alvik is intended to be programmed with MicroPyton. We recommend you to install the [Arduino Lab for MicroPython](https://labs.arduino.cc/en/labs/micropython) editor.

Now that all the previous steps have been set, let's see how to create custom programs for Alvik to move forward until detecting an object in front of it, Alvik will detect it, dodge it and continue on its way.

**1. **Create an Alvik folder in your computer and set it as the path of the Arduino Lab for MicroPython IDE

![Adding Alvik folder path to the IDE](assets/alvik_folder_path.png)

**2. **Create a new file "obstacle_avoider.py" in your local folder

![Creating obstacle_avoider.py file](assets/creating_file.png)

**3. **Double click on the file to open it. Once it is opened, erase the text on it and add the following code.

![Adding custom code](assets/adding_custom_code.gif)

``` python
from arduino_alvik import ArduinoAlvik
from time import sleep_ms
import sys

alvik = ArduinoAlvik()
alvik.begin()
sleep_ms(5000)  #waiting for the robot to setup
#robot.set_illuminator(0)
distance = 10
speed = 40 #rpm

def turning():
    alvik.set_wheels_speed(0,0)
    sleep_ms(250)
    alvik.set_wheels_speed(-35,-35)
    sleep_ms(1500)
    alvik.set_wheels_speed(35,-35)
    sleep_ms(1000)

while (True):

    distance_l, distance_cl, distance_c, distance_r, distance_cr  = alvik.get_distance()
    sleep_ms(50)
    print(distance_c)

    if distance_c < distance:
        turning()
    elif distance_cl < distance:
        turning()
    elif distance_cr < distance:
        turning()
    elif distance_l < distance:
        turning()
    elif distance_r < distance:
        turning()
    else:
        alvik.set_wheels_speed(speed, speed)

```

**4. **Connect Alvik to your PC using the cable included in the box, under the tray.

![Connecting Alvik to the PC](assets/connecting_alvik.gif)

***Make sure that Alvik is OFF before connecting it to your PC***

**5. **Once Alvik is connected to the PC, connect it to the Arduino Lab for MicroPython and open the _main.py_ file in the Alvik folder. Once the file is opened let's replace the `import demo` statement by `import obstacle_avoider`.

![Connecting Alvik to the IDE](assets/connecting_alvik_ide.gif)

*** If you want to go back to the out of the box experience where you could select between reg, green and blue programs, you only need to modify the _main.py_ again replacing the `import obstacle_avoider` statement by `import demo`***

**6. **The last step is to move the _obstacle_avoider.py_ file from the local repository to Alvik's memory.

![Moving file from local to Alvik's memory](assets/local2memory.gif)

You are now all set, disconnect Alvik from the PC, put some obstacles around Alvik, turn it ON and see how Alvik detects them and turns to avoid them.

## Next Steps
* There are a set of already build examples that will help you to better understand how Alvik works, you can download them from [this link](https://github.com/arduino/arduino-alvik-mpy/archive/refs/tags/0.2.0.zip), unzip them in your already created _alvik_ folder and you will be able to see them straight away in the Labs for MicroPython IDE
*  If you want to learn more about how Alvik is built or which functions you can use to program it, visit the documentation in the [Docs space for Alvik](https://docs.arduino.cc/hardware/alvik/).
* If you want to follow step-by-step guided projects following a educational approach to learn micropython and robotics topics with Alvik, follow the [Explore Robotics in MicroPython](https://explore-robotics-micropython.vercel.app/explore-robotics-micropython/) course.
