---
title: 'Getting Started with Interrupts on Opta™'
description: "Learn how to make use of the Interrupts on Opta™."
difficulty: beginner 
tags:
  - Getting started
  - Interrupts
author: 'Taddy Chung and José Bagur'
software:
  - ide-v1
  - ide-v2
hardware:
  - hardware/07.opta/opta-family/opta
---

## Overview

The Opta™ micro PLC is designed to operate in several industrial environments involving crucial processes. These process types require controllers to be responsive and precise to manage their delicate tasks, and capable of handling large sets of conditions within defined parameters in real time. Asynchronous operations or spontaneous events are one of many processes that could require attention at any moment.

The **Interrupt**, a basic yet vital feature, is available on Opta™ to handle time-sensitive and unexpected events based on state changes. This tutorial will help you to implement interrupt on Opta™ using the [Arduino IDE](https://www.arduino.cc/en/software) found within Arduino ecosystem tools.

## Goals

- Learn how to enable interrupts on Opta™
- Learn how to implement interrupts on Opta™

### Required Hardware and Software

#### Hardware Requirements

- Opta™ PLC (x1)
- USB-C® cable (x1)
- 12-24VDC/1A power supply (x1)

#### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- [Interrupt example code](assets/Interrupts_Opta.zip)

## Interrupt Basics

The **interrupts** are requests triggered based commonly on timed events caused by state changes. It will pause the current or active operations if the interrupt request gets accepted under parametrized conditions. The **Interrupt Service Routine**, or **ISR**, is the handler that executes when an interrupt is generated. Usually, it is defined to run particular routines periodically. However, it can also be set to use external signal feedback to call interrupt routine or as an indication of system failure.

### Interrupt Overall Type

Globally, interrupts are based on **hardware** and **software** events. The *hardware interrupt* takes action based on the hardware state change provided by external feedback. This type of interrupt can occur at any instance while instructions are running. A button press could be interpreted as a hardware interrupt. For example, an external device may send a signal anytime, if certain conditions are met, to the main device resulting in the execution of an interrupt routine to make adjustments to the process.

The *software interrupts* occur when the device itself is exposed to internally defined conditions or upon a particular instruction call. It is similar to subroutine calls but based on special conditionals that create interrupt cases. A few examples are service requests within the operating system or when interacting with device drivers as storage controllers for write and read operations.

***Please check out [Nick Gammon's Notes](http://gammon.com.au/interrupts) for more in-depth information about interrupts.***

### Interrupt Triggers

Interrupt signals are an important element to comprehend to set events with appropriate triggers, especially when it is to be implemented on programmable logic controllers such as Opta™. Since it will handle broad signal types, it is a good practice to understand which signal condition suits certain applications. Generally, they are **Level-Triggered** or **Edge-Triggered**. They are characterized as follows:

* Level-Triggered: this is when an interrupt has been requested with signals at a particular logic level, which can be either *HIGH* or *LOW*.
* Edge-Triggered: this is when an interrupt has been requested due to a signal at a specific transition level, which can be either *RISING* or *FALLING* edge. It can also be configured with *CHANGE* argument to interrupt whenever either signal transition has occurred.

With this, you will now be able to follow the interrupt example on Opta™ with much ease.

## Instructions

### Setting up the Arduino IDE

This tutorial will need the latest version of the Arduino IDE. You can download the Arduino IDE [here](https://www.arduino.cc/en/software). Please check the [getting started with the Opta™ tutorial](/tutorials/opta/getting-started) if it is your first time setting up the Opta™ with the Arduino IDE.

### Example Setup

The example will try to keep the setup as simple as possible while maintaining the scalability of the feature on Opta™. The setup will use the programmable user button (`BTN_USER`) and `A0-A1` inputs as interrupt pins. All available `D0-D3` relays will be configured as outputs and status LEDs will indicate the corresponding contact state.

Please refer to the following diagram to have an overview of the inputs and outputs position of the example model.

![Opta™ Interrupt Example Setup](assets/opta_interrupt_model.svg)

### Example Overview

The example will showcase different interrupt routines for Opta™, and you will be greeted with two scenarios. The `BTN_USER` is the user-programmable button that will be used to switch the relay and corresponding status LED state in sequence. The `A0` and `A1` inputs will be open to external devices that send signals periodically. The `A0` will be in charge of the `D0` and `D1` relays, while the `A1` will control the `D2` and `D3` relays. The following section will highlight the details of interest of the example code to help you understand it with ease.

### Example Description

First, because the variables used within interrupt should keep their value, they will be defined as `volatile` so that the variables found inside ISR can be shared with the main program. In this case, `counter` will keep the number of `BTN_USER` presses and `relayLedState` to track the status LED of the corresponding relay. The boolean variables `relCntState`, `batchState01`, and `batchState23` will be used to control the conditional flag when its respective interrupt is called.

```arduino
volatile unsigned int counter, relayLedState {};
volatile bool relCntState = false;
volatile bool batchState01 = false;
volatile bool batchState23 = false;
```

The relays and corresponding status LEDs are defined in an array including their status. Using the array provides the advantage to manage and call the data flexibly.

```arduino
int idx{ 0 };
int relays[]{ D0, D1, D2, D3 };
int leds[]{ LED_D0, LED_D1, LED_D2, LED_D3 };
bool statuses[]{ true, true, true, true };
```

The `setup()` will define the relay and status LED outputs, and also the inputs that will be used to attach to interrupt cases. The `attachInterrupt()` function configures the inputs as interrupts with its trigger method and connects to the defined ISR functions that can be found later in the example description. Thus, all the defined input pins are set as interrupt pins with their dedicated ISR functions and are programmed to trigger with a `RISING` signal.

```arduino
void setup(){

  ...

  // Outputs
  for (int i = 0; i < 4; i++) {
    pinMode(relays[i], OUTPUT);
    pinMode(leds[i], OUTPUT);
  }

  // Inputs
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(BTN_USER, INPUT);

  attachInterrupt(digitalPinToInterrupt(BTN_USER), relayCounterISR, RISING);
  attachInterrupt(digitalPinToInterrupt(A0), batch01_ISR, RISING);
  attachInterrupt(digitalPinToInterrupt(A1), batch23_ISR, RISING);
}
```

The `loop()` will be running tasks that are to execute based on `BTN_USER` or `A0-A1` interrupts. It will also be checking and keeping the number of button presses that represent interrupts generated by the `BTN_USER` button.

```arduino
void loop(){

  if (millis() > printNow) {
      Serial.print("Presses: ");
      Serial.println(counter);

      printNow = millis() + printInterval;
  }

  // For USR_BTN interrupts
  relayLinearCounter();
  
  // For A0 & A1 interrupts
  relayBatchInverter();
}
```

The `relayLinearCounter()` function runs a linear sequence for turning on and off the `D0` to `D3` relays with their corresponding status LEDs based on the interrupt triggered each time `BTN_USER` is pressed. The `counter` and `relayLedState` variables are used to track the total number of `BTN_USER` triggered interrupts, which also represents the number of button presses, and currently shifted relay status. The `relCntState` is used as a gatekeeper to allow only when a valid interrupt has occurred since the function is running inside the `loop()` function.

```arduino
// Relay and status indicator state in linear sequence
void relayLinearCounter(){
  if (relCntState == true){
    if (counter > 4){
      relayLedState = counter % 4;
      
      if (relayLedState == 0){
        relayLedState = 4;
      }
    } else {
      relayLedState = counter;      
    }

    Serial.print(F("Triggered Relay: "));
    Serial.println(relayLedState);
    Serial.print(F("Counter Status: "));
    Serial.println(counter);

    // Array indexes start at 0
    idx = relayLedState - 1;

    relayStateHandler(idx);

    relCntState = false;

  }
}
```

The `relayBatchInverter()` function checks to invert a relay batch and its corresponding status LEDs based on `A0` and `A1` interrupt pins. The `A0` controls the batch of relays `D0` and `D1`, while The `A1` controls `D2` and `D3` relays. Each input has an ISR function conditioned with `batchState01` and `batchState23` boolean variables. When either pin is triggered with an interrupt signal, it will invert the state of the corresponding relay batch based on present relay states.

```arduino
// Interrupt based on A0 & A1 to invert its defined states in batch
void relayBatchInverter(){
  if (batchState01 == true){
    Serial.println(F("A0 interrupt: Relay Batch 0 & 1"));
    for (int i = 0; i < 2; i++){
      relayStateHandler(i);
    }
    batchState01 = false;
  }

  if (batchState23 == true){
    Serial.println(F("A1 interrupt: Relay Batch 2 & 3"));
    for (int j = 2; j < 4; j++){
      relayStateHandler(j);
    }
    batchState23 = false;
  }
}
```

For both previous functions, the `relayStateHandler()` function is used to manage the relay status. The `digitalWrite()` function will use a special conditional which goes by `status`. It will seek the corresponding relay and compare its stored status to shift its state in a more automated way. It is a practical method to avoid writing the same lines of code in different parts of the sketch and helps maintain a cleaner code structure using a single function with an argument to process the data.

```arduino
void relayStateHandler(int relayID){
  // Get current status
  auto status = statuses[relayID] ? HIGH : LOW;
  
  // Apply new status to the outputs
  digitalWrite(relays[relayID], status);
  digitalWrite(leds[relayID], status);

  // Invert the statuses array to be updated
  statuses[relayID] = !statuses[relayID];
}
```

These are all the ISR functions that help to shift relay states within the corresponding process whenever an interrupt has occurred. These functions are kept as short as possible to maintain quick responses for interrupts that can happen at any time. For good practice, please do not use `delay()` inside these functions as it might cause erratic behaviors, and use it as a quick state modifier to be used with functions that may be running continuously.

```arduino
// All ISR functions
void relayCounterISR(){
  counter++;
  relCntState = true;
}

void batch01_ISR() {
  batchState01 = !batchState01;
}

void batch23_ISR() {
  batchState23 = !batchState23;
}
```

### Full Example Code

You can access the complete example code [here](assets/Interrupts_Opta.zip). After extracting the compressed file, you will be able to upload and test it out with your Opta™.

### Testing Interrupt

You will be able to observe the following results when testing if you were able to upload the example code correctly to the Opta™.

* You will be able to observe that the `D0-D3` relays are turning on in sequence and turning off in the next succession linearly as you press the `BTN_USER` button. The sequence then will repeat, and the counter will keep a record of the number of interrupts caused by `BTN_USER` button press, and currently actuated relay via `relayLedState`.
* If you send feedback on either `A0` or `A1` input with a rising edge signal, it will apply state inversion on top of the actual relay states as a result of the interrupt. Thus, you will observe the `D0` and `D1` relays invert their states if the interrupt was triggered on `A0`; while `A1` will do the same job, but on `D2` and `D3` relays.

Hence, your Opta™ is processing based on asynchronous interrupt generated by `BTN_USER` button while `A0-A1` are in charge of the interrupts generated periodically by an external device.

## Conclusion

In this tutorial, you have learned to enable and use interrupts on Opta™. On top of it, with the supplied example, you have tested Opta™ with multiple interrupt cases by using an integrated user-programmable button and signal sources from external devices, along with the Opta™ PLC's hardware features as onboard relays and status LEDs.

### Next Steps

Now that you are familiar with interrupts on the Opta™, take a look at the following documentation to learn more:

* Take a look at [getting started tutorial](/tutorials/opta/getting-started) to get a better overview of the features of Opta™

* If you wish to incorporate Wi-Fi®/Bluetooth® Low Energy in your Opta™ solutions, have a look at [connectivity tutorial](/tutorials/opta/getting-started-connectivity)