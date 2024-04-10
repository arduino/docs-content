---
title: "#include"
categories: "Structure"
subCategories: "Further Syntax"
---

**Description**

`#include` is used to include outside libraries in your sketch. This
gives the programmer access to a large group of standard C libraries
(groups of pre-made functions), and also libraries written especially
for Arduino.

The main reference page for AVR C libraries (AVR is a reference to the
Atmel chips on which the Arduino is based) is
[here^](http://www.nongnu.org/avr-libc/user-manual/modules.html).

Note that `#include`, similar to `link:../define[#define]`, has no
semicolon terminator, and the compiler will yield cryptic error messages
if you add one.

**Syntax**

`#include <LibraryFile.h>`
`#include "LocalFile.h"`

**Parameters**

`LibraryFile.h`: when the angle brackets syntax is used, the libraries
paths will be searched for the file.
`LocalFile.h`: When the double quotes syntax is used, the folder of the
file using the `#include` directive will be searched for the specified
file, then the libraries paths if it was not found in the local path.
Use this syntax for header files in the sketch’s folder.

**Example Code**

This example includes the Servo library so that its functions may be
used to control a Servo motor.

    #include <Servo.h>

    Servo myservo;  // create servo object to control a servo

    void setup() {
      myservo.attach(9);  // attaches the servo on pin 9 to the servo object
    }

    void loop() {
      for (int pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
        // in steps of 1 degree
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      for (int pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
    }

**See also**

