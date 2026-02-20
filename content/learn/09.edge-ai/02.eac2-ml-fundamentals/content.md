---
title: 'ML Fundamentals for Edge Devices (2/4)'
description: 'This module covers the most suitable algorithms, optimization techniques, and the complete lifecycle of Edge AI applications'
tags:
  - Edge AI
  - Fundamentals
  - Machine Learning
author: 'José Bagur'
hardware:
  - hardware/02.hero/boards/uno-r4-wifi
---

In the previous module, we explored what Edge AI is and why it is relevant for embedded applications and edge devices. In this module, we will delve deeper into the fundamentals of machine learning for resource-constrained devices, covering the most suitable algorithms, optimization techniques, and the complete lifecycle of Edge AI applications.

## Algorithm Types for Edge AI

Not all machine learning algorithms are suitable for running on edge devices. Here, we will examine the characteristics that make Edge AI efficient in resource-constrained environments, as well as the main types of tasks that can be performed with Edge AI.

### Efficient Algorithms for Resource-Constrained Devices

Edge devices, such as microcontrollers, have significant memory, processing, and power constraints. Therefore, Edge AI algorithms must be highly efficient [1].

The first criterion is **low memory consumption**. Models must be small enough to fit in the microcontroller's Flash memory (storage) and SRAM (inference execution). A typical TinyML model ranges from 10 KB to 250 KB, depending on the hardware [2].

The second criterion is **low computational complexity**, meaning minimizing the number of mathematical operations required to generate a prediction. This is commonly measured in FLOPS (floating-point operations per second) or MACs (multiply-accumulate operations).

Additionally, real-time applications require **predictable latency** to ensure timely responses. A latency is the response time interval between two actions; when it is predictable, it means that it has more or less a constant value over time. Finally, for battery-powered devices, energy efficiency is critical.

The following table presents the most commonly used model types in Edge AI:

|         **Model Type**        |            **Characteristics**           |              **Typical Use Cases**             |
|:-----------------------------:|:----------------------------------------:|:----------------------------------------------:|
|     **Decision trees**        | Low memory consumption, fast inference   |   Simple classification, anomaly detection     |
|  **Small neural networks**    |  Balance between accuracy and efficiency | Signal classification, pattern recognition     |
|     **Optimized CNNs**        |     Efficient for spatial data           | Computer vision, image classification          |
| **Anomaly detection models**  |       Low resource consumption           |  Predictive maintenance, sensor monitoring     |

### Classification vs. Regression vs. Detection

Machine learning algorithms can be classified according to the type of problem they solve. Understanding these differences is fundamental for selecting the appropriate approach for each application [3].

#### Classification

Classification is a supervised learning task in which the model assigns a category label to a given input. During training, the model learns to distinguish between predefined classes.

The model's output is a category, such as "normal" or "anomalous". The task can be binary (two classes) or multiclass (more than two options). During inference, the model assigns a probability to each class, including the prediction and its confidence.

In Edge AI, classification is used to recognize voice commands, classify gestures detected by accelerometers, identify environmental sounds, and detect human activities such as walking or running.

The performance of a classifier is evaluated with the following metrics:

- **Accuracy:** Proportion of correct predictions relative to the total number of predictions.
- **Precision:** Proportion of correctly predicted positives.
- **Recall (Sensitivity):** Proportion of actual positives correctly detected.
- **F1-Score:** Harmonic mean between precision and recall. Unlike a simple average, it penalizes imbalanced values, so a high F1-Score is only achieved when both metrics are reasonably good.

#### Regression

Regression is a supervised learning task in which the model predicts a continuous numerical value, learning the mathematical relationship between the input variables and the output variable.

Unlike classification, the output is a number that can take any value within a range. The model learns to approximate a function that maps inputs to outputs, which is helpful for quantitative predictions.

Regression applications in Edge AI include predicting future temperature or humidity from sensor readings, estimating remaining battery level, predicting energy consumption, and estimating distance or position.

The evaluation metrics for regression differ from those used in classification:

- **Mean Squared Error (MSE):** Average of the squared errors. By squaring, significant errors have a disproportionate impact, making this metric sensitive to outliers.
- **Mean Absolute Error (MAE):** Average of the absolute values of the errors. It is more intuitive than MSE because it is in the same units as the predicted variable and is less sensitive to outliers.
- **Coefficient of Determination (R²):** Proportion of variance explained by the model. A value of 1.0 indicates a perfect fit, while 0.0 means the model explains the data no better than simply using the average.

#### Anomaly Detection

Anomaly detection is the task of identifying patterns that deviate significantly from normal behavior. Unlike traditional classification, this approach is usually trained only with "normal" data [4].

