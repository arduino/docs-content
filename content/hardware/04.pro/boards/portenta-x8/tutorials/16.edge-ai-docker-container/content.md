---
title: 'Edge Impulse on Portenta X8 with Docker'
difficulty: intermediate
description: 'Learn how to deploy and run an Edge Impulse model on Portenta X8 using Docker containers and a Flow Sensor for real time anomaly detection.'
tags:
  - Portenta X8
  - Edge Impulse
  - Docker
  - Flow Sensor
  - Sensor Fusion
author: 'Taddy Ho Chung'
hardware:
  - Portenta X8
  - Flow Sensor
software:
  - Edge Impulse
  - Docker
  - Python
  - Arduino IDE
---

## Overview

Industrial systems often rely on flow sensors to monitor fluid movement in pipelines, ensuring consistent operation and detecting potential anomalies such as leaks or blockages. By integrating machine learning with Edge Impulse, flow monitoring can be improved by classifying real time patterns and identifying irregularities before they lead to system failures.

This application note describes deploying a flow anomaly detection system using the Portenta X8, a flow sensor and an Edge Impulse machine learning model running inside a Docker container. The system continuously captures flow rate data, processes it through an AI model trained with Edge Impulse and classifies flow conditions in real time. The classification results can be used immediately, such as triggering an alarm, sending commands to an M4 microcontroller for further processing or forwarding data to Arduino Cloud for remote monitoring and visualization.

## Goals

The project showcased in this application note has the following objectives:

- Monitor fluid movement using a flow sensor.
- Classify flow patterns in real time with a machine learning model trained in Edge Impulse.
- Deploy the trained model inside a Docker container on the Portenta X8.
- Send classification results to the M4 microcontroller for onboard processing.
- Share all collected data and classification results to Arduino Cloud for remote monitoring.

## Hardware and Software Requirements

### Hardware Requirements

This project uses the Portenta X8, integrating a flow sensor for real time fluid monitoring. The required hardware includes:

