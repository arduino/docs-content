---
title: Bricks Architecture and Configuration Reference
description: A technical reference for Bricks inside Arduino App Lab, detailing thread lifecycle, YAML schemas, and configuration specifications.
overwriteSidebar: Reference
tags:
  - Bricks
  - Architecture
  - Python
  - Docker
  - Configuration
---

This document details the underlying execution model, thread lifecycle management, file directory structures, and configuration specifications for both preinstalled official bricks and custom bricks in the Arduino App Lab ecosystem.

## Core Concepts & Lifecycle Management

Bricks follow one of two execution patterns inside the `arduino.app_utils` framework, depending on whether you implement them as plain functions or managed classes.

### Managed Bricks (Class-based)

The vast majority of preinstalled Arduino Bricks, and advanced custom bricks, use a managed lifecycle. By decorating a class with `@brick`, the `arduino.app_utils.App` framework automatically handles its execution in the background.

- **Auto-Registration:** The `@brick` decorator acts as a class patcher. It modifies the `__init__` method of the class so that every time the class is instantiated, it automatically registers itself with the central `AppController` via `App.register(self)`.
- **Method Discovery:** When `App.run()` executes, the orchestrator automatically searches for and spawns background threads to run specific methods defined in your class:
  - `start(self)`: Called exactly once when the application starts. Use this for setup operations.
  - `stop(self)`: Called exactly once when the application is shutting down. Use this for cleanup and releasing resources.
  - `loop(self)`: Executed repeatedly in an infinite loop inside a dedicated background thread.
  - `execute(self)`: Executed exactly once inside its own background thread.
- **Method Decorators:** Instead of using the exact naming conventions above, you can explicitly tag class methods using:
  - `@brick.loop`: Spawns a dedicated background thread to run the decorated method in an infinite loop.
  - `@brick.execute`: Spawns a dedicated background thread to run the decorated method exactly once.

### Unmanaged Bricks (Module or Function-based)

Bricks don't require a managed class structure to execute. They can also be implemented as plain Python modules or functions without lifecycle hooks.

- **Custom Functions:** A custom brick can define plain functions in its `__init__.py` file. The main application script imports these functions and calls them manually.
- **Module Wrappers:** The `arduino:streamlit_ui` brick is an example of an unmanaged brick; it exposes the third-party `streamlit` module directly, bypassing the `App.run()` lifecycle entirely.

## App.run() Thread Management

By default, the `App.run()` function blocks the main thread. It initiates an infinite sleep loop to keep the process alive and ensure that background brick threads continue executing.

### The `user_loop` Parameter

If you pass a callable function to `App.run(user_loop=...)`, the orchestrator will execute that function repeatedly inside the infinite loop on the main thread. This is ideal for running continuous, repetitive code in simple applications without manually configuring dedicated background threads.

```py
from arduino.app_utils import App
import time

def my_continuous_loop():
    # This runs repeatedly on the main thread
    print("Main thread active...")
    time.sleep(1)

# App.run blocks the main thread and repeatedly executes my_continuous_loop
App.run(user_loop=my_continuous_loop)
```

<Alert type="warning">**Warning:** Because `App.run()` blocks the main thread, you must perform all your brick initialization, variable reading, and setup logic *before* calling `App.run()`.</Alert>

## Custom Bricks Directory Structure

Custom bricks are stored locally in your application's `bricks/` folder. The folder name must match the custom brick's configuration ID.

```text
my-app/
├── app.yaml
├── python/main.py
└── bricks/
    └── my_custom_brick/            # The Brick ID (must match folder name)
        ├── __init__.py             # Python logic (required)
        ├── brick_config.yaml       # Metadata (required)
        ├── brick_compose.yaml      # Docker services (optional)
        └── requirements.txt        # Python dependencies (optional)
```

## Brick Manifest Specification (`brick_config.yaml`)

Every brick requires a `brick_config.yaml` file, which acts as a manifest for the App Lab UI and the orchestrator.

### File Schema

