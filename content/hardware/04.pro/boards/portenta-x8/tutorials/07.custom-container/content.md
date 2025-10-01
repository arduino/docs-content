---
title: '07. Deploy a Custom Container with Portenta X8 Manager'
difficulty: intermediate
tags: [Linux, Python®, Containers, ADB]
description: 'This tutorial will show you how to create and upload your custom container to your Portenta X8.'
author: 'Benjamin Dannegård'
hardware:
  - hardware/04.pro/boards/portenta-x8
software:
  - adb
---

## Overview

In this tutorial, we will create a Docker container for the Arduino Portenta X8. We will start by building a Docker image, which includes all necessary code and dependencies. Then, we will show how to deploy this image to the Portenta X8 and run it as a container. This process involves using ADB for device communication to manage containers on the Portenta X8.

## Goals

- Learn how to create and understand Docker images for the Portenta X8
- Learn how to deploy and run containers on the Portenta X8

### Required Hardware and Software

- [Portenta X8](https://store.arduino.cc/portenta-x8)
- ADB: [Check how to connect to your Portenta X8](https://docs.arduino.cc/tutorials/portenta-x8/user-manual#out-of-the-box-experience)
- [USB-C® cable (USB-C® to USB-A cable)](https://store.arduino.cc/products/usb-cable2in1-type-c)
- [Arduino Cloud Subscription](https://cloud.arduino.cc/)
- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2](https://www.arduino.cc/en/software), or [Arduino Cloud Editor](https://create.arduino.cc/editor)

## Instructions

A Docker container operates with an isolated filesystem derived from its image. The container's image acts as a blueprint, providing a custom filesystem containing all necessary components, such as dependencies, configurations, scripts, and binaries. It also includes settings like environment variables, default commands, and other metadata to ensure the container runs as intended.

## Container File Structure

Organize the essential files within a directory named **x8-custom-test** to prepare for container creation. This directory should include:

- **docker-build.conf**: Configuration for build specifics, including tests to verify the container's functionality.
- **docker-compose.yml**: YAML file for defining and running multi-container Docker applications.
- **Dockerfile**: A script with commands to assemble the image.
- **requirements.txt**: A list of Python® packages required for the application.
- **src folder**: A directory for source code.
- **main.py**: The main Python® script, located inside the src folder.

This organization eases a structured approach to building the Docker container. The complete folder should look as the following structure:

![Folder structure for container](assets/custom-container-folder.png)

### Docker-build.conf

This file specifies commands for basic validation tests within the container. Our setup defines a simple test to ensure the container's Python® environment is operational:

```python
TEST_CMD="python3 --help"
```

### Docker-compose.yml

The **docker-compose.yml** file stages the configuration of your application's services. This example defines a single service named **x8-custom-test**, configuring it with specific runtime properties such as restart policy, user permissions, and system settings. The image tag specifies the Docker image to use, in this case, *blob-opera:latest*, which will be built locally if it does not exist in the Docker registry.

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

The **Dockerfile** is a blueprint for building a Docker image, containing all the instructions (`FROM`, `COPY`, `COMMAND`, `ENTRYPOINT`, etc.) and detailing all steps from the base to the final image. It specifies the base image to use, the working directory, dependencies to install, and the command to run on container startup.

It sets up a Python® environment, installs dependencies from *requirements.txt*, and ensures the *main.py* script runs when the container is created.

```python
FROM python:3-alpine3.15

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

### Requirements.txt

This file lists the Python® packages required by your application, ensuring all dependencies are installed during the image build process. For this example, *Flask* is the required dependency, pinned to a specific version for consistency, reliability, or preference.

```python
Flask==0.12.3
```

### Source

Here we will keep the source code of the app you want to run in the container or a startup script. We will create a **main.py** file in this folder. This script will print "Hello World!" in the CLI window.

This section is dedicated to the application's source code or startup script for container execution. In the *src* folder, we will create a file named *main.py*. This script, using *Flask*, will display `"Hello World!"` in the CLI window.

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

Begin by resetting your board to its Factory settings as outlined in the Portenta X8 [Out-of-the-box experience from the User Manual](https://docs.arduino.cc/tutorials/portenta-x8/user-manual#out-of-the-box-experience).

Next, upload the **x8-custom-test folder** to a repository within the Factory environment. This repository, typically named *containers.git*, can be found on your Factory page under *Source*. Use the repository's URL for the following operations.

![Source on Foundries.io Factory page](assets/custom-factory-page.png)

![Where to find container.git](assets/custom-factory-git.png)

![Container.git page](assets/custom-git.png)

To pull or push repositories, you have to generate an API key. This is done by going to the user settings on the Factory page. Click on the user drop-down menu, enter the tokens page, and follow the steps to create a new API key. When creating the API key, please select the *Use for source code access* option and the correct Factory for which you want to use the key.

This token will be the password for all git operations, while the username can be anything except an empty string.

![User settings on your Factory page](assets/factory-user-settings.png)

![Token creation section in Foundries.io](assets/token-creation-page.png)

Use the following command in git on your machine. To get the repository on your machine, replace *YOUR_FACTORY* with the name of your Factory. After cloning the repository, the *-b* parameter specifies a branch to checkout. Running this command will get the container repository, where we will put our folder.

```bash
git clone https://source.foundries.io/factories/YOUR_FACTORY/containers.git -b devel
```

After cloning, add the **x8-custom-test** folder to this repository and push it with git.

When you have put the folder into the git folder, use *`git status`* to review changes; it will show the unadded changes in red. Then use *`git add`* to add the changes you want to your *`git commit`*. Then use *`git commit`* and *`git push`* to finally push the changes to the repository. Successfully pushing to "containers.git" triggers a new build in your FoundriesFactory, visible on the *Targets* page.

### Building and Running the Container

Once the build process is complete, it may take up to 10 minutes for your device to receive and apply the update over-the-air. You can monitor the update's progress through the *Devices* tab in your FoundriesFactory interface. After the update, the **x8-custom-test** folder will be on your device, ready for the next steps.

To build the container, use the *`docker build`* command in your Dockerfile's directory. The *`--tag`* option allows us to assign a version or name to the build, providing easier management of different container versions.

```bash
docker build --tag "x8-custom-test:latest" .
```

You can start the container using *`docker run`* with the built container image. Here, the *`--user`* flag is used to set the user identity (UID) for the container's process, as specified in the *docker-compose.yml* file.

```bash
docker run -it --rm --user "63" x8-custom-test:latest
```

This command starts the container interactively (*`-it`*), removes it after exit (*`--rm`*), and runs it under the specified user. The container will run with the settings and application defined in your *Dockerfile* and *Docker-compose* configurations.

### Using Docker Compose

For scenarios involving complex configurations, *`docker compose`* offers a streamlined approach to managing containerized applications. It removes the need for extensive command-line arguments using the settings defined in the *`docker-compose.yml`* file. Begin by navigating to the container's directory:

```bash
cd /home/fio/x8-custom-test
```

Using *`docker compose`*, the following command starts your application and sets it up as a `systemd` service, ensuring its persistence across reboots. As a result, your application will automatically start upon system startup:

```bash
docker compose up --detach
```

To stop the *`docker compose`* application, use the command below:

```bash
docker compose stop
```

## Deploying with Docker Hub

Docker Hub provides an alternative deployment method by hosting your container images on its platform. Start by creating a [Docker Hub account](https://hub.docker.com/) and setting up a repository for your container. Once your repository is ready, use the following command to upload your container image:

```bash
docker push HUB_USERNAME/x8-custom-test
```

Your custom container image will be available in your Docker Hub repository and accessible from any location with internet connectivity. To deploy this image to your Portenta X8, connect the device via ADB and execute the following commands. First, enter the device's shell:

```bash
adb shell
```

Then, pull and deploy the container image:

```bash
docker pull x8-custom-test
```

This command retrieves the container image, allowing you to deploy and run the container on your Portenta X8.

***For detailed instructions on creating and managing Docker Hub repositories for your custom Portenta X8 containers, refer to the official [Docker Hub Documentation](https://docs.docker.com/docker-hub/repos/#:~:text=To%20push%20an%20image%20to,docs%2Fbase%3Atesting%20).)***

## Conclusion

In this tutorial, we have outlined how to structure a Docker container for the Portenta X8, describing the necessary files and their purposes. We demonstrated integrating with Foundries.io's Factory for streamlined deployment and highlighted building and running the container on the device. Lastly, we introduced docker compose as a tool for testing containers, emphasizing speed and convenience.

### Next Steps

To get a better understanding of how to manage containers with Docker, take a look at our [Managing Containers with Docker on Portenta X8](https://docs.arduino.cc/tutorials/portenta-x8/docker-container). This tutorial will show some useful commands for the docker service and ADB or SSH.

## Troubleshooting

Here are some errors that might occur in the process of this tutorial:

- Make sure you have followed our other tutorials that show how to set up the Portenta X8 with [Out-of-the-box experience from the User Manual](https://docs.arduino.cc/tutorials/portenta-x8/user-manual#out-of-the-box-experience)
- If you are having issues with the adb shell, don't forget to try and use `sudo` and `su`
