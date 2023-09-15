---
title: 'Modbus RTU On Portenta Machine Control Using PLC IDE'
description: "Learn how to set and enable Modbus RTU on Portenta Machine Control using Arduino® PLC IDE."
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
  - hardware/05.pro-solutions/solutions-and-kits/portenta-machine-control
---

## Overview

The Portenta Machine Control boasts adaptable, high-quality industrial hardware and offers a diverse array of connection options. Its capabilities are further amplified by the Arduino PLC IDE software, optimizing the device for robust field operations. Moreover, the Portenta Machine Control is compatible with Modbus protocols, and with the Arduino PLC IDE, their integration is made straightforward.

![Portenta Machine Control with Modbus RTU Overview ](assets/pmc_plcide_general_system.png)

In this tutorial, you will discover how to establish Modbus RTU communication between two Portenta Machine Control devices through the Arduino PLC IDE.

## Goals

- Learn how to configure the workspace environment to work with Modbus RTU using Arduino PLC IDE.
- Learn how to configure Modbus RTU for Portenta Machine Control using Arduino PLC IDE.
- Learn how to verify that Portenta Machine Control has been correctly set up using an example that uses Modbus RTU communication.

## Required Hardware and Software

### Hardware Requirements

- [Portenta Machine Control](https://store.arduino.cc/collections/pro-family) (x2)
- USB-C® cable (x2)
- Wire with either specification for RS-485 connection (x3):
- STP/UTP 24-18AWG (Unterminated) 100-130Ω rated
- STP/UTP 22-16AWG (Terminated) 100-130Ω rated

### Software Requirements

- [Arduino PLC IDE Tools](https://www.arduino.cc/en/software#arduino-plc-ide)
- [Arduino PLC IDE software](https://www.arduino.cc/en/software#arduino-plc-ide)
- If you have a Portenta Machine Control, you will need a unique PLC IDE License key for your device. Get your license key [here](https://store.arduino.cc/products/plc-key-portenta-machine-control). Go to section [__License Activation with Product Key (Portenta Machine Control)__](https://docs.arduino.cc/software/plc-ide/tutorials/plc-ide-setup-license#6-license-activation-with-product-key-portenta-machine-control) to know more.
- [Portenta Machine Control Modbus RTU PLC IDE Project Example File](assets/ModbusRTU_PMC_Example.zip)

## Modbus Protocol

Modbus is a client/server architecture-based serial communication protocol that is open and free of licensing restrictions. Particularly in Building Management Systems (BMS) and Industrial Automation Systems (IAS), it is commonly employed in industrial electrical equipment.

It was released by Modicon (now Schneider Electric) in 1979 and has since become the de facto industry standard for industrial electronic devices to utilize when communicating with PLCs.

In Supervisory Control and Data Acquisition (SCADA) systems, a Remote Terminal Unit (RTU) and a supervisory device are frequently connected via the Modbus communication protocol. When communicating with electronic equipment, Modbus messages have a straightforward 16-bit format and a Cyclic-Redundant Checksum (CRC).

## Modbus RTU & PLC IDE

In this tutorial, we will walk you through the process of setting up two Portenta Machine Control devices for Modbus RTU communication using the Arduino PLC IDE. This tutorial aims to clarify the steps required for successful implementation.

The accompanying diagram offers a clear representation of the Portenta Machine Control configuration and deployment process for Modbus RTU:

![Modbus RTU Implementation with Arduino PLC IDE](assets/plcide_modbus_rtu_process.png)

The entire procedure is divided into three distinct stages:

* __Modbus RTU Configuration__ serves as the initial step, wherein we configure the Portenta Machine Control device with Modbus RTU and other inherent properties.

  In this phase, the role of the Portenta Machine Control device as either a Client or Server within Modbus RTU is specified. This includes settings such as 'Baud rate' and 'Serial Mode', which are crucial for the communication protocol.

  Depending on the device's role within Modbus RTU, we either outline the 'Status variables' or define the Modbus node to identify the devices communicating under this protocol.

* __PLC Program__, is created post device configuration, integrating Modbus RTU and other functionalities. An important aspect of this stage is the removal of the need for detailed Modbus RTU configurations within the PLC code.

  The setup is user-friendly. By referencing predefined variables in the PLC code, the system autonomously manages Modbus RTU data exchange. Such an approach leverages the device's initial configuration, reducing redundancy and ensuring efficient communication.

* __System Operation__ showcases the expected results after Modbus RTU setup and the PLC program's execution based on the developer's logic. As an outcome, the device can be seen communicating with its counterparts via Modbus RTU.

The given diagram emphasizes the consistent Modbus RTU configuration across different Arduino devices with the PLC IDE. A strength of this system is its flexibility. No matter the Modbus RTU specifics, the PLC program can operate seamlessly. Its robust design makes it versatile across diverse settings.

Additionally, the PLC code development is not restricted to one language. The system is compliant with the IEC61131-3 standard, granting the option to choose from the languages mentioned in the standard. This strikes the right balance between ease-of-use and precise code crafting.

With this broader perspective laid out, we are ready to delve into the details.

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

The two Portenta Machine Control devices will communicate using Modbus RTU. It is enabled by using RS-485 interface for both devices, set either with 'Full-Duplex' or 'Half-Duplex' mode. The following image shows the connection diagram to work with two Portenta Machine Control devices.

![RS-485 interface with Full-Duplex mode between Portenta Machine Control devices for Modbus RTU](assets/pmc_rtu_plcide_hardware_connection_full.png)

The previous illustration resembles a setup consisting of two Portenta Machine Control devices, communicating over RS-485 interface at Full-Duplex mode. The accompanying image shows an alternative mode at which two Portenta Machine Control devices are established over RS-485 interface with Half-Duplex mode.

![RS-485 interface with Half-Duplex mode between Portenta Machine Control devices for Modbus RTU](assets/pmc_rtu_plcide_hardware_connection_half.png)

Both configuration can be used to establish a Modbus RTU based communication. The Modbus RTU communication network can be scaled up by integrating additional protocol compatible devices as Portenta Machine Control or Opta™.

If we are connecting a Portenta Machine Control and an Opta™, the setup shown below can help you understand the overall connection.

![RS-485 interface between Portenta Machine Control and Opta™ for Modbus RTU](assets/pmc_opta_rtu_plcide_hardware_connection.png)

The Portenta Machine Control has integrated RS-485 120 Ω differential cable termination.

***Because Opta™ has no internal termination resistors, it must be installed per the Modbus protocol specification adding termination resistors. Also, if you experience inconsistent data transmission using Opta™ with other Modbus RTU compatible devices, please try again by inverting the A(-) and B(+) lines.***

### Workspace Pre-Configuration

For appropriate Modbus RTU operation, it requires some considerations to be taken into account beforehand to properly enable and use Modbus RTU on Portenta Machine Control using PLC IDE. Following subsections will help briefly explain such aspects.

***It is recommendable to check out [this tutorial](https://docs.arduino.cc/tutorials/portenta-machine-control/plc-ide-setup-license#3-project-setup) to familiarize with Arduino PLC IDE environment.***

#### Portenta Machine Control Basic Configuration
<br></br>

The Modbus RTU communication for the Portenta Machine Control does not require special pre-configuration. You will only have to make a manual sketch download with the desired protocol role with its properties, and its onboard elements to be used. These onboard elements can be programmable digital I/Os and dedicated digital outputs.

Portenta Machine Control can be initialized further in the process if additional changes in configuration is required.

![Arduino PLC IDE - Device Connection Procedure](assets/pmc_plcide_device_connection.gif)

#### Modbus RTU Client and Server Mode
<br></br>

The PLC IDE software provides the option to set the Portenta Machine Control as either a Modbus RTU Client, Server, or none of the previous modes. The option is configurable under `RS485 SerialPort` listed within `Resources` tab.

The Portenta Machine Control set as a Modbus RTU Client will provide 'Baud Rate' and 'Serial Mode' settings. The baud rate is available from 600 b/s to 115200 b/s. The serial mode provides set of options conformed with following elements:

- Parity: No Parity, Even Parity, Odd Parity
- Data Bits: 8 Data Bits (Only option for Data Bits)
- Stop Bits: 1 - 2 Stop Bits

Alternatively, the Portenta Machine Control set as a Modbus RTU Server requires an additional configuration called 'Slave Settings'. It will ask you to define the Modbus address with range between `1 .. 247`.

If you decide to disable Modbus RTU for the Portenta Machine Control, you can select the option 'none'. It will hide every Modbus RTU configuration parameter, disabling the protocol mode for the Portenta Machine Control.

#### General Modbus Node Configuration
<br></br>

The General Modbus Node allows to add information regarding the devices compatible with the Modbus messaging service.

![Arduino PLC IDE - General Modbus Node Configuration](assets/pmc_plcide_generalNode.png)

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

![Arduino PLC IDE - Modbus Custom Editor Configuration](assets/pmc_plcide_customModbus.png)

It is a useful feature to have frequently deployed device configuration stored that is compatible with Modbus protocol.

### Project Overview

The example project will be used to test the Modbus RTU connection between two Portenta Machine Control devices after you have prepared the necessary prerequisites and the necessary tools.

To create a live handshake verification procedure between two Portenta Machine Control devices, the example project will slightly modify its default example code using the counter ('cnt') variable and broadcast the counter data.

Using the counter data from the 'Modbus RTU Server Portenta Machine Control', the 'Modbus RTU Client Portenta Machine Control' manages the programmable digital I/Os and digital outputs. Each Portenta Machine Control is assigned a simple task using the aforementioned elements. You will learn to configure the Modbus RTU role for each Portenta Machine Control device, using the sections dedicated to each role.

You may access the entire example project [here](assets/ModbusRTU_PMC_Example.zip) if you would like to test it right away. Every setting and component is ready to be assembled and uploaded to the corresponding Portenta Machine Control.

The following sections will demonstrate how to set up each Portenta Machine Control according to its function in a Modbus RTU connection.

#### Modbus RTU Server Portenta Machine Control
<br></br>

To configure the Portenta Machine Control as a Modbus RTU Server, navigate to the `RS485 SerialPort` tab in the `Resources` panel within the PLC IDE. It will open a `Modbus Configuration` window where you should choose the `Modbus RTU Slave` setting. For the purpose of the tutorial example, we will employ the following properties for the server Portenta Machine Control:

- Port type: `RS485`
- Baud Rate: 19200 b/s
- Serial Mode: N,8,1 (No parity, 8 data bits, 1 stop bit)
- Slave settings (Modbus address): 10

![Arduino PLC IDE - Portenta Machine Control Server Modbus Configuration](assets/pmc_plcide_server_modbus.png)

Alternative values can be used per requirements if needed.

The subsequent image displays the `Status variables (volatile)` window. Within this window, we will define the `counter_stack` variable, specifying its access address and data type for Modbus RTU transmission.

![Arduino PLC IDE - Portenta Machine Control Server Status Variable](assets/pmc_plcide_server_statVar.png)

The `counter_stack` status variable uses the following parameters:

* Address: 25000 (dec) / 0x61A8 (hex)
* Name: cnt
* PLC type: INT

Upon finalizing the settings, go to `Resources -> Portenta Machine Control` and select the corresponding port, subsequently beginning the `Manual sketch download` process. Navigate to `On-line -> Set up Communication` and activate Modbus RTU, ensuring that the elevated USB port number designated for the Portenta Machine Control is selected.

![Arduino PLC IDE - Device Connection Procedure (Modbus TCP Server Portenta Machine Control)](assets/pmc_plcide_device_connection_server.gif)

Proceed with `On-line -> Connect` to set up a connection with the Portenta Machine Control server. If everything is set up correctly, we will see a message in the bottom right of the PLC IDE software that says it is connected.

![Arduino PLC IDE - Device Connection Status](assets/plcide_connection_stable.png)

Symbols `(1)` and `(2)` show different connection statuses: Portenta Machine Control connected without any PLC code, and Portenta Machine Control connected with an available PLC code, respectively.

To get the main PLC code onto the Portenta Machine Control, go to the `main` tab in the `Project` section. Then, you can enter the following code:

```arduino
counter_buffer := counter_buffer + 1;

IF counter_buffer >= delay_buffer THEN
	IF cnt < 255 THEN
	    cnt := cnt + 1;
	ELSE
	    cnt := 0;
	END_IF;
	counter_buffer := 0;
	counter_stack := counter_stack + 1;
END_IF;

// Translate count to binary
DO_0 := cnt AND 1;
DO_1 := SHR(cnt,1) AND 1;
DO_2 := SHR(cnt,2) AND 1;
DO_3 := SHR(cnt,3) AND 1;
DO_4 := SHR(cnt,4) AND 1;
DO_5 := SHR(cnt,5) AND 1;
DO_6 := SHR(cnt,6) AND 1;
DO_7 := SHR(cnt,7) AND 1;

IF counter_stack > 50 THEN
	counter_stack := 0;
END_IF;
```

The main function of the Portenta Machine Control server is to use a binary counter, which is programmed with digital outputs parameterized by a sub-counter variable named `cnt`. This `cnt` variable cycles within an 8-Bit map value. The pace of the counter is adjusted using the `counter_buffer` and `delay_buffer`, which serve as customizable timing factors. For the client Portenta Machine Control, the shared Modbus counter variable will be used and is defined as `counter_stack`.

![Arduino PLC IDE - Portenta Machine Control Server Global Variables](assets/pmc_plcide_server_globalVars.png)

To add the `counter_buffer` and `delay_buffer` variables, use the `New Variable` option, which can be found by right-clicking on `Global_vars`. The `counter_buffer` can be set as an `automatic` variable. On the other hand, the `delay_buffer` was initially added as a `constant` variable with a predefined value.

To upload the main PLC code to the Portenta Machine Control, you can either select `Download PLC code` or simply hit `F7`. Once everything is in place, a successful upload will look like the image shown below.

![Arduino PLC IDE - Portenta Machine Control Server Main Code](assets/pmc_plcide_server_mainCode.png)

Upon completing these steps, you will have effectively set up a Portenta Machine Control device to function as a Modbus RTU Server. The following section will guide you on how to configure another Portenta Machine Control as a Modbus RTU Client.

#### Modbus RTU Client Portenta Machine Control
<br></br>

To configure the Portenta Machine Control as a Modbus RTU Client, navigate to the `RS485 SerialPort` tab in the `Resources` section of the PLC IDE. This action will reveal the `Modbus Configuration` panel where you should choose the `Modbus RTU Master` setting. For the purpose of the tutorial example, set the client Portenta Machine Control with these specifications:

- Port type: `RS485`
- Baud Rate: 19200 b/s
- Serial Mode: N,8,1 (No parity, 8 data bits, 1 stop bit)

![Arduino PLC IDE - Portenta Machine Control Client Modbus Configuration](assets/pmc_plcide_client_modbus.png)

Alternative values can be used per requirements if needed.

To establish communication with the pre-configured Modbus RTU Server Portenta Machine Control, add a Modbus node by right-clicking the `RS485 SerialPort` tab within the `Resources` section. Once ready, you will see an 'Add' option. Use this to insert a 'Generic Modbus' node. For this example, configure the node with the following parameters:

* Name: PMC_RTU_1
* Modbus address: 10
* Minimum polling time: 1 ms
* Address type: Modbus
* Swap words mode: Little endian compliant (No words swapping)

Use the configuration model applied to the Modbus RTU Server Portenta Machine Control for these settings. The important detail to consider is the Modbus address. Make sure this address corresponds with that of the server Portenta Machine Control or any other compatible device, in case more nodes are added. The setup should resemble the image provided:

![Arduino PLC IDE - Portenta Machine Control Client Node](assets/pmc_plcide_client_nodeConfig.png)

After setting up the Modbus node for the client Portenta Machine Control,we need to specify the Modbus function responsible for retrieving the counter (`cnt`) data from the server Portenta Machine Control. Right-click on `PMC_RTU_1` or any other name you set with, to see the 'Add' option, which will bring forth a device catalog window showcasing all available Modbus functions:

![Arduino PLC IDE - Modbus Functions](assets/pmc_plcide_client_modbusFunctionConfig_reg.png)

To retrieve the counter data from the server Portenta Machine Control, select the 'Modbus FC-04 (Read Input Registers)' function. Configure the 'General' tab with the following parameters to ensure correct data access:

* Start address: 25000
* Polling time: 0 ms (Continuous Read)
* Timeout: 1000 ms

![Arduino PLC IDE - Modbus Functions](assets/pmc_plcide_modbus_functions.png)

Next, you will need to designate a variable to hold the counter data captured from the server Portenta Machine Control. To do this, go to the `Input Reg.` tab located in the Modbus function configuration menu. Create a variable named `counter_rec` to store the data sent via the protocol.

The following image shows a visual representation of the anticipated configuration:

![Arduino PLC IDE - Portenta Machine Control Client Modbus Function of the Node (Input Reg.)](assets/pmc_plcide_client_modbusFunctionInput_reg.png)

In this tutorial's demonstration, the client Portenta Machine Control is configured to use digital programmable I/Os and digital outputs.

The image below shows how digital outputs configuration should look within the PLC IDE interface:

![Arduino PLC IDE - Portenta Machine Control Client Digital Outputs Table](assets/pmc_plcide_device_localDO.png)

The digital programmable I/Os also needs labels to reference it later in the main PLC code. A table displaying the variable names designated for digital programmable I/Os can be seen below:

![Arduino PLC IDE - Portenta Machine Control Client Digital Programmable I/O Table](assets/pmc_plcide_device_DIO.png)

The main program below will be used to fetch counter data, control programmable digital I/Os, and manage corresponding digital outputs. A successful Modbus RTU communication will process previous tasks accordingly.

```arduino
counter := counter_rec;

IF counter >= 10 THEN
	DIO_0 := 1;
END_IF;

IF counter >= 20 THEN
	DIO_1 := 1;
END_IF;

IF counter >= 30 THEN
	DIO_2 := 1;
END_IF;

IF counter >= 40 THEN
	DIO_3 := 1;
END_IF;

IF counter >= 50 THEN
	DIO_0 := 0;
	DIO_1 := 0;
	DIO_2 := 0;
	DIO_3 := 0;
	server_opCycle := server_opCycle + 1;
END_IF;

// Translate count to binary
DO_0 := server_opCycle AND 1;
DO_1 := SHR(server_opCycle,1) AND 1;
DO_2 := SHR(server_opCycle,2) AND 1;
DO_3 := SHR(server_opCycle,3) AND 1;
DO_4 := SHR(server_opCycle,4) AND 1;
DO_5 := SHR(server_opCycle,5) AND 1;
DO_6 := SHR(server_opCycle,6) AND 1;
DO_7 := SHR(server_opCycle,7) AND 1;
```

The `counter` variable serves as a global reference for the client Portenta Machine Control. Conversely, `counter_rec` dedicated for Modbus transaction, storing the data obtained from the server Portenta Machine Control, which pertains to the `counter_stack` data. This variable was set up during the configuration of the 'Read Input Registers' Modbus function.

The client Portenta Machine Control will utilize four digital programmable outputs, with the complete digital outputs serving as an operation indicator. Each time the `counter` marks a new tenth value, it will activate the digital programmable output corresponding to the first digit of that counter value. For instance, when the `counter` reaches `10`, digital programmable output #1 will be activated.

Once the `counter` hits `50` and resets, it signifies the completion of one operation cycle. This process will continuously loop, using the digital outputs as a process cycle counter, displayed as a binary counter. The cyclic counter value is stored in the `server_opCycle`.


![Arduino PLC IDE - Portenta Machine Control Client Global Variables](assets/pmc_plcide_client_globalVars.png)

With this, we will compile and upload the main PLC code, the interface for the client Portenta Machine Control should mirror the image provided below:

![Arduino PLC IDE - Portenta Machine Control Client Main Code](assets/pmc_plcide_client_mainCode.png)

Finally, Portenta Machine Control is now ready as a Modbus RTU Client.

### Testing Modbus RTU Communication Between Portenta Machine Control Devices (PLC IDE)

You can access the complete example project [here](assets/ModbusRTU_PMC_Example.zip). You can download the compressed file, extract it, and use the pre-configured example project for your Portenta Machine Control devices.

Set both Portenta Machine Control devices running with the corresponding main PLC code with the hardware setup explained in [this section](#hardware-setup).

The following short clip shows a briefly expected behavior of the example project.

![Example Project Result](assets/pmc_plcide_rtu_example_result.gif)

The server Portenta Machine Control will:

- Execute a binary counter with digital outputs working as visual indicators, all contained within an 8-Bit boundary.
- Increase the shared Modbus counter variable each time the 8-Bit binary counter completes a cycle.
- Adjust the binary counter's speed by modifying buffer variables according to the desired values.

The client Portenta Machine Control will:

- Acquire server counter data through the Modbus protocol.
- Interpret and activate the corresponding programmable digital I/Os.
- Use the full cycle of the programmable digital I/Os to represent the total number of operation cycle, visualized using digital outputs as a binary counter.

## Conclusion

In this tutorial, you have learned to configure the workspace environment to work with Modbus RTU using Arduino PLC IDE and verified that Portenta Machine Control has been correctly set up and Modbus RTU communication is effective using an example project that controls Portenta Machine Control device's on-board features such as programmable digital I/Os and dedicated digital outputs based on customized example.

### Next Steps

Now that you have learned to implement the Modbus RTU between Portenta Machine Control devices using Arduino PLC IDE, try adding additional Modbus RTU compatible devices and create a Modbus RTU communication network.

Further, explore the possibilities by combining the Portenta Machine Control device's onboard features with the Modbus RTU communication network and deploy it as an enhancement solution for industrial management systems.