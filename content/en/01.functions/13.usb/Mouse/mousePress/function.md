---
title: Mouse.press()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Sends a button press to a connected computer. A press is the equivalent
of clicking and continuously holding the mouse button. A press is
cancelled with [Mouse.release()](../mouserelease).

Before using `Mouse.press()`, you need to start communication with
[Mouse.begin()](../mousebegin).

`Mouse.press()` defaults to a left button press.

**Syntax**

`Mouse.press()`
`Mouse.press(button)`

**Parameters**

`button`: which mouse button to press. Allowed data types: `char`.

-   `MOUSE_LEFT (default)`

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

When you use the `Mouse.press()` command, the Arduino takes over your
mouse! Make sure you have control before you use the command. A
pushbutton to toggle the mouse control state is effective.

**See also**

-   LANGUAGE [Mouse.click()](../mouseclick)

-   LANGUAGE [Mouse.end()](../mouseend)

-   LANGUAGE [Mouse.move()](../mousemove)

-   LANGUAGE [Mouse.release()](../mouserelease)

-   LANGUAGE [Mouse.isPressed()](../mouseispressed)

