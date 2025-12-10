<FeatureDescription>

The Portenta X8 is a high-performance board, with many exceptional features. With two microprocessors combined, the NXP® i.MX 8M Mini MPU (Linux) and STM32H747XI dual Cortex®-M7+M4 32bit low power ARM® MCU (Arduino), this board is a great source to power the upcoming generation of the Industrial Internet of Things.

Thanks to the use of containers, the Portenta X8 offers an easy and secure way to deploy applications running in a controlled environment. The user has full control of the containers that the board is executing, having the option of creating and running custom containers on its own without the requirement of any additional subscription services and totally free of charge.

In case the user needs a more advanced and scalable professional solution, Arduino has created, in collaboration with Foundries, a subscription service with many enterprise-grade features:

- Secure maintenance of Portenta X8 Linux distribution and applications over time
- Portenta X8 fleets monitoring from anywhere
- Secure Over-The-Air updates to target Portenta X8 devices/fleets

Learn more about the so-called Portenta X8 Manager [here](https://cloud.arduino.cc/plans#business).

</FeatureDescription>

<FeatureList>
  <Feature title="NXP® i.MX 8M Mini" image="core">
    Includes the powerful NXP® i.MX 8M Mini processor with 4x ARM® Cortex®-A53 core platforms up to 1.8GHz per core and 1x Cortex-M4 core up to 400MHz.
    <FeatureWrapper>
      <FeatureLink title="Datasheet" url="https://docs.arduino.cc/resources/datasheets/cortexa53.pdf" download blank/>
    </FeatureWrapper>
  </Feature>

  <Feature title="STM32H747XI dual Cortex®-M7+M4 32bit low power Arm® MCU" image="mcu">
    X8's integrated microcontroller is the dual-core STM32H747, including a Cortex® M7 running at 480 MHz and a Cortex® M4 running at 240 MHz. The M4 core can be programmed through the Arduino IDE to run sketches for multiple real-time applications, like control of motors or other time-critical machinery at a barebones level. The M7 core runs an Arduino custom firmware, normally invisible to the User, able to map all its peripherals as Linux devices.
    <FeatureWrapper>
    <FeatureLink title="Datasheet" url="https://docs.arduino.cc/resources/datasheets/Arduino-Portenta-H7_Datasheet_stm32h747xi.pdf" download/>
    </FeatureWrapper>
  </Feature>

  <Feature title="NXP® SE050C2" image="crypto-chip">
    The Crypto chip allows users to keep security in mind by ensuring a secure connection at the hardware level.
    <FeatureWrapper>
    <FeatureLink title="Datasheet" url="https://docs.arduino.cc/resources/datasheets/SE050-DATASHEET.pdf" download blank/>
    </FeatureWrapper>
  </Feature>

  <Feature title="Two industrial-grade products in one" image="communication">
    The X8 offers the best of two approaches: the flexibility of usage of Linux combined with real-time applications. This approach allows developers to leverage the Arduino environment to perform e.g. automation control while accomplishing high-performance processes on Linux cores at the same time.
  </Feature>

  <Feature title="Containerizing system" image="configurability">
    With the so called encapsulated application, developers can isolate a single package of software, which means that the applications can run within a controlled environment. This allows developers to design device-independent software while achieving modularization, thanks to the container composition.
  </Feature>
</FeatureList>
