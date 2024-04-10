---
title: Keyboard.press()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

When called, `Keyboard.press()` functions as if a key were pressed and
held on your keyboard. Useful when using [modifier
keys](../keyboardmodifiers). To end the key press, use
[Keyboard.release()](../keyboardrelease) or
[Keyboard.releaseAll()](../keyboardreleaseall).

It is necessary to call [Keyboard.begin()](../keyboardbegin) before
using `press()`.

**Syntax**

`Keyboard.press(key)`

**Parameters**

`key`: the key to press. Allowed data types: `char`.

**Returns**

Number of key presses sent. Data type: `size_t`.

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

