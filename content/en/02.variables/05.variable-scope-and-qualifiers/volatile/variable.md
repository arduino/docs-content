---
title: volatile
categories: "Variables"
subCategories: "Variable Scope & Qualifiers"
---

**Description**

`volatile` is a keyword known as a variable *qualifier*, it is usually
used before the datatype of a variable, to modify the way in which the
compiler and subsequent program treat the variable.

Declaring a variable `volatile` is a directive to the compiler. The
compiler is software which translates your C/C++ code into the machine
code, which are the real instructions for the Atmega chip in the
Arduino.

Specifically, it directs the compiler to load the variable from RAM and
not from a storage register, which is a temporary memory location where
program variables are stored and manipulated. Under certain conditions,
the value for a variable stored in registers can be inaccurate.

A variable should be declared `volatile` whenever its value can be
changed by something beyond the control of the code section in which it
appears, such as a concurrently executing thread. In the Arduino, the
only place that this is likely to occur is in sections of code
associated with interrupts, called an interrupt service routine.

**int or long volatiles**

If the `volatile` variable is bigger than a byte (e.g. a 16 bit int or a
32 bit long), then the microcontroller can not read it in one step,
because it is an 8 bit microcontroller. This means that while your main
code section (e.g. your loop) reads the first 8 bits of the variable,
the interrupt might already change the second 8 bits. This will produce
random values for the variable.

Remedy:

While the variable is read, interrupts need to be disabled, so they
can’t mess with the bits, while they are read. There are several ways to
do this:

1.  LANGUAGE [noInterrupts](../../../functions/interrupts/nointerrupts)

2.  use the ATOMIC\_BLOCK macro. Atomic operations are single MCU
    operations - the smallest possible unit.

**Example Code**

The `volatile` modifier ensures that changes to the `changed` variable
are immediately visible in `loop()`. Without the `volatile` modifier,
the `changed` variable may be loaded into a register when entering the
function and would not be updated anymore until the function ends.

    // Flashes the LED for 1 s if the input has changed
    // in the previous second.

    volatile byte changed = 0;

    void setup() {
      pinMode(LED_BUILTIN, OUTPUT);
      attachInterrupt(digitalPinToInterrupt(2), toggle, CHANGE);
    }

    void loop() {
      if (changed == 1) {
        // toggle() has been called from interrupts!

        // Reset changed to 0
        changed = 0;

        // Blink LED for 200 ms
        digitalWrite(LED_BUILTIN, HIGH);
        delay(200);
        digitalWrite(LED_BUILTIN, LOW);
      }
    }

    void toggle() {
      changed = 1;
    }

To access a variable with size greater than the microcontroller’s 8-bit
data bus, use the `ATOMIC_BLOCK` macro. The macro ensures that the
variable is read in an atomic operation, i.e. its contents cannot be
altered while it is being read.

    #include <util/atomic.h> // this library includes the ATOMIC_BLOCK macro.
    volatile int input_from_interrupt;

    // Somewhere in the code, e.g. inside loop()
      ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
        // code with interrupts blocked (consecutive atomic operations will not get interrupted)
        int result = input_from_interrupt;
      }

**See also**

-   LANGUAGE
    [attachInterrupt](../../../functions/external-interrupts/attachinterrupt)

