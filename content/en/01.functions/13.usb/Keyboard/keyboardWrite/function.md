---
title: Keyboard.write()
categories: "Functions"
subCategories: "USB"
leaf: true
---

**Description**

Sends a keystroke to a connected computer. This is similar to pressing
and releasing a key on your keyboard. You can send some ASCII characters
or the additional [keyboard modifiers and special
keys](../keyboardmodifiers).

Only ASCII characters that are on the keyboard are supported. For
example, ASCII 8 (backspace) would work, but ASCII 25 (Substitution)
would not. When sending capital letters, `Keyboard.write()` sends a
shift command plus the desired character, just as if typing on a
keyboard. If sending a numeric type, it sends it as an ASCII character
(ex. Keyboard.write(97) will send *a*).

For a complete list of ASCII characters, see
[ASCIITable.com](http://www.asciitable.com/).

**Syntax**

`Keyboard.write(character)`

**Parameters**

`character`: a char or int to be sent to the computer. Can be sent in
any notation that’s acceptable for a char. For example, all of the below
are acceptable and send the same value, 65 or ASCII A:

    Keyboard.write(65);         // sends ASCII value 65, or A
    Keyboard.write('A');            // same thing as a quoted character
    Keyboard.write(0x41);       // same thing in hexadecimal
    Keyboard.write(0b01000001); // same thing in binary (weird choice, but it works)

**Returns**

Number of bytes sent. Data type: `size_t`.

**Example Code**

    #include <Keyboard.h>

    void setup() {
      // make pin 2 an input and turn on the
      // pullup resistor so it goes high unless
      // connected to ground:
      pinMode(2, INPUT_PULLUP);
      Keyboard.begin();
    }

    void loop() {
      //if the button is pressed
      if (digitalRead(2) == LOW) {
        //Send an ASCII 'A',
        Keyboard.write(65);
      }
    }

**Notes and Warnings**

When you use the Keyboard.write() command, the Arduino takes over your
keyboard! Make sure you have control before you use the command. A
pushbutton to toggle the keyboard control state is effective.

