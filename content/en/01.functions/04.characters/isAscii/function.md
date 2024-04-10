---
title: isAscii()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is Ascii. Returns true if thisChar contains an Ascii
character.

**Syntax**

`isAscii(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is Ascii.

**Example Code**

    if (isAscii(myChar)) {  // tests if myChar is an Ascii character
      Serial.println("The character is Ascii");
    }
    else {
      Serial.println("The character is not Ascii");
    }

**See also**

-   LANGUAGE [char](../../../variables/data-types/char)

-   LANGUAGE [if (conditional
    operators)](../../../structure/control-structure/if)

-   LANGUAGE [while (conditional
    operators)](../../../structure/control-structure/while)

-   LANGUAGE [read()](../../communication/serial/read)

