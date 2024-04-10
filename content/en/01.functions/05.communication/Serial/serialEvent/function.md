---
title: serialEvent
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Called at the end of [`loop()`](../../../../structure/sketch/loop) when
data is available. Use `Serial.read()` to capture this data.

**Please note:** most modern boards do not support this method. See
"Notes and Warnings" further below this article.

**Syntax**

    void serialEvent() {
      //statements
    }

The Mega 2560 R3 and Due boards have additional serial ports which can
be accessed by adding the corresponding number at the end of the
function.

    void serialEvent1() {
      //statements
    }

    void serialEvent2() {
      //statements
    }

    void serialEvent3() {
      //statements
    }

**Parameters**

`statements`: any valid statements

**Returns**

Nothing

**Notes and Warnings**

Please note that `serialEvent()` **does not work** on any modern Arduino
boards. The only recognized boards to have support as of 2023/12/06 are
the **UNO R3**, **Nano**, **Mega 2560 R3** and **Due**.

Instead, you can use the [`available()`](../available) method. Examples
in this page demonstrates how to read serial data only when it is
available, similarly to how `Serial.event()` is implemented.

**See also**

-   EXAMPLE [Serial Event^](http://arduino.cc/en/Tutorial/SerialEvent)

-   LANGUAGE [begin()](../begin)

-   LANGUAGE [end()](../end)

-   LANGUAGE [available()](../available)

-   LANGUAGE [read()](../read)

-   LANGUAGE [peek()](../peek)

-   LANGUAGE [flush()](../flush)

-   LANGUAGE [print()](../print)

-   LANGUAGE [println()](../println)

-   LANGUAGE [write()](../write)

