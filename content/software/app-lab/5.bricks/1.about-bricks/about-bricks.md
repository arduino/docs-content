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

**Bricks** are the modular building blocks of an Arduino App Lab application. They package complex features—such as machine learning models, web interfaces, or database integrations—into reusable components. Add a Brick to your App and use it with a few lines of Python.

## Quick Links

Depending on your goal, jump directly to the relevant documentation:

- **[Add and Use Bricks](../use-bricks/)**: Learn how to add existing Bricks via the UI and wire them up in your Python code.
- **[Create Custom Bricks](../custom-bricks/)**: Learn how to author your own Custom Bricks to package your specialized Python logic or external Docker containers.
- **[Bricks Technical Reference](../bricks-reference/)**: Understand the background execution model, thread lifecycle, and YAML schemas.

## About Bricks

Bricks save time by handling heavy infrastructure and background tasks automatically. Instead of setting up complex machine learning environments, configuring databases, or writing socket servers, you instantiate a Brick, and the Brick handles the setup.

Technically, a **Brick** is a Python module that interacts with your main application. Bricks run in one of two ways:

- **Pure Python Bricks:** These run entirely inside your App's Python environment. They provide utility functions, compute logic, or cloud connections without launching additional containers.
- **Containerized Bricks:** These act as Python bridges to isolated **Docker containerized services** running in the background. Your application script (`main.py`) interacts with the Brick's Python API, which handles any necessary network communication with the underlying container.

While App Lab provides a wide catalog of pre-built Arduino Bricks, you can also create **Custom Bricks** directly within your application. Custom Bricks use the exact same architecture as pre-built Bricks, allowing you to package your own specialized Python logic or third-party Docker containers into modular, reusable components.

## How Bricks Work (Orchestration and Infrastructure)

When you add a Brick to your App via the App Lab interface, the system automates several steps:

1. **Configuration:** App Lab registers the Brick in your application's `app.yaml` file, together with its variables and selected AI model.
2. **Environment Preparation:** When the App starts, the `arduino-app-cli` orchestrator on the board downloads the container images and AI models the Bricks need, creates a private network for the App, and starts the containers.
3. **Python Path Integration:** The orchestrator adds the `bricks/` directory to the Python `sys.path`, allowing you to import your Custom Bricks by their folder name.
4. **Communication:** A Brick's Python API runs inside your App's Python process. Containerized Bricks talk to their containers over the App's private network, so your code never has to deal with the network directly.
5. **Execution:** The `App.run()` call at the bottom of your script starts the Bricks you have instantiated and keeps the App running.

<Alert type="info">

**Note:** Some containerized Bricks require an active internet connection during their first deployment so the board can download the necessary Docker images from the registry.

</Alert>

## List of Bricks

