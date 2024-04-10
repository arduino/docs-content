---
title: isSpace()
categories: "Functions"
subCategories: "Characters"
---

**Description**

Analyse if a char is a white-space character. Returns true if the
argument is a space, form feed (`'\f'`), newline (`'\n'`), carriage
return (`'\r'`), horizontal tab (`'\t'`), or vertical tab (`'\v'`).

**Syntax**

`isSpace(thisChar)`

**Parameters**

`thisChar`: variable. Allowed data types: `char`.

**Returns**

`true`: if thisChar is a white-space character.

**Example Code**

    if (isSpace(myChar)) {  // tests if myChar is a white-space character
      Serial.println("The character is white-space");
    }
    else {
      Serial.println("The character is not white-space");
    }

**See also**

-   LANGUAGE [char](../../../variables/data-types/char)

-   LANGUAGE [if (conditional
    operators)](../../../structure/control-structure/if)

-   LANGUAGE [while (conditional
    operators)](../../../structure/control-structure/while)

-   LANGUAGE [read()](../../communication/serial/read)

