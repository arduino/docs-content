---
title: isAlphaNumeric()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is alphanumeric (that is a letter or a numbers).
Returns true if thisChar contains either a number or a letter.

**Syntax**

`isAlphaNumeric(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is alphanumeric.

**Example Code**

    if (isAlphaNumeric(myChar)) { // tests if myChar isa letter or a number
      Serial.println("The character is alphanumeric");
    }
    else {
      Serial.println("The character is not alphanumeric");
    }

**See also**

-   LANGUAGE [char](../../../variables/data-types/char)

-   LANGUAGE [if (conditional
    operators)](../../../structure/control-structure/if)

-   LANGUAGE [while (conditional
    operators)](../../../structure/control-structure/while)

-   LANGUAGE [read()](../../communication/serial/read)
