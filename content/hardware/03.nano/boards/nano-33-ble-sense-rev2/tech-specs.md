**Please read: operating voltage**

The Arduino Nano 33 BLE Sense Rev2 operates at +3.3 VDC. Never apply more than +3.3 VDC to its digital and analog pins, as higher voltages will permanently damage the board. 

The 5V pin (between RST and A7) is not connected by default as a safety precaution. To enable the +5 VDC output on this pin:

1. Create a solder bridge on the VUSB pads
2. Power the board via USB (+5 VDC will not be available when powered through VIN)

The 3V3 pin is always available and provides sufficient current for sensors and actuators. When interfacing with +5 VDC systems, use appropriate level shifters to protect the board's inputs.