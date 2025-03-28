---
slug: '/en/Tutorial/LibraryExamples/EsploraKart'
date: 'February 05, 2018, at 08:43 PM'
title: 'EsploraKart'
description: 'Use the Esplora as a controller to play a kart racing game.'
---



## Esplora Kart

This example demonstrates how to turn your Esplora into a customized computer game pad.  It uses the analog joystick and the four switches as inputs to a video game. The Esplora will appear to the computer as a standard keyboard, the computer will see joystick movement and button presses as keystrokes.

The configuration chosen in this example is suitable for SuperTuxKart, an open-source racing game, available for Windows, OSX, and Linux. It can be downloaded from [http://supertuxkart.sourceforge.net/](http://supertuxkart.sourceforge.net/) .

## Hardware Required

- Arduino Esplora

## Circuit

Only your Arduino Esplora is needed for this example. Connect the Esplora to your computer with a USB cable.

![Esplora as SuperTuxKart game controller](./assets/Esplora_kart.jpg)

 

## Code

The default keys to play with the SuperTuxKart game are:

| **command** | **key**         |
| ----------- | --------------- |
| Throttle    | KEY_UP_ARROW    |
| Brake       | KEY_DOWN_ARROW  |
| Turn right  | KEY_RIGHT_ARROW |
| Turn Left   | KEY_LEFT_ARROW  |
| Fire        | SPACE_BAR       |
| Bend        | V               |
| Nitro       | N               |
| Look back   | B               |

You need to map these keyboard keystrokes to the available inputs on your Esplora board. To handle the eight different buttons, you'll use [arrays](https://www.arduino.cc/reference/en/language/variables/data-types/array/), ordered lists of variables with a fixed size. Each array has an index (counting from 0) to keep track of the position you're reading in the array, and each position can contain a number.

This code uses three different arrays: one for the buttons you'll read, a second to hold the current state of the buttons, and a third to hold the keystrokes associated with each button.

The Esplora has the ability to appear to a connected computer as a USB keyboard, so when you press the buttons and move the joystick, it's just like pressing keys on your keyboard.

The [for](https://www.arduino.cc/reference/en/language/structure/control-structure/for/)() loop checks the state of all the buttons and the joystick. If the button's state has changed, then the corresponding keypress or release is sent to the computer.  See the [keyboard library reference](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/) for more information on using the Esplora as a keyboard or mouse.

```arduino

/*

  Esplora Kart

  This sketch turns the Esplora into a PC game pad.

  It uses the both the analog joystick and the four switches.

  By moving the joystick in a direction or by pressing a switch,

  the PC will "see" that a key is pressed. If the PC is running

  a game that has keyboard input, the Esplora can control it.

  The default configuration is suitable for SuperTuxKart, an

  open-source racing game. It can be downloaded from

  http://supertuxkart.sourceforge.net/ .

  Created on 22 november 2012

  By Enrico Gueli <enrico.gueli@gmail.com>

*/

#include <Esplora.h>

/*

  You're going to handle eight different buttons. You'll use arrays,

  which are ordered lists of variables with a fixed size. Each array

  has an index (counting from 0) to keep track of the position

  you're reading in the array, and each position can contain a number.

  This code uses three different arrays: one for the buttons you'll read;

  a second to hold the current states of those buttons; and a third to hold

  the keystrokes associated with each button.

 */

/*

  This array holds the last sensed state of each of the buttons

  you're reading.

  Later in the code, you'll read the button states, and compare them

  to the previous states that are stored in this array. If the two

  states are different, it means that the button was either

  pressed or released.

 */

bool buttonStates[8];

/*

  This array holds the names of the buttons being read.

  Later in the sketch, you'll use these names with

  the method Esplora.readButton(x), where x

  is one of these buttons.

 */

const byte buttons[] = {

  JOYSTICK_DOWN,

  JOYSTICK_LEFT,

  JOYSTICK_UP,

  JOYSTICK_RIGHT,

  SWITCH_RIGHT, // fire

  SWITCH_LEFT, // bend

  SWITCH_UP, // nitro

  SWITCH_DOWN, // look back
};

/*

  This array tells what keystroke to send to the PC when a

  button is pressed.

  If you look at this array and the above one, you can see that

  the "cursor down" keystroke is sent when the joystick is moved

  down, the "cursor up" keystroke when the joystick is moved up

  and so on.

*/

const char keystrokes[] = {

  KEY_DOWN_ARROW,

  KEY_LEFT_ARROW,

  KEY_UP_ARROW,

  KEY_RIGHT_ARROW,

  ' ',

  'V',

  'N',

  'B'
};

/*

  This is code is run only at startup, to initialize the

  virtual USB keyboard.

*/
void setup() {

  Keyboard.begin();
}

/*

  After setup() is finished, this code is run continuously.

  Here we continuously check if something happened with the

  buttons.

*/
void loop() {

  // Iterate through all the buttons:

  for (byte thisButton = 0; thisButton < 8; thisButton++) {

    bool lastState = buttonStates[thisButton];

    bool newState = Esplora.readButton(buttons[thisButton]);

    if (lastState != newState) { // Something changed!

      /*

        The Keyboard library allows you to "press" and "release" the

        keys as two distinct actions. These actions can be

        linked to the buttons we're handling.

       */

      if (newState == PRESSED) {

        Keyboard.press(keystrokes[thisButton]);

      } else if (newState == RELEASED) {

        Keyboard.release(keystrokes[thisButton]);

      }

    }

    // Store the new button state, so you can sense a difference later:

    buttonStates[thisButton] = newState;

  }

  /*

    Wait a little bit (50ms) between a check and another.

    When a mechanical switch is pressed or released, the

    contacts may bounce very rapidly. If the check is done too

    fast, these bounces may be confused as multiple presses and

    may lead to unexpected behaviour.

   */

  delay(50);
}
```
