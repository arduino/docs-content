---
title: 'Cloud Editor (New)'
description: 'Get started with the Cloud Editor, an online IDE in the Arduino Cloud.'
author: 'Karl Söderby'
---

The [Cloud Editor](https://app.arduino.cc/sketches/) is an online code editor that is part of the [Arduino Cloud](https://app.arduino.cc/). With the Cloud Editor, you can write sketches that are automatically stored in your Cloud sketchbook, and upload them to your Arduino board.

The Cloud Editor features all the necessary tools to develop and test your Arduino projects, including:
- A compiler that checks that your code works on the specified board,
- an upload tool that uploads a sketch to your board,
- the Serial Monitor, a tool that reads the serial commands send from your board,
- all board packages & libraries available without download!

***To use the Cloud Editor, you will need to [install the Cloud Agent](), a plugin that allows your browser to access USB devices (your board). You will also need an [Arduino account](). The steps are covered later on in this guide.***

## Hardware & Software Needed

- [Cloud Agent](https://create.arduino.cc/getting-started/plugin/welcome)
- Arduino board (all Arduino boards are supported).
- USB cable (different depending on the board you are using).

## Setup

1. First, log in or create an [Arduino account]().
2. Then install the [Cloud Agent](https://create.arduino.cc/getting-started/plugin/welcome).
3. After installing the Cloud Agent, navigate to the [Cloud Editor](https://app.arduino.cc/sketches/).
4. Now connect an Arduino board to your computer. Once you connect it, it should show up in the editor.

    ![Connect board to computer.]()

5. Finally, let's upload a sketch to your board. Click on the **"Examples"** icon, and navigate to **01.Basics > Blink**. Clicking the example will open a new window.

    ![Select the example.]()

6. With the Blink example open, click on the **"Upload"** button. This will start the upload of the Blink sketch to your board. Do **not** disconnect the board during this process.

    ![Click on the "Upload" button.]()

7. You can see if it was successful or not in the console log window at the bottom. Here's an example of a successful upload:

    ![Successful upload.]()

8. Congratulations, you have now successfully setup and used the Cloud Editor!

## Cloud Editor Overview

Now that we are all setup, let's take a look at the main components of the editor:

![Cloud Editor overview.](assets/editor-overview.png)

1. **Arduino Cloud Menu** - navigation menu for the Arduino Cloud platform.
2. **Examples** -  a set of basic Arduino examples.
3. **[Libraries](#)** - all libraries that are included in the Arduino library manager (5000+).
4. **Reference** - the Arduino Reference provides an overview of the available methods in the Arduino programming API.
5. **Editor** - the code editor area, where we write the program for our board.
6. **Console Log** - this window informs you of the status of your compilation / upload. 
7. **Verify/Upload** - verify (compile) your code using the checkmark button, and upload it to your board using the right arrow. 
8. **Board Selection** - the board connected to your computer will be automatically displayed here. You can also manually change this.
9. **Serial Monitor** - a tool that reads serial data sent from your board to the computer. 

## Serial Monitor

The Serial Monitor is a tool that allows you to read serial data from your board. This is useful for any general debugging cases, such as checking if a block of code is executed, or making sure the values you are using are accurate.

To use the tool, you will need a board connected to your computer that sends serial data. You can for example use the **Examples > 01.Basics > AnalogReadSerial** example to test it out.

When clicking the Serial Monitor button, a new window will open, where you will receive the data. See the image below for a complete overview of its functions:

![Serial Monitor.]()

1. 

## Resources

The resources (examples, libraries & reference) are all available from the menu on the left hand side. 

### Examples

The examples found 

### Libraries

### Reference

The reference is an embedded version of the [Arduino Language Reference]().