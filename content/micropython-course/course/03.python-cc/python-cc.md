---
author: 'Karl Söderby'
hero_image: "./hero-banner.png"
featured: micropython-101
title: 'Python Crash Course'
description: 'Learn some Python fundamentals that will help you create MicroPython scripts.'
---

We ended last chapter by making **a light blink**, to make sure our setup was working properly. In this chapter, we will take you through some useful Python syntax that will be of help when you are creating MicroPython scripts.

***In this chapter we will cover a small part of the Python programming language. This will help you to better understand the rest of the course. If you are familiar with Python, this chapter is not a requirement.***

## Overview

This chapter introduces a number of Python syntax that will prove very useful throughout this course. The intention of this chapter is for you to get familiar with Python, so that the MicroPython examples in this course will be easier to understand.

Many of the examples presented in this chapter are just fragments. Try to combine different elements to test your Python skills!

### Learn Python

While this chapter provides some fundamental Python syntax, it does not cover all. If you are interested in learning more about Python, we recommend you checking out some of the links below:
- [learnpython.org](https://www.learnpython.org/)
- [W3Schools](https://www.w3schools.com/python/default.asp)

## Variables

Let's get to it! The very first thing to learn in Python is how to create a variable. Using Python, you do not need to name the data type, that is automatically handled.

```python
stringVar = 'This is a String' # string
numVar = 250 # numeric value
arrayVar = [1,3,6,7] # array
```

A variable can store just about anything, but pay attention to *how* they are stored. For example, a string (which holds characters, or text), needs the quotation marks, while a number does not need anything.

## Print

The `print()` function is the best way of knowing what's happening on your board. You can use `print()` to print the numeric value of a variable, the state of a button, or to send a message back to the computer.

```python
print('Hello') # print a string
print(4) # print a number
print(data) # print value of variable 
print(5+2) # prints 7
print(func()) # prints the return value of a function
print('Value: ', data) # prints "Value: <value of data variable>"
```

As you can see, there are many different approaches on how to print things to the terminal.

***The `print()` function is one of the most commonly used functions. When programming your board, this function allows you to see what happens on the board in real time.***

## Operators

Operators in Python are used to for example add two numbers together, assign a value to a variable or compare two values with each other, and are fundamental in Python programming.

To perform an **arithmetic** operation (addition, subtraction, division etc.), you can write it like:

```python
print(5+5) # value is 10
print(10-5) # value is 5
```

Operators can also be used to **assign** values to variables. For example:

```python
paragraph = "This is a sentence" 
x = 10
print(x) # prints 10
print(paragraph) # this prints "this is a sentence"
```

**Comparison** operators can be used to compare two values inside of a *statement*: 

```python
if 10 > 5:
    print("10 is indeed greater than 5")
```

If you want to compare multiple values, the **logic** operators can be used:

```python
if x > 10 and x < 15:
    print("x is larger than 10 but smaller than 15")
```

## If/Elif/Else Statements

In the example just above, we started using conditional statements. These statements are fundamental in programming as they allow us to create code that executes only under specific conditions. 

Below you can see how we can process the variable `x`. Three possible outcomes are available, which simply checks what number `x` is.

```python
x = 5+5

if x > 10:
    print("x is larger than 10")
elif x == 10:
    print("x is exactly 10") #this will print, since x is 10
else:
    print("x is smaller than 10")
```

Now take a look at what happens after each statement. Notice the empty space just before `print()`? This is called an *indentation*, and is how Python organises code.

Anything inside of this indentation will execute if the statement is met, and this is a fundamental principle that is used in every Python program that you write!

Now since we already defined `x` to be `5+5`, the terminal will of course print:
- `"x is larger than 10"` 

## While Loop

Now that we are a bit more familiar with statements, let's take a look at the `while` loop, which is designed to execute code *while* a condition is met.  

```python
x = 5

while(x == 5):
    # this code block will execute
    # over and over until x is not 5

while(x != 5):
    # this code block will execute
    # if x is anything else (!=) than 5 
```

The above example allows you to set up two different loops depending on what the value of `x` is.

For our Nano ESP32, this can be particularly useful, because we often want to repeat the code that we create, over and over again.

A method that can be used to loop something over and over again is:

```python
while(True):
    # this code block will execute forever
    # or until we stop the script
```

Now why is it useful to place the Nano ESP32 in a constant loop? Well, if we want to use the board in the real world, as maybe a sensor, an actuator or even both, we want to continuously be able to update certain values.

If we have a temperature sensor and a display, we would ideally see the temperature update on the display, maybe every second or so. To achieve this, we need to place the board in a loop that continuously checks the temperature. 

```python
while(True):
    # A value is read from the sensor
    sensor_value = sensor.read()
    # Sensor data is printed on a display
    display.print(sensor_value)
    # This happens every one second
    time.sleep(1)
    # And after this line, we will go back to the
    # start of the loop!
```

## For Loop

The for loop works similarly to the `while` loop, but it will not continue to loop once it has completed its instructions.

In the example below, we go through a list of numbers, and print them out, one by one.

```python
numbers = [1,2,3,4,5]
for x in numbers:
  print(x)
```

Once it reaches the end, it will stop executing.

We can also create a for loop that will execute some code for a specific number of times. For this, we will add the `range()` function:

```python
for x in range(0, 5):
  print(x)
```

## Functions

A function can store a block of code that can later be executed from within a script. It is useful when performing a computation, for example when adding two numbers together.

To create a function, use the `def` syntax, followed by a name of your choosing:

```python
def my_function():
    print("This line was executed inside a function!")

my_function()
```

We can also pass a value to the function, which can process it and return a value:

```python
def my_function(x,y):
    return x + y

value = my_function(5,5)
print(value)
```

The above function *returns* a value of `10`, because we fed `5`,`5` into it. The function simply adds it together, and returns the value to you.

## Summary

In this Python crash course, we've covered some of the very fundamental aspects of the Python programming language. 

In this course, we are focused on MicroPython, which is a micro-implementation of the language. This means that most core functionalites of the language is available, such as **operators, statements, loops & functions.**

- [Next Chapter: Digital Signals](/micropython-course/course/digital)