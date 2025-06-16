---
title: GIGA Display Shield AppWizard Guide
description: 'Learn how to use Segger AppWizard with the GIGA Display Shield.'
author: Benjamin Dannegård
tags: [Display, appwizard, segger, GUI]
---

## Introduction

Segger AppWizard is a graphical framework for building powerful UIs, and is fully compatible with the GIGA Display Shield. It allows you to build UIs, using pre-made widgets like buttons, images, loading bars, sliders, checkboxes, etc. It also allows you to fully customize the screen space on the display. In this guide, we will go through some of the different components and interactions, so you can learn how to best use AppWizard for your own projects.

![AppWizard GUI on GIGA Display Shield](assets/thumbnail.png)

Specifically, we will show you how to create a screen with AppWizard that includes some of the most common elements: a button, a text label, a progress bar, and a slider. We will also demonstrate how to export the code from AppWizard and create an Arduino library that implements the designed screen.

## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](https://store.arduino.cc/products/giga-r1-wifi)
- [Arduino GIGA Display Shield](https://store.arduino.cc/products/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)
- [AppWizard V1.44_6.38](https://www.segger.com/products/user-interface/emwin/tools/appwizard/)
- [emWin Arduino Library](https://github.com/SEGGERMicro/emWin-Arduino-Library/)

## Downloading the Library and Core

The GIGA R1 core includes the [Arduino_H7_Video](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) library that handles the display.

In this guide, we will be using three different libraries:
- [Arduino_H7_Video](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video), this one is bundled with the core, so make sure you have the latest version of the [Mbed core](https://github.com/arduino/ArduinoCore-mbed) installed.
- [Arduino_GigaDisplayTouch](https://www.arduino.cc/reference/en/libraries/arduino_gigadisplaytouch/), handles touch on the GIGA Display Shield
- [emWin Arduino Library](https://github.com/SEGGERMicro/emWin-Arduino-Library/)

To install this, open the library manager and install the latest version by searching for **"Arduino_GigaDisplayTouch"**.

## Creating an App Wizard Project

First go to **File -> New Project** to start your new project. Here we need to configure certain settings so it will work on the GIGA Display Shield. Set the `display size x` to **480** and `display size y` to **800**. Then we need to disable the `Enable simulation` and `Generate loop in MainTask()` options. It should look like the image below.

![Create project settings](assets/start-project.png)

## Setting Up The Project
First add a **screen** element to your project, this will be the base that contains all the other elements of the project. To add a background color add the **Box** object and set the color on the right side "Properties" menu.

![Screen and Box highlighted](assets/appwizard-screen-box.png)

## Creating Objects

### Button

Add a button from the object menu. On the right hand properties menu you can set the color of the button when it is unpressed and pressed.

![Adding a button](assets/appwizard-button.png)

In the right hand properties menu you can also add text to the button. Press the **set text** option. This will bring up a window that contains all the text elements in the project. Press **add text**, this will create a new text object with a unique id. Now to set the text that will be displayed press **New language** and enter **En**, we will be using English in this tutorial. Under the new **En** tab you can set the text that will be visible, change the **-** to **Button** and this text will be displayed on the button.

![Text objects box](assets/appwizard-text-box.png)

### Slider

Next create a slider by pressing the **Slider** button on the top left menu. You can configure the visual elements of the slider in the right "Properties" menu.

![Project with slider and gauge](assets/appwizard-slider.png)

### Switch

Next create a slider by pressing the **Switch** button on the top left menu. You can configure the visual elements of the switch in the right "Properties" menu.

![Project with switch](assets/appwizard-switch.png)

### Rotary

Next create a slider by pressing the **Rotary** button on the top left menu. You can configure the visual elements of the rotary in the right "Properties" menu.

![Project with rotary](assets/appwizard-rotary.png)

Now the complete project should look like this:

![Complete project](assets/appwizard-complete-gui.png)

Let's move on to how we can export this project to be displayed on the GIGA Display Shield.

## Exporting the Project

In AppWizard, go to **File -> Export & Save** in the upper left of the window. Now open the folder of the project. Create a new folder which we will put the exported files into, in this new folder create another folder named **src**. Now from the exported project folder, copy all the files contained in the **Resource** and **Source** subfolders (without copying the subfolders themselves) into the newly created **src** folder. Take all the files out of the folders before putting them in the **src** folder, if you have any folders inside of the **src** folder it will not import into the Arduino IDE later.

![Folder structure](assets/appwizard-demo-folder-src.png)

Now the folder name needs to be removed from the `#include` directives of the generated files. Inside the **ID_SCREEN_00_Slots.c** file change the `#include "../Generated/Resource.h"`
and `#include "../Generated/ID_SCREEN_00.h"` to `#include "Resource.h"` and `#include "ID_SCREEN_00.h"`.

![Screenshot of code](assets/appwizard-demo-folder-library-code.png)

When this is done create a **library.properties** file inside the root of the newly created folder. Then put this text into the file, you can change the name to whatever you like:

```arduino
name=AppWizardDemoLib
version=1.0.0
author=SEGGER Microcontroller GmbH
maintainer=SEGGER Microcontroller GmbH info@segger.com
sentence=
paragraph=
category=Display
url=
architectures=
includes=
depends=
```

![Folder with library properties file](assets/appwizard-demo-folder-library.png)

Finally, to create the Arduino sketch, create an **examples** folder inside the root of the newly created folder, inside this **examples** folder you can create another folder containing the **demo.ino** file. Use the following code for the **demo.ino**:

```arduino
#include <Resource.h>
void setup() {
  MainTask();                 
}
void loop() {
  GUI_Exec();
}
```

![Examples folder structure](assets/appwizard-examples-folder.gif)

Now all that is left is to import this whole folder as a library into the Arduino IDE. First, **compress** the folder into a **.zip** format, then in the Arduino IDE go to **Sketch -> Include library -> Add .ZIP Library**, select the created .zip file and add it.

![Importing library in Arduino IDE](assets/appwizard-library-include.png)

Now the demo sketch should be accessible under the examples tab inside the library. The library will have the name given inside the **library.properties** file.

![Showing example sketch](assets/appwizard-library-example.png)

Now select your board and upload the sketch. The GUI created in AppWizard should now display on the GIGA Display Shield!

![GUI deployed on the GIGA Display](assets/result.png)

### Conclusion

Now you have an idea of how to use the basic features of AppWizard! This tutorial went through how easy it is to import your design to your Arduino board using the Arduino IDE. You are now ready to create your own design and play around with AppWizard!