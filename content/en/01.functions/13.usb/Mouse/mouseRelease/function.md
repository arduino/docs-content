---
title: Mouse.release()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Sends a message that a previously pressed button (invoked through
[Mouse.press()](../mousepress)) is released. `Mouse.release()` defaults
to the left button.

**Syntax**

`Mouse.release()`
`Mouse.release(button)`

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
      //The switch that will initiate the Mouse press
      pinMode(2, INPUT);
      //The switch that will terminate the Mouse press
      pinMode(3, INPUT);
      //initiate the Mouse library
      Mouse.begin();
    }

    void loop() {
      //if the switch attached to pin 2 is closed, press and hold the left mouse button
      if (digitalRead(2) == HIGH) {
        Mouse.press();
      }
      //if the switch attached to pin 3 is closed, release the left mouse button
      if (digitalRead(3) == HIGH) {
        Mouse.release();
      }
    }

**Notes and Warnings**

When you use the `Mouse.release()` command, the Arduino takes over your
mouse! Make sure you have control before you use the command. A
pushbutton to toggle the mouse control state is effective.

**See also**

-   LANGUAGE [Mouse.click()](../mouseclick)

-   LANGUAGE [Mouse.end()](../mouseend)

-   LANGUAGE [Mouse.move()](../mousemove)

-   LANGUAGE [Mouse.press()](../mousepress)

-   LANGUAGE [Mouse.isPressed()](../mouseispressed)

