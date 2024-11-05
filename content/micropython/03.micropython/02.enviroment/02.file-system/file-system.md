---
title: 'File System'
description: 'Learn how to use the File Sytem in MicroPython.'
author: 'Pedro Lima'
tags: [MicroPython, REPL]
---


When working with MicroPython, we’re not limited to a single program like in traditional Arduino sketches. Instead, MicroPython provides a file system, enabling us to store and manage multiple files on our microcontroller. This opens up powerful capabilities for organizing code, managing assets, and creating modular projects.

In this article, we’ll explore how the MicroPython file system works, how to organize files effectively, and the typical structure of MicroPython projects.

## The MicroPython File System: Key Differences

In traditional Arduino programming, we upload a single compiled file directly to the microcontroller, where it runs immediately. With MicroPython, however, we work within a file system that can store multiple files. This file system allows us to:

- **Upload and Download Files**: We can save individual scripts, libraries, and assets directly on the device.
- **Organize Project Files**: Create folders, save multiple scripts, and organize files for a modular approach.
- **Edit Files Directly on the Device**: Modify files without needing to overwrite everything, making adjustments faster and more flexible.

## Accessing the MicroPython File System

To interact with the MicroPython file system, we’ll use Arduino Labs for MicroPython, which provides tools to manage and view files directly on our device. Here’s how to get started:

1. **Connect to Your Device**: Open Arduino Labs for MicroPython and establish a connection to our microcontroller.
2. **Upload and Download Files**: Use the file manager to upload files from our computer to the microcontroller or download files back to our computer.
3. **Organize Files**: We can create folders and store multiple files, making it easy to organize our project.

## Basic MicroPython File Structure

A typical MicroPython project includes a main file, boot script, libraries, and any supporting files our project needs. Here’s a standard layout:

```
/ (Root Directory)
├── boot.py
├── main.py
```

### Key Files

- **`boot.py`**: Runs once at startup, before `main.py`, and is typically used for system configurations that need to be set when the device first powers on.
- **`main.py`**: This is the primary script, similar to the `setup()` and `loop()` structure in Arduino. It runs automatically after `boot.py` finishes.

## Example: Switching Execution from `main.py` to `favorite_things.py`

Let’s say we’re creating a project where `main.py` runs and, at a certain point, hands off control to `favorite_things.py` to perform a specific task. Here’s how we might organize it.

1. **Write the Main Script** (`main.py`): This script runs some initial code and then switches to executing `favorite_things.py`.
2.Create the file "favourite_things.py".
3. **Add Content to `favorite_things.py`**: In this case, we’ll simply print a message from `favorite_things.py`.

### Sample `main.py` Code

Here’s how `main.py` might look, printing an introductory message and then executing `favorite_things.py`:

```python
def main():
    print("Getting the list of my favourite things...")
    
    # Now execute favorite_things.py
    print("Switch to favorite_things.py...")
    try:
        with open("favorite_things.py") as f:
            exec(f.read())
    except OSError:
        print("Error: Could not open favorite_things.py")

if __name__ == "__main__":
    main()
```

### Sample `favorite_things.py` Code

In `favorite_things.py`, we’ll keep it simple with a message:

```python
# favorite_things.py
print("Bears. Beets. Battlestar Galactica.")
```

### Explanation

- **Switching Execution**: `main.py` starts by printing an introductory message, and then uses `exec(f.read())` to read and run the content of `favorite_things.py`.
- **Running Another Script**: The `exec()` function allows `main.py` to execute `favorite_things.py` as if it were part of `main.py`, printing “Bears. Beets. Battlestar Galactica.” directly.

### Expected Output

When you run `main.py`, the output should look like this:

```
Getting the list of my favourite things...
Switch to favorite_things.py...
Bears. Beets. Battlestar Galactica.
```

This setup demonstrates how to use MicroPython’s file system to organize and execute multiple scripts, allowing for modular and readable code.

## Organizing Code with Modules and Libraries

When you start importing custom modules or libraries, MicroPython will automatically create a `/lib` folder to store them. This helps keep external libraries or reusable functions separate from your main code. You can use this structure to further organize your project, making it easy to manage larger codebases.

For example:

```
/ (Root Directory)
├── boot.py
├── main.py
├── /lib
│   ├── my_custom_library.py
```

### Using Libraries in `main.py`

After placing reusable code in `/lib`, you can import it directly in `main.py`:

```python
from lib.my_custom_library import some_function

some_function()
```

This structure allows for cleaner, more modular code that’s easy to scale as your project grows.

## Conclusion

MicroPython’s file system brings flexibility and structure to embedded programming, enabling a more organized and modular approach. By understanding the typical file structure and how to manage files, we’ll be able to create more complex and maintainable projects.

**Tips for Organizing Our MicroPython Projects**

- **Modularize Code with Additional Scripts**: Store reusable or specific tasks in separate files, making `main.py` clean and focused on high-level logic.
- **Leverage the `/lib` Folder**: Use the automatically created `/lib` folder to keep libraries organized and separate from your main application code.
- **Edit and Manage Files Easily**: Arduino Labs for MicroPython’s file management tools make it easy to upload, download, and modify files on the device.

With a well-organized file system, we can streamline our development process and unlock new possibilities with MicroPython!