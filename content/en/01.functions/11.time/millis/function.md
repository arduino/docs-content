---
title: millis()
categories: "Functions"
subCategories: "Time"
---

**Description**

Returns the number of milliseconds passed since the Arduino board began
running the current program. This number will overflow (go back to
zero), after approximately 50 days.

**Syntax**

`time = millis()`

**Parameters**

None

**Returns**

Number of milliseconds passed since the program started. Data type:
`unsigned long`.

**Example Code**

This example code prints on the serial port the number of milliseconds
passed since the Arduino board started running the code itself.

    unsigned long myTime;

    void setup() {
      Serial.begin(9600);
    }
    void loop() {
      Serial.print("Time: ");
      myTime = millis();

      Serial.println(myTime); // prints time since program started
      delay(1000);          // wait a second so as not to send massive amounts of data
    }

**Notes and Warnings**

-   The return value for millis() is of type `unsigned long`, logic
    errors may occur if a programmer tries to do arithmetic with smaller
    data types such as `int`. Even signed `long` may encounter errors as
    its maximum value is half that of its unsigned counterpart.

-   millis() is incremented (for 16 MHz AVR chips and some others) every
    1.024 milliseconds, then incrementing by 2 (rather than 1) every 41
    or 42 ticks, to pull it back into synch; thus some millis() values
    are skipped. For accurate timing over short intervals, consider
    using micros().

-   millis() will wrap around to 0 after about 49 days (micros in about
    71 minutes).

-   Reconfiguration of the microcontroller’s timers may result in
    inaccurate `millis()` readings. The "Arduino AVR Boards" and
    "Arduino megaAVR Boards" cores use Timer0 to generate `millis()`.
    The "Arduino ARM (32-bits) Boards" and "Arduino SAMD (32-bits ARM
    Cortex-M0+) Boards" cores use the SysTick timer.

**See also**

-   EXAMPLE [Blink Without
    Delay^](http://arduino.cc/en/Tutorial/BlinkWithoutDelay)