The model learns what constitutes normal behavior. During inference, it identifies deviations from that pattern. This characteristic is valuable because it does not require examples of every anomaly, which is ideal when anomalies are rare, unpredictable, or unknown.

In industrial environments, anomaly detection enables the identification of unusual vibrations in motors, anomalous sounds in machinery, and irregular electrical consumption patterns. It is also applied in security to detect intrusions or suspicious behavior.

The evaluation of these models focuses on the following metrics:

- **True Positive Rate (Sensitivity):** Proportion of actual anomalies that the model correctly detects.
- **False Positive Rate:** Proportion of typical cases that the model incorrectly classifies as anomalies. A high value generates unnecessary alerts.
- **Area Under the ROC Curve (AUC-ROC):** The ROC (*Receiver Operating Characteristic*) curve is a graph that shows the trade-off between sensitivity and false-positive rate at different decision thresholds. The AUC measures the area under this curve; a value of 1.0 indicates perfect separation between classes, while 0.5 indicates random classification.

#### Object Detection

Object detection combines classification and localization. It identifies the objects in an image and their locations. It is a more complex task and requires more computational resources than simple classification [5].

The model not only classifies the entire image. It also identifies multiple objects, shows their locations using bounding boxes, and assigns a class to each. This requires more complex network architectures, such as **YOLO** (*You Only Look Once*) or **SSD** (*Single Shot Detector*), specifically designed to detect multiple objects in a single pass through the image.

In Edge AI, object detection is applied to count people in commercial spaces, detect products on shelves, identify defects in production lines, and monitor wildlife.

### Signal Processing vs. Computer Vision

Edge AI applications can be divided into two major categories based on the type of data they process: signal processing and computer vision. Each category has distinct characteristics, techniques, and resource requirements.

#### Signal Processing

Signal processing focuses on sequential data captured by sensors such as accelerometers, microphones, or environmental sensors. These data are usually one-dimensional or low-dimensional, making them more manageable for resource-constrained devices [6].

The input data consists of time series, audio signals, or sensor readings. Before feeding this data to the model, preprocessing techniques are applied, such as filtering, normalization, and feature extraction. The resulting models generally occupy less than 50 KB and offer latencies in the order of milliseconds.

The most common transformations for converting signals into useful features for the model are as follows:

- **FFT (Fast Fourier Transform):** Converts signals from the time domain to the frequency domain, revealing frequency components hidden in the original signal.
- **MFCC (Mel-Frequency Cepstral Coefficients):** Provides a compact representation of audio signals that mimics human auditory perception and is widely used in speech recognition.
- **Spectrograms:** Offer a visual representation of how the frequency content of a signal varies over time.

#### Computer Vision

Computer vision processes images and video to extract visual information. These applications generally require more computational resources due to the high dimensionality of the data: a small 96×96 pixel grayscale image contains more than 9,000 values [7].

Preprocessing includes image resizing, pixel value normalization, and data augmentation techniques. The most widely used architectures are convolutional neural networks (CNNs), particularly optimized versions such as MobileNet and EfficientNet. Models can range from 50 KB to more than 500 KB, with typical latencies of tens to hundreds of milliseconds.

When implementing computer vision on edge devices, several factors should be considered. Reducing image resolution significantly decreases computational requirements. Grayscale images require 1/3 as much memory as color images. Additionally, architectures like MobileNet and EfficientNet are specifically designed for mobile devices and embedded systems, offering a good balance between accuracy and efficiency.

## TinyML: ML on Resource-Constrained Devices

TinyML represents the intersection between machine learning and ultra-efficient embedded systems. In this section, we will explore the fundamental principles that enable running ML models on microcontrollers with minimal resources.

### Principles and Optimization Techniques

To run machine learning models on devices with kilobytes of memory and milliwatts of power consumption, specialized optimization techniques are required [8]. These techniques are applied both during model design and after training.

#### Efficient Model Design

The first step in TinyML is to design or select inherently efficient model architectures. A *layer* is a group of connected units of information. **Shallow neural networks**, with 2-4 layers, are sufficient for many Edge AI tasks and reduce both model size and inference time.

**Depthwise Separable Convolutions**, used in architectures like MobileNet, significantly reduce the number of operations in convolutional layers by separating spatial convolutions from channel-wise convolutions [9]. Complementarily, **channel reduction** limits the number of filters per layer, thereby proportionally reducing model size and required operations.

#### Pruning

Pruning is all about getting rid of connections or neurons that aren't really adding anything significant to the model's output [10]. There are two main approaches: **unstructured pruning** removes individual weights that have values close to zero, while **structured pruning** removes entire neurons, channels, or layers.

