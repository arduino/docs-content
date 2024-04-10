---
title: Mouse.begin()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Begins emulating the mouse connected to a computer. `begin()` must be
called before controlling the computer. To end control, use
[Mouse.end()](../mouseend).

**Syntax**

`Mouse.begin()`

**Parameters**

None

**Returns**

Nothing

**Example Code**

    #include <Mouse.h>

    void setup() {
      pinMode(2, INPUT);
    }

    void loop() {
      //initiate the Mouse library when button is pressed
      if (digitalRead(2) == HIGH) {
        Mouse.begin();
      }
    }

**See also**

-   LANGUAGE [Mouse.click()](../mouseclick)

-   LANGUAGE [Mouse.end()](../mouseend)

-   LANGUAGE [Mouse.move()](../mousemove)

-   LANGUAGE [Mouse.press()](../mousepress)

-   LANGUAGE [Mouse.release()](../mouserelease)

-   LANGUAGE [Mouse.isPressed()](../mouseispressed)

