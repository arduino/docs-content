---
title: tone()
categories: "Functions"
subCategories: "Advanced I/O"
---

**Description**

Generates a square wave of the specified frequency (and 50% duty cycle)
on a pin. A duration can be specified, otherwise the wave continues
until a call to [noTone()](../notone). The pin can be connected to a
piezo buzzer or other speaker to play tones.

Only one tone can be generated at a time. If a tone is already playing
on a different pin, the call to `tone()` will have no effect. If the
tone is playing on the same pin, the call will set its frequency.

Use of the `tone()` function will interfere with PWM output on pins 3
and 11 (on boards other than the Mega).

It is not possible to generate tones lower than 31Hz. For technical
details, see [Brett Hagman’s
notes](https://github.com/bhagman/Tone#ugly-details).

**Syntax**

`tone(pin, frequency)`
`tone(pin, frequency, duration)`

**Parameters**

`pin`: the Arduino pin on which to generate the tone.
`frequency`: the frequency of the tone in hertz. Allowed data types:
`unsigned int`.
`duration`: the duration of the tone in milliseconds (optional). Allowed
data types: `unsigned long`.

**Returns**

Nothing

**Notes and Warnings**

- If you want to play different pitches on multiple pins, you need to
  call `noTone()` on one pin before calling `tone()` on the next pin.

- This function is non-blocking, which means that even if you provide
  the `duration` parameter the sketch execution will continue
  immediately even if the tone hasn’t finished playing.

**See also**

- LANGUAGE [analogWrite()](../../analog-io/analogwrite)

- EXAMPLE [Tone
  Melody^](https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneMelody)

- EXAMPLE [Pitch
  Follower^](https://www.arduino.cc/en/Tutorial/tonePitchFollower)

- EXAMPLE [Tone
  Keyboard^](https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneKeyboard)

- EXAMPLE [Tone
  Multiple^](https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneMultiple)

- EXAMPLE [PWM^](https://www.arduino.cc/en/Tutorial/PWM)