This technique can reduce the model size by 50% to 90% with minimal precision loss, depending on the task and the level of pruning.

#### Knowledge Distillation

This technique trains a small model (student) to mimic the behavior of a larger, more accurate model (teacher) [11]. The process follows three steps: first, the teacher model is trained to its full capacity; then, the student model learns to reproduce the teacher's outputs; and finally, the student captures the essential knowledge in a more compact architecture.

### Model Quantization and Compression

Quantization reduces the numerical precision of model weights and activations. Machine learning models typically use 32-bit floating-point numbers (FP32), but in Edge AI, we can use more compact representations [12]. 

Quantization is one of the most important techniques for reducing model size and accelerating inference on edge devices. Its impact is so significant that virtually all models deployed on microcontrollers use some form of quantization.

The following table shows the most common data types and their impact on model size:

| **Type** | **Bits** |  **Value Range**  | **Size Reduction** |
|:--------:|:--------:|:-----------------:|:------------------:|
|  `FP32`  |    32    |    ±3.4 × 10³⁸    |      Base (1x)     |
|  `FP16`  |    16    |    ±6.5 × 10⁴     |         2x         |
|  `INT8`  |     8    |    -128 to 127    |         4x         |
|  `INT4`  |     4    |      -8 to 7      |         8x         |

#### Types of Quantization

There are several approaches to applying quantization, each with different trade-offs between simplicity and precision:

* **Post-training quantization** is applied after the model has been trained. It is the most straightforward technique to implement. However, it may result in greater precision loss because the model was not trained to account for the limitations of the quantized representation.

* **Quantization-Aware Training** simulates quantization effects during training. This allows the model to adapt to numerical constraints, resulting in better precision after quantization.

* **Dynamic quantization** offers a hybrid approach in which weights are statically quantized while activations are dynamically quantized during inference.

#### Impact of Quantization

Quantization from `FP32` to `INT8` typically results in a 4x reduction in model size, a 2x to 4x inference speedup, reduced power consumption, and a precision loss of 1-2% or less in most cases. These benefits make `INT8` quantization the de facto standard for microcontroller deployments.

### Frameworks and Tools

The TinyML tools ecosystem has matured significantly, making it easier to develop Edge AI applications without requiring deep expertise in model optimization.

#### TensorFlow™ Lite Micro

TensorFlow Lite Micro is a version of TensorFlow designed specifically for microcontrollers [13]. It is the reference framework for TinyML and provides an interpreter optimized for devices with kilobytes of memory, support for quantized operations (`INT8`), operating system independence, and compatibility with multiple microcontroller architectures.

The typical workflow with TensorFlow Lite Micro consists of the following steps:

1. Train a model in TensorFlow (on a computer or in the cloud)
2. Convert the model to TensorFlow Lite format (.tflite)
3. Apply quantization during conversion
4. Integrate the model into the microcontroller application

However, this framework has some limitations. Not all TensorFlow operations are supported; integration requires C/C++ knowledge, and debugging can be complex.

#### Edge Impulse

Edge Impulse is a comprehensive development platform for Edge AI that simplifies the entire lifecycle [14]. This platform will be our primary tool in the practical part of the course.

