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
---

## Overview

This project provides a method to extract time series data from the Arduino Cloud and publish it to an S3 destination bucket. Data is extracted at a specified resolution through a scheduled Lambda function. The samples are stored in CSV files and uploaded to S3.

By default, data extraction occurs every hour (this interval is configurable), with samples aggregated at a 5-minute resolution (also configurable). Aggregation is performed as an average over the aggregation period. Non-numeric values, such as strings, are sampled based on the defined resolution.

