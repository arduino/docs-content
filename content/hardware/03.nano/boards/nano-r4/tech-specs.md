Here you will find the technical specifications for the Arduino® Nano R4.

**Please read: operating voltage**

The microcontroller on the **Arduino Nano R4** operates at 5 V, making it fully compatible with traditional Arduino shields, modules, and accessories designed for 5 V logic levels. This allows seamless reuse of existing components and simplifies interfacing with a wide variety of 5 V sensors and actuators.

Unlike boards based on 3.3 V logic (such as the Nano ESP32), the Nano R4 does not require logic level shifting when connecting to most classic Arduino components.

The board supports multiple power input options:

The VIN pin accepts an input voltage range of 6–21 V, regulated down to 5 V internally.

The board can also be powered directly via the USB-C® port, which supplies 5 V to the system.

All GPIO pins operate at 5 V and can source or sink up to 8 mA of current per pin.

Always verify the voltage requirements of any connected peripheral, and avoid drawing more current than the board’s limits to prevent instability or damage.