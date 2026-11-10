---
title: Use Bricks in Arduino App Lab
description: Learn how to add, configure, and initialize Bricks to extend your Apps's functionality.
overwriteSidebar: Using Bricks
tags:
  - Bricks
  - Python
  - Configuration
  - Arduino App Lab
---

Add and configure **Bricks** to expand your application with pre-built dashboards, AI models, or local databases. You manage Bricks via the Arduino App Lab interface and initialize them directly within your Python script.

## Add a Brick to Your App

You manage Bricks through the graphical interface in Arduino App Lab. When you add a Brick, the system automatically updates your project's configuration (`app.yaml`).

You can either add a pre-built Brick from the Bricks catalog, or create a Custom Brick from scratch.

### Add an Arduino Brick

1. [Open an App](../../apps/manage-apps/#open-an-app).
2. Click the **Add Brick** button at the top of the **Editor sidebar** to open the Bricks catalog.
   ![Screenshot of the App Editor in Arduino App Lab, highlighting the Bricks section in the Editor sidebar.](../../assets/playwright/editor/add-brick-button.png)
3. Select a Brick from the list and select **Add**.
4. Follow the prompts to configure any required settings (e.g., credentials or thresholds).
5. App Lab adds the Brick to your `app.yaml` file and suggests the next steps: check the Brick's **Usage examples**, and copy the code you need into `main.py`.

Bricks that are not available for your board are not listed. See the **Boards** column in the [list of Bricks](../about-bricks/#list-of-bricks).

### Configure Brick Variables

Many Bricks (both Arduino and Custom) accept configuration variables, such as API keys or threshold values.

1. Click on the Brick's name in the **Bricks** section of the Editor sidebar to open the Brick's detail page.
2. Select **Brick configuration** and set the variables. For AI Bricks, select the model in the **AI Models** tab (see [AI Models](../../integrations/models/)).
3. App Lab saves these settings to your `app.yaml` file, and passes them to the Brick as environment variables when the App runs.

If a required variable is missing when you select **Run**, App Lab asks you to configure the Brick first, then starts the App. Secret variables, such as API keys, are masked in the interface.

To remove a Brick from your App, open its menu in the **Bricks** section and select **Remove**.

<Alert type="note">

**Important:** When you use the App Lab UI, the system manages the `app.yaml` file automatically. Manual changes can cause syntax errors that prevent the editor from opening your project.

</Alert>

### Create a Blank Custom Brick

If you need to package your own Python logic or Docker containers into a reusable module, you can create a Custom Brick directly within your application.

To learn more, see [Create Custom Bricks](../custom-bricks/).

## Use Bricks in Python

After adding a Brick, you must import its Python package into your App's `main.py` file to instantiate its classes or call its functions.

### Managed Bricks

The vast majority of Bricks utilize the App framework's lifecycle management system. You import the class, instantiate it to register it with the system, and the App framework automatically manages its execution:

1. Import the Brick's Python package from the `arduino.app_bricks` namespace (or directly by its folder name if it's a Custom Brick).
2. Instantiate the Brick class.
3. Call `App.run()` at the very bottom of your script to start all registered Bricks.

```python
from arduino.app_utils import App

# 1. Import Bricks
from arduino.app_bricks.web_ui import WebUI
from my_sensors import MySensorBrick

# 2. Instantiate Bricks
ui = WebUI()
sensors = MySensorBrick()

# 3. Launch the App and all Bricks
App.run()
```

<Alert type="note">

**Important:** The `App.run()` call typically blocks the main thread. Ensure all your setup logic and Brick initializations happen before this call.

</Alert>

### Unmanaged Bricks

Some simpler Custom Bricks or specific official Bricks (like `arduino:streamlit_ui`) don't use the lifecycle management system. Instead, you manage their execution directly from the App's Python script code.

```python
import os
from my_simple_sensor import read_value

# Call a custom function directly
value = read_value()
```

## Access Brick Documentation

Each Brick includes its own specific API and usage examples.

- To view the documentation for a Brick, click on the Brick's name in the **Bricks** section of the Editor sidebar. The Brick opens in a new tab, with these sections:
  - **Overview**: What the Brick does and how it works.
  - **Usage examples**: Code snippets you can copy into your App.
  - **API documentation**: The classes and functions of the Brick's Python API.
  - **AI Models**: For AI Bricks, the models you can use. See [AI Models](../../integrations/models/).

<Alert type="success">

**Tip:** Use the **Usage examples** in the Brick documentation to find the exact code snippets needed for your implementation.

</Alert>
