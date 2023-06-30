Here you will find the technical specifications for the Arduino® UNO R4 WiFi.

**Note on ESP header:** the ESP32-S3 module on this board operates on 3.3 V. The ESP header located close to the USB-C® connector is 3.3V only and should not be connected to 5 V. This may damage your board.

**Note on Qwiic connector:** the Qwiic connector on this board is connected to a secondary I2C bus on this board, **IIC0**. This connector is **3.3 V only**, connecting higher voltages may damage your board. To initialize this bus, use `Wire1.begin()` instead.

**Maximum current draw per pin:** the UNO R4 series' maximum current draw per pin is **8 mA**, which is significantly lower than previous versions. Do not attempt to draw higher currents as this may damage your board.