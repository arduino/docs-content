---
title: isPunct()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is punctuation (that is a comma, a semicolon, an
exclamation mark and so on). Returns true if thisChar is punctuation.

**Syntax**

`isPunct(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is a punctuation.

**Example Code**

    if (isPunct(myChar)) {  // tests if myChar is a punctuation character
      Serial.println("The character is a punctuation");
    }
    else {
      Serial.println("The character is not a punctuation");
    }

**See also**

-   LANGUAGE [char](../../../variables/data-types/char)

-   LANGUAGE [if (conditional
    operators)](../../../structure/control-structure/if)

-   LANGUAGE [while (conditional
    operators)](../../../structure/control-structure/while)

-   LANGUAGE [read()](../../communication/serial/read)

