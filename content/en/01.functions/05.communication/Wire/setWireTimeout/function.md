---
title: setWireTimeout()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Sets the timeout for Wire transmissions in master mode.

**Note:** these timeouts are almost always an indication of an
underlying problem, such as misbehaving devices, noise, insufficient
shielding, or other electrical problems. These timeouts will prevent
your sketch from locking up, but not solve these problems. In such
situations there will often (also) be data corruption which doesn’t
result in a timeout or other error and remains undetected. So when a
timeout happens, it is likely that some data previously read or written
is also corrupted. Additional measures might be needed to more reliably
detect such issues (e.g. checksums or reading back written values) and
recover from them (e.g. full system reset). This timeout and such
additional measures should be seen as a last line of defence, when
possible the underlying cause should be fixed instead.

**Syntax**

`Wire.setWireTimeout(timeout, reset_on_timeout)`

`Wire.setWireTimeout()`

**Parameters**

-   `timeout a timeout`: timeout in microseconds, if zero then timeout
    checking is disabled

-   `reset_on_timeout`: if true then Wire hardware will be automatically
    reset on timeout

When this function is called without parameters, a default timeout is
configured that should be sufficient to prevent lockups in a typical
single-master configuration.

**Returns**

None.

**Example Code**

\`\`\` \#include &lt;Wire.h&gt;

void setup() { Wire.begin(); // join i2c bus (address optional for
master) \#if defined(WIRE\_HAS\_TIMEOUT) Wire.setWireTimeout(3000 /\* us
**/, true /** reset\_on\_timeout \*/); \#endif }

byte x = 0;

void loop() { /\* First, send a command to the other device \*/
Wire.beginTransmission(8); // transmit to device \#8 Wire.write(123); //
send command byte error = Wire.endTransmission(); // run transaction if
(error) { Serial.println("Error occured when writing"); if (error == 5)
Serial.println("It was a timeout"); }

    delay(100);

    /* Then, read the result */
    #if defined(WIRE_HAS_TIMEOUT)
    Wire.clearWireTimeoutFlag();
    #endif
    byte len = Wire.requestFrom(8, 1); // request 1 byte from device #8
    if (len == 0) {
      Serial.println("Error occured when reading");
      #if defined(WIRE_HAS_TIMEOUT)
      if (Wire.getWireTimeoutFlag())
        Serial.println("It was a timeout");
      #endif
    }

      delay(100);
    }
    ```

**Notes and Warnings**

How this timeout is implemented might vary between different platforms,
but typically a timeout condition is triggered when waiting for (some
part of) the transaction to complete (e.g. waiting for the bus to become
available again, waiting for an ACK bit, or maybe waiting for the entire
transaction to be completed).

When such a timeout condition occurs, the transaction is aborted and
`endTransmission()` or `requestFrom()` will return an error code or zero
bytes respectively. While this will not resolve the bus problem by
itself (i.e. it does not remove a short-circuit), it will at least
prevent blocking potentially indefinitely and allow your software to
detect and maybe solve this condition.

If `reset_on_timeout` was set to true and the platform supports this,
the Wire hardware is also reset, which can help to clear any incorrect
state inside the Wire hardware module. For example, on the AVR platform,
this can be required to restart communications after a noise-induced
timeout.

When a timeout is triggered, a flag is set that can be queried with
`getWireTimeoutFlag()` and must be cleared manually using
`clearWireTimeoutFlag()` (and is also cleared when `setWireTimeout()` is
called).

Note that this timeout can also trigger while waiting for clock
stretching or waiting for a second master to complete its transaction.
So make sure to adapt the timeout to accomodate for those cases if
needed. A typical timeout would be 25ms (which is the maximum clock
stretching allowed by the SMBus protocol), but (much) shorter values
will usually also work.

**Portability Notes**

This function was not available in the original version of the Wire
library and might still not be available on all platforms. Code that
needs to be portable across platforms and versions can use the
`WIRE_HAS_TIMEOUT` macro, which is only defined when
`Wire.setWireTimeout()`, `Wire.getWireTimeoutFlag()` and
`Wire.clearWireTimeout()` are all available.

When this timeout feature was introduced on the AVR platform, it was
initially kept disabled by default for compatibility, expecting it to
become enabled at a later point. This means the default value of the
timeout can vary between (versions of) platforms. The default timeout
settings are available from the `WIRE_DEFAULT_TIMEOUT` and
`WIRE_DEFAULT_RESET_WITH_TIMEOUT` macro.

If you require the timeout to be disabled, it is recommended you disable
it by default using `setWireTimeout(0)`, even though that is currently
the default.

