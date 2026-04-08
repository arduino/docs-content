---
title: Custom AI Models for Arduino App Lab
description: This tutorial teaches you how to create and train your own AI models to customize your App Bricks.
author: Christopher Méndez
hardware:
  - hardware/uno/boards/uno-q
tags: [SBC, Linux, Debian, AI, Model]
difficulty: beginner
---

## Overview

Predefined models offer a powerful starting point for understanding edge AI. In this tutorial, we will extend those capabilities by engineering and deploying our own custom machine learning models. By moving to a custom workflow, we can empower our Arduino App Lab applications to handle specialized tasks and unique datasets, allowing the system to be tailored to our specific project goals.

![Custom AI models](assets/thumbnail-new.png)

By training your own models, you gain precise control over classification parameters and performance metrics, ensuring the system meets the specific requirements of your deployed environment rather than relying on generic solutions.

## Goals

* **Collect** a custom dataset for audio or image-related models.
* **Train** a model from scratch in Edge Impulse Studio.
* **Integrate** your custom model into Arduino App Lab to customize your Bricks.

## Required Hardware and Software

### Hardware Requirements

* [Arduino UNO Q](https://store.arduino.cc/products/uno-q) (x1)
* USB Camera for image-based AI models
* USB microphone for audio-based AI models

### Software Requirements

- [Arduino App Lab](https://www.arduino.cc/en/software/#app-lab-section)
- Arduino Account (also used for Edge Impulse Studio)

## Machine Learning

To set the context, we need to understand what an "AI Model" actually is.

In the world of traditional programming, we write explicit rules: *If button A is pressed, turn on LED B.*
In **machine learning**, we don't write rules; we provide examples. We show the computer 100 photos of a "Banana" and 100 photos of an "Apple," and the computer figures out the rules to tell them apart itself. The result of that learning process is an **AI Model**.

![Machine Learning](assets/ml.png)

By creating a custom model, you are essentially creating a new "brain" file that you can swap into your Arduino App Lab Bricks to change their behavior completely.

### Edge Impulse Studio

To create these custom models, we use **Edge Impulse Studio**.

![Edge Impulse Studio](assets/edge-impulse.png)

Edge Impulse is the leading development platform for embedded machine learning. Think of it as a "lab" where we prepare our AI. It handles the entire pipeline required to build a model that can run on the UNO Q.

#### The Workflow

Instead of writing code to define the neural network, you use the Studio's visual interface to guide the process:

![Edge Impulse workflow](assets/workflow-2.png)

1.  **Data Acquisition:** This is the most critical step. You collect/import images or audio samples to Edge Impulse. You can do this by using your mobile phone, your computer, or even capturing data directly from the UNO Q.
2.  **Labeling:** Once your data is uploaded, you must assign a category or "label" to each sample. This step establishes the ground truth for the system, teaching it exactly which patterns correspond to which output class. Accurate and consistent labeling is essential, as it directly dictates what the model learns to recognize.
3.  **Impulse Design:** This is where you structure your "brain." You define an **Input block** (e.g., Audio or Image data), a **Processing block** (to clean up the data), and a **Learning block** (the neural network that learns the patterns).
4.  **Training:** The Studio uses its cloud servers to crunch the numbers. It will look at your data thousands of times until it learns to recognize the keywords or objects you defined.
5.  **Deployment:** Edge Impulse allows us to export the trained model specifically for the **Arduino UNO Q**, and it is imported directly into our Arduino App Lab application.

When you export for the UNO Q, you get an **.eim (Edge Impulse Model)** file. This file acts as a container, holding all the logic and trained parameters needed to run the model.

## Creating your Custom AI Model

- Inside the Arduino App Lab, navigate to **My Apps** and click on **Create New App**. Give it a name and save it.
- In your App Python file, update the `main.py` script by copying and pasting this:

  ```python
  from arduino.app_utils import App
  from arduino.app_bricks.video_objectdetection import VideoObjectDetection

  detection_stream = VideoObjectDetection(confidence=0.5, debounce_sec=0.0)

  # Register a callback for when all objects are detected
  def print_detections(detections: dict):
    for key, value in detections.items():
          for detection in value:
              entry = {
                  "content": key,
                  "confidence": f"{round(detection.get('confidence', 0) * 100)} %"
              }
              print(entry)

  detection_stream.on_detect_all(print_detections)

  App.run()
  ```

- Navigate to the Bricks section in the left Arduino App Lab menu and click on the **Add Brick** button. Select the **Video Object Detection Brick**. 

![Video Object Detection Brick](assets/app-lab-0.5.png)

- Navigate to the **AI models** tab in the Brick. The interface lists available models for your Brick, showing only the built-in Default models if no new ones have been trained.

![AI models Brick option](assets/app-lab-1.png)

- To start training your custom model, click on **Train new AI model** shown in the image above. Then, click on **Ok, let's start**.

![Start the Edge Impulse pairing](assets/app-lab-2.png)

- If this is your first time, you will be guided through the Arduino account creation or login process.

![Login Process](assets/app-lab-3.1.png)

- Your same Arduino account will be valid to log into the Edge Impulse Studio.

![Connect to Edge Impulse](assets/app-lab-5.png)

- You will be asked for permission to grant Arduino App Lab to access your Edge Impulse account.

![Edge Impulse permission](assets/app-lab-5.5.png)

- With your Arduino account and Edge Impulse now connected, click on the **Start to Train your AI Model** button.

![Start to train your AI model](assets/app-lab-6.png)

- Now, you should be redirected to the Edge Impulse Studio.

![Edge Impulse Studio](assets/app-lab-7.1.png)

### Image-Based Models

To create a machine vision model for detecting objects or classifying images, follow the steps below:

#### New Project:

Create your first project by navigating to your profile picture (in the top-right corner) and clicking on **Create new project**. Select a name that resonates with your project’s objectives.

![New project creation](assets/app-lab-8.png)

#### Classes:

Define the classes your model should detect (e.g., apple, banana). We will use them in the labeling process just before creating the dataset.

#### Dataset:

To train your model, you first need data. Start by creating a dataset of the objects you want to detect.

From your project **Dashboard**, click on **Collect new data**. You can build your dataset using your phone, computer, or the UNO Q itself, or by uploading existing images directly.

![Collecting new data](assets/app-lab-9.png)

For our convenience, we will use a smartphone. Scan the QR code to open the link, select the **Camera** option, and grant the necessary permissions.

![QR code to connect your phone](assets/app-lab-10.png)

Capture a variety of images for the classes you want to detect (e.g., apples and bananas). Additionally, Edge Impulse will automatically create a class called **background** to teach the model what to ignore based on your pictures.

![Apples and Bananas dataset](assets/app-lab-11.png)

***Note: You can label your images as you capture them, or label them later using the Edge Impulse labeling tools.***

#### Impulse Design

Create your Impulse in the **Create impulse** section. Here you will define your model settings:

![Impulse design](assets/app-lab-12.png)

- **Image resolution:** 320x320 pixels in this case 
- **Processing block:** Image
- **Learning block:** Object Detection (Images)

Click on **Save Impulse** and navigate to the _Image processing block_. Leave the **Color depth** parameter as `RGB`, then click on _Save parameters_ and finally on _Generate features_.

![Image processing block](assets/app-lab-13.gif)

#### Neural Network Tuning

Getting the right settings for your Neural Network takes time and trial and error. Follow the steps below for this model:

- Navigate to the Object detection block in the left menu.
- Change the model to **MobileNetV2 SSD FPN-Lite 320x320** by clicking on "Choose a different model".

![Available models](assets/app-lab-14.gif)

- Click on **Save & Train** with the default settings and wait for the training performance results.

![Training results](assets/app-lab-15.png)

**Optimize Training Cycles:** 

The default is set to **25 cycles**. Monitor the training output.
- If the accuracy hits a plateau or the validation loss stops decreasing significantly by epoch 15 or 20, you can **reduce** the cycles to save time on future runs.
- If the accuracy is still climbing or the loss is still dropping when the process hits epoch 25, **increase** the number of cycles (e.g., to 40 or 50) to allow the model to finish learning.

**Refine the Learning Rate:** 

This model uses a high default learning rate of **0.15**.
- If the loss graph is volatile (jumping up and down wildly) or the model fails to converge, the model might be "overshooting" the optimal weights. **Reduce** the learning rate (e.g., try `0.1` or `0.05`).
- If the training is stable but the accuracy remains poor, you can try slightly **increasing** it, but be careful as this model is sensitive to high rates.

**Prevent Overfitting:** 

By default, **Data augmentation** is **disabled**.
- If your model performs perfectly on the training data (high accuracy) but fails when you point the camera at real objects (low real-world performance), the model is "overfitting."
- To fix this, **enable** Data augmentation. It randomly transforms your images during training, forcing the model to learn general features rather than memorize exact pixel values.

**Check On-Device Constraints:** 

Object Detection models like SSD are computationally heavy.
- **Inferencing time:** Verify that the inference time is low enough for your application (e.g., <500ms for ~2 FPS).
- **Hardware limits:** Ensure your device has enough RAM to hold the model. If you see warnings that the model is too large for your MCU, verify that your specific hardware (like the Arduino UNO Q) has the memory required to run it.

In our case, the default settings gave us good results and converged:

- **Inferencing Time:** 370 ms
- **Flash Usage:** 11 MB

![Training graphs](assets/app-lab-16.png)

You can clone the model used in this tutorial from [here](https://studio.edgeimpulse.com/public/846966/live). 

***This is an example model with a very small dataset created for demonstration purposes. You can improve it by modifying it.***

**Impulse Design Effect:**

In the Edge Impulse project you will find another impulse design called `Impulse #2`. We set this one up to illustrate a point.

![New performance results](assets/app-lab-25.png)

This Impulse has the following settings:

- **Resolution:** 96x96 pixels
- **Neural Network architecture:** FOMO (Faster Objects, More Objects) MobileNetV2 0.35

Notice that the training result is shown as a confusion matrix and with these settings we have accomplished a very different performance:

- **Inferencing Time:** 3 ms
- **Peak RAM Usage:** 887.1 kB
- **Flash Usage:** 102.1 kB

***A key advantage of this model is that it uses lower-resolution input images, which significantly reduces the computational resources required for inference. Additionally, unlike traditional object detection that provides bounding boxes, FOMO is optimized to locate the center point (centroid) of detected objects.***

#### Model Testing

To test your model's performance with new data, use the **Live classification** and **Model testing** sections. These tools allow you to verify how well your model detects apples and bananas in images that were not used during the training process.

![Live classification](assets/app-lab-17.png)

You can also test your model on your smartphone using the same QR code we used to create the dataset (also found in the **Deployment** section). This time, tap on **Switch to classification mode** and wait for the model to download and start. Finally, use the camera to search for some apples and bananas.

![Model running on phone](assets/app-lab-18.png)

***With your model already tested and validated, __go back to the Arduino App Lab__.***

## Custom AI Model Usage

Once you return to the Arduino App Lab, your new model will appear in your Brick's available models list. 

![Custom model selection](assets/app-lab-21.1.png)

To use it in your App, click on the **Install** button and wait for it to be built and installed on your Arduino UNO Q.

![Model installation](assets/app-lab-22.1.png)

Finally, you can select your new model by clicking on your **Brick Configuration** button.

![Model selection](assets/app-lab-23.1.png)

### Running the App

Now, run your App, and it will be using your custom AI model to detect apples and bananas.

![Run the App](assets/final-image.png)

***In the Python console you will see the detection logs and their confidence.***

Also, you can preview your cameras live feed and see the model running in real-time by navigating to `<UNO-Q-IP-ADDRESS>:4912` in your favorite browser.

![Image of the Edge Impulse live feed](assets/fruits-detector.gif)

## Conclusion

In this tutorial, you learned how to extend the capabilities of Arduino App Lab by engineering and deploying custom AI models using Edge Impulse Studio. You explored the complete machine learning pipeline—from collecting a custom dataset of images to training a MobileNetV2 SSD object detection model optimized for the Arduino UNO Q.

Thanks to the seamless integration between Arduino App Lab and Edge Impulse, you can now swap generic "models" for specialized ones, enabling your Bricks to recognize specific objects like apples and bananas with high precision. This transforms your UNO Q from a simple computer into a tailored edge AI device capable of solving unique, real-world problems.

## Next Steps

* Expand your current dataset with more samples and variations (lighting, angles) to improve your object detection model's accuracy and robustness.
* Try creating an audio classification model using a USB microphone to teach your UNO Q to recognize voice commands or environmental sounds.
* Integrate your new custom model into a Logic flow within App Lab to trigger specific actions, such as turning on an LED or sending a notification, when a specific object is detected.
* Export the `.eim` file manually from Edge Impulse to experiment with running your custom model in C++ or Python projects outside of Arduino App Lab.



