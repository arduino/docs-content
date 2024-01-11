---
title: 'Connecting MKR WiFi 1010 to a Wi-Fi Network'
difficulty: intermediate
compatible-products: [mkr-wifi-1010]
description: 'Learn how to program your board to connect to a Wi-Fi network.' 
tags: 
  - IoT
  - Wi-Fi
author: 'Karl Söderby'
libraries:
  - name: WiFiNINA
    url:  https://www.arduino.cc/en/Reference/WiFiNINA
hardware:
  - hardware/01.mkr/01.boards/mkr-wifi-1010
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Introduction

One of the MKR WiFi 1010's core strengths is the ability to connect to a Wi-Fi network. In this tutorial, we will focus on achieving this with the help of the **WiFiNINA** library. We will first connect to a Wi-Fi network and then look at some functions that can help us gather information such as, the IP address of our board, encryption type, RSSI strength and the name of the network we are connecting to.

This tutorial is a great starting point for any maker interested in making applications connected to the Internet.

___

## Hardware & Software Needed

- Arduino MKR WiFi 1010
- Micro USB cable
- Arduino IDE (offline and online versions available)
- Arduino SAMD Board Package installed (for offline editor only)
- WiFiNINA library (explained later in this tutorial)


### Circuit

This tutorial requires no circuit. We just need a Micro USB cable to connect our MKR WiFi 1010 board to a computer.


![Simple circuit using only the board.](assets/mkr_tutorial_02_img_01_rev2.png)
___

## Creating the Program

The goal with this tutorial is to be able to connect our MKR WiFi 1010 board to a Wi-Fi network, and print relevant information regarding the connection.

The following steps are needed in order to create this program:

- Create a header file to store our credentials for the Wi-Fi network which we will connect to.
- Create a function to connect to the Wi-Fi network.
- Create a function to print information regarding the connection.

**1.** First, let's make sure we have the drivers installed. If we are using the Web Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it. 

**2.** Now, we need to install the library needed. If we are using the Web Editor, there is no need to install anything. If we are using an offline editor, simply go to **Tools > Manage libraries..**, and search for **WiFiNINA** and install it.

**3.** Then, we need to create a new header file, to store our credentials. We do this, so we don't accidentally store our credentials in a code we may share on the Internet. Depending on what editor you are using, the process is slightly different, but we can follow the instructions below:

### Using the Offline Editor

If you are using the offline editor, simply click on the arrow pointing downwards on the top right corner, following the picture below.

![Creating a new tab.](assets/mkr_tutorial_02_img_02.png)

This will open up a yellow field in the bottom of the editor, where we need to name our file **"arduino_secrets.h"**. When we have named it, click "OK" and a new tab will open.

![Naming the file.](assets/mkr_tutorial_02_img_03.png)

Inside this tab, we need to enter the following code. Simply replace `"yourNetwork"` and `"yourPassword"` with the credentials of your Wi-Fi network. Remember that it is case-sensitive!

```arduino
#define SECRET_SSID "yourNetwork"
#define SECRET_PASS "yourPassword"
```

### Using the Online Editor
In the online editor, we need to click the downward arrow next to our sketch tab, and click **"Add Secret Tab**. This will create a tab called **Secret**.

![Add secret tab.](assets/mkr_tutorial_02_img_04.png)

We now need to head back to the original sketch file, and enter the following code:

```arduino
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
```

This will automatically create two fields in the **Secret** tab. If we go back to this tab, we can enter our credentials there.

![Enter network and password credentials.](assets/mkr_tutorial_02_img_05.png)

___

## Code Explanation

>**Note:** This section is optional, you can find the complete code further down on this tutorial.

We have now finished creating our secret credential tab in either the offline or online editor, so let's get started with the code! In this section, we will go through the code, step by step, to get familiar with the different programming concepts we are using.

First, we need to include the **WiFiNINA** library to access its functionalities. We then need to include the **arduino_secrets.h** file we created (not required in online editor). After that, we need to create two `char` variables, one to store our network name, another to store our network password. If you are using the online editor, we have already pasted this in the code in the previous step. We then set the initial Wi-Fi radio's status to idle.

