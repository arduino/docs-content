---
title: 'Modbus RTU On Opta™ Using PLC IDE'
description: "Learn how to set and enable Modbus RTU on Opta™ using Arduino® PLC IDE."
author: 'Taddy Chung and José Bagur'
libraries:
  - name: 'ArduinoModbus'
    url: https://www.arduino.cc/reference/en/libraries/arduinomodbus
difficulty: intermediate
tags:
  - Getting-started
  - ModbusRTU
software:
  - plc-ide
hardware:
  - hardware/07.opta/opta-family/opta
---

## Overview

Opta™ has scalable industrial-grade hardware with a wide range of connectivity choices. Opta™ is enhanced by the Arduino PLC IDE software, which makes the most of the device for solid field deployments. Opta™ supports Modbus protocols, and the Arduino PLC IDE makes it simple to implement them.

In this tutorial, you will learn how to implement Modbus RTU based communication between two Opta™ devices using Arduino PLC IDE.

## Goals

- Learn how to configure the workspace environment to work with Modbus RTU using Arduino PLC IDE.
- Learn how to configure Modbus RTU for Opta™ using Arduino PLC IDE.
- Learn how to verify that Opta™ has been correctly set up using an example that uses Modbus RTU communication.

## Required Hardware and Software

### Hardware Requirements

