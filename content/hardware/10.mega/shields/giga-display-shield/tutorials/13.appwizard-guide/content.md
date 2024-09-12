---
title: GIGA Display Shield app wizard Guide
description: 'Learn how to use Seggers App Wizard with the GIGA Display Shield.'
author: Benjamin Dannegård
tags: [Display, appwizard, segger, GUI]
---

## Introduction

Segger's app wizard is a graphical framework for building powerful UIs, and is fully compatible with the GIGA Display Shield. It allows you to build UIs, using pre-made widgets like buttons, images, loading bars, sliders, checkboxes, etc. It also allows you to fully customize the screenspace on the display. In this guide, we will go through some of the different components, so you can learn how to best implement it in your projects.

![Appwizard full demo running on the GIGA Display Shield](assets/)

## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](https://store.arduino.cc/products/giga-r1-wifi)
- [Arduino GIGA Display Shield](https://store.arduino.cc/products/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)
- [App Wizard](https://www.segger.com/products/user-interface/emwin/tools/appwizard/)
- [emWin Arduino Library](https://github.com/SEGGERMicro/emWin-Arduino-Library/)

## Downloading the Library and Core

The GIGA R1 core includes the [Arduino_H7_Video](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) library that handles the display.

In this guide, we will be using three different libraries:
- [Arduino_H7_Video](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video), this one is bundled with the core, so make sure you have the latest version of the [Mbed core](https://github.com/arduino/ArduinoCore-mbed) installed.
- [Arduino_GigaDisplayTouch](https://www.arduino.cc/reference/en/libraries/arduino_gigadisplaytouch/), handles touch on the GIGA Display Shield
- [emWin Arduino Library](https://github.com/SEGGERMicro/emWin-Arduino-Library/)

To install this, open the library manager and install the latest version by searching for **"Arduino_GigaDisplayTouch"**.

## Creating an App Wizard project

First go to  **File -> New Project** to start your new project. Here we need to configure certain settings so it will work on the GIGA Display Shield. Set the  display size x to **480** and display size y to **800**. Then we need to disable the **Enable simulation** and **Generate loop in MainTask()** options. It should look like the image below.

![Create project settings]()

## Setting Up The Project
First add a **screen** element to your project, this will be the base that contains all the other elements of the project.

![Screen highlighted]()

To add a background color add the **Box** object and set the color on the right side properties menu.

![Box highlighted]()

### Button

Add a button from the object menu. On the right hand properties menu you can set the color of the button when it is unpressed and pressed.

![Adding a button]()

In the right hand properties menu you can also add text to the button. Press the **set text** option. This will bring up a window that contains all the text elements in the project. Press **add text**, this will create a new text object with a unique id. Now to set the text that will be displayed press **New language** and enter **En**, we will be using English in this tutorial. Under the new **En** tab you can set the text that will be visible, change the **-** to **Button** and this text will be displayed on the button.

[Text objects box]()

## Adding Interactions

### Textbox

Let's add a textbox which will display a value that will increase when the button is pressed.

First add a textbox by clicking the **Text** box in the "Add objects" section. Then feel free to set the text color and background color to your desired color in the properties menu. Here the textbox needs to be set to decimal mode, do that by clicking the "Set decimal mode" button and then putting a "0" in the mask box.

[Textbox added]()

Next a variable is needed to keep track of the value. In the bottom left "Rescoureces" section press the **Open variables window** button. This will open a window where variables can be managed.

[Variables window highlighted in App Wizard]()

Press **Add variable** and then rename the variable to something relevant so it is easier to keep track of later, here we will name it "ID_BUTTON_VAR".

[Image of variable window]()

Now we need to add interactions for the button and text. Press the **+** button in the interactions box to add an interaction. Set the variable as the "Emitter", the signal should be "VALUE_CHANGED", job should be "SETVALUE" and the receiver should be the text box which here is "ID_TEXT_00". Now the text will be set to the same value as the variable.

To add the buttons interaction, set the emitter as the button, the signal should be "RELEASED", so that the value increses when the button is released. The job should be "ADDVALUE" and the receiver should be the variable, so the value gets added to the variable. In the window that pops up the increment of the value added to the variable, here we set it to "1". You can try out the interaction by pressing the **Start play mode** in the upper right corner of the "Editor" window.

### Progress Bar

Now lets try adding a progress bar to the previous interaction. Start by pressing the **progbar** button and set the initial value to "0". 


### Gauge

### Slider



## Exporting the project

## 

## Conclusion

This guide went through the building blocks of the different components that can be implemented with emWin. To see these examples in a full running example sketch go to **File > Examples > Arduino_H7_Video > emWinDemo**.

![Example in the IDE](assets/example-in-ide.png)

This demo sketch will show the different components using a screen manager in a 2x2 grid.

## Next Step
emWin is a comprehensive library and GUI framework that has a lot of customizability, if you are interested in playing around more with it, you can find many different examples and widgets on the official website for [Segger® emWin](https://wiki.segger.com/Main_Page). The code on the website can easily be adapted into a sketch for the GIGA Display Shield.
