---
title: 'Loops'
description: 'Learn how to use different loops with MicroPython.'
author: 'Pedro Lima'
tags: [MicroPython, Loops]
---

Loops are fundamental constructs in all programming languages, that allow you to execute a block of code multiple times. In MicroPython, loops help you perform repetitive tasks efficiently and are an awesome tool to keep in your coder's toolbox. 

In this guide, we will explore the different loop structures available.

## Requirements

Before we start, let's check the requirements:

### MicroPython Compatible Arduino Boards

MicroPython is officially supported on several Arduino boards. Here’s a list of the compatible boards:

- [Portenta C33](https://store.arduino.cc/products/portenta-c33)
- [Arduino GIGA R1 WiFi](https://store.arduino.cc/products/arduino-giga-r1-wifi)
- [Portenta H7](https://store.arduino.cc/products/portenta-h7)
- [Portenta H7 Lite](https://store.arduino.cc/products/portenta-h7-lite)
- [Portenta H7 Lite Connected](https://store.arduino.cc/products/portenta-h7-lite-connected)
- [Opta](https://store.arduino.cc/products/opta)
- [Opta Wifi](https://store.arduino.cc/products/opta-wifi)
- [Opta RS485](https://store.arduino.cc/products/opta-rs485)
- [Arduino Nano RP2040 Connect](https://store.arduino.cc/products/arduino-nano-rp2040-connect)
- [Nicla Vision](https://store.arduino.cc/products/nicla-vision)
- [Arduino Nano 33 BLE](https://store.arduino.cc/products/arduino-nano-33-ble)
- [Arduino Nano 33 BLE Rev2](https://store.arduino.cc/products/arduino-nano-33-ble-rev2)
- [Arduino Nano 33 BLE Sense](https://store.arduino.cc/products/arduino-nano-33-ble-sense)
- [Arduino Nano 33 BLE Sense Rev2](https://store.arduino.cc/products/arduino-nano-33-ble-sense-rev2)
- [Arduino Nano ESP32](https://store.arduino.cc/products/arduino-nano-esp32)

### Software Requirements

- [Arduino Lab for Micropython](https://labs.arduino.cc/en/labs/micropython) - Arduino Lab for MicroPython is an editor where we can create and run MicroPython scripts on our Arduino board.

***Note that the editor is also available online, at [Arduino Cloud - Arduino Labs for MicroPython](https://lab-micropython.arduino.cc/)***

## Board and Editor Setup

1. Open the [Arduino Lab for MicroPython]() application.
2. Plug the Arduino board into the computer using a USB cable.
    ![Connect board to computer.]()
3. Press the connection button on the top left corner of the window.
    ![Connect the editor to the board.]()
4. The connected Arduino board should appear, and we can click it:
    ![Select board.]()

***Need help installing MicroPython on your board? Visit the [MicroPython installation guide]().***

## Loop Structures in MicroPython

MicroPython supports two primary loop structures, each with a specific purpose:

- **`for` loops**: These loops iterate over a predefined sequence, such as a list, tuple, or string. The loop automatically retrieves each item in the sequence, one at a time, and performs actions until every item has been handled.

- **`while` loops**: These loops continue executing as long as a specified condition is true. Unlike `for` loops, which depend on a sequence, `while` loops rely on a conditional expression that determines when the loop should stop.

To better understand these loops, let’s imagine them as tasks at the supermarket:

- **`for` loops**: Imagine walking down a supermarket aisle with a shopping list that specifies exactly how many items to pick up, one by one, in order. Once you’ve gathered all the items on your list, your task is complete. This is like a `for` loop iterating over a sequence, handling each specified item one at a time.

![How for loops work.]()

- **`while` loops**: Imagine going to the supermarket to buy a certain product that’s on sale, as long as it stays in stock. You keep coming back, day after day, until the sale ends or the stock runs out. In a `while` loop, you keep “coming back” as long as a condition (like the sale continuing) remains true.

![How while loops work.]()

## For Loops

The `for` loop is used for iterating over a sequence. It automatically retrieves each item in the sequence one after another.

### Syntax

```python
for variable in sequence:
    # Code block to execute
```

- **`for`**: Keyword that starts the loop.
- **`variable`**: Takes the value of each item in the sequence during iteration this is where you will get the value for each iteration of a collection.
- **`in`**: Keyword used to specify the sequence to iterate over.
- **`sequence`**: The collection (like a list, tuple, or string) over which the loop iterates.
- **Code block**: The indented block of code that runs on each iteration.

### Example: Iterating Over "Arduino" with a `for` Loop

```python
import time

cycle = 1
for letter in "Arduino":
    print(f"{cycle} - {letter} - printed with for loop")
    cycle += 1
    time.sleep(3)
```

Let's take a look at what's included in this code example:

- `import time` - we import the `time` module to use the `sleep()` function for delays.
- **Initialize `cycle` Variable**: We start a `cycle` counter at 1.
- **`for letter in "Arduino"`**: The loop iterates over each character in the string `"Arduino"`, assigning each character to the variable `letter`.
- **Print Statement**: Outputs the cycle number, the current letter, and mentions that it's printed with a `for` loop.
- **Increment `cycle`**: Increases the cycle counter by 1 after each iteration.
- **`time.sleep(3)`**: Pauses the program for 3 seconds before the next iteration.



## Using a `while` Loop

A `while` loop continues to execute as long as a specified condition is true.

### Syntax of a `while` Loop

```python
while condition:
    # Code block to execute
```

- **`while`**: Keyword that starts the loop.
- **`condition`**: A boolean expression evaluated before each iteration; if `True`, the loop continues.
- **Code block**: The indented block of code that runs on each iteration.

### Example: Iterating Over "Arduino" with a `while` Loop

```python
import time

word = "Arduino"
index = 0
cycle = 1

while index < len(word):
    letter = word[index]
    print(f"{cycle} - {letter} - printed with while loop")
    index += 1
    cycle += 1
    time.sleep(3)
```

**Explanation:**

- **Initialize Variables**:
  - `word`: The string we're iterating over.
  - `index`: Starts at 0, used to access each character in `word`.
  - `cycle`: Counts the number of iterations.
- **`while index < len(word)`**: The loop continues as long as `index` is less than the length of `word`.
- **Retrieve Letter**: `letter = word[index]` gets the character at the current index.
- **Print Statement**: Outputs the cycle number, the current letter, and mentions that it's printed with a `while` loop.
- **Increment Counters**: Increases `index` and `cycle` by 1.
- **`time.sleep(3)`**: Pauses the program for 3 seconds before the next iteration.

## Control Statements

While inside a loop, we can control how it should behave using control statements: **continue** and **break**

### Continue

The `continue` statement can be used to skip past an iteration. For example, if we for some reason want to skip every fifth iteration, we could use the following code:

```python
for i in range(10)
    if i == 5:
        continue
    print(i)
```

Running this script will result in:

```python
0
1
2
3
4
6 # we skip the 5th iteration
7
8
9
10
```

### Break

The `break` statement can be used to break out of a loop before it finishes all iterations. This can be useful to for example cancel a process if something unexpected happens.

```python
for i in range(10)
    if i == 5:
        break
    print(i)
```

Running this script will result in:

```python
0
1
2
3
4
```

## Conclusion

Loops are essential for automating repetitive tasks in MicroPython. Understanding how to use different loop structures allows you to write more efficient and effective code. In these examples, we've demonstrated how to iterate over the string "Arduino" using various loop methods, printing each letter with a delay to observe the output in real time.

**Try Modifying the Examples**

- **Different Strings**: Replace `"Arduino"` with another word to see how the loops handle different sequences.
- **Additional Information**: Include more details in the print statement, such as the ASCII value of each letter.