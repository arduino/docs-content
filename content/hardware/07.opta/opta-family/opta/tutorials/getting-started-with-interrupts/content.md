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

The Opta™ micro PLC is designed to operate in several industrial environments. Because it is developed for implementation in crucial industrial processes, it is capable of managing delicate tasks and recognizing defined parameter set of variables when such measurement or request conditions are met to proceed with appropriate operation.

The **Interrupt** feature can be set and used on Opta™ to handle time-sensitive and strictly scheduled tasks based on the state changes. This tutorial will help you learn to implement interrupt on Opta™ using Arduino ecosystem tools as the [Arduino IDE](https://www.arduino.cc/en/software).

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

## Interrupt Basics

The **interrupts** are requests triggered based commonly on timed events caused by certain state changes. It will pause the current or active operations if the request gets accepted under parametrized conditions. The **Interrupt Service Routine**, or **ISR**, is the handler that executes when an interrupt is generated. Usually, it is defined to run certain routine in a timely manner; but it can be also defined to use signal feedbacks whether to call interrupt routine depending on the external feedback, or as an indication for system failure.

### Interrupt Overall Type

Globally, interrupts are based on **hardware** and **software** events. The *hardware interrupt* takes action based on chage of the hardware state fed by an external feedback. This type of interrupt can occur at any instance while instructions are running. A button press could be interpreted as a hardware interrupt. For example, an external device may send a signal anytime, if certain conditions are met, to the main device resulting in execution of interrupt routine to make adjustments for the process.

The *software interrupts* are generated when the device itself is exposed to interally defined conditions or upon particular instruction call. It is similar to subroutine calls, but based on special conditionals that creates interrupt case. Such as examples are service requests within operating system or when interacting with device drivers as storage controllers for write and read operations.

***Please check out more with [Nick Gammon's Notes](http://gammon.com.au/interrupts), if you would like to dive deeper about interrupts.***

### Interrupt Triggers

For implementing on programmable logic controllers as Opta™, an important characteristic to know is about interrupt signals. Since it will handle broad types of signal, it is preferable to understand which signal condition suits certains applications. Generally they are **Level-Triggered** or **Edge-Triggered**. They are characterized as follows:

* Level-Triggered: this is when an interrupt has been requested with signals at particular logic level, which can be either *HIGH* or *LOW*.
* Edge-Triggered: this is when an interrupt has been requested due to signal at specific transition level, which can be either *RISING* or *FALLING* edge. It can also be configured with *CHANGE* argument to interrupt whenever either signal transition has occured.

With this, you will be able to understand how the following interrupt example on Opta™ will work.

## Instructions

### Setting up the Arduino IDE

This tutorial will need the latest version of the Arduino IDE. You can download the Arduino IDE [here](https://www.arduino.cc/en/software). Please check the [getting started with the Opta™ tutorial](/tutorials/opta/getting-started) if it is your first time setting up the Opta™ with the Arduino IDE.

### Example Setup

The example will try to keep the setup as simple as possible while providing the scalability of the Opta™. The setup will use the programmable user button (`BTN_USER`) and A0-A1 inputs as interrupt pins. All available D0-D3 relays will be configured as outputs and status LEDs will indicate corresponding contact state.

Please refer to the following diagram to have an overview of the inputs and outputs position of the example model.

![Opta™ Example Setup](assets/opta_interrupt_model.svg)

### Example Overview

The example will showcase different interrupt routines for Opta™ and you will be greeted with two scenarios. The `BTN_USER`, which is the user programmable button, will be used to switch the relay and corresponding status LED state in sequence. The `A0` and `A1` inputs will be open to external devices that sends signals periodically. The `A0` will be in charge of `D0` and `D1` relay, while the `A1` will control the `D2` and `D3` relays. The following section will highlight the important details of the example code to help you understand with ease.

### Example Description

First, becasue the variables used within interrupt should keep its value, it will be defined as `volatile` so that the variables found inside ISR can be shared with main program. In this case, `counter` will keep the number of `BTN_USER` presses and `relayLedState` to track status LED of the corresponding relay. The boolean variables `relCntState`, `batchState01`, and `batchState23` will be used to control the conditional flag when its respective interrupt is called.

```arduino
volatile unsigned int counter, relayLedState {};
volatile bool relCntState = false;
volatile bool batchState01 = false;
volatile bool batchState23 = false;
```

The relays and corresponding status LEDs are defined as an array, while its status which is shared, will also be managed via array.

```arduino
constexpr auto printInterval { 1000lu };
auto printNow { 0lu };

int idx{ 0 };
int relays[]{ D0, D1, D2, D3 };
int leds[]{ LED_D0, LED_D1, LED_D2, LED_D3 };
bool statuses[]{ true, true, true, true };
```

The `setup()` will define the relay and status LED outputs, and also the inputs that will be used to attach to interrupt cases.

```arduino
void setup(){

  Serial.begin(115200);
  for (const auto timeout = millis() + 2500; !Serial && millis() < timeout; delay(250))
      ;

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

The `loop()` will be running tasks that are tied to `BTN_USER` or `A0-A1` interrupts. But it will also be checking and keeping the number of button presses that represents interrupts generated by `BTN_USER` button.

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

The `relayLinearCounter()` function runs a linear sequence for turning on and off the D0 to D3 relays with its corresponding status LEDs based on `BTN_USER` response to trigger interrupt. The `counter` and `relayLedState` variables are used to track relay shift and also to provide button press counter to maintain total number of triggred interrupts. The `relCntState` is used as a gatekeeper to allow only when a valid interrupt has occured since the function is running inside the `loop()` function. The `counter` variable` is also incremented inside the ISR function which you will get to know later.

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

The `relayBatchInverter()` function checks to invert batch of relays and its corresponding status LEDs based on configured `A0` and `A1` interrupt pins. The `A0` controls the batch of relay `D0` and `D1`, while The `A1` controls `D2` and `D3` relays. Each input has ISR function to handle `batchState01` and `batchState23` boolean variables. When either pin is triggered with interrupt signal, it will invert the actual state of the corresponding relay batch.

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

For both previous functions, the `relayStateHandler()` function is used manage the relay status.

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

These are all the ISR functions that helps to shift relay states of the correspoding process whenever an interrupt has ocurred. These functions are kept as short as possible to maintain quick responses for interrupts that can happen at any time. For good practice, please do not use `delay()` inside these functions as it might cause erratic behaviors and use it as a quick state modifier to be used with functions that may be running continuosly.

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

You will be able to observe following results when testing if you were able to upload the example code correctly to the Opta™.

* You will be able to observe that the relays from D0 to D3 are turning on in sequence and turning off in the next sequence linearly as you press the `BTN_USER`. The sequence then will repeat, the counter will keep record of number of interrupts caused by `BTN_USER`, and actuated relay via `relayLedState`.
* If you send feedback on either `A0` or `A1` input with rising edge signal, it will proceed to apply state inversion on top of the actual relay states as a result of interrupt. Thus, you will observe the `D0` and `D1` relays have inverted its states if the interrupt was on `A0`; while `A1` will run the same task, but on `D2` and `D3` relays.

## Conclusion

You have now learned to enable and use interrupts on Opta™. With two main scenarios presented with the example, you have tested Opta™ with different interrupt cases by using integrated user programmable button and signal sources from external devices.

### Next Steps

Now that you are familiar with interrupts on the Opta™, take a look at the following documentation to learn more:

* Take a look at [getting started tutorial](/tutorials/opta/getting-started) to get a better overview of the features of Opta™

* If you wish to incorporate Wi-Fi®/Bluetooth® Low Energy in your Opta™ solutions, have a look at [connectivity tutorial](/tutorials/opta/getting-started-connectivity)