```yaml
id: "arduino:object_detection"  # Unique identifier
name: "Object Detection"        # Display name in UI
description: "Detects objects using AI"
category: "video"               # UI Category (miscellaneous, video, audio, text, UI, Storage)
requires_display: webview       # Signal UI to automatically launch a webview window
required_devices:               # Required device classes (validated at startup)
  - camera
ports:                          # Network ports to expose
  - 7000
variables:                      # Configurable parameters (Environment Variables)
  - name: "THRESHOLD"
    description: "Detection sensitivity threshold (0.0 to 1.0)"
    default_value: "0.5"
    hidden: false               # If true, hidden from the UI
    secret: false               # If true, value is masked in the UI
  - name: "API_KEY"
    description: "Optional cloud service token"
    # No default_value means this is a required field in the UI
    secret: true                # Masks the input field

supported_boards:               # Limit brick to specific hardware
  - unoq
  - ventunoq
requires_services:              # Depend on core system containers
  - "arduino:genie"
mount_devices_into_container: true # Allow Docker containers to access hardware
```

### Key Fields Detail

- **`id`**: The unique identifier used by the system.
  - **Official Bricks:** Use the `arduino:` prefix (e.g., `arduino:web_ui`).
  - **Custom Bricks:** Match the folder name in `bricks/` and do **not** use a namespace prefix.
- **`variables`**: Parameters injected as **Environment Variables** into the app's environment.
  - Accessed in Python via `os.getenv("VARIABLE_NAME")`.
  - **Required Variables:** If `default_value` is missing, the user must provide a value in the UI before running the app.
  - **Secrets:** Setting `secret: true` will mask the input field in the App Lab UI.
- **`requires_display`**: When set to `webview`, this indicates that the brick exposes a graphical interface. This signals the App Lab desktop application to automatically open a new window or browser tab directed to the brick's web interface as soon as the app finishes starting.
- **`requires_services`**: List of core system services (IDs) that must be running for this brick to function (e.g., `arduino:genie` for LLM bricks).
- **`required_devices`**: Defines the *classes* of hardware devices the brick requires (e.g., `camera`, `microphone`, `speaker`). When the app is started, the `arduino-app-cli` performs startup validation to ensure at least one physical device of that class is currently connected to the board. If not, an error is raised.
- **`mount_devices_into_container`**: When `true`, hardware devices (like `/dev/video0`) requested in `required_devices` are automatically mounted into the brick's Docker container.

## Application Configuration (`app.yaml`)

Bricks must be declared in the `bricks` list within the application's `app.yaml` descriptor file. The CLI parses this file to configure the orchestrator.

Arduino App Lab automatically manages this section when using the visual interface.

```yaml
name: "My App Name"
description: "A description of the app"
icon: "😀"                 # Must be a single valid emoji
ports: []                 # Array of exposed ports for the app
bricks:
  # Official brick (simple declaration)
  - arduino:web_ui: {}

  # Custom brick with configuration variables
  - my_custom_brick:
      variables:
        NAME: "Arduino"
      model: "my_custom_model_id"  # Optional: Bind a specific AI model
```

## Containerization and Networking Constraints

Bricks can execute within an isolated background Docker container. You configure and manage this behavior using the following reference-grade rules:

- **Service Dependencies (`requires_services`):** If your brick relies on core containerized system services (such as local AI inference engines), list their system IDs here (e.g., `arduino:genie`). The orchestrator ensures these system services are active before launching your brick.
- **Hardware Access (`mount_devices_into_container`):** Setting this boolean field to `true` instructs the orchestrator to automatically mount any physical hardware devices matching the classes in `required_devices` (e.g., `/dev/video0`) into the brick's Docker container.
- **Virtual Compose Network:** When defining custom services inside a standard [Docker Compose file](https://docs.docker.com/reference/compose-file/) named `brick_compose.yaml`, the orchestrator runs those containers inside an isolated virtual network. The custom brick's Python code running inside the main application container communicates with these services via network APIs (HTTP, WebSockets, or TCP/IP) using the compose service name as the hostname.
- **Pre-compiled Images:** Arduino App Lab doesn't support compiling custom Docker images directly on the board from a `Dockerfile` via the `build` directive in `brick_compose.yaml`. You must build custom images beforehand, publish them to a public registry (such as GitHub Container Registry or Docker Hub), or load them onto the board manually using `docker load`.

## Official Repositories

| Repository | Purpose |
| :---- | :---- |
| `arduino/app-bricks-py` | Source code for preinstalled official bricks. |
| `arduino/app-bricks-examples` | Reference applications demonstrating brick integration. These are accessible in Arduino App Lab. |
| `arduino/arduino-app-lab` | The Arduino App Lab application. |
| `arduino/arduino-app-cli` | Command-line tool for managing and validating apps. |
