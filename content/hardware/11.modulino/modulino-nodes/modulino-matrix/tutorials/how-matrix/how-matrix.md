---
title: "Getting Started with Modulino Matrix"
description: "Complete guide for the Modulino LED Matrix display module and how to program it with Arduino and MicroPython."
tags:
 - Modulino
 - LED Matrix
 - Display
 - Graphics
 - QWIIC
 - I2C
author: 'Pedro Sousa Lima'
hardware:
 - hardware/11.modulinos/modulinos/modulino-matrix
software:
 - ide-v2
 - web-editor
 - micropython
---

![Matrix Overview](assets/MatrixOverview.png)

The Modulino LED Matrix is a modular display featuring an 8×12 LED matrix (96 LEDs total) for displaying text, graphics, and animations, making it perfect to add visual feedback to your projects! It uses the standardised Modulino form factor with QWIIC connectors for easy integration.

## Hardware Overview

### General Characteristics

The Modulino LED Matrix features 96 individually controllable LEDs arranged in an 8×12 matrix:

| Parameter    | Condition | Minimum | Typical | Maximum | Unit |
|--------------|-----------|---------|---------|---------|------|
| Matrix Size  | -         | -       | 8×12    | -       | LEDs |
| Total LEDs   | -         | -       | 96      | -       | -    |
| Resolution   | Rows      | -       | 8       | -       | -    |
| Resolution   | Columns   | -       | 12      | -       | -    |
| Current      | All LEDs  | -       | -       | 200     | mA   |

### Device Details

The **Modulino LED Matrix** module uses an 8×12 LED matrix controlled via charlieplexing technology. The LEDs do not have native I²C capabilities. Instead, the matrix is driven by the Modulino's onboard microcontroller (STM32C011F4), which handles the complex timing required for charlieplexing and provides I²C communication.

The display provides the same functionality as the Arduino® UNO R4 WiFi LED matrix, ensuring code compatibility.

One unique feature of this setup is the ability to change the I²C address via software, making it adaptable to different system configurations.

The default I²C address for the **Modulino LED Matrix** module is:

| Modulino I²C Address | Hardware I²C Address | Editable Addresses (HEX)                        |
|----------------------|----------------------|-------------------------------------------------|
| 0x32                 | 0x19                 | Any custom address (via software configuration) |

### Pinout

![Modulino LED Matrix Pinout](assets/MatrixPinouts.png)

**Qwiic / I2C (1×4 Header)**

| **Pin** | **Function**         |
|---------|----------------------|
| GND     | Ground               |
| 3.3 V   | Power Supply (3.3 V) |
| SDA     | I2C Data             |
| SCL     | I2C Clock            |

These pads and the Qwiic connectors share the same I2C bus at 3.3 V.

**Additional 1×6 Header (Debug & Power)**

| **Pin** | **Function**     |
|---------|------------------|
| GND     | Ground           |
| 3V3     | 3.3 V Power      |
| PF2     | RESET (NRST)     |
| SWCLK   | SWD Clock (PA14) |
| SWDIO   | SWD Data (PA13)  |
| GND     | Ground           |

**Note:** The LED matrix is controlled by pins PA0, PA1, PA2, PA3, PA4, PA5, PA6, PA7, PA8, PA11, and PA12 using charlieplexing. Due to space constraints on the specialised PCB, only the RESET strap is populated.

### Power Specifications

| Parameter           | Condition        | Typical | Unit |
|---------------------|------------------|---------|------|
| Operating Voltage   | -                | 3.3     | V    |
| Current Consumption | Idle             | ~3.4    | mA   |
| Current Consumption | LEDs Illuminated | Variable| mA   |
| Current Consumption | Peak (All LEDs)  | 200     | mA   |

The module includes a power LED that draws 1 mA and turns on as soon as it is powered.

### Schematic

The Modulino LED Matrix features a specialised 4-layer PCB design for controlling 96 LEDs efficiently.

The main components are the 8×12 LED matrix and the **STM32C011F4** microcontroller (U1), which handles charlieplexing control and I²C communication.

You can connect to the I²C pins (SDA and SCL) using either the **QWIIC connectors** (J1 and J2, this is the recommended method) or the **solderable pins** (J4). The board runs on **3.3V**, which comes from the QWIIC cable or the **3V3 pin** on J4.

There's also a small power LED indicator that lights up when the board is on.

