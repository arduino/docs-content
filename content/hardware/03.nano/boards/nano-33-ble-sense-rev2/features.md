<FeatureDescription>
The Arduino Nano 33 BLE Sense Rev2 is an excellent choice for beginners, makers, and professionals getting started with embedded machine learning and IoT applications. Built on the powerful nRF52840 microcontroller with a 64 MHz Arm® Cortex®-M4F processor, this board combines Bluetooth® Low Energy 5.0 connectivity with a comprehensive sensor suite. With 1 MB Flash memory and 256 KB SRAM, it provides ample space for complex applications while maintaining the compact Nano form factor.
</FeatureDescription>

<FeatureList>

<Feature title="Bluetooth® Low Energy 5.0" image="bluetooth">
  Features the NINA-B306 module with Bluetooth® Low Energy 5.0 and internal antenna. Enables wireless communication with smartphones, tablets, and other BLE devices for IoT applications and data transmission using the ArduinoBLE library.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense/ble-device-to-device"/>
  <FeatureLink variant="secondary" title="Library" url="https://www.arduino.cc/reference/en/libraries/arduinoble/"/>
</FeatureWrapper>
</Feature>

<Feature title="9-axis IMU" image="imu">
  Combines the BMI270 (6-axis accelerometer and gyroscope) with the BMM150 (3-axis magnetometer) to provide complete motion sensing. Detect orientation, movement, vibrations, and magnetic fields for navigation and gesture recognition applications.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense-rev2/imu-accelerometer"/>
  <FeatureLink variant="secondary" title="Library" url="https://github.com/arduino-libraries/Arduino_BMI270_BMM150"/>
</FeatureWrapper>
</Feature>

<Feature title="Digital MEMS Microphone" image="microphone">
  The omnidirectional MP34DT06JTR MEMS microphone captures high-quality audio for real-time analysis. Create voice interfaces, sound-triggered applications, or perform audio pattern recognition using the PDM library.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense-rev2/microphone-sensor"/>
  <FeatureLink variant="secondary" title="Library" url="/learn/built-in-libraries/pdm"/>
</FeatureWrapper>
</Feature>

<Feature title="Gesture and Proximity Sensor" image="proximity-sensor">
  The APDS9960 sensor provides gesture recognition, proximity detection up to 100mm, ambient light sensing, and RGB color detection. Create touchless interfaces, adaptive lighting systems, or color-sensing applications.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense-rev2/gesture-sensor"/>
  <FeatureLink variant="secondary" title="Library" url="https://www.arduino.cc/reference/en/libraries/arduino_apds9960/"/>
</FeatureWrapper>
</Feature>

<Feature title="Environmental Sensing" image="temperature-sensor">
  Dual environmental sensors provide comprehensive monitoring: the HS3003 measures humidity and temperature with ±0.1°C accuracy, while the LPS22HB barometric sensor measures pressure from 260 to 1260 hPa for altitude and weather applications.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense-rev2/humidity-and-temperature-sensor"/>
  <FeatureLink variant="secondary" title="Library" url="https://reference.arduino.cc/reference/en/libraries/arduino_hs300x/"/>
</FeatureWrapper>
</Feature>

<Feature title="Edge AI" image="core">
  With its Arm® Cortex®-M4F processor and sensor array, this board excels at edge AI applications. Run edge AI models directly on the device for pattern recognition, anomaly detection, and predictive maintenance without cloud connectivity.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense/edge-impulse"/>
  <FeatureLink variant="secondary" title="Learn More" url="/machine-learning"/>
</FeatureWrapper>
</Feature>

<Feature title="MicroPython Support" image="python">
  Program the board using MicroPython, a lean implementation of Python® 3 optimized for microcontrollers. Access all sensors and features through Python libraries for rapid prototyping and education.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense/micropython-installation"/>
  <FeatureLink variant="secondary" title="Learn More" url="/micropython"/>
</FeatureWrapper>
</Feature>

<Feature title="Extensive I/O Capabilities" image="core">
  Access 21 GPIO pins including 8 analog inputs (12-bit ADC), one analog output (12-bit DAC on A0), 5 PWM outputs, and dedicated I²C, SPI, and UART interfaces. Power options include USB (+5 VDC), VIN (+5-18 VDC), or direct +3.3 VDC supply.
<FeatureWrapper>
  <FeatureLink variant="primary" title="Documentation" url="/tutorials/nano-33-ble-sense-rev2/get-started-nano-33-ble-sense-rev2"/>
  <FeatureLink variant="secondary" title="Pinout" url="/hardware/nano-33-ble-sense-rev2#pinout"/>
</FeatureWrapper>
</Feature>

</FeatureList>