---
title: 'Arduino Libraries'
description: 'Libraries are files which provide your sketches with extra functionality.'
tags: 
  - Libraries
---
Libraries are files written in C or C++ (.c, .cpp) which provide your sketches with extra functionality (e.g. the ability to control an LED matrix, or read an encoder, etc.). They were introduced in Arduino 0004.

To use an existing library in a sketch simply go to the Sketch menu, choose "Import Library", and pick from the libraries available. This will insert an **#include** statement at the top of the sketch for each header (.h) file in the library's folder. These statements make the public functions and constants defined by the library available to your sketch. They also signal the Arduino environment to link that library's code with your sketch when it is compiled or uploaded.

User-created libraries as of version 0017 go in a subdirectory of your default sketch directory. For example, on OSX, the new directory would be **~/Documents/Arduino/libraries/**. On Windows, it would be **My Documents\Arduino\libraries\.**  To add your own library, create a new directory in the libraries directory with the name of your library. The folder should contain a C or C++ file with your code and a header file with your function and variable declarations. It will then appear in the **Sketch | Import Library** menu in the Arduino IDE.

**Note:** for users of versions previous to 0017, libraries belong in a subdirectory of the Arduino application directory: **ARDUINO/lib/targets/libraries.** For version 0017, the libraries directory was moved to make them more convenient to install and use.

Because libraries are uploaded to the board with your sketch, they increase the amount of space used by the ATmega8 on the board. See the [FAQ](http://www.arduino.cc/en/Main/FAQ) for an explanation of various memory limitations and tips on reducing program size. If a sketch no longer needs a library, simply delete its **#include** statements from the top of your code. This will stop the Arduino IDE from linking the library with your sketch and decrease the amount of space used on the Arduino board.

To get started writing libraries, download this [test library](https://www.arduino.cc/en/uploads/Hacking/Test.zip). It should provide a basic template for creating a new library. After you've made changes to your library, in order to get it to recompile, you will have to delete the .o file generated in the library's directory.