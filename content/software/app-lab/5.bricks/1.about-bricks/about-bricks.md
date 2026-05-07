---
title: "Overview: Bricks in Arduino App Lab"
description: Learn about Bricks, the modular building blocks that provide pre-packaged AI models and functionalities for your Apps.
overwriteSidebar: Overview
tags:
  - Arduino App Lab
  - Bricks
  - AI
  - IoT
---

**Bricks** are the modular building blocks of an Arduino App Lab application. They package complex features—such as machine learning models, web interfaces, or database integrations—into reusable components. Think of them as "plug-and-play" services: instead of writing thousands of lines of code from scratch, you add a Brick to your project and interact with it using a few lines of Python.

## Quick Links

Depending on your goal, jump directly to the relevant documentation:

- **[Add and Use Bricks](../use-bricks/)**: Learn how to add existing Bricks via the UI and wire them up in your Python code.
- **[Create Custom Bricks](../custom-bricks/)**: Learn how to author your own Custom Bricks to package your specialized Python logic or external Docker containers.
- **[Bricks Technical Reference](../bricks-reference/)**: Understand the background execution model, thread lifecycle, and YAML schemas.

## About Bricks

Bricks save time by handling heavy infrastructure and background tasks automatically. Instead of setting up complex machine learning environments, configuring databases, or writing socket servers, you instantiate a Brick and let the framework handle the rest.

Technically, a **Brick** is a Python module that interacts with your main application. Bricks run in one of two ways:

- **Pure Python Bricks:** These run entirely in the board's main Python environment. They provide utility functions, compute logic, or cloud connections without launching external containers.
- **Containerized Bricks:** These act as Python bridges to isolated **Docker containerized services** running in the background. Your application script (`main.py`) interacts with the Brick's Python API, which handles any necessary network communication with the underlying container behind the scenes.

While App Lab provides a wide catalog of pre-built Arduino Bricks, you can also create **Custom Bricks** directly within your application as a local variant. Custom Bricks use the exact same architecture as pre-built Bricks, allowing you to package your own specialized Python logic or third-party Docker containers into modular, reusable components.

## How Bricks Work (Orchestration and Infrastructure)

When you add a Brick to your App via the App Lab interface, the system automates several steps:

1. **Configuration:** The orchestrator registers the Brick in your application's `app.yaml` file.
2. **Environment Preparation:** For containerized Bricks, the `arduino-app-lab` system manages the deployment, virtual network creation, and startup of all required background containers.
3. **Python Path Integration:** The orchestrator automatically adds the `bricks/` directory to the Python `sys.path`, allowing you to import your Custom Bricks seamlessly by their folder name.
4. **Communication:** Bricks communicate with your main Python application (`main.py`) via the Arduino Router. 
5. **Execution:** The `App.run()` call at the bottom of your script initializes the communication bridge and launches the background processes required by your Bricks.

<Alert type="info">**Note:** Some containerized Bricks require an active internet connection during their first deployment so the board can download the necessary Docker images from the registry.</Alert>

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
