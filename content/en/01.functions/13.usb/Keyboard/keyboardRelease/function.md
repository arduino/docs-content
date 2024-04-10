---
title: Keyboard.release()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Lets go of the specified key. See [Keyboard.press()](../keyboardpress)
for more information.

**Syntax**

`Keyboard.release(key)`

**Parameters**

`key`: the key to release. Allowed data types: `char`.

**Returns**

The number of keys released. Data type: `size_t`.

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
      Keyboard.release(ctrlKey);
      Keyboard.release('n');
      // wait for new window to open:
      delay(1000);
    }

