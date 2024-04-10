---
title: Serial.write()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Writes binary data to the serial port. This data is sent as a byte or
series of bytes; to send the characters representing the digits of a
number use the [print()](../print) function instead.

**Syntax**

`_Serial_.write(val)`
`_Serial_.write(str)`
`_Serial_.write(buf, len)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`val`: a value to send as a single byte.
`str`: a string to send as a series of bytes.
`buf`: an array to send as a series of bytes.
`len`: the number of bytes to be sent from the array.

**Returns**

`write()` will return the number of bytes written, though reading that
number is optional. Data type: `size_t`.

**Example Code**

    void setup() {
      Serial.begin(9600);
    }

    void loop() {
      Serial.write(45); // send a byte with the value 45

      int bytesSent = Serial.write("hello");  //send the string "hello" and return the length of the string.
    }

**Notes and Warnings**

Serial transmission is asynchronous. If there is enough empty space in
the transmit buffer, `Serial.write()` will return before any characters
are transmitted over serial. If the transmit buffer is full then
`Serial.write()` will block until there is enough space in the buffer.
To avoid blocking calls to `Serial.write()`, you can first check the
amount of free space in the transmit buffer using
[availableForWrite()](../availableforwrite).

