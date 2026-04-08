---
title: Getting Started with the Bridge
description: Learn how to use the Bridge to establish communication between the Linux microprocessor and the C++ microcontroller on your board.
overwriteSidebar: Getting Started
tags:
  - Getting Started
  - Bridge
  - RPC
  - API
  - Python
  - C++
  - Arduino App Lab
  - UNO Q
---

The Bridge is an RPC-based communication layer that allows the Linux microprocessor (MPU) and the Arduino microcontroller (MCU) on your board to exchange data. This guide walks you through a basic implementation: sending a message from a Python script on the Linux MPU to the MCU, which then prints a confirmation back to the console.

## Explore the Examples

The easiest way to see the Bridge in action is to explore the built-in examples. These example projects use the Bridge to establish communication between the Linux MPU and the Arduino MCU:

*   **Blink LED:** A simple example of using Python to toggle an LED pin on the microcontroller.
*   **Blink LED with UI:** Uses the WebUI Brick to control the MCU LED from a browser-based dashboard.
*   **Weather forecast on LED Matrix:** Fetches weather data in Python and sends it to the MCU to be displayed on an LED matrix.

To learn more about how to access and run Examples, see [Using Examples](../../2.getting-started/3.examples/examples.md).

## Use Bridge Communication in Your App

You can follow these steps by creating a new App or by implementing the logic into an existing project.

### 1. Prepare your App

If you are starting from scratch:
1. Open **Arduino App Lab**.
2. Select **My Apps** from the left sidebar.
3. Select **Create new app +**, provide a name (e.g., `Bridge Communication`), and select **Create new**.

If you are using an existing project, ensure you have both a `sketch/sketch.ino` (C++) and a `python/main.py` (Python) file ready.

### 2. Configure the Microcontroller (C++)

First, configure the MCU to listen for commands and respond. This is done by defining a function and "exposing" it so the Python environment can see it.

Open your `sketch/sketch.ino` file. We will build the sketch piece by piece:

1. **[Use the Sketch Library Manager](../../3.apps/5.develop-apps/develop-apps.md#add-sketch-libraries)** to add the `Arduino_RouterBridge` library to your App.

1. **Include the Library:**
   At the top of your file, include the Bridge library:
   ```cpp
   #include "Arduino_RouterBridge.h"
   ```
   
1. **Define the Callback Function:**
   Create the function that you want the Python script to trigger. In this case, we want to receive a number and print it to the console:
   ```cpp
   void handle_message(int value) {
     // Use Monitor.print to send text back to the App Lab console
     Monitor.print("MCU received value: ");
     Monitor.println(value);
   }
   ```
   
1. **Initialize and Expose:**
   In the `setup()` function, initialize the Bridge and register your function:
   ```cpp
   void setup() {
     // Start the Bridge communication layer
     Bridge.begin();
   
     // Expose the function to the Bridge so Python can call it.
     // We use "print_value" as the name Python will use to find it.
     Bridge.provide_safe("print_value", handle_message);
   }
   
   void loop() {
     // The Bridge handles incoming calls automatically in the background.
     // Keep the loop clear of blocking code.
   }
   ```
   
   `Bridge.provide_safe()` ensures your function executes within the main loop context when the processor is idle. This prevents conflicts with hardware interrupts or other background tasks.

### 3. Configure the Linux Script (Python)

Next, configure the Linux MPU to send data to the MCU using the Bridge.

1. Open your `python/main.py` file:
   
   **Import Utilities**
   Import the necessary tools to run the App and access the Bridge:
   ```python
   from arduino.app_utils import App, Bridge
   import time
   ```
   
1. **Define the Loop:**
   Create a function that will run repeatedly. We will use a counter to send different values:
   ```python
   counter = 0
   
   def loop():
       global counter
       
       # Wait for two seconds between messages
       time.sleep(2)
       
       # Increment the counter
       counter += 1
       
       # Call the C++ function "print_value" that we exposed earlier
       # We pass the current counter as the argument
       Bridge.call("print_value", counter)
   ```
   
1. **Start the App:**
   Finally, tell the system to start the App and run `loop()` function repeatedly:
   ```python
   App.run(user_loop=loop)
   ```

### 4. Run and Monitor

1. Click the **Run** button (play icon) in the top right corner.
2. Once the App starts, open the **Serial Monitor** tab in the **Console**.
3. You should see a message appearing every two seconds: `MCU received value: 1`, `MCU received value: 2`, and so on.

### 5. Tweak and Experiment

Try these modifications to see how the communication changes. Remember to **Stop** and **Run** the App again after making changes.

*   **Change the Frequency:** In `main.py`, change `time.sleep(2)` to `0.5`. Notice how much faster the messages appear.
*   **Send Different Data:** Instead of a simple counter, try sending a calculation or a random number (using the `random` module in Python).
*   **Multiple Arguments:** You can pass multiple values. Update your C++ function to accept two integers `void handle_message(int a, int b)` and update your Python call: `Bridge.call("print_value", val1, val2)`.
*   **Bidirectional Communication:** You can also expose functions in Python using `App.provide()` and call them from C++ using `Bridge.call()`.

## Best Practices

*   **Avoid Deadlocks:** Never call `Bridge.call()` or `Monitor.print()` inside a C++ function that you have exposed via `Bridge.provide()`. This can cause the communication layer to hang.
*   **Non-Blocking Code:** Ensure your `loop()` in both C++ and Python does not contain long `delay()` or `sleep()` calls that might prevent the Bridge from processing incoming requests.

## Next Steps

*   **[Bridge API Reference](/software/app-lab/5.bridge/1.bridge-api/content.md)**
*   **[Using Bricks with Bridge](/software/app-lab/4.bricks/2.use-bricks/use-bricks.md)**
