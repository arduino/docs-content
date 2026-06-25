---
title: Create Custom Bricks in Arduino App Lab
description: Learn how to create and manage Custom Bricks to expand your Apps with custom Python libraries and Docker containers.
overwriteSidebar: Custom Bricks
tags:
  - Bricks
  - Python
  - Docker
  - Custom
  - Arduino App Lab
---

**Custom Bricks** let you package your own Python modules or third-party Docker services into reusable components. Build a feature once, package it as a Custom Brick, and reuse it across your projects.

While Arduino Bricks provide ready-to-use features, Custom Bricks let you integrate any tool or service your application needs. 

## Anatomy of a Custom Brick

A Custom Brick is a self-contained package stored locally within your App. Each Custom Brick is located inside the `bricks/` folder within your App's root directory, and the Brick's ID corresponds to the name of its folder. Custom Bricks don't use a namespace prefix (like `arduino:`).

A typical Custom Brick structure looks like this:

```text
my-app/
├── app.yaml
├── python/main.py
└── bricks/
    └── my_custom_brick/            # The Brick ID and folder name
        ├── __init__.py             # Python logic (required)
        ├── brick_config.yaml       # Brick metadata and variables (required)
        ├── brick_compose.yaml      # Docker Compose configuration (optional)
        └── requirements.txt        # Python dependencies (optional)
```

<Alert type="info">**Note:** Custom Bricks are local to the App they are created in. They are not shared across different Apps or shown in the official Bricks index.</Alert>

## Create a Custom Brick

You can generate the foundational structure for a Custom Brick directly from the App Lab interface.

1. [Open an App](../../apps/manage-apps/#open-an-app).
2. Click the **Add Brick** button at the top of the **Editor sidebar**.
3. At the bottom of the Bricks catalog, select **Create Custom Brick**.
4. Enter a name (ID) for your Brick. This must be a valid Python package name (e.g., lowercase letters, numbers, and underscores).
5. App Lab will generate the folder structure and basic files for your Custom Brick inside the `bricks/` directory.

### Configuration (`brick_config.yaml`)

The `brick_config.yaml` file defines the identity of your Brick and the environment variables it accepts from the App Lab UI.

```yaml
id: my_custom_brick
name: My Custom Brick
description: "A description of what my Custom Brick does."
category: miscellaneous
variables:
  - name: "MY_SETTING"
    description: "A custom setting for this brick"
    default_value: "123"
```

### Python Logic (`__init__.py`)

Custom Bricks can be implemented in two ways depending on your needs:

#### 1. Simple Function-based Bricks
For utility functions or simple logic, you define plain Python functions. You don't need to use any special decorators.

```python
# bricks/my_custom_brick/__init__.py
def say_hello():
    print("Hello from the custom brick!")
```

#### 2. Managed Class-based Bricks
If you want your Custom Brick to behave exactly like an official Brick with automatic lifecycle management (background threads, startup/shutdown hooks), you can use the `@brick` decorator.

```python
# bricks/my_custom_brick/__init__.py
from arduino.app_utils import brick
import time

@brick
class MyManagedBrick:
    def start(self):
        print("[Brick] Started")
    
    @brick.loop
    def my_background_task(self):
        print("[Brick] Running in background...")
        time.sleep(1)
```

### Docker Containers (`brick_compose.yaml`)

If your Custom Brick requires external services (such as databases or companion APIs), you can define them in this file. The `brick_compose.yaml` file is a standard [Docker Compose file](https://docs.docker.com/reference/compose-file/). The orchestrator will automatically pull and run these containers alongside your App. For full details on Docker capabilities and networking, see [Bricks Architecture and Configuration Reference](../bricks-reference/).

```yaml
# bricks/my_custom_brick/brick_compose.yaml
services:
  my_database:
    image: postgres:latest
```

<Alert type="warning">**Important:** The orchestrator executes the custom brick's Python code (in `__init__.py`) within the main application's container, **not** inside the custom Docker containers you define here. This means your Python code can't directly access system libraries or files inside `my_database`. Instead, your Python code must communicate with the containerized service over the virtual Docker Compose network using a network API (such as HTTP, WebSockets, or TCP/IP). You can reach the service using the service name defined in your `brick_compose.yaml` (e.g., `my_database`) as the hostname.</Alert>

<Alert type="info">**Note:** Docker images specified in `brick_compose.yaml` must be publicly accessible, as App Lab doesn't currently support private registries for Custom Bricks.</Alert>

## Using Your Custom Brick

Once created, you must register your Custom Brick in `app.yaml` and import it into `main.py`.

**1. Registration:** The App Lab UI manages `app.yaml` for you when you create the Custom Brick.
```yaml
# app.yaml
bricks:
  - my_custom_brick:
      variables:
        MY_SETTING: "123"
```

**2. Implementation:** Because the orchestrator automatically adds the `bricks/` directory to your Python path, you can import your custom brick directly by its folder name. 

```python
# python/main.py
import os
from arduino.app_utils import App
from my_custom_brick import say_hello, MyManagedBrick

# Call a simple function
say_hello()

# Read the variable passed from the UI
print("Setting:", os.getenv("MY_SETTING"))

# Instantiate a managed brick so App.run() handles it
managed_brick = MyManagedBrick()

# Start the App
App.run()
```

## AI Models in Custom Bricks

In the App Lab ecosystem, there is a strict separation between **AI Bricks** (the Python interface and Docker Runner) and **AI Models** (the data blobs/weights). 

If your Custom Brick relies on Edge Impulse models, you declare them in a `models-list.yaml` file. The orchestrator uses this file to download the `.eim` models to the board so the runner can load them.

```yaml
# bricks/my_custom_brick/models-list.yaml
models:
  - my-model:
      runner: brick
      name: "Custom Model"
      bricks:
        - id: "my_custom_brick"
      metadata:
        ei-project-id: 12345
        ei-model-url: "https://studio.edgeimpulse.com/public/12345/live"
```

<Alert type="info">**Note:** When you export an App that contains a Custom Brick, the Brick's source code is included in the export. However, external dependencies like AI models or Docker images are not exported and must be re-downloaded when the App is imported elsewhere.</Alert>
