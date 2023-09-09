---
title: No Data Image Classification with Remyx AI
difficulty: beginner
tags: [Machine Learning, Remyx AI, TinyML, Tensorflow]
description: This tutorial teaches you how to create a machine learning model without data using Remyx AI to classify images on the Arduino Nicla Vision.
author: Terry Rodriguez & Salma Mayorquin
---

## Overview 
This tutorial teaches you how to train a custom machine learning model with Remyx AI and to do image classification on the Arduino Nicla Vision. The Machine Learning (ML) model will use the TensorFlow Lite format and run on OpenMV.

## Goals

- Learn how to create a model with Remyx AI
- Learn how to use OpenMV to run a classification example
- Learn how to embed a ML model in the OpenMV firmware

## Required Hardware and Software

- [Nicla Vision board](https://store.arduino.cc/products/nicla-vision)
- Micro USB cable
- A [Remyx AI](https://engine.remyx.ai/) account for training the ML model
- Up to 5 objects you'd like to classify. Objects commonly found on the internet will work well. 

This example will use the labels `empty tent interior` and `dog` for a dog presence classifier.

## Machine Learning on the Edge
Machine learning has been a common practice on powerful computers, but it is a relatively new territory when it comes to microcontrollers. Although these smaller devices might struggle with high-speed, high-resolution tasks, they offer many benefits. For example, they can run on low power for extended periods, and they can operate without an internet connection, ensuring data privacy. Microcontrollers can even be set to activate only when a sensor detects activity, making them an excellent choice for battery-powered devices.

## The Remyx AI Platform
Remyx AI is a platform that allows anyone to create a custom vision model without data or machine learning expertise required. The engine applies state-of-the-art automatic data labeling, generative AI, and model training to minimize the upfront requirements of getting started. This training method may also provide more privacy as your data will not be collected and used for training.

### 1. Create your ML Model
Using the Remyx Engine to create a custom image classifier is very straightforward. Chat with the Remyx Agent found in the Home tab and describe your project. Include information about your chosen device, in this case, the Arduino Nicla Vision, and define the labels you want to classify. Here's an example:

> I'm making a dog presence project using the Arduino Nicla Vision. The Arduino needs to differentiate between an empty tent interior and a dog. Name my model DoggyTentExample.

![Chat with the Remyx Agent to create your model.](assets/remyx_chat.gif)


### 2. Test the Model
Training takes around 30 minutes for this example. Soon, you'll see your model's progress on the Home or Dashboard tab. When it's done, click to see more details. To run a quick test, go to "Predictions" on the dashboard, click "Options" and then "Run model in browser". Drop a test image and see the result.

![View, test, and download your model](assets/remyx_dashboard.gif)

## Using the ML Model

The ML model is trained and converted to be used with microcontrollers. Download your model from the dashboard by clicking "Options" then "Download" and choosing "TFLite".

### Deploy
![Flash your TFLite model using the OpenMV IDE](assets/deployment.gif)

Make sure you have OpenMV IDE and can connect to your Nicla Vision. Copy the downloaded model.tflite model into the Nicla Vision's drive. Open the following python script in the OpenMV editor. Update the labels as needed for your application.

```python
import sensor, image, time, tf

# Initialize and configure the sensor
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# Load the TFLite model
net = tf.load('model.tflite', load_to_fb=True)  # Change the path

# Create a clock object to track the FPS
clock = time.clock()

while True:
    clock.tick()

    # Capture image
    img = sensor.snapshot()

    # Run the TFLite classifier (adjust the input/output tensor as needed)
    obj = net.classify(img, min_scale=1.0, scale_mul=0.5, x_overlap=0.0, y_overlap=0.0)
    # Note: The classify() method's arguments can vary depending on the model,
    # refer to the OpenMV documentation for details.

    # Get classification results
    if obj:
        prediction = obj[0].output()  # This will be a list if you have multiple output nodes in your neural network
        label = prediction.index(max(prediction))
        confidence = max(prediction)
        label = 'Dog' if label else 'Tent Interior'

        # Draw a box around the object and label it
        img.draw_rectangle(obj[0].rect())
        img.draw_string(obj[0].x()+8, obj[0].y()-3, str(label) + ' ' + '{:.2f}'.format(confidence), scale=2.0, mono_space = False)

    print("FPS:", clock.fps())
```

Put the board in bootloader mode and click on the connect symbol in the OpenMV IDE. Finally, press the run button at the bottom left of the IDE to see the streaming inference results from the camera!


## Conclusion

You've created and deployed a custom TFLite machine learning model to your board! 🎉

