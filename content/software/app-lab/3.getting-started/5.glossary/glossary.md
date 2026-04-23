# Arduino App Lab & UNO Q Ecosystem Glossary

## **ADB (Android Debug Bridge)**

A command-line tool used to access the UNO Q's Linux shell over a USB connection. It allows users to run commands, manage files, and access the board's terminal without a network connection.

## **AI (Artificial Intelligence)**

The simulation of human intelligence by machines. In App Lab, AI models are often deployed as Bricks to perform tasks like face detection or object classification locally on the UNO Q.

## **API (Application Programming Interface)**

A set of rules allowing different software entities to communicate. Bricks expose high-level APIs that allow Apps to access complex functionalities like AI models or hardware drivers without low-level implementation.

## **App**

Arduino Apps exist in two distinct forms: a developer project created within the Arduino App Lab IDE workspace, and an execution package that runs under the Arduino App CLI. While the project is a workspace for human-readable logic and design, the package encapsulates all the elements needed to run.

Arduino Apps can contain several resources described in a .yaml manifest: high-level logic files (typically Python) for features such as UI, AI or networking, a low-level sketch (C++) for sensor and motor control, and Arduino Bricks, pre-built modules added to bring specific additional functionalities.

## **app.yaml**

A configuration file included in every App directory that stores metadata, such as the App's name, description, and the list of Bricks used in the project. This file is automatically updated when Bricks are added via the UI.

## **Arduino CLI**

An all-in-one command-line tool that handles board detection, library management, and sketch compilation. It serves as the underlying engine for Arduino App Lab and the Arduino App CLI.

## **Arduino App CLI**

A command-line interface tool pre-installed on the UNO Q that allows users to manage, build, start, and stop Apps directly from the terminal without using the graphical desktop application. It utilizes the standard **Arduino CLI** for sketch-related operations.

## **Arduino App Lab**

The integrated development environment (IDE) and resource manager designed for the Arduino UNO Q. It allows users to create, edit, and deploy Apps. It can run on a personal computer (Windows, macOS, Linux) or directly on the UNO Q board itself when in SBC Mode.

## **Arduino Flasher CLI**

A standalone command-line tool used to hard-reset the UNO Q by "flashing" a fresh installation of the Linux operating system (Image) onto the board. This process wipes all user data.

## **Arduino Router**

A background Linux service (`arduino-router`) that acts as a traffic controller between the Linux processor and the microcontroller. It manages the Bridge connection, allowing multiple processes to communicate with the hardware simultaneously.

## **Brick**

A reusable building block that an app can include to provide a specific feature, such as a web interface, a camera pipeline, an AI model, storage, or cloud connectivity. Bricks expose a high-level API so apps can use their functionality without implementing it from scratch.

## **Bridge**

A library and mechanism that enables bidirectional communication between the UNO Q's Linux microprocessor (MPU) and the STM32 microcontroller (MCU) using **Remote Procedure Calls (RPC)**. It allows Python scripts to control hardware pins and Arduino sketches to trigger Linux processes using functions like `provide`, `call`, and `notify`.

## **Console**

The interface within Arduino App Lab used to view logs and the status of a running App. It is divided into three tabs: Start-up (deployment logs), Main (Python output), and Sketch (Microcontroller output sent via `Monitor.print`).

## **CSI (Camera Serial Interface)**

A high-speed specification for camera-to-processor communication. The UNO Q features dual MIPI CSI connectors, enabling high-performance computer vision and imaging applications.

## **CV (Computer Vision)**

A field of AI that enables computers to derive meaningful information from visual inputs. The UNO Q is optimized for CV tasks such as barcode scanning, object tracking, and image analysis.

## **Desktop Mode (or USB Mode)**

One of the three main ways to operate the board. In this mode, the UNO Q is connected to a computer via a USB-C cable. The Arduino App Lab software runs on the computer, deploying Apps to the board over the USB connection.

## **Docker**

The underlying technology used to deploy Bricks (specifically those containing AI models) as isolated containers on the UNO Q board. Users can view the status of these containers via the board's terminal.

## **EDL Mode (Emergency Download Mode)**

A special boot mode used when flashing a new Linux image to the board. In this mode, the board changes its USB identity (VID `05c6`, PID `9008`), often requiring specific permissions (udev rules) on Linux computers to function.

## **GPIO (General Purpose Input/Output)**

Digital pins on the UNO Q that can be programmed as either inputs or outputs to control external components like LEDs or read data from sensors.

## **Linux Image**

The operating system file flashed onto the UNO Q. The board comes pre-installed with a customized Debian Linux distribution that includes necessary drivers and the Arduino App Lab runtime.

## **MCU (Microcontroller Unit)**

In the UNO Q architecture, the MCU is an **STM32U5** processor. It handles real-time tasks, hardware I/O, and runs the Zephyr OS, operating independently but in coordination with the more powerful MPU.

## **ML (Machine Learning)**

A subset of AI focused on building systems that learn from data. Developers can deploy ML models on the "edge" (directly on the UNO Q) using App Lab and Bricks.

## **MQTT (Message Queuing Telemetry Transport)**

A lightweight messaging protocol for sensors and mobile devices. The UNO Q supports MQTT (via Mosquitto) for efficient IoT communication and data reporting.

## **MPU (Microprocessor Unit)**

The primary processor of the UNO Q (**Qualcomm QRB2210**) capable of running a full Linux OS (Debian). It handles high-level logic, networking, and UI while communicating with the MCU via the Bridge.

## **Modulino**

A line of hardware nodes (sensors and actuators) connected via the **QWIIC** I2C connector, allowing for soldering-free expansion of the UNO Q's capabilities.

## **Network Mode**

A connection state where the UNO Q is accessed remotely over a local Wi-Fi network rather than a direct USB cable. This allows users to develop and run Apps on the board wirelessly via the Arduino App Lab after an initial setup.

## **QWIIC**

A standardized connection system for I2C sensors and actuators using 4-pin JST cables. The UNO Q features a built-in QWIIC connector, allowing users to quickly attach Modulino nodes and other peripherals without soldering.

## **RPC (Remote Procedure Call)**

A protocol that allows a program to execute a procedure in another address space. On the UNO Q, RPC is the foundation of the Bridge, enabling seamless communication between Python logic on the MPU and C++ code on the MCU.

## **SBC Mode (Single-Board Computer)**

A standalone mode where the UNO Q operates as a fully functional desktop computer. This requires connecting a USB-C hub (dongle) with power delivery, a monitor (HDMI), a keyboard, and a mouse directly to the board.

## **Sketch**

The specific file (`sketch.ino`) within an App that contains the C++ code running on the UNO Q's microcontroller (MCU).

## **SSH (Secure Shell)**

A cryptographic network protocol used to securely access the UNO Q's Linux terminal over a network (Wi-Fi). It is the primary way to manage the board wirelessly when not using USB/ADB.

## **UNO Q**

The hardware board supported by Arduino App Lab. It features a unique architecture with both a **Qualcomm QRB2210** microprocessor (running Debian Linux) and an **STM32U5** microcontroller (running Zephyr OS).

## **Zephyr OS**

The Real-Time Operating System (RTOS) that runs on the UNO Q's STM32U5 microcontroller (MCU). It operates beneath the Arduino core to handle real-time tasks and secure communication.