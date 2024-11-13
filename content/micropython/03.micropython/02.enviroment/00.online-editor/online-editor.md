---
title: 'Arduino Lab for MicroPython (online)'
description: 'The Arduino Lab for MicroPython is an online code editor for writing and loading MicroPython scripts.'  
author: 'Karl Söderby'  
---

The [Arduino Lab for MicroPython]() is an online code editor that allows you to load MicroPython scripts to your Arduino board. This editor is part of the [Arduino Cloud](), and is free to use for everyone.

In this tutorial, we will take a look at how we can access it, and test out it out by writing a simple script.

***Note that this tutorial does not go in depth on how the Arduino Lab for MicroPython work. For more details, you can visit the [guide to the Arduino Lab for MicroPython]().***

## Requirements

- **Google Chrome** - this is currently the only supported browser.
- [Arduino Cloud account registered]()
- [A MicroPython compatible board]()

## Setting Up

***To follow these steps, you will need to have MicroPython installed on your board. Haven't done this yet? Don't worry, check out the [Installing MicroPython]() guide.***

Setting up the online environment is quick and easy. Follow the steps below to achieve it:

1. Go to [Arduino Cloud](https://app.arduino.cc/) and log in / create an account.
2. Navigate to [lab-micropython.arduino.cc](https://lab-micropython.arduino.cc/). This is accessible through the cloud interface, under **Resources > Online Lab for MicroPython**.
   ![Navigate to the editor.](assets/online-editor-access.png)
3. Click on the **"Connect"** button, and select our board from the list.
   ![Select your board](assets/connect-board.png)
4. With the board connected, in the text area, copy and paste the following:
   ```python
   print("Hello World!")
   ```

We should now see `Hello World!` printed in the REPL.

## Troubleshooting

- If the "RUN" button is faded out, it means the board is not connected. Click the "Connect" button to get a list of available boards connected.
- Make sure MicroPython is installed on your board.
- If you have recently installed MicroPython on your board, try resetting the board by pressing the reset button (once), or disconnect & reconnect the USB cable.

