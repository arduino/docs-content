<FeatureDescription>

The **Portenta H7** simultaneously runs high level code along with real time tasks, since it includes two processors that can run tasks in parallel. For example, it is possible to execute Arduino compiled code along with MicroPython one and have both cores to communicate with one another. The Portenta functionality is two-fold, it can either be running like any other embedded microcontroller board or as the main processor of an embedded computer. For instance, use the **Portenta Vision Shield** to transform your H7 into an industrial camera capable of performing real-time machine learning algorithms on live video feeds.

</FeatureDescription>


<FeatureList>
<Feature title="Portenta H7 Microcontroller" image="nano-form-factor">

  The Portenta H7 allows for programming with high-level languages and AI while performing low-latency operations on its customizable hardware.
<FeatureWrapper>
  <FeatureLink title="Datasheet" url="https://docs.arduino.cc/resources/datasheets/ABX00042-ABX00045-ABX00046-datasheet.pdf" download blank/>
</FeatureWrapper>
</Feature>

<Feature title="STM32H747XI dual Cortex®-M7+M4 32bit low power Arm® MCU" image="mcu">

  H7's main microcontroller is the dual core STM32H747, including a Cortex® M7 running at 480 MHz and a Cortex® M4 running at 240 MHz. The two cores communicate via a Remote Procedure Call mechanism that allows calling functions on the other processor seamlessly.
<FeatureWrapper>
  <FeatureLink title="Datasheet" url="https://content.arduino.cc/assets/Arduino-Portenta-H7_Datasheet_stm32h747xi.pdf" download/>
</FeatureWrapper>
</Feature>

<Feature title="Murata 1DX dual WiFi and Bluetooth® 5.1" image="wifi-bluetooth">

  The onboard wireless module allows to simultaneously manage WiFi and Bluetooth® connectivity.
<FeatureWrapper>
  <FeatureLink title="Datasheet" url="https://content.arduino.cc/assets/Arduino-Portenta-H7_Datasheet_Murata-1dx.pdf" download blank/>
</FeatureWrapper>
</Feature>

<Feature title="PF1550 Power Management IC" image="power">

  High efficiency PMIC chip with programmable voltage regulation and battery charging.

  <FeatureLink title="Library" url="https://github.com/arduino-libraries/Arduino_PF1550" download blank/>
</Feature>

<Feature title="Chrom-ART graphical hardware Accelerator™" image="mcu">

  Probably one of the most exciting features of the Portenta H7 is the possibility of connecting an external monitor to build your own dedicated embedded computer with a user interface. This is possible thanks to the STM32H747 processor's on-chip GPU, the Chrom-ART Accelerator™. Besides the GPU, the chip includes a dedicated JPEG encoder and decoder.

</Feature>

</FeatureList>
