---
author: 'Arduino'
description: 'This example demonstrate how to use two pushbuttons and distunguish between them using only one pin on your Arduino'
title: 'Two Switches, One Pin'
tags: [Pushbuttons, Resistors]
---

## Introduction
There are handy 20K pullup resistors (resistors connected internally between Arduino I/O pins and VCC - +5 volts in the Arduino's case) built into the Atmega chip upon which Arduino boards are based. They are accessible from software by using the digitalWrite() function, when the pin is set to an input.

This sketch exploits the pullup resistors under software control. The idea is that an external 200K resistor to ground will cause an input pin to report LOW when the internal (20K) pullup resistor is turned off. When the internal pullup resistor is turned on however, it will overwhelm the external 200K resistor and the pin will report HIGH.

One downside of the scheme (there always has to be a downside doesn't there?) is that one can't tell if both buttons are pushed at the same time. In this case the scheme just reports that sw2 is pushed. The job of the 10K series resistor, incidentally, is to prevent a short circuit if a pesky user pushes both buttons at once. It can be omitted on a center-off slide or toggle switch where the states are mutually exclusive.


## Hardware Required
- Arduino Board ([Link to store](https://store.arduino.cc/))
- 2x Pushbutton
- 1x 10K ohm Resistor
- 1x 200K - 1M ohm resistor

## Code
```arduino
/*
 * Read_Two_Switches_On_One_Pin
 * Read two pushbutton switches or one center-off toggle switch with one Arduino pin
 * Paul Badger 2008 
 * From an idea in Electronic Design News
 *
 * Exploits the pullup resistors available on each I/O and analog pin
 * The idea is that the 200K resistor to ground will cause the input pin to report LOW when the 
 * (20K) pullup resistor is turned off, but when the pullup resistor is turned on, 
 * it will overwhelm the 200K resistor and the pin will report HIGH.
 *
 * Schematic Diagram    ( can't believe I drew this funky ascii schematic )     
 *
 *
 *                             +5 V
 *                                |
 *                                \
 *                                /   
 *                                \    10K
 *                                /
 *                                \
 *                                |
 *                               /    switch 1  or 1/2 of center-off toggle or slide switch
 *                              /       
 *                                |
 *            digital pin ________+_____________/\/\/\____________   ground              
 *                                |               
 *                                |               200K to 1M  (not critical)
 *                               /   
 *                              /        switch 2 or 1/2 of center-off toggle or slide switch
 *                                |
 *                                |
 *                              _____   
 *                               ___     ground
 *                                _
 *
 */


#define swPin 2                 // pin for input  - note: no semicolon after #define
int stateA, stateB;             // variables to store pin states
int sw1, sw2;                   // variables to represent switch states 

void setup()                   
{
   Serial.begin(9600);
}

void loop()            
{
   digitalWrite(swPin, LOW);                   // make sure the pullup resistors are off
   stateA = digitalRead(swPin);
   digitalWrite(swPin, HIGH);                  // turn on the pullup resistors
   stateB = digitalRead(swPin);

   if ( stateA == 1 && stateB == 1 ){          // both states HIGH - switch 1 must be pushed
      sw1 = 1;
      sw2 = 0;
   }
   else if ( stateA == 0 && stateB == 0 ){     // both states LOW - switch 2 must be pushed
      sw1 = 0;
      sw2 = 1;
   }
   else{                                       // stateA HIGH and stateB LOW 
      sw1 = 0;                                 // no switches pushed - or center-off toggle in middle position
      sw2 = 0;
   }  

   Serial.print(sw1);
   Serial.print("    ");     // pad some spaces to format print output
   Serial.println(sw2);

   delay(100);  
}
```