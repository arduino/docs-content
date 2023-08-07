---
title: 'Using PLC IDE With Arduino® IoT Cloud'
description: "Learn how to integrate PLC IDE compatible devices with the Arduino IoT Cloud."
difficulty: beginner 
tags:
  - Opta™
  - PLC IDE
author: 'Taddy Chung, José Bagur and Giampaolo Mancini'
hardware:
  - hardware/07.opta/opta-family/opta
software:
  - plc-ide
  - iot-cloud
---

## Overview

The Arduino PLC IDE offers multiple possibilities to expand the connectivity of your industrial applications. The integration of the PLC IDE with the Arduino IoT Cloud allows you to create advanced HMI for your professional solutions that can be controlled in real-time in multiple ways and devices.

In this comprehensive tutorial, you will learn how to integrate and utilize the Arduino IoT Cloud with the Arduino PLC IDE. The tutorial covers the process of connecting your compatible devices and creating a compact, cloud-connected application using Opta™.

## Goals

- Learn how the Arduino IoT Cloud and the PLC IDE cooperate for seamless data exchange.
- Learn how to set the workspace environment on the PLC IDE for use with the Arduino IoT Cloud.
- Program a device using an Opta™ as an example integrating the PLC IDE and Arduino IoT Cloud.

## Hardware and Software Requirements

### Hardware Requirements

