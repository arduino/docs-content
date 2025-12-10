---
title: 'Keyboard Reprogram'
compatible-products: [due, micro, leonardo]
difficulty: intermediate
description: 'Opens a new window in the Arduino IDE and reprograms the Leonardo with a simple blink program.'
tags: 
  - USB
  - Keyboard
  - Pushbutton
---

This example uses the Keyboard library to open a new Arduino Software (IDE) sketch window, send keyboard commands that type in the Blink example, and reprograms the board. After running this sketch and connecting pin 2 to ground using the pushbutton, the board will have a new program, Blink.

**NB:  When you use the Keyboard.print() command, the Arduino takes over your computer's keyboard! To insure you don't lose control of your computer while running a sketch with this function, make sure to set up a reliable control system before you call Keyboard.print(). This sketch is designed to only send Keyboard commands after digital pin 2 is pulled to ground.**

### Hardware Required

- [Arduino Leonardo, Micro, or Due board](https://store.arduino.cc/collections/boards-modules)

- pushbutton

- hook-up wires

- breadboard

### Software Required

- Arduino IDE running

### Circuit


![](assets/circuit.png)


### Schematic

![](assets/schematic.png)

### Code

Connect your board to the USB port, then push the button to connect D2 with GND and initiate the sketch keyboard keypress emulation. Remember to have the Arduino Software (IDE) window selected before you press the button.

```arduino

/*

  Arduino Programs Blink

  This sketch demonstrates the Keyboard library.

  For Leonardo and Due boards only.

  When you connect pin 2 to ground, it creates a new window with a key

  combination (CTRL-N), then types in the Blink sketch, then auto-formats the

  text using another key combination (CTRL-T), then uploads the sketch to the

  currently selected Arduino using a final key combination (CTRL-U).

  Circuit:

  - Arduino Leonardo, Micro, Due, LilyPad USB, or Yún

  - wire to connect D2 to ground

  created 5 Mar 2012

  modified 29 Mar 2012

  by Tom Igoe

  modified 3 May 2014

  by Scott Fitzgerald

  This example is in the public domain.

  https://www.arduino.cc/en/Tutorial/KeyboardReprogram

*/

#include "Keyboard.h"

// use this option for OSX.
// Comment it out if using Windows or Linux:
char ctrlKey = KEY_LEFT_GUI;
// use this option for Windows and Linux.
// leave commented out if using OSX:
//  char ctrlKey = KEY_LEFT_CTRL;

void setup() {

  // make pin 2 an input and turn on the pull-up resistor so it goes high unless

  // connected to ground:

  pinMode(2, INPUT_PULLUP);

  // initialize control over the keyboard:

  Keyboard.begin();
}

void loop() {

  while (digitalRead(2) == HIGH) {

    // do nothing until pin 2 goes low

    delay(500);

  }

  delay(1000);

  // new document:

  Keyboard.press(ctrlKey);

  Keyboard.press('n');

  delay(100);

  Keyboard.releaseAll();

  // wait for new window to open:

  delay(1000);

  // versions of the Arduino IDE after 1.5 pre-populate new sketches with

  // setup() and loop() functions let's clear the window before typing anything new

  // select all

  Keyboard.press(ctrlKey);

  Keyboard.press('a');

  delay(500);

  Keyboard.releaseAll();

  // delete the selected text

  Keyboard.write(KEY_BACKSPACE);

  delay(500);

  // Type out "blink":

  Keyboard.println("void setup() {");

  Keyboard.println("pinMode(13, OUTPUT);");

  Keyboard.println("}");

  Keyboard.println();

  Keyboard.println("void loop() {");

  Keyboard.println("digitalWrite(13, HIGH);");

  Keyboard.print("delay(3000);");

  // 3000 ms is too long. Delete it:

  for (int keystrokes = 0; keystrokes < 6; keystrokes++) {

    delay(500);

    Keyboard.write(KEY_BACKSPACE);

  }

  // make it 1000 instead:

  Keyboard.println("1000);");

  Keyboard.println("digitalWrite(13, LOW);");

  Keyboard.println("delay(1000);");

  Keyboard.println("}");

  // tidy up:

  Keyboard.press(ctrlKey);

  Keyboard.press('t');

  delay(100);

  Keyboard.releaseAll();

  delay(3000);

  // upload code:

  Keyboard.press(ctrlKey);

  Keyboard.press('u');

  delay(100);

  Keyboard.releaseAll();

  // wait for the sweet oblivion of reprogramming:

  while (true);
}
```

### Learn more

You can find more basic tutorials in the [built-in examples](/built-in-examples) section.

You can also explore the [language reference](https://www.arduino.cc/reference/en/), a detailed collection of the Arduino programming language.

*Last revision 2015/07/29 by SM*