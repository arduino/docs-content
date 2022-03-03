---
title: 'Arduino Style Guide for Creating Images'
description: 'Learn how to create clear Arduino approved images for your contributed content.'
tags: 
  - Styleguide
  - Guidelines
author: 'Josefine Hansson 4arduino'
---

This is a guide for creating clear Arduino approved screenshots, circuit diagrams and schematics for your contributed content. This can be read and used for beginners and advanced users alike. This is not a set of hard and fast rules, it's a set of guidelines. Some of these guidelines might even conflict with each other. Use your judgment on when they're best followed, and if you're not sure, ask someone who'll be learning from what you write what makes the most sense. You might also be interested in the [Writing Style Guide](/content/hacking/01.software/ArduinoStyleGuide) and [Writing Libraries](/content/hacking/01.software/LibraryTutorial) for Arduino.

This tutorial will focus on creating **circuit diagrams**, **schematics** and **screenshots** for your contributed content.

## Creating images

- Don't over-use images.
- Format images to be 1920x1080

### Suggested creation platforms

- Fritzing
- Figma

## Image styles

### Circuit Diagrams

![Example of a circuit diagram](assets/simple-circuit.png)

**Circuit diagrams** represent how Arduino products work with components in order to function. 

**Basic rules**

* Rounded wire corners are to be done in increments of 8. eg 8,16,32.
* Try to avoid wires crossing if possible, to make the circuit look tidy and keep the breadboard clear of wires.

**Wire colors**

|Color|Code|
|-----|----|
|Bronze|#9E826D|
|Teal|#008184|
|Sunflower|#F1C40F|
|Red|#FF0000|
|Green|#72D075|
|Black|#000000|
|Blue|#1D71B8|
|Orange|#F1970F|

![Colors of jumper wires](assets/jumperwires.png)

Components for the circuit diagrams can be found [here]().

### Schematics

![Example of schematic.](assets/simple-schematic.png)

A **schematic** is a stylized electronic diagram explaining electric circuits.

Standard circuit diagrams or schematics are non stylised and are used primarily by hardware engineers and programmers internally. An example of this can be seen below.

![Complex schematic.](assets/engineer-schematic.png)

The schematics for the Arduino Documentation website however are a bit more simple.

![Simple schematic.](assets/simple-schematic.png)

**Basic rules**

* The wires should be colored with brown (#9E826D) color.
* Try to avoid wires crossing if possible, to make the circuit look tidy and keep the breadboard clear of wires.

### Screenshots

![Example of screenshot.](assets/screenshot-example.png)

**Screenshots** are most often used to show the program in the Arduino IDE or any other chosen software.

When taking screenshots it's important to think of legibility, consistency and aesthetic. 

* On a Mac use cmd + shift + 4 + space bar to take a screen shot of a specific Application window.
* On a PC use a specific tool screenshot tool and take a shot of the specific Application window.

|Background color|Code|
|-----|----|
|Teal|#A5F2EE66 at 40%|

![Example browser.](assets/screenshot.png)

![Example standard IDE.](assets/standard-IDE-screenshot.png)

![Example zoomed in.](assets/zoomed-in-screenshot-on-specific-area.png)
