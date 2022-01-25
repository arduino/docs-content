---
title: 'Curie Timer One Library'
description: 'This library allows to use Timer functions on Arduino and Genuino 101 boards.'
author: Arduino
---

## Overview

***This library is included in the [Arc32 core](https://github.com/arduino/ArduinoCore-arc32/tree/master/libraries). This core can be installed through the Arduino IDEs , where the package is named "Intel Curie Boards".*** 

This library allows to use Timer functions on Arduino and Genuino 101 boards. With this library you can add and manage events based on timer functions. The timer is set up with a number of microseconds and every time this number is reached, a counter is incremented and an interrupt, if set, is asserted. This means that you may program recurring interrupts setting up their frequency. This library supports also PWM signal generation with 1024 steps of resolution and a period that can be set up in microseconds.

To use this library:

```
#include <CurieTimerOne.h>
```

## Examples

- [Curie Timer One Interrupt](https://www.arduino.cc/en/Tutorial/CurieTimer1Interrupt): Set up a timer and assert an interrupt.
- [Curie Timer One PWM](https://www.arduino.cc/en/Tutorial/CurieTimer1PWM): Generate a PWM signal on a digital pin with full control over the parameters.


## Functions

---

### `start()`
#### Description
Starts the timer function, sets the interval at which the timer ticks and also sets the interrupt callback function.

#### Syntax
```
CurieTimerOne.start(int timerPeriodUsec, userCallBack)
```
#### Parameters
timerPeriodUsec: the number of microseconds that are the period of time at which the timer ticks and generates an interrupt

userCallBack: the function that is called when an interrupt is asserted

#### Returns
none

---

### `restart()`
#### Description
Restarts the timer function, sets the counter to zeroand sets the interval at which the timer ticks.

#### Syntax
```
CurieTimerOne.restart(int timerPeriodUsec)
```
#### Parameters
timerPeriodUsec: the number of microseconds that are the period of time at which the timer ticks and generates an interrupt

#### Returns
none

---

### `kill()`
#### Description
Disables the timer and puts it back in the power up default state

#### Syntax
```
CurieTimerOne.kill()
```
#### Parameters
none

#### Returns
none

---

### `attachInterrupt()`
#### Description
Attaches the interrupt to the call back function

#### Syntax
```
CurieTimerOne.attachInterrupt(userCallBack)
```
#### Parameters
userCallBack: the function that is called when an interrupt is asserted

#### Returns
none

---

### `detachInterrupt()`
#### Description
Detaches the interrupt from the call back function; this doesn't disable the interrupt, it just inhibit the call of the call back function. the interrupt count is still increased at each interrupt.

#### Syntax
```
CurieTimerOne.detachInterrupt()
```
#### Parameters
none

#### Returns
none

---

### `readTickCount()`
#### Description
Returns the count of the interrupts asserted since the timer activation or the last reset.

#### Syntax
```
CurieTimerOne.readTickCount()
```
#### Parameters
none

#### Returns
an integer containing the number of interrupts counted since the last start/reset.

---

### `rdRstTickCount()`
#### Description
Reads and resets the number of timer interrupts counted so far.

#### Syntax
```
CurieTimerOne.rdRstTickCount()
```
#### Parameters
none

#### Returns
The number of interrupts generated since the start or the last reset.

---

### `pause()`
#### Description
Pauses the timer suspending the interrupt generation. While the timer is paused, the count does not increase and no interrupt is asserted.

#### Syntax
```
CurieTimerOne.pause()
```
#### Parameters
none

#### Returns
none

---

### `resume()`
#### Description
Resumes the timer restarting from where it was left after a pause() .

#### Syntax
```
CurieTimerOne.resume()
```
#### Parameters
none

#### Returns
none

---

### `pwmStart()`
#### Description
This function generates a PWM signal on any digital pin with frequency and duty cycle specified as arguments. The timer is consumed once PWM is set, stopping any interrupt generation that was set up as timer.

#### Syntax
```
CurieTimerOne.pwmStart(int outputPin, int dutyRange, unsigned int periodUsec)
or
CurieTimerOne.pwmStart(int outputPin, double dutyPercentage, unsigned int periodUsec)
```
#### Parameters
outputPin: is the digital pin on which we want to generate the pwm signal.

dutyRange: is the value expressed as an integer from 0 to 1023, where a 50% duty cycle is 512 and 255 equals 24.9% of duty cycle.

dutyPercentage: is the value expressed as a floating point percentage. This function manages only one decimal position.

periodUsec: is the length of the PWM waveform period, expressed in microseconds. To convert this value to hertz, use this formula:
Hz=(periodUsec/1000000)

#### Returns
none

---

### `pwmStop()`
#### Description
This function ends the software generation of PWM. Puts the timer back to default, de-asserts the selected port and sets its level to LOW.

#### Syntax
```
CurieTimerOne.pwmStop()
```
#### Parameters
none
#### Returns
none