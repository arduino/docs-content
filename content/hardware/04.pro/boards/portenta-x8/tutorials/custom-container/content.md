---
title: Create and Upload a Custom Container Portenta X8
difficulty: easy
tags: [Linux, Python, Containers]
description: This tutorial will show you how to create and upload your custom container to your Portenta X8
author: Benjamin Dannegård
hardware:
  - hardware/04.pro/board/portenta-x8
software:
  - adb
---

## Overview

In this tutorial we will create a simple container that we can then upload to the Portenta X8. A container consists of an image file and all it's dependencies if there are any. This tutorial will go through the different files needed to create a container and their functions. Building this container locally and then uploading it to a Portenta X8.

## Goals

- Learn how to create a container for use with the Portenta X8
- Learn how to upload a container to the Portenta X8

### Required Hardware and Software

-   [Portenta X8](https://store.arduino.cc/portenta-x8)

## Instructions

When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image. Since the image contains the container’s filesystem, it must contain everything needed to run an application - all dependencies, configuration, scripts, binaries, etc. The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.

## Container File Structure

To create our container we need to collect our necessary files. Creating a folder called **hello-world**, then putting the following files in the folder:
- docker-build.conf
- docker-compose.yml
- Dockerfile
- requirements.txt
- src folder
- main.py (This file should be inside the src folder)

Lets go through what these files contain and do.

### docker-buil.conf
A file containing the minimal "unit test" command to be executed on the container to prove it's working.

```python
TEST_CMD="python3 --help"
```

### docker-compose.yml
This file defines the app name through the factory, permissions and settings for the involved containers.

```python
version: '3.6'

services:
  python-hello-world:
    image: blob-opera:latest
    restart: always
    tty: true
    read_only: true
    user: "63"
    tmpfs:
    - /run
    - /var/lock
    - /var/log
    - /tmp
```

### Dockerfile
This is used to build the container.

```python
# Copyright (c) 2022 Arduino.cc
#

# Examples:
# docker build --tag "python-hello-world:latest" .
# docker run -it --rm --user "63" python-hello-world:latest

FROM python:3-alpine3.15

LABEL maintainer="Massimo Pennazio <maxipenna@libero.it>"

# Set our working directory
WORKDIR /usr/src/app

# Copy requirements.txt first for better cache on later pushes
COPY requirements.txt requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
RUN pip install -r requirements.txt

# This will copy all files in our root to the working  directory in the container
COPY ./src/main.py ./

# Enable udevd so that plugged dynamic hardware devices show up in our container.
ENV UDEV=1

# main.py will run when container starts up on the device
CMD ["python","-u","main.py"]
```

### requirements.txt

```python
Flask==0.12.3
```

### Source
Here we will keep source code of the app you want to run in the container or simply a startup script. We will create a file and name it **main.py** in this folder. This script will ?????.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

## Upload container

Using docker-compose

Should be the preferred way of testing app/containers since inside docker-compose.yml you specify a lot of settings that may not be trivial to convert to docker run arguments

```
cd /home/fio/hello-world
```
```
docker-compose up --detach
```

Should start your application and register it as a systemd service that will be persistent

accross reboots (e.g. at next boot your docker-compose app will be executed automagically)

```
docker-compose stop
```
This command will stop your docker-compose app from running


## Conclusion

This tutorial went through how to create a container for a script or app using Python. And then how to upload this container to a Portenta X8. This is a good method for creating and quickly testing containers. Allowing you to make sure a container works before pushing it to your factory.
