---
title: 'Nano XL Link User Manual'
difficulty: beginner
compatible-products: [nano-xl-link]
description: 'Learn about the hardware and software features of the Arduino® Nano XL Link board.'
tags:
  - Cheat sheet
  - User manual
  - Industrial
  - CAN FD
  - RS-485
  - Ethernet
author: 'José Bagur'
hardware:
  - hardware/nano/boards/nano-xl-link
software:
  - ide-v2
  - web-editor
---
 
This user manual provides an overview of the Nano XL Link board, highlighting its hardware and software elements. With it, you will learn how to set up, configure, and use the main features of the Nano XL Link board.
 
## Hardware and Software Requirements
 
### Hardware Requirements
 
- [Nano XL Link](https://store.arduino.cc/products/nano-xl-link) (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- [Breadboard](https://store.arduino.cc/products/breadboard-400-contacts) (x1) (recommended)
- [Male/male jumper wires](https://store.arduino.cc/products/breadboard-400-contacts) (recommended)
 
### Software Requirements
 
- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Cloud Editor](https://create.arduino.cc/editor)
- [Arduino Zephyr core](https://github.com/arduino/ArduinoCore-zephyr)
 
	
<Alert type="info">
The Nano XL Link is compatible with the Arduino ecosystem and can be programmed directly as a standalone device.
</Alert> 

## Nano XL Link Overview
 
The Nano XL Link is a compact microcontroller board designed for industrial and building automation applications. It is based on the PIC32CK2051SG01144 microcontroller from Microchip® and extends the standard Nano pinout through two 2.54 mm double-row headers. The board integrates three industrial communication transceivers (CAN FD, RS-485 and a 10/100 Ethernet PHY), which allows it to communicate directly with industrial equipment without additional interface boards.
 
The Nano XL Link includes a 32-bit Arm® Cortex®-M33 microcontroller with 2 MB of flash memory and 512 kB of RAM, an onboard Qwiic connector, a programmable RGB LED and a user LED. The board operates at +3.3 VDC logic levels and is rated for an operating temperature range of -20 °C to +85 °C.
 
### Nano XL Link Architecture Overview
 
The Nano XL Link board combines a microcontroller with onboard fieldbus transceivers in a compact form factor, which suits applications such as machine-level control, building automation and energy monitoring.
 
The top view of the Nano XL Link board is shown in the image below:
 
The bottom view of the Nano XL Link board is shown in the image below:

<Alert type="info">
The bottom side of the Nano XL Link board features test points for debugging and development purposes (SWD, USB and `RESET`), along with the board's certification markings and identification information (board model and SKU).
</Alert>
 
Here is an overview of the board's main components shown in the images above:
 
- **Microcontroller**: At the heart of the Nano XL Link board there is a Microchip PIC32CK2051SG01144 microcontroller, based on an Arm® Cortex®-M33 core with 2 MB of flash memory, 512 kB of RAM and an integrated hardware security module (HSM). The microcontroller is clocked from a 12 MHz quartz crystal.
- **CAN FD transceiver**: An onboard Texas Instruments® TCAN3414 transceiver provides the physical layer for the microcontroller's CAN FD controller. The `CANH` and `CANL` signals are available on the board headers.
- **RS-485 transceiver**: An onboard Texas Instruments® THVD2410 transceiver provides a half-duplex RS-485 interface. The `A` and `B` signals are available on the board headers.
- **Ethernet PHY**: An onboard Microchip® KSZ8081RNAIA PHY provides a 10/100 Mbps Ethernet interface. The differential transmit and receive pairs and an activity LED signal are available on the board headers.
- **Bus termination jumpers**: Two solder jumpers connect 120 Ω termination resistors to the fieldbuses: `SJ1` for the CAN bus and `SJ2` for the RS-485 bus. Both jumpers are **closed** by default on the board.
- **USB-C connector**: The Nano XL Link board features a USB-C connector for programming, power supply, and serial communication.
- **Qwiic connector**: The Nano XL Link board includes an onboard Qwiic connector to expand the board's communication capabilities via I²C, facilitating connection with a wide range of sensors, actuators and peripherals, such as the Arduino Modulino nodes.
- **Programmable RGB LED**: The board has an onboard user-programmable RGB LED to provide visual feedback about different operating states.
- **User LED**: In addition to the RGB LED, the board includes an onboard user-programmable yellow LED for basic status indications.
- **Power LED**: A green LED indicates that the board's +3.3 VDC rail is powered.
- **Reset button**: An onboard push button resets the microcontroller.
- **Extended headers**: Two 2x15 pin headers (`J3` and `J4`) with 2.54 mm pitch expose the board's signals, power pins, and fieldbus lines.

### Board Core and Libraries
 
The **Arduino Zephyr** core contains the libraries and examples to work with the Arduino Nano XL Link's peripherals and onboard components, such as its PIC32CK microcontroller, the CAN FD controller, the Ethernet interface and the onboard LEDs. 

To install the core for the Nano XL Link board, navigate to **Tools > Board > Boards Manager** or click the **Boards Manager** icon in the left tab of the IDE. In the Boards Manager tab, search for `Zephyr` and install the latest version of the core.
 
The Arduino Zephyr core provides support for the following:
 
- Board control and configuration (pin configuration and reset)
- Analog input (12-bit ADC) and PWM output
- Communication interfaces (UART, I²C and SPI)
- CAN and CAN FD communication through the `CAN` library
- Ethernet communication through the `Ethernet` library
- RS-485 communication through the `ArduinoRS485` library
- Onboard LED control (RGB LED and user LED)

The Arduino Zephyr core runs Arduino sketches on top of the Zephyr® real-time operating system (RTOS). Sketches are written with the same Arduino API used on other Arduino boards, while the underlying drivers are provided by Zephyr.

### Pinout
 
The full pinout is available and downloadable as PDF from the link below:
 
- [Nano XL Link pinout](https://docs.arduino.cc/resources/pinouts/ABX00182-full-pinout.pdf)

### Datasheet
 
The complete datasheet is available and downloadable as PDF from the link below:
 
- [Nano XL Link datasheet](https://docs.arduino.cc/resources/datasheets/ABX00182-datasheet.pdf)
### Schematics
 
The complete schematics are available and downloadable as PDF from the link below:
 
- [Nano XL Link schematics](https://docs.arduino.cc/resources/schematics/ABX00182-schematics.pdf)
### STEP Files
 
The complete STEP files are available and downloadable from the link below:
 
- [Nano XL Link STEP files](../../downloads/ABX00182-step.zip)

## First Use
 
### Unboxing the Product
 
When opening the Nano XL Link box, you will find the board and its corresponding documentation. **The Nano XL Link does not include additional cables**, so you will need a USB-C cable ([available separately here](https://store.arduino.cc/products/usb-cable2in1-type-c)) to connect the board to your computer.
 
The Nano XL Link is a standalone device that can be programmed directly without requiring additional boards. For fieldbus projects, the board can be mounted on the Nano Connector Carrier (ASX00090) ([available separately here](https://store.arduino.cc/products/usb-cable2in1-type-c)), which provides screw terminals and connectors for its signals.

### Connecting the Board
 
The Nano XL Link can be connected to your computer using its onboard USB-C connector. It can also be integrated into larger projects using the following:
 
- **Direct USB-C connection**: For programming, power supply and serial communication with the computer
- **Pin connection**: For integration into breadboards, carriers or custom PCBs through the `J3` and `J4` headers
- **Qwiic connection**: For rapid expansion with compatible sensors and modules
- **Fieldbus connection**: For direct connection to CAN, RS-485 and Ethernet networks through the header pins

<Alert type="warning">
Important note: The Nano XL Link operates at +3.3 VDC. When connecting sensors, modules or shields designed for +5 VDC logic, make sure to verify voltage compatibility to avoid component damage.
</Alert> 

### Voltage Compatibility Considerations
 
Before connecting any external components to your Nano XL Link, it is important to understand its voltage characteristics to prevent damage to the board and to your sensors and modules.
 
**The Nano XL Link operates at +3.3 VDC**, which means:
 
- All digital I/O pins use +3.3 VDC logic levels (`HIGH` = +3.3 VDC, `LOW` = 0 VDC)
- Analog inputs measure voltages from 0 to +3.3 VDC
- Communication pins (I²C, SPI and UART) operate at +3.3 VDC logic levels
- The Qwiic connector operates at +3.3 VDC and can be used directly with Qwiic, STEMMA QT and Modulino® devices

**For +5 VDC components**, add **external level shifters** on all data lines and use the `+VBUS` pin only when the board is powered from USB (see the following section). Always check your component's datasheet for voltage specifications before connecting. When in doubt, use a multimeter to verify voltage levels or add protective level shifting.
 
### Powering the Board
 
The Nano XL Link can be powered in several ways:
 
- **Via USB-C connector**: The most common method during development and programming
- **Via `VIN` pin**: Using an external +7-24 VDC power supply that is regulated down to +3.3 VDC by the onboard buck converter (MPQ4334)
- **Via `+3V3` pin**: Directly connecting a regulated +3.3 VDC source, which bypasses the onboard buck converter
 
<Alert type="warning">
Important note: The Nano XL Link's `VIN` pin accepts a voltage range of +7-24 VDC. Do not connect voltages outside this range as you could permanently damage the board.
</Alert>
 
 <Alert type="warning">
Important note: When powering the board through the `+3V3` pin, do not connect a power source to the `VIN` pin or the USB-C connector at the same time. Applying an external +3.3 VDC source together with another power source can damage the board. Always verify all the connections before applying power.
</Alert>

#### +3.3 VDC and +VBUS Outputs
 
When the board is powered through the USB-C connector or the `VIN` pin, the following power outputs are available on the headers to supply external circuits:
 
| **Pin**  | **Voltage** | **Maximum Current** |                **Notes**                 |
| :------: | :---------: | :-----------------: | :--------------------------------------: |
|  `+3V3`  |  +3.3 VDC   |         1 A         |      Output of the buck converter        |
| `+VBUS`  |   +5 VDC    |       500 mA        |  Available only when powered via USB-C   |
 
The `+VBUS` pin is fed directly from the USB-C connector through an MP5077 load switch, which delays the activation of the rail during power-up. **No +5 VDC is available on the headers when the board is powered only through the `VIN` pin.**

### Hello World Example
 
Let's program the Nano XL Link to reproduce the classic `Hello World` example used in the Arduino ecosystem: the `Blink` sketch. We will use this example to verify that the Nano XL Link's connection to the computer works correctly, that the Arduino IDE is properly configured, and that both the board and development environment function as expected.
 
First, connect your Nano XL Link to your computer using a USB-C cable, open the Arduino IDE, and make sure that the board is connected correctly. If you are new to the Arduino IDE, please refer to the official Arduino documentation for more detailed information about initial setup. Copy and paste the following example sketch into a new Arduino IDE file:

/**
Blink Example for the Arduino Nano XL Link Board
Name: nano_xl_link_blink.ino
Purpose: This sketch demonstrates how to blink the built-in
user LED of the Arduino Nano XL Link board.

@author Arduino Product Experience Team
@version 1.0 06/10/26
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
  Serial.println("- Arduino Nano XL Link - Blink Example started...");
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

To upload the sketch to the board, click the **Verify** button to compile the sketch and check for errors, then click the **Upload** button to program the device with the sketch.
 
You should see the built-in yellow user LED of your Nano XL Link board turn on for one second, then turn off for one second, repeating this cycle continuously.
 
Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages that the example sketch sends each time the LED state changes.

This example confirms the following:
 
- The Nano XL Link board is correctly connected
- The Arduino IDE is properly configured
- The board is functioning correctly
- USB communication and sketch upload are working
- Digital pins respond to commands

Congratulations! You have successfully completed your first program on the Nano XL Link board. You are now ready to explore the more advanced features of the board.

## LEDs
 
This user manual section covers the Nano XL Link built-in LEDs, showing their main hardware and software characteristics.
 
### RGB LED
 
The Nano XL Link features a built-in RGB LED that can be used as a visual feedback indicator for the user.
 
The built-in RGB LED can be accessed through the following macro definitions:
 
| **Built-in LED** | **Macro Definition** | **Arduino Pin** | **Microcontroller Pin** |
| :--------------: | :------------------: | :-------------: | :---------------------: |
|     Red LED      |        `LEDR`        |      `D39`      |         `PC15`          |
|    Green LED     |        `LEDG`        |      `D40`      |         `PC16`          |
|     Blue LED     |        `LEDB`        |      `D41`      |         `PC17`          |
 
<Alert type="info">
The built-in RGB LED on the Nano XL Link is a common-anode LED connected to +3.3 VDC, so each color must be pulled to ground (`GND`) to make it light up. This means that a voltage level of `LOW` on each of their pins will turn the specific color of the LED on, and a voltage level of `HIGH` will turn it off.
</Alert> 
 
You can turn each color on and off using the `pinMode()` and `digitalWrite()` functions:
 
The following example sketch turns on each of the RGB LED colors at an interval of 500 ms:
 
```arduino
/**
RGB LED Example for the Arduino Nano XL Link Board
Name: nano_xl_link_rgb_led.ino
Purpose: This sketch demonstrates how to control the built-in
RGB LED of the Arduino Nano XL Link board.
 
@author Arduino Product Experience Team
@version 1.0 06/10/26
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
 
  Serial.println("- Arduino Nano XL Link - RGB LED Example started...");
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
 
Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages that the example sketch sends each time the RGB LED state changes.

<Alert type="info"> 
The three RGB LED pins also support PWM for brightness control. When using `analogWrite()`, the polarity is already inverted by the core, so higher values result in a brighter LED; for example, `analogWrite(LEDG, 255)` sets the green LED at maximum brightness.
</Alert>
 
### User LED
 
The Nano XL Link also features a built-in yellow user LED that can be used for basic status indications and debugging purposes.
 
The built-in user LED can be accessed through the following macro definition:
 
| **Built-in LED** | **Macro Definition** | **Arduino Pin** | **Microcontroller Pin** |
| :--------------: | :------------------: | :-------------: | :---------------------: |
| Yellow User LED  |    `LED_BUILTIN`     |      `D38`      |         `PB16`          |
 
<Alert type="info">
Unlike the RGB LED, the built-in user LED on the Nano XL Link operates with standard logic levels. This means that a voltage level of `HIGH` will turn the LED on, and a voltage level of `LOW` will turn it off.
</Alert>
 
The [Hello World example](#hello-world-example) shows how to control the built-in user LED. **Unlike the RGB LED pins, `LED_BUILTIN` does not support PWM**.
 
### Power LED
 
The green power LED is connected directly to the +3.3 VDC rail and turns on whenever the board is powered. **It cannot be controlled from a sketch**.

## Pins
 
This user manual section provides information about the Nano XL Link's pin capabilities and functionality. Understanding the board's pin capabilities and configurations is important for making the most of your projects with the Nano XL Link board.
 
### Pins Overview
 
The Nano XL Link exposes its signals through **two 2x15 pin headers** (`J3` and `J4`), for a total of 60 pins. The headers keep the signals of the classic Nano form factor and add a second row with additional I/O, communication interfaces, fieldbus lines and USB signals.

### Pins Specifications and Characteristics
 
The Nano XL Link's header pins are organized into the following categories:
 
|     **Pin Type**     | **Count** |                  **Pin Numbers**                   |             **Primary Functions**             |
| :------------------: | :-------: | :------------------------------------------------: | :-------------------------------------------: |
|   **Digital Pins**   |    26     |              `D0` - `D13`, `D22` - `D33`             | Digital I/O, PWM (8 pins), UART, SPI, I²C, I²S |
|   **Analog Pins**    |     8     |              `A0` - `A7` (`D14` - `D21`)             |          Analog input, Digital I/O           |
|  **Fieldbus Pins**   |     9     | `CANH`, `CANL`, `RS485 A`, `RS485 B`, `ETH_TX_P/N`, `ETH_RX_P/N`, `LED_ACT` |   CAN FD, RS-485 and Ethernet bus lines   |
|    **USB Pins**      |     4     |        `USB_D+`, `USB_D-`, `USB_HS D+`, `USB_HS D-`    |              USB data lines                  |
|    **Power Pins**    |     8     |            `VIN`, `+VBUS`, `+3V3`, `GND` (x5)           |            Power supply and ground            |
|   **Special Pins**   |     4     |             `RESET`, `AREF`, `SWDIO`, `SWCLK`            |       System control, reference and debug       |
 
***__Important voltage compatibility note__: The Nano XL Link operates at +3.3 VDC. This affects all digital and analog pins, including communication interfaces like I²C, SPI and UART. Before connecting any sensors, modules or shields, always verify their voltage compatibility. __Applying +5 VDC signals to the board's pins without proper level shifting can permanently damage the board__.***
 
The following table shows the electrical specifications and operating limits for the pins on the Nano XL Link board:
 
|    **Specification**    |   **Value**    |            **Notes**             |
| :---------------------: | :------------: | :------------------------------: |
|  **Operating Voltage**  |    +3.3 VDC    | Logic level for all digital pins |
| **Input Voltage Range** | 0 to +3.3 VDC  |        Analog and digital         |
| **Max Current per Pin** | TO VERIFY      |    Source/sink current limit     |
|  **Analog Reference**   |    +3.3 VDC    |   Default reference (`VDD`)      |
 
 <Alert type="info">
The digital pin numbers `D34` to `D43` are also defined in the core, but they are connected to onboard components (Qwiic connector, Ethernet PHY control, LEDs and RS-485 transceiver control) and are not available on the headers. Avoid using them as general-purpose I/O.
</Alert>

### Digital Pins
 
The Nano XL Link features **26 digital pins** on its headers (`D0` to `D13` and `D22` to `D33`), plus the analog pins `A0` to `A7`, which can also be used as digital pins `D14` to `D21`. All of them can be configured as digital inputs or digital outputs and operate at +3.3 VDC logic levels.
 
The Nano XL Link digital pins provide the following functionality:
 
| **Arduino Pin** | **Microcontroller Pin** | **Header Pin** | **Additional Functions** |
| :-------------: | :---------------------: | :------------: | :----------------------: |
|      `D0`       |         `PA00`          |    `J4-30`     |     `Serial1` TX         |
|      `D1`       |         `PA01`          |    `J4-28`     |     `Serial1` RX         |
|      `D2`       |         `PC19`          |    `J4-22`     |           PWM            |
|      `D3`       |         `PC20`          |    `J4-20`     |           PWM            |
|      `D4`       |         `PA21`          |    `J4-18`     |           PWM            |
|      `D5`       |         `PA20`          |    `J4-16`     |           PWM            |
|      `D6`       |         `PB11`          |    `J4-14`     |           PWM            |
|      `D7`       |         `PD11`          |    `J4-12`     |           PWM            |
|      `D8`       |         `PA23`          |    `J4-10`     |           PWM            |
|      `D9`       |         `PB24`          |     `J4-8`     |           PWM            |
|      `D10`      |         `PA26`          |     `J4-6`     |        `SPI` CS          |
|      `D11`      |         `PA27`          |     `J4-4`     |       `SPI` MOSI         |
|      `D12`      |         `PA24`          |     `J4-2`     |       `SPI` MISO         |
|      `D13`      |         `PA25`          |     `J3-1`     |        `SPI` SCK         |
|      `D22`      |         `PC21`          |     `J3-6`     |       `SPI1` MOSI        |
|      `D23`      |         `PC23`          |     `J3-8`     |       `SPI1` MISO        |
|      `D24`      |         `PC22`          |    `J3-10`     |       `SPI1` SCK         |
|      `D25`      |         `PC14`          |    `J3-12`     |        `SPI1` CS         |
|      `D26`      |         `PB21`          |    `J3-14`     |       `Wire1` SDA        |
|      `D27`      |         `PB22`          |    `J3-16`     |       `Wire1` SCL        |
|      `D28`      |         `PD14`          |    `J3-18`     |          I²S CK          |
|      `D29`      |         `PD13`          |    `J3-20`     |          I²S WS          |
|      `D30`      |         `PD16`          |    `J3-22`     |         I²S SDI          |
|      `D31`      |         `PD17`          |    `J3-24`     |         I²S SDO          |
|      `D32`      |         `PD08`          |    `J3-28`     |     `Serial2` TX         |
|      `D33`      |         `PD09`          |    `J3-30`     |     `Serial2` RX         |
 
<Alert type="info">
Important note: On the Nano XL Link, pin `D0` is the `Serial1` transmit line (TX) and pin `D1` is the receive line (RX). This is the opposite of the classic Nano boards, where `D0` is RX and `D1` is TX. Take this into account when connecting serial devices or reusing Nano shields. Pins `D28` to `D31` are reserved for a future I²S interface and can currently be used as general-purpose digital I/O.
</Alert>
 
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
 
The available pin modes are `OUTPUT` for digital output, `INPUT` for digital input with high impedance, and `INPUT_PULLUP` for digital input with internal pull-up resistor enabled. Digital output values can be `HIGH` (+3.3 VDC) or `LOW` (0 VDC), and digital input readings will return `HIGH` or `LOW` based on the voltage level detected on the pin. Digital pins can also trigger interrupts through the `attachInterrupt()` function.
 
The following example demonstrates how to use a digital input with an external interrupt to toggle the built-in user LED each time a push button connected to pin `D2` is pressed:
 
```arduino
/**
Digital Input Interrupt Example for the Arduino Nano XL Link Board
Name: nano_xl_link_digital_interrupt.ino
Purpose: This sketch demonstrates how to use an external interrupt
on a digital input pin to toggle the built-in user LED each time
a push button is pressed.
 
@author Arduino Product Experience Team
@version 1.0 06/10/26
*/
 
// Pin definitions
const int buttonPin = 2;            // Button input on D2
const int ledPin = LED_BUILTIN;     // Built-in LED
 
// Debounce time in milliseconds
const unsigned long debounceTime = 50;
 
// Variables shared with the interrupt service routine
volatile bool buttonPressed = false;
 
// Variables to store the LED state and the last valid press
bool ledState = false;
unsigned long lastPressTime = 0;
 
// Interrupt service routine, keep it short
void onButtonPress() {
  buttonPressed = true;
}
 
void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
 
  // Configure pins
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
 
  // Turn off LED initially
  digitalWrite(ledPin, LOW);
 
  // Trigger the interrupt when the button pulls the pin LOW
  attachInterrupt(digitalPinToInterrupt(buttonPin), onButtonPress, FALLING);
 
  Serial.println("- Arduino Nano XL Link - Digital Interrupt Example started...");
  Serial.println("- Press button to toggle the built-in LED");
}
 
void loop() {
  // Check if the interrupt detected a button press
  if (buttonPressed) {
    buttonPressed = false;
 
    // Ignore presses detected within the debounce time
    if (millis() - lastPressTime > debounceTime) {
      lastPressTime = millis();
 
      // Toggle LED state
      ledState = !ledState;
      digitalWrite(ledPin, ledState);
 
      Serial.print("- Button pressed! LED is now ");
      if (ledState) {
        Serial.println("ON");
      } else {
        Serial.println("OFF");
      }
    }
  }
}
```
 
To test this example, connect a push button to the Nano XL Link board as follows:
 
- Connect one leg of a push button to pin `D2`
- Connect the other leg of the push button to `GND`
- No external components needed (using the built-in LED and the internal pull-up resistor)
 
You should now see the built-in user LED toggle on and off each time you press the button. The interrupt is triggered on the falling edge (`FALLING`) of the pin, and the sketch ignores presses detected within 50 ms of the previous one to filter out the mechanical bounce of the button. Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see messages indicating when the button is pressed and the current LED state.
 
<Alert type="info">
Keep interrupt service routines as short as possible. In this example, the routine only sets a flag, and the LED and Serial Monitor updates are handled in the `loop()` function.
</Alert>

### Analog Pins
 
The Nano XL Link features **8 analog input pins** (`A0` to `A7`) that can be read using the `analogRead()` function. These pins allow you to measure continuously varying voltages, making them suitable for reading sensors like potentiometers, light sensors, temperature sensors and other analog components. The analog-to-digital converter (ADC) of the PIC32CK microcontroller converts the analog voltage into a digital value that your sketch can process.
 
The Nano XL Link analog pins provide the following functionality:
 
| **Arduino Pin** | **Digital Pin** | **Microcontroller Pin** | **Header Pin** | **ADC Channel** |
| :-------------: | :-------------: | :---------------------: | :------------: | :-------------: |
|      `A0`       |      `D14`      |         `PB12`          |     `J3-7`     |   ADC0 ch 11    |
|      `A1`       |      `D15`      |         `PA05`          |     `J3-9`     |    ADC0 ch 1    |
|      `A2`       |      `D16`      |         `PA06`          |    `J3-11`     |    ADC0 ch 2    |
|      `A3`       |      `D17`      |         `PA07`          |    `J3-13`     |    ADC0 ch 3    |
|      `A4`       |      `D18`      |         `PA11`          |    `J3-15`     |    ADC0 ch 7    |
|      `A5`       |      `D19`      |         `PA12`          |    `J3-17`     |    ADC0 ch 8    |
|      `A6`       |      `D20`      |         `PA09`          |    `J3-19`     |    ADC0 ch 5    |
|      `A7`       |      `D21`      |         `PA10`          |    `J3-21`     |    ADC0 ch 6    |
 
<Alert type="info">
Important note: Unlike the classic Nano boards, pins `A4` and `A5` of the Nano XL Link are not connected to the I²C bus. The I²C interfaces of the board are available on the Qwiic connector (`Wire`) and on pins `D26` and `D27` (`Wire1`).
</Alert>
 
The Nano XL Link's analog pins offer the following specifications:
 
|   **Specification**   |   **Value**   |            **Notes**             |
| :-------------------: | :-----------: | :------------------------------: |
|     Input Voltage     | 0 to +3.3 VDC |    Maximum safe input voltage    |
|  Default Resolution   |    10-bit     |  Values 0-1023 (`analogRead()`)  |
| Hardware Resolution   |    12-bit     |          Values 0-4095           |
|   Default Reference   |   +3.3 VDC    |      Microcontroller supply      |
 
You can read analog values using the `analogRead()` function:
 
```arduino
value = analogRead(pin);
```
 
The ADC of the Nano XL Link samples at 12 bits, but by default `analogRead()` returns 10-bit values (0 to 1023) for compatibility with other Arduino boards. You can change the returned resolution using the `analogReadResolution()` function in the `setup()` of your sketch; for example, `analogReadResolution(12)` returns the full 12-bit range (0 to 4095).
 
The following example demonstrates how to read an analog value with the full 12-bit resolution and display it on the Serial Monitor:
 
```arduino
/**
Analog Input Example for the Arduino Nano XL Link Board
Name: nano_xl_link_analog_input.ino
Purpose: This sketch demonstrates how to read an analog input
with the 12-bit ADC and display the value on the Serial Monitor.
 
@author Arduino Product Experience Team
@version 1.0 06/10/26
*/
 
// Analog input pin
const int analogPin = A0;
 
void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
 
  // Set analog read resolution to 12-bit (0 - 4095)
  analogReadResolution(12);
 
  Serial.println("- Arduino Nano XL Link - Analog Input Example started...");
  Serial.println("- Reading analog values from pin A0 (12-bit resolution)");
}
 
void loop() {
  // Read the analog value (0 - 4095 with 12-bit resolution)
  int analogValue = analogRead(analogPin);
 
  // Convert to voltage (0 to +3.3 VDC)
  float voltage = analogValue * (3.3 / 4095.0);
 
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

To test this example, connect a potentiometer to the Nano XL Link board as follows:
 
- Connect the middle pin of the potentiometer to `A0`
- Connect one outer pin of the potentiometer to `+3V3`
- Connect the other outer pin of the potentiometer to `GND`
 
You can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the real-time analog values and voltage measurements as you adjust the potentiometer. As you turn the potentiometer, the values will range from 0 to 4095, with corresponding voltage readings from 0 to +3.3 VDC.

<Alert type="warning">
Do not connect the potentiometer to the `+VBUS` pin. Applying more than +3.3 VDC to an analog input can permanently damage the board.
</Alert>

### PWM (Pulse Width Modulation)
 
The Nano XL Link features multiple pins with PWM capability that can be used to generate analog-like output signals. PWM works by rapidly switching a digital output between `HIGH` and `LOW` states, where the ratio of `HIGH` time to the total period determines the effective analog voltage output.
 
The Nano XL Link board provides PWM functionality on the following pins:
 
| **Arduino Pin** | **Microcontroller Pin** | **Timer** | **Output** |
| :-------------: | :---------------------: | :-------: | :--------: |
|      `D2`       |         `PC19`          |  `TCC1`   |   `WO4`    |
|      `D3`       |         `PC20`          |  `TCC1`   |   `WO5`    |
|      `D4`       |         `PA21`          |  `TCC4`   |   `WO1`    |
|      `D5`       |         `PA20`          |  `TCC4`   |   `WO0`    |
|      `D6`       |         `PB11`          |  `TCC3`   |   `WO6`    |
|      `D7`       |         `PD11`          |  `TCC2`   |   `WO2`    |
|      `D8`       |         `PA23`          |  `TCC5`   |   `WO1`    |
|      `D9`       |         `PB24`          |  `TCC6`   |   `WO1`    |
|  `LEDR` (`D39`) |         `PC15`          |  `TCC1`   |   `WO0`    |
|  `LEDG` (`D40`) |         `PC16`          |  `TCC1`   |   `WO1`    |
|  `LEDB` (`D41`) |         `PC17`          |  `TCC1`   |   `WO2`    |
 
<Alert type="info">
Important note: Pins `D2` and `D3` share the `TCC1` timer with the three channels of the RGB LED, and pins `D4` and `D5` share the `TCC4` timer. Pins that share a timer always run at the same PWM frequency.
</Alert>
 
The Nano XL Link's PWM offers the following technical specifications:
 
|  **Specification**  |   **Value**   |           **Notes**            |
| :-----------------: | :-----------: | :----------------------------: |
| Default Resolution  | 8-bit (0-255) | Standard Arduino compatibility |
|  Default Frequency  |    500 Hz     |   Defined by the board core    |
|   Output Voltage    | 0 to +3.3 VDC |      +3.3 VDC logic level      |
 
You can use PWM pins as analog output pins with the `analogWrite()` function:
 
```arduino
analogWrite(pin, value);
```
 
**By default, the resolution is 8-bit (0 to 255)**. You can use the `analogWriteResolution()` function to change the range of values accepted by `analogWrite()`:
 
```arduino
analogWriteResolution(resolution);
```
<Alert type="warning">
If `analogWrite()` is called on a pin without PWM capability, the core configures the pin as a digital output and sets it `HIGH` for values above half of the range, or `LOW` otherwise.
</Alert>
 
The following example demonstrates how to fade an LED connected to pin `D3`:
 
```arduino
/**
PWM Example for the Arduino Nano XL Link Board
Name: nano_xl_link_pwm_led.ino
Purpose: This sketch demonstrates how to use PWM to control
the brightness of an external LED connected to pin D3.
 
@author Arduino Product Experience Team
@version 1.0 06/10/26
*/
 
// PWM output pin
const int ledPin = 3;
 
void setup() {
  // Initialize serial communication and wait up to 2.5 seconds for a connection
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
 
  // No need to set pinMode for PWM pins - analogWrite() handles this
 
  Serial.println("- Arduino Nano XL Link - PWM LED Example started...");
  Serial.println("- External LED on D3 will fade in and out continuously");
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
 
To test this example, connect an LED to the Nano XL Link board as follows:
 
- Connect the anode (longer leg) of the LED to pin `D3` through a 220 Ω resistor
- Connect the cathode (shorter leg) of the LED to `GND`
 
You should now see the LED gradually fade in and out, creating a smooth breathing effect that repeats continuously. Additionally, you can open the Arduino IDE's Serial Monitor (Tools > Serial Monitor) to see the status messages that the example sketch sends at key brightness levels.