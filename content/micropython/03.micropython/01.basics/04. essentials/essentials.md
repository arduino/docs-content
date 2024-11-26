---
title: 'Essentials'
description: 'A guide to digital inputs and outputs using MicroPython.'
author: 'Pedro Lima'
tags: [MicroPython, Basics, Essentials]
---

To make the most of all the tools available in your "Python" belt (thankfully, pythons are non-venomous!), understanding MicroPython's fundamental concepts is essential. This guide focuses on the language basics, covering variable types, lists, tuples, functions, and exception handling to help you build efficient and powerful programs.

## Variables and Data Types

Variables in MicroPython don’t need explicit type declarations. The type is inferred based on the assigned value.

### Example:

```python
# Different data types
integer_var = 42            # Integer
float_var = 3.14            # Float
string_var = "Hello!"       # String
boolean_var = True          # Boolean

# Print variable types
print(type(integer_var))  # Output: <class 'int'>
print(type(float_var))    # Output: <class 'float'>
print(type(string_var))   # Output: <class 'str'>
print(type(boolean_var))  # Output: <class 'bool'>
```

## Lists

Lists are a versatile way to store collections of items in MicroPython. They can hold any combination of data types and are mutable, meaning you can modify them after creation.

### Creating Lists

To create a list, we need to define a variable, followed by square brackets `[]`. The content of the list is separated by a comma (`,`).

```python
my_list = [1, 2, 3, "Four", True]
print(my_list)  # Output: [1, 2, 3, 'Four', True]
```

### Accessing Elements

Lists are zero-indexed, meaning the first element is at index `0`.

```python
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: Four
```

### Modifying Lists

We can modify an element inside a list by assigning it a new value.

```python
my_list[1] = 20
print(my_list)  # Output: [1, 20, 3, 'Four', True]
```

### Common List Methods

```python
my_list.append("New Item")  # Add an item
print(my_list)              # Output: [1, 20, 3, 'Four', True, 'New Item']

my_list.pop(2)              # Remove item at index 2
print(my_list)              # Output: [1, 20, 'Four', True, 'New Item']
```



## Tuples

Tuples are similar to lists but **immutable**, meaning their values cannot be changed after they are created. They are useful for representing fixed collections of items.

### Creating Tuples

```python
my_tuple = (1, 2, 3, "Four", True)
print(my_tuple)  # Output: (1, 2, 3, 'Four', True)
```

### Accessing Elements:

Like lists, tuples are zero-indexed.

```python
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: Four
```

### Why Use Tuples?

- **Efficiency**: Tuples consume less memory than lists.
- **Safety**: Their immutability prevents accidental changes to the data.

### Common Tuple Methods:

Tuples are limited compared to lists but have a few useful methods:

```python
my_tuple = (1, 2, 3, 2, 4)

print(my_tuple.count(2))  # Output: 2 (number of times 2 appears)
print(my_tuple.index(3))  # Output: 2 (index of the first occurrence of 3)
```

## Functions

Functions allow you to encapsulate reusable blocks of code, making your programs more modular and readable.

To define a function, we use `def` followed by the name of the function and parameters. In this case, let's define a function named `greet()`, which has the parameter `name`.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Then, we can call the function, and insert a name.

```python
greet("Karl")  # Output: Hello, Karl!
greet("Alex")    # Output: Hello, Alex!
```

The result will be: 

```cmd
Hello Karl!
Hello Alex!
```

### Returning Values

A function can also accept numbers, and compute them for you. In this case, we want to find out the **square number** of a number (a number multiplied by itself).

Inside the function we use `number * number` to get the value, and `return` to return the value to where it is called.

```python
def square(number):
    return number * number

result = square(4)
print(result)  # Output: 16
```

### Default Arguments

If you have function with parameters, you can set a **default** value, so that if we call the function without a parameter, we get a default value returned.

In this case, we set the default to be `"World"`.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, World!
greet("Karl")   # Output: Hello, Karl!
```

## Objects

Objects are a cornerstone of Python, and MicroPython fully supports object-oriented programming (OOP). An object is an instance of a **class**, and it can have **properties (attributes)** and **behaviors (methods)**. Let’s break these concepts down:

- **Class**: A blueprint or template for creating objects. It defines the structure (attributes) and behavior (methods) that the objects will have. Think of a class as the recipe for making objects.
- **Attributes**: Variables that store data specific to an object. These are the properties or characteristics of the object, like a dog’s name or breed.
- **Methods**: Functions defined inside a class that operate on the object’s attributes or perform specific actions. These represent the behavior of the object, like a dog barking.

Here’s how these concepts come together:

### Defining a Class

Use the `class` keyword to define a class. Inside the class, we can define attributes and methods.

```python
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name      # Attribute: name
        self.breed = breed    # Attribute: breed

    # Method: A behavior of the dog
    def bark(self):
        print(f"{self.name} says: Woof!")
```

### Creating an Object

An object is an instance of the class. It represents a specific entity created from the class blueprint.

```python
# Create an object of the Dog class
my_dog = Dog("Denver", "Golden Retriever")

# Access attributes
print(my_dog.name)   # Output: Denver
print(my_dog.breed)  # Output: Golden Retriever

# Call a method
my_dog.bark()        # Output: Buddy says: Woof!
```

In this example:
1. The `Dog` class is the blueprint.
2. `name` and `breed` are attributes (properties of the dog).
3. `bark()` is a method (a behavior of the dog).


## Exception Handling

In MicroPython, exceptions are a powerful way to deal with errors gracefully, ensuring your program doesn’t crash unexpectedly. By catching and handling exceptions, you can recover or retry alternative solutions.

Exceptions use logic we are already familiar with, just in a slightly different format, and contribute to making more foolproof code.

### Basic Structure

Exceptions follow a simple structure using `try`, `except`, and optionally `finally` blocks:

```python
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType:
    # Code to handle the exception
finally:
    # Code that runs no matter what (optional)
```

### Common Exceptions

- **`ZeroDivisionError`**: Raised when dividing by zero.
- **`ValueError`**: Raised when a function receives an invalid argument.
- **`TypeError`**: Raised when an operation is applied to an unsupported type.

#### Example: Handling a ZeroDivisionError

In this case, we will set up the script to "fail", by providing it with an impossible task: dividing something by `0`.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!
```

### Example: Using `else` and `finally`

We can make the decision tree a bit more complex, by using the `else` and `finally` operators.

In this case, we first try a division. If successful, we skip the `except` and jump to the `else`, which will print out the value, and `finally` we print out a statement `"Completed!"`.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")  # Output: Result: 5.0
finally:
    print("Completed!")  # Always executes
```

### Raising Custom Exceptions

We can also implement custom exceptions:

```python
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive!")

try:
    check_positive(-5)
except ValueError as e:
    print(e)  # Output: Number must be positive!
```



## Summary

MicroPython provides a solid foundation for programming microcontrollers with ease. In this guide, we covered:

- Variables and data types
- Lists and tuples
- Defining and calling functions
- Exception handling for graceful error recovery

With these fundamentals, you’re ready to build powerful and efficient applications. Dive into our additional tutorials for more advanced topics!  
