
<FeatureDescription>

The MKR Motor Carrier features a **ATSAMD11** processor for automated control of the outputs, two **MC33926** DC / servo motor drivers and two **DRV8871** DC motor drivers. It also features screw terminals for motor outputs, male header pins for motor outputs, an I2C connector, encoder inputs, LiPo battery connector and battery reading capabilities.

</FeatureDescription>

<FeatureList>
<Feature title="ATSAMD11" image="core">

The MKR Motor Carrier features an on-board processor for automated control the outputs.
<FeatureWrapper>
<FeatureLink title="Datasheet" url="http://ww1.microchip.com/downloads/en/devicedoc/atmel-42363-sam-d11_datasheet.pdf" download blank/>
</FeatureWrapper>
</Feature>

<Feature title="MC33926" image="mcu">

The MKR Motor Carrier features a DC / Servo motor driver capable of handling currents up to 5A.
<FeatureWrapper>
<FeatureLink title="Datasheet" url="https://www.nxp.com/docs/en/data-sheet/MC33926.pdf" download blank/>
</FeatureWrapper>
</Feature>


<Feature title="DRV8871" image="mcu">

The MKR Motor Carrier features a DC motor driver with PWM control capable of handling currents up to 3A.
<FeatureWrapper>
<FeatureLink title="Datasheet" url="https://www.ti.com/document-viewer/DRV8871/datasheet/features" download blank/>
</FeatureWrapper>
</Feature>

<Feature title="Motor outputs" image="connection">

The carrier features four servo motor outputs and four DC motor outputs (two standard, two high performance).

</Feature>

<Feature title="Encoder inputs" image="hw-pin">

The MKR Motor Carrier features two inputs for encoders.

</Feature>

<Feature title="Screw terminals" image="hw-pin">

Screw terminals makes connections more robust for projects in motion.

</Feature>

<Feature title="LiPo battery connector" image="power">

Connect a 6.5V - 11.1V battery to either the male headers (2S and 3S compatible) or to the screw terminals.

</Feature>


<Feature title="Male header pins" image="hw-pin">

Several male header connections for DC / servo motors are available. In addition, it also has a 4 pin I2C connector.

</Feature>

<Feature title="Battery status" image="power">

The MKR Motor Carrier is capable of reading the current status of batteries.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/mkr-motor-carrier/mkr-motor-carrier-battery"/>
  <FeatureLink variant="secondary" title="Library" url="https://github.com/arduino-libraries/ArduinoMotorCarrier/"/>
</FeatureWrapper>
</Feature>

</FeatureList>
