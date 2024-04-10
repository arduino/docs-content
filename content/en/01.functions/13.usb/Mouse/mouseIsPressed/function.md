---
title: Mouse.isPressed()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Checks the current status of all mouse buttons, and reports if any are
pressed or not.

**Syntax**

`Mouse.isPressed();`
`Mouse.isPressed(button);`

**Parameters**

When there is no value passed, it checks the status of the left mouse
button.

`button`: which mouse button to check. Allowed data types: `char`.

-   `MOUSE_LEFT (default)`

-   `MOUSE_RIGHT`

-   `MOUSE_MIDDLE`

**Returns**

Reports whether a button is pressed or not. Data type: `bool`.

**Example Code**

    #include <Mouse.h>

    void setup() {
      //The switch that will initiate the Mouse press
      pinMode(2, INPUT);
      //The switch that will terminate the Mouse press
      pinMode(3, INPUT);
      //Start serial communication with the computer
      Serial.begin(9600);
      //initiate the Mouse library
      Mouse.begin();
    }

    void loop() {
      //a variable for checking the button's state
      int mouseState = 0;
      //if the switch attached to pin 2 is closed, press and hold the left mouse button and save the state ina  variable
      if (digitalRead(2) == HIGH) {
        Mouse.press();
        mouseState = Mouse.isPressed();
      }
      //if the switch attached to pin 3 is closed, release the left mouse button and save the state in a variable
      if (digitalRead(3) == HIGH) {
        Mouse.release();
        mouseState = Mouse.isPressed();
      }
      //print out the current mouse button state
      Serial.println(mouseState);
      delay(10);
    }

**See also**

-   LANGUAGE [Mouse.click()](../mouseclick)

-   LANGUAGE [Mouse.end()](../mouseend)

-   LANGUAGE [Mouse.move()](../mousemove)

-   LANGUAGE [Mouse.press()](../mousepress)

-   LANGUAGE [Mouse.release()](../mouserelease)