The [platform](https://www.edgeimpulse.com/) offers an intuitive web interface for the entire workflow, data collection directly from devices, automatic signal and image preprocessing, model training optimized for edge devices, automatic quantization and optimization, and one-click deployment for Arduino and other microcontrollers.

For developers getting started with Edge AI, Edge Impulse offers significant advantages: it does not require prior machine learning experience, provides native integration with Arduino boards, offers a library of pre-trained models, and allows performance profiling before deployment.

The workflow in Edge Impulse follows these steps:

1. Connect the device and collect data
2. Design the processing pipeline (processing blocks)
3. Select and configure the learning model
4. Train and evaluate the model
5. Optimize for the target hardware
6. Download the library for Arduino

#### Tool Comparison

The following table summarizes the main differences between the two tools:

|        **Aspect**        | **TensorFlow Lite Micro** |      **Edge Impulse**     |
|:------------------------:|:-------------------------:|:-------------------------:|
|   **Learning curve**     |          Steep            |          Gentle           |
|     **Flexibility**      |           High            |          Medium           |
| **Arduino integration**  |          Manual           |         Automatic         |
|   **Data collection**    |         External          |         Integrated        |
|     **Optimization**     |          Manual           |         Automatic         |
|         **Cost**         |           Free            |    Free (basic tier)      |

## Edge AI Development Cycle

Developing a successful Edge AI application requires following a structured process that spans from problem definition to system deployment and maintenance.

### Complete Cycle Overview

The Edge AI development cycle consists of six main phases that are executed iteratively [15]:

1. Problem definition
2. Data collection
3. Data processing
4. Model training
5. Evaluation and deployment
6. Monitoring and improvement

#### Phase 1: Problem Definition

Before starting any technical development, it is essential to clearly define the problem being solved. This phase must answer key questions: What decision or action should the system take? What is the minimum acceptable accuracy? What are the latency requirements? What hardware constraints exist? How will project success be measured?

#### Phase 2: Data Collection

Data is the fuel of machine learning. This phase involves identifying the data needed to train the model, designing the data-capture process, collecting representative data from all classes or scenarios, correctly labeling the data, and verifying its quality and diversity.

#### Phase 3: Data Processing

Raw data is rarely ready for training. Processing includes data cleaning (removing noise and outliers), normalization and standardization, feature extraction, data augmentation to improve generalization, and splitting into training, validation, and test sets.

#### Phase 4: Model Training

With the data prepared, the model training proceeds. This phase covers architecture selection, hyperparameter configuration, iterative training with metric monitoring, validation to avoid overfitting, and fine-tuning based on results.

#### Phase 5: Evaluation and Deployment

Before deployment, the model must be evaluated and optimized. This includes evaluation on the test set (unseen data), quantization and optimization for the target hardware, verification that the model meets memory and latency constraints, integration with the application code, and testing on the actual device.

#### Phase 6: Monitoring and Improvement

Once deployed, the system requires continuous monitoring. Activities include collecting performance metrics in production, identifying cases where the model fails, periodic retraining with new data, and updating the model on devices.

### Planning Edge AI Projects

Effective planning is key to the success of Edge AI projects. Below are important considerations for each project aspect.

#### Hardware Selection

Hardware selection should be based on the specific requirements of the project:

|      **Requirement**      |        **Hardware Consideration**       |
|:-------------------------:|:---------------------------------------:|
|     **Model size**        |        Available Flash memory           |
|   **Inference speed**     |   Processor frequency, accelerators     |
|     **Sensor type**       |    Available peripherals, interfaces    |
|     **Battery life**      |  Power consumption, low-power modes     |
|     **Connectivity**      |      Wi-Fi, Bluetooth, LoRa, etc.       |
|        **Cost**           |     Unit price, production volume       |

#### Resource Estimation

Before starting development, it is essential to estimate the necessary resources. A basic Edge AI project typically requires 6 to 12 weeks, distributed approximately as follows: 1-2 weeks for definition and planning, 2-4 weeks for data collection, 2-4 weeks for model development, and 1-2 weeks for integration and testing.

Regarding data, recommended quantities vary according to task complexity. For simple classification, 100 to 500 samples per class are needed. Complex classification requires 500 to 2,000 samples per class. For anomaly detection, more than 1,000 samples of normal behavior are recommended.

### Common Challenges and Solutions

Edge AI development presents unique challenges [16]. Below are the most common ones and their solutions.

#### Challenge 1: Insufficient or Imbalanced Data

When there is not enough training data or some classes have many more examples than others, data augmentation techniques (rotation, scaling, noise addition), class rebalancing through oversampling or undersampling, transfer learning with pre-trained models, or additional collection focused on minority classes can be applied.

#### Challenge 2: Too Large Model 

If the trained model exceeds the device's available memory, solutions include applying more aggressive quantization (INT8 or INT4), reducing the architecture size (fewer layers, fewer neurons), pruning to remove unnecessary weights, or using hardware with more memory.

#### Challenge 3: Excessive Latency

When inference time is too long for the application, model complexity can be reduced, data preprocessing can be optimized, quantized operations can be used (faster than floating-point), or input data resolution or sampling rate can be reduced.

#### Challenge 4: Poor Production Performance

If the model works well in the lab but fails in real conditions, it is necessary to collect data under more diverse, realistic conditions, including variations in environment, noise, and lighting during training; implement robust preprocessing (e.g., filtering, adaptive normalization); and test exhaustively in the deployment environment.

#### Challenge 5: High Power Consumption

When the device drains the battery too quickly, strategies include enabling low-power modes when there is no activity, reducing inference frequency when possible, using activity detection before running the whole model, and optimizing code to minimize CPU cycles.

## Summary

In this module, we have delved deeper into the fundamentals of machine learning for edge devices.

**Algorithms for Edge AI** must be efficient in memory, computation, and power. The main task types include classification, regression, and anomaly detection, each with its own evaluation metrics and use cases.

**Signal processing** and **computer vision** represent the two major application categories. Signal processing works with sensor and audio data, generally with more modest resource requirements. Computer vision processes images and requires optimized architectures, such as MobileNet, to function efficiently on edge devices.

**TinyML** enables running ML on microcontrollers through techniques such as efficient architecture design, pruning unnecessary connections, knowledge distillation, and, especially, model quantization.

**TensorFlow Lite Micro** and **Edge Impulse** are the primary tools in the ecosystem. TensorFlow Lite Micro offers maximum flexibility but requires more technical expertise. At the same time, Edge Impulse significantly simplifies the process and will be our primary tool in the practical part of the course.

The **Edge AI development cycle** is iterative and includes problem definition, data collection, processing, training, deployment, and continuous monitoring. Each phase presents specific challenges with established solutions.

In the next module, we will explore in detail the workflow for creating Edge AI applications and prepare for practical implementation with the Arduino UNO R4 WiFi board.

## References

[1] P. Warden and D. Situnayake, *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*. Sebastopol, CA, USA: O'Reilly Media, 2019.

[2] V. J. Reddi et al., "Widening access to applied machine learning with TinyML," *Harvard Data Science Review*, vol. 4, no. 1, 2022, doi: 10.1162/99608f92.a31e8c72.

[3] I. Goodfellow, Y. Bengio, and A. Courville, "Machine learning basics," in *Deep Learning*. Cambridge, MA, USA: MIT Press, 2016, ch. 5. [Online]. Available: https://www.deeplearningbook.org/contents/ml.html

[4] V. Chandola, A. Banerjee, and V. Kumar, "Anomaly detection: A survey," *ACM Comput. Surv.*, vol. 41, no. 3, pp. 1–58, Jul. 2009, doi: 10.1145/1541880.1541882.

[5] R. Girshick, J. Donahue, T. Darrell, and J. Malik, "Rich feature hierarchies for accurate object detection and semantic segmentation," in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR)*, Columbus, OH, USA, 2014, pp. 580–587, doi: 10.1109/CVPR.2014.81.

