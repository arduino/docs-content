---
title: noTone()
categories: "Functions"
subCategories: "Advanced I/O"
---

# Description

Stops the generation of a square wave triggered by `tone()`. Has no
effect if no tone is being generated.

# Syntax

`noTone(pin)`

# Parameters

`pin`: the Arduino pin on which to stop generating the tone

# Returns

Nothing

# Notes and Warnings

If you want to play different pitches on multiple pins, you need to call
`noTone()` on one pin before calling `tone()` on the next pin.

# See also

