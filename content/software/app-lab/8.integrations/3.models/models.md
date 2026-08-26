---
title: AI Models in Arduino App Lab
overwriteSidebar: AI Models
description: An overview of all supported out-of-the-box AI models in Arduino App Lab.
author: Arduino
tags: [App Lab, AI, Models, Machine Learning]
difficulty: beginner
---

## Overview

The following tables present the AI models available out-of-the-box for Arduino App Lab. These models are declared in the App Lab models registry and are grouped by the capabilities they provide.

<!-- app-lab-models table start -->
### Vision

Camera-in models: detection, classification and anomaly spotting over image or video streams.

| Model | Boards | Description | Source |
| :--- | :--- | :--- | :--- |
| Concrete crack anomaly detection | UNO Q | Anomaly detection model to identify cracks in concrete structures. | [Edge Impulse](https://studio.edgeimpulse.com/public/800941/live) |
| Concrete crack anomaly detection - High resolution | VENTUNO Q | Anomaly detection model to identify cracks in concrete structures with higher resolution input images for improved accuracy. This version of the model is optimized for NPU acceleration on supported devices, providing faster inference times while maintaining accuracy. | [Edge Impulse](https://studio.edgeimpulse.com/public/906179/live) |
| General purpose image classification | Unrestricted | General purpose image classification model based on MobileNetV2. This model is trained on the ImageNet dataset and can classify images into 1000 categories. | [Edge Impulse](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2) |
| General purpose object classification - EfficientNet-B4 | VENTUNO Q | EfficientNetB4 is a machine learning model that can classify images from the Imagenet dataset. It can also be used as a backbone in building more complex models for specific use cases. This version of the model is optimized for NPU acceleration on supported devices, providing faster inference times while maintaining accuracy. | [Edge Impulse](https://aihub.qualcomm.com/compute/models/efficientnet_b4) |
| General purpose object detection - YoloX nano | UNO Q | General purpose object detection model based on YoloX-Nano. This model is trained on the COCO dataset and can detect 80 different object classes. | [Edge Impulse](https://github.com/Megvii-BaseDetection/YOLOX) |
| General purpose object detection - YoloX nano | VENTUNO Q | General purpose object detection model based on YoloX-Nano. This model is trained on the COCO dataset and can detect 80 different object classes. This version of the model is optimized for NPU acceleration on supported devices, providing faster inference times while maintaining accuracy. | [Edge Impulse](https://github.com/Megvii-BaseDetection/YOLOX) |
| General purpose object detection - YoloX small | VENTUNO Q | General purpose object detection model based on YoloX-Small. This model is trained on the COCO dataset and can detect 80 different object classes. This version of the model is optimized for NPU acceleration on supported devices, providing faster inference times while maintaining accuracy. | [Edge Impulse](https://aihub.qualcomm.com/models/yolox) |
| Hand gestures | Unrestricted | A lightweight vision model that detects four hand gestures: neutral fist, open hand (five), V-sign (peace), and thumbs-up (good). | [Edge Impulse](https://studio.edgeimpulse.com/public/842271/live) |
| Lightweight-Face-Detection | UNO Q | A small and accurate model for detecting bounding boxes for faces in images. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/face_det_lite) |
| Lightweight-Face-Detection | VENTUNO Q | A small and accurate model for detecting bounding boxes for faces in images. This version of the model is optimized for NPU acceleration on supported devices, providing faster inference times while maintaining accuracy. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/face_det_lite) |
| MediaPipe Hand-Gesture Recognition | Unrestricted | The MediaPipe Gesture Recognizer is a real-time machine learning pipeline that detects hands, predicts 21 hand landmarks, determines handedness (left/right), and classifies gestures from a predefined set. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/mediapipe_hand_gesture) |
| Person classification | Unrestricted | Person classification model based on WakeVision dataset. This model is trained to classify images into two categories: person and not-person. | [Edge Impulse](https://studio.edgeimpulse.com/public/755016/live) |
| PoseNet MobileNet Pose Estimation | Unrestricted | PoseNet performs real-time multi-person pose estimation, detecting up to 10 people per frame and locating 17 body keypoints (nose, eyes, ears, shoulders, elbows, wrists, hips, knees, ankles) for each person. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/posenet_mobilenet) |

### Audio & speech

Microphone-in models: wake words, sound classification, transcription and synthesis.

| Model | Boards | Description | Source |
| :--- | :--- | :--- | :--- |
| Glass breaking classifier | Unrestricted | A glass breaking classifier model to detect glass breaking sounds in audio recordings | [Edge Impulse](https://studio.edgeimpulse.com/public/749446/live) |
| Keyword spotting - Hey Arduino! | Unrestricted | A keyword-spotting model to detect the 'Hey Arduino!' in audio streams. | [Edge Impulse](https://studio.edgeimpulse.com/studio/757509/live) |
| Melo TTS (Chinese) | VENTUNO Q | MeloTTS is a high-quality multi-lingual text-to-speech library - Chinese version. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/melotts_zh) |
| Melo TTS (English) | VENTUNO Q | MeloTTS is a high-quality multi-lingual text-to-speech library - English version. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/melotts_en) |
| Melo TTS (Spanish) | VENTUNO Q | MeloTTS is a high-quality multi-lingual text-to-speech library - Spanish version. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/melotts_es) |
| Piper TTS (English) | VENTUNO Q | Piper is a high-quality multi-lingual text-to-speech library - English version. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/pipertts_en) |
| Piper TTS (German) | VENTUNO Q | Piper is a high-quality multi-lingual text-to-speech library - German version. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/pipertts_de) |
| Piper TTS (Italian) | VENTUNO Q | Piper is a high-quality multi-lingual text-to-speech library - Italian version. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/pipertts_it) |
| Whisper Small (quantized) | VENTUNO Q | Whisper ASR (Automatic Speech Recognition) model is a state-of-the-art system designed for transcribing spoken language into written text. This model is based on the transformer architecture and has been optimized for edge inference by replacing Multi-Head Attention (MHA) with Single-Head Attention (SHA) and linear layers with convolutional (conv) layers. It exhibits robust performance in realistic, noisy environments, making it highly reliable for real-world applications. Specifically, it excels in long-form transcription, capable of accurately transcribing audio clips up to 30 seconds long. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/whisper_small_quantized) |

