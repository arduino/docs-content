---
title: 'Arduino Nesso N1 User Manual'
difficulty: beginner
compatible-products: [nesso-n1]
description: 'Learn how to set up and use the Arduino Nesso N1, a ready to use IoT development board.'
tags:
  - User Manual
  - Cheat sheet
  - ESP32-C6
  - Bluetooth
  - Wi-Fi 6
  - LoRa
  - Thread
  - Zigbee®
  - Matter
author: 'Ernesto Voltaggio'
hardware:
  - hardware/09.kits/maker/nesso-n1
software:
  - ide-v1
  - ide-v2
  - iot-cloud
  - web-editor
---

The **Arduino® Nesso N1** is an all-in-one enclosed development board. Based on the ESP32-C6 System on Chip (SoC), it integrates a suite of communication protocols, including 2.4 GHz Wi-Fi® 6, Bluetooth® 5.3 LE, 802.15.4 (Thread/Zigbee®), and long-range LoRa®. It also includes a 1.14" color touchscreen, buttons, and a built-in LiPo battery for immediate user interaction in portable applications.

This document serves as a comprehensive user manual for the Nesso N1, providing technical specifications, setup guides, and detailed explanations of its features to help you bring your projects to life.

![ ](assets/hero-banner.png)

## Hardware and Software Requirements

### Hardware Requirements

