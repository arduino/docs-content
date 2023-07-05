Here you will find the technical specifications for the Arduino® Nano ESP32.

**Please read: operating voltage**

The microcontroller on the **Arduino Nano ESP32** runs at 3.3 V, which means that you must never apply more than 3.3 V to its Digital and Analog pins. Care must be taken when connecting sensors and actuators to assure that this limit of 3.3 V is never exceeded. Connecting higher voltage signals, like the 5 V commonly used with the other Arduino boards, will damage the Nano ESP32.

Note that this board does not have a 5V pin, instead, it has a VUSB pin. The VUSB pin provides 5 V as long as it is powered via USB. Powering via VIN will not enable the VUSB pin, meaning you have no option to receive 5 V unless powered with USB. For communication with 5 V devices, you can opt to use a logic level translator.