### Language

Generative models running on-device through Genie or llama.cpp.

| Model | Boards | Description | Source |
| :--- | :--- | :--- | :--- |
| Gemma 3 1B | VENTUNO Q, UNO Q | Gemma 3 1B is an efficient AI model developed by Google DeepMind. | [Hugging Face](https://huggingface.co/unsloth/gemma-3-1b-it-GGUF) |
| Gemma 4 E2B | VENTUNO Q | Gemma 4 E2B is an efficient, open AI model developed by Google DeepMind. Activating an effective two billion parameters, it is engineered specifically for mobile and edge devices. It's optimized for offline agentic workflows. | [Hugging Face](https://huggingface.co/google/gemma-4-E2B-it-qat-q4_0-gguf) |
| Gemma 4 E4B | VENTUNO Q | Gemma 4 E4B is an efficient, open AI model developed by Google DeepMind. Activating an effective four billion parameters, it is engineered specifically for mobile and edge devices. It's optimized for offline agentic workflows. | [Hugging Face](https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-gguf) |
| Qwen 2.5-VL-7B VLM | VENTUNO Q | Qwen2.5-VL 7B is a multimodal vision-language model with 7 billion parameters that can process both images and text, enabling visual question answering, image description, and other vision-language tasks. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/qwen2_5_vl_7b_instruct) |
| Qwen 3-4B Instruct | VENTUNO Q | The Qwen3-4B is a state-of-the-art multilingual base language model with 4 billion parameters, excelling in language understanding, generation, coding, and mathematics. This version of the model has been tuned as instruct model, optimized for following human instructions and providing detailed responses.  It is ideal for applications such as chatbots, virtual assistants, and any use case that benefits from a more conversational and responsive AI. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/qwen3_4b_instruct_2507) |
| Qwen 3-VL-4B VLM | VENTUNO Q | Qwen3-VL is a vision-language model from Alibaba Cloud capable of understanding both text and images for multimodal reasoning tasks such as visual question answering and image captioning. | [Qualcomm AI Hub](https://aihub.qualcomm.com/models/qwen3_vl_4b_instruct) |
| Qwen 3.5 0.8B | VENTUNO Q, UNO Q | Qwen 3.5 0.8B is a compact yet powerful language model developed by Alibaba, designed to deliver efficient performance on edge devices. With 0.8 billion parameters, it strikes a balance between capability and resource efficiency, making it ideal for applications that require natural language understanding and generation in constrained environments. | [Hugging Face](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) |

### Sensor

Models over accelerometer and vibration data, no camera or microphone required.

| Model | Boards | Description | Source |
| :--- | :--- | :--- | :--- |
| Continuous motion detection | Unrestricted | A motion detection model designed to identify up/down, wave, and snake movements evalauting accelerometer data. | [Edge Impulse](https://studio.edgeimpulse.com/public/734960/live) |
| Fan anomaly detection | Unrestricted | An anomaly detection model designed to identify anomalies in fan operation. | [Edge Impulse](https://studio.edgeimpulse.com/public/774707/live) |
<!-- app-lab-models table end -->
