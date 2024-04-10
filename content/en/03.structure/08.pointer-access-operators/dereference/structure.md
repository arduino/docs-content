---
title: "* (dereference operator)"
categories: "Structure"
subCategories: "Pointer Access Operators"
---

**Description**

Dereferencing is one of the features specifically for use with pointers.
The asterisk operator `*` is used for this purpose. If `p` is a pointer,
then `*p` represents the value contained in the address pointed by `p`.

**Example Code**

    int *p;       // declare a pointer to an int data type
    int i = 5;
    int result = 0;
    p = &i;       // now 'p' contains the address of 'i'
    result = *p;  // 'result' gets the value at the address pointed by 'p'
                  // i.e., it gets the value of 'i' which is 5

**Notes and Warnings**

Pointers are one of the complicated subjects for beginners in learning
C, and it is possible to write the vast majority of Arduino sketches
without ever encountering pointers. However for manipulating certain
data structures, the use of pointers can simplify the code, and
knowledge of manipulating pointers is handy to have in one’s toolkit.

**See also**

-   DEFINITION
    [Pointers^](https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29)

