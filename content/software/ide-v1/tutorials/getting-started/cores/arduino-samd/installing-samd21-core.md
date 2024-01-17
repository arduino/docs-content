---
title: 'Installing the SAMD21 core for MKR boards'
compatible-products: [mkr-1000-wifi, mkr-zero, mkr-wifi-1010, mkr-fox-1200, mkr-wan-1300, mkr-wan-1310, mkr-nb-1500, mkr-vidor-4000, nano-33-iot, zero]
difficulty: beginner
description: 'A step-by-step guide to install the core needed for the MKR Family, Zero and Nano 33 IoT boards.'
author: 'Karl Söderby'
---

## Installing the SAMD21 core for MKR boards

In this tutorial, we will go through a few simple steps on installing the **SAMD21** core. This installation is necessary to use your board with the offline Arduino IDE.

This tutorial uses the **Arduino IDE**. You can download the editor easily from [our software page](https://www.arduino.cc/en/software).

If you are using the **Web Editor**, you can follow the [getting started with the Web Editor tutorial](/cloud/web-editor/tutorials/getting-started/getting-started-web-editor).


### Boards using the SAMD21 core

- MKR Zero
- MKR WiFi 1000
- MKR WiFi 1010
- MKR FOX 1200
- MKR WAN 1300
- MKR WAN 1310
- MKR GSM 1400
- MKR NB 1500
- MKR VIDOR 4000
- Arduino Nano 33 IoT
- Arduino Zero

### Downloading and installing

1. First, we need to download the Arduino IDE, which can be done from the [software page](https://www.arduino.cc/en/software).

2. Install the Arduino IDE on your local machine.

3. Open the Arduino IDE.

### Installing the SAMD core

After we have downloaded, installed and opened the Arduino IDE, let's continue to installing the SAMD21 core.

When we open the editor, we will see an empty sketch.

![An empty Arduino IDE sketch window.](assets/install_samd21_img01.png)

Here we need to navigate to **Tools > Board > Board Manager**.

![Selecting board manager.](assets/install_samd21_img02.png)

This will open up a new window, with all available cores. Type in `"samd"` in the search field, and install the **Arduino SAMD Boards (32-bits ARM Cortex-M0+)** core.

![List of cores.](assets/install_samd21_img03.png)

This process may take some time, and you may need to accept the installation window that comes up (depending on your operative system). When it is finished, it should say `"INSTALLED"` under the title.

>**Note:** This process may take several minutes.

Exit the board manager, and go to **Tools > Board > Arduino SAMD Boards (32-bits ARM Cortex-M0+)**. Here you can see all the SAMD boards listed, where you can select the MKR board you are using. You have now successfully installed the core.

![List of available boards.](assets/install_samd21_img04.png)

### Selecting the port

Now, let's make sure that our board is found by our computer, by selecting the port. Regardless what kind of program we are uploading to the board, we **always** need to choose the port for the board we are using. This is simply done by navigating to **Tools > Port**, where you select your board from the list.

![Selecting the right board and port.](assets/install_samd21_img05.png)

This will look different depending on what kind of operative system you are using.

For **Windows** users, it could look like this:

- `<COM29> (Arduino MKR WiFi 1010)`

For **MAC** users, it could look like this:

- `/dev/cu.usbmodem14112 (Arduino MKR WiFi 1010)`

### Uploading a simple example

You are now ready to start using your board! The easiest way to check that everything is working, is to upload just a simple blink example to your board. This is done by navigating to **File > Examples > 01.Basics > Blink**.

![Selecting the blink example.](assets/install_samd21_img06.png)

To upload the sketch, simply click on the arrow in the top left corner. This process takes a few seconds, and it is important to not disconnect the board during this process.

![Uploading the sketch.](assets/install_samd21_img07.png)

When the code is uploaded, the text `"Done uploading."` is visible in the bottom left corner.

If you look closely at your board, you will notice an orange LED blink with an interval of one second. This means you have successfully uploaded a program to your board.