[6] J. Lin, L. Zhu, W.-M. Chen, W.-C. Wang, and S. Han, "Tiny machine learning: Progress and futures," *IEEE Circuits Syst. Mag.*, vol. 23, no. 3, pp. 8–34, 2023, doi: 10.1109/MCAS.2023.3302182.

[7] A. G. Howard et al., "MobileNets: Efficient convolutional neural networks for mobile vision applications," *arXiv preprint arXiv:1704.04861*, 2017.

[8] Y. Abadade, A. Temouden, H. Bamoumen, N. Benamar, Y. Chtouki, and A. S. Hafid, "A comprehensive survey on TinyML," *IEEE Access*, vol. 11, pp. 96892–96922, 2023, doi: 10.1109/ACCESS.2023.3294111.

[9] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L. Chen, "MobileNetV2: Inverted residuals and linear bottlenecks," in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR)*, Salt Lake City, UT, USA, 2018, pp. 4510–4520, doi: 10.1109/CVPR.2018.00474.

[10] S. Han, J. Pool, J. Tran, and W. J. Dally, "Learning both weights and connections for efficient neural networks," in *Proc. Adv. Neural Inf. Process. Syst. (NeurIPS)*, Montreal, Canada, 2015, pp. 1135–1143.

[11] G. Hinton, O. Vinyals, and J. Dean, "Distilling the knowledge in a neural network," *arXiv preprint arXiv:1503.02531*, 2015.

[12] B. Jacob et al., "Quantization and training of neural networks for efficient integer-arithmetic-only inference," in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR)*, Salt Lake City, UT, USA, 2018, pp. 2704–2713, doi: 10.1109/CVPR.2018.00286.

[13] R. David et al., "TensorFlow Lite Micro: Embedded machine learning for TinyML systems," in *Proc. Mach. Learn. Syst. (MLSys)*, 2021, pp. 800–811.

[14] Edge Impulse, "Edge Impulse Documentation," 2024. [Online]. Available: https://docs.edgeimpulse.com/

[15] A. Garcia, P. Serrano, D. Urda, J. J. Rodriguez, and C. Garcia-Osorio, "Embedded AI and TinyML: A practical analysis of workflows and libraries," in *Distributed Computing and Artificial Intelligence (DCAI 2024)*, vol. 1259, Lecture Notes in Networks and Systems. Cham, Switzerland: Springer, 2025, pp. 1–10.

[16] R. Kallimani et al., "TinyML: Enabling of inference deep learning models on ultra-low-power IoT edge devices for AI applications," *Micromachines*, vol. 13, no. 6, p. 851, May 2022, doi: 10.3390/mi13060851.