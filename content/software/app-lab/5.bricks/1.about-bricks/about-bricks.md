---
title: About Bricks in Arduino App Lab
description: Learn about Bricks, the modular building blocks that provide pre-packaged AI models and functionalities for your Apps.
overwriteSidebar: About Bricks
tags:
  - Bricks
  - AI
  - IoT
  - Modular
---

Bricks are the modular building blocks of the Arduino App Lab ecosystem. They allow you to add complex functionalities—such as machine learning models, web servers, or cloud connectors—to your applications without writing thousands of lines of code from scratch.

## What is a Brick?

A **Brick** is a pre-configured service or Docker container that runs on the board's Linux environment. Each Brick provides a specific set of capabilities that your Python script (`main.py`) can interact with through a high-level API.

## How Bricks Work

When you add a Brick to your App via the App Lab interface, the IDE performs the following actions:

1. **Configuration:** Adds the Brick's unique identifier to your `app.yaml` manifest.
2. **Deployment:** Ensures the necessary Docker image is present on the board's microprocessor.
3. **Integration:** Makes the corresponding Python library available for import in your `main.py` file.

<Alert type="info">**Note:** Most Bricks require your board to have an active internet connection during the first deployment to download the necessary Docker images from the Arduino registry.</Alert>

<!-- TODO: Verify current status -->

## List of Bricks

<!-- app-bricks-py table start -->
| Brick | Description | Source |
| --- | --- | --- |
| Air Quality Monitoring | Online air quality monitoring module for Arduino using aqicn.org. Requires an internet connection. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/air_quality_monitoring) |
| Arduino Cloud | Connects to Arduino Cloud | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/arduino_cloud) |
| Audio Classification | Brick for audio classification using a pre-trained model. It processes audio input to classify different sounds. Brick is designed to work with pre-trained models provided by framework or with custom audio classification models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/audio_classification) |
| Automatic Speech Recognition (ASR) | Automatic Speech Recognition brick for offline speech-to-text processing | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/asr) |
| Camera Code Detection | Scans a camera for barcodes and QR codes | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/camera_code_detection) |
| Cloud ASR | Cloud ASR Brick provides a unified and flexible way to connect cloud-based Automatic Speech Recognition (ASR) services and transform spoken audio into text. It enables real-time, streaming transcription from a connected microphone, leveraging leading cloud providers to deliver low-latency speech-to-text processing. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/cloud_asr) |
| Cloud LLM | Cloud LLM Brick enables seamless integration with cloud-based Large Language Models (LLMs) for advanced AI capabilities in your Arduino projects. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/cloud_llm) |
| Database - SQL | Simplified database storage layer for Arduino sensor data using SQLite local database. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/dbstorage_sqlstore) |
| Database - Time Series | Simplified time series database storage layer for Arduino sensor samples built on top of InfluxDB. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/dbstorage_tsstore) |
| Gesture Recognition | This gesture recognition brick utilizes a pre-trained model to analyze video streams from a camera. The output is a video stream featuring gesture recognition as overlay, with the added capability to trigger actions based on these detections. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/gesture_recognition) |
| Image Classification | Brick for image classification using a pre-trained model. It processes images and returns the predicted class label and confidence score. Brick is designed to work with pre-trained models provided by framework or with custom image classification models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/image_classification) |
| Keyword Spotting | Brick for keyword spotting using a pre-trained model. It processes audio input to detect specific keywords or phrases. Brick is designed to work with pre-trained models provided by framework or with custom audio classification models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/keyword_spotting) |
| Large Language Model (LLM) | Large Language Model (LLM) Brick enables seamless integration with locally hosted LLMs for advanced AI capabilities in your Arduino projects. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/llm) |
| Mood Detection | This brick analyzes text sentiment to detect the mood expressed. It classifies text as positive, negative, or neutral. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/mood_detector) |
| Motion detection | This Brick is designed for motion detection and recognition, leveraging pre-trained models. It takes input from accelerometer sensors to identify various motion patterns. You can use it with pre-trained models provided by the framework or with your custom motion classification models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/motion_detection) |
| MQTT Connector | MQTT connector module. Acts as a client for receiving and publishing messages to an MQTT broker. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/mqtt) |
| Object Detection | Brick for object detection using a pre-trained model. It processes images and returns the predicted class label, bounding-boxes and confidence score. Brick is designed to work with pre-trained models provided by framework or with custom object detection models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/object_detection) |
| Sound Generator | Generate sounds like notes, tones, or melodies using waveforms. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/sound_generator) |
| Telegram Bot | A brick to interact with Telegram Bot API | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/telegram_bot) |
| Text-to-Speech (TTS) | Text-to-Speech brick for offline speech synthesis | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/tts) |
| Vibration Anomaly detection | This Brick is designed for vibration anomaly detection and recognition, leveraging pre-trained models. It takes input from sensors (accelerometer) to identify possible anomalies based on vibration patterns. You can use it with pre-trained models provided by the framework or with your own custom anomaly detections models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/vibration_anomaly_detection) |
| Video Image Classification | This image classification brick utilizes a pre-trained model to analyze video streams from a camera. It identifies objects, returning their predicted class labels and confidence scores. The output is a video stream featuring classification as overaly, with the added capability to trigger actions based on these detections. It supports pre-trained models provided by the framework and custom object detection models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/video_imageclassification) |
| Video Object Detection | This object detection brick utilizes a pre-trained model to analyze video streams from a camera. It identifies objects, returning their predicted class labels, bounding boxes, and confidence scores. The output is a video stream featuring bounding boxes around detected objects, with the added capability to trigger actions based on these detections. It supports pre-trained models provided by the framework and custom object detection models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/video_objectdetection) |
| Visual Anomaly Detection | Brick for visual anomaly detection using a pre-trained model. It processes images to identify unusual patterns and returns detected anomalies with bounding boxes.  Supports pre-trained models provided by the framework or custom anomaly detection models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/visual_anomaly_detection) |
| Visual Language Model (VLM) | Visual Language Model (VLM) Brick enables seamless integration with locally hosted VLMs for advanced AI capabilities in your Arduino projects. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/vlm) |
| Wave Generator | Continuous wave generator for audio synthesis. Generates sine, square, sawtooth, and triangle waveforms with smooth frequency and amplitude transitions. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/wave_generator) |
| Weather Forecast | Online weather forecast module for Arduino using open-meteo.com geolocation and weather APIs. Requires an internet connection. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/weather_forecast) |
| WebUI - HTML | A user interface based on HTML and JavaScript that can rely on additional APIs and a WebSocket exposed by a web server. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/web_ui) |
| WebUI - Streamlit | A simplified user interface based on Streamlit and Python. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/streamlit_ui) |

<!-- app-bricks-py table end -->

## Next Steps

- [Use Bricks in Your App](../use-bricks/)
