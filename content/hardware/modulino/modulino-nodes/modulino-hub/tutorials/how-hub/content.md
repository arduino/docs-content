---
title: "Getting Started with Modulino Hub"
description: "Learn how to use the Modulino Hub, an 8-channel I2C multiplexer, with Modulino nodes and other I2C devices in Arduino and MicroPython."
tags:
 - Modulino
 - Hub
 - I2C
 - Multiplexer
 - TCA9548A
 - Qwiic
author: 'Pedro Sousa Lima, José Bagur'
hardware:
 - hardware/11.modulinos/modulinos/modulino-hub
software:
 - ide-v2
 - web-editor
 - micropython
---

![Modulino Hub Overview](assets/hub_overview.png)

The Modulino Hub is an I²C multiplexer that provides eight independent I²C channels. It lets you use several devices with the same I²C address in the same project and helps organize larger I²C networks into separate bus segments. This tutorial describes the Modulino Hub hardware and shows how to use it with Modulino nodes and other I²C devices using both the Arduino and MicroPython libraries.

## Why Use the Modulino Hub?

Each device on an I²C bus has a unique address. When two devices share the same address, the host board cannot distinguish between them, and communication with both fails. Some Modulino nodes, such as the Modulino Thermo, have a fixed I²C address, so you can't connect two of them directly to the same bus. The Modulino Hub solves this by placing each device on its own channel: when the host selects a channel, the Modulino Hub connects only that channel to the main bus, and the devices on it can be accessed without conflicts.

Devices connected to the main Modulino chain remain visible on the bus at all times. Devices connected to the Modulino Hub's output channels are visible only while their channel is selected. Modulino nodes and other I²C devices can therefore coexist in the same project, with the Modulino Hub used only for the devices that need it.

