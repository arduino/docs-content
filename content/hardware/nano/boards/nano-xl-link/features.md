<FeatureDescription>

The Nano XL Link is based on the Microchip® PIC32CK2051SG01144 microcontroller, a 32-bit Arm® Cortex®-M33 with 2 MB of flash memory, 512 kB of RAM and an integrated hardware security module (HSM). The board is programmed with the Arduino Zephyr core, which runs Arduino sketches on top of the Zephyr® real-time operating system.

The board integrates CAN FD, RS-485 and 10/100 Ethernet interfaces and extends the classic Nano pinout through two 2x15 headers, so it can connect directly to industrial networks.

</FeatureDescription>

<FeatureList>

<Feature title="Arm® Cortex®-M33 Microcontroller" image="mcu">

The PIC32CK2051SG01144 provides 2 MB of flash memory, 512 kB of RAM and a hardware security module (HSM) for secure boot and key storage.

</Feature>

<Feature title="CAN FD Interface" image="industry">

An onboard TCAN3414 transceiver exposes the `CANH` and `CANL` lines on the headers. Supports classic CAN and CAN FD with payloads of up to 64 bytes and data rates of up to 8 Mbps.

</Feature>

<Feature title="RS-485 Interface" image="communication">

An onboard THVD2410 half-duplex transceiver exposes the `A` and `B` lines on the headers, with support for the `ArduinoRS485` library and Modbus RTU applications.

</Feature>

<Feature title="10/100 Ethernet" image="connection">

An onboard KSZ8081RNAIA PHY provides a 10/100 Mbps Ethernet interface through the Zephyr network stack (IPv4, TCP, UDP, DHCP and DNS). The RJ45 connector and magnetics are provided by the Nano Connector Carrier.

</Feature>

<Feature title="Extended Nano Pinout" image="nano-form-factor">

Two 2x15 headers keep the classic Nano digital, analog and power pins and add a second row with 12 extra digital pins, a second SPI bus, an I²C bus, a second UART, I²S and the fieldbus lines.

</Feature>

<Feature title="Qwiic Connector" image="hw-pin">

The onboard Qwiic connector provides a +3.3 VDC I²C bus with pull-up resistors for Qwiic, STEMMA QT and Modulino® devices, without soldering.

</Feature>

<Feature title="Wide Power Input" image="power">

The board can be powered from USB-C, from +7-24 VDC on the `VIN` pin through the onboard buck converter, or from a regulated +3.3 VDC source on the `3V3` pin.

</Feature>

<Feature title="Industrial Temperature Range" image="temperature-sensor">

Rated for operation from -20 °C to +85 °C, with bus termination resistors for CAN and RS-485 selectable through onboard solder jumpers.

</Feature>

</FeatureList>