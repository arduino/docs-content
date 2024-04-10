---
title: isLowerCase()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is lower case (that is a letter in lower case).
Returns true if thisChar contains a letter in lower case.

**Syntax**

`isLowerCase(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is lower case.

**Example Code**

    if (isLowerCase(myChar)) {  // tests if myChar is a lower case letter
      Serial.println("The character is lower case");
    }
    else {
      Serial.println("The character is not lower case");
    }

**See also**

-   LANGUAGE [char](../../../variables/data-types/char)

-   LANGUAGE [if (conditional
    operators)](../../../structure/control-structure/if)

-   LANGUAGE [while (conditional
    operators)](../../../structure/control-structure/while)

-   LANGUAGE [read()](../../communication/serial/read)