<!-- app-bricks-py table start -->
| Brick | Boards | Description | Source |
| --- | --- | --- | --- |
| Air Quality Monitoring | All | Online air quality monitoring module for Arduino using aqicn.org. Requires an internet connection. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/air_quality_monitoring) |
| Arduino Cloud | All | Connects to Arduino Cloud | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/arduino_cloud) |
| Audio Classification | All | Brick for audio classification using a pre-trained model. It processes audio input to classify different sounds. Brick is designed to work with pre-trained models provided by framework or with custom audio classification models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/audio_classification) |
| Automatic Speech Recognition (ASR) | VENTUNO Q | Automatic Speech Recognition brick for offline speech-to-text processing | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/asr) |
| Camera Code Detection | All | Scans a camera for barcodes and QR codes | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/camera_code_detection) |
| Cloud ASR | All | Cloud ASR Brick provides a unified and flexible way to connect cloud-based Automatic Speech Recognition (ASR) services and transform spoken audio into text. It enables real-time, streaming transcription from a connected microphone, leveraging leading cloud providers to deliver low-latency speech-to-text processing. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/cloud_asr) |
| Cloud LLM | All | Cloud LLM Brick enables seamless integration with cloud-based Large Language Models (LLMs) for advanced AI capabilities in your Arduino projects. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/cloud_llm) |
| Database - SQL | All | Simplified database storage layer for Arduino sensor data using SQLite local database. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/dbstorage_sqlstore) |
| Database - Time Series | All | Simplified time series database storage layer for Arduino sensor samples built on top of InfluxDB. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/dbstorage_tsstore) |
| Gesture Recognition | VENTUNO Q | This gesture recognition brick utilizes a pre-trained model to analyze video streams from a camera. The output is a video stream featuring gesture recognition as overlay, with the added capability to trigger actions based on these detections. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/gesture_recognition) |
| Image Classification | All | Brick for image classification using a pre-trained model. It processes images and returns the predicted class label and confidence score. Brick is designed to work with pre-trained models provided by framework or with custom image classification models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/image_classification) |
| Keyword Spotting | All | Brick for keyword spotting using a pre-trained model. It processes audio input to detect specific keywords or phrases. Brick is designed to work with pre-trained models provided by framework or with custom audio classification models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/keyword_spotting) |
| Large Language Model (LLM) | UNO Q, VENTUNO Q | Large Language Model (LLM) Brick enables seamless integration with locally hosted LLMs for advanced AI capabilities in your Arduino projects. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/llm) |
| MCP Client | All | This brick helps you connect to the MCP server and send/receive messages. It provides a simple interface for communication with the MCP server, allowing you to easily integrate it into your Arduino projects. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/mcp_client) |
| Mood Detection | All | This brick analyzes text sentiment to detect the mood expressed. It classifies text as positive, negative, or neutral. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/mood_detector) |
| Motion detection | All | This Brick is designed for motion detection and recognition, leveraging pre-trained models. It takes input from accelerometer sensors to identify various motion patterns. You can use it with pre-trained models provided by the framework or with your custom motion classification models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/motion_detection) |
| Object Detection | All | Brick for object detection using a pre-trained model. It processes images and returns the predicted class label, bounding-boxes and confidence score. Brick is designed to work with pre-trained models provided by framework or with custom object detection models trained on Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/object_detection) |
| Pose Estimation | VENTUNO Q | This pose estimation brick analyzes a camera video stream and detects the body poses of up to 10 people at a time, locating 17 keypoints per person (eyes, ears, nose, shoulders, elbows, wrists, hips, knees, ankles). The output is a video stream featuring the skeleton overlay, with the added capability to trigger actions based on the detected poses, people presence and people count. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/pose_estimation) |
| Sound Generator | All | Generate sounds like notes, tones, or melodies using waveforms. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/sound_generator) |
| Telegram Bot | All | A brick to interact with Telegram Bot API | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/telegram_bot) |
| Text-to-Speech (TTS) | VENTUNO Q | Text-to-Speech brick for offline speech synthesis | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/tts) |
| TPS | All | Collects nearby Wi-Fi access points and determines device location using the Qualcomm TPS Location API cloud service | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/tps) |
| Vibration Anomaly detection | All | This Brick is designed for vibration anomaly detection and recognition, leveraging pre-trained models. It takes input from sensors (accelerometer) to identify possible anomalies based on vibration patterns. You can use it with pre-trained models provided by the framework or with your own custom anomaly detections models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/vibration_anomaly_detection) |
| Video Image Classification | All | This image classification brick utilizes a pre-trained model to analyze video streams from a camera. It identifies objects, returning their predicted class labels and confidence scores. The output is a video stream featuring classification as overaly, with the added capability to trigger actions based on these detections. It supports pre-trained models provided by the framework and custom object detection models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/video_imageclassification) |
| Video Object Detection | All | This object detection brick utilizes a pre-trained model to analyze video streams from a camera. It identifies objects, returning their predicted class labels, bounding boxes, and confidence scores. The output is a video stream featuring bounding boxes around detected objects, with the added capability to trigger actions based on these detections. It supports pre-trained models provided by the framework and custom object detection models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/video_objectdetection) |
| Vision Language Model (VLM) | VENTUNO Q | Vision Language Model (VLM) Brick enables seamless integration with locally hosted VLMs for advanced AI capabilities in your Arduino projects. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/vlm) |
| Visual Anomaly Detection | All | Brick for visual anomaly detection using a pre-trained model. It processes images to identify unusual patterns and returns detected anomalies with bounding boxes.  Supports pre-trained models provided by the framework or custom anomaly detection models trained on the Edge Impulse platform. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/visual_anomaly_detection) |
| Wave Generator | All | Continuous wave generator for audio synthesis. Generates sine, square, sawtooth, and triangle waveforms with smooth frequency and amplitude transitions. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/wave_generator) |
| Weather Forecast | All | Online weather forecast module for Arduino using open-meteo.com geolocation and weather APIs. Requires an internet connection. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/weather_forecast) |
| WebUI - HTML | All | A user interface based on HTML and JavaScript that can rely on additional APIs and a WebSocket exposed by a web server. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/web_ui) |
| WebUI - Streamlit | All | A simplified user interface based on Streamlit and Python. | [GitHub](https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/streamlit_ui) |

<!-- app-bricks-py table end -->

## Next Steps

- [Use Bricks in Your App](../use-bricks/)
