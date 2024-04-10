---
title: continue
categories: "Structure"
subCategories: "Control Structure"
---

**Description**

The `continue` statement skips the rest of the current iteration of a
loop (`link:../for[for]`, `link:../while[while]`, or
`link:../dowhile[do...while]`). It continues by checking the conditional
expression of the loop, and proceeding with any subsequent iterations.

**Example Code**

The following code writes the value of 0 to 255 to the `PWMpin`, but
skips the values in the range of 41 to 119.

    for (int x = 0; x <= 255; x ++) {
      if (x > 40 && x < 120) {  // create jump in values
        continue;
      }

      analogWrite(PWMpin, x);
      delay(50);
    }

**See also**