```arduino
#include <WiFiNINA.h>

#include "arduino_secrets.h"

char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int status = WL_IDLE_STATUS;     // the Wifi radio's status
```

In the `setup()`, we start serial communication, followed by `while(!Serial);`, which basically means that unless we open the Serial Monitor, the program will not run. We then create a while loop that checks if we are not connected to Wi-Fi, to begin connecting to it. We then use `status = WiFi.begin(ssid, pass);` to start connecting to WiFi, and a delay of 10 seconds to give it enough time to connect.

Finally, we will print a simple line, and call on the `printData()` function. This function contains information regarding the connection.

```arduino
void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial);

  // attempt to connect to Wifi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to network: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  // you're connected now, so print out the data:
  Serial.println("You're connected to the network");

  Serial.println("----------------------------------------");
  printData();
  Serial.println("----------------------------------------");
}
```

The loop is very easy: it only executes the `printData()` function every 10 seconds, and then prints a line to separate the information in the Serial Monitor.

```arduino
void loop() {
  // check the network connection once every 10 seconds:
 delay(10000);
 printData();
 Serial.println("----------------------------------------");
}
```

The final step of this code is to create the `printData()` function, that we have used in both the setup and loop.

The function is quite basic, it simply prints out three different types of information:
- Board's IP address.
- Name of network connected to.
- Signal strength.

This information is then printed in the Serial Monitor.

```arduino
void printData() {
  Serial.println("Board Information:");
  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  Serial.println();
  Serial.println("Network Information:");
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.println(rssi);

}
```

## Complete Code

If you choose to skip the code building section, the complete sketch can be found below. Upload the sketch to the board.

>**Note:** You will still need to create a secrets tab yourself and add your credentials if you copy this code.

```arduino
#include <WiFiNINA.h>

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int status = WL_IDLE_STATUS;     // the Wifi radio's status

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial);

  // attempt to connect to Wifi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to network: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  // you're connected now, so print out the data:
  Serial.println("You're connected to the network");
  
  Serial.println("----------------------------------------");
  printData();
  Serial.println("----------------------------------------");
}

void loop() {
  // check the network connection once every 10 seconds:
 delay(10000);
 printData();
 Serial.println("----------------------------------------");
}

void printData() {
  Serial.println("Board Information:");
  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  Serial.println();
  Serial.println("Network Information:");
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.println(rssi);

  byte encryption = WiFi.encryptionType();
  Serial.print("Encryption Type:");
  Serial.println(encryption, HEX);
  Serial.println();
}
```

>**Note:** You will still need to create a secrets tab yourself and add your credentials if you copy this code.

## Testing It Out

When the sketch has been successfully uploaded, open the Serial Monitor and the results should match the following images. Note that the network information in this example is greyed out for security reasons.

**If you are using the OFFLINE editor, it will look like this:**

![Network information (offline editor).](assets/mkr_tutorial_02_img_06.png)

**If you are using the ONLINE editor, it will look like this:**

![Network information (online editor).](assets/mkr_tutorial_02_img_07.png)

Congratulations, you have not only connected your board to your Wi-Fi network, but you have also retrieved information from the network. One particularly good feature is the signal strength (rssi). One experiment you can do, is to try to move your MKR WiFi 1010 board close to the router and observe the Serial Monitor.

### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- We have not updated the latest firmware for the board.
- We have not installed the Board Package required for the board.
- We have not installed the WiFiNINA library.
- We have not entered the SSID and PASS: remember, it is case sensitive.
- We have not selected the right port to upload: depending on what computer we use, sometimes the board is duplicated. By simply restarting the editor, this issue can be solved.

## Conclusion

In this tutorial, we have learned how to simply connect to a Wi-Fi network by using the credentials in the code. We also learned how to obtain specific information regarding our connection, such as signal strength, IP address and name of our network.

Now that you have learned a little bit how to use the **WiFiNINA** library, you can try out some of our other tutorials for the MKR WiFi 1010 board. You can also check out the [WiFiNINA](https://www.arduino.cc/en/Reference/WiFiNINA) library for more examples and inspiration for creating wireless projects!

