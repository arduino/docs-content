Here you will find the technical specifications for the Arduino® Nano 33 BLE Rev2.

**Please read: operating voltage**

The microcontroller on the Nano 33 BLE Rev2 runs at 3.3 V, which means that you must never apply more than 3.3 V to its Digital and Analog pins. Care must be taken when connecting sensors and actuators to ensure that this limit of 3.3 V is never exceeded. Connecting higher voltage signals, like the 5 V commonly used with the other Arduino boards, will damage the Nano 33 BLE Rev2.

To mitigate potential risks in your existing projects, it's important to note that the 5 V pin on the header, located between RST and A7, is not initially connected as per the default factory settings when using the Nano. If your design relies on drawing 5 V from this pin, it won't function right away. This precaution is in place to emphasize the need for compliance with the 3.3 V requirement for both digital and analog inputs.

5V on that pin is available only when two conditions are met: you make a solder bridge on the two pads marked as VUSB and you power the Nano 33 BLE Rev2 through the USB port. If you power the board from the VIN pin, you won't get any regulated 5V and therefore even if you do the solder bridge, nothing will come out of that 5V pin. The 3.3V, on the other hand, is always available and supports enough current to drive your sensors. Please make your designs so that sensors and actuators are driven with 3.3V and work with 3.3V digital IO levels. 5V is now an option for many modules and 3.3V is becoming the standard voltage for electronic ICs.