- [Nesso N1](https://store.arduino.cc/products/nesso-n1) (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)

### Software Requirements

- [Arduino IDE](https://www.arduino.cc/en/software) or [Arduino Cloud Editor](https://app.arduino.cc/sketches)
- [ESP32 Boards core by Espressif](https://github.com/espressif/arduino-esp32)

## Board Overview

The Nesso N1 packs a rich set of features into a compact and portable form factor. It includes an integrated color touchscreen, multiple sensors, programmable buttons, and extensive expansion options, all powered by a rechargeable LiPo battery with power management.

![Arduino Nesso N1 Pinout](assets/simple-pinout.png)

The full pinout is available and downloadable as a PDF from the link below:

- [Nesso N1 pinout](../../downloads/TPX00227-full-pinout.pdf)

### Datasheet

The full datasheet is available as a downloadable PDF from the link below:

- [Nesso N1 datasheet](../../datasheets/TPX00227-datasheet.pdf)

### Main Components

- **ESP32-C6 SoC**: A powerful single-core RISC-V microcontroller with integrated Wi-Fi® 6, Bluetooth® 5.3 LE, and 802.15.4 radios.
- **SX1262 LoRa® Module**: A long-range, low-power LoRa® transceiver for communication in remote or challenging environments.
- **1.14" Color Touchscreen**: An intuitive IPS display for user interaction and data visualization.
- **BMI270 IMU**: A 6-axis Inertial Measurement Unit for precise motion and orientation sensing.
- **Rechargeable Battery**: A built-in 250 mAh LiPo battery with a sophisticated power management system for portable applications.
- **Expansion Connectors**: Standard Grove and Qwiic interfaces, plus an 8-pin port compatible with the M5StickC HAT series for easy hardware expansion.
- **Onboard Peripherals**: Includes an infrared (IR) transmitter, a buzzer for audio feedback, a built-in LED, and two programmable user buttons.

## Installation

The Nesso N1 can be programmed using the Arduino IDE or the Arduino Cloud Editor. To get started, you will need to install the appropriate board package.

### Arduino IDE

To use the board in the Arduino IDE, you need to install the latest version of the **esp32 by Espressif Systems** package from the boards manager.

1.  Open the Arduino IDE.
2.  Navigate to **Boards Manager** (**Tools > Board > Boards Manager...**).
3.  Search for **"esp32"** and find the package by **Espressif Systems**.
4.  Click the **Install** button.
5.  Once installed, select **Arduino Nesso N1** from the **Tools > Board > esp32** menu.

### Arduino Cloud Editor

The Arduino Cloud Editor is an online IDE that supports the Nesso N1 without requiring manual installation of the board package.

Read more in the [Getting Started with the Cloud Editor](https://docs.arduino.cc/arduino-cloud/guides/editor/) guide.

## First Use

### Unboxing the Product

When opening the Nesso N1 box, you will find the device and a hexagon key. The device comes pre-assembled in a sleek enclosure.

![Nesso N1 form factor](assets/unboxing.png)

The detachable LoRa® antenna is conveniently stored in a compartment on the back of the device. You can slide it out to connect it to the MMCX connector for long-range communication.

![Nesso N1 LoRa® antenna](assets/lora-antenna.png)

For projects where a slimmer profile is desired, the included hexagon key can be used to remove the antenna storage compartment, making the device thinner.

![Removable Antenna Storage](assets/antenna-storage-removable.png)

***The Nesso N1 does not include a USB-C® cable, which is required to connect the board to your computer. A compatible cable is [available separately here](https://store.arduino.cc/products/usb-cable2in1-type-c).***

## Power Supply

The Nesso N1 can be powered in three ways:

- **USB-C® Connector**: Provide a regulated 5 V DC supply through the USB-C® port. This method also charges the internal battery.
- **Built-in Battery**: The onboard 250 mAh LiPo battery allows the device to operate untethered, making it ideal for portable and remote monitoring applications.
- **VIN Pin**: You can use the `VIN` pin on the 8-pin expansion header to power the board from an external 5 V DC source.

***WARNING: Handle the internal LiPo battery with care. Do not puncture, short-circuit, or expose it to high temperatures.***

## Battery Management

The board incorporates a power management system featuring the **AW32001** power path management chip and the **BQ27220** battery monitoring chip. This system provides:

- **Automatic Charging**: The battery charges automatically when a 5 V source is connected via USB-C®.
- **Real-Time Monitoring**: You can programmatically access battery voltage, current, and capacity to monitor the power status of your application.
- **Over-Current & Over-Voltage Protection**: Ensures safe and stable operation during charging and discharging cycles.

## Microcontroller (ESP32-C6)

At the core of the Nesso N1 is the **ESP32-C6**, a highly integrated SoC from Espressif.

### Key Features

- **CPU**: Single-core 32-bit RISC-V, up to 160 MHz.
- **Memory**: 16 MB external flash + 1536 kB on-chip SRAM.

The ESP32-C6 features a comprehensive set of connectivity options:

- 2.4 GHz Wi-Fi® 6 (802.11ax).
- Bluetooth® 5.3 Low Energy.
- 802.15.4 radio for Thread and Zigbee® protocols.
- Support for the Matter protocol.

***WARNING: All GPIO pins are 3.3 V logic only and are not 5 V tolerant.***

## Pins

The Nesso N1 exposes a variety of pins for interacting with internal and external hardware. Some pins are connected directly to the ESP32-C6, while others are managed by two PI4IOE5V6408 I/O expanders to provide additional functionality.

### Direct ESP32-C6 Pins

These pins are directly controlled by the main microcontroller.

| Pin Name | GPIO | Function |
| :--- | :--- | :--- |
| `SDA` | 10 | I2C Data |
| `SCL` | 8 | I2C Clock |
| `MOSI` | 21 | SPI Master Out Slave In |
| `MISO` | 22 | SPI Master In Slave Out |
| `SCK` | 20 | SPI Serial Clock |
| `IR_TX_PIN` | 9 | Infrared Transmitter Output |
| `BEEP_PIN` | 11 | Buzzer Output |
| `GROVE_IO_0` | 5 | Grove Connector I/O |
| `GROVE_IO_1` | 4 | Grove Connector I/O |
| `LORA_IRQ` | 15 | LoRa® Module Interrupt Request |
| `LORA_CS` | 23 | LoRa® Module Chip Select (SPI) |
| `LORA_BUSY` | 19 | LoRa® Module Busy Indicator |
| `SYS_IRQ` | 3 | System Interrupt (from IMU & I/O expander) |
| `LCD_CS` | 17 | LCD Chip Select (SPI) |
| `LCD_RS` | 16 | LCD Register Select |
| `D1` | 7 | 8-pin Header Digital I/O |
| `D2` | 2 | 8-pin Header Digital I/O |
| `D3` | 6 | 8-pin Header Digital I/O |

### I/O Expander Pins

The Nesso N1 uses two PI4IOE5V6408 I/O expanders (addresses `0x43` and `0x44`) to manage additional pins over the I2C bus. These pins are accessed in code using special `ExpanderPin` objects.

| Pin Object | Expander Port | Function |
| :--- | :--- | :--- |
| `KEY1` | E0.P0 | Programmable Button 1 |
| `KEY2` | E0.P1 | Programmable Button 2 |
| `LORA_LNA_ENABLE` | E0.P5 | LoRa® Low-Noise Amplifier Enable |
| `LORA_ANTENNA_SWITCH` | E0.P6 | LoRa® RF Antenna Switch Control |
| `LORA_ENABLE` | E0.P7 | LoRa® Module Reset/Enable |
| `POWEROFF` | E1.P0 | System Power Off Control |
| `LCD_RESET` | E1.P1 | LCD Reset |
| `GROVE_POWER_EN` | E1.P2 | Grove Connector Power Enable |
| `VIN_DETECT` | E1.P5 | External Power (VIN) Detection |
| `LCD_BACKLIGHT` | E1.P6 | LCD Backlight Control |
| `LED_BUILTIN` | E1.P7 | Onboard Status LED (Green) |

To use an expander pin, you must first initialize it with `pinMode()`, then you can use `digitalWrite()` and `digitalRead()` as with standard pins.


## Battery

You can interact with the battery system using the `NessoBattery` object and expander pins.

### Enable Charge

```arduino
// The NessoBattery object is available by default
NessoBattery battery;

void setup() {
  Serial.begin(115200);

  // Enable battery charging (it is enabled by default)
  battery.enableCharge();

}

void loop() {
}
```
### Read Battery Voltage


Additionally the `VIN_DETECT` expander pin can be read to determine if external power is connected (`HIGH` if connected, `LOW` if running on battery).


## Buttons and LED

The Nesso N1 features several physical controls for user interaction.

### Power Button

The Nesso N1 has a multi-function button for power control:

- **Click (from off state)**: Power on.
- **Click (from on state)**: Reset the device.
- **Double-click (from on state)**: Power off.
- **Press and hold (from on state)**: Enter Download/Bootloader mode.

![Power Button](assets/power-button.png)


Additionally the `POWEROFF` expander pin allows you to shut down the device programmatically.


### User Buttons

The board has two physical buttons, **KEY1** and **KEY2**, that are connected to the I/O expander. These can be read using `digitalRead()`.

![User Buttons](assets/programmable-buttons.png)

```arduino
void setup() {
  Serial.begin(115200);
  pinMode(KEY1, INPUT_PULLUP);
  pinMode(KEY2, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(KEY1) == LOW) {
    Serial.println("Button 1 pressed!");
    delay(200); // Simple debounce
  }
  if (digitalRead(KEY2) == LOW) {
    Serial.println("Button 2 pressed!");
    delay(200); // Simple debounce
  }
}
```

### Built-in Programmable LED

The board has an onboard green LED that can be controlled using the `LED_BUILTIN` object. It is visible on the side of the board through the power button gaps.

![Built-in LED](assets/built-in-led.png)

```arduino
void setup() {
  // Configure the built-in LED as an output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Blink the LED
  digitalWrite(LED_BUILTIN, LOW); // Turn LED ON
  delay(500);
  digitalWrite(LED_BUILTIN, HIGH); // Turn LED OFF
  delay(500);
}
```

***Please note that `LED_BUILTIN` uses inverted logic. Writing `LOW` to the pin turns the LED on, while writing `HIGH` turns it off.***


## Display & Touchscreen

The Nesso N1 features a 1.14-inch IPS color touchscreen with a resolution of 135 x 240 pixels.

- **Display Controller**: ST7789, controlled via SPI.
- **Touch Controller**: FT6336U, controlled via I2C.

The display can be programmed using the **M5GFX** library, which can be installed using the Arduino IDE Library Manager.

Here is an example to display touch input as text on the screen:

```arduino
#include <M5GFX.h>

M5GFX display;  // Create a display instance

void setup() {
  // Initialize the display
  display.begin();

  // Set the display to landscape (horizontal) mode
  display.setRotation(1);

  // Set text properties
  display.setTextDatum(MC_DATUM); // Middle-Center datum for text alignment
  display.setTextColor(TFT_WHITE, TFT_BLACK);
  display.setTextSize(2);

  // Clear the screen and display an initial message
  display.fillScreen(TFT_BLACK);
  display.drawString("Touch the screen", display.width() / 2, display.height() / 2);
}

void loop() {
  // Create a structure to hold touch data
  lgfx::touch_point_t tp;

  // Check if the screen is being touched
  if (display.getTouch(&tp)) {
    String touch = "X: " + String(tp.x) + " Y:" + String(tp.y);
    display.fillScreen(TFT_BLACK); 
    
    // Draw the string at the center of the screen
    display.drawString(touch, display.width() / 2, display.height() / 2);
  }

  // A small delay to keep the loop responsive
  delay(50);
}
```

## Connectivity

### Wi-Fi®, Bluetooth®, Thread & Zigbee®

The ESP32-C6 provides a rich set of wireless protocols, making the Nesso N1 a powerful hub for IoT projects.

- **Wi-Fi® 6**: Offers higher efficiency, lower latency, and improved performance in dense wireless environments.
- **Bluetooth® 5.3 Low Energy (LE)**: Enables communication with a wide range of mobile devices and low-power sensors.
- **Thread & Zigbee®**: The 802.15.4 radio allows the Nesso N1 to participate in low-power mesh networks, essential for smart home and industrial applications. It also supports the **Matter** protocol for interoperability.

### LoRa®

The onboard **SX1262** module provides long-range, low-power communication capabilities, operating in the 850–960 MHz frequency range. It comes with a detachable external antenna that connects via an MMCX connector.

![LoRa® Antenna Attached](assets/antenna-mounted.png)

***WARNING: To avoid damage to your board, always use the LoRa® module with the antenna attached.***

The LoRa® module is controlled via SPI and several dedicated pins on both the ESP32-C6 and the I/O expander.

| Pin Name | GPIO | Expander Port | Function |
| :--- | :--- | :--- | :--- |
| `MOSI` | 21 | | SPI Master Out Slave In |
| `MISO` | 22 | | SPI Master In Slave Out |
| `SCK` | 20 | | SPI Serial Clock |
| `LORA_IRQ` | 15 | | LoRa® Module Interrupt Request |
| `LORA_CS` | 23 | | LoRa® Module Chip Select (SPI) |
| `LORA_BUSY` | 19 | | LoRa® Module Busy Indicator |
| `LORA_LNA_ENABLE` | | E0.P5 | LoRa® Low-Noise Amplifier Enable |
| `LORA_ANTENNA_SWITCH` | | E0.P6 | LoRa® RF Antenna Switch Control |
| `LORA_ENABLE` | | E0.P7 | LoRa® Module Reset/Enable |

Here is a simple example to send a LoRa® packet using the [RadioLib](https://github.com/jgromes/RadioLib) library:

```arduino
#include <RadioLib.h>

// Create an SX1262 radio object
SX1262 radio = new Module(LORA_CS, LORA_IRQ, LORA_ENABLE, LORA_BUSY);

void setup() {
  Serial.begin(115200);

  // Initialize the LoRa® module
  // Frequency: 915.0 MHz
  int state = radio.begin(915.0);
  if (state != RADIOLIB_ERR_NONE) {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true);
  }
}

void loop() {
  Serial.print(F("[SX1262] Transmitting packet... "));

  // Send a simple string
  int state = radio.transmit("Hello World!");

  if (state == RADIOLIB_ERR_NONE) {
    Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
  }
  
  delay(5000);
}
```

## Onboard Sensors & Peripherals

### 6-Axis IMU

The **BMI270** is a high-performance 6-axis Inertial Measurement Unit (IMU) that combines a 3-axis accelerometer and a 3-axis gyroscope. It connects to the ESP32-C6 via the I2C bus (`SCL` on GPIO8, `SDA` on GPIO10) and provides an interrupt signal on `SYS_IRQ` (GPIO3). It is ideal for motion tracking, gesture recognition, and orientation sensing.

Here is a minimal example using the [Arduino_BMI270_BMM150](https://github.com/arduino-libraries/arduino_bmi270_bmm150)  library:

```arduino
#include <Arduino_BMI270_BMM150.h>

void setup() {
  Serial.begin(115200);
  while (!Serial); // Wait for serial port to connect

  Serial.println("Initializing IMU...");
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accel Rate: ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");

  Serial.print("Gyro Rate: ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");

  Serial.println("X\tY\tZ\t\t| X\tY\tZ");
  Serial.println("Accel (g)\t\t| Gyro (°/s)");
}

void loop() {
  float ax, ay, az;
  float gx, gy, gz;

  if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
    IMU.readAcceleration(ax, ay, az);
    IMU.readGyroscope(gx, gy, gz);

    Serial.print(ax, 2);
    Serial.print('\t');
    Serial.print(ay, 2);
    Serial.print('\t');
    Serial.print(az, 2);
    Serial.print("\t| ");
    Serial.print(gx, 2);
    Serial.print('\t');
    Serial.print(gy, 2);
    Serial.print('\t');
    Serial.println(gz, 2);
  }

  delay(100);
}
```

### Buzzer

A passive buzzer connected to `BEEP_PIN` (GPIO11) provides audible feedback. You can generate simple tones using the standard `tone()` function.

```arduino
void setup() {
  // No setup needed for tone()
}

void loop() {
  // Play a 1 kHz tone for 500 ms
  tone(BEEP_PIN, 1000, 500);
  delay(2000);
}
```

### Infrared (IR) Transmitter

An onboard IR LED connected to `IR_TX_PIN` (GPIO9) allows the Nesso N1 to function as a remote control for various electronic devices.

Here is an example using the [IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote) library to send a NEC command:

```arduino
#include <IRremote.h>

void setup() {
  Serial.begin(115200);
  IrSender.begin(IR_TX_PIN);
}

void loop() {
  Serial.println("Sending IR signal...");
  // Send a NEC command: Address 0x01, Command 0x04
  IrSender.sendNEC(0x01, 0x04, 1);
  delay(2000);
}
```

***Please note: There is a known hardware timer conflict between the tone() function and the IRremote library. To use both features in the same sketch, you must fully reset the pin and re-initialize the IR sender before each transmission. First, set the pin mode to INPUT to release it from the timer, then call IrSender.begin() to reconfigure it for IR.***

## Expansion Ports

### Voltage Compatibility Considerations

Before connecting any external components to your Nesso N1, it is important to understand its voltage characteristics to prevent damage to your sensors and modules:

**The Nesso N1 operates at 3.3 VDC**, which means:

- All digital I/O pins use 3.3 VDC logic levels (HIGH = 3.3 VDC, LOW = 0 VDC).
- Analog inputs can safely accept 0 to 3.3 VDC.
- Communication pins (I2C, SPI, UART) operate at 3.3 VDC logic levels.

**For 5 VDC components**, you must add **external level shifters** for digital communication pins.

Always check your component's datasheet for voltage specifications before connecting. When in doubt, use a multimeter to verify voltage levels or add protective level shifting.

### Qwiic Connector

The Nesso N1 includes one standard **Qwiic** connector for easy, solder-free expansion. It provides a 3.3 V I2C interface (`SCL` on GPIO8, `SDA` on GPIO10).

![Qwiic Connector](assets/qwiic-connector.png)

### Grove Connector

The Nesso N1 also includes one standard **Grove** connector. It provides a 5 V interface with two digital I/O pins (`GROVE_IO_0` on GPIO5, `GROVE_IO_1` on GPIO4).

![Grove Connector](assets/grove-connector.png)

### 8-Pin Expansion Port

An 8-pin female header provides access to additional I/O and power pins. It is designed to be compatible with the **M5StickC HAT** series of expansion boards.

![8 pins Expansion Port](assets/expansion-port.png)

| # | Pin Name | GPIO | Function |
| :-- | :--- | :--- |:--- |
| 1 | `GND` | - | Ground |
| 2 | `+5V OUT` | - | 5 V Output |
| 3 | `D1` | 7 | Digital PWM I/O |
| 4 | `D3` | 6 | Digital PWM I/O |
| 5 | `D2` | 2 | Digital PWM I/O |
| 6 | `BATTERY OUT` | - | Direct Battery Voltage Output |
| 7 | `+3V3 OUT` | - | 3.3 V Output |
| 8 | `+5V IN` | - | 5 V Input (VIN) |

***The `BATTERY OUT` pin provides the direct, unregulated voltage from the LiPo battery. Be cautious when using this pin, as the voltage will vary depending on the charge level.***