---
title: Keyboard.end()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Stops the keyboard emulation to a connected computer. To start keyboard
emulation, use [Keyboard.begin()](../keyboardbegin).

**Syntax**

`Keyboard.end()`

**Parameters**

None

**Returns**

Nothing

**Example Code**

    #include <Keyboard.h>

    void setup() {
      //start keyboard communication
      Keyboard.begin();
      //send a keystroke
      Keyboard.print("Hello!");
      //end keyboard communication
      Keyboard.end();
    }

    void loop() {
      //do nothing
    }

