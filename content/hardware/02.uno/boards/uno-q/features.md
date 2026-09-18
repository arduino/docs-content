<FeatureDescription>

The **Arduino® UNO Q** integrates the Qualcomm® QRB2210 Microprocessor (MPU), running a full Debian-based Linux environment, with the STMicroelectronics® STM32U585 Microcontroller (MCU) built on Arm® Cortex®-M33 architecture, all within the compact UNO form factor. This dual-architecture platform combines high-performance computing with deterministic real-time control, delivering the power and versatility needed for modern AI at the edge applications.

Unlock hybrid development with Arduino App Lab, seamlessly uniting Python applications, Arduino sketches, and AI models in a single workflow. From AI-powered vision and sound solutions that react intelligently to their environment to sophisticated smart home systems, UNO Q with Arduino App Lab delivers next-generation embedded innovation to makers, educators, and professionals alike. At the same time, developers enjoy true freedom of choice: program the MCU subsystem with the Arduino IDE, or integrate Arduino CLI into existing workflows with popular editors like VS Code.

</FeatureDescription>

<FeatureList>

  <Feature title="Qualcomm Dragonwing™ QRB2210" image="core">
    Includes the powerful Qualcomm Dragonwing™ QRB2210 processor featuring:
    <ul>
        <li>Quad-core Arm® Cortex®-A53 @ 2.0 GHz</li>
        <li>Adreno GPU 3D graphics accelerator</li>
        <li>2x ISP (13 MP + 13 MP or 25 MP) @ 30 fps</li>
    </ul>
    <FeatureWrapper>
      <FeatureLink title="Overview" url="https://www.qualcomm.com/products/internet-of-things/robotics-processors/qrb2210" blank/>
    </FeatureWrapper>
  </Feature>

  <Feature title="STM32U585 Arm® Cortex®-M33 32-bit MCU" image="mcu">
    The UNO Q integrates the STM32U585 microcontroller featuring:
    <ul>
        <li>Arm® Cortex®-M33 up to 160 MHz</li>
        <li>2 MB flash memory</li>
        <li>786 kB SRAM</li>
        <li>Floating Point Unit</li>
    </ul>
    <FeatureWrapper>
    <FeatureLink title="Datasheet" url="https://www.st.com/resource/en/datasheet/stm32u585ai.pdf" download blank/>
    </FeatureWrapper>
  </Feature>

  <Feature title="Single-Board Computer" image="display">
    You can use the UNO Q as a standalone single-board computer leveraging its built-in <strong>Debian Linux environment</strong>. By using a USB-C dongle with external power delivery connected to the UNO Q USB-C port, you can connect:
    <div style="display: flex; flex-wrap: wrap; gap: 0.5em 2em;">
      <ul style="flex: 1; min-width: 200px; margin: 0;">
        <li>HDMI display</li>
        <li>Mouse and keyboard</li>
        <li>USB camera</li>
        <li>USB drive</li>
      </ul>
      <ul style="flex: 1; min-width: 200px; margin: 0;">
        <li>Ethernet cable</li>
        <li>microSD card</li>
        <li>USB microphone</li>
        <li>USB headphones</li>
      </ul>
    </div>
    <strong>Note:</strong> Recommended with the <strong>4 GB RAM</strong> UNO Q variant.
  </Feature>

<Feature title="Debian Linux OS" image="core">
  The Arduino UNO Q features a built-in <strong>Debian Linux</strong> environment with upstream support powered by its high-performance application processor, allowing you to develop in a familiar Linux environment without additional hardware.  
</Feature>

  <Feature title="Wireless Connectivity" image="wifi-bluetooth">
    The WCBN3536A wireless module allows to simultaneously manage WiFi® and Bluetooth® connectivity. The module features:
    <ul>
        <li><strong>Wi-Fi® 5</strong> Dual-band (2.4/5 GHz) with onboard antenna</li>
        <li><strong>Bluetooth® 5.1</strong> with onboard antenna</li>
    </ul>
  </Feature>

  <Feature title="Easily Expandable" image="connection">
    Take the UNO Q even further with its expandability leveraging the following features:
    <ul>
        <li><strong>Qwiic connector</strong> for seamless compatibility with Modulino nodes</li>
        <li><strong>Traditional UNO headers</strong> allowing you to stack official or custom shields on top of the UNO Q</li>
        <li><strong>New bottom high-speed connectors</strong> for using carriers to connect MIPI-CSI cameras, MIPI-DSI displays, analog audio, and much more</li>
    </ul>
  </Feature>

  <Feature title="Multiple IDE Compatibility" image="file-icon">
    The UNO Q is designed for flexible development, with first-class support for the <strong>Arduino App Lab</strong> and compatibility with the latest <strong>Arduino IDE 2.0+</strong>.  
    <ul>
        <li><strong>Arduino App Lab</strong> – Develop for both the onboard MPU and MCU with ease. Recommended for a full development experience.</li>
        <li><strong>Arduino IDE 2.0+</strong> – Program only the MCU using the beloved Arduino IDE.</li>
    </ul>
  </Feature>

  <Feature title="Remote Procedure Call (RPC)" image="communication">
    A built-in RPC library (i.e., Arduino Bridge) brings together the MPU running Linux and the microcontroller so you can create powerful and responsive applications in both worlds.
  </Feature>

</FeatureList>
