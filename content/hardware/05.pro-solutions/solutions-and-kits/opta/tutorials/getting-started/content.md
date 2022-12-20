---
title: 'Getting Started With the Opta'
description: 'Get started with the Opta and get to know some of its features.'
difficulty: beginner
tags:
  - Getting started
  - Relays
  - Analog Input
author: 'Benjamin Dannegård'
software:
  - ide-v1
  - ide-v2
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/opta
---

## Overview

Opta is a robust micro PLC solution with many engaging features. In this tutorial we will go through how the setup of Opta with the Arduino IDE and explain how to use its basic features, showing through examples how to program the LEDs on the device, how to use the programmable button, as well as using inputs and outputs.

## Goals

- Putting Opta to work with the Arduino IDE
- Blinking the LEDs on the device
- Programming the button on the device
- Testing the inputs and outputs on the device
- Connecting the device to the cloud

### Required Hardware and Software

- USB-C® cable (either USB-C to USB-A or USB-C to USB-C)
- [Arduino Opta](https://store.arduino.cc/pages/opta)
- [Arduino IDE](https://www.arduino.cc/en/software)
- 12-24V DC, 1A Power supply (optional if not running the section related to the relays)
- Analog inputs (optional, alternatively the section related to analog inputs will work but reading random values)

## Instructions

### Setup with the Arduino IDE

Make sure the latest version of the Arduino IDE is installed. The IDE can be downloaded [here](https://www.arduino.cc/en/software). 
Within the Arduino IDE install the core for the Opta. Go to **Tools > Board > Boards Manager**, in the boards manager search for **Opta mbed** and install it.

![Finding the Core in the Arduino IDE 2.0](assets/opta-core-install.png)

Now you are ready to upload sketches to the Opta via the Arduino IDE.

### Trying a Blink Sketch

When the IDE and the core are installed, let's warm up by uploading a first sketch to your Opta. We will be using a classic version of the Arduino blink sketch to put your device to work and test everything is set properly. 
Let's create a simple blink sketch that will blink the four STATUS LEDs on the Opta, highlighted in the image below.
All the STATUS LEDs on the device are defined in the core. 
Hereafter you can see the correspondence between each of them as identified on the front panel and their definition in the core:

LED_D0 --> STATUS 1

LED_D1 --> STATUS 2

LED_D2 --> STATUS 3

LED_D3 --> STATUS 4

LED_RESET --> LED above the reset button

LED_USER --> LED above the user button (only available on Opta WiFi (AFX00002))

Select the correct **board** and **port** in the **Tools** section.
Copy the sketch below into the Arduino IDE sketch editor, then upload it to Opta. 
When the sketch is uploaded you will see the Opta's STATUS LEDs blinking in sequence. 

```arduino
void setup() {
  pinMode(LED_D0, OUTPUT);
  pinMode(LED_D1, OUTPUT);
  pinMode(LED_D2, OUTPUT);
  pinMode(LED_D3, OUTPUT);
}

void loop() {
  digitalWrite(LED_D0, HIGH);
  delay(100);
  digitalWrite(LED_D0, LOW);
  delay(100);
  digitalWrite(LED_D1, HIGH);
  delay(100);
  digitalWrite(LED_D1, LOW);
  delay(100);
  digitalWrite(LED_D2, HIGH);
  delay(100);
  digitalWrite(LED_D2, LOW);
  delay(100);
  digitalWrite(LED_D3, HIGH);
  delay(100);
  digitalWrite(LED_D3, LOW);
  delay(500);  
}
```

![The blinking LEDs on the Opta](assets/opta-device-LED.png)

### Configuring the Programmable Button on the Opta

Opta has a programmable button, shown on the image below and identified as USER. It can be programmed using the Arduino IDE to fit your needs.  
To show how much simple is to use it, let's create a sketch and program the button as a trigger to modify the status of the STATUS LEDs. 
The button is defined in the core as `BTN_USER`: 'HIGH' as default (not pressed), 'LOW' when pressed. 
The new sketch will turn on more of the LEDs when the button is pressed, and then start over when all the lights have been turned on.
Below you can find the entire sketch, where a simple [Switch (case) Statement](https://www.arduino.cc/reference/en/language/structure/control-structure/switchcase/) is used, and an image highlighting where the USER button is located on the device. 

```arduino
int buttonState = 0;
int counter = 0;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_D0, OUTPUT);
  pinMode(LED_D1, OUTPUT);
  pinMode(LED_D2, OUTPUT);
  pinMode(LED_D3, OUTPUT);
  pinMode(BTN_USER, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  buttonState = digitalRead(BTN_USER);
  if(buttonState == LOW){
    if(counter < 4){
      counter++;
    }
    else{
      counter = 0;
    }
    delay(100);
  }
  changeLights();
}

void changeLights() {
  switch(counter){
    case 0:
      digitalWrite(LED_D0, LOW);
      digitalWrite(LED_D1, LOW);
      digitalWrite(LED_D2, LOW);
      digitalWrite(LED_D3, LOW);
      break;
    case 1:
      digitalWrite(LED_D0, HIGH);
      break;
    case 2:
      digitalWrite(LED_D1, HIGH);
      break;
    case 3:
      digitalWrite(LED_D2, HIGH);
      break;
    case 4:
      digitalWrite(LED_D3, HIGH);
      break;
  }
  delay(100);
}
```

![The button and LEDs that will light up on the Opta](assets/opta-device-button.png)

Now the more lights should turn on when the button is pressed, the rest turn on in sequence as the button is pressed. This is the sequence the lights should follow:

First press --> LED 1 ON.

Second press --> LEDs 1 and 2 ON.

Third press --> LEDS 1, 2 and 3 ON.

Fourth press --> LEDS 1, 2, 3 and 4 ON. 

Fifth press --> All leds off and back.


### Using Out Relays

Opta has 4 outputs, consisting of 4 electromechanical relays NO (SPST) with a capacity of 10 A at 250 V AC (considering a resistive load). They are identified as OUTPUTS and located on the bottom of Opta as shown in the image. They correspond to pins D0 to D3 as follows:

OUTPUT 1 --> D0

OUTPUT 2 --> D1

OUTPUT 3 --> D3

OUTPUT 4 --> D4

![Out relays on the Opta](assets/opta-out-relays.png)

The OPTA output contacts are "clean" contacts, they are contacts that are not live in a non-connection situation. This type of contact allows it to be used in any system and with any type of voltage. To function, the outputs must therefore be connected by bringing, for example a power cable to a terminal, and exiting the terminal on the side, go towards the load to be managed.
In this way, when the contact is closed by the logic set via IDE, that power supply signal will cross the contact and will switch on or in any case carry the signal up to the reference load.
The “clean” contact also allows to carry a different power system or type of load for each output contact.

![Clean contact on the Opta](assets/opta-clean-contact.png)

Let's run a simple sketch to test the output relays on Opta: in this sketch all the 4 relays are closing and reopening their contacts and after each relay's cycle a led, will be turned on to provide a visual feedback. 
To activate the relays and run this sketch you need to provide Opta with a voltage from 12 to 24 V DC by connecting it a proper power supply. 
In this sketch all the 4 relays are closing and reopening their contacts and after each relay's cycle a led, will be turned on to provide a visual feedback.

Opta has dedicated terminals for power supply, located in the upper part of Opta next to the Inputs. They are doubled to help the user to connect the power supply and any common part for the input terminals but are at the same potential (upon polarity) and equivalent.

These terminals are polarized, it is therefore mandatory to strictly respect the power supply polarity by connecting the positive connector of the power supply to "+" and the negative to "-".

![Connect these pins to drive the relays on the Opta](assets/opta-voltage-pins.png)

```arduino
void setup() {
 // initialize Relays outputs.
 pinMode(D0, OUTPUT); // sets the rele pin D0 as output
 pinMode(D1, OUTPUT); // sets the rele pin D1 as output
 pinMode(D2, OUTPUT); // sets the rele pin D2 as output
 pinMode(D3, OUTPUT); // sets the rele pin D3 as output
 
 // initialize digital pin LED_BUILTIN as an output.
 pinMode(LED_D0, OUTPUT);
 pinMode(LED_D1, OUTPUT);
 pinMode(LED_D2, OUTPUT);
 pinMode(LED_D3, OUTPUT);
}

void loop() {
 // closes and opens the contcat of the relay 1 and turns on led 1.
 digitalWrite(D0, HIGH); // sets the Rele 1 on
 digitalWrite(LED_D0, HIGH);
 delay(1000); // waits for a second
 digitalWrite(D0, LOW); // sets the Rele 1 off
 digitalWrite(LED_D0, LOW);
 delay(1000); // waits for a second
 
 // closes and opens the contcat of the relay 2 and turns on led 2
 digitalWrite(D1, HIGH); // sets the Rele 1 on
 digitalWrite(LED_D1, HIGH);
 delay(1000); // waits for a second
 digitalWrite(D1, LOW); // sets the Rele 1 off
 digitalWrite(LED_D1, LOW);
 delay(1000); // waits for a second
 
 // closes and opens the contcat of the relay 3 and turns on led 3
 digitalWrite(D2, HIGH); // sets the Rele 1 on
 digitalWrite(LED_D2, HIGH);
 delay(1000); // waits for a second
 digitalWrite(D2, LOW); // sets the Rele 1 off
 digitalWrite(LED_D2, LOW);
 delay(1000); // waits for a second

 // closes and opens the contcat of the relay 4 and turns on led 4
 digitalWrite(D3, HIGH); // sets the Rele 1 on
 digitalWrite(LED_D3, HIGH);
 delay(1000); // waits for a second
 digitalWrite(D3, LOW); // sets the Rele 1 off
 digitalWrite(LED_D3, LOW);
 delay(1000); // waits for a second
}
```

### Using Opta's Inputs

Opta has 8 input pins, that can be programmed to be used as analog or digital. The mapping between the marking on the Opta physical terminals (I1 to I8) and their definition in the core can be found below:

I1 --> A0

I2 --> A1

I3 --> A2

I4 --> A3

I5 --> A4

I6 --> A5

I7 --> A6

I8 --> A7

The 8 inputs pins can be used as digital (having the logical values of LOW or HIGH) or as analog inputs (within a range from 0 to 10V). 
* To use them as digital inputs, add the Arduino command *pinMode(pinName, INPUT);* inside the setup(). 
* To use them as analog inputs, add the command *analogReadResolution();* with the bit resolution that you want to use.

![Analog inputs on the Opta](assets/opta-analog-inputs.png)

Now let's try a sketch that will read the analog inputs on the Opta. The inputs can operate in a range between 0 and 10V.
The max voltage managed by the microcontroller is 3V. This maximum voltage needs to be put into relationship with the maximum resolution factor that we want to chose which can be selected within a range between 16bit (65535) and 12bit (4095). 
To get and display the proper voltage value read by the input, we need to convert the value read by the analogRead function and apply a rescaling factor of 0.3 which is determined by the internal voltage divider.
The sketch will read the inputs on the analog pins A0, A1 and A2 and then print the result in the serial monitor.

```arduino
void setup() {
 Serial.begin(9600);
 // 65535 is the max value with 16 bits resolution set by analogReadResolution(16)
 // 4095 is the max value with 12 bits resolution set by analogReadResolution(12)
 analogReadResolution(12);
}

void loop() {

 // read the input on analog input 1 corresponding to A0:
int sensorValueA0 = analogRead(A0);
float voltageA0 = sensorValueA0 * (3.0 / 4095.0)/ 0.3;
 // print out the value you read from o to the max value for the analog inputs resolution:
 Serial.print("I1 value: ");
 Serial.print(sensorValueA0);
 Serial.print(" corresponding to ");
 // print the voltage as a floating point number with 5 decimal digits
 Serial.print(voltageA0, 5);
 Serial.println("Volts");
 
 // read the input on analog input 2 corresponding to A1:
 int sensorValueA1 = analogRead(A1);
 float voltageA1 = sensorValueA1 * (3.0 / 4095.0)/0.3;
 // print out the value you read:
 Serial.print("I2 value: ");
 Serial.print(sensorValueA1);
 Serial.print(" corresponding to ");
 // print the voltage as a floating point number with 5 decimal digits
 Serial.print(voltageA1, 5);
 Serial.println("Volts");
 
 // read the input on analog input 3 corresponding to A2:
 int sensorValueA2 = analogRead(A2);
 float voltageA2 = sensorValueA2 * (3.0 / 4095.0)/0.3;
 // print out the value you read:
 Serial.print("I3 value: ");
 Serial.print(sensorValueA2);
 Serial.print(" corresponding to ");
 // print the voltage as a floating point number with 5 decimal digits
 Serial.print(voltageA2, 5);
 Serial.println("Volts");
 delay(1000);
}
```

You may notice from the output values that when the maximum value of 10V is reached, the corresponding numerical value is not 4095 as the max value with 12 bits resolution; this is because there is a precautional margin taken on the max voltage level applicable to the inputs to preserve the microcontroller.

### Connecting Opta to the Cloud

It is possible to use the Opta with the Arduino Cloud. To set up the Opta to the cloud go to the [Arduino Cloud](https://cloud.arduino.cc/). For help with how to get started with the cloud, go to our [Getting started with the cloud tutorial](https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started). We also have a number of other helpful tutorials for [the Arduino cloud](https://docs.arduino.cc/arduino-cloud/).

## Conclusion

This tutorial went through the basics of the Opta. Now you should know how to program the LEDs on the board. We also showed how to program the programmable button on the device. The analog inputs and the out relays were also covered. After going through this tutorial you should be ready to go into the other Opta tutorials and learn more about the device and its features. 

### Next Steps

Now that you know the basics of the Opta it could be a good idea to combine these features with other features on the Opta. For example, if you want to add connectivity to your solution, take a look at the [Getting started with connectivity on the Opta tutorial]().