You can grab the full schematic and PCB files from the [Modulino Matrix page](https://docs.arduino.cc/hardware/modulino-matrix/).

## Programming with Arduino

The Modulino LED Matrix is fully compatible with the Arduino IDE and the official Modulino library. The following examples showcase how to display text, graphics, and animations on your LED matrix.

### Prerequisites

- Install the Modulino library via the Arduino IDE Library Manager
- Connect your Modulino LED Matrix via QWIIC or solderable headers

For detailed instructions on setting up your Arduino environment and installing libraries, please refer to the [Getting Started with Modulinos guide](../how-general).

Library repository available [here](https://github.com/arduino-libraries/Arduino_Modulino).

### Basic Example

```arduino
/**
 * This example shows how to use the Modulino LED Matrix library to display
 * basic graphics and animations on the Modulino LED Matrix display.
 *
 * Initial author: Sebastian Romero
 */

#include "Modulino_LED_Matrix.h"
#include "LEDMatrixGallery.h" // This header contains predefined animations for the LED matrix display.

ModulinoLEDMatrix matrix;

void setup() {
  if (!matrix.begin()) {
    // If initialization fails, we enter an infinite loop and
    // blink the built-in LED to indicate an error.
    while (true){
      digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN)); // Blink built-in LED to indicate error
      delay(500);
    }
  }
}

void loop() {
  // Play startup animation from gallery
  matrix.setSequence(LEDMATRIX_ANIMATION_STARTUP);
  matrix.play();
  delay(500);

  // Show the UNO icon from the gallery
  matrix.setFrame(LEDMATRIX_UNO);
  delay(1000);

  // Clear the display
  matrix.clear();
  delay(500);
}
```

### Key Functions

- `begin()`: Initializes I2C communication with the LED Matrix (returns 1 on success)
- `setFrame(buffer)`: Displays a single frame on the matrix (accepts predefined icons or custom data)
- `setSequence(frames)`: Loads an animation sequence into the matrix
- `play(looping)`: Plays the loaded animation sequence (blocking, optional looping parameter)
- `nextFrame()`: Advances to the next frame in a sequence (non-blocking)
- `clear()`: Turns off all LEDs
- `setMode(DisplayMode)`: Sets the display mode (MonochromaticVertical, MonochromaticHorizontal, or Grayscale)

### Advanced Example - Graphics Drawing

This example demonstrates how to use the ArduinoGraphics library integration to draw shapes, lines, and patterns on the LED matrix.

```arduino
/*
* This example shows how to use the Modulino LED Matrix library to display
* basic shapes using the ArduinoGraphics library.
* The sketch cycles through displaying a point, a line, a rectangle, and a circle on the LED matrix.
*
* Initial author: Sebastian Romero
*/

#include "ArduinoGraphics.h"
#include "Modulino_LED_Matrix.h"

ModulinoLEDMatrix matrix;

void setup() {
  // Initialize the LED matrix
  if (!matrix.begin()) {
    // If initialization fails, we enter an infinite loop and
    // blink the built-in LED to indicate an error.
    while (true){
      digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN)); // Blink built-in LED to indicate error
      delay(500);
    }
  }
}

void loop() {
  // Draw a Point
  matrix.clear();
  matrix.beginDraw();
  matrix.stroke(0xFFFFFF); // Set color to white (ON)
  matrix.point(5, 4);      // Draw a point at x=5, y=4
  matrix.endDraw();
  delay(2000);

  // Draw a Line
  matrix.clear();
  matrix.beginDraw();
  matrix.stroke(0xFFFFFF);
  matrix.line(0, 0, 11, 7); // Draw a line from (0,0) to (11,7)
  matrix.endDraw();
  delay(2000);

  // Draw a Rectangle (outlined)
  matrix.clear();
  matrix.beginDraw();
  matrix.stroke(0xFFFFFF);
  matrix.noFill();
  // Rect parameters: x, y, width, height
  matrix.rect(2, 1, 8, 6);
  matrix.endDraw();
  delay(2000);

  // Draw a Circle
  matrix.clear();
  matrix.beginDraw();
  matrix.stroke(0xFFFFFF);
  matrix.noFill();
  // Circle parameters: x, y, radius
  matrix.circle(6, 4, 3);
  matrix.endDraw();
  delay(2000);

  // Draw a Filled Rectangle
  matrix.clear();
  matrix.beginDraw();
  matrix.stroke(0xFFFFFF);
  matrix.fill(0xFFFFFF); // Enable fill
  matrix.rect(3, 2, 6, 4);
  matrix.endDraw();
  delay(2000);
}
```

### Advanced Feature - Grayscale Display

The Modulino LED Matrix supports **4-bit grayscale rendering**, allowing you to display images and animations with 16 different intensity levels (0-15) per pixel. This feature is perfect for creating smooth gradients, realistic animations, and detailed graphics.

#### Understanding Grayscale Mode

In grayscale mode, each pixel can have a brightness value from 0 (off) to 15 (maximum brightness). The frame data is packed efficiently: each byte contains two pixels (4 bits each).

**Frame Data Format:**
- Total pixels: 96 (8 rows × 12 columns)
- Frame buffer size: 48 bytes (96 pixels ÷ 2 pixels per byte)
- Byte format: `0xAB` where A is the first pixel (0-15), B is the second pixel (0-15)

#### Display Modes

The LED Matrix supports three display modes:

- `DisplayMode::Grayscale` - 4-bit grayscale (16 intensity levels)
- `DisplayMode::MonochromaticHorizontal` - Row-major monochromatic (on/off only)
- `DisplayMode::MonochromaticVertical` - Column-major monochromatic (on/off only)

#### Grayscale Example

```arduino
/**
 * This example shows how to use the Modulino LED Matrix library to display
 * grayscale graphics and animations on the Modulino LED Matrix display.
 *
 * Initial author: Sebastian Romero
 */

#include "Modulino_LED_Matrix.h"
#include "flames_animation.h"

/* Graphic in 4-bit grayscale */
constexpr uint8_t GRADIENT[] = { 	0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0x01, 0x23, 0x45, 0x67,
									0x89, 0xAB, 0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0x01, 0x23,
									0x45, 0x67, 0x89, 0xAB, 0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0x01, 0x23, 0x45, 0x67, 0x89, 0xAB};

ModulinoLEDMatrix matrix;

/**
 * Blinks the built-in LED to signal that the animation sequence is done.
 */
void blinkLED(){
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  if (!matrix.begin()) {
    // If initialization fails, we enter an infinite loop and
    // blink the built-in LED to indicate an error.
    while (true){
      digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN)); // Blink built-in LED to indicate error
      delay(500);
    }
  }

  // Set a callback to be called when the sequence is done
  matrix.setSequenceDoneCallback(blinkLED);

  // Set the display to Grayscale mode and show a gradient
  matrix.setMode(DisplayMode::Grayscale);
  matrix.setFrame(GRADIENT);
  delay(1000);

  // Play a grayscale animation in a loop
  matrix.setSequence(FLAMES);
  matrix.play(true);
}

void loop() {
}
```

**Note:** You can create custom grayscale animations using image editing software and convert them to the appropriate format. Each frame should be 48 bytes (96 pixels packed as 4-bit values).

## Programming with MicroPython

The Modulino LED Matrix is fully compatible with MicroPython through the official Modulino MicroPython library. The following examples demonstrate how to create visual displays, graphics, and animations in your MicroPython projects.

### Prerequisites

- Install the Modulino MicroPython library (see [Getting Started with Modulinos](./how-general) for detailed instructions)
- Ensure Arduino Lab for MicroPython is installed

Library repository available [here](https://github.com/arduino/arduino-modulino-mpy).

### Basic Example

```python
"""
This example demonstrates how to use the Modulino LED Matrix module.
It shows how to set and unset individual pixels, draw shapes, display text, frames,
and run a simple Matrix-style rain animation.

Initial author: Sebastian Romero
"""

from modulino import ModulinoLEDMatrix
from time import sleep_ms

led_matrix = ModulinoLEDMatrix()
led_matrix.clear().show()

def fill_pixels(matrix: ModulinoLEDMatrix):
    # Set all pixels one by one
    for y in range(8):
        for x in range(12):
            matrix.set_pixel(x, y)
            matrix.show()
            sleep_ms(10)

def unfill_pixels(matrix: ModulinoLEDMatrix):
    # Unset all pixels in reverse order
    for y in range(7, -1, -1):
        for x in range(11, -1, -1):
            matrix.set_pixel(x, y, False)
            matrix.show()
            sleep_ms(10)

def draw_spiral(matrix: ModulinoLEDMatrix):
    # Spiral pattern
    for layer in range(6):
        for x in range(layer, 12 - layer):
            matrix.set_pixel(x, layer)
            matrix.show()
            sleep_ms(10)
        for y in range(layer + 1, 8 - layer):
            matrix.set_pixel(11 - layer, y)
            matrix.show()
            sleep_ms(10)
        for x in range(11 - layer - 1, layer - 1, -1):
            matrix.set_pixel(x, 7 - layer)
            matrix.show()
            sleep_ms(10)
        for y in range(7 - layer - 1, layer, -1):
            matrix.set_pixel(layer, y)
            matrix.show()
            sleep_ms(10)

def draw_squares(matrix: ModulinoLEDMatrix):
    # Draw small squares and circles
    for i in range(4):
        matrix.rect(i, i, 12 - 2 * i, 8 - 2 * i).show()
        sleep_ms(500)
        matrix.clear()

def draw_circles(matrix: ModulinoLEDMatrix):
    for i in range(4):
        matrix.ellipse(6, 3, 3 - i, 3 - i).show()
        sleep_ms(500)
        matrix.clear()

def display_text_animation(matrix: ModulinoLEDMatrix):
    """Display a simple text animation."""
    for c in "ARDUINO IS":
        matrix.clear()
        matrix.text(2, 0, c).show()
        sleep_ms(250)

def display_ascii_frame(matrix: ModulinoLEDMatrix):
    """Display a simple ASCII art frame."""
    heart_frame = """
    ............
    ..##....##..
    .##########.
    .##########.
    ..########..
    ...######...
    ....####....
    .....##.....
    """
    matrix.clear()
    matrix.set_frame_from_ascii(heart_frame).show()

def raining_code(matrix: ModulinoLEDMatrix, steps: int = 300, spawn_chance: int = 35, delay_ms: int = 70):
    """Play a brief Matrix-style rain animation."""
    from random import getrandbits

    def _randint(n: int) -> int:
        """Small helper to avoid importing full random."""
        return getrandbits(16) % n

    drops = []  # each drop: (x, head_y, length)

    for _ in range(steps):
        # Maybe spawn a new drop at the top
        if _randint(100) < spawn_chance:
            x = _randint(12)
            length = 2 + _randint(4)  # 2..5 pixels long
            drops.append([x, -1, length])

        matrix.clear()

        active = []
        for x, head_y, length in drops:
            head_y += 1
            tail_y = head_y - length

            # Draw the drop from head down to tail within bounds
            for y in range(max(0, tail_y), min(matrix._height, head_y + 1)):
                matrix.set_pixel(x, y, True)

            # Keep drop if it still intersects the display
            if tail_y < matrix._height:
                active.append([x, head_y, length])

        drops = active
        matrix.show()
        sleep_ms(delay_ms)

def draw_checkerboard(matrix: ModulinoLEDMatrix):
    """Draw a checkerboard pattern using hline and vline."""
    for y in range(8):
        if y % 2 == 0:
            matrix.hline(0, y, 12, True)
    for x in range(12):
        if x % 2 == 0:
            matrix.vline(x, 0, 8, True)

    matrix.show()
def draw_diamond(matrix: ModulinoLEDMatrix):
    """Draw a diamond shape using poly()."""
    points = [(6, 0), (11, 3), (6, 7), (1, 3)]
    matrix.poly(0,0,points).show()


# Run the animations sequentially
fill_pixels(led_matrix)
sleep_ms(500)
unfill_pixels(led_matrix)
sleep_ms(500)
draw_spiral(led_matrix)
sleep_ms(500)
draw_squares(led_matrix)
sleep_ms(500)
draw_circles(led_matrix)
sleep_ms(500)
draw_checkerboard(led_matrix)
sleep_ms(500)
draw_diamond(led_matrix)
sleep_ms(1000)
display_text_animation(led_matrix)
sleep_ms(500)
display_ascii_frame(led_matrix)
sleep_ms(500)
raining_code(led_matrix)
led_matrix.clear().show()
```

### Key Methods

**Initialization:**
- `ModulinoLEDMatrix()`: Creates LED Matrix instance (default address)
- `ModulinoLEDMatrix(address=0x39)`: Creates instance with custom I2C address
- `ModulinoLEDMatrix(use_grayscale=True)`: Enable 16-level grayscale mode

**Drawing Methods:**
- `.set_pixel(x, y, color)`: Set individual pixel (x: 0-11, y: 0-7)
- `.clear_pixel(x, y)`: Turn off a specific pixel
- `.clear()`: Turn off all pixels
- `.fill(color)`: Fill entire matrix with color
- `.hline(x, y, length, color)`: Draw horizontal line
- `.vline(x, y, length, color)`: Draw vertical line
- `.line(x1, y1, x2, y2, color)`: Draw line between two points
- `.rect(x, y, width, height, color)`: Draw rectangle outline
- `.ellipse(x, y, width, height, color)`: Draw ellipse
- `.text(x, y, string, color)`: Display text
- `.show()`: Update the display with current buffer

**Frame Operations:**
- `.set_frame(data)`: Load frame from bytes/bytearray
- `.set_frame_from_ascii(ascii_art, fill_char='#')`: Create frame from ASCII art

### Advanced Example - Animations

This example demonstrates how to create a simple animation on the Modulino LED Matrix by cycling through a series of pre-defined frames with specific durations.

```python
"""
This example demonstrates how to create a simple animation on the Modulino LED Matrix
by cycling through a series of pre-defined frames with specific durations.

Initial author: Sebastian Romero
"""

from modulino import ModulinoLEDMatrix, Animation

led_matrix = ModulinoLEDMatrix(use_grayscale=False)
led_matrix.clear().show()

frames = [
    (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 66),
    (b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00', 66),
    (b'\x00\x00\x00\x20\x10\x00\x00\x00\x00\x00\x00\x00', 40),
    (b'\x00\x00\x20\x20\x10\x00\x00\x00\x00\x00\x00\x00', 40),
    (b'\x00\x20\x20\x20\x10\x00\x00\x00\x00\x00\x00\x00', 40),
    (b'\x10\x20\x20\x20\x10\x00\x00\x00\x00\x00\x00\x00', 40),
    (b'\x18\x20\x20\x20\x10\x00\x00\x00\x00\x00\x00\x00', 40),
    (b'\x1c\x20\x20\x20\x10\x00\x00\x00\x00\x00\x00\x00', 40),
    (b'\x1c\x22\x20\x20\x10\x00\x00\x00\x00\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x20\x10\x00\x00\x00\x00\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x10\x00\x00\x00\x00\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x14\x00\x00\x00\x00\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x14\x08\x00\x00\x00\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x00\x00\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x00\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x20\x00\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x20\x20\x00\x00', 30),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x20\x20\x10\x00', 40),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x20\x20\x18\x00', 40),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x20\x20\x1c\x00', 40),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x20\x22\x1c\x00', 40),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x20\x22\x22\x1c\x00', 40),
    (b'\x1c\x22\x22\x22\x14\x08\x10\x22\x22\x22\x1c\x00', 66),
    (b'\x1c\x22\x22\x22\x14\x08\x14\x22\x22\x22\x1c\x00', 240),
    (b'\x1c\x22\x32\x22\x14\x08\x14\x22\x26\x22\x1c\x02', 66),
    (b'\x1c\x22\x2a\x22\x14\x08\x14\x22\x2a\x22\x1c\x01', 400),
    (b'\x22\x2a\x22\x14\x08\x14\x22\x2a\x22\x1c\x01\x00', 66),
    (b'\x2a\x22\x14\x08\x14\x22\x2a\x22\x1c\x01\x00\x3c', 66),
    (b'\x22\x14\x08\x14\x22\x2a\x22\x1c\x01\x00\x3c\x0a', 66),
    (b'\x14\x08\x14\x22\x2a\x22\x1c\x01\x00\x3c\x0a\x0a', 66),
    (b'\x08\x14\x22\x2a\x22\x1c\x01\x00\x3c\x0a\x0a\x3c', 66),
    (b'\x14\x22\x2a\x22\x1c\x01\x00\x3c\x0a\x0a\x3c\x00', 66),
    (b'\x22\x2a\x22\x1c\x01\x00\x3c\x0a\x0a\x3c\x00\x3e', 66),
    (b'\x2a\x22\x1c\x01\x00\x3c\x0a\x0a\x3c\x00\x3e\x0a', 66),
    (b'\x22\x1c\x01\x00\x3c\x0a\x0a\x3c\x00\x3e\x0a\x0a', 66),
    (b'\x1c\x01\x00\x3c\x0a\x0a\x3c\x00\x3e\x0a\x0a\x34', 66),
    (b'\x01\x00\x3c\x0a\x0a\x3c\x00\x3e\x0a\x0a\x34\x00', 66),
    (b'\x00\x3c\x0a\x0a\x3c\x00\x3e\x0a\x0a\x34\x00\x3e', 100),
    (b'\x3c\x0a\x0a\x3c\x00\x3e\x0a\x0a\x34\x00\x3e\x22', 66),
    (b'\x0a\x0a\x3c\x00\x3e\x0a\x0a\x34\x00\x3e\x22\x22', 66),
    (b'\x0a\x3c\x00\x3e\x0a\x0a\x34\x00\x3e\x22\x22\x1c', 66),
    (b'\x3c\x00\x3e\x0a\x0a\x34\x00\x3e\x22\x22\x1c\x00', 66),
    (b'\x00\x3e\x0a\x0a\x34\x00\x3e\x22\x22\x1c\x00\x1e', 66),
    (b'\x3e\x0a\x0a\x34\x00\x3e\x22\x22\x1c\x00\x1e\x20', 66),
    (b'\x0a\x0a\x34\x00\x3e\x22\x22\x1c\x00\x1e\x20\x20', 66),
    (b'\x0a\x34\x00\x3e\x22\x22\x1c\x00\x1e\x20\x20\x1e', 66),
    (b'\x34\x00\x3e\x22\x22\x1c\x00\x1e\x20\x20\x1e\x00', 66),
    (b'\x00\x3e\x22\x22\x1c\x00\x1e\x20\x20\x1e\x00\x22', 66),
    (b'\x3e\x22\x22\x1c\x00\x1e\x20\x20\x1e\x00\x22\x3e', 66),
    (b'\x22\x22\x1c\x00\x1e\x20\x20\x1e\x00\x22\x3e\x22', 66),
    (b'\x22\x1c\x00\x1e\x20\x20\x1e\x00\x22\x3e\x22\x00', 66),
    (b'\x1c\x00\x1e\x20\x20\x1e\x00\x22\x3e\x22\x00\x3e', 66),
    (b'\x00\x1e\x20\x20\x1e\x00\x22\x3e\x22\x00\x3e\x04', 66),
    (b'\x1e\x20\x20\x1e\x00\x22\x3e\x22\x00\x3e\x04\x08', 66),
    (b'\x20\x20\x1e\x00\x22\x3e\x22\x00\x3e\x04\x08\x3e', 66),
    (b'\x20\x1e\x00\x22\x3e\x22\x00\x3e\x04\x08\x3e\x00', 66),
    (b'\x1e\x00\x22\x3e\x22\x00\x3e\x04\x08\x3e\x00\x1c', 66),
    (b'\x00\x22\x3e\x22\x00\x3e\x04\x08\x3e\x00\x1c\x22', 66),
    (b'\x22\x3e\x22\x00\x3e\x04\x08\x3e\x00\x1c\x22\x22', 66),
    (b'\x3e\x22\x00\x3e\x04\x08\x3e\x00\x1c\x22\x22\x1c', 66),
    (b'\x22\x00\x3e\x04\x08\x3e\x00\x1c\x22\x22\x1c\x00', 66),
    (b'\x00\x3e\x04\x08\x3e\x00\x1c\x22\x22\x1c\x00\x00', 66),
    (b'\x3e\x04\x08\x3e\x00\x1c\x22\x22\x1c\x00\x00\x00', 66),
    (b'\x04\x08\x3e\x00\x1c\x22\x22\x1c\x00\x00\x00\x00', 66),
    (b'\x08\x3e\x00\x1c\x22\x22\x1c\x00\x00\x00\x00\x00', 66),
    (b'\x3e\x00\x1c\x22\x22\x1c\x00\x00\x00\x00\x00\x00', 66),
    (b'\x00\x1c\x22\x22\x1c\x00\x00\x00\x00\x00\x00\x00', 66),
    (b'\x1c\x22\x22\x1c\x00\x00\x00\x00\x00\x00\x00\x00', 66),
    (b'\x22\x22\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00', 66),
    (b'\x22\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 66),
    (b'\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 66),
    (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 66),
]

print(f"Playing animation with {len(frames)} frames. {len(frames)*len(frames[0]):,} bytes in total.")
print("Press Ctrl+C to stop.")

try:
    animation = Animation(led_matrix, frames)
    animation.play(loop=True)

except KeyboardInterrupt:
    print("Animation stopped by user.")
    led_matrix.clear().show()
```

### Advanced Example - Grayscale Mode

```python
from modulino import ModulinoLEDMatrix
from time import sleep_ms

led_matrix = ModulinoLEDMatrix(use_grayscale=True)
led_matrix.clear().show()

def gradient_pattern(matrix: ModulinoLEDMatrix):
    # Set each row of 12 pixels to increasing brightness
    for row in range(8):
        for col in range(12):
            brightness = col  # Brightness increases from 0 to 11
            matrix.set_pixel(col, row, brightness)
    matrix.show()

def raining_code(matrix: ModulinoLEDMatrix, steps: int = 300, spawn_chance: int = 35, delay_ms: int = 70):
    """
    Play a brief Matrix-style rain animation with a grayscale trail.

    Args:
        matrix: The ModulinoLEDMatrix instance to use.
        steps: Number of animation steps to perform.
        spawn_chance: Chance (0-100) of spawning a new drop each step.
        delay_ms: Delay in milliseconds between each animation step. This controls speed.
    """
    from random import getrandbits

    def _randint(n: int) -> int:
        """Small helper to avoid importing full random."""
        return getrandbits(16) % n

    drops = []  # each drop: (x, head_y, length)

    for _ in range(steps):
        # Maybe spawn a new drop at the top
        if _randint(100) < spawn_chance:
            x = _randint(12)
            length = 2 + _randint(4)  # 2..5 pixels long
            drops.append([x, -1, length])

        matrix.clear()

        active = []
        for x, head_y, length in drops:
            head_y += 1
            tail_y = head_y - length

            # Draw the drop from head down to tail within bounds, brighter toward the head
            for y in range(max(0, tail_y), min(matrix._height, head_y + 1)):
                distance_from_head = head_y - y  # 0 at head, increases upward
                brightness = 15 - (distance_from_head * 14) // max(1, length - 1)
                brightness = 0 if brightness < 0 else brightness  # clamp to avoid wrapping negatives
                matrix.set_pixel(x, y, brightness)

            # Keep drop if it still intersects the display
            if tail_y < matrix._height:
                active.append([x, head_y, length])

        drops = active
        matrix.show()
        sleep_ms(delay_ms)


gradient_pattern(led_matrix)
sleep_ms(2000)
led_matrix.clear().show()

raining_code(led_matrix)
```

**Note:** For more examples including MPJ file animations from the [LED Matrix Editor](https://ledmatrix-editor.arduino.cc/), check the [arduino-modulino-mpy examples](https://github.com/arduino/arduino-modulino-mpy/tree/main/examples).

## Troubleshooting

### Device Not Reachable

If your Modulino's power LED isn't on or the device isn't responsive:
- Ensure both the board and the Modulino are connected to your computer
- Verify that the power LED on the Modulino is lit
- Check that the QWIIC cable is properly clicked into place on both ends
- Try a different QWIIC cable if available
- Verify the I2C address (default is 0x39) matches your configuration

### LEDs Not Displaying

If the LEDs don't illuminate or show the expected pattern:
- Check that you're using `setFrame()` or the graphics `endDraw()` method to update the display
- Verify your frame data format matches the selected display mode (monochromatic vs grayscale)
- Ensure your power supply can handle the current draw (up to 200mA with all LEDs on)
- Try the basic example first to confirm the hardware is working

### Animation Issues

If animations don't play or appear glitchy:
- Verify your animation data format is correct (frame data + duration)
- Check that `play()` is called after `setSequence()`
- For manual frame control, ensure `nextFrame()` is called at appropriate intervals
- Verify the frame count matches your animation data

### Library Issues

See the [Getting Started with Modulinos](./how-general) guide for library installation troubleshooting.

## Project Ideas

Now that you've learned how to use your Modulino LED Matrix, try these projects:

- **Status Display**: Show system status with colour-coded indicators
- **Progress Bar**: Visualise completion of tasks or loading processes
- **Music Visualiser**: Create light shows that respond to audio input
- **Game Display**: Build simple LED-based games
- **Notification Centre**: Display alerts with different colour patterns
- **Temperature Indicator**: Show temperature ranges with colour gradients
- **Traffic Light System**: Create multi-state indicators
- **Binary Clock**: Display time in a unique LED pattern
