---
title: 'Getting Started with Arduino AWS S3 CSV Exporter'
description: 'Learn how to set up the Arduino AWS S3 CSV Exporter to extract and store time series data from the Arduino Cloud into an AWS S3 bucket.'
difficulty: intermediate
tags:
  - Arduino Cloud
  - AWS
  - CSV Export
  - Data Aggregation  
author: 'Taddy Ho Chung'
software:
  - iot-cloud
  - aws-lambda
  - go
---

## Overview

The **Arduino AWS S3 CSV Exporter** is designed to extract time series data from **Arduino Cloud** and publish it to an **AWS S3** bucket. The data extraction is managed by a scheduled AWS Lambda function that operates at configurable intervals, with samples aggregated based on the user’s preference. Data is stored in CSV format and uploaded to S3, providing a structured way to manage and store data.

## Goals

* Understand the functionality of the Arduino AWS S3 CSV Exporter
* Learn how to configure and deploy the Lambda function for data extraction
* Set up filtering and resolution options for optimized data aggregation
* Get started with configuring the exporter using CloudFormation

## Required Software

* [Arduino Cloud](https://cloud.arduino.cc/). If you do not have an account, you can create one for free inside [cloud.arduino.cc](https://cloud.arduino.cc/home/?get-started=true).
* [AWS CLI](https://aws.amazon.com/cli/)
* [Go Programming Language](https://go.dev/) (version 1.22 or higher)
* [Official Arduino AWS S3 CSV Exporter Repository](https://github.com/arduino/aws-s3-integration)

## Deployment Using CloudFormation Template

The exporter setup involves deploying resources using a CloudFormation template. Ensure your AWS account has permissions for:

* CloudFormation stack creation (policy: `AWSCloudFormationFullAccess`)
* S3 bucket management (policy: `AmazonS3FullAccess`)
* IAM role creation (policy: `IAMFullAccess`)
* Lambda function deployment (policy: `AWSLambda_FullAccess`)
* EventBridge rule configuration (policy: `AmazonEventBridgeFullAccess`)
* Parameter management in SSM (policy: `AmazonSSMFullAccess`)

### Setting Up

Get the [Lambda binaries](https://github.com/arduino/aws-s3-integration/releases) (`.zip` file) and the [CloudFormation template](https://github.com/arduino/aws-s3-integration/releases) (`.yaml` file).

Upload the binaries and the template to an accessible S3 bucket. Note the object URL for use in the stack creation process.

Use the CloudFormation console to create a new stack, entering the required parameters:
  
- **Mandatory:** Arduino API key and secret, the S3 bucket for code, and the destination S3 bucket.
- **Optional:** Tag filter, organization ID, and data resolution settings.

## Configuration Parameters

Below are the supported configuration parameters that are editable in the AWS Parameter Store. These parameters are pre-filled during stack creation but can be modified later:

| **Parameter**                                                  | **Description**                           |
|----------------------------------------------------------------|-------------------------------------------|
| `/arduino/s3-exporter/{stack-name}/iot/api-key`                | IoT API key                               |
| `/arduino/s3-exporter/{stack-name}/iot/api-secret`             | IoT API secret                            |
| `/arduino/s3-exporter/{stack-name}/iot/org-id`                 | Organization ID (Optional)                |
| `/arduino/s3-exporter/{stack-name}/iot/filter/tags`            | Tag filter (e.g., `tag=value`) (Optional) |
| `/arduino/s3-exporter/{stack-name}/iot/samples-resolution`     | Aggregation resolution (Optional)         |
| `/arduino/s3-exporter/{stack-name}/iot/scheduling`             | Execution schedule                        |
| `/arduino/s3-exporter/{stack-name}/iot/align_with_time_window` | Align data extraction with time windows   |
| `/arduino/s3-exporter/{stack-name}/destination-bucket`         | S3 destination bucket                     |
| `/arduino/s3-exporter/{stack-name}/enable_compression`         | Enable gzip compression for CSV uploads   |

## Tag Filtering

You can filter devices in the Arduino Cloud using tags. Add tags in the Arduino Cloud UI under the Metadata section of each device.

During CloudFormation stack creation, configure tag filters using:

```bash
/arduino/s3-exporter/{stack-name}/iot/filter/tags
```

## CSV File Structure

The exported CSV files have the following format:

```bash
timestamp,thing_id,thing_name,property_id,property_name,property_type,value,aggregation_statistic
```

Files are organized by date, and the naming follows a structured format for easy identification:

```bash
<bucket>:2024-09-04/2024-09-04-10-00.csv
<bucket>:2024-09-04/2024-09-04-11-00.csv
```

## Building the Code

Ensure [**Go (version 1.22)**](https://go.dev/) is installed to build the exporter locally. The core code can be built using:

```bash
./compile-lambda.sh
```

This creates a **`arduino-s3-integration-lambda.zip`** file. Alternatively, run:

```bash
task go:build
```

## Additional Documentation

* [Arduino Cloud Documentation](https://docs.arduino.cc/cloud/iot-cloud)
* [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
* [Go Programming Language Documentation](https://go.dev/doc/)
