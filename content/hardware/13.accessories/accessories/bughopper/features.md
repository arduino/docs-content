<FeatureDescription>
The Arduino Bughopper is a compact USB-to-UART debug accessory built around the FT230XQ bridge IC. It connects to compatible target boards through their JCTL 2.54 mm debug connector, providing a dedicated serial debug channel without occupying the board's main USB port. Onboard ESD protection, automatic voltage level translation and status LEDs make it a reliable tool for remote debugging, firmware logging and continuous UART monitoring.
</FeatureDescription>

<FeatureList>

<Feature title="FT230XQ USB-to-UART Bridge" image="communication">
The FT230XQ converts USB traffic from your development machine into a standard UART serial link (TXD/RXD), enabling real-time debug logging and serial communication with the target board at baud rates from 300 bps up to 3 Mbps.
</Feature>

<Feature title="Automatic Voltage Level Translation" image="mcu">
An onboard bidirectional level translator automatically bridges the +3.3 VDC host logic domain and the target board's voltage domain, ensuring reliable signal integrity regardless of the target operating voltage.
</Feature>

<Feature title="ESD-Protected USB Lines" image="usb">
ESD diodes protect the USB data lines against electrostatic discharge, safeguarding both the Bughopper and the connected target board from damage during insertion and normal use.
</Feature>

<Feature title="Dual Output Connectors" image="communication">
The board provides two physical connection options: a female 2.54 mm 2×5 header (J2) for direct connection to JCTL header and a male 1.27 mm 2×5 header (J3) for compact ribbon cable setups, offering flexible integration into any workspace or enclosure.
</Feature>

<Feature title="USB-C® Connectivity" image="usb">
A USB-C® connector provides a modern, reversible connection to the host development machine, supplying the +5 VDC required to power the board and its internal +3.3 VDC logic.
</Feature>

<Feature title="Four Status LEDs" image="power">
Four onboard LEDs provide at-a-glance visibility of the system state: a green LED indicates +3.3 VDC power, a red LED confirms the target board is powered and connected, and two yellow LEDs indicate serial activity on the TXD and RXD lines respectively.
</Feature>

<Feature title="Auxiliary GPIOs" image="mcu">
Four auxiliary GPIO lines (CBUS0–CBUS3) are available  as open-drain signals on the output connectors, allowing the FT230XQ to send control signals to the target board preventing back-powering.
</Feature>

</FeatureList>