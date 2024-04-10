---
title: Stream.parseInt()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`parseInt()` returns the first valid (long) integer number from the
current position.

In particular:

-   Parsing stops when no characters have been read for a configurable
    time-out value, or a non-digit is read;

-   If no valid digits were read when the time-out (see
    [Stream.setTimeout()](../streamsettimeout)) occurs, 0 is returned;

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.parseInt()`
`stream.parseInt(lookahead)`
`stream.parseInt(lookahead, ignore)`

**Parameters**

`stream` : an instance of a class that inherits from Stream.
`lookahead`: the mode used to look ahead in the stream for an integer.
Allowed data types: `LookaheadMode`. Allowed `lookahead` values:

-   `SKIP_ALL`: all characters other than digits or a minus sign are
    ignored when scanning the stream for an integer. This is the default
    mode.

-   `SKIP_NONE`: Nothing is skipped, and the stream is not touched
    unless the first waiting character is valid.

-   `SKIP_WHITESPACE`: Only tabs, spaces, line feeds, and carriage
    returns are skipped.

`ignore`: used to skip the indicated char in the search. Used for
example to skip thousands divider. Allowed data types: `char`

**Returns**

Data type: `long`.