Beyond resolving address conflicts, the Modulino Hub helps organize larger projects. Specific channels can be dedicated to different parts of a system, for example, environmental sensors on channels 0 to 2 and input devices on channels 3 to 5. This segmentation also improves signal integrity in larger I²C networks. Since unselected channels are isolated from the main bus, the capacitance of their cables and devices does not add to the bus load. When a project requires more than eight channels, you can connect additional Modulino Hubs to the same bus, as described in the [Address Configuration](#address-configuration) section.

## Hardware Overview

### General Characteristics

The **Modulino Hub** is based on the **TCA9548ARGER**, an 8-channel I²C switch from Texas Instruments. The Modulino Hub connects to the main Modulino chain through its input connectors and routes the I²C bus to one of its eight output channels, each with its own Qwiic connector. Because each channel is an independent I²C bus segment, you can connect devices that share the same I²C address to different channels and access them one at a time.

The main characteristics of the Modulino Hub are summarized in the following table:

| **Specification** | **Details**                                  |
|:-----------------:|----------------------------------------------|
|         IC        | TCA9548ARGER (8-channel I²C switch)          |
|      Channels     | 8 independent I²C buses                      |
|   Supply Voltage  | +3.3 VDC (from the Qwiic input connectors)   |
|     Interface     | I²C                                          |
| Pull-up Resistors | 4.7 kΩ on SDA and SCL of each output channel |
|  Qwiic Connectors | 10 (2 input, 8 output)                       |
|     Indicator     | Green power LED                              |

Each output channel includes 4.7 kΩ pull-up resistors to +3.3 VDC on its SDA and SCL lines, so devices connected to the output channels do not require external pull-up resistors. The main bus on the input side does not include pull-up resistors on the Modulino Hub; it relies on the host board's pull-up resistors and those of other devices in the Modulino chain.

Channels are selected through software. Only the selected channel is connected to the main bus, while the remaining channels stay isolated. In the Modulino library API, channels are referred to as ports. The default I²C address of the Modulino Hub is as follows:

| **Modulino I²C Address** | **Hardware I²C Address** |   **Configurable Addresses**   |
|:------------------------:|:------------------------:|:------------------------------:|
|          `0x70`          |          `0x70`          | `0x70`-`0x77` (solder jumpers) |

### Pinout

![Modulino Hub Pinout](assets/HubPinout.png)

#### Qwiic Connectors (10×, 1×4 Each)

The Modulino Hub provides ten Qwiic connectors: two input connectors for the main Modulino chain and eight output connectors, one for each channel. The two input connectors are on the short sides of the board and are wired in parallel, so you can place the Modulino Hub anywhere in the Modulino chain while passing the main bus to the next node. The horizontal output connectors for channels 2, 3, 6, and 7 are located on the long sides of the board, while the vertical output connectors for channels 0, 1, 4, and 5 are placed diagonally around the TCA9548ARGER, in the center of the board. The channel number of each output connector is printed on the board next to it.

The orientation, location, and function of each connector are summarized in the following table:

| **Connector** | **Orientation** |         **Location**         |              **Function**             |
|:-------------:|:---------------:|:----------------------------:|:-------------------------------------:|
|   Input (2)   |    Horizontal   |          Short sides         | Connection to the main Modulino chain |
|     Output    |    Horizontal   |          Long sides          |        Channels 2, 3, 6, and 7        |
|     Output    |     Vertical    | Center, around the switch IC |        Channels 0, 1, 4, and 5        |

All Qwiic connectors share the same pin assignment:

| **Pin** |       **Function**      |
|:-------:|:-----------------------:|
|   GND   |          Ground         |
|   3V3   | Power supply (+3.3 VDC) |
|   SDA   |         I²C data        |
|   SCL   |        I²C clock        |

#### Optional Headers (Not Mounted)

The Modulino Hub also includes unpopulated headers for direct access to its signals, plus test points for the main bus (3V3, GND, SDA, and SCL) on the bottom side of the board. The unpopulated headers and their functions are described in the following table:

|  **Header**  | **Pins** | **Function**                                                            |
|:------------:|:--------:|-------------------------------------------------------------------------|
|   Main bus   | SDA, SCL | Direct access to the main I²C bus                                       |
|     Power    | 3V3, GND | +3.3 VDC supply and ground                                              |
| Channels (8) | SDx, SCx | Direct access to the SDA and SCL lines of each output channel           |
|     Reset    | RST, GND | Active-low reset input of the TCA9548ARGER (4.7 kΩ pull-up to +3.3 VDC) |

### Power Specifications

The Modulino Hub is powered at +3.3 VDC through the Qwiic input connectors, as per the Qwiic standard. Its electrical characteristics are listed in the following table:

|   **Parameter**   |    **Condition**    | **Minimum** | **Typical** | **Maximum** | **Unit** |
|:-----------------:|:-------------------:|:-----------:|:-----------:|:-----------:|:--------:|
|   Supply Voltage  |          -          |      -      |     3.3     |      -      |     V    |
| Operating Current | No channel selected |      -      |     1.5     |      -      |    mA    |
| Operating Current |   Channel selected  |      -      |     3.5     |      -      |    mA    |

<Alert type="note">
**The Modulino Hub does not include a voltage regulator.** It is powered by the +3.3 VDC supply from the Qwiic input connectors, and the same supply rail powers all devices connected to its output channels. The host board must therefore provide enough current for the Modulino Hub and every device connected to it.
</Alert>

### Address Configuration

The Modulino Hub's I²C address is set by the three address inputs of the TCA9548ARGER (A0, A1, and A2). Each address input has a pair of solder jumpers on the bottom side of the board: one jumper connects the input to GND (logic low, L), and the other connects it to +3.3 VDC (logic high, H). **By default, all address inputs are connected to GND, which sets the address to `0x70`.**

The solder jumpers associated with each address input are shown in the following table:

| **Address Input** | **Jumper to GND (L)** | **Jumper to +3.3 VDC (H)** |
|:-----------------:|:---------------------:|:--------------------------:|
|        `A0`       |          SJ4          |             SJ1            |
|        `A1`       |          SJ5          |             SJ2            |
|        `A2`       |          SJ6          |             SJ3            |

<Alert type="warning">
Never close both jumpers of the same address input. Doing so creates a short circuit between +3.3 VDC and GND. To set an address input high, first open its GND jumper and then close its +3.3 VDC jumper.
</Alert>

The addresses available on the Modulino Hub are listed in the following table:

| **A2** | **A1** | **A0** |  **I²C Address** |
|:------:|:------:|:------:|:----------------:|
|    L   |    L   |    L   | `0x70` (default) |
|    L   |    L   |    H   |      `0x71`      |
|    L   |    H   |    L   |      `0x72`      |
|    L   |    H   |    H   |      `0x73`      |
|    H   |    L   |    L   |      `0x74`      |
|    H   |    L   |    H   |      `0x75`      |
|    H   |    H   |    L   |      `0x76`      |
|    H   |    H   |    H   |      `0x77`      |

This addressing scheme allows up to eight Modulino Hubs on the same I²C bus, providing up to 64 independent I²C channels. Since the selected channel shares the bus with the Modulino Hub, devices connected to the output channels must not use the address assigned to any Modulino Hub on the bus.

### Block Diagram

![Modulino Hub Block Diagram](assets/Modulino_Hub_Block_Diagram.png)

The host board communicates with the Modulino Hub through the input connectors. The **TCA9548ARGER** connects the main bus to the selected output channel, while the remaining channels remain isolated. Each output channel has its own pull-up resistors.

### Power Tree

![Modulino Hub Power Tree](assets/Modulino_Hub_Power_Tree.png)

The +3.3 VDC rail from the input Qwiic connectors powers the TCA9548ARGER and the power LED, and is distributed directly to the eight output connectors and to the 3V3 pin of the power header, with no regulation stage.

### Schematic

The Modulino Hub uses a simple circuit built around the **TCA9548ARGER** I²C switch, whose main bus connects to the two **input Qwiic connectors** and whose eight channels connect to the **output Qwiic connectors**, each with its own pull-up resistors. Solder jumpers set the address inputs, and the board powers at **+3.3 VDC** through the input Qwiic connectors or the power header.

The full schematic and PCB files are available from the [Modulino Hub page](https://docs.arduino.cc/hardware/modulinos/modulino-hub) on Docs.

## How to Connect

### Basic Connection

![Modulino Hub Connection Guide](assets/hub_connect.gif)

The Modulino Hub requires no configuration when used with its default address. To add it to your project, follow these steps:

1. Connect your Arduino board to one of the Modulino Hub's input Qwiic connectors on the short sides of the board using a Qwiic cable.
2. Connect your Modulino nodes or other I²C devices to any of the eight output Qwiic connectors.
3. Power your Arduino board. The Modulino Hub's green power LED turns on, and the Modulino Hub is ready to use.

Boards with an onboard Qwiic connector, such as the **UNO R4 WiFi**, the **UNO Q**, and the **Nano R4**, connect directly to the Modulino Hub. Boards in the Nano form factor without a Qwiic connector can be mounted on the **Nano Connector Carrier**, which adds Qwiic connectors. Because the two input connectors are wired in parallel, you can place the Modulino Hub anywhere in the Modulino chain, and other Modulino nodes can continue the chain from the second input connector.

Each output channel can also host more than one device, as long as the devices connected to the same channel have different I²C addresses. For example, a Modulino Thermo and a Modulino Movement can share one channel, while a second pair of the same nodes is connected to another channel. All devices connected to the Modulino Hub are powered by the +3.3 VDC supply of the host board; when connecting many devices, verify that the host board can provide the required current, as described in the [Power Specifications](#power-specifications) section.

### Multiple Modulino Hubs

When a project requires more than eight channels, you can connect several Modulino Hubs to the same I²C bus. Each Modulino Hub must have a unique I²C address, configured through its solder jumpers before connecting it. To connect multiple Modulino Hubs, follow these steps:

1. Assign a different address to each Modulino Hub using the solder jumpers on the bottom side of the board, as described in the [Address Configuration](#address-configuration) section.
2. Connect every Modulino Hub to the main bus through its input connectors. Because the input connectors are wired in parallel, you can chain Modulino Hubs one after another using their input connectors.
3. Connect your devices to the output channels of each Modulino Hub.

<Alert type="warning">
Do not connect a Modulino Hub to an output channel of another Modulino Hub. This configuration is not supported by the Modulino library for Arduino. Connect every Modulino Hub directly to the main bus through its input connectors.
</Alert>

## Programming with Arduino

The Modulino Hub is supported by the [Arduino_Modulino](https://github.com/arduino-libraries/Arduino_Modulino) library, which is compatible with the Arduino IDE and the Arduino Cloud Editor. The following examples show how to use the Modulino Hub with Modulino nodes, which select their channel automatically, and with third-party I²C devices, which require manual channel selection.

### Prerequisites

To follow the Arduino examples of this tutorial, you will need the following:

- An Arduino board with an onboard Qwiic connector (**UNO R4 WiFi**, **UNO Q**, or **Nano R4**), or a Nano form factor board mounted on the **Nano Connector Carrier**
- Qwiic cables
- The `Arduino_Modulino` library, installed from the Arduino IDE Library Manager, along with its dependencies. If you use the Arduino Cloud Editor, the library is already available, and no installation is required.

On the UNO R4 WiFi, the UNO Q, and the Nano R4, the Qwiic connector is wired to the secondary I²C interface, and `Modulino.begin()` automatically selects `Wire1`. On any other board, the library defaults to `Wire`. **You do not need to specify the interface in your sketch.**

For detailed instructions on setting up your Arduino environment and installing libraries, refer to the [Getting Started with Modulinos](../how-general) guide.

### Basic Example

The following sketch reads the temperature from two Modulino Thermo nodes connected to channels 0 and 1 of the Modulino Hub. Since both nodes share the same I²C address, they could not be used on the same bus without the Modulino Hub:

```arduino
/**
Basic Example for the Arduino Modulino Hub
Name: modulino_hub_basic.ino
Purpose: This sketch demonstrates how to read two Modulino Thermo
nodes that share the same I2C address by connecting them to
different channels of the Modulino Hub.

@author Arduino Product Experience Team
@version 1.0 20/10/26
*/

#include <Arduino_Modulino.h>

ModulinoHub hub;                      // Create Hub object (default address 0x70)
ModulinoThermo sensor1(hub.port(0));  // Temperature sensor on channel 0
ModulinoThermo sensor2(hub.port(1));  // Temperature sensor on channel 1

void setup() {
  Serial.begin(115200);
  Modulino.begin();

  if (!sensor1.begin()) {
    Serial.println("Sensor 1 not found.");
  }
  if (!sensor2.begin()) {
    Serial.println("Sensor 2 not found.");
  }
}

void loop() {
  Serial.print("Sensor 1 - ");
  Serial.print(sensor1.getTemperature());
  Serial.println(" °C");

  Serial.print("Sensor 2 - ");
  Serial.print(sensor2.getTemperature());
  Serial.println(" °C");

  delay(1000);
}
```

After uploading the sketch, open the Serial Monitor at 115200 baud to see the temperature readings of both sensors.

### Key Functions

The basic example above relies on the following functions of the `Arduino_Modulino` library:

- `Modulino.begin()`: Initializes the Modulino system (uses `Wire1` on boards with an onboard Qwiic connector).
- `ModulinoHub hub;`: Creates the Modulino Hub object with the default address `0x70`. To use a Modulino Hub with a different address, pass the address to its constructor, for example, `ModulinoHub hub(0x71);`.
- `hub.port(n)`: Returns an object that represents channel `n` of the Modulino Hub, which is passed to the constructor of a Modulino node. With this information, the library selects the corresponding channel before each I²C transaction with the node and releases it afterward, so you don't need to select the channel manually.
- `hub.select(n)` and `hub.clear()`: Connect channel `n` to the main bus and disconnect all channels from it, respectively. You only need these functions with third-party devices, as shown in the advanced example.

### Advanced Example - Third-Party I²C Devices

The Modulino Hub is compatible with other I²C devices, not only Modulino nodes. Because third-party libraries are not aware of the Modulino Hub, you must select the channel manually with `select()` before communicating with the device and release it with `clear()` afterward.

The following sketch uses an SSD1306 OLED display (128×64 pixels) connected to channel 0 of the Modulino Hub. It requires the **Adafruit SSD1306** and **Adafruit GFX** libraries, which can be installed from the Library Manager of the Arduino IDE:

```arduino
/**
Third-Party Device Example for the Arduino Modulino Hub
Name: modulino_hub_third_party.ino
Purpose: This sketch demonstrates how to use a third-party I2C
device (an SSD1306 OLED display) connected to a channel of the
Modulino Hub, selecting and releasing the channel manually.

@author Arduino Product Experience Team
@version 1.0 20/10/26
*/

#include <Arduino_Modulino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< Common addresses are 0x3C or 0x3D; check your display module

// On boards where the Qwiic connector uses Wire1 (for example, UNO R4 WiFi), replace &Wire with &Wire1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

ModulinoHub hub;

void setup() {
  Serial.begin(115200);
  
  // Initialize Modulino I2C communication
  Modulino.begin();

  // Route I2C traffic to port 0 on the Modulino Hub
  // Change this if your SSD1306 is connected to a different port
  hub.select(0);

  // Initialize the OLED display
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed. Check connections and port number."));
    while(1); // Don't proceed, loop forever
  }
  
  // Clear the display buffer
  display.clearDisplay();
  
  // Display some text
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println(F("Modulino Hub"));
  display.println(F("Initialization OK!"));
  display.display();
  delay(2000);

  // Clear the hub routing to free the I2C bus for other ports
  hub.clear();
}

void loop() {
  // Before communicating with the 3rd party I2C device again, 
  // you must re-select the port it's connected to.
  hub.select(0);

  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(F("Modulino Hub: Port 0"));
  display.print(F("Uptime: "));
  display.print(millis() / 1000);
  display.println(F(" seconds"));
  display.display();

  // Once communication is finished for this cycle, 
  // clear the hub's port selection.
  hub.clear();

  delay(1000);
}
```

The `hub.select(0)` call connects channel 0 to the main bus, so the display library can communicate with the display as if it were connected directly to the board. After each communication cycle, `hub.clear()` disconnects all channels from the main bus. Operations that only modify the display buffer do not require I²C communication, but `display.begin()` and `display.display()` do, so they must always run while the channel is selected.

<Alert type="warning">
On the UNO R4 WiFi, Nano R4, UNO Q, and VENTUNO Q boards, the Qwiic connector is connected to the `Wire1` I²C interface, which `Modulino.begin()` uses by default on these boards. When using a third-party library on these boards, pass `Wire1` to it instead of `Wire`; otherwise, the library communicates through a different I²C interface than the Modulino Hub.
</Alert>

When combining Modulino nodes and third-party devices in the same project, always call `hub.clear()` after communicating with a third-party device. A channel that remains selected stays connected to the main bus, and its devices can conflict with devices in the main Modulino chain that share the same address.

## Programming with MicroPython

The [Modulino MicroPython package](https://github.com/arduino/arduino-modulino-mpy) supports the Modulino Hub. The following examples show how to use the Modulino Hub with Modulino nodes and third-party I²C devices.

### Prerequisites

To follow the MicroPython examples of this tutorial, you will need the following:

- An Arduino board that officially supports MicroPython, such as the **Nano ESP32**, **Nano RP2040 Connect**, **Nano 33 BLE Sense**, **GIGA R1 WiFi**, or **Portenta H7**. Mount a Nano form-factor board on the **Nano Connector Carrier** to connect the Modulino Hub through Qwiic.
- Qwiic cables
- The Modulino MicroPython package, installed with the [Arduino MicroPython Package Installer](https://labs.arduino.cc/en/labs/micropython-package-installer) by searching for **Modulino**, or from a terminal with `mpremote` and `mip`:

  ```bash
  mpremote mip install github:arduino/arduino-modulino-mpy
  ```

- Arduino Lab for MicroPython, to run the scripts on the board

On Arduino boards, the package detects the correct I²C interface automatically, so `ModulinoHub()` needs no arguments. For detailed instructions, refer to the [Getting Started with Modulinos](../how-general) guide.

### Basic Example

The following script reads the temperature and relative humidity from two Modulino Thermo nodes connected to channels 0 and 1 of the Modulino Hub:

```python
"""
Basic Example for the Arduino Modulino Hub
Name: modulino_hub_basic.py
Purpose: This script demonstrates how to read two Modulino Thermo
nodes that share the same I2C address by connecting them to
different channels of the Modulino Hub.

@author Arduino Product Experience Team
@version 1.0 20/10/26
"""

import time
from modulino import ModulinoHub, ModulinoThermo

print("Initializing Modulino Hub...")
hub = ModulinoHub()

# Initialize each Modulino Thermo with the Hub port it is connected to.
# The library selects the port automatically whenever it communicates with the sensor.
thermo_a = ModulinoThermo(hub_port=hub.get_port(0))
thermo_b = ModulinoThermo(hub_port=hub.get_port(1))

# Wait a moment for the sensor to be ready after being connected to the bus
time.sleep(0.1)

print("Starting continuous temperature and humidity readings...\n")

def print_sensor_data(sensor, port):
    data = sensor.measurements
    temp = data.temperature
    hum = data.relative_humidity
    
    if temp is not None and hum is not None:
        print(f"Port {port}: Temperature: {temp:.2f} °C, Humidity: {hum:.2f} %")
    else:
        print(f"Port {port}: Failed to read data from the sensor.")

while True:
    try:
        print_sensor_data(thermo_a, 0)
        print_sensor_data(thermo_b, 1)    
    except OSError as e:
        print(f"I2C Communication error: {e}")
        
    time.sleep(1)
```

### Key Methods

The basic example above relies on the following methods of the `ModulinoHub` class:

- `ModulinoHub()`: Creates the Modulino Hub object with the default address `0x70`. To use a Modulino Hub with a different address, pass the address to its constructor, for example, `hub = ModulinoHub(address=0x71)`.
- `.get_port(n)`: Returns an object that represents channel `n` of the Modulino Hub, which is passed to each Modulino node through the `hub_port` parameter. The library then selects the corresponding channel before each I²C transaction with the node and releases it afterward, so no manual channel selection is required.
- `.i2c_bus`: Exposes the underlying I²C bus, which is needed to initialize third-party drivers, as shown in the advanced example.

### Differences From the Arduino Library

The MicroPython implementation follows the same model as the Arduino one, with a few differences in how it refers to and selects channels. The following table summarizes them:

|       **Aspect**       |          **Arduino**          |            **MicroPython**           |
|:----------------------:|:-----------------------------:|:------------------------------------:|
|     Channel object     |        `hub.port(n)`          |          `hub.get_port(n)`           |
|   Passing the channel  | Constructor argument of the node | `hub_port` keyword argument of the node |
| Manual channel selection | `hub.select(n)` / `hub.clear()` | `with port:` context manager        |
|  Access to the I²C bus |      Not exposed              |            `hub.i2c_bus`             |

### Advanced Example - Third-Party I²C Devices

As with Arduino, third-party libraries are not aware of the Modulino Hub, so you must select the channel manually. In MicroPython, do this with the port object as a context manager: every I²C operation inside a `with port:` block runs with the channel selected, and the channel is released automatically when the block ends.

The following script uses an SSD1306 OLED display (128×64 pixels) connected to channel 3 of the Modulino Hub. It requires the `ssd1306` driver from the official MicroPython library, which can be installed with the Arduino MicroPython Package Installer by searching for **ssd1306**, or from a terminal with the following command:

```bash
mpremote mip install ssd1306
```

The driver uses the I²C address `0x3C` by default. If your display uses a different address, pass it with the `addr` parameter, for example, `ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D)`. The complete script is shown below:

```python
"""
Third-Party Device Example for the Arduino Modulino Hub
Name: modulino_hub_third_party.py
Purpose: This script demonstrates how to use a third-party I2C
device (an SSD1306 OLED display) connected to a channel of the
Modulino Hub, selecting the channel with a context manager.

@author Arduino Product Experience Team
@version 1.0 20/10/26
"""

import time
import ssd1306
from modulino import ModulinoHub

print("Initializing Modulino Hub...")
hub = ModulinoHub()

# The Modulino instance exposes the underlying I2C bus as `i2c_bus`
i2c = hub.i2c_bus

print("Initializing SSD1306 on Port 3...")
# Retrieve the Port object for the port where the 3rd party module is connected.
port = hub.get_port(3)

# Any I2C initialization needs to be surrounded by a "with" statement using the Port object.
with port:
    # Initialize the SSD1306 OLED display (128x64 resolution is common)
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    
    # We can perform the first operations inside the context
    display.fill(0)
    display.text("Hello Modulino!", 0, 0)
    display.show()

counter = 0

while True:
    try:
        # Buffer operations (like fill, text) don't require I2C communication,
        # so they can safely run outside the with block.
        display.fill(0)
        display.text(f"Count: {counter}", 0, 20)
        
        # We need to use the `with` statement whenever actual I2C transmission happens,
        # which is exactly what display.show() does when pushing the buffer.
        with port:
            display.show()
            
        counter += 1
    except OSError as e:
        print(f"I2C Communication error: {e}")
        
    time.sleep(1)
```

The display driver uses the same I²C bus as the Modulino Hub, obtained through `hub.i2c_bus`. On Arduino boards, the package automatically detects the Qwiic connector's I²C interface, so no additional configuration is required to select the correct interface.

## Troubleshooting

### Modulino Hub Not Responding

If the Modulino Hub is not detected on the I²C bus, first verify that the green power LED is on. If the LED is off, check that the Qwiic cable is firmly connected to an input connector and that the host board is powered.

If the LED is on, confirm that the address used in your code matches the address configured on the Modulino Hub. The default address is `0x70`; if the solder jumpers were modified, pass the configured address to the `ModulinoHub` constructor. Also verify that no address input has both of its jumpers closed, as described in the [Address Configuration](#address-configuration) section.

To confirm the Modulino Hub address, scan the I²C bus. In MicroPython, call `hub.i2c_bus.scan()`, which returns the addresses of all devices detected on the main bus. In Arduino, use an I²C scanner sketch on the I²C interface of the Qwiic connector (`Wire1` on the UNO R4 WiFi, Nano R4, UNO Q, and VENTUNO Q boards).

### Devices on Channels Not Responding

If the devices connected to the output channels are not responding, verify that they are connected to output connectors, not input connectors. Then check that the channel number used in your code matches the channel number printed next to the connector on the board.

For third-party devices, confirm that the channel is selected before communicating with the device: with `hub.select()` in Arduino, or inside a `with port:` block in MicroPython. In Arduino, also verify that the third-party library uses the same I²C interface as the Modulino Hub, as described in the [Advanced Example](#advanced-example---third-party-i²c-devices) of the Arduino section.

If several devices share the same channel, verify that each has a different I²C address and that none uses the address of a Modulino Hub on the bus. Finally, if a device still does not respond, connect it directly to the host board, without the Modulino Hub, to confirm that the device itself works correctly.

### Address Conflicts with Multiple Modulino Hubs

If you experience issues when using multiple Modulino Hubs, verify that each Modulino Hub has a unique address configured through its solder jumpers and that each `ModulinoHub` object in your code uses the address of the corresponding Modulino Hub. Scanning the I²C bus should show each Modulino Hub at its configured address, in the range from `0x70` to `0x77`.

### Communication Errors

If I²C communication errors occur, verify that your code releases the selected channel with `hub.clear()` in Arduino, or by exiting the `with port:` block in MicroPython, after communicating with third-party devices. A channel that remains selected stays connected to the main bus and can interfere with communication with other devices.

Long cables increase bus capacitance and can cause communication errors, so use the shortest practical Qwiic cables, especially on the main bus. Also verify that the host board can supply the current required by the Modulino Hub and all connected devices, as described in the [Power Specifications](#power-specifications) section.

Since the Modulino Hub does not include pull-up resistors on the main bus, communication on the main bus depends on the pull-up resistors on the host board and other devices in the Modulino chain. If the Modulino Hub is connected to a board without pull-up resistors on its I²C lines, for example, through a Qwiic-to-header cable, add external pull-up resistors to the main bus.

### Library Issues

See the [Getting Started with Modulinos](../how-general) guide for library installation troubleshooting.

## Project Ideas

Now that you are familiar with the Modulino Hub, you can use it in projects such as the following:

- **Multi-point temperature monitor**: Read several Modulino Thermo nodes placed in different locations, as shown in the basic examples
- **Mixed-device dashboard**: Combine Modulino nodes with a third-party OLED display to show readings locally
- **Organized sensor network**: Group the devices of a larger project by function, with each group on its own channel
- **Expanded I²C network**: Connect multiple Modulino Hubs to the same bus to reach up to 64 independent channels
- **Long-distance segments**: Combine the Modulino Hub with a Modulino Extender to place each channel over its own cable run

## Conclusion

In this tutorial, you learned how the Modulino Hub uses the TCA9548ARGER I²C switch to provide eight independent I²C channels, how to connect it to your Arduino board and to other devices, and how to configure its address to use multiple Modulino Hubs on the same bus. You also learned how to program it with both the Arduino and MicroPython libraries, using Modulino nodes, which select their channel automatically, and third-party I²C devices, which require manual channel selection.

For more information, refer to the following resources:

- [Modulino Hub page](https://docs.arduino.cc/hardware/modulinos/modulino-hub), with the datasheet, the schematic, and the pinout
- [Arduino_Modulino library](https://github.com/arduino-libraries/Arduino_Modulino)
- [Modulino MicroPython package](https://github.com/arduino/arduino-modulino-mpy)