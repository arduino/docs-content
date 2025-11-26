---
title: 'Nano R4 User Manual'
difficulty: beginner
compatible-products: [nano-r4]
description: 'Learn about the hardware and software features of the Arduino® Nano R4 board.'
tags:
  - Cheat sheet
  - User manual
author: 'José Bagur'
hardware:
  - hardware/04.nano/boards/nano-r4
software:
  - ide-v1
  - ide-v2
  - iot-cloud
  - web-editor
---

This user manual provides a comprehensive overview of the Nano R4 board, highlighting its hardware and software elements. With it, you will learn how to set up, configure and use all the main features of the Nano R4 board.

![ ](assets/hero-banner.png)

## Hardware and Software Requirements

### Hardware Requirements

- [Nano R4](https://store.arduino.cc/products/nano-r4) (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- [Breadboard](https://store.arduino.cc/products/breadboard-400-contacts) (x1) (recommended) 
- [Male/male jumper wires](https://store.arduino.cc/products/breadboard-400-contacts) (recommended)

### Software Requirements

- [Arduino IDE](https://www.arduino.cc/en/software) or [Arduino Cloud Editor](https://create.arduino.cc/editor)
- [Arduino UNO R4 Boards core](https://github.com/arduino/ArduinoCore-renesas)

***The Nano R4 is compatible with the complete Arduino ecosystem and can be programmed directly as a standalone device.***

## Nano R4 Overview

The Nano R4 board represents the natural evolution of the Nano family, combining the powerful RA4M1 microcontroller from Renesas with the compact and familiar Nano form factor. This board is designed to facilitate seamless transition from prototyping to production, using the same powerful core already used in the UNO R4 family.

![ ](assets/front-page.png)

The Nano R4 includes a high-performance 32-bit microcontroller (R7FA4M1AB3CFM), expanded connectivity through an onboard Qwiic connector and advanced features such as DAC, CAN and operational amplifiers. Its compact dimensions (18 mm x 45 mm) and robust construction make the Nano R4 board an excellent choice for projects that demand sensor fusion capabilities and the computational power of modern microcontrollers.


### Nano R4 Architecture Overview

The Nano R4 board features a secure, certified and durable design that suits various applications, such as industrial automation, building automation and rapid prototyping.

The top view of the Nano R4 board is shown in the image below:

![The Nano R4 main components (top view)](assets/user-manual-1.png)

The bottom view of the Nano R4 board is shown in the image below:

![The Nano R4 main components (bottom view)](assets/user-manual-2.png)

***The bottom side of the Nano R4 board features only test points for debugging and development purposes, along with the board's certification markings and identification information (board model and SKU).***


Here is an overview of the board's main components shown in the images above:

- **Microcontroller**: At the heart of the Nano R4 board there is a Renesas RA4M1 family microcontroller ([R7FA4M1AB3CFM](https://www.renesas.com/en/document/dst/ra4m1-group-datasheet?srsltid=AfmBOoryT-HIws0lHBASVG1QdfHDNWNQ5FNnoQV3hpoQ0FbncC7FI3h4)). This single-chip microcontroller, recognized as one of the industry's most energy-efficient microcontroller, is based on a 48 MHz Arm® Cortex®-M4 core with up to 256 KB of flash memory and 32 KB of SRAM memory.
- **USB-C connector**: The Nano R4 board features a modern USB-C connector for programming, power supply and serial communication with the external world.
- **Qwiic connector**: The Nano R4 board also includes an onboard Qwiic connector to expand the board's communication capabilities via I²C, facilitating connection with a wide range of boards, sensors, actuators and different peripherals.

- **Programmable RGB LED**: The Nano R4 board has an onboard user-programmable RGB LED to provide visual feedback about different operating states.
- **User LED**: In addition to the onboard user-programmable RGB LED, the board also includes an additional onboard user-programmable orange LED for basic status indications.
- **Castellated pins**: The board's castellated pins allow surface mounting as a module, facilitating integration into custom hardware designs.
- **Advanced microcontroller features**: The R7FA4M1AB3CFM microcontroller has integrated peripherals such as a 12-bit Digital-to-Analog Converter (DAC), CAN bus for industrial communications, integrated Operational Amplifiers (OpAmp) and HID emulation capabilities (keyboard/mouse).

### Board Core and Libraries

The **Arduino UNO R4 Boards** core contains the libraries and examples to work with the Arduino Nano R4's peripherals and onboard components, such as its RA4M1 microcontroller, advanced peripherals (DAC, CAN and OpAmp), Qwiic connector and the onboard RGB LED. To install the core for the Nano R4 board, navigate to **Tools > Board > Boards Manager** or click the **Boards Manager** icon in the left tab of the IDE. In the Boards Manager tab, search for `UNO R4` and install the latest Arduino UNO R4 Boards version.


![Installing the Arduino UNO R4 Boards core in the Arduino IDE](assets/user-manual-3.png)

The Arduino UNO R4 Boards core provides support for the following:

- Board control and configuration (reset, pin configuration and power management)
- Advanced peripheral functions (12-bit DAC, ADC, CAN bus and OpAmp)
- Communication interfaces (UART, I²C and SPI)
- Onboard LED control (RGB LED and orange LED)
- Real-time clock (RTC) functionality
- HID emulation capabilities (keyboard and mouse)
- Standard Arduino libraries compatibility

***__Important note:__ Since the Nano R4 uses the same RA4M1 microcontroller as the UNO R4 WiFi and the UNO R4 Minima, it shares complete code and library compatibility, making it easy to transition projects between these boards.***


### Pinout

![Nano R4 pinout](assets/simple-pinout.png)

The full pinout is available and downloadable as PDF from the link below:

- [Nano R4 pinout](https://docs.arduino.cc/resources/pinouts/ABX00142-full-pinout.pdf)

### Datasheet

The complete datasheet is available and downloadable as PDF from the link below:

- [Nano R4 datasheet](https://docs.arduino.cc/resources/datasheets/ABX00142-datasheet.pdf)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

[- Nano R4 schematics](https://docs.arduino.cc/resources/schematics/ABX00142-schematics.pdf)

### STEP Files

The complete STEP files are available and downloadable from the link below:

- [Nano R4 STEP files](../../downloads/ABX00142-step.zip)

## First Use

### Unboxing the Product

When opening the Nano R4 box, you will find the board and its corresponding documentation. **The Nano R4 does not include additional cables**, so you will need a USB-C cable ([available separately here](https://store.arduino.cc/products/usb-cable2in1-type-c)) to connect the board to your computer.

![Nano R4 unboxing](assets/unboxing.png)
 
The Nano R4 is a standalone device that can be programmed directly without requiring additional boards. However, for more complex projects, you can easily combine it with Arduino shields compatible with the Nano family or connect it to other Arduino devices through its onboard Qwiic connector.

### Connecting the Board

The Nano R4 can be connected to your computer using its onboard USB-C connector. It can also be integrated into larger projects using the following:

- **Direct USB-C connection**: For programming, power supply and serial communication with the computer
- **Pin connection**: For integration into breadboards or custom PCBs
- **Qwiic connection**: For rapid expansion with compatible sensors and modules

- **Module mounting**: Using the board's castellated pins for direct soldering to PCBs

***__Important note:__ The Nano R4 operates at +5 VDC natively. When connecting sensors or modules that operate at +3.3 VDC, make sure to verify voltage compatibility to avoid component damage.***

### Voltage Compatibility Considerations

Before connecting any external components to your Nano R4, it is important to understand its voltage characteristics to prevent damage to your sensors and modules:

**The Nano R4 operates at +5 VDC**, which means:

- All digital I/O pins use +5 VDC logic levels (HIGH = +5 VDC, LOW = 0 VDC)
- Analog inputs can safely accept 0 to +5 VDC
- Communication pins (I²C, SPI, UART) operate at +5 VDC logic levels

**For +3.3 VDC components**, you have these safe options:

- Use the onboard **Qwiic connector** for I²C devices (includes built-in level shifting)
- Add **external level shifters** for digital communication pins
- Use the onboard **+3.3 VDC power pin** to power your devices (but still need level shifting for data lines)

**Common components that typically require level shifting:**

- Modern sensors from SparkFun (Qwiic), Adafruit (STEMMA QT), and Pimoroni for example
- Most MEMS sensors (for example, accelerometers, gyroscopes, pressure sensors)
- Many OLED and TFT displays
- SD card modules
- Most wireless modules (Wi-Fi®, Bluetooth®, LoRa®)

Always check your component's datasheet for voltage specifications before connecting. When in doubt, use a multimeter to verify voltage levels or add protective level shifting.

### Powering the Board

The Nano R4 can be powered in several ways:

- **Via USB-C connector**: The most common method during development and programming
- **Via `VIN` pin**: Using an external +6-21 VDC power supply that will be internally regulated to +5 VDC
- **Via `5V` pin**: Directly connecting a regulated +5 VDC source (with caution)

![Different ways to power the Nano R4 board](assets/user-manual-4.png)

***__Important note:__ The Nano R4's `VIN` pin accepts a voltage range of +6-21 VDC. Do not connect voltages outside this range as you could permanently damage the board. Always verify all the connections before applying power.***

#### Internal +3.3 VDC Power Supply

The Nano R4 also includes an onboard +3.3 VDC regulator ([AP2112K](https://www.diodes.com/assets/Datasheets/AP2112.pdf)) that provides power for the following:

- **Qwiic connector**: Supplies +3.3 VDC power to connected I²C devices
- **I²C level translation**: Enables communication between the +5 VDC microcontroller and +3.3 VDC Qwiic devices
- **Internal +3.3 VDC peripherals**: Powers certain internal circuits that require +3.3 VDC operation

This internal +3.3 VDC supply allows the board to interface with both +5 VDC and +3.3 VDC devices through the Qwiic ecosystem while maintaining the +5 VDC operation of the board's main microcontroller.

#### VBATT Pin

The `VBATT` pin allows the connection of a backup battery (within the +1.6-3.6 VDC range) to maintain the microcontroller's real-time clock (RTC) and certain low-power functions when the main power source is disconnected from the board. This is particularly useful for applications that need to keep track of time or maintain certain settings of the microcontroller during power outages. 

Common battery options for this purpose include the following:

- Coin cell batteries (CR2032: +3 VDC)
- Rechargeable LiPo batteries (+3.7 VDC nominal)
- AA/AAA batteries (+1.5-3 VDC depending on the chemistry of the battery)

    
### Hello World Example

Let's program the Nano R4 to reproduce the classic `Hello World` example used in the Arduino ecosystem: the `Blink` sketch. We will use this example to verify that the Nano R4's connection to the computer works correctly, that the Arduino IDE is properly configured, and that both the board and development environment function as expected.

First, connect your Nano R4 to your computer using a USB-C cable, open the Arduino IDE, and make sure that the board is connected correctly. If you are new to the Arduino IDE, please refer to the official Arduino documentation for more detailed information about initial setup. Copy and paste the following example sketch into a new Arduino IDE file:

```arduino
/**
Blink Example for the Arduino Nano R4 Board
Name: nano_r4_blink.ino
Purpose: This sketch demonstrates how to blink the built-in
user LED of the Arduino Nano R4 board.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

// Built-in LED pin
#define LED_PIN LED_BUILTIN

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Configure LED pin as output
  pinMode(LED_PIN, OUTPUT);
  
  // Startup message
  Serial.println("- Arduino Nano R4 - Blink Example started...");
}

void loop() {
  // Turn on the LED, wait 1 second
  digitalWrite(LED_PIN, HIGH);
  Serial.println("- LED on!");
  delay(1000);
  
  // Turn off the LED, wait 1 second
  digitalWrite(LED_PIN, LOW);
  Serial.println("- LED off!");
  delay(1000);  
}
```

To upload the sketch to the board, click the **Verify** button to compile the sketch and check for errors, then click the **Upload** button to program the device with the sketch.

![Uploading a sketch to the Nano R4 in the Arduino IDE](assets/user-manual-5.png)

As shown in the animation below, you should see the built-in orange user LED of your Nano R4 board turn on for one second, then turn off for one second, repeating this cycle continuously. 

![Onboard orange user LED blinking](assets/user-manual-6.gif)

Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages that the example sketch sends each time the LED state changes.

![Arduino IDE Serial Monitor output for the Blink sketch](assets/user-manual-7.png)

This example confirms the following:

- The Nano R4 board is correctly connected
- The Arduino IDE is properly configured
- The board is functioning correctly
- USB communication is working
- Digital pins respond to commands

Congratulations! You have successfully completed your first program on the Nano R4 board. You are now ready to explore the more advanced features of this tiny but powerful board.

## LEDs

This user manual section covers the Nano R4 built-in LEDs, showing their main hardware and software characteristics.

### RGB LED

The Nano R4 features a built-in RGB LED that can be used as a visual feedback indicator for the user.

![Built-in RGB LED of the Nano R4 board](assets/user-manual-8.png)

The built-in RGB LED can be accessed through the following macro definitions:

| **Built-in LED** | **Macro Definition** | **Microcontroller Pin** |
| :--------------: | :------------------: | :---------------------: |
|     Red LED      |        `LEDR`        |         `P409`          |
|    Green LED     |        `LEDG`        |         `P411`          |
|     Blue LED     |        `LEDB`        |         `P410`          |

***The built-in RGB LED on the Nano R4 must be pulled to ground (`GND`) to make it light up. This means that a voltage level of `LOW` on each of their pins will turn the specific color of the LED on, and a voltage level of `HIGH` will turn them off.***

The following example sketch each of the RGB LED colors at an interval of 500 ms:

```arduino
/**
RGB LED Example for the Arduino Nano R4 Board
Name: nano_r4_rgb_led.ino
Purpose: This sketch demonstrates how to control the built-in
RGB LED of the Arduino Nano R4 board.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Initialize LEDR, LEDG and LEDB as outputs
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDB, OUTPUT);
  
  // Turn off all LEDs initially
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);
  
  Serial.println("- Arduino Nano R4 - RGB LED Example started...");
}

void loop() {
  // Turn on the built-in red LED and turn off the rest
  digitalWrite(LEDR, LOW);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);
  Serial.println("- Red LED on!");
  delay(500);
  
  // Turn on the built-in green LED and turn off the rest
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, LOW);
  digitalWrite(LEDB, HIGH);
  Serial.println("- Green LED on!");
  delay(500);
  
  // Turn on the built-in blue LED and turn off the rest
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, LOW);
  Serial.println("- Blue LED on!");
  delay(500);
  
  // Turn off all LEDs
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);
  Serial.println("- All LEDs off!");
  delay(500);
}
```

You should now see the built-in RGB LED cycling through red, green, and blue colors, followed by a brief moment with all LEDs off, repeating this pattern continuously.

![Onboard RGB user LED blinking](assets/user-manual-9.gif)

Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages that the example sketch sends each time the RGB LEDs state changes.

![Arduino IDE Serial Monitor output for the RGB LED example sketch](assets/user-manual-10.png)

### Orange LED

The Nano R4 also features a built-in orange user LED that can be used for basic status indications and debugging purposes.

![Built-in user LED of the Nano R4 board](assets/user-manual-12.png)


The built-in user LED can be accessed through the following macro definition:

| **Built-in LED** | **Macro Definition** | **Microcontroller Pin** |
| :--------------: | :------------------: | :---------------------: |
| Orange User LED  |    `LED_BUILTIN`     |         `P204`          |

***Unlike the RGB LED, the built-in user LED on the Nano R4 operates with standard logic levels. This means that a voltage level of `HIGH` will turn the LED on, and a voltage level of `LOW` will turn it off.***

The following example sketch demonstrates how to control the built-in user LED:

```arduino
/**
User LED Example for the Arduino Nano R4 Board
Name: nano_r4_user_led.ino
Purpose: This sketch demonstrates how to control the built-in
user LED of the Arduino Nano R4 board.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Configure LED_BUILTIN pin as output
  pinMode(LED_BUILTIN, OUTPUT);
  
  // Turn off LED initially
  digitalWrite(LED_BUILTIN, LOW);
  
  Serial.println("- Arduino Nano R4 - User LED Example started...");
}

void loop() {
  // Turn on the built-in user LED
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("- User LED on!");
  delay(1000);
  
  // Turn off the built-in user LED
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("- User LED off!");
  delay(1000);
}
```

You should now see the built-in orange user LED blinking on and off at 1-second intervals, repeating this pattern continuously.

![Onboard RGB user LED blinking](assets/user-manual-13.gif)

Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages that the example sketch sends each time the user LED state changes.

![Arduino IDE Serial Monitor output for the orange LED example sketch](assets/user-manual-7.png)

## Pins

This user manual section provides comprehensive information about the Nano R4's pin capabilities and functionality. Understanding the board's pins capabilities and configurations is important for making the most of your projects with the Nano R4 board.


### Pins Overview

The Nano R4 features a total of **20 accessible pins** arranged in the classic Nano form factor, maintaining compatibility with existing Nano shields and breadboard layouts. These pins provide various functionalities including digital I/O, analog input, PWM output and several communication protocols.

![Nano R4 pinout overview](assets/simple-pinout.png)

### Pins Specifications and Characteristics

The Nano R4's pins are organized into the following categories:

|   **Pin Type**   | **Count** |      **Pin Numbers**      |           **Primary Functions**            |
| :--------------: | :-------: | :-----------------------: | :----------------------------------------: |
| **Digital Pins** |    14     |       `D0` - `D13`        |    Digital I/O, PWM (6 pins), SPI, UART    |
| **Analog Pins**  |     8     |        `A0` - `A7`        | Analog input, Digital I/O, I²C, DAC (`A0`) |
|  **Power Pins**  |     4     | `VIN`, `5V`, `3V3`, `GND` |          Power supply and ground           |
| **Special Pins** |     2     |     `RESET`, `VBATT`      |         System control and backup          |

The Nano R4 offers several advanced pin capabilities including multi-function pins that can serve multiple purposes depending on your project needs, native +5 VDC operation for compatibility with classic Arduino shields, internal +3.3 VDC level translation for modern sensors and electronic components via Qwiic, and built-in advanced peripherals such as DAC, CAN bus and operational amplifiers on specific pins of the board.

***__Important voltage compatibility Note__: Unlike many other boards in the Nano family (Nano 33 BLE Sense, Nano 33 IoT, Nano ESP32) that operate at +3.3 VDC, the Nano R4 operates at +5 VDC. This fundamental difference affects ALL digital and analog pins, including communication interfaces like I²C (`A4/A5`), SPI, and UART. Before connecting any sensors, modules, or shields, always verify their voltage compatibility. __Using +3.3 VDC devices without proper level shifting can result in permanent damage to those components__.***

The following table shows the electrical specifications and operating limits for all pins on the Nano R4 board:

|    **Specification**    |  **Value**   |            **Notes**             |
| :---------------------: | :----------: | :------------------------------: |
|  **Operating Voltage**  |    +5 VDC    | Logic level for all digital pins |
| **Input Voltage Range** | 0 - +5.5 VDC |      +5 VDC tolerant inputs      |
| **Max Current per Pin** |     8 mA     |    Source/sink current limit     |
|  **Max Total Current**  |    200 mA    |  Combined current for all pins   |
|  **Analog Reference**   |    +5 VDC    |      Default `AREF` voltage      |

***__Important safety considerations when working with the Nano R4 pins:__ Never exceed +5.5 VDC on any pin to avoid permanent damage, respect the 8 mA per pin and 200 mA total current limits, handle the board with proper anti-static precautions, avoid connecting pins directly to ground or power and always verify voltage levels when connecting +3.3 VDC devices.***


### Digital Pins

The Nano R4 features 14 digital pins (`D0` to `D13`) that can be configured as either digital inputs or digital outputs. These pins operate at +5 VDC logic levels and can source or sink up to 8 mA of current per pin. Digital pins are the foundation of most Arduino projects, allowing you to control LEDs, read button states, interface with sensors and communicate with other devices.

The Nano R4 digital pins provide the following functionality:

| **Arduino Pin** | **Microcontroller Pin** | **Additional Functions** | **Special Features** |
| :-------------: | :---------------------: | :----------------------: | :------------------: |
|      `D0`       |         `P104`          |       UART RX, PWM       | Serial communication |
|      `D1`       |         `P105`          |       UART TX, PWM       | Serial communication |
|      `D2`       |         `P213`          |           PWM            |  External interrupt  |
|      `D3`       |         `P212`          |           PWM            |  External interrupt  |
|      `D4`       |         `P109`          |       CAN TX, PWM        |  CAN communication   |
|      `D5`       |         `P110`          |       CAN RX, PWM        |  CAN communication   |
|      `D6`       |         `P107`          |           PWM            |     Digital I/O      |
|      `D7`       |         `P106`          |           PWM            |     Digital I/O      |
|      `D8`       |         `P300`          |           PWM            |     Digital I/O      |
|      `D9`       |         `P108`          |           PWM            |     Digital I/O      |
|      `D10`      |         `P103`          |       SPI CS, PWM        |  SPI communication   |
|      `D11`      |         `P101`          |      SPI MOSI, PWM       |  SPI communication   |
|      `D12`      |         `P100`          |         SPI MISO         |  SPI communication   |
|      `D13`      |         `P102`          |         SPI SCK          |  SPI communication   |

***__Important note:__ Pins `D0` and `D1` are used for serial communication (UART) and should be avoided for general digital I/O when using Serial communication. Pins `D4` and `D5` can be used for CAN bus communication. Pins `D10`, `D11`, `D12` and `D13` are used for SPI communication.***


The Nano R4's digital pins offer the following specifications:

|  **Specification**   |   **Value**    |           **Notes**           |
| :------------------: | :------------: | :---------------------------: |
|    Logic Voltage     |     +5 VDC     | `HIGH` and `LOW` logic levels |
|    Input Voltage     | 0 to +5.5 VDC  |    +5 VDC tolerant inputs     |
| Max Current (Source) |      8 mA      |    Per pin source current     |
|  Max Current (Sink)  |      8 mA      |     Per pin sink current      |
|  Total Max Current   |     200 mA     |     Combined for all pins     |
|   Input Resistance   |    20-50 kΩ    |   Internal pull-up resistor   |
|    Digital `HIGH`    | +3.5 to +5 VDC |  Minimum voltage for `HIGH`   |
|    Digital `LOW`     | 0 to +1.5 VDC  |   Maximum voltage for `LOW`   |

Digital pins can be configured and controlled using the following basic Arduino functions.

You can configure a pin's mode using the `pinMode()` function:

```arduino
pinMode(pin, mode);
```

To write a digital value to an output pin, use the `digitalWrite()` function:

```arduino
digitalWrite(pin, value);
```

To read the state of a digital input pin, use the `digitalRead()` function:

```arduino
digitalRead(pin);
```

The available pin modes are `OUTPUT` for digital output, `INPUT` for digital input with high impedance, and `INPUT_PULLUP` for digital input with internal pull-up resistor enabled. Digital output values can be `HIGH` (+5 VDC) or `LOW` (0 VDC), and digital input readings will return `HIGH` or `LOW` based on the voltage level detected on the pin.

***The following example demonstrate basic digital pin functionality using simple connections that you can easily test with the Nano R4 board.*** 

The following example demonstrates using both digital input and output simultaneously by reading a button and controlling the built-in LED of the board:

```arduino
/**
Combined Digital I/O Example for the Arduino Nano R4 Board
Name: nano_r4_digital_io_combined.ino
Purpose: This sketch demonstrates reading a button input and toggling
the built-in LED state each time the button is pressed.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

// Pin definitions
const int buttonPin = 2;            // Button input on D2
const int ledPin = LED_BUILTIN;     // Built-in LED

// Variables to store button and LED state
int buttonState = 0;
int lastButtonState = HIGH;
bool ledState = false;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Configure pins
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  
  // Turn off LED initially
  digitalWrite(ledPin, LOW);
  
  Serial.println("- Arduino Nano R4 - Combined Digital I/O Example started...");
  Serial.println("- Press button to toggle the built-in LED");
}

void loop() {
  // Read current button state
  buttonState = digitalRead(buttonPin);
  
  // Check if button was just pressed (state change from HIGH to LOW)
  if (buttonState == LOW && lastButtonState == HIGH) {
    // Button press detected - toggle LED state
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    
    Serial.print("- Button pressed! LED is now ");
    if (ledState) {
      Serial.println("ON");
    } else {
      Serial.println("OFF");
    }
    
    // Simple debounce delay
    delay(50);  
  }
  
  // Save current button state for next iteration
  lastButtonState = buttonState;
  
  // Small delay for stability
  delay(10);
}
```

To test this example, connect a push button to the Nano R4 board as follows:

- Connect one leg of a push button to pin `D2`
- Connect the other leg of the push button to `GND`
- No external components needed (using built-in LED and internal pull-up)

![Digital pins test circuit on the Nano R4 board](assets/digital-pins-1.png)

You should now see the built-in LED toggle on and off each time you press the button. The LED will stay in its current state until you press the button again. Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see messages indicating when the button is pressed and the current LED state.

![Arduino IDE Serial Monitor output for the combined digital I/O example sketch](assets/digital-pins-2.png)

### Analog Pins

The Nano R4 features **8 analog input pins** (`A0` to `A7`) that can be read using the `analogRead()` function. These pins allow you to measure continuously varying voltages, making them perfect for reading sensors like potentiometers, light sensors, temperature sensors and other analog components and devices. The analog-to-digital converter (ADC) built into the RA4M1 microcontroller of the Nano R4 board converts the analog voltage into a digital value that your sketch can process.

The Nano R4 analog pins provide the following functionality:

| **Arduino Pin** | **Microcontroller Pin** | **Additional Functions** | **Special Features**  |
| :-------------: | :---------------------: | :----------------------: | :-------------------: |
|      `A0`       |         `P000`          |           DAC            |   12-bit DAC output   |
|      `A1`       |         `P001`          |         OPAMP +          | Operational amplifier |
|      `A2`       |         `P002`          |         OPAMP -          | Operational amplifier |
|      `A3`       |         `P003`          |        OPAMP OUT         | Operational amplifier |
|      `A4`       |         `P004`          |        SDA (I²C)         |   I²C communication   |
|      `A5`       |         `P010`          |        SCL (I²C)         |   I²C communication   |
|      `A6`       |         `P014`          |        Analog In         |   Analog input only   |
|      `A7`       |         `P015`          |        Analog In         |   Analog input only   |

***__Important note:__ Pin `A0` has a built-in 12-bit Digital-to-Analog Converter (DAC) for analog output. Pins `A1`, `A2` and `A3` are connected to the integrated operational amplifier. Pins `A4` and `A5` are primarily used for I²C communication (SDA and SCL respectively).***


The Nano R4's analog pins offer the following specifications:

| **Specification**  |  **Value**   |          **Notes**           |
| :----------------: | :----------: | :--------------------------: |
|   Input Voltage    | 0 to +5 VDC  |  Maximum safe input voltage  |
| Default Resolution |    10-bit    |        Values 0-1023         |
| Maximum Resolution |    14-bit    |        Values 0-16383        |
| Default Reference  |    +5 VDC    |         AREF voltage         |
| Internal Reference |   +1.5 VDC   | Built-in precision reference |
|    Sample Rate     | Up to 1 MSPS |    Maximum sampling speed    |
|      Accuracy      |    ±2 LSB    | Typical conversion accuracy  |

You can read analog values using the `analogRead()` function:

```arduino
value = analogRead(pin);
``` 

The default reference voltage of these pins is +5 VDC, but this can be changed using the `analogReference()` function. You can use `analogReference(AR_DEFAULT)` for the default reference of +5 VDC or `analogReference(AR_INTERNAL)` for the built-in reference of +1.5 VDC.

The default resolution is set to 10-bit, but it can be updated to 12-bit and 14-bit resolutions using the `analogReadResolution()` function in the `setup()` of your sketch. Available options are analogReadResolution(10) for default 10-bit, analogReadResolution(12) for 12-bit, or analogReadResolution(14) for maximum 14-bit resolution.


***The following examples demonstrate basic analog pin functionality using simple connections that you can easily test with the Nano R4 board.***

The following example demonstrates how to read an analog value and display it on the Serial Monitor:

```arduino
/**
Analog Input Example for the Arduino Nano R4 Board
Name: nano_r4_analog_input.ino
Purpose: This sketch demonstrates how to read an analog input
and display the value on the Serial Monitor.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

// Analog input pin
const int analogPin = A0;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - Analog Input Example started...");
  Serial.println("- Reading analog values from pin A0");
}

void loop() {
  // Read the analog value (0 - 1023 with 10-bit resolution)
  int analogValue = analogRead(analogPin);
  
  // Convert to voltage (0 to +5 VDC)
  float voltage = analogValue * (5.0 / 1023.0);
  
  // Display the results
  Serial.print("- Analog Value: ");
  Serial.print(analogValue);
  Serial.print(" | Voltage: ");
  Serial.print(voltage, 2);
  Serial.println(" VDC");
  
  // Wait half a second before next reading
  delay(500);  
}
```

To test this example, connect a potentiometer to the Nano R4 board as follows:

- Connect the middle pin of a potentiometer to `A0`
- Connect one outer pin of the potentiometer to +5 VDC
- Connect the other outer pin of the potentiometer to `GND`

![ADC test circuit on the Nano R4 board](assets/analog-1.png)

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the real-time analog values and voltage measurements as you adjust the potentiometer. As you turn the potentiometer, the values will range from 0 to 1023, with corresponding voltage readings from 0 to +5 VDC.

![Arduino IDE Serial Monitor output for the analog input example sketch](assets/analog-2.png)

The following example demonstrates how to use 14-bit resolution for more precise analog readings; **use the same potentiometer connection from the first example**:

```arduino
/**
High-Resolution Analog Input Example for the Arduino Nano R4 Board
Name: nano_r4_analog_high_res.ino
Purpose: This sketch demonstrates how to use 14-bit resolution
for precise analog input measurements.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

// Analog input pin
const int analogPin = A0;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Set analog read resolution to 14-bit (0 - 16383)
  analogReadResolution(14);
  
  Serial.println("- Arduino Nano R4 - High-Resolution Analog Input Example started...");
  Serial.println("- Using 14-bit resolution (0 - 16383)");
}

void loop() {
  // Read the analog value (0 - 16383 with 14-bit resolution)
  int analogValue = analogRead(analogPin);
  
  // Convert to voltage (0 - +5 VDC)
  float voltage = analogValue * (5.0 / 16383.0);
  
  // Calculate percentage (0 - 100%)
  float percentage = (analogValue / 16383.0) * 100.0;
  
  // Display the results
  Serial.print("- Analog Value: ");
  Serial.print(analogValue);
  Serial.print(" | Voltage: ");
  Serial.print(voltage, 3);
  Serial.print(" VDC | Percentage: ");
  Serial.print(percentage, 1);
  Serial.println(" %");
  
  // Wait half a second before next reading
  delay(500);
}
```

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the high-resolution analog values, voltage measurements and percentage calculations as you adjust the potentiometer. With 14-bit resolution, the values will range from 0 to 16383 instead of the standard 0 to 1023, providing significantly higher precision for sensitive measurements.

![Arduino IDE Serial Monitor output for the high-resolution analog input example sketch](assets/analog-3.png)

### PWM (Pulse Width Modulation)

The Nano R4 board  features multiple pins with PWM capability that can be used to generate analog-like output signals. PWM works by rapidly switching a digital output between `HIGH` and `LOW` states, where the ratio of `HIGH` time to the total period determines the effective analog voltage output.

***__PWM Compatibility Note__: The Nano R4 shares identical PWM capabilities with the UNO R4 Minima, as both boards use the same RA4M1 microcontroller. This includes the same default 8-bit resolution, maximum 16-bit resolution, and PWM frequency control features. Code written for PWM on the UNO R4 Minima will work identically on the Nano R4.***

The Nano R4 board provides PWM functionality on the following pins:

| **Arduino Pin** | **Microcontroller Pin** | **PWM Channel** | **Primary Function**  |
| :-------------: | :---------------------: | :-------------: | :-------------------: |
|      `D3`       |         `P212`          |   Channel 0B    |      Digital I/O      |
|      `D5`       |         `P110`          |   Channel 1B    |      Digital I/O      |
|      `D6`       |         `P107`          |   Channel 0A    |      Digital I/O      |
|      `D9`       |         `P108`          |   Channel 0B    |      Digital I/O      |
|      `D10`      |         `P103`          |   Channel 2A    |  Digital I/O, SPI CS  |
|      `D11`      |         `P101`          |   Channel 5A    | Digital I/O, SPI MOSI |

***__Important notes__: Pins `D3` and `D9` share the same PWM channel (`Channel 0B`) and cannot be used for PWM simultaneously. When using PWM on one of these pins, the other cannot output an independent PWM signal. Similarly, pins `D6`, `D3`, and `D9` all use timer `GPT0`, which means they will share the same PWM frequency setting. The onboard LEDs (`LEDR`, `LEDG`, `LEDB`, `LED_BUILTIN`) also support PWM for brightness control.***

The Nano R4's PWM offers the following technical specifications:

|  **Specification** |     **Value**    |            **Notes**           |
|:------------------:|:----------------:|:------------------------------:|
| Default Resolution |   8-bit (0-255)  | Standard Arduino compatibility |
| Maximum Resolution | 16-bit (0-65535) |     Full precision control     |

You can use PWM pins as analog output pins with the `analogWrite()` function:

```arduino
analogWrite(pin, value);
```

**By default, the resolution is 8-bit (0 to 255)**. You can use the `analogWriteResolution()` resolution to change this, supporting up to 16-bit (0 to 65535) resolution: 

```arduino
analogWriteResolution(resolution);
```

The Nano R4 supports the following PWM resolution options that you can configure based on your project's precision requirements:

- `analogWriteResolution(8)`: 8-bit resolution (0 to 255, **default resolution**)
- `analogWriteResolution(10)`: 10-bit resolution (0 to 1023)
- `analogWriteResolution(12)`: 12-bit resolution (0 to 4095)
- `analogWriteResolution(14)`: 14-bit resolution (0 to 16383)
- `analogWriteResolution(16)`: 16-bit resolution (0 to 65535, **maximum resolution**)

***The following PWM examples use the built-in orange user LED (`LED_BUILTIN`) of the Nano R4 board, which supports PWM for brightness control. This eliminates the need for external components and allows you to test PWM functionality immediately.***

The following example demonstrates how to control the brightness of the built-in orange user LED using PWM:

```arduino
/**
PWM Example for the Arduino Nano R4 Board
Name: nano_r4_pwm_led.ino
Purpose: This sketch demonstrates how to use PWM to control
the brightness of the built-in user LED of the Nano R4 board.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

// Built-in LED pin (supports PWM)
const int ledPin = LED_BUILTIN;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // No need to set pinMode for PWM pins - analogWrite() handles this
  
  Serial.println("- Arduino Nano R4 - PWM LED Example started...");
  Serial.println("- Built-in LED will fade in and out continuously");
}

void loop() {
  // Fade in (0 to 255)
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(ledPin, brightness);
    delay(5);
  }
  
  Serial.println("- LED at maximum brightness");
  delay(500);
  
  // Fade out (255 to 0)
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(ledPin, brightness);
    delay(5);
  }
  
  Serial.println("- LED turned off");
  delay(500);
}
```

You should now see the built-in orange user LED of your Nano R4 board gradually fade in and out, creating a smooth breathing effect that repeats continuously.

![Onboard RGB user LED fading](assets/pwm-1.gif)

Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages that the example sketch sends at key brightness levels.

![Arduino IDE Serial Monitor output for the PWM example sketch](assets/pwm-2.png)

The following example demonstrates how to use a 12-bit PWM resolution for more precise control of the built-in orange user LED:

```arduino
/**
High-Resolution PWM Example for the Arduino Nano R4 Board
Name: nano_r4_pwm_high_res.ino
Purpose: This sketch demonstrates how to use 12-bit PWM resolution
for precise control of the built-in orange user LED brightness.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

// Built-in LED pin (supports PWM)
const int pwmPin = LED_BUILTIN;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Set PWM resolution to 12-bit (0-4095)
  analogWriteResolution(12);
  
  Serial.println("- Arduino Nano R4 - High-Resolution PWM Example started...");
  Serial.println("- Using 12-bit resolution (0-4095) with built-in LED");
}

void loop() {
  // Generate a smooth sine wave using 12-bit PWM
  for (int i = 0; i < 360; i++) {
    // Calculate sine wave value and map to 12-bit range
    float sineValue = sin(i * PI / 180.0);
    int pwmValue = (int)((sineValue + 1.0) * 2047.5);  // Map -1 to 1 → 0 to 4095
    
    analogWrite(pwmPin, pwmValue);
    
    // Print current values every 30 degrees
    if (i % 30 == 0) {
      Serial.print("- Angle: ");
      Serial.print(i);
      Serial.print("°, PWM Value: ");
      Serial.println(pwmValue);
    }
    
    delay(10);
  }
  
  Serial.println("- Sine wave cycle completed");
  delay(1000);
}
```

This high-resolution example creates a smooth sine wave pattern with the built-in LED brightness, demonstrating the precision available with a 12-bit PWM resolution. You should see a very smooth transition in the LED brightness following a sine wave pattern. Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the angle and PWM value outputs that demonstrate the precise 12-bit control values being used.

![Arduino IDE Serial Monitor output for the high-resolution PWM example sketch](assets/pwm-3.png)

### Operational Amplifier (OPAMP)

The Nano R4 board features a built-in operational amplifier (OPAMP) that provides signal conditioning and amplification capabilities directly on the board. The OPAMP is connected to analog pins `A1`, `A2` and `A3`, allowing you to perform analog signal processing without requiring external amplifier circuits. This feature is particularly useful for sensor signal amplification, buffering and analog filtering applications.

The Nano R4 board OPAMP provides the following pin connections:

| **Arduino Pin** | **Microcontroller Pin** | **OPAMP Function** |     **Description**     |
| :-------------: | :---------------------: | :----------------: | :---------------------: |
|      `A1`       |         `P001`          |      OPAMP +       | Non-inverting input (+) |
|      `A2`       |         `P002`          |      OPAMP -       |   Inverting input (-)   |
|      `A3`       |         `P003`          |     OPAMP OUT      |    Amplifier output     |

***__Important note:__ When using the OPAMP functionality, pins `A1`, `A2` and `A3` cannot simultaneously be used as regular analog inputs. The positive supply (Vs+) is fixed to approximately +5 VDC and the negative supply (Vs-) is fixed to `GND`.***


The Nano R4's OPAMP offers the following electrical characteristics:

|       **Parameter**        | **Low-Speed Mode** | **High-Speed Mode** | **Unit** |       **Notes**        |
| :------------------------: | :----------------: | :-----------------: | :------: | :--------------------: |
| Common Input Voltage Range |    +1.8 to +5.5    |    +0.3 to +4.4     |   VDC    | Typical with 5V supply |
|    Output Voltage Range    |    +0.1 to +4.9    |    +0.1 to +4.9     |   VDC    | Typical with 5V supply |
|    Input Offset Voltage    |     -10 to +10     |     -10 to +10      |    mV    |           -            |
|       Open Loop Gain       |    60 (typical)    |    125 (typical)    |    dB    |           -            |
|   Gain-Bandwidth Product   |         -          |         1.7         |   MHz    |    High-speed mode     |
|         Slew Rate          |        0.12        |          -          |   V/μs   |       CL = 20 pF       |
|       Settling Time        |        650         |         13          |    μs    |     To 1% accuracy     |
|        Load Current        |    -100 to +100    |    -100 to +100     |    μA    |        Maximum         |
|      Load Capacitance      |         20         |         20          |    pF    |        Maximum         |

You can configure and use the OPAMP using the dedicated `OPAMP.h` library, which is included in the Arduino UNO R4 Boards core. To startup the OPAMP, simply include the library and call `OPAMP.begin(speed)` where speed can be `OPAMP_SPEED_LOWSPEED` for lower power consumption or `OPAMP_SPEED_HIGHSPEED` for better performance.

The following example demonstrates how to initialize and use the OPAMP. The same code works for both voltage follower and amplifier configurations, **the difference is only in the external connections**:

```arduino
/**
OPAMP Example for the Arduino Nano R4 Board
Name: nano_r4_opamp_example.ino
Purpose: This sketch demonstrates how to initialize the built-in OPAMP.
Works for both voltage follower and amplifier configurations.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include <OPAMP.h>

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - OPAMP Example started...");
  Serial.println("- Initializing OPAMP in high-speed mode...");
  
  // Initialize OPAMP in high-speed mode
  OPAMP.begin(OPAMP_SPEED_HIGHSPEED);
  
  Serial.println("- OPAMP initialized successfully!");
  Serial.println("- OPAMP is now ready for use with external connections");
  Serial.println("- The behavior depends on how you connect the external components");
}

void loop() {
  // The OPAMP operates automatically based on external connections
  // No additional code needed in the loop
  
  Serial.println("- OPAMP running...");
  delay(2000);
}
```

To configure the OPAMP as a **voltage follower**, connect the Nano R4 board as follows:

- Connect pin `A2` (-) to pin `A3` (Output) with a jumper wire
- Connect the input signal to pin `A1` (+)

For testing, connect pin `A1` to `GND` to see 0 VDC output, or connect pin `A1` to +3.3 VDC to verify voltage following.

![Voltage follower test circuit on the Nano R4 board](assets/opamp-1.png)

***In voltage follower configuration, any voltage applied at `A1` should be mirrored onto `A3`. This provides a high-impedance buffer that doesn't load down the input signal source.***

The Nano R4 OPAMP can also be configured as a **non-inverting amplifier** to amplify small signals. For example, a simple 2x amplifier can be built using two 10k Ω resistors as follows:

- Connect one 10k Ω resistor between `A2` (-) and `GND`
- Connect another 10k Ω resistor between `A3` (Output) and `A2` (-)

For testing, apply an input signal to `A1` (+).

![Non inverting amplifier test circuit on the Nano R4 board](assets/opamp-2.png)

The output at `A3` will be double the amplitude of the input signal.

***In a non-inverting amplifier configuration, remember that the input signal and the Nano R4 should share the same GND, and the amplified output signal should not exceed approximately +4.7 VDC to avoid clipping.***

## Digital-to-Analog Converter (DAC)

The Nano R4 features a built-in 12-bit Digital-to-Analog Converter (DAC) connected to pin `A0`. Unlike PWM pins that simulate analog output through rapid switching, the DAC provides true analog voltage output. This makes it ideal for applications requiring precise analog signals, such as audio generation, sensor calibration, control systems and waveform generation.

The Nano R4 DAC provides the following functionality:

|  **Specification**   |     **Value**     |            **Notes**             |
| :------------------: | :---------------: | :------------------------------: |
|      Resolution      |      12-bit       |   4096 discrete output levels    |
|      Output Pin      |       `A0`        |     Dedicated DAC output pin     |
| Output Voltage Range | +0.35 to +4.5 VDC | Typical range with +5 VDC supply |
|  Default Resolution  |       8-bit       |             0 to 255             |
|  Maximum Resolution  |      12-bit       |            0 to 4095             |
|   Output Impedance   |   5Ω (typical)    |       Low impedance output       |
|   Conversion Time    |     Max 30 μs     |  Time to update output voltage   |
|    Resistive Load    |     Min 30 kΩ     |     Minimum recommended load     |
|   Load Capacitance   |     Max 50 pF     |     Maximum capacitive load      |

***__Important note:__ When using the DAC on pin `A0`, this pin cannot simultaneously be used as an analog input. The DAC provides true analog output, making it superior to PWM for applications requiring smooth, continuous voltage levels.***


The Nano R4's DAC offers the following technical specifications:

|          **Parameter**          | **Min** | **Typ** | **Max** | **Unit** |      **Notes**      |
| :-----------------------------: | :-----: | :-----: | :-----: | :------: | :-----------------: |
| Differential Nonlinearity (DNL) |    -    |  ±0.5   |  ±2.0   |   LSB    |      DNL error      |
|   Integral Nonlinearity (INL)   |    -    |  ±2.0   |  ±16.0  |   LSB    |      INL error      |
|          Offset Error           |    -    |    -    |   ±30   |    mV    |    Output offset    |
|        Full-Scale Error         |    -    |    -    |   ±30   |    mV    | Full-scale accuracy |

You can write analog values to the DAC using the `analogWrite()` function:

```arduino
analogWrite(DAC, value);
```

The default resolution is 8-bit (0 to 255), but this can be changed using the `analogWriteResolution()` function. You can use `analogWriteResolution(8)` for 8-bit resolution, `analogWriteResolution(10)` for 10-bit resolution or `analogWriteResolution(12)` for maximum 12-bit resolution.

The DAC reference voltage depends on the selected reference mode, and the output voltage is calculated as: `Output Voltage = (DAC_Value / 4095) × Reference_Voltage`. The output voltage range is typically from +0.35 VDC to +4.5 VDC when using the supply voltage as reference.

***The following examples demonstrate basic DAC functionality that you can easily test with the Nano R4 board.***

The following example demonstrates how to generate a simple voltage output using the DAC. **No external components are needed for this example**:

```arduino
/**
DAC Basic Output Example for the Arduino Nano R4 Board
Name: nano_r4_dac_basic.ino
Purpose: This sketch demonstrates how to use the DAC to generate
precise analog voltages on pin A0.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Set DAC resolution to 12-bit for maximum precision
  analogWriteResolution(12);
  
  Serial.println("- Arduino Nano R4 - DAC Basic Output Example started...");
  Serial.println("- Generating precise voltages on pin A0");
  Serial.println("- Connect a multimeter to A0 to measure output");
}

void loop() {
  // Generate different voltage levels
  // 0, +1.25, +2.5, +3.75 and +5 VDC
  int dacValues[] = {0, 1024, 2048, 3072, 4095}; 
  float voltages[] = {0.0, 1.25, 2.5, 3.75, 5.0};
  
  for (int i = 0; i < 5; i++) {
    analogWrite(DAC, dacValues[i]);
    
    Serial.print("- DAC Value: ");
    Serial.print(dacValues[i]);
    Serial.print(" | Target Voltage: ");
    Serial.print(voltages[i], 2);
    Serial.println(" VDC");
    
    // Hold each voltage for 2 seconds
    delay(2000);  
  }
  
  Serial.println("- Cycle completed, repeating...");
  delay(1000);
}
```

To test this example, connect a digital multimeter between pin `A0` and `GND` to measure the output voltage. You should see the voltage change in precise steps every two seconds, showing the DAC's ability to generate exact analog voltages. For best results, connect an oscilloscope to pin `A0` to visualize the step output.

![Step output oscilloscope output](assets/dac-1.png)

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the DAC values and corresponding target voltages. The output should closely match the calculated voltages with high precision.

The following example demonstrates how to generate a smooth sine wave using the DAC. **No external components are needed for this example**:

```arduino
/**
DAC Sine Wave Generator for the Arduino Nano R4 Board
Name: nano_r4_dac_sine_wave.ino
Purpose: This sketch generates a smooth sine wave using the 12-bit DAC
for testing and signal generation applications.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Set DAC resolution to 12-bit for smooth waveform
  analogWriteResolution(12);
  
  Serial.println("- Arduino Nano R4 - DAC Sine Wave Generator started...");
  Serial.println("- Generating sine wave on pin A0");
  Serial.println("- Connect an oscilloscope to A0 to view waveform");
}

void loop() {
  // Generate one complete sine wave cycle (360 degrees)
  for (int angle = 0; angle < 360; angle++) {
    // Calculate sine value (-1 to +1) and convert to DAC range (0 to 4095)
    float sineValue = sin(angle * PI / 180.0);
    int dacValue = (int)((sineValue + 1.0) * 2047.5);  // Center at +2.5 VDC
    
    // Output the calculated value to DAC
    analogWrite(DAC, dacValue);
    
    // Print debug info every 30 degrees
    if (angle % 30 == 0) {
      float voltage = (dacValue / 4095.0) * 5.0;
      Serial.print("- Angle: ");
      Serial.print(angle);
      Serial.print("° | DAC: ");
      Serial.print(dacValue);
      Serial.print(" | Voltage: ");
      Serial.print(voltage, 2);
      Serial.println(" VDC");
    }
    
    // Control wave frequency (~28 Hz)
    delayMicroseconds(100);  
  }
}
```

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the sine wave generation progress with angle, DAC values, and corresponding voltages. 

For best results, connect an oscilloscope to pin `A0` to visualize the smooth sine wave output.

![Sine wave output oscilloscope output](assets/dac-2.png)

## Real-Time Clock (RTC)

The Nano R4 features a built-in Real-Time Clock (RTC) that allows your projects to keep track of date and time. The RTC is integrated within the RA4M1 microcontroller and can maintain accurate timekeeping for applications that require scheduling, data logging or time-based events. With optional backup power support via the board's `VBATT` pin, the RTC can continue running even when the main power is disconnected, using a 100-year calendar from 2000 to 2099 that automatically adjusts dates for leap years.

The RTC is particularly useful when your project needs to know the actual date and time, rather than just measuring time intervals. While Arduino functions like `millis()` and `delay()` are perfect for timing operations (like blinking an LED every second), the RTC is essential for applications like data loggers that need timestamps, alarm clocks, scheduling systems or any project that needs to know "what time is it right now?" even after being powered off and on again.

The Nano R4's RTC offers the following technical specifications:

|    **Parameter**    |   **Value**    |     **Notes**     |
| :-----------------: | :------------: | :---------------: |
|     Time Range      |  2000 to 2099  | 100-year calendar |
|   Backup Voltage    |  1.6V to 3.6V  |   Via VBATT pin   |
| Current Consumption |     ~1 μA      |  In backup mode   |
|  Temperature Range  | -40°C to +85°C |  Operating range  |

You can configure and use the RTC using the dedicated `RTC.h` library, which is included in the Arduino UNO R4 Boards core. The library provides functions to set time, get time, check RTC status and configure alarms.

The following example demonstrates how to initialize the RTC and display the current date and time:

```arduino
/**
RTC Basic Example for the Arduino Nano R4 Board
Name: nano_r4_rtc_basic.ino
Purpose: This sketch demonstrates how to use the built-in RTC
to keep track of date and time.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include "RTC.h"

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - RTC Basic Example started...");
  Serial.println("- Initializing RTC...");
  
  // Initialize RTC
  RTC.begin();
  
  // Set initial time: January 15, 2025, 12:00:00 PM, Monday
  RTCTime startTime(15, Month::JANUARY, 2025, 12, 0, 0, DayOfWeek::MONDAY, SaveLight::SAVING_TIME_INACTIVE);
  RTC.setTime(startTime);
  
  Serial.println("- RTC time has been set to January 15, 2025, 12:00:00 PM");
  Serial.println("- Current date and time will be displayed every second");
}

void loop() {
  // Get current time from RTC
  RTCTime currentTime;
  RTC.getTime(currentTime);
  
  // Get individual values
  int year = currentTime.getYear();
  int month = Month2int(currentTime.getMonth());
  int day = currentTime.getDayOfMonth();
  
  int hour = currentTime.getHour();
  int minute = currentTime.getMinutes();
  int second = currentTime.getSeconds();
  
  // Display date (YYYY/MM/DD)
  Serial.print("Date: ");
  Serial.print(year);
  Serial.print("/");
  if (month < 10) Serial.print("0");
  Serial.print(month);
  Serial.print("/");
  if (day < 10) Serial.print("0");
  Serial.print(day);
  
  // Display time (HH:MM:SS)
  Serial.print(" | Time: ");
  if (hour < 10) Serial.print("0");
  Serial.print(hour);
  Serial.print(":");
  if (minute < 10) Serial.print("0");
  Serial.print(minute);
  Serial.print(":");
  if (second < 10) Serial.print("0");
  Serial.print(second);
  
  // Display day of week
  Serial.print(" | Day: ");
  DayOfWeek dayOfWeek = currentTime.getDayOfWeek();
  
  if (dayOfWeek == DayOfWeek::MONDAY) {
    Serial.print("Monday");
  } else if (dayOfWeek == DayOfWeek::TUESDAY) {
    Serial.print("Tuesday");
  } else if (dayOfWeek == DayOfWeek::WEDNESDAY) {
    Serial.print("Wednesday");
  } else if (dayOfWeek == DayOfWeek::THURSDAY) {
    Serial.print("Thursday");
  } else if (dayOfWeek == DayOfWeek::FRIDAY) {
    Serial.print("Friday");
  } else if (dayOfWeek == DayOfWeek::SATURDAY) {
    Serial.print("Saturday");
  } else if (dayOfWeek == DayOfWeek::SUNDAY) {
    Serial.print("Sunday");
  }
  
  Serial.println();
  
  // Wait one second before next reading
  delay(1000);
}
```

***To test this example, no external connections are needed. The RTC operates internally within the microcontroller.***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the real-time date and time updates. The display will show the current date, time, and day of the week, updating every second.

![Arduino IDE Serial Monitor output for the RTC example sketch](assets/rtc-1.png)

To maintain RTC timekeeping when the main power is disconnected, you can connect a backup battery to the `VBATT` pin:

- Connect the positive terminal of a 3V coin cell battery (CR2032) to the `VBATT` pin of the board
- Connect the negative terminal of the battery to `GND`

With this configuration, the board's RTC will continue running on backup power when main power is removed. You can also set the board's RTC time programmatically using the following format. Remember to update the date and time values to match the current date when you upload your sketch:

```arduino
// Create RTCTime object with current date and time
// Format: day, month, year, hour, minute, second, dayOfWeek, daylightSaving
RTCTime newTime(30, Month::JUNE, 2025, 15, 30, 45, DayOfWeek::MONDAY, SaveLight::SAVING_TIME_INACTIVE);

// Set the RTC time
RTC.setTime(newTime);
```

When working with the RTC on the Nano R4, there are several key points to keep in mind for successful implementation:

- **The RTC requires an initial time setting** before it can provide accurate timekeeping, so make sure to configure the date and time when you first start your project. For applications that need continuous timekeeping even when the main power is disconnected, connecting a backup battery to the VBATT pin is highly recommended. 
- Keep in mind that **the RTC stores time exactly as you set it**, so you'll need to handle time zone conversions and daylight saving time adjustments in your application code if needed.

## EEPROM (Non-Volatile Memory)

The Nano R4 board features built-in EEPROM (Electrically Erasable Programmable Read-Only Memory) that allows your projects to store data permanently, even when the board is powered off. The EEPROM is implemented using flash memory emulation within the RA4M1 microcontroller and provides 8 KB of non-volatile storage space for applications that need to remember settings, sensor calibrations, or user preferences between power cycles.

EEPROM is particularly useful when your project needs to remember information permanently, rather than just during program execution. While variables stored in SRAM are lost when power is removed, EEPROM retains data indefinitely. This makes it essential for applications like saving user preferences, storing sensor calibration values, keeping configuration settings, or any project that needs to "remember" data even after being unplugged and reconnected.

The Nano R4's EEPROM offers the following technical specifications:

|   **Parameter**   |     **Value**     |         **Notes**        |
|:-----------------:|:-----------------:|:------------------------:|
|      Capacity     |        8 KB       |         Data area        |
|    Memory Type    | Data flash memory |  SuperFlash® technology  |
|    Write Cycles   |      100,000      | Program/erase cycles max |
|  Programming Unit |       64-bit      |    Minimum write unit    |
|     Erase Unit    |        1 KB       |    Minimum erase unit    |
|     Read Speed    |   6 clock cycles  |     Time to read data    |
|   Retention Time  |     10+ years     |   Data retention period  |
| Operating Voltage |       +5 VDC      |       Same as board      |

You can read and write to EEPROM using the dedicated `EEPROM.h` library, which is included in the Arduino UNO R4 Boards core. The library provides simple functions to store and retrieve individual bytes or larger data structures.

The following example demonstrates how to store and retrieve data from EEPROM:

```arduino
/**
EEPROM Basic Example for the Arduino Nano R4 Board
Name: nano_r4_eeprom_basic.ino
Purpose: This sketch demonstrates how to store and retrieve data
from the built-in EEPROM memory.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include <EEPROM.h>

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - EEPROM Basic Example started...");
  
  // Read a counter from EEPROM address 0
  int bootCounter = EEPROM.read(0);
  
  // If this is the first time (EEPROM starts with 255), set counter to 0
  if (bootCounter == 255) {
    bootCounter = 0;
    Serial.println("- First boot detected!");
  }
  
  // Add 1 to the counter
  bootCounter = bootCounter + 1;
  
  // Save the new counter value to EEPROM
  EEPROM.write(0, bootCounter);
  
  // Show the results
  Serial.print("- This board has been reset ");
  Serial.print(bootCounter);
  Serial.println(" times");
  
  // Store a user preference (LED brightness)
  int brightness = 128;  // Value from 0 to 255
  EEPROM.write(1, brightness);
  Serial.print("- LED brightness setting saved: ");
  Serial.println(brightness);
  
  // Read the brightness setting back
  int savedBrightness = EEPROM.read(1);
  Serial.print("- LED brightness setting loaded: ");
  Serial.println(savedBrightness);
  
  Serial.println("- Reset the board to see the counter increase!");
}

void loop() {
  // Nothing to do in the loop
  // The counter only increases when you reset the board
  delay(1000);
}
```

***To test this example, no external connections are needed. The EEPROM operates internally within the microcontroller.***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the EEPROM operations. Each time you reset the board, the boot counter will increment, demonstrating that the value persists in EEPROM memory.

![Arduino IDE Serial Monitor output for the EEPROM example sketch](assets/eeprom-1.png)

You can also store complex data structures using the `EEPROM.put()` and `EEPROM.get()` functions:

```arduino
// Define a structure for complex data
struct Settings {
  int threshold;
  float calibration;
  bool enabled;
  char deviceName[16];
};

// Store structure to EEPROM
Settings mySettings = {512, 3.14, true, "NanoR4Device"};
EEPROM.put(0, mySettings);

// Read structure from EEPROM
Settings loadedSettings;
EEPROM.get(0, loadedSettings);
```

When working with EEPROM on the Nano R4, there are several key points to keep in mind for successful implementation:

- The EEPROM requires careful management of write operations since flash memory has a limited number of write cycles (100,000). Avoid writing to the same address repeatedly in tight loops, as this will quickly wear out the memory. Instead, only write when values actually change, and consider spreading data across different addresses to distribute wear evenly.
- Keep in mind that EEPROM stores data as individual bytes (0 to 255), so larger data types need to be broken down or use the `put()` and `get()` functions for automatic handling.
- The EEPROM retains data for over 10 years under normal conditions, making it excellent for long-term storage of configuration data and user preferences.

## UART Communication

The Nano R4 board features built-in UART (Universal Asynchronous Receiver-Transmitter) communication that allows your projects to communicate with other devices through serial data transmission. UART is implemented within the RA4M1 microcontroller and provides two separate hardware serial ports: one connected to the USB-C connector for computer communication, and another available on pins `D0` and `D1` for external device communication. This makes it perfect for projects that need to communicate with sensors, modules or other microcontrollers while maintaining USB connectivity for debugging.

UART is particularly useful when your project needs to communicate with devices that require simple, reliable serial communication, rather than the more complex protocols like SPI or I²C. While SPI excels at high-speed communication and I²C is ideal for multiple device networks, UART provides straightforward point-to-point communication that works well with GPS modules, Bluetooth® modules, Wi-Fi® modules and other serial devices. UART communication is asynchronous, meaning it doesn't require a shared clock signal, making it robust over longer distances.

The Nano R4's UART interface offers the following technical specifications:

|   **Parameter**   |    **Value**   |       **Notes**      |
|:-----------------:|:--------------:|:--------------------:|
|     Baud Rates    | 300 to 2000000 | Common: 9600, 115200 |
|     Data Bits     |      8-bit     |  Standard data width |
|   Communication   |   Full-duplex  |  Simultaneous TX/RX  |
|   Hardware Ports  |        2       | USB Serial + Serial1 |
|     UART Pins     |   `D0`, `D1`   |  RX, TX respectively |
| Operating Voltage |     +5 VDC     |   TTL logic levels   |
|    Flow Control   |    Software    |  XON/XOFF supported  |

The Nano R4 board uses the following pins for UART communication:

| **Arduino Pin** | **Microcontroller Pin** | **UART Function** | **Description** |
|:---------------:|:-----------------------:|:-----------------:|:---------------:|
|       `D0`      |          `P104`         |         RX        |   Receive Data  |
|       `D1`      |          `P105`         |         TX        |  Transmit Data  |

You can communicate via UART using the built-in `Serial` and `Serial1` objects. The `Serial` object is connected to the USB-C port for computer communication, while `Serial1` is connected to pins `D0` and `D1` for external device communication.

The following example demonstrates basic UART communication patterns:

```arduino
/**
UART Basic Example for the Arduino Nano R4 Board
Name: nano_r4_uart_basic.ino
Purpose: This sketch demonstrates basic UART communication
using both USB Serial and hardware Serial1.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

void setup() {
  // Initialize USB serial communication at 115200 baud
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Initialize hardware serial on pins D0/D1 at 9600 baud
  Serial1.begin(9600);
  
  Serial.println("- Arduino Nano R4 - UART Basic Example started...");
  Serial.println("- USB Serial (Serial): 115200 baud");
  Serial.println("- Hardware Serial (Serial1): 9600 baud on D0/D1");
  Serial.println("- Connect logic analyzer to D0 (RX) and D1 (TX)");
  Serial.println("- Type messages in Serial Monitor to send via Serial1");
  Serial.println();
}

void loop() {
  // Check for data from USB Serial (computer)
  if (Serial.available()) {
    String message = Serial.readString();

    // Remove newline characters
    message.trim(); 
    
    if (message.length() > 0) {
      Serial.print("- USB received: \"");
      Serial.print(message);
      Serial.println("\"");
      
      // Send the message via Serial1 (D0/D1)
      Serial1.print("- Message from USB: ");
      Serial1.println(message);
      
      Serial.println("- Message sent via Serial1 (D0/D1)!");
    }
  }
  
  // Check for data from Serial1 (external device on D0/D1)
  if (Serial1.available()) {
    String response = Serial1.readString();

    // Remove newline characters
    response.trim(); 
    
    if (response.length() > 0) {
      Serial.print("- Serial1 received: \"");
      Serial.print(response);
      Serial.println("\"");
    }
  }
  
  // Send periodic test data via Serial1
  static unsigned long lastSend = 0;
  if (millis() - lastSend > 3000) {
    lastSend = millis();
    
    // Send test data with timestamp
    Serial1.print("Test data: ");
    Serial1.print(millis());
    Serial1.println(" ms");
    
    Serial.println("- Periodic test data sent via Serial1!");
  }
  
  delay(10);
}
```

***To test this example, no external UART devices are required, the code will demonstrate UART communication patterns that can be observed with a logic analyzer. You can type messages in the Arduino IDE's Serial Monitor to see them transmitted via `Serial1` on pins `D0`/`D1`.***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to interact with the USB serial port and observe the communication patterns. Connect a logic analyzer to pins `D0` (RX) and `D1` (TX) to observe the actual UART protocol signals.

![Arduino IDE Serial Monitor output for the UART example sketch](assets/uart-1.png)

The image below shows how the UART communication from our example appears in the Digilent Waveforms logic analyzer software, with the decoded protocol showing the transmitted data bytes and timing.

![Digilent Waveforms logic analyzer output for UART](assets/uart-2.png)

The Nano R4 board provides two distinct UART communication channels, giving you the flexibility to handle multiple communication tasks simultaneously. The first channel is the USB Serial (`Serial`), which is your primary interface for programming and debugging. This channel offers several key features:

- Connected to the onboard USB-C connector
- Used for programming and debugging
- Typically runs at 115200 baud
- Automatic baud rate detection
- No external connections required 

The second channel is the Hardware Serial (`Serial1`), which is dedicated to external device communication. This channel provides robust connectivity for your project peripherals:

- Connected to pins `D0` (RX) and `D1` (TX)
- Used for external device communication
- Configurable baud rate (300 to 2000000)
- TTL voltage levels (0 VDC/+5 VDC)
- Requires external device connection

Here is a practical example of how to use both UART channels simultaneously, such as when connecting a GPS module:

```arduino
// Example: Connecting a GPS module via Serial1
void setup() {
  Serial.begin(115200);   // USB debugging
  Serial1.begin(9600);    // GPS module communication
  
  Serial.println("GPS module communication started");
}

void loop() {
  // Forward GPS data to USB Serial for monitoring
  if (Serial1.available()) {
    String gpsData = Serial1.readString();
    Serial.print("GPS: ");
    Serial.print(gpsData);
  }
  
  // Send commands to GPS module from USB Serial
  if (Serial.available()) {
    String command = Serial.readString();
    Serial1.print(command);
    Serial.println("Command sent to GPS");
  }
}
```

When working with UART on the Nano R4, there are several key points to keep in mind for successful implementation: 

- The dual UART design is different from the UNO R3 board that shared one UART between USB and pins D0/D1. This separation allows simultaneous USB debugging and external device communication. 
- Always ensure that both devices use the same baud rate, data bits (typically 8), and stop bits (typically 1) for successful communication.
- Keep in mind that UART communication uses TTL voltage levels (0 VDC for logic `LOW`, +5 VDC for logic `HIGH`). If you need to communicate over longer distances or with RS-232 devices, you'll need a level converter. 
- When connecting external devices, remember that TX connects to RX and RX connects to TX (crossover connection). 
- The Nano R4's UART ports are full-duplex, meaning they can send and receive data simultaneously, making them perfect for interactive communication with modules like GPS, Bluetooth®, Wi-Fi®, or other microcontrollers.

## SPI Communication

The Nano R4 board features built-in SPI (Serial Peripheral Interface) communication that allows your projects to communicate with external devices like sensors, displays, memory cards and other microcontrollers. SPI is implemented within the RA4M1 microcontroller and uses four dedicated pins to provide high-speed synchronous serial communication.

SPI is particularly useful when your project needs to communicate with external components at high speeds, rather than using slower protocols. While I²C is perfect for simple sensor communication and UART for basic serial data exchange, SPI excels at high-speed communication with devices like SD cards, TFT displays, wireless modules or external memory chips. SPI can achieve much faster data rates than I²C and can handle multiple devices on the same bus through individual chip select lines.

The Nano R4's SPI interface offers the following technical specifications:

|   **Parameter**   |   **Value**  |          **Notes**          |
|:-----------------:|:------------:|:---------------------------:|
|    Clock Speed    | Up to 24 MHz |    Maximum SPI frequency    |
|   Data Transfer   |     8-bit    |     Standard data width     |
|   Communication   |  Full-duplex |  Simultaneous send/receive  |
|      SPI Pins     |  `D10`-`D13` | `CS`, `MOSI`, `MISO`, `SCK` |
|  Multiple Devices |   Supported  |   Via different `CS` pins   |
| Operating Voltage |    +5 VDC    |        Same as board        |
|  Protocol Support | Mode 0,1,2,3 |   All SPI modes available   |

The Nano R4 board uses the following pins for SPI communication:

| **Arduino Pin** | **Microcontroller Pin** | **SPI Function** |    **Description**   |
|:---------------:|:-----------------------:|:----------------:|:--------------------:|
|      `D10`      |          `P103`         |       `CS`       |      Chip Select     |
|      `D11`      |          `P101`         |      `MOSI`      | Master Out, Slave In |
|      `D12`      |          `P100`         |      `MISO`      | Master In, Slave Out |
|      `D13`      |          `P102`         |       `SCK`      |     Serial Clock     |

You can communicate via SPI using the dedicated `SPI.h` library, which is included in the Arduino UNO R4 Boards core. The library provides simple functions to initialize the bus, send and receive data and manage multiple devices.

The following example demonstrates how to use SPI communication to send and receive data:

```arduino
/**
SPI Basic Example for the Arduino Nano R4 Board
Name: nano_r4_spi_basic.ino
Purpose: This sketch demonstrates how to use SPI communication
to send and receive data.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include <SPI.h>

// Chip Select pin for SPI device
const int CS_PIN = 10;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - SPI Basic Example started...");
  
  // Set CS pin as output and set it HIGH (inactive)
  pinMode(CS_PIN, OUTPUT);
  digitalWrite(CS_PIN, HIGH);
  
  // Initialize SPI communication
  SPI.begin();
  
  // Configure SPI settings
  // - Clock speed: 1 MHz (1000000 Hz)
  // - Data order: Most Significant Bit first
  // - Data mode: Mode 0 (Clock polarity = 0, Clock phase = 0)
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
  
  Serial.println("- SPI initialized successfully");
  Serial.println("- Ready to communicate with SPI devices");
  
  // Example: Send some test data
  sendSPIData();
}

void loop() {
  // Send a counter value every 2 seconds
  static int counter = 0;
  
  // Select the device (CS LOW)
  digitalWrite(CS_PIN, LOW);
  
  // Send counter value
  byte response = SPI.transfer(counter);
  
  // Deselect the device (CS HIGH)
  digitalWrite(CS_PIN, HIGH);
  
  // Display results
  Serial.print("- Sent: ");
  Serial.print(counter);
  Serial.print(" | Received: ");
  Serial.println(response);
  
  // Increment counter and wrap around at 255
  counter++;
  if (counter > 255) {
    counter = 0;
  }
  
  delay(2000);
}

void sendSPIData() {
  Serial.println("- Sending test data...");
  
  // Select the device
  digitalWrite(CS_PIN, LOW);
  
  // Send a sequence of test bytes
  for (int i = 0; i < 5; i++) {
    byte testData = 0x10 + i;  // Send 0x10, 0x11, 0x12, 0x13, 0x14
    byte response = SPI.transfer(testData);
    
    Serial.print("  Sent: 0x");
    if (testData < 16) Serial.print("0");
    Serial.print(testData, HEX);
    Serial.print(" | Received: 0x");
    if (response < 16) Serial.print("0");
    Serial.println(response, HEX);
    
    delay(100);
  }
  
  // Deselect the device
  digitalWrite(CS_PIN, HIGH);
  
  Serial.println("- Test data transmission complete");
}
```

***To test this example, no external SPI device is required. The code will demonstrate SPI communication patterns, though without a connected device, the received data will typically be `0xFF`.***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the SPI communication in action. The example sketch shows how to properly select devices, send data and handle responses.

![Arduino IDE Serial Monitor output for the SPI example sketch](assets/spi-1.png)

The image below shows how the SPI communication from our example appears in the Digilent Waveforms logic analyzer software, with the decoded protocol showing the chip select, clock and data signals being transmitted.

![Digilent Waveforms logic analyzer output for SPI](assets/spi-2.png)

For connecting multiple SPI devices, you can use different digital pins as additional Chip Select (`CS`) lines while sharing the `MOSI`, `MISO` and `SCK` pins:

```arduino
// Multiple device example
const int DEVICE1_CS = 10;  // First SPI device
const int DEVICE2_CS = 9;   // Second SPI device
const int DEVICE3_CS = 8;   // Third SPI device

void setup() {
  SPI.begin();
  
  // Configure all CS pins
  pinMode(DEVICE1_CS, OUTPUT);
  pinMode(DEVICE2_CS, OUTPUT);
  pinMode(DEVICE3_CS, OUTPUT);
  
  // Set all CS pins HIGH (inactive)
  digitalWrite(DEVICE1_CS, HIGH);
  digitalWrite(DEVICE2_CS, HIGH);
  digitalWrite(DEVICE3_CS, HIGH);
}
```

When working with SPI on the Nano R4, there are several key points to keep in mind for successful implementation:

- The SPI protocol requires careful attention to timing and device selection. Always ensure that only one device is selected (`CS LOW`) at a time, and remember to deselect devices (`CS HIGH`) after communication to avoid conflicts.
- Different SPI devices may require different clock speeds and modes, so check your device's datasheet for the correct `SPISettings()` parameters.
- Keep in mind that SPI is a synchronous protocol, meaning that data is transferred in both directions simultaneously with each clock pulse. Even if you only need to send data, you'll still receive data back, and vice versa.
- The Nano R4 board can communicate with multiple SPI devices by using different Chip Select (`CS`) pins, making it perfect for complex projects that need to interface with various sensors, displays and storage devices.

## I²C Communication

The Nano R4 board features built-in I²C (Inter-Integrated Circuit) communication that allows your projects to communicate with multiple devices using just two wires. I²C is implemented within the RA4M1 microcontroller and uses two dedicated pins to provide reliable serial communication with sensors, displays, memory modules and other microcontrollers. This makes it perfect for projects that need to connect several devices without using many pins.

***__CRITICAL WARNING__: The Nano R4's I²C pins (A4/A5) operate at +5 VDC logic levels WITHOUT built-in level shifting. Directly connecting +3.3 VDC I²C devices to these pins may damage them permanently. This is different from many other Nano family boards that operate at +3.3 VDC.***

Understanding the voltage differences between the Nano R4's I²C interfaces is important for protecting your components. The board offers two different I²C connection methods, each with distinct voltage characteristics. The following table summarizes these critical differences:

|  **Interface**  | **Operating Voltage** | **Level Shifting** | **Safe for +3.3 VDC Devices** |
|:---------------:|:---------------------:|:------------------:|:-----------------------------:|
|    Pins A4/A5   |         +5 VDC        |        None        | ❌ No (Requires level shifter) |
| Qwiic Connector |        +3.3 VDC       |      Built-in      |   ✅ Yes (direct connection)   |

When you need to connect +3.3 VDC I²C devices to your Nano R4 board, you have three main options to ensure safe and reliable operation:

1. **Use the Qwiic connector `Wire1`**: This is the simplest solution as it provides automatic level translation and +3.3 VDC power supply for your devices
2. **Add an external level shifter**: Bi-directional I²C level translators like the [SparkFun Logic Level Converter (BOB-12009)](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html) or the [Adafruit 4-Channel I2C-Safe Bi-directional Logic Level Converter (BSS138)](https://www.adafruit.com/product/757) can safely convert between +5 VDC and +3.3 VDC logic levels

3. **Use +5 VDC-compatible sensors**: Select I²C devices specifically designed to operate at +5 VDC to avoid any compatibility issues

### I²C Overview

I²C is particularly useful when your project needs to communicate with multiple sensors and devices in a simple way, rather than using complex wiring. While SPI is excellent for high-speed communication and UART for basic serial data exchange, I²C excels at connecting many devices with minimal wiring. Multiple I²C devices can share the same two-wire bus, each with its own unique address, making it ideal for sensor networks, display modules and expandable systems.

The Nano R4's I²C interface offers the following technical specifications:

|   **Parameter**   |     **Value**     |          **Notes**         |
|:-----------------:|:-----------------:|:--------------------------:|
|    Clock Speed    |   Up to 400 kHz   |     Standard/Fast mode     |
|   Data Transfer   |       8-bit       |     Standard data width    |
|   Communication   |    Half-duplex    |   One direction at a time  |
|      I²C Pins     |     `A4`, `A5`    |    SDA, SCL respectively   |
| Device Addressing |    7-bit/10-bit   | Up to 127 unique addresses |
| Operating Voltage |       +5 VDC      |        Same as board       |
| Pull-up Resistors | External required |    No internal pull-ups    |

The Nano R4 uses the following pins for I²C communication:

| **Arduino Pin** | **Microcontroller Pin** | **I²C Function** |  **Description**  |
|:---------------:|:-----------------------:|:----------------:|:-----------------:|
|       `A4`      |          `P004`         |        SDA       |  Serial Data Line |
|       `A5`      |          `P010`         |        SCL       | Serial Clock Line |

You can communicate via I²C using the dedicated `Wire.h` library, which is included in the Arduino UNO R4 Boards core. The library provides simple functions to initialize the bus, send and receive data and manage multiple devices.

***__Important note__: The Nano R4 board has two I²C interfaces. Use `Wire` for the standard I²C interface on pins `A4/A5` (+5 VDC logic), and `Wire1` for the Qwiic connector (+3.3 VDC with built-in level shifting). This dual-interface design allows you to separate +5 VDC and +3.3 VDC I²C devices on different buses if needed.***

The following example demonstrates basic I²C communication patterns:

```arduino
/**
I2C Basic Example for the Arduino Nano R4 Board
Name: nano_r4_i2c_basic.ino
Purpose: This sketch demonstrates basic I2C communication
patterns for protocol analysis.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include <Wire.h>

// Example device address
const int DEVICE_ADDRESS = 0x48;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - I2C Basic Example started...");
  
  // Initialize I2C communication as master
  Wire.begin();
  
  Serial.println("- I2C initialized successfully");
  Serial.println("- Connect protocol analyzer to A4 (SDA) and A5 (SCL)");
  Serial.println("- Starting I2C communication patterns...");
  
  delay(2000);
}

void loop() {
  // Write a single byte
  Serial.println("- Writing single byte (0xAA) to device 0x48...");
  Wire.beginTransmission(DEVICE_ADDRESS);
  Wire.write(0xAA);
  Wire.endTransmission();
  
  delay(1000);
  
  // Write multiple bytes
  Serial.println("- Writing multiple bytes (0x10, 0x20, 0x30) to device 0x48...");
  Wire.beginTransmission(DEVICE_ADDRESS);
  Wire.write(0x10);
  Wire.write(0x20);
  Wire.write(0x30);
  Wire.endTransmission();
  
  delay(1000);
  
  // Request data from device
  Serial.println("- Requesting 2 bytes from device 0x48...");
  Wire.requestFrom(DEVICE_ADDRESS, 2);
  
  // Read any available data
  while (Wire.available()) {
    int data = Wire.read();
    Serial.print("Received: 0x");
    if (data < 16) Serial.print("0");
    Serial.println(data, HEX);
  }
  
  delay(2000);
  Serial.println("---");
}
```
***To test this example, no external I²C devices are required. The code will generate I²C communication patterns that can be analyzed with a protocol analyzer. Without devices connected, read operations will typically return `0xFF`.***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the I²C operations being performed. Connect a protocol analyzer to pins `A4` (SDA) and `A5` (SCL) to observe the actual I²C protocol signals.

![Arduino IDE Serial Monitor output for the I²C example sketch](assets/i2c-1.png)

The image below shows how the I²C communication from our example appears in the Digilent Waveforms logic analyzer software, with the decoded protocol showing the device address and data bytes being transmitted.

![Arduino IDE Serial Monitor output for the I²C example sketch](assets/i2c-2.png)

***The I²C protocol requires pull-up resistors on both SDA and SCL lines. __The Nano R4 board does not have internal pull-ups on `A4` and `A5` to avoid interference with their analog input functionality, so external 4.7kΩ pull-up resistors to +5 VDC are required for proper I²C operation__.***

One of the main advantages of I²C is the ability to connect multiple devices to the same bus. Here is how to connect multiple I²C devices:

```arduino
// Example: Communicating with multiple I2C devices
void communicateWithMultipleDevices() {
  // Device addresses (examples)
  const int SENSOR_ADDRESS = 0x48;    // Temperature sensor
  const int DISPLAY_ADDRESS = 0x3C;   // OLED display
  const int EEPROM_ADDRESS = 0x50;    // External EEPROM
  
  // Read from temperature sensor
  Wire.beginTransmission(SENSOR_ADDRESS);
  Wire.write(0x00);  // Register to read
  Wire.endTransmission();
  
  Wire.requestFrom(SENSOR_ADDRESS, 2);
  if (Wire.available() >= 2) {
    int tempHigh = Wire.read();
    int tempLow = Wire.read();
    Serial.print("Temperature: ");
    Serial.println((tempHigh << 8) | tempLow);
  }
  
  // Send data to display
  Wire.beginTransmission(DISPLAY_ADDRESS);
  Wire.write(0x40);  // Data mode
  Wire.write(0xFF);  // Sample data
  Wire.endTransmission();
  
  // Write to EEPROM
  Wire.beginTransmission(EEPROM_ADDRESS);
  Wire.write(0x00);  // Memory address
  Wire.write(0x55);  // Data to write
  Wire.endTransmission();
}
```

When working with I²C on the Nano R4 board, there are several key points to keep in mind for successful implementation:

- Each I²C device must have a unique address on the bus, so check device datasheets to avoid address conflicts.
- Keep in mind that I²C is a half-duplex protocol, meaning data flows in only one direction at a time. The master device (your Nano R4 board) controls the clock line and initiates all communication.
- When connecting multiple devices, simply connect all SDA pins together and all SCL pins together, along with power and ground connections.
- The Nano R4 board can communicate with up to 127 different I²C devices on the same bus, making it perfect for complex sensor networks and expandable systems.

## CAN Communication

The Nano R4 board features built-in CAN (Controller Area Network) communication that allows your projects to communicate with automotive systems, industrial devices, and other CAN-enabled equipment. CAN is implemented within the RA4M1 microcontroller and uses two dedicated pins to provide robust, real-time communication over longer distances with multiple devices. This makes it perfect for automotive applications, industrial automation and distributed control systems that require reliable communication in noisy environments.

CAN is particularly useful when your project needs to communicate in industrial or automotive environments where reliability and noise immunity are critical, rather than simple point-to-point communication. While UART excels at simple serial communication and SPI provides high-speed data transfer, CAN offers multi-node networking with built-in error detection, collision handling and message prioritization. CAN communication is differential signaling, making it highly resistant to electromagnetic interference and suitable for harsh environments.

The Nano R4's CAN interface offers the following technical specifications:

|   **Parameter**   |   **Value**   |         **Notes**        |
|:-----------------:|:-------------:|:------------------------:|
|     Baud Rates    |  Up to 1 Mbps |    Configurable speed    |
|    Data Frames    |   0-8 bytes   |    Standard CAN frame    |
|   Communication   |  Multi-master |  Multiple nodes support  |
|      CAN Pins     |   `D4`, `D5`  |    TX, RX respectively   |
|    Message IDs    | 11-bit/29-bit | Standard/Extended format |
| Operating Voltage |     +5 VDC    | Requires CAN transceiver |
| External Hardware |    Required   |  CAN transceiver needed  |

The Nano R4 uses the following pins for CAN communication:

| **Arduino Pin** | **Microcontroller Pin** | **CAN Function** | **Description** |
|:---------------:|:-----------------------:|:----------------:|:---------------:|
|       `D4`      |          `P109`         |     `CAN_TX`     |   CAN Transmit  |
|       `D5`      |          `P110`         |     `CAN_RX`     |   CAN Receive   |

***__Important note__: The Nano R4's CAN interface provides logic-level signals only. You must use an external CAN transceiver (such as SN65HVD230 from Texas Instruments® or the MCP2561 from Microchip®) to convert these signals to the differential CAN bus levels (`CANH`/`CANL`) required for actual CAN communication.***

You can communicate via CAN using the built-in `Arduino_CAN` library included in the Arduino UNO R4 Boards core. The library provides functions to initialize the bus, send and receive CAN frames and handle message filtering.

The following example demonstrates basic CAN communication patterns: 

```arduino
/**
CAN Basic Example for the Arduino Nano R4 Board
Name: nano_r4_can_basic.ino
Purpose: This sketch demonstrates basic CAN communication
for automotive and industrial applications.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include <Arduino_CAN.h>

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - CAN Basic Example started...");
  
  // Initialize CAN communication at 500k baud
  if (!CAN.begin(CanBitRate::BR_500k)) {
    Serial.println("- Error: Failed to initialize CAN bus!");
    while (1) delay(10);
  }
  
  Serial.println("- CAN bus initialized at 500k baud");
  Serial.println("- Connect CAN transceiver to D4 (TX) and D5 (RX)");
  Serial.println("- Sending periodic CAN messages...");
  
  delay(1000);
}

void loop() {
  // Send periodic CAN messages
  static unsigned long lastSend = 0;
  if (millis() - lastSend > 1000) {
    lastSend = millis();
    
    // Create a CAN message
    uint8_t data[8] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08};
    CanMsg msg(CAN_ID(0x123), sizeof(data), data);
    
    // Send the message
    int result = CAN.write(msg);
    if (result == 1) {
      Serial.print("- CAN message sent - ID: 0x");
      Serial.print(0x123, HEX);
      Serial.print(", Data: ");
      for (int i = 0; i < 8; i++) {
        Serial.print("0x");
        if (data[i] < 16) Serial.print("0");
        Serial.print(data[i], HEX);
        if (i < 7) Serial.print(" ");
      }
      Serial.println();
    } else {
      Serial.println("- Error: Failed to send CAN message!");
    }
  }
  
  // Check for incoming CAN messages
  if (CAN.available()) {
    CanMsg receivedMsg = CAN.read();
    
    Serial.print("- CAN message received - ID: 0x");
    Serial.print(receivedMsg.id, HEX);
    Serial.print(", Length: ");
    Serial.print(receivedMsg.data_length);
    Serial.print(", Data: ");
    
    for (int i = 0; i < receivedMsg.data_length; i++) {
      Serial.print("0x");
      if (receivedMsg.data[i] < 16) Serial.print("0");
      Serial.print(receivedMsg.data[i], HEX);
      if (i < receivedMsg.data_length - 1) Serial.print(" ");
    }
    Serial.println();
  }
  
  delay(10);
}
```

***To test this example, you need an external CAN transceiver connected to pins `D4` and `D5`. The code will demonstrate CAN communication patterns that can be observed with a CAN analyzer. Without a CAN transceiver and CAN network, the messages will not be transmitted on the actual CAN bus.***

Since the Nano R4's CAN interface provides only logic-level signals, you'll need an external CAN transceiver to convert these signals to the differential voltage levels required by CAN networks. The transceiver acts as a bridge between your Nano R4 board and the actual CAN bus, handling the electrical requirements and providing isolation.

For prototyping with the Nano R4 board, you need a +5 VDC-compatible transceiver like the [MCP2561 from Microchip](https://ww1.microchip.com/downloads/en/DeviceDoc/20005167C.pdf), which matches the board's +5 VDC logic levels. While the [SN65HVD230 from Texas Instruments](https://www.ti.com/lit/ds/symlink/sn65hvd230.pdf) is popular and widely used, it operates at +3.3 VDC and may require level shifting when used with the +5 VDC Nano R4.

When working with CAN on the Nano R4, there are several key points to keep in mind for successful implementation:

- Always ensure proper termination with 120 Ω resistors at both ends of the CAN bus to prevent signal reflections.
- Keep in mind that CAN uses message-based communication with unique identifiers rather than device addresses. Lower ID numbers have higher priority, so critical messages should use lower IDs.
- The CAN protocol provides automatic error detection, retransmission and collision resolution, making it extremely reliable for safety-critical applications.
- The Nano R4 supports both standard (11-bit) and extended (29-bit) CAN identifiers, allowing compatibility with most automotive and industrial CAN networks.

## HID (Human Interface Device) Communication

The Nano R4 board features built-in HID (Human Interface Device) communication that allows your projects to emulate input devices like keyboards and mice. HID is implemented within the RA4M1 microcontroller and uses the USB-C connection to communicate directly with computers as standard input devices. This makes it perfect for automation projects, assistive technologies, gaming controllers and interactive installations that need to control computers or send keystrokes and mouse movements.

HID is particularly useful when your project needs to interact directly with computer software, rather than just sending data through serial communication. While serial communication requires special software on the computer to interpret data, HID devices are recognized automatically by any operating system as standard keyboards or mice. This allows your Nano R4 to trigger keyboard shortcuts, type text, move the mouse cursor, or click buttons, making it ideal for presentation controllers, accessibility devices and automation systems.

The Nano R4's HID interface offers the following technical specifications:

|   **Parameter**  |     **Value**    |         **Notes**         |
|:----------------:|:----------------:|:-------------------------:|
|   Device Types   | Keyboard & Mouse |    Standard HID classes   |
|    Connection    |       USB-C      |   Native USB connection   |
|   Compatibility  |  Cross-platform  |   Windows, macOS, Linux   |
|   Key Modifiers  |   All standard   | Ctrl, Alt, Shift, GUI/Cmd |
|   Mouse Buttons  |     3 buttons    |    Left, Right, Middle    |
|  Mouse Movement  |  Relative/Delta  |   Smooth cursor movement  |
|   Scroll Wheel   |     Supported    |    Vertical scroll only   |
| Multiple Devices |     Supported    | Keyboard + Mouse together |

The Nano R4 uses the USB-C connector for HID communication:

| **Connection** | **Function** |        **Description**       |
|:--------------:|:------------:|:----------------------------:|
|      USB-C     |      HID     | Keyboard and Mouse emulation |

***__Important note__: When HID functionality is active, the Nano R4 board will be recognized by your computer as an input device. Be careful with your code to avoid sending unintended keystrokes or mouse movements that could interfere with normal computer operation.***

You can use HID communication through the dedicated `Keyboard.h` and `Mouse.h` libraries, which are included in the Arduino UNO R4 Boards core. These libraries provide simple functions to send keystrokes, key combinations, mouse movements and clicks.

The following example demonstrates basic keyboard emulation capabilities:

```arduino
/**
HID Keyboard Example for the Arduino Nano R4 Board
Name: nano_r4_hid_keyboard.ino
Purpose: This sketch demonstrates how to use the Nano R4 as a 
USB keyboard to send keystrokes and key combinations.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include "Keyboard.h"

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - HID Keyboard Example started...");
  Serial.println("- WARNING: This will send actual keystrokes to your computer!");
  
  // Wait 5 seconds before starting HID to give user time to read warning
  Serial.println("- Starting in 5 seconds...");
  for (int i = 5; i > 0; i--) {
    Serial.print(i);
    Serial.println(" seconds remaining");
    delay(1000);
  }
  
  // Initialize keyboard functionality
  Keyboard.begin();
  Serial.println("- Keyboard HID initialized. Starting demonstration...");
  
  delay(1000);
  
  // Demonstrate basic text typing
  Serial.println("- Typing basic text...");
  Keyboard.print("Hello from Nano R4! ");
  delay(1000);
  
  // Demonstrate special keys
  Serial.println("- Pressing Enter key...");
  Keyboard.press(KEY_RETURN);
  delay(100);
  Keyboard.releaseAll();
  delay(1000);
  
  // Demonstrate keyboard shortcuts
  Serial.println("- Sending Ctrl+A (Select All)...");
  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press('a');
  delay(100);
  Keyboard.releaseAll();
  delay(1000);
  
  Serial.println("- Keyboard demonstration completed!");
}

void loop() {
  // Send a timestamp every 10 seconds
  static unsigned long lastMessage = 0;
  if (millis() - lastMessage > 10000) {
    lastMessage = millis();
    
    Serial.println("- Sending periodic message...");
    
    // Send message with only letters, numbers and spaces
    Keyboard.print("Nano R4 ");
    Keyboard.print(millis() / 1000);
    Keyboard.print(" seconds");
    Keyboard.press(KEY_RETURN);
    delay(50);
    Keyboard.releaseAll();
  }
  
  delay(100);
}
```

***To test this example, no external components are needed. The code will wait 5 seconds before activating HID functionality, then automatically demonstrate various keyboard functions.***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages.

![Arduino IDE Serial Monitor output for the keyboard emulation example sketch](assets/hid-1.png)

After 5 seconds, the Nano R4 board will type text directly into whatever application has focus on your computer.

![Keyboard emulation example](assets/hid-2.gif)

The following example demonstrates mouse emulation capabilities:

```arduino
/**
HID Mouse Example for the Arduino Nano R4 Board
Name: nano_r4_hid_mouse.ino
Purpose: This sketch demonstrates how to use the Nano R4 as a 
USB mouse to control cursor movement and clicking.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include "Mouse.h"

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - HID Mouse Example started...");
  Serial.println("- WARNING: This will control your actual mouse cursor!");
  
  // Wait 5 seconds before starting HID
  Serial.println("- Starting in 5 seconds...");
  for (int i = 5; i > 0; i--) {
    Serial.print(i);
    Serial.println(" seconds remaining");
    delay(1000);
  }
  
  // Initialize mouse functionality
  Mouse.begin();
  Serial.println("- Mouse HID initialized. Starting demonstration...");
  
  delay(1000);
  
  // Demonstrate basic mouse movement
  Serial.println("- Moving mouse in a square pattern...");
  Mouse.move(100, 0);    // Move right
  delay(500);
  Mouse.move(0, 100);    // Move down
  delay(500);
  Mouse.move(-100, 0);   // Move left
  delay(500);
  Mouse.move(0, -100);   // Move up
  delay(500);
  
  // Demonstrate mouse clicks
  Serial.println("- Performing mouse clicks...");
  Mouse.click(MOUSE_LEFT);
  delay(500);
  Mouse.click(MOUSE_RIGHT);
  delay(500);
  
  // Demonstrate scrolling
  Serial.println("- Demonstrating scroll wheel...");
  Mouse.move(0, 0, 3);   // Scroll up
  delay(500);
  Mouse.move(0, 0, -3);  // Scroll down
  delay(500);
  
  Serial.println("- Mouse demonstration completed!");
}

void loop() {
  // Create a gentle circular mouse movement every 15 seconds
  static unsigned long lastMovement = 0;
  if (millis() - lastMovement > 15000) {
    lastMovement = millis();
    
    Serial.println("- Creating circular mouse movement...");
    for (int angle = 0; angle < 360; angle += 30) {
      int x = (int)(10 * cos(angle * PI / 180));
      int y = (int)(10 * sin(angle * PI / 180));
      Mouse.move(x, y);
      delay(100);
    }
  }
  
  delay(100);
}
```

***To test this example, no external components are needed. The code will automatically demonstrate mouse movement, clicking and scrolling functions.***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages. 

![Arduino IDE Serial Monitor output for the mouse emulation example sketch](assets/hid-3.png)

The mouse cursor will move and click according to the button presses.

![Mouse emulation example](assets/hid-4.gif)

When working with HID on the Nano R4, there are several key points to keep in mind for successful implementation:

- HID functionality makes your Nano R4 board appear as a real keyboard and mouse to your computer, so always include safeguards and delays in your code to prevent unintended actions that could interfere with normal computer operation.
- Always include a delay or warning period before activating HID functionality to give yourself time to prepare or stop the program if needed.
- Keep in mind that HID devices are automatically recognized by all modern operating systems without requiring special drivers, making your projects instantly compatible with Windows, macOS and Linux.
- For debugging HID projects, use `Serial.println()` statements to track what your code is doing, since you cannot rely on the Arduino IDE's Serial Monitor once HID actions start interfering with your computer.
- The Nano R4 can function as both a keyboard and mouse simultaneously, allowing for complex automation sequences that combine typing, shortcuts and mouse control.
- Remember that different operating systems may have slightly different keyboard layouts and shortcuts, so test your HID projects on your target platform to ensure compatibility.

## External Interrupts

The Nano R4 features external interrupt capability through the RA4M1 microcontroller's ICU (Interrupt Control Unit). Interrupts allow your Nano R4 board to immediately respond to pin state changes by temporarily pausing the main program to execute an Interrupt Service Routine (ISR), then returning to where it left off. This makes interrupts essential for time-critical applications like button detection, encoder reading, and sensor monitoring.

### Interrupt Specifications

The Nano R4 board's external interrupt capabilities offer the following technical specifications:

|      **Parameter**     | **Value** |                 **Notes**                |
|:----------------------:|:---------:|:----------------------------------------:|
|    Hardware Channels   |     9     |         Channels 0-7, 9 available        |
| Interrupt-capable Pins |  13 pins  |         7 digital + 6 analog pins        |
|      Trigger Modes     |     4     | `RISING`, `FALLING`, `CHANGE`, and `LOW` |
|      Response Time     |   < 1 μs  |         Typical interrupt latency        |

### Interrupt-Capable Pins

The following pins support external interrupts on the Nano R4 board:

| **Arduino Pin** | **Interrupt Channel** | **Primary Function** |          **Notes**         |
|:---------------:|:---------------------:|:--------------------:|:--------------------------:|
|       `D0`      |       Channel 6       |      Digital I/O     |  Shares channel with `A1`  |
|       `D1`      |       Channel 5       |      Digital I/O     |      Dedicated channel     |
|       `D2`      |       Channel 0       |      Digital I/O     | Recommended for interrupts |
|       `D3`      |       Channel 1       |   Digital I/O, PWM   |  Shares channel with `A4`  |
|       `D8`      |       Channel 9       |      Digital I/O     |      Dedicated channel     |
|      `D12`      |       Channel 3       |   Digital I/O, MISO  |  Shares channel with `A6`  |
|      `D13`      |       Channel 4       |   Digital I/O, SCK   |      Dedicated channel     |
|       `A1`      |       Channel 6       |    Analog, OPAMP+    |  Shares channel with `D0`  |
|       `A2`      |       Channel 7       |    Analog, OPAMP-    |      Dedicated channel     |
|       `A3`      |       Channel 2       |   Analog, OPAMP OUT  |  Shares channel with `A5`  |
|       `A4`      |       Channel 1       |    Analog, I²C SDA   |  Shares channel with `D3`  |
|       `A5`      |       Channel 2       |    Analog, I²C SCL   |  Shares channel with `A3`  |
|       `A6`      |       Channel 3       |     Analog input     |  Shares channel with `D12` |

***__Important note__: Pins sharing the same interrupt channel cannot be used for interrupts simultaneously. For example, `D3` and `A4` both use channel 1, so only one can be configured for interrupt functionality at a time.***

### Interrupt Trigger Modes

The Nano R4 board supports four interrupt trigger modes:

|  **Mode** |         **Trigger Condition**        |        **Typical Use Cases**       |
|:---------:|:------------------------------------:|:----------------------------------:|
|  `RISING` | Pin transitions from `LOW` to `HIGH` | Button press detection (pull-down) |
| `FALLING` | Pin transitions from `HIGH` to `LOW` |  Button press detection (pull-up)  |
|  `CHANGE` | Pin changes state (either direction) |   Encoder reading, pulse counting  |
|   `LOW`   |      Pin remains at `LOW` level      |       Level-triggered events       |

***__Important note__: The `HIGH` trigger mode is not supported by the hardware. If specified, it will behave as `RISING` mode (detecting only the `LOW`-to-`HIGH` transition, not the continuous `HIGH` state). For continuous `HIGH` level detection, use polling with `digitalRead()` instead.***

You can attach interrupts using the dedicated Arduino functions:

```arduino
attachInterrupt(digitalPinToInterrupt(pin), ISR_function, mode);
detachInterrupt(digitalPinToInterrupt(pin));
```

The following example demonstrates basic interrupt usage:

```arduino
/**
External Interrupt Example for the Arduino Nano R4 Board
Name: nano_r4_interrupt_example.ino
Purpose: This sketch demonstrates how to use external interrupts
to detect button presses.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

const int buttonPin = 2;
const int ledPin = LED_BUILTIN;

// Variables shared with ISR must be volatile
volatile bool buttonPressed = false;
volatile unsigned long pressCount = 0;

// Interrupt Service Routine - keep it short!
void buttonISR() {
  buttonPressed = true;
  pressCount++;
}

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  
  // Attach interrupt to button pin
  attachInterrupt(digitalPinToInterrupt(buttonPin), buttonISR, FALLING);
  
  Serial.println("- Arduino Nano R4 - External Interrupt Example started...");
  Serial.println("- Press the button to trigger interrupts");
}

void loop() {
  if (buttonPressed) {
    buttonPressed = false;
    digitalWrite(ledPin, !digitalRead(ledPin));
    
    Serial.print("- Button pressed! Count: ");
    Serial.println(pressCount);
  }
  
  delay(10);
}
```

To test this example, connect a push button to the Nano R4 board as follows:

- Connect one leg of a push button to pin `D2`
- Connect the other leg of the push button to `GND`
- No external components needed (using built-in LED and internal pull-up)

![Interrupt pins test circuit on the Nano R4 board](assets/interrupt-pins-1.png)

Open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the interrupt count increase with each button press.

![Arduino IDE Serial Monitor output for the basic interrupt example sketch](assets/interrupt-pins-2.png)

When working with interrupts on the Nano R4 board, there are several key points to keep in mind for successful implementation:

- Keep ISR functions short and fast: Avoid `delay()`, `Serial.print()`, or complex calculations inside ISRs as they block other interrupts.
- Use volatile variables: Always declare variables shared between ISRs and main code as volatile to prevent compiler optimization issues.
- Manage channel conflicts: Verify that pins don't share the same interrupt channel when using multiple interrupts.
- Consider debouncing: Mechanical switches may cause multiple triggers (add a 100nF capacitor or implement software debouncing).
- Protect shared multi-byte variables: Disable interrupts temporarily when accessing them.

## Qwiic Connector

The Nano R4 board features an onboard Qwiic connector that provides a simple, tool-free solution for connecting I²C devices. The Qwiic ecosystem, developed by SparkFun Electronics, has become an industry standard for rapid prototyping with I²C devices, allowing you to connect sensors, displays, and other peripherals without soldering or complex wiring. This makes it perfect for quickly building sensor networks, adding displays, or expanding your project's capabilities with minimal effort.

![Qwiic connector of the Nano R4 board](assets/qwiic-connector.png)

The Qwiic connector enhances the Nano R4's versatility by providing a dedicated interface for the extensive ecosystem of +3.3 VDC I²C modules. While the Nano R4's native +5 VDC operation ensures compatibility with classic Arduino shields and components, the Qwiic interface adds seamless integration with modern sensors and modules. The board includes built-in level translation between the +5 VDC microcontroller and the +3.3 VDC Qwiic bus, giving you the best of both worlds: full compatibility with traditional Arduino hardware on the main pins, plus instant access to the latest Qwiic-compatible devices.

### Qwiic Specifications

The Nano R4's Qwiic connector offers the following specifications:

|   **Parameter**   |          **Value**         |                    **Notes**                   |
|:-----------------:|:--------------------------:|:----------------------------------------------:|
|   Connector Type  |      JST SH 4-pin 1mm      |             Industry standard Qwiic            |
| Operating Voltage |          +3.3 VDC          |          Powered by onboard regulator          |
|   I²C Interface   |           `Wire1`          |         Secondary I²C bus (not `Wire`)         |
|   Level Shifting  |          Built-in          | Automatic +5 VDC to +3.3 VDC level translation |
|     Pin Order     | `GND`, `VCC`, `SDA`, `SCL` |              Standard Qwiic pinout             |

The Qwiic connector is a small 4-pin connector with a 1.00 mm pitch. The mechanical details of the connector can be found in the connector's [datasheet](https://www.jst-mfg.com/product/pdf/eng/eSH.pdf).

The pin layout of the Qwiic connector is the following:

- `GND`: Ground
- `VCC`: +3.3 VDC power supply
- `SDA`: I²C data line
- `SCL`: I²C clock line

The `VCC` pin provides a stable +3.3 VDC output from the onboard regulator when the board is powered. The manufacturer part number of the Qwiic connector is [SM04B-SRSS-TB](https://www.jst-mfg.com/product/pdf/eng/eSH.pdf), and its matching cable assemblies use the [SHR-04V-S-B](https://www.jst-mfg.com/product/pdf/eng/eSH.pdf) receptacle.

### Understanding the Dual I²C Architecture

The Nano R4 implements a dual I²C bus architecture that separates +5 VDC and +3.3 VDC devices:

| **I²C Bus** | **Arduino Object** | **Physical Connection** | **Voltage** | **Level Shifter** |          **Use Case**         |
|:-----------:|:------------------:|:-----------------------:|:-----------:|:-----------------:|:-----------------------------:|
|   Primary   |       `Wire`       |       Pins `A4/A5`      |    +5 VDC   |        None       |  +5V sensors, Arduino shields |
|  Secondary  |       `Wire1`      |     Qwiic Connector     |   +3.3 VDC  |      Built-in     | Modern sensors, Qwiic devices |

***__Important note__: The Qwiic connector uses `Wire1` object, not the standard `Wire` object. This is different from boards with a single I²C bus. Always use `Wire1.begin()` and related `Wire1` functions when communicating with Qwiic devices.***

### Connecting Qwiic Devices

Connecting Qwiic devices to your Nano R4 board is straightforward. Simply get a standard Qwiic cable (available in various lengths) and plug one end into the Nano R4's Qwiic connector and the other into your Qwiic device. Most Qwiic devices have two connectors, allowing you to daisy-chain multiple devices without any soldering or breadboarding. The polarized connectors prevent incorrect connections, making the setup process foolproof.

![Nano R4 and Modulino Movement connected via Qwiic](assets/qwiic-connection.png)

The Qwiic system's key advantages include:

- **Plug-and-play connectivity**: No breadboards, jumper wires, or soldering required
- **Polarized connectors**: Prevents accidental reverse connections
- **Daisy-chain capability**: Connect multiple devices in series
- **Built-in pull-up resistors**: No external resistors needed
- **Standard pinout**: Compatible across all Qwiic ecosystem devices

### Working with Qwiic Devices

The following example demonstrates how to use the [Arduino Modulino Movement](https://store.arduino.cc/collections/modulino/products/modulino-movement) sensor via the Qwiic connector:

```arduino
/**
Modulino Movement Example for the Arduino Nano R4 Board
Name: nano_r4_modulino_movement.ino
Purpose: This sketch demonstrates reading motion data from the 
Modulino Movement sensor via the Qwiic connector.

@author Arduino Product Experience Team
@version 1.0 01/06/25
*/

#include <Modulino.h>
#include <Wire.h>

// Create Modulino Movement object
ModulinoMovement movement;

// Variables for sensor data
float x, y, z;
float roll, pitch, yaw;

void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  Serial.println("- Arduino Nano R4 - Modulino Movement Example started...");
  
  // Initialize Wire1 for Qwiic connector
  Wire1.begin();
  
  // Initialize Modulino system
  Modulino.begin();
  
  // Initialize Movement sensor
  movement.begin();
  
  Serial.println("- Modulino Movement connected successfully!");
  Serial.println("- Reading motion data...\n");
}

void loop() {
  // Read new movement data from the sensor
  movement.update();
  
  // Get acceleration values
  x = movement.getX();
  y = movement.getY();
  z = movement.getZ();
  
  // Get gyroscope values
  roll = movement.getRoll();
  pitch = movement.getPitch();
  yaw = movement.getYaw();
  
  // Display acceleration
  Serial.print("- Accel (g): X=");
  Serial.print(x, 2);
  Serial.print(" Y=");
  Serial.print(y, 2);
  Serial.print(" Z=");
  Serial.print(z, 2);
  
  // Display gyroscope
  Serial.print(" | Gyro (dps): Roll=");
  Serial.print(roll, 1);
  Serial.print(" Pitch=");
  Serial.print(pitch, 1);
  Serial.print(" Yaw=");
  Serial.print(yaw, 1);
  
  Serial.println();
  
  // Update at 10Hz
  delay(100);
}
```

***To test this example, you need an [Arduino Modulino Movement](https://store.arduino.cc/collections/modulino/products/modulino-movement) connected to the Nano R4's Qwiic connector via a Qwiic cable. Install the Modulino library from the Arduino IDE Library Manager (Tools > Manage Libraries > Search "Modulino").***

You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the real-time acceleration and gyroscope data. Try moving or rotating the sensor to see the values change.

![Arduino IDE Serial Monitor output for the Modulino Movement sketch](assets/qwicc-modulino-serial-monitor.png)

This example demonstrates the key aspects of using Qwiic devices with the Nano R4:

- Using `Wire1.begin()` instead of `Wire.begin()` for the Qwiic connector
- Direct plug-and-play connection without additional wiring
- Automatic +3.3 VDC power and level translation
- Access to Arduino's ecosystem of Modulino sensors

## Bootloader

The Nano R4 board features a built-in bootloader that enables sketch uploading directly from the Arduino IDE without requiring external programming hardware. The bootloader is a small program stored in a protected area of the RA4M1 microcontroller's flash memory that runs each time the board powers on or resets. It manages the critical communication between your computer and the board during sketch uploads, making the development process simple and accessible.

During normal operation, when you connect your Nano R4 to your computer and upload a sketch, the bootloader receives the new program data via USB and writes it to the appropriate memory location. This process happens automatically and transparently, allowing you to focus on developing your projects rather than managing low-level programming details.

### Understanding the Bootloader Operation

When the Nano R4 board resets or powers on, the bootloader performs the following sequence:

1. **Initialization**: The bootloader initializes the USB communication and checks for incoming programming commands
2. **Wait Period**: It waits briefly for new sketch data from the Arduino IDE
3. **Program Execution**: If no new sketch is received, it jumps to your previously uploaded program

This automatic process ensures that your board is always ready to receive new sketches while maintaining quick startup times for your applications.

### Bootloader Recovery

In certain situations, the bootloader may become corrupted or stop functioning properly. Common symptoms of bootloader issues include:

- The board is not recognized by the Arduino IDE
- Upload attempts fail with timeout errors
- The board appears as an unknown device in your computer's device manager
- The onboard LEDs behave abnormally during connection attempts

The Nano R4 includes a special hardware feature for bootloader recovery: the `BOOT` pin. This pin, when connected to ground (`GND`) during power-up, puts the board into a special programming mode that allows you to restore the bootloader using the Renesas Flash Programmer tool.

![The Nano R4 BOOT pin (top view)](assets/boot-pin.png)

***__Important note__: The `BOOT` pin is located on the bottom side of the board and is clearly labeled. This pin should only be used for bootloader recovery or advanced programming operations. During normal use, leave this pin unconnected.***

### Technical Specifications

The Nano R4's bootloader offers the following technical specifications:

|   **Parameter**  |         **Value**        |                 **Notes**                |
|:----------------:|:------------------------:|:----------------------------------------:|
|  Recovery Method |    `BOOT` pin + `GND`    |     Hardware recovery mode activation    |
|  Bootloader File |      `dfu_nano.hex`      | Included with Arduino UNO R4 Boards core |
| Programming Tool | Renesas Flash Programmer |   Official tool for bootloader recovery  |

### Bootloader File Location

The bootloader file (`dfu_nano.hex`) can be obtained in two ways:

**Option 1: Direct Download (recommended)**: 

Download directly from the Arduino GitHub repository:

- [Download dfu_nano.hex](https://github.com/arduino/ArduinoCore-renesas/blob/main/bootloaders/NANOR4/dfu_nano.hex)

**Option 2: From Arduino IDE Installation**:

The bootloader file (`dfu_nano.hex`) is automatically installed with the Arduino UNO R4 Boards core. You can find it in the following locations:

**Windows:**

```bash
C:\Users\[YourUsername]\AppData\Local\Arduino15\packages\arduino\hardware\renesas_uno\[version]\bootloaders\NANOR4\
```

**macOS:**

```bash
~/Library/Arduino15/packages/arduino/hardware/renesas_uno/[version]/bootloaders/NANOR4/
```

**Linux:**

```bash
~/.arduino15/packages/arduino/hardware/renesas_uno/[version]/bootloaders/NANOR4/
```

***Replace `[YourUsername]` with your actual username and `[version]` with the installed core version number.***

### When to Consider Bootloader Recovery

Bootloader recovery should be considered when:

- Standard troubleshooting steps (different cables, USB ports, driver reinstallation) have failed
- The board was working previously but stopped being recognized after a failed upload
- Power was interrupted during a sketch upload
- You need to restore the board to factory programming state
- The board is not responding to the reset button normally

### Bootloader Recovery Tutorial

For detailed step-by-step instructions on recovering and reflashing the bootloader on your Nano R4 board, please refer to our **[Nano R4 Bootloader Recovery and Flashing Tutorial](https://docs.arduino.cc/tutorials/nano-r4/bootloader-flashing/)**. This tutorial covers the following topics:


- Preparing your board for bootloader flashing
- Installing and configuring the Renesas Flash Programmer tool
- Step-by-step flashing process
- Verifying successful bootloader restoration
- Troubleshooting common issues

***__Important note__: Bootloader recovery should only be performed when necessary. Ensure stable power supply and follow the tutorial instructions carefully. The process requires only the Renesas Flash Programmer tool and the bootloader file.***

### Maintaining Bootloader Health

To minimize the risk of bootloader corruption and ensure reliable operation, we recommend the following:

- **Always allow uploads to complete**: Never disconnect the USB cable or remove power during sketch uploads
- **Use quality USB cables**: Poor quality or damaged cables can cause communication errors
- **Ensure stable power**: Use a reliable power source when uploading sketches
- **Keep the Arduino IDE updated**: Newer versions often include improvements to the upload process
- **Handle the board carefully**: Avoid static discharge and physical damage to the board

The bootloader is a critical component that makes the Nano R4 board user-friendly and accessible. While it's designed to be robust and reliable, understanding its operation and recovery options ensures you can always restore your board to working condition if issues arise.

## Support

If you encounter any issues or have questions while working with your Nano R4 board, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for Nano family boards. The Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Nano family help center page](https://support.arduino.cc/hc/en-us/sections/360004605400-Nano-Family)

### Forum

Join our community forum to connect with other Nano family board users, share your experiences, and ask questions. The Forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Nano R4.

- [Nano category in the Arduino Forum](https://forum.arduino.cc/c/official-hardware/nano-family/87)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Nano family boards.

- [Contact us page](https://www.arduino.cc/en/contact-us/)