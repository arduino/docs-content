---
title: Use Bricks in Arduino App Lab
description: Learn how to add, configure, and initialize Bricks to extend your application's functionality.
overwriteSidebar: Using Bricks
tags:
  - Bricks
  - Python
  - Configuration
  - Arduino App Lab
---

Bricks provide modular, pre-packaged functionality—like a web interface or a database—that runs alongside your App's logic. This guide covers the workflow for adding Bricks to your project and initializing them in your code.

## Add a Brick to Your App

You manage Bricks through the graphical interface in Arduino App Lab. When you add a Brick, the system automatically updates your project's configuration.

1. [Open an App](../../3.apps/2.manage-apps/manage-apps.md#open-an-app).
2. Click the **Add Brick** button in the left sidebar to open the Bricks catalog.
   ![Screenshot of the App Editor in Arduino App Lab, highlighting the Bricks section in the left sidebar.](../../assets/app-lab-editor-hl-bricks.png)
3. Select a Brick from the list.
4. Follow the prompts to configure any required settings (e.g., port numbers or authentication keys).
5. Arduino App Lab automatically adds the Brick entry to your `app.yaml` file.

<Alert type="note">**Important:** Do not manually edit the `bricks` entry inside the `app.yaml` file. Manual changes can cause syntax errors that prevent the App Lab editor from opening your project.</Alert>

## Use Bricks in Python

After adding a Brick via the UI, you must import and initialize it in your `python/main.py` file to use its features.

### 1. Import the Brick Class

Import the specific Brick class from the `arduino.app_bricks` module. For example, to use the Web UI Brick:

```python
from arduino.app_bricks.web_ui import WebUI
```

### 2. Initialize the Brick

Create an instance of the Brick object in your script. This initializes the connection between your Python logic and the Brick process.

```python
web_ui = WebUI()
```

### 3. Launch the App

You must include the `App.run()` function at the very bottom of your `main.py` file. This command acts as the orchestrator, launching all imported Bricks and starting the Bridge communication.

```python
from arduino.app_utils import App

# ... your initialization code ...

# Start the App and all Bricks
App.run()
```

<Alert type="warning">**Warning:** The App framework ignores any code placed after `App.run()`. Ensure all your logic and Brick initializations happen before this call.</Alert>

## Access Brick Documentation

Each Brick includes its own specific API and usage examples.

* When you add a Brick, its documentation opens automatically in a new tab.
* To view the documentation for an existing Brick, click on the Brick's name in the left sidebar.

<Alert type="success">**Tip:** Use the **Usage examples** in the Brick documentation to find the exact code snippets needed for your implementation.</Alert>
