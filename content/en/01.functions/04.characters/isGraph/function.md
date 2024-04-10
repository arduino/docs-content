---
title: isGraph()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is printable with some content (space is printable but
has no content). Returns true if thisChar is printable.

**Syntax**

`isGraph(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is printable.

**Example Code**

    if (isGraph(myChar)) {  // tests if myChar is a printable character but not a blank space.
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

