---
title: Keyboard.releaseAll()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Lets go of all keys currently pressed. See
[Keyboard.press()](../keyboardpress) for additional information.

**Syntax**

`Keyboard.releaseAll()`

**Parameters**

None

**Returns**

Nothing

**Example Code**

    #include <Keyboard.h>

    // use this option for OSX:
    char ctrlKey = KEY_LEFT_GUI;
    // use this option for Windows and Linux:
    //  char ctrlKey = KEY_LEFT_CTRL;

    void setup() {
      // make pin 2 an input and turn on the
      // pullup resistor so it goes high unless
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
    }

