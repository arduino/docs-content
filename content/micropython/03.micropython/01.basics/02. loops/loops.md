---

featured: micropython-101
title: '3. Micropython Basics - Loops'
description: 'Learn the basics for loops on MicroPython.'
author: 'Pedro Lima'
hero_image: "./hero-banner.png"

---

Loops are fundamental constructs in programming that allow you to execute a block of code multiple times. In MicroPython, loops help you perform repetitive tasks efficiently and are an awesome tool to keep in your coder's toolbox. In this article, we will explore the different loop structures available.

## Loop Structures in MicroPython

MicroPython supports two primary loop structures:

- **`for` loops**: Iterate over a sequence (like a list, tuple, or string).
- **`while` loops**: Continue executing as long as a condition is true.

Let's delve into each of these with examples.



## Using a `for` Loop

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

**Explanation:**

- **Import `time` Module**: We import the `time` module to use the `sleep()` function for delays.
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





## Conclusion

Loops are essential for automating repetitive tasks in MicroPython. Understanding how to use different loop structures allows you to write more efficient and effective code. In these examples, we've demonstrated how to iterate over the string "Arduino" using various loop methods, printing each letter with a delay to observe the output in real time.

**Try Modifying the Examples**

- **Different Strings**: Replace `"Arduino"` with another word to see how the loops handle different sequences.
- **Additional Information**: Include more details in the print statement, such as the ASCII value of each letter.