---
title: 'Nicla Voice User Manual'
difficulty: beginner
compatible-products: [nicla-voice]
description: 'Learn about the hardware and software features of the Arduino® Nicla Voice.'
tags: 
  - IMU
  - Cheat sheet
  - RGB
  - Communication
author: 'José Bagur, Benjamin Dannegård and Christopher Méndez'
hardware:
  - hardware/06.nicla/boards/nicla-voice
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

This user manual will provide you with a comprehensive overview of the Arduino Nicla Voice board, covering its main hardware and software features. This user manual will also show you how to set up, configure, and use these features. 

## Hardware and Software Requirements

### Hardware Requirements

- [Nicla Voice](https://store.arduino.cc/products/nicla-voice) (x1)
- [Micro USB cable](https://store.arduino.cc/products/usb-2-0-cable-type-a-micro) (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Cloud Editor](https://create.arduino.cc/editor)
- To create custom Machine Learning models, the integrated [Machine Learning Tools](https://cloud.arduino.cc/machine-learning-tools/) of the [Arduino Cloud](https://create.arduino.cc/iot/) are needed. In case you do not have an Arduino Cloud account, you will need to create one first.

## Product Overview

The Nicla Voice is an innovative and versatile development board designed by the Arduino team for sound-enabled projects and applications. This board has an onboard always-on speech recognition and sensor-fusion processor, advanced motion sensors, and wireless connectivity via Bluetooth® Low Energy. The Nicla Voice is an ideal solution for various applications, from ultra-low power predictive maintenance and gesture or voice recognition systems to contactless wireless applications.

### Board Architecture Overview

The Nicla Voice features a robust and efficient architecture integrating various components to enable speech, sound, and motion projects and applications. 

![The Nicla Voice main components (top view)](assets/user-manual-2.png)

![The Nicla Voice main components (bottom view)](assets/user-manual-3.png)

Here is an overview of the board's architecture's main components shown in the images above:

- **Microcontroller**: at the heart of the Nicla Voice is the nRF52832, a powerful and versatile System-on-Chip (SoC) from Nordic® Semiconductor. The nRF52832 is built around a 32-bit Arm® Cortex®-M4 processor running at 64 MHz.
- **Speech and sensor-fusion processor**: the board features the NDP120 Neural Decision Processor™, an ultra-low power always-on audio and sensor-fusion processor from Syntiant®, which enables several applications, including echo-cancellation, beamforming, noise suppression, speech enhancement, speaker identification, keyword spotting, acoustic event and scene classification, and multi-sensor fusion. 
- **Onboard advanced motion sensors**: the board features the BMI270, a high-precision Inertial Measurement Unit (IMU) from Bosch® Sensortec, which combines a 3-axis accelerometer and a 3-axis gyroscope for precise motion tracking and orientation detection. The board also features the BMM150, a compact geomagnetic sensor from Bosch® Sensortec with a 3-axis magnetometer.
- **Onboard high-performance microphone**:  the Nicla Voice is equipped with the IM69D130, a high-quality MEMS microphone by Infineon® Technologies. The IM69D130 offers excellent audio quality and low noise performance, ensuring accurate and distortion-free audio capturing.
- **Onboard connector for external PDM microphone**: an external PDM microphone can be connected to the board via an onboard connector.  
- **Wireless connectivity**: the board supports Bluetooth® Low Energy connectivity, provided by the ANNA-B112 module developed by u-blox®. This compact, high-performance Bluetooth® Low Energy module allows the Nicla Voice to communicate wirelessly with other devices and systems.
- **Power management**: the Nicla Voice is designed for ultra-low power operation, with efficient power management features that ensure minimal energy consumption even when using always-on speech recognition and multiple sensors. The Nicla Voice features the BQ25120 from Texas Instruments®; a highly integrated battery charge management integrated circuit (IC) designed for wearables and Internet of Things (IoT) devices. 

### Board Core and Libraries

The **Arduino Mbed OS Nicla Boards** core contains the libraries and examples you need to work with the board's components, such as its IMU, magnetometer, and onboard microphone. To install the core for Nicla boards, navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `nicla` and install the latest `Arduino Mbed OS Nicla Boards` version.


![Installing the Arduino Mbed OS Nicla Boards core in the Arduino IDE bootloader](assets/dsp-install.png)

### Pinout

![Nicla Voice pinout](assets/nicla-voice-pinout.png)

The full pinout is available and downloadable as PDF from the link below:

- [Nicla Voice pinout](https://docs.arduino.cc/resources/pinouts/ABX00061-full-pinout.pdf)

### Datasheet

The complete datasheet is available and downloadable as PDF from the link below:

- [Nicla Voice datasheet](https://docs.arduino.cc/resources/datasheets/ABX00061-datasheet.pdf)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

- [Nicla Voice schematics](https://docs.arduino.cc/resources/schematics/ABX00061-schematics.pdf)

### STEP Files

The complete STEP files are available and downloadable from the link below:

- [Nicla Voice STEP files](../../downloads/ABX00061-step.zip)

## First Use

### Powering the Board

The Nicla voice can be powered by:

- Using a Micro USB cable (not included). 
- Using an external **5V power supply** connected to `VIN_BQ25120` pin (please refer to the [board pinout section](#pinout) of the user manual).
- Using a **3.7V Lithium Polymer (Li-Po) battery** connected to the board through the onboard battery connector; the manufacturer part number of the battery connector is BM03B-ACHSS and its matching receptacle manufacturer part number is ACHR-03V-S. The **recommended minimum battery capacity for the Nicla Voice is 200 mAh**. A Li-Po battery with an integrated NTC thermistor is also recommended for thermal protection. 
- Using the onboard **ESLOV connector**, which has a dedicated 5V power line.

![Different ways to power the Nicla Voice](assets/user-manual-6.png)

***A 3.7V Li-Po battery can be also connected through the board's pins: `1 (NTC)`, `2 (VBAT)`, and `6 (GND)`. Please refer to the board's [pinout](#pinout) to locate those pins on your Nicla Voice board.***

#### Onboard Battery Charger
<br></br>

The onboard battery charger of your board is, by default, **disabled**. To enable it, you can use the `enableCharging()` function defined in the Nicla Voice board core:

```arduino
// Enable the onboard battery charger 
// The function parameter defines the charging current in mA (between 5 mA and 300 mA)
nicla::enableCharging(100);
```

The desired charging current can be set to a value between 5 mA and 300 mA; the default value is 20 mA.

***A safe default charging current value that works for most common LiPo batteries is 0.5C, which means charging at a rate equal to half the battery's capacity. For example, a 200 mAh battery could be safely charged at 100 mA (0.1 A).***

 To disable the onboard battery charger, you can use the `disableCharging()` function defined in the Nicla Voice board core:

```arduino
// Disable the onboard battery charger 
nicla::disableCharging();
```

### NDP120 Processor Firmware Update

![NDP Syntiant AI Processor](assets/ndp.png)

It is recommended to update the NDP120 processor firmware and the built-in speech recognition model to the latest release. Follow these three steps to complete the update process:

1. Select the Nicla Voice board in the Arduino IDE so you can have access to the board built-in examples.
2. Upload the `Syntiant_upload_fw_ymodem` sketch. This sketch can be found in the board's built-in examples by navigating to **File > Examples > NDP > Syntiant_upload_fw_ymodem**. 
3. After uploading the sketch, **format your board's external Flash memory** before uploading the updated NDP120 processor firmware files. You can do this by navigating to the Arduino IDE Serial Monitor and typing `F` and then `Enter`.
4. Extract [this .zip file](assets/nicla_voice_uploader_and_firmwares.zip), which contains the compiled uploaders for various operating systems, and the updated NDP120 processor firmware and speech recognition model, in a known location on your computer. 
5. Open a new terminal in the location where the .zip file was extracted and execute the following command:

    ```bash
    syntiant-uploader-<OS> send -m "Y" -w "Y" -p $portName $filename
    ```

    Replace `portName` and `filename` with the relevant information. Three different files must be uploaded to the board by executing the following three commands, for example on **Windows** the commands are the following:

    ```bash
    ./syntiant-uploader-win send -m "Y" -w "Y" -p COM12 mcu_fw_120_v91.synpkg
    ```

    ```bash
    ./syntiant-uploader-win send -m "Y" -w "Y" -p COM12 dsp_firmware_v91.synpkg
    ```

    ```bash
    ./syntiant-uploader-win send -m "Y" -w "Y" -p COM12 alexa_334_NDP120_B0_v11_v91.synpkg
    ```

    ***As we are using Windows, the command used is `syntiant-uploader-win`, use your OS respective one.***

    Ensure all executed commands return a `filename sent successful` message in the console, as shown in the image below. 

    ![Uploader feedback messages](assets/fw_update.png)

After uploading the three files, your board's firmware is updated to the latest release and ready to be used.

#### External Memory Format

Your board NDP120 processor files (firmware and models) are stored in your board's external Flash memory. It is recommended to **format your Nicla Voice external Flash memory** every time you are going to update the processor firmware or when you are going to update/add models to the external Flash memory.

Follow these steps to perform the external memory format process:

1. Select the Nicla Voice board in the Arduino IDE so you can have access to the board built-in examples.
2. Upload the `Syntiant_upload_fw_ymodem` sketch. This sketch can be found in the board's built-in examples by navigating to **File > Examples > NDP > Syntiant_upload_fw_ymodem**. 
3. After uploading the sketch, navigate to the IDE's Serial Monitor, type `F`, and press `Enter`. Your board's external memory should be formatted now, you can confirm this by typing an `L` and pressing `Enter`.

After completing this process, you can upload NDP processor's firmware and model files to your board's external memory without issues as explained before.

### Built-in Speech Recognition Example

The speech recognition example can be found in the board's built-in examples by navigating to **File > Examples > NDP > AlexaDemo**. 

![Alexa speech recognition example](assets/alexa.png)

After successfully updating the NDP120 processor firmware and the speech recognition model to the latest release, we can upload the speech recognition example to the Nicla Voice. To test the example, say "Alexa"; this should make the onboard LED of the Nicla Voice blink blue if the keyword "Alexa" is recognized. If there is no response from the board, try speaking from a closer proximity or louder. You should also see in the Serial Monitor if the word "Alexa" was detected, as shown in the image below:

![AlexaDemo example feedback in the Arduino IDE Serial Monitor](assets/user-manual-5.png)

## Pins

The Nicla Voice pinout is shown in the image below:

![Nicla Voice pinout](assets/nicla-voice-pinout.png)

### Analog Pins

The Nicla Voice has **two analog input pins**, mapped as follows:

| **Microcontroller Pin** | **Arduino Pin Mapping** |
|:-----------------------:|:-----------------------:|
|      `ADC1`/`P0_02`     |           `A0`          |
|      `ADC2`/`P0_30`     |           `A1`          |

Both pins can be used through the built-in functions of the Arduino programming language.

Nicla boards ADC can be configured to 8, 10 or 12 bits defining the argument of the following function respectively (default is 10 bits):

```arduino
analogReadResolution(12);  // ADC resolution set to 12 bits (0-4095)
```

***The Nicla boards ADC reference voltage is fixed to 1.8V, this means that it will map the ADC range from 0 to 1.8 volts.***

The example code shown below reads the voltage value from a potentiometer connected to `A0` and displays it on the IDE Serial Monitor. To understand how to properly connect a potentiometer to the Nicla Voice pins, take the following image as a reference:

![ADC input example wiring](assets/adc-input.svg)

```arduino
#include "Nicla_System.h"

int sensorPin = A0;   // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {

  analogReadResolution(12); // ADC bits configuration
  nicla::begin();           // Nicla peripherals initialization, this enables the VDDIO_EXT 3.3V output.
  Serial.begin(115200);     // Serial initialization
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  // print the value
  Serial.println(sensorValue);
  delay(1000);
}
```

***The ADC inputs support 3.3V even when the ADC reference is 1.8V. In this perspective, the ADC will not sense any change from 1.8V and above.***

### Digital Pins

The Nicla Voice has **twelve digital pins**, mapped as follows:

| **Microcontroller Pin** | **Arduino Pin Mapping** |
|:-----------------------:|:-----------------------:|
|         `P0_10`         |           `0`           |
|         `P0_09`         |           `1`           |
|         `P0_20`         |           `2`           |
|         `P0_23`         |           `3`           |
|         `P0_22`         |           `4`           |
|         `P0_24`         |           `5`           |
|         `P0_29`         |           `6`           |
|         `P0_27`         |           `7`           |
|         `P0_28`         |           `8`           |
|         `P0_11`         |           `9`           |
|         `P0_02`         |           `A0`          |
|         `P0_30`         |           `A1`          |

Notice that analog pins `A0` and `A1` (`P0_02` and `P0_30`) can also be used as digital pins. Please, refer to the [board pinout section](#pins) of the user manual to find them on the board.

The digital pins of the Nicla Voice can be used as inputs or outputs through the built-in functions of the Arduino programming language. 

***The Nicla Voice digital I/O's are low power, so to drive output devices like LEDs, resistive loads, buzzers, etc, it is recommended to use a MOSFET driver or a buffer to guarantee the required current flow. Learn more about the Nicla I/O's considerations [here](https://docs.arduino.cc/learn/hardware/nicla-form-factor).***

The configuration of a digital pin is done in the `setup()` function with the built-in function `pinMode()` as shown below:

```arduino
// Pin configured as an input
pinMode(pin, INPUT);        

// Pin configured as an output
pinMode(pin, OUTPUT);        

// Pin configured as an input, internal pull-up resistor enabled
pinMode(pin, INPUT_PULLUP);  
```

The state of a digital pin, configured as an input, can be read using the built-in function `digitalRead()` as shown below:

```arduino
// Reads pin state, stores value in state variable
state = digitalRead(pin);
```

The state of a digital pin, configured as an output, can be changed using the built-in function `digitalWrite()` as shown below:

```arduino
// Set pin on
digitalWrite(pin, HIGH);    

// Set pin off
digitalWrite(pin, LOW);    
```

The example code shown below uses digital pin `3` to control an LED and reads the state of a button connected to digital pin `2`:

![Digital I/O example wiring](assets/digital-io-mosfet.svg)

```arduino
#include "Nicla_System.h"

// Define button and LED pin
int buttonPin = 2;
int ledPin = 3;

// Variable to store the button state
int buttonState = 0;

void setup() {

  nicla::begin();           // Nicla peripherals initialization, this enables the VDDIO_EXT 3.3V output.

  // Configure button and LED pins
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);

  // Initialize Serial communication
  Serial1.begin(9600);
}

void loop() {
  // Read the state of the button
  buttonState = digitalRead(buttonPin);

  // If the button is pressed, turn on the LED and print its state to the Serial Monitor
  if (buttonState == LOW) {
    digitalWrite(ledPin, HIGH);
    Serial1.println("- Button is pressed. LED is on.");
  } else {
    // If the button is not pressed, turn off the LED and print to the Serial Monitor
    digitalWrite(ledPin, LOW);
    Serial1.println("- Button is not pressed. LED is off.");
  }

  // Wait for 1000 milliseconds
  delay(1000);
}
```
### PWM Pins

Most digital and analog pins of the Nicla Voice can be used as PWM (Pulse Width Modulation) pins. This functionality of the Nicla Voice pins can be used with the built-in function `analogWrite()` as shown below:

```arduino
analogWrite(pin, value);  
```

By default, the output resolution is 8 bits, so the output value should be between 0 and 255. To set a greater resolution, do it using the built-in function `analogWriteResolution` as shown below:

```arduino
analogWriteResolution(bits);
```

Here is a complete example code that outputs a 50% duty-cycle PWM signal through pin 3 of the Nicla Voice:

```arduino
#include "Nicla_System.h"

#define out_pwm 3 // Nicla Voice pin 3

void setup() {
  // put your setup code here, to run once:
  nicla::begin();  // Nicla peripherals initialization, this enables the VDDIO_EXT 3.3V output.
  analogWriteResolution(12);
  analogWrite(out_pwm, 2048);
}

void loop() {
  // put your main code here, to run repeatedly:
}
```

Using this function has some limitations, for example, the PWM signal frequency is fixed at 500 Hz, and this could not be ideal for every application.

![PWM output signal using analogWrite()](assets/500-Hz.png)

If you need to work with a higher frequency PWM signal, you must do it by working with the PWM peripheral at a lower level as shown in the example code below:

```arduino
#include "Nicla_System.h"
#include "nrfx_pwm.h"

static nrfx_pwm_t pwm1 = NRFX_PWM_INSTANCE(0);

static uint16_t /*const*/ seq1_values[] = {0};

static nrf_pwm_sequence_t seq1 = {
  .values = { .p_common = seq1_values },
  .length = NRF_PWM_VALUES_LENGTH(seq1_values),
  .repeats = 0,
  .end_delay = 0
};

void setup() {

  nicla::begin();           // Nicla peripherals initialization, this enables the VDDIO_EXT 3.3V output.
  nrfx_pwm_config_t config1 = {
    .output_pins = {
      32 + 23,  // Nicla Voice pin 3  = pin P0_23 in the ANNAB112 MCU
    },
    .irq_priority = APP_IRQ_PRIORITY_LOWEST,
    .base_clock = NRF_PWM_CLK_1MHz,   // 1 us period
    .count_mode = NRF_PWM_MODE_UP,
    .top_value = 1000,                //  PWM counter limit, this will set the final output frequency 1MHz / 1000 = 1KHz
    .load_mode = NRF_PWM_LOAD_COMMON,
    .step_mode = NRF_PWM_STEP_AUTO,
  };

  nrfx_pwm_init(&pwm1, &config1, NULL);

  (*seq1_values) = 500;   // this variable sets the signal duty cycle, for a 50% we are using 500. (1000 / 500  = 1/2)
  (void)nrfx_pwm_simple_playback(&pwm1, &seq1, 1, NRFX_PWM_FLAG_LOOP);
}

void loop() {

}
```

The code above results in a 1KHz square waveform with a 50% duty cycle as in the image below. The frequency is defined by the `.base_clock` and `.top_value` variables, and the duty cycle by the `seq1_values` variable.

![PWM output signal using the PWM at a lower level](assets/1000-Hz.png)

## Onboard Sensors

The Nicla Voice boards come with various onboard sensors that allow you to capture and process environmental and motion data via a high-performance microphone, a 6-axis IMU, and a 3-axis magnetometer. The onboard sensors can be used for developing various applications, such as voice recognition, gesture control, and environmental monitoring.

### Microphone

The onboard high-performance microphone of the Nicla Voice is the IM69D130 from Infineon® Technologies. The IM69D130 is specifically designed for applications that require high-quality audio recording and accurate voice detection, such as voice-controlled Internet of Things (IoT) devices, smart home systems, and mobile devices.

![Nicla Voice onboard high-performance microphone](assets/user-manual-9.png)

An external PDM microphone can be connected to the board via an onboard Zero Insertion Force (ZIF) connector. The manufacturer part number of the onboard ZIF connector is FH33J-4S-0.5SH(99); a 4-pin 0.5 mm pitch FFC cable is compatible with this connector.

![Nicla Voice onboard ZIF connector](assets/user-manual-10.png)

The example code shown below captures audio from the onboard microphone of the Nicla Voice, compresses the audio using the G722 codec, and streams the compressed audio data to the serial port. The example can be found in the board's built-in examples by navigating to **File > Examples > NDP > Record_and_stream**. 

Keep in mind that this example code requires the following libraries:

- [arduino-libg722](https://github.com/pschatzmann/arduino-libg722)
- [arduino-audio-tools __v0.9.6__](https://github.com/pschatzmann/arduino-audio-tools/releases/tag/v0.9.6)

***__Important:__ This code requires `arduino-audio-tools` version __v0.9.6__ to compile.***

Make sure that you have updated the NDP120 firmware. See the steps [here](#ndp120-processor-firmware-update).

```arduino
// Include necessary libraries for the Nicla Voice board, audio processing, and G722 codec support
#include "Arduino.h"
#include "NDP.h"

#undef abs
#define USE_INT24_FROM_INT
#include "AudioTools.h"
#include "AudioCodecs/CodecG722.h"

G722Encoder encoder;

uint8_t data[2048];

void ledGreenOn() {
  nicla::leds.begin();
  nicla::leds.setColor(green);
  delay(200);
  nicla::leds.setColor(off);
  nicla::leds.end();
}

void setup() {

  Serial.begin(115200);
  nicla::begin();
  nicla::disableLDO();
  nicla::leds.begin();

  NDP.onEvent(ledGreenOn);

  AudioBaseInfo bi;
  bi.channels = 1;
  bi.sample_rate = 16000;

  encoder.setOptions(0);
  encoder.begin(bi);

  encoder.setOutputStream(Serial);

  NDP.begin("mcu_fw_120_v91.synpkg");
  NDP.load("dsp_firmware_v91.synpkg");
  NDP.load("alexa_334_NDP120_B0_v11_v91.synpkg");
  NDP.turnOnMicrophone();
  int chunk_size = NDP.getAudioChunkSize();
  if (chunk_size >= sizeof(data)) {
    for(;;);
  }
}

void loop() {
  unsigned int len = 0;

  NDP.extractData(data, &len);
  encoder.write(data, len);
}
```

Here you can find a step-by-step explanation of the code:

First, the necessary libraries are included: 

- `Arduino.h` and `NDP.h` for the Nicla Voice board's basic functions and microphone control; `AudioTools.h` and `CodecG722.h` for audio processing and G722 codec support.
- An instance of the `G722Encoder` class is created to handle audio encoding.
- The `data` buffer is declared with a size of 2048 bytes to store audio data temporarily.

In the `setup()` function:

- The serial communication is initialized at a baud rate of 115200.
- The Nicla Voice board is initialized, and the LDO is disabled.
- The green LED is configured to turn on when an event occurs.
- The `G722Encoder` instance is set up with the proper audio parameters (1 channel, 16 kHz sample rate).
- The output stream for the encoder is set to the serial port.
- The NDP Processor is set up with the necessary firmware packages and the onboard microphone is turned on.
- The audio chunk size is checked to ensure it doesn't exceed the buffer size.

In the `loop()` function:

- Audio data is extracted from the NDP processor and stored in the `data` buffer.
- The length of the extracted audio data is stored in the `len` variable.
- The extracted audio data is passed to the G722 encoder, which compresses the audio and sends it to the serial port.

#### Linux Workflow

To extract the audio data on a **Linux computer**, follow the steps below:

- Set up the serial port as raw:

```bash
stty -F /dev/ttyACM0 115200 raw
```
- Dump the data to a file (e.g., test.g722):

```bash
cat /dev/ttyACM0 > test.g722
```
- Install **ffmpeg** with `sudo apt install ffmpeg` to convert the `.g722` file to `.wav`:

```bash
ffmpeg -f g722 -i test.g722 -ar 16000 test.wav
```
Then you can open the `.wav` file with software like [Audacity](https://www.audacityteam.org/) to play it back.


#### Windows Workflow

To extract the audio data on a **Windows computer**, follow the steps below:

Download **PuTTY** for free [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), install it and open it.

1. Select "Serial" as the connection type

2. Enter the serial port where your board is connected
3. Set the baud rate to `115200`
4. In the left menu, navigate to "Logging"
5. Select "All session output"
6. Define the directory to save the recorded file `.g722`
7. Click on "Open" to start recording audio

![PuTTY steps](assets/serial-g722.png)

- To stop recording, simply close the terminal window
- Navigate to your `.g722` file directory, and now it is time to convert it to `.wav`
- Download **FFmpeg** for Windows [here](https://www.gyan.dev/ffmpeg/builds/)
- From the Command Prompt (CMD), navigate to the download directory to use it, or add it to your system PATH
- Run the following command to convert the `.g722` file into `.wav`

  ```bash
  ffmpeg -f g722 -i <update-with-directory>\test.g722 -ar 16000 test.wav
  ```
Then, you can open the `.wav` file with software like [Audacity](https://www.audacityteam.org/) or any media player to play back the audio.



#### Machine Learning and Audio Analysis

You can use the Nicla Voice and the [Machine Learning Tools](https://cloud.arduino.cc/machine-learning-tools/) of the Arduino Cloud to create your own audio analysis Machine Learning models. Check out this [tutorial](https://docs.arduino.cc/tutorials/nicla-voice/getting-started-ml) and start with Machine Learning with the Nicla Voice. 

![Edge Impulse Studio for ML and AI](assets/edge-impulse.png)

Learn more about the Nicla Voice integration with Edge Impulse [here](https://docs.edgeimpulse.com/docs/edge-ai-hardware/mcu-+-ai-accelerators/arduino-nicla-voice).

### IMU

The Nicla Voice features an advanced IMU and a magnetometer, which allows the board to sense motion, orientation, and magnetic fields. The IMU on the Nicla Voice board is the BMI270 from Bosch®. It consists of a 3-axis accelerometer and a 3-axis gyroscope. They can provide information about the board's motion, orientation, and rotation in a 3D space. The BMI270 is designed for wearables and offers low power consumption and high performance, making it suitable for various applications, such as gesture recognition, motion tracking, or stabilization.

![Nicla Voice onboard IMU](assets/user-manual-11.png)

#### Accelerometer and Gyroscope Data

The example sketch below shows how to get acceleration (m/s<sup>2</sup>) and angular velocity (in °/s) data from the onboard IMU and streams it to the Arduino IDE Serial Monitor and Serial Plotter. The sketch needs the `BMI270_Init.h` header file to be in the same directory as the sketch. You can download the example sketch and the header files [here](assets/nv_acc_gyro_test.zip).

***For this example to work you must update the NDP processor, see the details on this [section](#ndp120-processor-firmware-update).***

```arduino
#include "NDP.h"
#include "BMI270_Init.h"

// Named constants
#define READ_START_ADDRESS 0x0C
#define READ_BYTE_COUNT 16
#define SENSOR_DATA_LENGTH 16

// Accelerometer range is set to +/-2g
// Raw accelerometer data is represented as a signed 16-bit integer
// Raw accelerometer data can be converted to acceleration in m/s^2 units using the following scale factor:
#define ACCEL_SCALE_FACTOR ((2.0 / 32767.0) * 9.8)

// Gyroscope has a sensitivity of 16.4 LSB/dps
#define GYRO_SCALE_FACTOR (1 / 16.4)

// Macros for checking the sensor status.
#define CHECK_STATUS(s) \
  do { \
    if (s) { \
      Serial.print("SPI access error in line "); \
      Serial.println(__LINE__); \
      for (;;) \
        ; \
    } \
  } while (0)

void setup() {
  int status;
  uint8_t __attribute__((aligned(4))) sensor_data[SENSOR_DATA_LENGTH];

  // Initiate Serial communication for debugging and monitoring.
  Serial.begin(115200);

  // Initialize Nicla Voice board's system functions.
  // Disable the LDO regulator on the Nicla Voice board for power saving.
  // Initialize the built-in RGB LED of the Nicla Voice board.
  nicla::begin();
  nicla::disableLDO();
  nicla::leds.begin();

  // NDP processor initialization with firmwares and models
  Serial.println("- NDP processor initialization...");
  NDP.begin("mcu_fw_120_v91.synpkg");
  NDP.load("dsp_firmware_v91.synpkg");
  Serial.println("- NDP processor initialization done!");

  // Set the BMI270 sensor in SPI mode, then read sensor data.
  status = NDP.sensorBMI270Read(0x0, 1, sensor_data);
  CHECK_STATUS(status);
  status = NDP.sensorBMI270Read(0x0, 1, sensor_data);
  CHECK_STATUS(status);

  // Perform a software reset of the sensor.
  status = NDP.sensorBMI270Write(0x7E, 0xB6);
  CHECK_STATUS(status);
  delay(20);

  // Set the sensor back to SPI mode after the software reset.
  status = NDP.sensorBMI270Read(0x0, 1, sensor_data);
  CHECK_STATUS(status);
  status = NDP.sensorBMI270Read(0x0, 1, sensor_data);
  CHECK_STATUS(status);

  // Disable power configurations.
  status = NDP.sensorBMI270Write(0x7C, 0x00);
  CHECK_STATUS(status);
  delay(20);

  // Prepare to load the sensor configuration.
  status = NDP.sensorBMI270Write(0x59, 0x00);
  CHECK_STATUS(status);

  // Sensor configuration.
  Serial.println("- BMI270 initialization starting...");
  status = NDP.sensorBMI270Write(0x5E, sizeof(bmi270_maximum_fifo_config_file), (uint8_t*)bmi270_maximum_fifo_config_file);
  CHECK_STATUS(status);
  Serial.println("- BMI270 Initialization done!");
  status = NDP.sensorBMI270Write(0x59, 0x01);
  CHECK_STATUS(status);
  delay(200);

  // Check sensor status.
  status = NDP.sensorBMI270Read(0x21, 1, sensor_data);
  CHECK_STATUS(status);

  // Configure the device to normal power mode with both accelerometer and gyroscope operational.
  // Set the accelerometer and gyroscope settings such as measurement range and data rate.
  status = NDP.sensorBMI270Write(0x7D, 0x0E);  // Normal power mode
  CHECK_STATUS(status);
  status = NDP.sensorBMI270Write(0x40, 0xA8);  // Accelerometer configuration.
  CHECK_STATUS(status);
  status = NDP.sensorBMI270Write(0x41, 0x00);  // Set the accelerometer range to +/- 2g.
  CHECK_STATUS(status);
  status = NDP.sensorBMI270Write(0x42, 0xA9);  // Gyroscope configuration.
  CHECK_STATUS(status);
  status = NDP.sensorBMI270Write(0x43, 0x00);  // Set the gyroscope range to +/- 2000 dps.
  CHECK_STATUS(status);
}

void loop() {
  // Allocate space for raw sensor data.
  uint8_t __attribute__((aligned(4))) sensor_data[SENSOR_DATA_LENGTH];

  // Declare variables for accelerometer and gyroscope data.
  int16_t x_acc_raw, y_acc_raw, z_acc_raw, x_gyr_raw, y_gyr_raw, z_gyr_raw;
  float x_acc, y_acc, z_acc, x_gyr, y_gyr, z_gyr;

  // Read operation status variable.
  int status;

  // Perform data read from the BMI270 sensor. The data read includes accelerometer and gyroscope data.
  // The sensor's read function is called with 0x0C as the start address and 16 as the number of bytes to read.
  // Collected data is placed into sensor_data array.
  status = NDP.sensorBMI270Read(READ_START_ADDRESS, READ_BYTE_COUNT, &sensor_data[0]);

  // Check the status of the read operation.
  CHECK_STATUS(status);

  // Parse the read sensor data. Data is in 16-bit format, where lower byte comes first (little endian).
  // Data for each axis (X, Y, Z) of the accelerometer and gyroscope is extracted from the array.
  x_acc_raw = (0x0000 | sensor_data[0] | sensor_data[1] << 8);
  y_acc_raw = (0x0000 | sensor_data[2] | sensor_data[3] << 8);
  z_acc_raw = (0x0000 | sensor_data[4] | sensor_data[5] << 8);
  x_gyr_raw = (0x0000 | sensor_data[6] | sensor_data[7] << 8);
  y_gyr_raw = (0x0000 | sensor_data[8] | sensor_data[9] << 8);
  z_gyr_raw = (0x0000 | sensor_data[10] | sensor_data[11] << 8);

  // Convert raw accelerometer data to acceleration expressed in m/s^2.
  x_acc = x_acc_raw * ACCEL_SCALE_FACTOR;
  y_acc = y_acc_raw * ACCEL_SCALE_FACTOR;
  z_acc = z_acc_raw * ACCEL_SCALE_FACTOR;

  // Convert raw gyroscope data to angular velocity expressed in °/s.
  x_gyr = x_gyr_raw * GYRO_SCALE_FACTOR;
  y_gyr = y_gyr_raw * GYRO_SCALE_FACTOR;
  z_gyr = z_gyr_raw * GYRO_SCALE_FACTOR;

  // Print accelerometer data (expressed in m/s^2).
  Serial.print("x_acc:");
  Serial.print(x_acc);
  Serial.print(",");
  Serial.print("y_acc:");
  Serial.print(y_acc);
  Serial.print(",");
  Serial.print("z_acc:");
  Serial.println(z_acc);

  // Print gyroscope data (expressed in °/s). 
  Serial.print("x_gyr:");
  Serial.print(x_gyr);
  Serial.print(",");
  Serial.print("y_gyr:");
  Serial.print(y_gyr);
  Serial.print(",");
  Serial.print("z_gyr:");
  Serial.println(z_gyr);

  delay(10);
}
```

Here you can find a step-by-step explanation of the code:

First, the necessary libraries are included: 

- `NDP.h` and `BMI270_Init.h` for the Nicla Voice board's basic functions and the IMU control.
- Macros are defined for checking the status of the IMU; these macros allow the sketch to detect and handle sensor errors. 

Next, in the `setup()` function:

- The serial communication is initialized at a baud rate of `115200`.
- The Nicla Voice board is initialized, and the LDO regulator (used for putting the board into power-saving mode) is disabled to avoid communication problems with the IMU. 
- Error and event handlers are initialized.
- NDP processor is initialized; this process includes populating the external Flash memory of the board with the NDP processor's internal microcontroller firmware (`mcu_fw_120_v91.synpkg`), and the NDP processor's internal DSP firmware (`dsp_firmware_v91.synpkg`).
- The BMI270 sensor is initialized; this includes a software reset, loading the sensor configuration, and setting it into normal power mode with the accelerometer and gyroscope operational. 

Finally, in the `loop()` function:

- Memory is allocated for the sensor data; data is then read from the sensor and stored in this allocated space.
- Raw sensor data is then parsed and extracted into raw accelerometer and gyroscope data. This data is represented as 16-bit signed integers ranging from -32768 to 32767.
- Raw sensor data is converted into understandable and standard unit measurements; for the accelerometer, data is converted to meters per second squared, and for the gyroscope, data is converted to degrees per second. 
- Converted accelerometer and gyroscope data are printed on the Serial Monitor, allowing the user to observe sensor data in real-time.

After uploading the example code, you should see accelerometer and gyroscope data on the IDE's Serial Monitor as shown below:

![Nicla Voice onboard IMU data on the IDE's Serial Monitor](assets/user-manual-13.png)

Let's use also the Arduino IDE Serial Plotter to test the example IMU sketch, open the IDE's Serial Plotter by navigating to **Tools > Serial Plotter**. After a while, you should see a real-time graph showing data from the board's onboard accelerometer and gyroscope, as shown below:

![Nicla Voice onboard IMU data on the IDE's Serial Plotter](assets/imu_gyro.gif)

When the board is not moving, you should see acceleration measurements close to zero on the x and y-axis, while the z-axis will be close to 1g (approximately 9.81 m/s<sup>2</sup>), the gyroscope measurements on the three-axis will stay close to zero.

#### IMU and Machine Learning

The example code below demonstrates how to use the Nicla Voice board to perform Machine Learning inference on IMU data. The code sets up event indicators using the onboard RGB LED and sends IMU data to the NDP processor for inference. The example can be found in the board's built-in examples by navigating to **File > Examples > NDP > IMUDemo**.


```arduino
#include "NDP.h"

// Set to 'true' for the lowest power consumption mode, 'false' otherwise
const bool lowestPower = false;

// Function to turn on the blue LED and print a label to the serial monitor if not in the lowest power mode
void ledBlueOn(char* label) {
  nicla::leds.begin();
  nicla::leds.setColor(blue);
  delay(200);
  nicla::leds.setColor(off);
  if (!lowestPower) {
    Serial.println(label);
  }
  nicla::leds.end();
}

// Function to turn on the green LED briefly
void ledGreenOn() {
  nicla::leds.begin();
  nicla::leds.setColor(green);
  delay(200);
  nicla::leds.setColor(off);
  nicla::leds.end();
}

// Function to make the red LED blink continuously
void ledRedBlink() {
  while (1) {
    nicla::leds.begin();
    nicla::leds.setColor(red);
    delay(200);
    nicla::leds.setColor(off);
    delay(200);
    nicla::leds.end();
  }
}

void setup() {
  Serial.begin(115200);
  nicla::begin();
  nicla::disableLDO();
  nicla::leds.begin();

  // Register event handlers for error, match, and event
  NDP.onError(ledRedBlink);
  NDP.onMatch(ledBlueOn);
  NDP.onEvent(ledGreenOn);

  // Load Edge Impulse model and related firmware
  Serial.println("Loading synpackages");
  NDP.begin("mcu_fw_120_v91.synpkg");
  NDP.load("dsp_firmware_v91.synpkg");
  NDP.load("ei_model_imu.synpkg");
  Serial.println("packages loaded");

  NDP.getInfo();
  NDP.configureInferenceThreshold(1088);
  NDP.interrupts();

  // Enter the lowest power mode, if set
  nicla::leds.end();
  if (lowestPower) {
    NRF_UART0->ENABLE = 0;
  }
}

// Predefined IMU data for testing
extern "C" const unsigned char data_opensset_bin[];
extern "C" const unsigned char data_circ_bin[];
extern "C" const unsigned int data_opensset_bin_len;
extern "C" const unsigned int data_circ_bin_len;

void loop() {
  // Send openset data (no match expected)
  Serial.println("Sending openset data... (no match expected)");
  NDP.sendData((uint8_t*)data_opensset_bin, data_opensset_bin_len);
  delay(1000);

  // Send circular IMU data (match expected)
  Serial.println("Sending circular IMU data.... (match expected)");
  NDP.sendData((uint8_t*)data_circ_bin, data_circ_bin_len);
  delay(5000);
}
```

In the example code above, a Machine Learning model is loaded into the Nicla Voice board, and predefined IMU data is sent to the Machine Learning model for inferencing. Depending on the result, the board will light its built-in RGB LED with different colors:

- If the model matches the input data with a known motion pattern, the built-in RGB LED is turned blue, and the event label is printed to the IDE's Serial Monitor.
- If an error occurs, the built-in RGB LED will blink red continuously. 
- While an event is recognized, the built-in RGB LED is turned on green.

To learn more about your Nicla Voice board Machine Learning capabilities, check out the following tutorial and learn how to create a simple motion detection application: 

- [Motion Detection with Nicla Voice and Machine Learning Tools](https://docs.arduino.cc/tutorials/nicla-voice/motion-detection-ml)

### Magnetometer

The onboard magnetometer of the Nicla Voice can be used to determine the board's orientation relative to Earth's magnetic field, which is helpful for compass applications, navigation, or detecting the presence of nearby magnetic objects. The magnetometer on the Nicla Voice board is the BMM150, also from Bosch®. It is a 3-axis sensor that measures the strength and direction of magnetic fields surrounding the board.

![Nicla Voice onboard magnetometer](assets/user-manual-12.png)

#### Magnetometer Data

The example code below shows how to get raw magnetic field and Hall resistance data from the onboard magnetometer and stream it to the Arduino IDE Serial Monitor and Serial Plotter. You can download the example sketch [here](assets/nv_mag_test.rar).

```arduino
#include "NDP.h"

// Named constants
#define READ_START_ADDRESS 0x42
#define READ_BYTE_COUNT 8
#define SENSOR_DATA_LENGTH 16

/**
  Blinks onboard red LED periodically every 200 ms.
*/
void ledRedBlink() {
  while (1) {
    nicla::leds.begin();
    nicla::leds.setColor(red);
    delay(200);
    nicla::leds.setColor(off);
    delay(200);
    nicla::leds.end();
  }
}

// Macro definition used for checking the sensor status, print error if SPI access fails.
#define CHECK_STATUS(s) \
  do { \
    if (s) { \
      Serial.print("SPI access error in line "); \
      Serial.println(__LINE__); \
      for (;;) \
        ; \
    } \
  } while (0)

void setup() {
  int status;
  uint8_t __attribute__((aligned(4))) sensor_data[SENSOR_DATA_LENGTH];

  // Initiate Serial communication for debugging and monitoring.
  Serial.begin(115200);

  // Initialize Nicla Voice board's system functions.
  // Disable the LDO regulator on the Nicla Voice board for power saving.
  // Initialize the built-in RGB LED of the Nicla Voice board.
  nicla::begin();
  nicla::disableLDO();
  nicla::leds.begin();

  // Set up error and event handlers:
  // - In case of error, the red LED will blink.

  NDP.onError(ledRedBlink);

  // NDP processor initialization with firmwares and models.
  Serial.println("- NDP processor initialization...");
  NDP.begin("mcu_fw_120_v91.synpkg");
  NDP.load("dsp_firmware_v91.synpkg");
  Serial.println("- NDP processor initialization done!");

  // Enable power control bit
  status = NDP.sensorBMM150Write(0x4B, 0x01);
  CHECK_STATUS(status);
  delay(20);

  // Read power control byte
  status = NDP.sensorBMM150Read(0x4B, 1, sensor_data);
  CHECK_STATUS(status);

  // Set the magnetometer to active mode (normal operation), with an output data rate of 10 Hz.
  status = NDP.sensorBMM150Write(0x4C, 0x00);
  CHECK_STATUS(status);

  // Read chip ID
  status = NDP.sensorBMM150Read(0x40, 1, sensor_data);
  CHECK_STATUS(status);
}

void loop() {
  // Allocate space for raw sensor data.
  uint8_t __attribute__((aligned(4))) sensor_data[SENSOR_DATA_LENGTH];

  // Declare variables for magnetometer data.
  int16_t x_mag_raw, y_mag_raw, z_mag_raw, hall_raw;
  float x_mag, y_mag, z_mag;

  // Read operation status variable.
  int status;

  // Perform data read from the BMM150 sensor.
  // The sensor's read function is called with 0x42 as the start address and 8 as the number of bytes to read.
  // Collected data is placed into sensor_data array.
  status = NDP.sensorBMM150Read(READ_START_ADDRESS, READ_BYTE_COUNT, sensor_data);

  // Check the status of the read operation.
  CHECK_STATUS(status);

  // The sensor data is read into an array of bytes (8-bit values). Each measurement from the magnetometer consists
  // of two bytes, hence the bit shifting and bitwise OR operations to combine these two bytes into one 16-bit value.
  // Data for each axis (X, Y, Z) of the magnetometer is extracted from the array.

  x_mag_raw = (0x0000 | sensor_data[0] >> 3 | sensor_data[1] << 5);
  y_mag_raw = (0x0000 | sensor_data[2] >> 3 | sensor_data[3] << 5);
  z_mag_raw = (0x0000 | sensor_data[4] >> 1 | sensor_data[5] << 7);
  hall_raw  = (0x0000 | sensor_data[6] >> 2 | sensor_data[7] << 6);

  // Print raw magnetometer data.
  Serial.print("x_mag_raw:");
  Serial.print(x_mag_raw);
  Serial.print(",");
  Serial.print("y_mag_raw:");
  Serial.print(y_mag_raw);
  Serial.print(",");
  Serial.print("z_mag_raw:");
  Serial.print(z_mag_raw);
  Serial.print(",");
  Serial.print("hall_raw:");
  Serial.println(hall_raw);

  delay(100);
}
```

Here you can find a step-by-step explanation of the sketch:

First, the necessary libraries are included: 

- `NDP.h` for the Nicla Voice board's basic functions and the magnetometer control.
- Macros are defined for checking the status of the magnetometer; these macros allow the sketch to detect and handle sensor errors. 

Next, user function `ledRedBlink()` definition: 

- These functions allow the onboard LEDs to flash red to indicate an error.

Next, in the `setup()` function:

- The serial communication is initialized at a baud rate of 115200.
- The Nicla Voice board is initialized, and the LDO regulator (used for putting the board into power-saving mode) is disabled to avoid communication problems with the magnetometer. 
- Error and event handlers are initialized.
- NDP processor is initialized; this process includes populating the external Flash memory of the board with the NDP processor's internal microcontroller firmware (`mcu_fw_120_v91.synpkg`) and the NDP processor's internal DSP firmware (`dsp_firmware_v91.synpkg`).
- The BMM150 sensor is initialized; this includes setting it into normal operation with an output data rate (ODR) of 10 Hz. 

Finally, in the `loop()` function:

- Memory is allocated for the sensor data; data is then read from the sensor and stored in this allocated space.
- Raw sensor data is then extracted and parsed into raw magnetometer data. Raw sensor data is extracted from the `sensor_data` array, 8-bits at a time, and then combined to form a 16-bit integer for each axis (X, Y, Z) and raw Hall resistance value. 
- Raw magnetometer data is printed on the Serial Monitor, allowing the user to observe sensor data in real-time.

After uploading the example code, you should see the magnetometer data on the IDE's Serial Monitor, as shown below:

![Nicla Voice onboard raw magnetometer data on the IDE's Serial Monitor](assets/user-manual-15.png)

Now open the IDE's Serial Plotter by navigating to **Tools > Serial Plotter**. After a while, you should see a real-time graph showing raw data from the board's onboard magnetometer, as shown below (move the board):

![Nicla Voice onboard raw magnetometer data on the IDE's Serial Plotter](assets/user-manual-16.gif)

## Actuators

### RGB LED

The Nicla Voice features a built-in I2C RGB LED that can be a visual feedback indicator for the user. The LED is connected through the boards' I2C port; therefore, specific functions must be used to operate the LED colors. 

![Nicla Voice built-in RGB LED](assets/user-manual-7.png)

To use the RGB LED, include the `Nicla System` header:

```arduino
// Include the Nicla System header to access the built-in RGB LED functions
#include "Nicla_System.h" 
```

Since the functions are scoped under a class name called `nicla`, you must explicitly write it before each statement. To initialize the board's built-in RGB LED along with the Nicla system inside the void `setup()` function:

```arduino
void setup() {
  // Initialize the Nicla system and the built-in RGB LED
  nicla::begin();
  nicla::leds.begin();
}
```

The built-in RGB LED can be set to a desired color using the RGB color model in which the red, green, and blue primary colors of light are added together in various ways to reproduce a broad array of colors. There are predefined colors: `red`, `green`, `blue`, `yellow`, `magenta`, and `cyan`; to turn off the LED, use `off`. To set the built-in RBG LED to a predefined color, for example, green or blue:

```arduino
// Set the LED color to green, wait for 1000 milliseconds
nicla::leds.setColor(green);
delay(1000);

// Set the LED color to blue, wait for 1000 milliseconds
nicla::leds.setColor(blue);
delay(1000);  
```

To turn off the built-in RGB LED:

```arduino
// Turn off the LED
nicla::leds.setColor(off);
```

You can also choose a value between 0 and 255 for each color component (red, green, or blue) to set a custom color:


```arduino
// Define custom color values for red, green, and blue components
int red = 234;
int green = 72;
int blue = 122;

// Set the LED to the custom color, wait for 1000 milliseconds
nicla::leds.setColor(red, green, blue);
delay(1000);

// Turn off the LED and wait, wait for 1000 milliseconds
nicla::leds.setColor(off);
delay(1000); 
```
Here you can find a complete example code to blink the built-in I2C RGB LED of the Nicla Voice:


```arduino
// Include the Nicla System header to access the built-in RGB LED functions
#include "Nicla_System.h"

void setup() {
  // Initialize the Nicla system and the built-in RGB LED
  nicla::begin();
  nicla::leds.begin();  
}

void loop() {
  // Set the LED color to red, wait for 1000 milliseconds
  nicla::leds.setColor(red);
  delay(1000);

  // Turn off the LED and wait, wait for 1000 milliseconds
  nicla::leds.setColor(off);
  delay(1000); 
}
```

## Communication

This section of the user manual covers the different communication protocols that are supported by the Nicla Voice board, including the Serial Peripheral Interface (SPI), Inter-Integrated Circuit (I2C), Universal Asynchronous Receiver-Transmitter (UART), and Bluetooth® Low Energy; communication via the onboard ESLOV connector is also explained in this section. The Nicla Voice features dedicated pins for each communication protocol, making connecting and communicating with different components, peripherals, and sensors easy.

### SPI

The Nicla Voice supports SPI communication, which allows data transmission between the board and other SPI-compatible devices. The pins used in the Nicla Voice for the SPI communication protocol are the following:

| **Microcontroller Pin** | **Arduino Pin Mapping** |
|:-----------------------:|:-----------------------:|
|       `CS`/`P0_29`      |       `SS` or `6`       |
|      `COPI`/`P0_27`     |       `SCK` or `8`      |
|      `CIPO`/`P0_28`     |      `MOSI` or `7`      |
|      `SCLK`/`P0_11`     |      `MISO` or `9`      |

Please, refer to the [board pinout section](#pins) of the user manual to find them on the board.

Include the `SPI` library at the top of your sketch to use the SPI communication protocol. The SPI library provides functions for SPI communication:

```arduino
#include <SPI.h>
```

In the `setup()` function, initialize the SPI library, define and configure the chip select (`CS`) pin:

```arduino
void setup() {
  // Set the chip select pin as output
  pinMode(SS, OUTPUT); 

  // Pull the CS pin HIGH to unselect the device
  digitalWrite(SS, HIGH); 
  
  // Initialize the SPI communication
  SPI.begin();
}
```

To transmit data to an SPI-compatible device, you can use the following commands:

```arduino
// Replace with the target device's address
byte address = 0x00; 

// Replace with the value to send
byte value = 0xFF; 

// Pull the CS pin LOW to select the device
digitalWrite(SS, LOW); 

// Send the address
SPI.transfer(address); 

// Send the value
SPI.transfer(value); 

// Pull the CS pin HIGH to unselect the device
digitalWrite(SS, HIGH); 
```

### I2C

The Nicla Voice supports I2C communication, which allows data transmission between the board and other I2C-compatible devices. The pins used in the Nicla Voice for the I2C communication protocol are the following:

| **Microcontroller Pin** | **Arduino Pin Mapping** |
| :---------------------: | :---------------------: |
|         `P0_23`         |    `I2C_SCL` or `3`     |
|         `P0_22`         |    `I2C_SDA` or `4`     |

Please, refer to the [board pinout section](#pins) of the user manual to find them on the board. The I2C pins are also available through the onboard ESLOV connector of the Nicla Voice.

To use I2C communication, include the `Wire` library at the top of your sketch. The `Wire` library provides functions for I2C communication:

```arduino
#include <Wire.h>
```

In the `setup()` function, initialize the I2C library:

```arduino
 // Initialize the I2C communication
Wire.begin();
```

To transmit data to an I2C-compatible device, you can use the following commands:

```arduino
// Replace with the target device's I2C address
byte deviceAddress = 0x1; 

// Replace with the appropriate instruction byte
byte instruction = 0x00; 

// Replace with the value to send
byte value = 0xFF; 

// Begin transmission to the target device
Wire.beginTransmission(deviceAddress); 

// Send the instruction byte
Wire.write(instruction); 

// Send the value
Wire.write(value); 

// End transmission
Wire.endTransmission(); 
```

To read data from an I2C-compatible device, you can use the `requestFrom()` function to request data from the device and the `read()` function to read the received bytes:

```arduino
// The target device's I2C address
byte deviceAddress = 0x1; 

// The number of bytes to read
int numBytes = 2; 

// Request data from the target device
Wire.requestFrom(deviceAddress, numBytes);

// Read while there is data available
while (Wire.available()) {
  byte data = Wire.read(); 
}
```

### UART

The pins used in the Nicla Voice for the UART communication protocol are the following:

| **Microcontroller Pin** | **Arduino Pin Mapping** |
| :---------------------: | :---------------------: |
|         `P0_09`         |   `SERIAL1_TX` or `1`   |
|         `P0_20`         |   `SERIAL1_RX` or `2`   |

Please, refer to the [board pinout section](#board-pinout) of the user manual to find them on the board.

To begin with UART communication, you'll need to configure it first. In the `setup()` function, set the baud rate (bits per second) for UART communication:

```arduino
// Start UART communication at 9600 baud
Serial1.begin(9600); 
```

To read incoming data, you can use a `while()` loop to continuously check for available data and read individual characters. The code shown above stores the incoming characters in a String variable and process the data when a line-ending character is received:

```arduino
// Variable for storing incoming data
String incoming = ""; 

void loop() {
  // Check for available data and read individual characters
  while (Serial1.available()) {
    // Allow data buffering and read a single character
    delay(2); 
    char c = Serial1.read();
    
    // Check if the character is a newline (line-ending)
    if (c == '\n') {
      // Process the received data
      processData(incoming);

      // Clear the incoming data string for the next message
      incoming = ""; 
    } else {
      // Add the character to the incoming data string
      incoming += c; 
    }
  }
}
```

To transmit data to another device via UART, you can use the `write()` function:

```arduino
// Transmit the string "Hello world!
Serial1.write("Hello world!");
```

You can also use the `print` and `println()` to send a string without a newline character or followed by a newline character:

```arduino
// Transmit the string "Hello world!" 
Serial1.print("Hello world!");

// Transmit the string "Hello world!" followed by a newline character
Serial1.println("Hello world!");
```

### Bluetooth® Low Energy

To enable Bluetooth® Low Energy communication on the Nicla Voice, you can use the [ArduinoBLE library](https://www.arduino.cc/reference/en/libraries/arduinoble/).

Here is an example of how to use the ArduinoBLE library to create a voltage level monitor application:

```arduino
#include "Nicla_System.h"
#include <ArduinoBLE.h>


// Define the voltage service and its characteristic
BLEService voltageService("1101");
BLEUnsignedCharCharacteristic voltageLevelChar("2101", BLERead | BLENotify);


const int analogPin = A0;


/**
 Read voltage level from an analog input of the Nicla Voice,
 then maps the voltage reading to a percentage value ranging from 0 to 100.


 @param none
 @return the voltage level percentage (int).
*/
int readVoltageLevel() {
 int voltage = analogRead(analogPin);
 int voltageLevel = map(voltage, 0, 1023, 0, 100);
 return voltageLevel;
}


void setup() {
 // Initialize the Nicla system and the built-in RGB LED
 nicla::begin();
 nicla::leds.begin();


 Serial.begin(9600);
 // Wait for the serial connection to be established
 while (!Serial)
   ;


 // Initialize the BLE module
 if (!BLE.begin()) {
   Serial.println("starting BLE failed!");
   while (1)
     ;
 }


 // Set the local name and advertised service for the BLE module
 BLE.setLocalName("VoltageMonitor");
 BLE.setAdvertisedService(voltageService);
 voltageService.addCharacteristic(voltageLevelChar);
 BLE.addService(voltageService);


 // Start advertising the BLE service
 BLE.advertise();
 Serial.println("- Bluetooth device active, waiting for connections...");
}


void loop() {
 // Check for incoming BLE connections
 BLEDevice central = BLE.central();


 // If a central device is connected
 if (central) {
   Serial.print("- Connected to central: ");
   Serial.println(central.address());


   // Turn off the LED when disconnected
   nicla::leds.setColor(blue);


   // While the central device is connected
   while (central.connected()) {
     // Read the voltage level and update the BLE characteristic with the level value
     int voltageLevel = readVoltageLevel();


     Serial.print("- Voltage level is: ");
     Serial.println(voltageLevel);
     voltageLevelChar.writeValue(voltageLevel);


     delay(200);
   }
 }


 // Turn off the LED when disconnected
 nicla::leds.setColor(red);


 Serial.print("- Disconnected from central: ");
 Serial.println(central.address());
}
```

The example code shown above creates a Bluetooth® Low Energy service and characteristic for transmitting a voltage value read by the analog pin A0 of the Nicla Voice to a central device Bluetooth® device like a smartphone or another microcontroller.

- The code begins by importing all the necessary libraries and defining the Bluetooth® Low Energy service and characteristics.
- In the `setup()` function, the code initializes the Nicla Voice board and sets up the Bluetooth® Low Energy service and characteristic; then, it begins advertising the defined Bluetooth® Low Energy service.
- A Bluetooth® Low Energy connection is constantly verified in the `loop()` function, being the built-in LED in red while looking for a connection. When a central device connects to the Nicla Voice, its built-in LED will change its color to blue. The code then enters into a loop that constantly reads the voltage level from an analog input and maps it to a percentage value between 0 and 100. The voltage level is printed to the Serial Monitor and transmitted to the central device over the defined Bluetooth® Low Energy characteristic.

You can use the [nRF Connect for Mobile](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-mobile) app from Nordic Semiconductor to test the functionality of the example code shown below. nRF Connect is a powerful tool that allows you to scan and explore Bluetooth® Low Energy devices and communicate with them.


![Bluetooth® Low Energy service and characteristic information from a Nicla Voice device](assets/user-manual-bt.png)


### ESLOV Connector 

The Nicla Voice board features an onboard ESLOV connector meant as an **extension** of the I2C communication bus. This connector simplifies connecting various sensors, actuators, and other modules to the Nicla Voice without soldering or wiring.

![Nicla Voice built-in ESLOV connector](assets/user-manual-8.png)


 The ESLOV connector is a small 5-pin connector with a 1.00 mm pitch; the mechanical details of the connector can be found in the connector's datasheet.

The pin layout of the ESLOV connector is the following:

1. VCC_IN (5V input)
2. INT
3. SCL
4. SDA
5. GND

The manufacturer part number of the ESLOV connector is SM05B-SRSS and its matching receptacle manufacturer part number is SHR-05V-S-B. 

## Support

If you encounter any issues or have questions while working with the Nicla Voice, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our [Help Center](https://support.arduino.cc/hc/en-us), which offers a comprehensive collection of articles and guides for the Nicla Voice. The Arduino Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Nicla Family help center page](https://support.arduino.cc/hc/en-us/sections/4410176504978-Nicla-Family)

### Forum

Join our community forum to connect with other Nicla Voice users, share your experiences, and ask questions. The forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Nicla Voice.

- [Nicla Voice category in the Arduino Forum](https://forum.arduino.cc/c/hardware/nicla-family/nicla-voice/180)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Nicla Voice.

- [Contact us page](https://www.arduino.cc/en/contact-us/) 
