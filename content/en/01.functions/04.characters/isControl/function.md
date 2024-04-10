---
title: isControl()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is a control character. Returns true if thisChar is a
control character.

**Syntax**

`isControl(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is a control character.

**Example Code**

    if (isControl(myChar)) {  // tests if myChar is a control character
      Serial.println("The character is a control character");
    }
    else {
      Serial.println("The character is not a control character");
    }

**See also**

-   LANGUAGE [char](../../../variables/data-types/char)

-   LANGUAGE [if (conditional
    operators)](../../../structure/control-structure/if)

-   LANGUAGE [while (conditional
    operators)](../../../structure/control-structure/while)

-   LANGUAGE [read()](../../communication/serial/read)