- [Portenta X8](https://store.arduino.cc/products/portenta-x8) (x1)
- [Portenta Hat Carrier](https://store.arduino.cc/products/portenta-hat-carrier) (x1)
- Flow Sensor (e.g., YFS201) (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- Wi-Fi® Access Point or Ethernet with Internet access (x1)

### Software Requirements

To start with this application, ensure your Portenta X8 runs the latest Linux image.

- Ensure your Portenta X8 has the latest Linux image. Check [this section of Portenta X8's user manual](https://docs.arduino.cc/tutorials/portenta-x8/user-manual/#portenta-x8-os-image-update) to verify that your Portenta X8 is up-to-date.

***For the smooth functioning of the Portenta Hat Carrier with the Portenta X8, it is crucial to have at least Linux __image version > 746__ on the Portenta X8. To update your board to the latest image, use the [Portenta X8's Arduino Wizard Experience](https://docs.arduino.cc/tutorials/portenta-x8/image-flashing/#update-through-arduino-linux-wizard-experience) method or [manually flash it](https://docs.arduino.cc/tutorials/portenta-x8/image-flashing/#update-using-uuu-flashing-tool), downloading the most recent version from this [link](https://downloads.arduino.cc/portentax8image/image-latest.tar.gz).***

To develop and deploy the flow monitoring system, the following software tools and platforms are required:

- Edge Impulse for model training and deployment
- [Edge Impulse® CLI](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-overview), to manage Machine Learning models, we can install the Edge Impulse® Cli tool following these [instructions](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation).
- Docker for running inference models on Portenta X8
- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Web Editor](https://create.arduino.cc/editor)
- The [Arduino Create Agent](https://cloud.arduino.cc/download-agent/)
- The [Arduino Cloud](https://cloud.arduino.cc/). If you do not have an account, you can create one for free inside [cloud.arduino.cc](https://cloud.arduino.cc/home/?get-started=true).

## Machine Learning Model for Flow Anomaly Detection

Machine Learning allows industrial systems to analyze sensor data, recognize patterns and make data driven decisions. This application uses a machine learning model to classify flow patterns in real time, detecting anomalies that could indicate leaks, blockages or irregular pressure fluctuations. By leveraging Edge Impulse, the model is trained to distinguish between normal and abnormal flow conditions based on real time sensor data.

Using the Edge Impulse platform, the model undergoes a structured workflow consisting of data acquisition, feature extraction, model training and deployment. This process allows the Portenta X8 to perform real time flow analysis, allowing predictive maintenance and minimizing downtime in industrial pipelines.

### Model Design

The dataset consists of flow sensor readings sampled at a predefined frequency, capturing variations in fluid movement. The data is processed using digital signal processing (DSP) techniques to extract meaningful features before being analyzed by the machine learning model.

### Data Acquisition

A dataset of flow sensor readings is collected under different operating conditions to build an accurate model. The sensor data represents various flow states, such as stable, low, high and disrupted. These readings are continuously sampled at a predefined frequency to provide a representation of fluid movement over time.

The flow sensor is connected to the Portenta X8 to collect data, which forwards the raw readings to the Edge Impulse platform. This dataset serves as the foundation for training a machine learning model capable of distinguishing normal operational patterns from anomalies.

Once sufficient data is gathered, it is labeled and divided into training and testing sets to evaluate model performance.

### Feature Extraction

Raw sensor data alone is not sufficient for effective anomaly detection. Therefore, digital signal processing (DSP) techniques are applied to extract meaningful features from the collected flow data.

- Time-Series Analysis: Captures how flow rate changes over time.
- Spectral Analysis: Converts time domain signals into the frequency domain to highlight variations that may not be visible in raw data.
- Statistical Features: Computes mean, variance and standard deviation values to differentiate normal and abnormal flow patterns.

These extracted features are used as inputs to the machine learning model, improving its ability to detect subtle anomalies.

### Model Training

Using Edge Impulse, the processed data is used to train a machine learning model capable of classifying flow conditions. The model is designed to:

- Recognize normal flow patterns based on historical data.
- Detect anomalous flow conditions, such as unexpected fluctuations, obstructions or irregular flow rates.

Different machine learning techniques, such as decision trees, neural networks or anomaly detection models, may be considered to determine the most effective approach. The model is validated using a test dataset to ensure reliable performance before deployment.

### Deployment and Real-Time Inference

Once trained, the machine learning model is deployed to the Portenta X8 inside a Docker container. This allows real-time inference directly at the edge.

As new sensor data is collected, the model continuously classifies flow conditions, providing immediate feedback to the system. If an anomaly is detected, the system can trigger predefined actions, such as:

- Activating an alarm to alert operators.
- Sending notifications to Arduino Cloud for remote monitoring.
- Adjusting system parameters to mitigate potential failures.

This edge AI approach improves system reliability by detecting anomalies as they happen, reducing downtime and improving operation consistency.

## System Architecture and Data Flow

The flow anomaly detection system has real-time sensor data acquisition, machine learning inference and cloud-based monitoring. The architecture consists of three main layers:

- Data Collection Layer: The Portenta X8 reads flow sensor data, capturing variations in fluid movement.
- Processing & Inference Layer: The Edge Impulse trained model runs inside a Docker container on the Portenta X8, classifying flow patterns and detecting anomalies.
- Cloud & Visualization Layer: The system forwards classification results to Arduino Cloud, allowing remote monitoring, notifications and real-time dashboards.

### Data Flow Overview

The flow sensor continuously measures fluid movement and sends readings to the Portenta X8.

The Portenta X8 preprocesses the raw data and forwards it to a Docker container running the Edge Impulse inference model.

The model classifies the flow state, determining whether the condition is normal or anomalous.

If an anomaly is detected, the system triggers an alert and sends the data to Arduino Cloud for remote visualization.

Optionally, the Portenta X8’s M4 core can receive classification results for further embedded processing.

### Communication Between Components

- Flow Sensor & Portenta X8: The sensor outputs flow rate data, which the Portenta X8 reads at a fixed sampling interval.
- Portenta X8 & Docker Container (Edge Impulse Model): A Python script collects sensor readings and passes them to the inference engine. The Edge Impulse model classifies the flow state and returns a prediction.
- Portenta X8 & Arduino Cloud: Classification results are sent to the Arduino Cloud. Anomalies trigger cloud-based actions, such as alerts or data logging.

### System Workflow

- Data Acquisition: The Portenta X8 reads real-time flow sensor data. Raw readings are formatted for Edge Impulse inference.
- Edge AI Processing: The inference container analyzes the data. The model classifies the flow condition (e.g., normal, low, high or anomalous). The result is stored locally and optionally sent to the M4 core for additional processing.
- Cloud Integration & Alerts: The system pushes an alert to Arduino Cloud if an anomaly is detected. Cloud dashboards visualize flow trends and anomaly history. Notifications can be triggered for system operators.

### Edge Processing vs. Cloud Processing

The system leverages a hybrid processing approach, combining edge inference on the Portenta X8 with cloud based monitoring and analysis in Arduino Cloud.

#### Edge Processing

The Portenta X8 directly performs real-time inference on the device, running the trained Edge Impulse model inside a Docker container.

By running the machine learning model locally, the system can classify flow conditions and detect anomalies with minimal latency. This immediate response is critical for time-sensitive applications, such as detecting blockages or leaks before they cause operational disturbances.

Additionally, edge processing reduces dependency on continuous cloud connectivity, ensuring the system remains operational even in network restricted environments. This is particularly valuable in industrial settings, where stable internet access may not always be available. The system minimizes bandwidth usage by processing data at the edge, as only essential classification results are sent to the cloud.

#### Cloud Processing

While edge processing allows fast, on-device decision making, Arduino Cloud integration extends the system’s capabilities beyond real time inference. Classification results, including detected anomalies, are logged and stored in the cloud for remote access. This allows users to monitor flow conditions using cloud dashboards and historical trend analysis to gain deeper insights into system performance over time.

Furthermore, cloud connectivity allows alerts and notifications, ensuring that users are informed when anomalies occur. By combining edge inference with cloud based monitoring, the system can identify long-term trends in fluid movement, helping predict potential failures before they escalate.

#### Optimizing Real-Time Response and Data Storage

The system can benefit from its advantages by balancing local processing and cloud analytics. Edge AI ensures low latency and real time responses, while cloud based logging and visualization allow for comprehensive trend analysis.

This approach could be useful in industrial automation, where immediate anomaly detection and historical performance tracking are important for predictive maintenance and system optimization.

## Instructions

This section details the technical steps to implement the setup, including the necessary code and commands.

### Data Acquisition with Flow Sensor

The Portenta X8’s M4 microcontroller captures real time flow sensor data and outputs it in CSV format, which is compatible with Edge Impulse for model training. The sensor-data-generation.ino script configures the system to read and transmit flow rate values at one second intervals.

```arduino
#include <Arduino.h>
#include <FlowSensor.h>

#if defined(ARDUINO_PORTENTA_X8)
#define SerialDebug Serial1  // Use Serial1 for Portenta Carrier family
#else
#define SerialDebug Serial
#endif

// Define Flow Sensor Type (Change if using another model)
#define SENSOR_TYPE YFS201  
#define SENSOR_PIN PD_15  // Flow sensor signal pin

FlowSensor flowSensor(SENSOR_TYPE, SENSOR_PIN);

// Define 1Hz Sampling Frequency
#define INTERVAL_MS 1000  // 1 sample per second

static unsigned long last_interval_ms = 0;

// Interrupt function for counting pulses
void count() {
  flowSensor.count();
}

void setup() {
  SerialDebug.begin(115200);
  while (!SerialDebug);

  pinMode(LED_BUILTIN, OUTPUT);
  flowSensor.begin(count);

  SerialDebug.println("Setup complete. Streaming flow rate at 1 Hz");
}

void loop() {
  if (millis() - last_interval_ms >= INTERVAL_MS) { 
    last_interval_ms = millis(); 

    flowSensor.read();
    float flowRate = flowSensor.getFlowRate_m();      // Flow rate in L/min

    // Avoid NaN or Inf issues
    if (isnan(flowRate) || isinf(flowRate)) {
        SerialDebug.println("0.00");                  // Send 0 if no valid reading
    } else {
        SerialDebug.println(flowRate, 2);             // Print flow rate
    }

    // Blink LED to indicate data collection
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
  }
}
```

### Sending Data to Edge Impulse for Model Training

Use the Edge Impulse Data Forwarder tool to stream flow sensor data to Edge Impulse for training.

Connect the Portenta X8 to your PC via USB and make sure it is recognized as a serial device. Then, run:

```bash
edge-impulse-data-forwarder
```

Follow the prompts to select the correct serial port and map the flow rate variable to Edge Impulse. Upload the collected data and configure a custom target with Portenta X8 (Linux aarch64). Select Sensor Fusion as the processing block. Train the model using different flow rate conditions as normal, low, high, and anomaly.

After training and validating the model, export it as a Docker container for deployment.

```
networks:
  sensorfusion:

services:
  cad:
    image: arduino/python-sf:latest
    build: .
    restart: unless-stopped
    depends_on:
      - inference
    tty: true
    environment:
      M4_PROXY_HOST: m4proxy
      M4_PROXY_PORT: 5001
    extra_hosts:
      - "m4proxy:host-gateway"
    networks:
      sensorfusion:
        aliases:
          - collect-and-dispatch
    command: ["inference", "1337"]

  inference:
    image: public.ecr.aws/g7a8t7v6/inference-container:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    restart: unless-stopped
    ports:
      - 1337:1337
    networks:
      sensorfusion:
        aliases:
          - ei-inference
    command: [
      "--api-key", "ei_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "--run-http-server", "1337",
      "--force-target", "runner-linux-aarch64",
      "--model-variant", "int8"
    ]
```

Once connected with the Portenta X8, upload the required files using ADB:

```bash
adb push
```

### Running the Inference Model on Docker

With all files in place, navigate to the project directory and build the container:

```bash
docker build -t arduino/python-sf .
```

Start the application:

```bash
docker-compose up -d
```

To verify the inference engine is running, check logs:

```bash
docker-compose logs -f -n 10
```

### Classifying Flow Rate in Real-Time

```arduino
#include <Arduino.h>
#include <RPC.h>
#include <SerialRPC.h>
#include <FlowSensor.h>

// Define Flow Sensor Type and Pin
#define SENSOR_TYPE YFS201  
#define SENSOR_PIN PD_15  // Flow sensor signal pin

FlowSensor flowSensor(SENSOR_TYPE, SENSOR_PIN);

// Interrupt function for counting pulses
void count() {
    flowSensor.count();
}

// Function to calculate and return flow rate (for RPC)
float getFlowRate() {
    flowSensor.read();
    float flowRate = flowSensor.getFlowRate_m();  // Get flow rate in L/min

    // Avoid NaN or Inf issues
    if (isnan(flowRate) || isinf(flowRate)) {
        return 0.0;  // Default to 0 if no valid reading
    }
    return flowRate;
}

void setup() {
    flowSensor.begin(count);

    // Register the RPC function
    RPC.bind("flow_rate", getFlowRate);
}

void loop() {
    // Nothing needed in loop, RPC handles function calls when requested
}
```

The `main.py` script reads flow sensor data, sends it to Edge Impulse for classification and forwards the results to the M4 microcontroller for further action.

```python
import os
import time
import json
import argparse
from msgpackrpc import Address as RpcAddress, Client as RpcClient, error as RpcError

# Retrieve M4 Proxy settings from environment variables (or use defaults)
m4_proxy_host = os.getenv("M4_PROXY_HOST", "m4proxy")
m4_proxy_port = int(os.getenv("M4_PROXY_PORT", "5001"))
m4_proxy_address = RpcAddress(m4_proxy_host, m4_proxy_port)

# Define the single sensor we are using
sensors = ("flow_rate",)  # Tuple with one element to keep extend() valid

def get_sensors_data_from_m4():
    """
    Get flow sensor data from the M4 via RPC (MessagePack-RPC).
    The Arduino sketch on the M4 must implement the "flow_rate" method.
    """
    try:
        get_value = lambda value: RpcClient(m4_proxy_address).call(value)  # Ensure this returns a value
        data = [get_value(sensor) for sensor in sensors]  # Ensure it's a list
        
        print(f"Sensor Data: {data}")  # Debug output
        return data

    except RpcError.TimeoutError:
        print("Unable to retrieve sensor data from the M4: RPC Timeout")
        return []  # Ensure an empty list is returned instead of `None`

def get_sensors_and_classify(host, port):
    """
    Collect sensor data and send it for classification to Edge Impulse.
    """
    url = f"http://{host}:{port}/api/features"

    while True:
        print("Collecting 400 features from sensors... ", end="")

        data = {
            "features": [],
            "model_type": "int8"  # Force quantized inference mode
        }
        start = time.time()

        for _ in range(100):  # Collect data in chunks
            sensor_values = get_sensors_data_from_m4()

            if not isinstance(sensor_values, list):  # Validate that we get a list
                print(f"Error: Expected list but got {type(sensor_values)} with value {sensor_values}")
                sensor_values = []  # Default to an empty list
            
            data["features"].extend(sensor_values)  # Avoid TypeError

            time.sleep(100e-6)  # Small delay to match sampling rate

        stop = time.time()
        print(f"Done in {stop - start:.2f} seconds.")

        try:
            response = requests.post(url, json=data)
        except ConnectionError:
            print("Connection Error: retrying later")
            time.sleep(5)
            continue

        # Check the response
        if response.status_code != 200:
            print(f"Failed to submit features. Status Code: {response.status_code}")
            continue

        print("Successfully submitted features.")

        # Process the JSON response to extract classification results
        response_data = response.json()
        classification = response_data.get("result", {}).get("classification", {})

        print(f"Classification: {classification}")

        if classification:
            label = max(classification, key=classification.get)
            value = classification[label]

            print(f"{label}: {value}")

            request_data = json.dumps({"label": label, "value": value})

            try:
                client = RpcClient(m4_proxy_address)
                result = client.call("classification", request_data)
                print(f"Sent to {m4_proxy_host}:{m4_proxy_port}: {request_data}. Result: {result}")
            except RpcError.TimeoutError:
                print("Unable to send classification data to M4: RPC Timeout.")
        else:
            print("No classification found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get flow sensor data and send it to inference container for classification")
    parser.add_argument("host", help="The hostname or IP address of the inference server")
    parser.add_argument("port", type=int, help="The port number of the inference server")

    args = parser.parse_args()

    print("Classifying Flow Sensor Data with AI... Press Ctrl+C to stop.")

    try:
        get_sensors_and_classify(args.host, args.port)
    except KeyboardInterrupt:
        print("Exiting gracefully...")
```

## Additional Resources

- Portenta X8 Documentation: [docs.arduino.cc](https://docs.arduino.cc/hardware/portenta-x8/)
- Edge Impulse Documentation: [docs.edgeimpulse.com](https://docs.edgeimpulse.com/)
- GitHub Repository: [portenta-x8/webinars](https://github.com/arduino/fae-artifacts-public/tree/main/portenta-x8/webinars/2025-01-23_eletkor-edge-ai-solutions)

## Support

If you encounter any issues or have questions while working with the Portenta X8, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our [Help Center](https://support.arduino.cc/hc/en-us), which offers a comprehensive collection of articles and guides for the Portenta X8. The Arduino Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Portenta Family help center page](https://support.arduino.cc/hc/en-us/sections/360004767859-Portenta-Family)

### Forum

Join our community forum to connect with other Portenta X8 users, share your experiences, and ask questions. The forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Portenta X8.

- [Portenta X8 category in the Arduino Forum](https://forum.arduino.cc/c/hardware/portenta/portenta-x8/172)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Portenta X8.

- [Contact us page](https://www.arduino.cc/en/contact-us/)
