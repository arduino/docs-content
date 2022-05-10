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

To create our container we need to collect our necessary files. Creating a folder called **x8-custom-test**, the following files needs to be in the folder:
- docker-build.conf
- docker-compose.yml
- Dockerfile
- requirements.txt
- src folder
- main.py (This file should be inside the src folder)

Lets go through what these files contain and do.

### docker-buil.conf
A file containing the minimal "unit test" command to be executed on the container to prove it's working. Our file will make our containers minimal unit test a test of Python3's help commmand.

```python
TEST_CMD="python3 --help"
```

### docker-compose.yml
This file defines the app name through the factory, permissions and settings for the involved containers. The argument in the image tag will make it so our image file builds locally.

```python
version: '3.6'

services:
  x8-custom-test:
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
# docker build --tag "hello-world:latest" .
# docker run -it --rm --user "63" hello-world:latest

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
Here we will keep source code of the app you want to run in the container or simply a startup script. We will create a file and name it **main.py** in this folder. This script will print "Hello World!" in the CLI window.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

## Uploading the Container Folder

First, you have to have set up your board to a factory, as shown in the [Portenta X8 Out of the Box tutorial]().

Once this is done, we will push our folder to a repository within the factory. Lets place our folder "x8-custom-test" inside the "containers.git" repository. You can find this repository inside your factory page, if you click on "Source". And then on "container.git", the url of this page will be used in the next command.

In bash use the following command, replace the "YOUR_FACTORY" with the name of your factory, to get the container repository, where we will put our folder. The "-m" tag selects the manifest file within the repository. If no manifest name is selected, the default is "default.xml". And the "-b" tag specifies a revision.

```python
repo init -u https://source.foundries.io/factories/YOUR_FACTORY/containers.git -m arduino.xml -b devel
```

We can also run ```repo sync``` to get the latest version of the repository. Put the "x8-custom-test" folder in the repository.

### Building and Running the Container

After uploading the folder to the repository. Navigate into the "x8-custom-test" folder, that should be located on your board now. This allows us to build our container with a simple command. Using ```docker build``` with --tag will let us give the container a tag so we can easily keep track of what version of the build this is.

```python
docker build --tag "x8-custom-test:latest" .
```

Now that it is built we can run it with ```docker run```, finding it with the tag that we chose to give to the build we want to run. Here we will have to enter the user information into the --user tag. This information is found inside the "docker-compose.yml" file.

```python
docker run -it --rm --user "63" x8-custom-test:latest
```

###  Using docker-compose


A option for testing an app or container is to use "docker-compose". This is helpful when we have a lot of settings in our "docker-compose.yml" file, since we don't have to use those settings in the run argument with this method. First navigate into the container folder.

```python
cd /home/fio/x8-custom-test
```

This docker-compose command will start your application and register it as a systemd service that will presist even when a reboot occurs. So at the next boot your docker-compose app will run automatically.

```python
docker-compose up --detach
```

To stop the docker-compose app from running, use the following command:

```python
docker-compose stop
```


## Conclusion

This tutorial went through how to create a container for a script or app using Python. And then how to upload this container to a Portenta X8. This is a good method for creating and quickly testing containers. Allowing you to make sure a container works before pushing it to your factory.
