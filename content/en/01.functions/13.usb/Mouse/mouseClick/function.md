---
title: Mouse.click()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Sends a momentary click to the computer at the location of the cursor.
This is the same as pressing and immediately releasing the mouse button.

`Mouse.click()` defaults to the left mouse button.

**Syntax**

`Mouse.click()`
`Mouse.click(button)`

**Parameters**

`button`: which mouse button to press. Allowed data types: `char`.

-   `MOUSE_LEFT` (default)

-   `MOUSE_RIGHT`

-   `MOUSE_MIDDLE`

**Returns**

Nothing

**Example Code**

    #include <Mouse.h>

    void setup() {
      pinMode(2, INPUT);
      //initiate the Mouse library
      Mouse.begin();
    }

    void loop() {
      //if the button is pressed, send a left mouse click
      if (digitalRead(2) == HIGH) {
        Mouse.click();
      }
    }

**Notes and Warnings**

When you use the `Mouse.click()` command, the Arduino takes over your
mouse! Make sure you have control before you use the command. A
pushbutton to toggle the mouse control state is effective.

**See also**

-   LANGUAGE [Mouse.end()](../mouseend)

-   LANGUAGE [Mouse.move()](../mousemove)

-   LANGUAGE [Mouse.press()](../mousepress)

-   LANGUAGE [Mouse.release()](../mouserelease)

-   LANGUAGE [Mouse.isPressed()](../mouseispressed)

