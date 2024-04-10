---
title: isPrintable()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is printable (that is any character that produces an
output, even a blank space). Returns true if thisChar is printable.

**Syntax**

`isPrintable(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is printable.

**Example Code**

    if (isPrintable(myChar)) {  // tests if myChar is printable char
      Serial.println("The character is printable");
    }
    else {
      Serial.println("The character is not printable");
    }

**See also**

-   LANGUAGE [char](../../../variables/data-types/char)

-   LANGUAGE [if (conditional
    operators)](../../../structure/control-structure/if)

-   LANGUAGE [while (conditional
    operators)](../../../structure/control-structure/while)

-   LANGUAGE [read()](../../communication/serial/read)