- [Opta™ WiFi](https://store.arduino.cc/products/opta-wifi) (x1)
- USB-C® cable (x1)

### Software Requirements

- [Arduino PLC IDE software](https://www.arduino.cc/en/software#arduino-plc-ide)
- [Arduino PLC IDE Tools](https://www.arduino.cc/en/software#arduino-plc-ide)
- If you have an Opta™, you do not need any license key to activate your product. Go to section __License Activation With Pre-Licensed Products (Opta™)__ to know more.
- The [Arduino Cloud](https://cloud.arduino.cc/) will be required to perform remote actuation and status monitoring via Wi-Fi® connectivity using the sketch provided in the following section. In case you do not have an account, you can create one for free inside the [cloud.arduino.cc](https://cloud.arduino.cc/home/?get-started=true).
- To ensure optimal Wi-Fi® connectivity on Opta™, please use the `WiFiFirmwareUpdater` to update with the latest network firmware version. This can be done by going to `Examples -> STM32H747_System -> WiFiFirmwareUpdater` on Arduino IDE 2. Additionally, please ensure that you have the latest __Arduino Mbed OS Opta Boards__ version, which can be checked under `Boards Manager`.
- [PLC IDE & Arduino IoT Cloud integration example project](assets/Opta_PLCIDE_Cloud.zip) file compatible with Opta™

***The present tutorial requires the latest versions of the PLC IDE & PLC IDE Tools ( >= v 1.0.4 ). You can get the latest versions [here](https://www.arduino.cc/en/software#arduino-plc-ide) for the latest PLC IDE and its tools. If it is your first time using the Arduino PLC IDE, we highly recommend you to begin with [Arduino® PLC IDE Setup & Device License Activation](https://docs.arduino.cc/software/plc-ide/tutorials/plc-ide-setup-license).***

## PLC IDE & Arduino IoT Cloud Integration

In this present tutorial, we will be utilizing two distinct platforms: the **Arduino PLC IDE** and the **Arduino IoT Cloud**. Each of these tools brings unique features and capabilities to the table, making them integral to our workflow.

* The [__Arduino PLC IDE__](https://www.arduino.cc/pro/software-plc-ide) integrates the capability to use **IEC IEC61131-3** programming languages, which are Ladder Diagram (LD), Sequential Function Chart (SFC), Function Block Diagram (FBD), Structured Text (ST), and Instruction List (IL). All these languages are applicable for Opta™.
  
  A wide set of standard features are included with these PRO solutions to develop industrial automation or advanced applications. You can find more tutorials related to the PLC IDE [the arduino documentation page](https://docs.arduino.cc/software/plc-ide) and the latest version of the software can be [downloaded here](https://www.arduino.cc/en/software#arduino-plc-ide).

* The __IoT Cloud__ is a platform that allows users to deploy IoT applications with ease and control parameters at any given moment. The platform provides robust security characteristics, of which Opta™ take advantage to provide secure industrial application deployments. You can find more about Arduino IoT Cloud at [here](https://docs.arduino.cc/arduino-cloud/).

### Understanding the Process

The PLC IDE supports seamless integration with Arduino IoT Cloud, enabling IoT capabilities for its compatible devices. The application field can be expanded thanks to this feature with the needed security elements, ensuring stable industrial operations.

The structure comprises two elements:

* The PLC IDE defines the device program with its connectivity settings and designed tasks.
* The Arduino IoT Cloud processes information exchange with the Arduino layer of the PRO solution devices.

![Dynamics of PLC IDE with Cloud Support Workflow](assets/plc-ide-iot-cloud-img_01.png)

The device is programmed in two layers: The PLC main execution program and the Arduino sketch. To communicate and interchange data in a safe way between these two different program layers, the PLC IDE use 'Shared variables' between these two layers.
The functions of each layer are:

* The *PLC program layer* will manage internal communication and data handling. It can be programmed to read sensor information that is obtained via selected Modbus protocol or available I/O pins. Then use this data to send out to or receive from the Arduino sketch layer.

* The *Arduino sketch* will handle data exchange bound between the PLC program layer and the Arduino IoT Cloud platform. The methods are '__PLCOut.varname__' and '__PLCIn.varname__', which are used to access the shared variables. For the purpose of the tutorial and to easily classify these methods, we will replace the 'varname' with the 'Shared_variable' tag.

  Therefore, the '__PLCOut.Shared_Variable__' and '__PLCIn.Shared_Variable__' methods manage the shared variables that facilitate communication between the two systems:

  - __PLCOut.Shared_Variable__: This variable refers to the data that is being sent from the PLC program layer to the Arduino sketch layer, which will be sent to Arduino IoT Cloud.
  
    In other words, it represents output from the PLC program. It could be sensor readings, status information, or any other data that the PLC program is designed to generate and share.

  - __PLCIn.Shared_Variable__: Conversely, this variable refers to the data that is being sent to the PLC from the Arduino sketch layer, received from Arduino IoT Cloud platform.
  
    This is input for the PLC program. It could be commands, configuration data, or other information that the Arduino IoT Cloud system sends to control or interact with the PLC.

![Shared variables between layers](assets/plc-ide-iot-cloud-img_02.png)

In most industrial IoT applications, the PLC program layer will be responsible for direct control of machinery or processes based on its programming, while the Arduino IoT Cloud platform will often be used as an HMI for operators, analytics, and remote control capabilities. The `Shared_Variables` commands allow in both cases real-time communication between these two layers.

## Example Implementation

A demonstrative example will be used to show how both features are integrated. The example will consist of an Arduino IoT Cloud dashboard and a PLC IDE project file configured for an Opta™.

Opta™ will be programmed to execute the following actions:

- Send analog readings and counter values to Arduino IoT Cloud.
- The user programmable LED of Opta™ will be controlled via an interactive button found within the Arduino IoT Cloud dashboard, which can later be designed to trigger certain actions.

The following diagram shows the main steps to connect Opta™ to the Arduino IoT Cloud using the PLC IDE. In the following sections, you will find how to perform all of these steps in detail.

![Example Implementation Procedure Overview](assets/plc-ide-cloud-procedure-overview.png)

The example implementation comprises the following sequence:

1. [Setting up the Arduino IoT Cloud](#setting-up-the-arduino-iot-cloud)
2. [Setting up the PLC IDE](#setting-up-the-plc-ide)
   1. [Shared variables configuration](#shared-variables-configuration)
   2. [Analog port](#analog-port-configuration) & [user programmable LED](#user-programmable-led-configuration) configuration
   3. [Library management](#library-components)
3. [Setting up the Arduino IoT Cloud dashboard](#arduino-iot-cloud-dashboard)
4. [System integration test](#testing-plc-ide-with-iot-cloud)

### Setting Up the Arduino IoT Cloud

We will begin by configuring the Arduino IoT Cloud with Opta™ to create a Thing. It will have Opta™ registered with variables and the dashboard configured to perform different actions.

***To learn more about how to use the Arduino IoT Cloud, please take a look at ["Getting Started With the Arduino IoT Cloud" tutorial](https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started).***

The following cloud variables will be created:

| **Cloud Variables** |        **Type**       | **Variable Permission** | **Send Values** |
|---------------------|-----------------------|-------------------------|-----------------|
| analog01            | Float (0 - 65535)     | Read Only               | On change       |
| counter             | Integer (0 - 2500)    | Read Only               | On change       |
| cloudButton         | Boolean               | Read & Write            | On change       |

The cloud variables will subsequently be linked to the 'Shared variables' within the PLC IDE environment to set up the communication pathway. Furthermore, the table displays a full 16-bit resolution range for 'analog01', as it can be paired with any chosen analog sensor. The 'counter' is set with a default limit of 2500, beyond which the device will reset to 0. If necessary, this limit can be adjusted in the PLC program, as elaborated further in this tutorial.

Once the Arduino IoT Cloud Thing has been created successfully, we will have a similar window on Arduino IoT Cloud Thing as the following image:

![Arduino IoT Cloud Thing and Cloud variables for Opta™](assets/plc-ide-cloud-thing.png)

We can now extract the code that will serve as the base for the Arduino sketch for Opta™ in the PLC IDE. The code can be accessed by going to the full editor. It will require some of the lines from the `ThingProperties.h`.

Please follow `Things -> "Opta PLC IDE Cloud" Thing -> Sketch -> Open full editor`, of which 'Opta PLC IDE Cloud' is the name of your created Thing, to get to the full editor window.

![Arduino IoT Cloud Full Editor](assets/iot-cloud-full-editor.png)

The base sketch of the example will be as follows:

```arduino
#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>

const char SSID[]     = "SECRET_SSID";    // Network SSID (name)
const char PASS[]     = "SECRET_OPTIONAL_PASS";    // Network password (use for WPA, or use as key for WEP)

void onCloudButtonChange();

float analog01;
int counter;
bool cloudButton;

WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PA
void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
  // This delay gives the chance to wait for a Serial Monitor without blocking if none is found
  delay(1500); 

  // Defined in thingProperties.h
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  
  /*
     The following function allows you to obtain more information
     related to the state of network and IoT Cloud connection and errors
     the higher number the more granular information you’ll get.
     The default is 0 (only errors).
     Maximum is 4
 */
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();
  // Your code here 
}

void initProperties(){
  ArduinoCloud.addProperty(analog01, READ, ON_CHANGE, NULL);
  ArduinoCloud.addProperty(counter, READ, ON_CHANGE, NULL);
  ArduinoCloud.addProperty(cloudButton, READWRITE, ON_CHANGE, onCloudButtonChange);
}

/*
  Since CloudButton is READ_WRITE variable, onCloudButtonChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onCloudButtonChange()  {
  // Add your code here to act upon CloudButton change
}
```

Save this example template for later. We will now proceed with a demonstrative example to show you how to set up the PLC IDE to be connected to the Arduino IoT cloud "Thing" we just created.

### Setting Up the PLC IDE

***Before continuing with the PLC IDE configuration with Opta™, please remember to have the latest PLC IDE with its corresponding tools stated within [Software Requirements](#software-requirements).***

The PLC IDE configuration will play an important role in establishing successful communication with the Arduino IoT Cloud. It will require setting onboard features and the communication protocol for Opta™ as usual. However, a proper 'Shared variables' setting will define the communication outcome with the Arduino IoT Cloud.

Thus, you will learn to configure the 'Shared variables' based on the peripherals and tasks you may assign to Opta™.

#### Shared Variables Configuration

The successful communication between Opta™ configured with PLC IDE and Arduino IoT Cloud relies on the 'Shared variables'. The 'Shared variables' is defined by heading to `Resources > Opta > Shared variables`. It will then offer two additional tabs: 'Inputs' and 'Outputs'.

![PLC IDE - Shared 'Input' and 'Output' variables](assets/plc-ide-shared-variable.png)

The '**Inputs**' define variables that will capture the data that comes from the Arduino IoT Cloud through the local Arduino sketch to Opta™ PLC main program runtime. It is the compilation of variables that the Arduino IoT Cloud will send accordingly.

Subsequently, the user programmable LED will be controlled via Arduino IoT Cloud dashboard. We will define a variable so that it can be assigned later to update LED state variable accordingly.

![PLC IDE - Shared inputs](assets/plc-ide-shared-variable-input.png)

The `in_cloudButton` will represent user programmable LED of Opta™ as a two state variable and indicates that is an input variable with the `in` tag.

The '**Outputs**' define the variables that Opta™ will send to Arduino IoT Cloud. It is the compilation of variables that you would want to monitor within the Arduino IoT Cloud dashboard.

The analog port reading and the counter value of Opta™ are the information that we want to display on the Arduino IoT Cloud dashboard. It can be programmed to use Modbus compatible devices and use its information further development.

The following table shows the variables added to the 'Shared outputs' table.

![PLC IDE - Shared outputs](assets/plc-ide-shared-variable-output.png)

The shared output variables are indicated with an `out` tag and represent the following information:

- `out_analog01`: Analog port number one reading
- `out_counter` : Counter value

The same variable name is used to maintain variable relationship and simplicity with the Cloud variables that we have defined [here](#setting-up-the-arduino-iot-cloud) previously.

Depending on the project's development requirements, you can add all the variables that will be used to exchange information with the Arduino IoT Cloud.

We will now configure Opta™ device's features to link all these shared variables.

#### Analog Port Configuration

The analog port is configured using the following properties under `Resources > Opta > Local IO Mapping > Programmable Inputs`:

| **Analog Port** | **Name** | **Variable** | **IO Type** | **Type** |
|-----------------|----------|--------------|-------------|----------|
| #1              | I1       | analog01     | Analog      | UINT     |

Opta™ has available 8 I/O ports that can be programmed either as analog or digital. You will select port number one and assign the `analog01` as the variable. The 'IO Type' must be 'Analog' and the 'Type' will update based on the selection of the 'IO Type' property.

The 'Programmable inputs mapping' table should look as the following image:

![PLC IDE - Programmable inputs mapping table](assets/plc-ide-programmable-inputs-mapping.png)

You can also change the analog resolution if needed, and the options are:

- 12 bits
- 14 bits
- 16 bits

#### User Programmable LED Configuration

The user programmable LED of Opta™ is configurable under `Resources > Opta > Local IO Mapping > LED Outputs`. To use the user programmable LED, you will need to assign a variable that will represent the 'LB' row.

![PLC IDE - LED outputs mapping table](assets/plc-ide-led-output-mapping.png)

In this case, the `userLed` is assigned as the variable that will represent the user programmable LED of Opta™ that emits blue light. The `userLed` is a boolean type variable as well as the `in_cloudButton`. It will be matched inside the PLC program to pass the boolean state per the command sent from the Arduino IoT Cloud dashboard.

#### Library Components

The Library section would be where you could find various pre-written codes or functions specific to PLC operations. It could include libraries for handling several industrial protocols, dealing with specific types of I/O, or even specialized functions for certain control systems. It makes the development process more efficient by providing ready-to-use codes, saving time and effort.

In the context of the PLC IDE, the libraries will need to be added manually under the `Sketch Libraries` found within the 'Resources' tab. These libraries are required to manage Arduino IoT Cloud connection and it is as follows:

| **Library Name**          | **Version** |
|---------------------------|-------------|
| ArduinoIoTCloud           | 1.11.2      |
| Arduino_ConnectionHandler | 0.7.6       |
| ArduinoECCX08             | 1.3.7       |
| ArduinoMqttClient         | 0.1.7       |
| Arduini_DebugUtils        | 1.4.0       |
| Arduino_Portenta_OTA      | 1.1.3       |

Once the libraries are in place within `Sketch Libraries`, we should have similar table as the following image:

![PLC IDE - Required libraries for Arduino IoT Cloud integration](assets/plc-ide-libraries.png)

These libraries are indexed, thus they are certified guaranteeing optimized performance and reliability. Leveraging them will not only speed up your development process but also increase the robustness of your applications for industrial environments. It may seem an extra step but it will help you keep cleaner, more reliable, and maintainable code.

***For more information about managing libraries inside PLC IDE, please have a look at ["Library Management"](https://docs.arduino.cc/software/plc-ide/tutorials/plc-programming-introduction#library-management) section from the [Programming Introduction with Arduino PLC IDE](https://docs.arduino.cc/software/plc-ide/tutorials/plc-programming-introduction).***

#### Arduino Sketch

We can now build the Arduino sketch that will be used to establish communication with the Arduino IoT Cloud and manage data traffic. The base sketch will be needed and can be found as discussed in the ['Setting Up the Arduino IoT Cloud'](#setting-up-the-iot-cloud) section.

Most of the code will keep the same structure contrary to the `loop()` and `onCloudButtonChange()` functions. It will integrate the 'Shared variables' with the `PLCOut.Shared_Variable` or `PLCIn.Shared_Variable` to establish information exchange between the device and platform.

Beginning with the `loop()` function, we have the following code:

```arduino
void loop() {
  ArduinoCloud.update();
   
  analog01 = PLCOut.out_analog01;
  counter = PLCOut.out_counter;
}
```

The `loop()` function is used to periodically update the `analog01` and `counter` variables with the shared output variables. The shared output variables are `out_analog01` and `out_counter`, and they are attached to `PLCOut`.

This means that the PLC program, which is capturing the analog port reading and updating the counter value, is defined to bring the data to the Arduino sketch layer and update the cloud variables accordingly. The Arduino IoT Cloud dashboard then displays updated information after the `ArduinoCloud.update()` method based on the cloud variables, which are `analog01` and `counter`.

The `onCloudButtonChange()` function is cloud generated and designed to process similar tasks. Every time a new value is updated from the Arduino IoT Cloud, the function will be triggered and run the assigned tasks. In this instance, it will update the user programmable LED of Opta™ whenever a change is detected with the assigned dashboard button.

```
/*
  Since CloudButton is READ_WRITE variable, onCloudButtonChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onCloudButtonChange()  {
  // Add your code here to act upon CloudButton change
  PLCIn.in_cloudButton = cloudButton;
}
```

The exact process involves assigning the updated cloud variable value to the `PLCIn.in_cloudButton` variable. It will update the shared variables attached to `PLCIn`, which is the `in_cloudButton`, and pass its value to the PLC program layer updating the status of Opta™.

Consequently, you will have an Opta™ constantly exchanging information with the Arduino IoT Cloud. The complete code for the Arduino sketch is as follows:

```arduino
#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>

const char SSID[]     = "NETWORK_SSID";    // Network SSID (name)
const char PASS[]     = "NETWORK_PASS";    // Network password (use for WPA, or use as key for WEP)

void onCloudButtonChange();

bool cloudButton;
float analog01;
int counter;

WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PASS);

void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
  // This delay gives the chance to wait for a Serial Monitor without blocking if none is found
  delay(1500); 

  // Defined in thingProperties.h
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  
  /*
     The following function allows you to obtain more information
     related to the state of network and IoT Cloud connection and errors
     the higher number the more granular information you’ll get.
     The default is 0 (only errors).
     Maximum is 4
 */
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();
  
  analog01 = PLCOut.out_analog01;
  counter = PLCOut.out_counter;
}

void initProperties(){
  ArduinoCloud.addProperty(cloudButton, READWRITE, ON_CHANGE, onCloudButtonChange);
  ArduinoCloud.addProperty(counter, READ, ON_CHANGE, NULL);
  ArduinoCloud.addProperty(analog01, READ, ON_CHANGE, NULL);
}

/*
  Since CloudButton is READ_WRITE variable, onCloudButtonChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onCloudButtonChange()  {
  // Add your code here to act upon CloudButton change
  PLCIn.in_cloudButton = cloudButton;
}
```

The `NETWORK_SSID` and `NETWORK_PASS` requires to be manually defined. Please replace these parameters to establish connection with the desired network. Also, the parameters must be defined in between the quotation marks, replacing `NETWORK_SSID` and `NETWORK_PASS` fields.

#### PLC Program

The Arduino sketch is ready, and it needs a PLC program that will control the onboard features of Opta™ and data readings.

The PLC program will do the following processes:

- Run a linear counter and store to `cnt`, and pass the data to `out_counter` (Shared variables)
- Reset counter value when it reaches 2500 in its value
- Update the user programmable LED state of Opta™ based on `in_cloudButton` (Shared variables)
- Update analog reading on the port number one defined to `analog01` and passing it to `out_analog01` (Shared variables)

The following code delivers the previous tasks:

```
cnt := cnt + 1;
out_counter := cnt;

IF out_counter >= 2500 THEN
	cnt := 0;
END_IF;

userLed := in_cloudButton;

out_analog01 := analog01;

```

With this PLC program, we are all set to configure Opta™ device's internal processes and use Arduino sketch to establish a connection with the Arduino IoT Cloud.

For a good practice, we will set the present PLC program as a 'Fast Task'. It can be done by adding the `main`, which is the present PLC program we will use, to `Tasks -> Fast` under `Project` window tab.

![PLC IDE - Fast Task assignment](assets/plc-ide-fast-task.png)

### Arduino IoT Cloud Dashboard

The Arduino IoT Cloud dashboard can be designed to your preference. The following image shows a dashboard example that allows for the control of the user programmable LED and the display of information received from Opta™.

![Arduino IoT Cloud dashboard example](assets/plc-ide-cloud-dashboard.png)

More information about Arduino IoT Cloud can be found [here](https://docs.arduino.cc/arduino-cloud/).

### Testing PLC IDE with Arduino IoT Cloud

The complete example project file for PLC IDE can be downloaded [here](assets/Opta_PLCIDE_Cloud.zip). It is ready to use with Opta™ in the instance at the preferred workspace.

***The first compilation process may take some time to finish. It can take upto 7 minutes or more depending on the environment.***

Once we have successfully configured Opta™ with PLC IDE and established communication with the Arduino IoT Cloud dashboard, we have following tasks in action:

- Arduino IoT Cloud dashboard displays the analog port number one reading and counter value of the connected Opta™
- The user programmable LED of Opta™ can be controlled using the button found within the Arduino IoT Cloud dashboard

The animation below shows a simple active desktop dashboard:

![Arduino IoT Cloud dashboard preview animation](assets/plc-ide-cloud-preview.gif)

The mobile dashboard is also available if on-demand monitoring and actuation is needed:

![Arduino IoT Cloud mobile dashboard preview animation](assets/plc-ide-cloud-dashboard-mobile.gif)

***If Opta™ fails to communicate with the Arduino IoT Cloud after configuration, please use the `WiFiFirmwareUpdater` to update Opta™ with the latest network firmware version.***

## Conclusion

You have now set an Opta™ using PLC IDE and successfully connected to the Arduino IoT Cloud platform. You learned how these tools integrate and can be used to create a simple interface allowing you to oversee Opta™ device's status. With this, you are now more familiar with the PLC IDE and Arduino IoT Cloud environment.

### Next Steps

As you progress, feel free to delve into the vast Arduino ecosystem. It will encourage you to utilize an array of libraries and hardware enhancements to construct robust, secure, and interconnected industrial solutions with Opta™. For a deeper understanding of its software and hardware characteristics, consider reviewing our beginner's guide to Opta™ [here](https://docs.arduino.cc/tutorials/opta/getting-started).

## Support

If you encounter any issues or have questions while working with the PLC IDE or Arduino IoT Cloud, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for the the PLC IDE or Arduino IoT Cloud. The Arduino Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Arduino help center page](https://support.arduino.cc/hc)

### Forum

Join our community forum to connect with other the PLC IDE and Arduino IoT Cloud users, share your experiences, and ask questions. The forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to PLC IDE and Arduino IoT Cloud.

- [The PLC IDE and Arduino IoT Cloud in the Arduino Forum](https://forum.arduino.cc/)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the the PLC IDE and Arduino IoT Cloud.

- [Contact us page](https://www.arduino.cc/pro/contact-us)
