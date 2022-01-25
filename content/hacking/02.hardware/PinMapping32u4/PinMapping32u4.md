---
title: 'ATmega32U4-Arduino Pin Mapping'
description:  'A diagram showing the correspondence between the pins on an Arduino board and those of the ATmega32U4 microcontroller.'
tags: 
  - ATmega32U4
---

![ATmega32U4 pin mapping.](./assets/32U4PinMapping.png)

**Arduino Leonardo pin mapping table** 

| Pin Number | Pin Name                      | Mapped Pin Name          |
| ---------- | ----------------------------- | ------------------------ |
| 1          | PE6 (INT.6/AIN0)              | Digital pin 7            |
| 2          | UVcc                          | +5V                      |
| 3          | D-                            | RD-                      |
| 4          | D+                            | RD+                      |
| 5          | UGnd                          | UGND                     |
| 6          | UCap                          | UCAP                     |
| 7          | VUSB                          | VBus                     |
| 8          | (SS/PCINT0) PB0               | RXLED                    |
| 9          | (PCINT1/SCLK) PB1             | SCK                      |
| 10         | (PDI/PCINT2/MOSI) PB2         | MOSI                     |
| 11         | (PDO/PCINT3/MISO) PB3         | MISO                     |
| 12         | (PCINT7/OC0A/OC1C/#RTS) PB7   | Digital pin 11 (PWM)     |
| 13         | RESET                         | RESET                    |
| 14         | Vcc                           | +5V                      |
| 15         | GND                           | GND                      |
| 16         | XTAL2                         | XTAL2                    |
| 17         | XTAL1                         | XTAL1                    |
| 18         | (OC0B/SCL/INT0) PD0           | Digital pin 3 (SCL)(PWM) |
| 19         | (SDA/INT1) PD1                | Digital pin 2 (SDA)      |
| 20         | (RX D1/AIN1/INT2) PD2         | Digital pin 0 (RX)       |
| 21         | (TXD1/INT3) PD3               | Digital pin 1 (TX)       |
| 22         | (XCK1/#CTS) PD5               | TXLED                    |
| 23         | GND1                          | GND                      |
| 24         | AVCC                          | AVCC                     |
| 25         | (ICP1/ADC8) PD4               | Digital pin 4            |
| 26         | (T1/#OC4D/ADC9) PD6           | Digital pin 12           |
| 27         | (T0/OC4D/ADC10) PD7           | Digital Pin 6 (PWM)      |
| 28         | (ADC11/PCINT4) PB4            | Digital pin 8            |
| 29         | (PCINT5/OC1A/#OC4B/ADC12) PB5 | Digital Pin 9 (PWM)      |
| 30         | (PCINT6/OC1B/OC4B/ADC13) PB6  | Digital Pin 10 (PWM)     |
| 31         | (OC3A/#0C4A) PC6              | Digital Pin 5 (PWM)      |
| 32         | (ICP3/CLK0/)0C4A) PC7         | Digital Pin 13 (PWM)     |
| 33         | (#HWB) PE2                    | HWB                      |
| 34         | Vcc1                          | +5V                      |
| 35         | GND2                          | GND                      |
| 36         | (ADC7/TDI) PF7                | Analog In 0              |
| 37         | (ADC6/TDO) PF6                | Analog In 1              |
| 38         | (ADC5/TMS) PF5                | Analog In 2              |
| 39         | (ADC4/TCK) PF4                | Analog In 3              |
| 40         | (ADC1) PF1                    | Analog In 4              |
| 41         | (ADC0) PF0                    | Analog In 5              |
| 42         | AREF                          | AEF                      |
| 43         | GND3                          | GND                      |
| 44         | AVCC1                         | AVCC                     |