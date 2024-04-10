---
title: Keyboard.println()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Sends one or more keystrokes to a connected computer, followed by a
keystroke on the Enter key.

`Keyboard.println()` must be called after initiating
[Keyboard.begin()](../keyboardbegin).

**Syntax**

`Keyboard.println()`
`Keyboard.println(character)`
`Keyboard.println(characters)`

**Parameters**

`character`: a char or int to be sent to the computer as a keystroke,
followed by Enter.
`characters`: a string to be sent to the computer as keystrokes,
followed by Enter.

**Returns**

Number of keystrokes sent. Data type: `size_t`.

**Example Code**

    #include <Keyboard.h>

    void setup() {
      // make pin 2 an input and turn on the
      // pullup resistor so it goes high unless
      // connected to ground:
      pinMode(2, INPUT_PULLUP);
      Keyboard.begin();
    }

    void loop() {
      //if the button is pressed
      if (digitalRead(2) == LOW) {
        //Send the message
        Keyboard.println("Hello!");
      }
    }

**Notes and Warnings**

When you use the Keyboard.println() command, the Arduino takes over your
keyboard! Make sure you have control before you use the command. A
pushbutton to toggle the keyboard control state is effective.

