---
title: Develop Apps in Arduino App Lab
overwriteSidebar: Develop Apps
description: Learn how to write code, manage dependencies, and use the Bridge to build hybrid applications in Arduino App Lab.
tags:
  - Apps
  - Development
  - Python
  - Sketch
  - Bridge
  - Arduino App Lab
---

Developing an App for the Arduino UNO Q involves programming for two distinct environments simultaneously: a Linux microprocessor running Python, and an STM32 microcontroller running an Arduino C++ sketch.

## Project Files

Every App contains two core files that host your code:

* **`python/main.py`**: The entry point for the Linux-side application, [written in Python](#python-development).
* **`sketch/sketch.ino`**: The [Arduino sketch](#sketch-development) running on the microcontroller.
* **`README.md`**: Project documentation.

Arduino App Lab automatically manages these configuration files:

* **`sketch/sketch.yaml`**: The configuration file for the sketch (read-only).
* **`app.yaml`**: The configuration file for Bricks and App properties (read-only).

To learn more about the App file structure, see [About Apps](../1.about-apps/about-apps.md).

### Explore and Open Files

1. [Open an App](../2.manage-apps/manage-apps.md#open-an-app).
1. Find the **File Manager** in the left sidebar.
   ![Screenshot of the App Editor in Arduino App Lab, highlighting in the Files browser.](../../assets/app-lab-editor-multi-tab-hl-files.png)
1. If folders are not displaying correctly, try closing and expanding the File Manager.
1. Click on a folder to expand it.
1. Click on a file to open it in a new tab.

### Add Files or Folders

**Create a file or folder in the project root directory:**

1. Select an existing file on the same level, like `README.md`.
1. Click the **Create file** icon.
   ![The "Create file" icon in Arduino App Lab.](../../assets/app-lab-editor-files-hl-add.png)
1. Select one of the following:
   * _Create new file_
   * _Create new folder_

**Create a file or folder inside a folder:**

1. **Right-click** on a folder.
1. Select one of the following:
   * _Create new file_
   * _Create new folder_

### Rename or Delete Files

1. **Right-click** on the file you want to rename or delete.
1. Select one of the following:
   * _Rename_
   * _Delete_

### Moving files and folders

Arduino App Lab currently does not support moving files and folders.

## Python Development

The Python script (`main.py`) handles the high-level logic and complex processing of your application. Running in its own isolated environment on the board, it provides the power needed for tasks like running AI models, hosting web servers, or performing data analysis.

### App.run()

Every Python script **must** include the `App.run()` function at the very bottom of the file to start the App. This command initializes App utilities and launches any imported Bricks. Note that the App framework ignores any code placed after `App.run()`.

The usage of `App.run()` depends on how you want to control your App's logic:

#### With user_loop function

If you need your Python script to perform repetitive tasks or maintain its own execution flow, pass a custom function to the `user_loop` parameter. This function will be called repeatedly by the App framework.

```python
from arduino.app_utils import App
import time

def loop():
    # This logic runs repeatedly on the Linux side
    print("Performing periodic task...")
    time.sleep(10)

# Start the App and run the loop
App.run(user_loop=loop)
```

#### Without user_loop function

If **Bricks** (e.g., a Web UI with its own event loop) or the **Sketch** (via Bridge calls that trigger Python functions) handle your App's logic, you can call `App.run()` without any arguments. This starts Bricks and utilities while keeping the Python environment active in the background.

```python
from arduino.app_utils import App, Bridge
import time

def my_function():
   # This logic runs when the function is called by the microcontroller
    print("Performing task...")


# Allow the microcontroller to call "my_function"
Bridge.provide("my_function", my_function)

# Start the App (no custom loop needed)
App.run()
```

### Add Bricks

Bricks are pre-packaged code modules that run as separate processes alongside your App. Each Brick provides a specific functionality, such as a web interface or a database, that you can interact with from your Python script.

**To use a Brick:**

1. Click the **Add Brick** button in the left sidebar to open the Bricks catalog.
   ![Screenshot of the App Editor in Arduino App Lab, highlighting the Bricks section in the left sidebar.](../../assets/app-lab-editor-hl-bricks.png)
2. Select a Brick from the list and follow the prompts to configure any required settings.
3. Arduino App Lab automatically adds the Brick configuration to your `app.yaml` file. Note that you should not manually edit the `bricks` entry in this file.
4. Review the Brick's documentation, which Arduino App Lab opens in a new tab when you add the Brick. The **Overview** and **Usage examples** contain the specific code needed for implementation.
5. Import and initialize the Brick in your `main.py` file.

<Alert type="success">**Tip:** Click on an added Brick in the sidebar to open its documentation.</Alert>

### Use Python Packages

You can use external Python packages (like `numpy` or `flask`) by creating a requirements file.

**To add dependencies:**

1. In the file browser, create a new file named `requirements.txt`.
2. **Important:** Place the `requirements.txt` file inside the `python/` folder, not the root of the App.
3. List your packages (one per line) in the file.
4. When you click **Run**, the `uv` package manager automatically installs the listed packages into the App's virtual environment.

## Sketch Development

The Arduino sketch (`sketch.ino`) handles real-time interaction with hardware, such as reading sensors or controlling motors.

### Add Sketch Libraries

In Arduino App Lab, you install libraries on a per-App basis to prevent version conflicts between projects.

**To add a library:**

1. Click the **Add sketch library** button (the open book icon with a **+** sign) in the left sidebar.
   ![Screenshot of the App Editor in Arduino App Lab. The "Sketch Libraries" section in the left sidebar is highlighted.](../../assets/app-lab-editor-hl-libraries.png)
2. Search for the library you need (e.g., `Servo` or `OneWire`).
3. Select the desired version and click **Install**.
4. Arduino App Lab updates the `sketch.yaml` file automatically and downloads the library when you launch the App.

### Serial Monitor

The system routes standard `Serial.print()` commands from your sketch to hardware UART pins (0 and 1), so they do not appear in the App Lab console. To debug your code in the UI, use the `Monitor` object.

**To use the Monitor:**

1. [Use the Sketch Libraries Manager](#add-sketch-libraries) to add the **Arduino_RouterBridge** library.
1. Include the bridge header at the top of your sketch: `#include "Arduino_RouterBridge.h"`.
1. Call `Monitor.begin();` inside your `setup()` function.
1. Use `Monitor.print()` or `Monitor.println()` for logging. Output will appear in the **Serial Monitor** tab of the Console.

![Screenshot of Arduino App Lab, displaying the Serial Monitor tab of the Console.](../../assets/app-lab-editor-console-serial-monitor-top.png)

This sketch will print `Hello from the MCU!` once per second:

```cpp
#include "Arduino_RouterBridge.h"

void setup() {
  Bridge.begin();
  Monitor.begin();
}

void loop() {
  Monitor.println("Hello from the MCU!");
  delay(1000);
}
```

## Python/Sketch Communication

The `Bridge` allows your Python script and Arduino sketch to exchange data using Remote Procedure Calls (RPC).

See [Getting Started with the Bridge](../../5.bridge/1.get-started-with-bridge/get-started-with-bridge.md) to learn more.

## Running and Monitoring Your App

Once your code is ready, click the **Run** button in the top right corner. The environment will compile the sketch, flash it to the microcontroller, and start the Python container.

Monitor your App using the **Console** tab:

* **App launch**: Compilation output and deployment logs.
* **Serial Monitor**: `Monitor.print()` output from your Arduino sketch.
* **Python**: `print()` output from your Python script.

See [Run and Monitor Apps](../6.run/run.md) to learn more.
