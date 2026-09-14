Here you will find the technical specifications for the Arduino® Bughopper.

**Please read: power supply and voltage domains**

The **Bughopper** is powered exclusively through its **USB-C® connector**, which supplies +5 VDC from the host development machine. The onboard **FT230XQ** bridge IC uses this +5 VDC input to generate a regulated +3.3 VDC rail internally, which powers the FT230XQ logic and is indicated by the green LED.

The board operates across two distinct voltage domains:

- The **host side** (FT230XQ) operates at +3.3 VDC. All internal serial signals (TXD and RXD) between the FT230XQ and the level translator run at this voltage.

- The **target side** operates at the voltage supplied by the connected target board through the 1.27 mm debug connector, referred to here as **VTARGET**. The onboard level translator automatically bridges these two domains, ensuring signal integrity at any target operating voltage. The red LED lights up when VTARGET is present, confirming that the target board is powered and connected.

**Important: The Bughopper does not supply power to the target board and does not draw power from it.** Always ensure the target board is independently powered before connecting the Bughopper to avoid undefined behavior.