- [Opta™](https://store.arduino.cc/collections/pro-family) (x2)
- USB-C® cable (x2)
- Wire with either specification for RS-485 connection (x3):
- STP/UTP 24-18AWG (Unterminated) 100-130Ω rated
- STP/UTP 22-16AWG (Terminated) 100-130Ω rated

### Software Requirements

- [Arduino PLC IDE Tools](https://www.arduino.cc/en/software#arduino-plc-ide)
- [Arduino PLC IDE software](https://www.arduino.cc/en/software#arduino-plc-ide)
- If you have an Opta™, you do not need any license key to activate your product. Go to section [__License Activation With Pre-Licensed Products (Opta™)__](https://docs.arduino.cc/software/plc-ide/tutorials/plc-ide-setup-license#7-license-activation-with-pre-licensed-products-opta) to know more.
- [Opta™ Modbus RTU PLC IDE Project Example File](assets/ModbusRTU_Opta_Example.zip)

## Modbus Protocol

Modbus is a client/server architecture-based serial communication protocol that is open and free of licensing restrictions. Particularly in Building Management Systems (BMS) and Industrial Automation Systems (IAS), it is commonly employed in industrial electrical equipment.

It was released by Modicon (now Schneider Electric) in 1979 and has since become the de facto industry standard for industrial electronic devices to utilize when communicating with PLCs.

In Supervisory Control and Data Acquisition (SCADA) systems, a Remote Terminal Unit (RTU) and a supervisory device are frequently connected via the Modbus communication protocol. When communicating with electronic equipment, Modbus messages have a straightforward 16-bit format and a Cyclic-Redundant Checksum (CRC).

***For more information regarding the Modbus RTU protocol implementation on an Opta™, it may interest you to check out ["Getting Started with Modbus RTU on Opta™"](https://docs.arduino.cc/tutorials/opta/getting-started-with-modbus-rtu) tutorial.***

## Modbus RTU & PLC IDE

In this tutorial, we will guide you through setting up two Opta™ devices with Modbus RTU using the Arduino PLC IDE. The present tutorial will help understand the overall process of implementation.

The following diagram illustrates a concise visualization of how Opta™ is configured and deployed with Modbus RTU:

![Modbus RTU Implementation with Arduino PLC IDE](assets/plcide_modbus_rtu_process.png)

The entire procedure is divided into three distinct stages:

* __Modbus RTU Configuration__ is the foundational step where we initialize Opta™ device with Modbus RTU and other essential properties intrinsic to the device.
  
  During this stage, the Modbus RTU role, either Client or Server, is designated to Opta™ device. It includes 'Baud rate' and 'Serial Mode' configuration, which is essential for Modbus RTU communication.
  
  Based on the device setting within the Modbus RTU, either the 'Status variables' are delineated or the Modbus node is defined to determine the communicating devices using this protocol.

* __PLC Program__, established after device setup, is based on Modbus RTU and additional features. A significant advantage of this phase is the elimination of intricate configurations or specific programming tied to Modbus RTU within the PLC code.
  
  The procedure is designed for ease of use. By simply using predefined variables in the PLC code, the system handles data transfer through Modbus RTU on its own. This approach benefits from the device's prior setup, minimizing repetitive tasks and promoting effective communication.

* __System Operation__ represents the anticipated outcome post the Modbus RTU configuration and the execution of the PLC program based on the developer's designed logic. Consequently, we can observe the device engaging in communication with other devices through Modbus RTU.

The diagram presented shows the uniformity of the Modbus RTU setup across various Arduino devices using the PLC IDE. One main advantage of this system is its adaptability. Regardless of the specifics of the Modbus RTU setup, the PLC program consistently performs effectively. Its design ensures that it can be used in many different environments.

In addition, when developing the PLC code, there is no limitation to a single language. The system adheres to the IEC61131-3 standard, allowing one to select from the languages outlined in this standard. This ensures a balance between user convenience and accurate code development.

Having provided an overview of the entire process, we can now delve into the specifics.

## Instructions

### Setting Up the Arduino PLC IDE

Access the Arduino PLC IDE software by following [Arduino PLC IDE official website](https://www.arduino.cc/pro/software-plc-ide). You will have to download two executable files for proper software installation:

- [Arduino PLC IDE Tools](https://www.arduino.cc/en/software#arduino-plc-ide)
- [Arduino PLC IDE](https://www.arduino.cc/en/software#arduino-plc-ide)

![Arduino PLC IDE Software Download Section](assets/plcide_software_download.svg)

The **Arduino PLC IDE Tools** will provide all the required drivers, libraries, and cores for development while the **Arduino PLC IDE** will install the IDE software.

Install the Arduino PLC IDE Tools before the Arduino PLC IDE to avoid potential problems related to old libraries and drivers.

***For more details regarding Arduino PLC IDE setup, please take a look at [Arduino PLC IDE Setup and Board's License Activation](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license) tutorial.***

### Hardware Setup

The two Opta™ devices will communicate using Modbus RTU. It is enabled by using RS-485 interface for both devices. The following image shows the connection diagram to work with two Opta™ devices.

![RS-485 interface between Opta™ devices for Modbus RTU](assets/opta_rtu_plcide_hardware_connection.svg)

The Modbus RTU communication network can be scaled up by integrating additional protocol compatible devices as Opta™ or Portenta Machine Control.

### Workspace Pre-Configuration

For appropriate Modbus RTU operation, it requires some considerations to be taken into account beforehand to properly enable and use Modbus RTU on Opta™ using PLC IDE. Following subsections will help briefly explain such aspects.

***It is recommendable to check out [this tutorial](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license#3-project-setup) to familiarize with Arduino PLC IDE environment.***

#### Opta™ Basic Configuration

The Modbus RTU communication for Opta™ does not require special pre-configuration. You will only have to make a manual sketch download with the desired protocol role with its properties, and its onboard elements to be used. These onboard elements can be status LEDs and relays.

Opta™ can be initialized further in the process if additional changes in configuration is required.

#### Modbus RTU Client and Server Mode
<br></br>

The PLC IDE software provides the option to set Opta™ as either a Modbus RTU Client, Server, or none of the previous modes. The option is configurable under `RS485 SerialPort` listed within `Resources` tab.

Opta™ set as a Modbus RTU Client will provide 'Baud Rate' and 'Serial Mode' settings. The baud rate is available from 600 b/s to 115200 b/s. The serial mode provides set of options conformed with following elements:

- Parity: No Parity, Even Parity, Odd Parity
- Data Bits: 8 Data Bits (Only option for Data Bits)
- Stop Bits: 1 - 2 Stop Bits

On the other hand, Opta™ set as a Modbus RTU Server requires an additional configuration called 'Slave Settings'. It will ask you to define the Modbus address with range between `1 .. 247`.

If you decide to disable Modbus RTU for Opta™, you can select the option 'none'. It will hide every Modbus RTU configuration parameter, disabling the protocol mode for Opta™.

#### General Modbus Node Configuration
<br></br>

The General Modbus Node allows to add information regarding the devices compatible with the Modbus messaging service.

![Arduino PLC IDE - General Modbus Node Configuration](assets/opta_plcide_generalNode.png)

It will require you to fill in basic information under the `General` tab and parameters to manage under the `Parametrization` tab. The basic information consists of:

- Name of the device to be communicated under Modbus protocol
- Modbus address (1..247)
- Minimum polling time [ms]
- Address type
- Swap words mode

These information will help identify and correctly communicate with the target device.

#### PLC IDE Modbus Custom Editor
<br></br>

The Modbus Custom Editor allows you to define a Modbus node with set of pre-defined parameters and variables. It can be later added by using 'Add' option under 'RS485 SerialPort'.

To open the Modbus Custom Editor window, go to `Tools -> Run Modbus Custom Editor` on PLC IDE.

![Arduino PLC IDE - Modbus Custom Editor Configuration](assets/opta_plcide_customModbus.png)

It is a useful feature to have frequently deployed device configuration stored that is compatible with Modbus protocol.

### Project Overview

The example project will be used to test the Modbus RTU connection between two Opta™ devices after you have prepared the necessary prerequisites and the necessary tools.

To create a live handshake verification procedure between two Opta™ devices, the example project will slightly modify its default example code using the counter (`cnt`) variable and broadcast the counter data.

Based on the counter data it receives from the "Modbus RTU Server Opta™," the "Modbus RTU Client Opta™" will activate the relay and the status LED. You may learn how to configure the Modbus RTU role for each Opta™ device using the role-specific sections.

You may access the entire example project [here](assets/ModbusRTU_Opta_Example.zip) if you would like to test it right away. Every setting and component is ready to be assembled and uploaded to the corresponding Opta™.

The following sections will demonstrate how to set up each Opta™ according to its function in a Modbus RTU connection.

#### Modbus RTU Server Opta™
<br></br>

To set Opta™ as a Modbus RTU Server, navigate to the `RS485 SerialPort` tab located in the `Resources` panel of the PLC IDE. A window named `Modbus Configuration` will open and we will need to select `Modbus RTU Slave` option. For the purpose of the tutorial example, we will use the following properties for client Opta™:

- Baud Rate: 19200 b/s
- Serial Mode: N,8,1 (No parity, 8 data bits, 1 stop bit)
- Slave settings (Modbus address): 10

![Arduino PLC IDE - Opta™ Modbus RTU Server Configuration](assets/opta_plcide_server_modbusMainConfig.png)

Alternative values can be used per requirements if needed.

The following image shows the `Status variables (volatile)` window. Here, we will define the `cnt` variable, assigning its access address and datatype for Modbus RTU transmission.

![Arduino PLC IDE - Opta™ Server Status Variable](assets/opta_plcide_server_statVar.png)

The `cnt` status variable uses the following parameters:

* Address: 25000 (dec) / 0x61A8 (hex)
* Name: cnt
* PLC type: INT

With these settings ready, you need to go to `Resources -> Opta`, select the corresponding port, and begin the `Manual sketch download` process. Then you need to go to `On-line -> Set up Communication` and activate Modbus RTU with the higher USB port number assigned for Opta™.

![Arduino PLC IDE - Device Connection Procedure (Modbus TCP Server Opta™)](assets/opta_plcide_device_connection.gif)

Proceed with `On-line -> Connect` and it will establish communication between your computer and the Opta™ server. If everything is fine, you will be able to observe the message found at the lower right corner of the PLC IDE software stating that it is connected.

![Arduino PLC IDE - Device Connection Status](assets/plcide_connection_stable.png)

Symbols `(1)` and `(2)` denote the connection statuses: Opta™ connected without a PLC code, and Opta™ connected with an available PLC code, respectively.

Next, the main PLC code, also referred to as the primary code, must be compiled and uploaded to Opta™. To do this, navigate to the `main` tab within the `Project` panel, and input the following code:

```arduino
cnt := cnt + 1;

IF cnt >= 2750 THEN
    cnt := 0;
END_IF;
```

The Opta™ server device's task runs a simple counter and resets whenever the counter reaches `2750`. Use the `Download PLC code` option or press `F7` to initiate the code's compilation and uploading process to Opta™. A successful upload will resemble the image provided below.

![Arduino PLC IDE - Opta™ Server Main Code](assets/opta_plcide_server_mainCode.png)

Upon completing these steps, you will have successfully configured an Opta™ device as a Modbus RTU Server. The next section will guide you through setting up another Opta™ as a Modbus RTU Client.

#### Modbus RTU Client Opta™
<br></br>

To set Opta™ as a Modbus RTU Client, navigate to the `RS485 SerialPort` tab located in the `Resources` panel of the PLC IDE. The `Modbus Configuration` panel will open and we will need to select `Modbus RTU Master` option. For the purpose of the tutorial example, we will use the following properties for client Opta™:

- Baud Rate: 19200 b/s
- Serial Mode: N,8,1 (No parity, 8 data bits, 1 stop bit)

![Arduino PLC IDE - Opta™ Modbus RTU Client Configuration](assets/opta_plcide_client_modbusMainConfig.png)

Alternative values can be used per requirements if needed.

To establish communication with the configured Modbus RTU Server Opta™, Modbus node can be added by right-clicking on the `RS485 SerialPort` tab located under the `Resources` panel. Once done, the 'Add' option will be made visible. This option should be selected to introduce a 'Generic Modbus' node. For this example, the node must be configured with the following parameters:

* Name: Opta_RTU_1
* Modbus address: 10
* Minimum polling time: 1 ms
* Address type: Modbus
* Swap words mode: Little endian compliant (No words swapping)

For these settings, follow the configuration pattern used for the Modbus RTU Server Opta™. The most important detail to set is the Modbus address. Ensure this address matches the one given to the server Opta™ or any other compatible device should you add more nodes. The setup should resemble the image provided:

![Arduino PLC IDE - Opta™ Client Node](assets/opta_plcide_client_nodeConfig.png)

Once you have established the Modbus node for the client Opta™, it is time to determine the Modbus function that will fetch the counter (`cnt`) data from the server Opta™. Right-click on `Opta_RTU_1` or any other name you set with, and the 'Add' option will show up, displaying a device catalog window with all available Modbus functions:

![Arduino PLC IDE - Modbus Functions](assets/opta_plcide_modbus_functions.png)

To retrieve counter information from the server Opta™, select the 'Modbus FC-04 (Read Input Registers)' function. The 'General' tab needs to be configured with the following parameters to ensure correct data access:

* Start address: 25000
* Polling time: 0 ms (Continuous Read)
* Timeout: 1000 ms

Subsequently, you will need to define a variable to store the counter data retrieved from the server Opta™. To do this, navigate to the `Input Reg.` tab found within the Modbus function configuration interface. Introduce a variable named `counter_rec` to capture the data transmitted through the protocol.

The following image shows a visual representation of the anticipated configuration:

![Arduino PLC IDE - Opta™ Client Modbus Function of the Node (Input Reg.)](assets/opta_plcide_client_modbusFunctionConfig_reg.png)

In this tutorial's demonstration, the client Opta™ is configured to use status LEDs and relays as response to certain action. We have the flexibility to assign variables to these status LEDs. For the present example, we will use designations ranging from `LED1` to `LED4` for the corresponding status LEDs.

For example, to use the `relay_1` and `LED1` variables for the first relay and status LED respectively, these variables should be defined under the 'Local IO Mapping' section, specifically within 'Relay Outputs' and 'LED Outputs'. Neglecting this step will cause the program compilation to flag errors because of these undefined designations.

The following image shows a glimpse into how the configuration should appear within the PLC IDE interface:

![Arduino PLC IDE - Opta™ Client Status LED Table](assets/opta_plcide_client_ledSet.png)

Relays also need specific designations to reference them in the main PLC code. Below is a table presenting the variable names designated for the relays:

![Arduino PLC IDE - Opta™ Client Relay Table](assets/opta_plcide_client_relaySet.png)

The program outlined below is designed to retrieve counter data, oversee status LEDs, and handle the corresponding relays. Proper functioning of Modbus RTU communication ensures the efficient execution of the aforementioned tasks.

```arduino
counter := counter_rec;

IF counter >= 500 THEN
	relay_1 := TRUE;
	LED1 := TRUE;
END_IF;

IF counter >= 1000 THEN 
	relay_2 := TRUE;
	LED2 := TRUE;
END_IF;

IF counter >= 1500 THEN 
	relay_3 := TRUE;
	LED3 := TRUE;
END_IF;

IF counter >= 2000 THEN 
	relay_4 := TRUE;
	LED4 := TRUE;
END_IF;

IF counter >= 2500 THEN
	relay_1 := FALSE;
	relay_2 := FALSE;
	relay_3 := FALSE;
	relay_4 := FALSE;
	LED1 := FALSE;
	LED2 := FALSE;
	LED3 := FALSE;
	LED4 := FALSE;
END_IF;
```

The variable `counter` serves as a global reference for the client Opta™. While `counter_rec` is the Modbus-specific variable that stores data fetched from the server Opta™. This variable was defined during the configuration of the 'Read Input Registers' Modbus function.

Upon successful compilation and downloading of the main PLC code, the complete interface for the client Opta™ should resemble the image provided below:

![Arduino PLC IDE - Opta™ Client Main Code](assets/opta_plcide_client_mainCode.png)

Finally, Opta™ is now ready as a Modbus RTU Client.

### Testing Modbus RTU Communication Between Opta™ Devices (PLC IDE)

You can access the complete example project [here](assets/ModbusRTU_Opta_Example.zip). You can download the compressed file, extract it, and use the pre-configured example project for your Opta™ devices.

Set both Opta™ devices running with the corresponding main PLC code with the hardware setup explained in [this section](#hardware-setup). You will be able to observe the following results on client Opta™ repeatedly:

* Counter value = `500`: The status LED #1 and relay #1 will turn on
* Counter value = `1000`: The status LED #2 and relay #2 will turn on
* Counter value = `1500`: The status LED #3 and relay #3 will turn on
* Counter value = `2000`: The status LED #4 and relay #4 will turn on
* Counter value = `2500`: All status LEDs and relays will turn off

The following short clip shows a briefly expected behavior of the example project.

![Example Project Result](assets/opta_plcide_rtu_example_result.gif)

The left window shows the client Opta™, while the right window represents the server Opta™.

## Conclusion

In this tutorial, you have learned to configure the workspace environment to work with Modbus RTU using Arduino PLC IDE and verified that Opta™ has been correctly set up and Modbus RTU communication is effective using an example project that controls Opta™ device's on-board features such as relays and status LEDs based on customized example.

### Next Steps

Now that you have learned to implement the Modbus RTU between Opta™ devices using Arduino PLC IDE, try adding additional Modbus RTU compatible devices and create a Modbus RTU communication network.

Further, explore the possibilities by combining Opta™ device's onboard features with the Modbus RTU communication network and deploy it as an enhancement solution for industrial management systems.