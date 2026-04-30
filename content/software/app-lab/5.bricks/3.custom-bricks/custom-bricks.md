---
title: Create Custom Bricks in Arduino App Lab
description: Learn how to create and manage Custom Bricks to extend your App Lab applications with personalized Python libraries and Docker containers.
overwriteSidebar: Custom Bricks
tags:
  - Bricks
  - Python
  - Docker
  - Custom
  - Arduino App Lab
---

**Custom Bricks** transform App Lab into an extensible platform, allowing you to package your own specialized services or third-party tools into modular, reusable components. Build something once, package it as a Brick, and reuse it across your project.

While the built-in Bricks provide ready-to-use functionalities like AI models and Web UIs, Custom Bricks give you the freedom to integrate any tool or service you need. If you can code it in Python, you can make a Brick out of it.

## Types of Custom Bricks

Custom Bricks come in two varieties, suited to different levels of complexity:

1. **Python-only Bricks**: The simplest approach. You create a Python library that exposes an API to your main program. This is perfect for utility functions, data processing, or custom algorithms you want to reuse.
2. **Python + Container Bricks**: Add Docker containers to your Brick for more powerful capabilities. This allows you to run specialized tools, external APIs, or complex services (like a PostgreSQL database or a custom MQTT broker) alongside your app in isolated environments.

## Anatomy of a Custom Brick

A Custom Brick is a self-contained Python package stored locally within your App's directory. Each Custom Brick is located inside a reserved `bricks/` folder within your App's root directory, and the Brick's ID corresponds to the name of its Python package folder.

A typical Custom Brick structure looks like this:

```text
my-app/
├── app.yaml
├── python/
│   └── main.py
└── bricks/
    └── my_custom_brick/            # The Brick ID and Python package name
        ├── __init__.py             # Your Python logic
        ├── brick_config.yaml       # Brick metadata (ID, name, description)
        ├── brick_compose.yaml      # (Optional) Docker Compose configuration
        ├── requirements.txt        # (Optional) Python dependencies
        ├── docs/                   # (Optional) Brick documentation
        │   └── API.md
        └── examples/               # (Optional) Usage examples
            ├── 01_basic.py
            └── 02_advanced.py
```

<Alert type="info">**Note:** Custom Bricks are local to the App they are created in. They are not shared across different Apps or shown in the built-in Bricks index.</Alert>

## Create a Custom Brick

You can generate the foundational structure for a Custom Brick directly from the App Lab interface.

1. [Open an App](../../apps/manage-apps/#open-an-app).
2. Click the **Add Brick** button at the top of the **Editor sidebar**.
3. At the bottom of the Bricks catalog, select **Create Custom Brick**.
4. Enter a name (ID) for your Brick. This must be a valid Python package name (e.g., lowercase letters, numbers, and underscores).
5. App Lab will generate the folder structure and basic files for your Custom Brick inside the `bricks/` directory.

### Configuration (`brick_config.yaml`)

The `brick_config.yaml` file defines the identity of your Brick.

```yaml
id: my_custom_brick
name: My Custom Brick
description: "A description of what my Custom Brick does."
```

When your App is initialized, the system automatically reads this file and makes the Brick available. Ensure the `id` matches the folder name exactly.

### Python Logic (`__init__.py`)

This is where you write the Python code that interfaces with your App. You expose functionality using the `@brick` decorator provided by the Arduino App Lab utilities.

```python
from arduino.app_utils import brick

@brick
class CustomBrick:
    """My Custom Brick implementation."""

    def __init__(self):
        print("[CustomBrick] Initialized")
    
    def do_something(self):
        print("[CustomBrick] Doing something useful...")
```

### Docker Containers (`brick_compose.yaml`)

If your Custom Brick requires external services, you can define them using a Docker Compose file. The system will automatically pull and run these containers alongside your App.

```yaml
services:
  my_service:
    image: custom_registry/my_service:latest
    ports:
      - "8080:8080"
```

<Alert type="warning">**Important:** Docker images specified in `brick_compose.yaml` must be publicly accessible, as App Lab does not currently support private registries for Custom Bricks.</Alert>

## Using Your Custom Brick

Once created, using a Custom Brick is identical to using a built-in Brick. Import the class from your package and initialize it in your App's `main.py`.

```python
from arduino.app_utils import App
from my_custom_brick import CustomBrick

# Initialize the Custom Brick
my_brick = CustomBrick()

# Use its functionality
my_brick.do_something()

# Start the App
App.run()
```

## AI Models in Custom Bricks

Advanced Custom Bricks can utilize their own local index of AI models by including a `models-list.yaml` file. This allows the Brick to declare dependencies on specific models that need to be downloaded to the board.

```yaml
# models-list.yaml inside your Custom Brick folder
models:
  - my-model:
      runner: brick
      name: "Lightweight-Face-Detection"
      description: "My custom detection model"
      model_labels:
        - face
      bricks:
        - id: "my_custom_brick"
          model_configuration:
            "MY_ENV": "test"
      metadata:
        source: "qualcomm-ai-hub"
        ei-gpu-mode: false
        ei-project-id: 830703
        ei-model-url: "https://studio.edgeimpulse.com/public/830703/live"      
        source-model-id: "face-det-lite"
        source-model-url: "https://aihub.qualcomm.com/models/face_det_lite"
```

<Alert type="info">**Note:** When you export an App that contains a Custom Brick, the Brick's source code is included in the export. However, external dependencies like AI models or Docker images are not exported and must be re-downloaded when the App is imported elsewhere.</Alert>
