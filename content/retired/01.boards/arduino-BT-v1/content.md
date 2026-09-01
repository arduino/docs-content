---
title: "Arduino BT v1"
source: "https://arduino.cc/en/Main/ArduinoBoardBluetoothNew"
---

## Arduino BT (Bluetooth®)

![](assets/ArduinoBT400.jpg)

### Overview

The Arduino BT (Bluetooth®) is a microcontroller board based on the ATmega168 ([datasheet](/resources/datasheets/Datasheet-ATmega48-88-168-doc2545.pdf)) and the Bluegiga WT11 Bluetooth® module [datasheet](/resources/datasheets/WT11_Datasheet.pdf) \[pdf\]). It has 14 digital input/output pins (of which 6 can be used as PWM outputs and one can be used to reset the WT11 module), 6 analog inputs, a 16 MHz crystal oscillator, screw terminals for power, an ICSP header, and a reset button. It contains everything needed to support the microcontroller and can be programmed wirelessly over the Bluetooth® connection. Instructions are available for [getting started with the Arduino BT](//www.arduino.cc/en/Guide/ArduinoBT).


### Summary

|||
|-|-|
|Microcontroller|ATmega168|
|Operating Voltage|5V|
|Input Voltage|1.2-5.5 V|
|Digital I/O Pins|14 (of which 6 provide PWM output)|
|Analog Input Pins|6|
|DC Current per I/O Pin|40 mA|
|DC Current for 3.3V Pin|50 mA|
|Flash Memory|16 KB (of which 2 KB used by bootloader)|
|SRAM|1 KB|
|EEPROM|512 bytes|
|Clock Speed|16 MHz|

### Schematic & Reference Design

Reference Design: [arduino-bt-reference-design.zip](//www.arduino.cc/en/uploads/Main/arduino-bt-reference-design.zip)   
Schematic: [arduino\_bt06.pdf](//www.arduino.cc/en/uploads/Main/arduino%5Fbt06.pdf) 

### Power

The Arduino BT can be powered via the V+ and GND screw terminals. The board contains a DC-DC convector that allows it to be powered with as little as 1.2V, but a maximum of 5.5V. **Higher voltages or reversed polarity in the power supply can damage or destroy the board.** 

The power pins are as follows:

* **9V.** The input voltage to the Arduino board (i.e. the same as the V+ screw terminal). You can supply voltage through this pin, or, if supplying voltage via the screw terminals, access it through this pin. **Warning: despite the label, do not attach 9V to this pin. It will damage the board.**
* **5V.** The regulated power supply used to power the microcontroller and other components on the board. This can come either from V+ via the on-board DC-DC converter, or be supplied by a regulated 5V supply.
* **GND.** Ground pins.

### Memory

The ATmega168 has 16 KB of flash memory for storing code (of which 2 KB is used for the bootloader). It has 1 KB of SRAM and 512 bytes of EEPROM (which can be read and written with the [EEPROM library](http://www.arduino.cc/en/Reference/EEPROM)).

### Input and Output

Each of the 14 digital pins on the BT can be used as an input or output, using [pinMode()](//www.arduino.cc/en/Reference/PinMode), [digitalWrite()](//www.arduino.cc/en/Reference/DigitalWrite), and [digitalRead()](//www.arduino.cc/en/Reference/DigitalRead) functions. They operate at 5 volts. Each pin can provide or receive a maximum of 40 mA and has an internal pull-up resistor (disconnected by default) of 20-50 kOhms. In addition, some pins have specialized functions:

* **Serial: 0 (RX) and 1 (TX).** Used to receive (RX) and transmit (TX) TTL serial data. These pins are connected to the corresponding pins of the Bluegiga WT11 module.
* **External Interrupts: 2 and 3.** These pins can be configured to trigger an interrupt on a low value, a rising or falling edge, or a change in value. See the [attachInterrupt()](//www.arduino.cc/en/Reference/AttachInterrupt) function for details.
* **PWM: 3, 5, 6, 9, 10, and 11.** Provide 8-bit PWM output with the [analogWrite()](//www.arduino.cc/en/Reference/AnalogWrite) function.
* **SPI: 10 (SS), 11 (MOSI), 12 (MISO), 13 (SCK).** These pins support SPI communication, which, although provided by the underlying hardware, is not currently included in the Arduino language.
* **BT Reset: 7.** Connected to the reset line of the Bluegiga WT11 module, which is active high.
* **LED: 13.** There is a built-in LED connected to digital pin 13\. When the pin is HIGH value, the LED is on, when the pin is LOW, it's off.

The BT has 6 analog inputs, each of which provide 10 bits of resolution (i.e. 1024 different values). By default they measure from ground to 5 volts, though is it possible to change the upper end of their range using the AREF pin and some low-level code. Additionally, some pins have specialized functionality:

* **I2C: 4 (SDA) and 5 (SCL).** Support I2C (TWI) communication using the [Wire library](http://wiring.org.co/reference/libraries/Wire/index.html) (documentation on the Wiring website).

There are a couple of other pins on the board:

* **AREF.** Reference voltage for the analog inputs. Used with [analogReference](//www.arduino.cc/en/Reference/AnalogReference)().

See also the [mapping between Arduino pins and ATmega168 ports](https://docs.arduino.cc/hacking/hardware/PinMapping168).

### Bluetooth® Communication

The Bluegiga WT11 module on the Arduino BT provides Bluetooth® communication with computers, phones, and other Bluetooth® devices. The WT11 communicates with the ATmega168 via serial (shared with the RX and TX pins on the board). It comes configured for 115200 baud communication. The module should be configurable and detectable by your operating system's Bluetooth® drivers, which should then provide a virtual com port for use by other applications. The Arduino software includes a serial monitor which allows simple textual data to be sent to and from the Arduino board over this Bluetooth® connection. The board can also be reprogrammed using this same wireless connection.

The WT11 is specially configured for use in the Arduino BT. Its name is set to ARDUINOBT and passcode to 12345\. For details, see the complete initialization sketch below.

### Communication

The Arduino BT has a number of other facilities for communicating. The ATmega168's UART TTL (5V) serial communication is available on digital pins 0 (RX) and 1 (TX) as well as being connected to the WT11 module.

A [SoftwareSerial library](http://www.arduino.cc/en/Reference/SoftwareSerial) allows for serial communication on any of the BT's digital pins.

The ATmega168 also supports I2C (TWI) and SPI communication. The Arduino software includes a Wire library to simplify use of the I2C bus; see the [documentation on the Wiring website](http://wiring.org.co/reference/libraries/Wire/index.html) for details. To use the SPI communication, please see the ATmega168 datasheet.

### Programming

The Arduino BT can be programmed with the Arduino software ([download](//www.arduino.cc/en/Main/Software)). For details, see the [reference](//www.arduino.cc/en/Reference/HomePage) and [tutorials]((https://docs.arduino.cc/tutorials/).

The ATmega168 on the Arduino BT comes preburned with a [bootloader](https://docs.arduino.cc/hacking/software/Bootloader) that allows you to upload new code to it without the use of an external hardware programmer. It communicates using the original STK500 protocol ([reference](/resources/datasheets/doc2525.pdf), [C header files](/resources/datasheets/assets/avr061.zip)).

You can also bypass the bootloader and program the ATmega168 through the ICSP (In-Circuit Serial Programming) header; see [these instructions](https://docs.arduino.cc/hacking/software/Programmer) for details.

### Physical Characteristics

The maximum length and width of the BT are approximately 3.2 and 2.1 inches respectively. Three screw holes allow the board to be attached to a surface or case. Note that the distance between digital pins 7 and 8 is 160 mil (0.16"), not an even multiple of the 100 mil spacing of the other pins.

---

## Arduino BT v1 Initialization Sketch

This sketch is run once on each Arduino BT v1 to initialize the Bluetooth® module before the board is shipped (you shouldn't need to run this code; it's just here for reference). For details on the commands sent to the module, see the [iWrap data sheet](/resources/datasheets/UG218.pdf).

```arduino
/* BT test 01
* ------------------
* Massimo Banzi
*
*/

int LED = 13;   // select the pin for the LED
int RESET = 7;

void setup() {
  pinMode(LED,OUTPUT);   // declare the LED's pin as output
  pinMode(RESET,OUTPUT);   // declare the LED's pin as output
  Serial.begin(115200);        // connect to the serial port
  digitalWrite(RESET, HIGH);
  delay(10);
  digitalWrite(RESET, LOW);
  delay(2000);
  Serial.println("SET BT PAGEMODE 3 2000 1");
  Serial.println("SET BT NAME ARDUINOBT");
  Serial.println("SET BT ROLE 0 f 7d00");
  Serial.println("SET CONTROL ECHO 0");
  Serial.println("SET BT AUTH * 12345");
  Serial.println("SET CONTROL ESCAPE - 00 1");
  Serial.println("SET CONTROL BAUD 115200,8n1");      //first release 19200
}

void loop () {
  digitalWrite(LED, HIGH);
  delay(100);
  digitalWrite(LED, LOW);
  Serial.println("ciao");
  delay(1000);
}
```
