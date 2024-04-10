---
title: Keyboard.begin()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

When used with a Leonardo or Due board, `Keyboard.begin()` starts
emulating a keyboard connected to a computer. To end control, use
[Keyboard.end()](../keyboardend).

**Syntax**

`Keyboard.begin()`
`Keyboard.begin(layout)`

**Parameters**

`layout`: the keyboard layout to use. This parameter is optional and
defaults to `KeyboardLayout_en_US`.

**Keyboard layouts**

Currently, the library supports the following national keyboard layouts:

-   `KeyboardLayout_da_DK`: Denmark

-   `KeyboardLayout_de_DE`: Germany

-   `KeyboardLayout_en_US`: USA

-   `KeyboardLayout_es_ES`: Spain

-   `KeyboardLayout_fr_FR`: France

-   `KeyboardLayout_hu_HU`: Hungary

-   `KeyboardLayout_it_IT`: Italy

-   `KeyboardLayout_pt_PT`: Portugal

-   `KeyboardLayout_sv_SE`: Sweden

**Returns**

Nothing

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
        Keyboard.print("Hello!");
      }
    }

**Notes and Warnings**

Custom layouts can be created by copying and modifying an existing
layout. See the instructions in the Keyboard library’s KeyboardLayout.h
file.

