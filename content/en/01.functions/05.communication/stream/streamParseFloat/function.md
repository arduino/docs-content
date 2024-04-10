---
title: Stream.parseFloat()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`parseFloat()` returns the first valid floating point number from the
current position. `parseFloat()` is terminated by the first character
that is not a floating point number. The function terminates if it times
out (see [Stream.setTimeout()](../streamsettimeout)).

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.parseFloat()`
`stream.parseFloat(lookahead)`
`stream.parseFloat(lookahead, ignore)`

**Parameters**

`stream` : an instance of a class that inherits from Stream.
`lookahead`: the mode used to look ahead in the stream for a floating
point number. Allowed data types: `LookaheadMode`. Allowed `lookahead`
values:

-   `SKIP_ALL`: all characters other than a minus sign, decimal point,
    or digits are ignored when scanning the stream for a floating point
    number. This is the default mode.

-   `SKIP_NONE`: Nothing is skipped, and the stream is not touched
    unless the first waiting character is valid.

-   `SKIP_WHITESPACE`: Only tabs, spaces, line feeds, and carriage
    returns are skipped.

`ignore`: used to skip the indicated char in the search. Used for
example to skip thousands divider. Allowed data types: `char`

**Returns**

Data type: `float`.
