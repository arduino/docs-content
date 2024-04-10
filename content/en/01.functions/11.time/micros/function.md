---
title: micros()
categories: "Functions"
subCategories: "Time"
---

**Description**

Returns the number of microseconds since the Arduino board began running
the current program. This number will overflow (go back to zero), after
approximately 70 minutes. On the boards from the Arduino Portenta family
this function has a resolution of one microsecond on all cores. On 16
MHz Arduino boards (e.g. Duemilanove and Nano), this function has a
resolution of four microseconds (i.e. the value returned is always a
multiple of four). On 8 MHz Arduino boards (e.g. the LilyPad), this
function has a resolution of eight microseconds.

**Syntax**

`time = micros()`

**Parameters**

None

**Returns**

Returns the number of microseconds since the Arduino board began running
the current program. Data type: `unsigned long`.

**Example Code**

The code returns the number of microseconds since the Arduino board
began.

    unsigned long time;

    void setup() {
      Serial.begin(9600);
    }
    void loop() {
      Serial.print("Time: ");
      time = micros();

      Serial.println(time); //prints time since program started
      delay(1000);          // wait a second so as not to send massive amounts of data
    }

**Notes and Warnings**

There are 1,000 microseconds in a millisecond and 1,000,000 microseconds
in a second.

**See also**

