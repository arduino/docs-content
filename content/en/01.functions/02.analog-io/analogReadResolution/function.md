---
title: analogReadResolution()
categories: "Functions"
subCategories: "Analog I/O"
---

**Description**

analogReadResolution() is an extension of the Analog API for the Zero,
Due, MKR family, Nano 33 (BLE and IoT) and Portenta.

Sets the size (in bits) of the value returned by `analogRead()`. It
defaults to 10 bits (returns values between 0-1023) for backward
compatibility with AVR based boards.

The **Zero, Due, MKR family and Nano 33 (BLE and IoT)** boards have
12-bit ADC capabilities that can be accessed by changing the resolution
to 12. This will return values from `analogRead()` between 0 and 4095.
The **Portenta H7** has a 16 bit ADC, which will allow values between 0
and 65535.

**Syntax**

`analogReadResolution(bits)`

**Parameters**

`bits`: determines the resolution (in bits) of the value returned by the
`analogRead()` function. You can set this between 1 and 32. You can set
resolutions higher than the supported 12 or 16 bits, but values returned
by `analogRead()` will suffer approximation. See the note below for
details.

**Returns**

Nothing

**Example Code**

The code shows how to use ADC with different resolutions.

    void setup() {
      // open a serial connection
      Serial.begin(9600);
    }

    void loop() {
      // read the input on A0 at default resolution (10 bits)
      // and send it out the serial connection
      analogReadResolution(10);
      Serial.print("ADC 10-bit (default) : ");
      Serial.print(analogRead(A0));

      // change the resolution to 12 bits and read A0
      analogReadResolution(12);
      Serial.print(", 12-bit : ");
      Serial.print(analogRead(A0));

      // change the resolution to 16 bits and read A0
      analogReadResolution(16);
      Serial.print(", 16-bit : ");
      Serial.print(analogRead(A0));

      // change the resolution to 8 bits and read A0
      analogReadResolution(8);
      Serial.print(", 8-bit : ");
      Serial.println(analogRead(A0));

      // a little delay to not hog Serial Monitor
      delay(100);
    }

**Notes and Warnings**

If you set the `analogReadResolution()` value to a value higher than
your board’s capabilities, the Arduino will only report back at its
highest resolution, padding the extra bits with zeros.

For example: using the Due with `analogReadResolution(16)` will give you
an approximated 16-bit number with the first 12 bits containing the real
ADC reading and the last 4 bits **padded with zeros**.

If you set the `analogReadResolution()` value to a value lower than your
board’s capabilities, the extra least significant bits read from the ADC
will be **discarded**.

Using a 16 bit resolution (or any resolution **higher** than actual
hardware capabilities) allows you to write sketches that automatically
handle devices with a higher resolution ADC when these become available
on future boards without changing a line of code.

**See also**

-   EXAMPLE [Description of the analog input
    pins^](http://arduino.cc/en/Tutorial/AnalogInputPins)

-   LANGUAGE [analogRead()](../../analog-io/analogread)

