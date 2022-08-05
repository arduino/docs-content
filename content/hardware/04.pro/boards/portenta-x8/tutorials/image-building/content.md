---
beta: true
title: 'How To build a custom image to your Portenta X8'
description: 'This tutorial teaches you how to compile a custom image for your Portenta X8 through USB'
difficulty: intermediate
tags:
  - Embedded Linux
  - Building
  - Foundries.io
author: 'Pablo Marquínez'
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

In this tutorial you will see how to build an image for the Portenta X8 with the files provided at Foundries.io.

***In this tutorial we are using Ubuntu LTS 20.04 inside the Windows Subsystem for Linux (WSL) through the Windows Terminal***

## Goals

- Make sure our Ubuntu machine has access to internet
- Provide your linux machine with the needed software
- Set up your computer with the required SSH keys and API Tokens
- Get the required files
- Configure the building settings
- Build the image

### Required Hardware and Software

- Supported linux distribution compatible with Yocto (https://docs.yoctoproject.org/ref-manual/system-requirements.html#supported-linux-distributions)
- Arduino Create account
- Arduino Pro Cloud Subscription. [Learn more about the Pro Cloud](https://www.arduino.cc/pro/hardware/product/portenta-x8#pro-cloud).
- Foundries.io account (linked with the Pro Cloud subscription)
- FoundriesFactory® ([Check the Getting Started tutorial](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box))

## Instructions

### Check Machine's Internet Access

As in this tutorial we are using Ubuntu 20.04 LTS on the Windows Subsystem for Linux (WSL), we need to check that we have access to the internet.

We can check it by pinging to a web server: `ping <URL>` 
![terminal_ping_fail.png](assets/terminal_ping_fail.png)

If you have a message like the one above, if you are using the *WSL* you should change the `/etc/resolv.conf` file to let the system know the correct DNS

Edit that file using the **nano** editor by typing: `sudo nano /etc/resolv.conf`
![](assets/terminal_nano_resolv.png)

Once its open you need to add a new line with `nameserver 1.1.1.1`
![](assets/terminal_nano_nameserver.png)

Then press `CTRL + O` and then `enter` to save the file and confirm.
To close `CTRL + X` to Exit the editor.

Now the machine should have access to the internet, check again pinging your webserver, we also made `cat /etc/resolv.conf` to output in the console the file text.

To exit the ping command, press `CTRL + C`

![](assets/terminal_ping_success.png)

### Folder Structure

We need to structure our directories, in this tutorial we used this structure:

```linux
home
└── builds
  ├── portenta-x8
  └── .bin
    └── repo
```

To achieve that lets navigate to the home directory with `cd ~` and create a directory `mkdir builds`.

### Dependencies
Make sure you have the latest index for dependencies with `sudo apt-get update` and the system with `sudo apt update`

Install available updates for your machines `sudo apt-get upgrade` and the system `sudo apt upgrade`
To be capable of building the image you will need some essentials packages (like python and some dependencies) that you can get with the following command.

**Only for Ubuntu:**
```linux
sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint3 xterm python3-subunit mesa-common-dev zstd liblz4-tool
```

***Check the needed dependencies at [Yoctoproject build host dependencies](https://docs.yoctoproject.org/ref-manual/system-requirements.html#required-packages-for-the-build-host)***


### Setup SSH Keys and Foundries API Token

It is required to have an SSH key and an API Token from **foundries** to get the needed image files

#### SSH Key

To setup your SSH Key go to the `.ssh` directory, `cd ~/.ssh`.

Crete a new key with `ssh-keygen -t rsa -b 4096 -C <yourEmail>"`

Follow the instructions, after that you should have two new files in the directory, `<yourSSHkey> and <yourSSHkey>.pub`

Now initialize the `ssh-agent` with `eval "$(ssh-agent -s)"`

Add your key with `ssh-add ~/.ssh/<yourSSHkey>`

***Make sure your `ssh-agent` is running, you can check the keys that your agent has with the command `ssh-add -l` if there is no key attached repeat the steps of adding the key and check if it was successfully added***

#### Foundries API Token

***This step is only mandatory if you want to get the source code from your foundries factory***

To get the needed files (source code) for compiling the image we need access to our foundries factory repository.

To make that happen browse to your [Foundries account > Settings > Api Tokens](https://app.foundries.io/settings/tokens/)
![](assets/foundries_API_tokens.png)

Press the "New Token" button and follow the instructions.
![](assets/foundries_API_token_create.png)

Now make sure you select the correct Scopes to "Use for source code access" and in Factory you chose your derived factory.
![](assets/foundries_API_token_create_scopes.png)

Once it has been generated copy the token shown
![](assets/foundries_API_token_created.png)

Switch to your machine and create a variable to store that token and add it on the Git global configuration of your machine, to do so:
```linux
API_TOKEN="<YourToken>"
git config --global http.https://source.foundries.io.extraheader "Authorization: basic $(echo -n $API_TOKEN | openssl base64)"
```

Check that your token has been properly configured by cloning the "containers" repository of your factory.
```
git clone https://source.foundries.io/factories/<factory>/containers.git
```

Make sure you clone the repository outside our `builds` folder, you can remove it after it has been cloned.

Also you can see your Git's configuration with `git config --global -l` you should see:
```
http.https://source.foundries.io.extraheader=Authorization: basic <yourToken on base64>
``` 

### Google's Repo Application

This application will handle the different repositories.

To install this software by going to the `.bin` directory, use `cd ~/builds`.

Use this commands to create a `.bin` folder and install the `repo` application inside and add it to the system PATH so you will be able to use the `repo` command anywhere.

```linux
mkdir -p .bin
PATH="${HOME}/builds/.bin:${PATH}"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/builds/.bin/repo
chmod a+rx ~/builds/.bin/repo
```

Now you should be able to access the command `repo` anywhere.

### Setting the Repository

Switch to your build directory and create a folder to store the source code
```
cd ~/builds/
mkdir portenta-x8
cd portenta-x8
```

Get your repository link
* Public repository [lmp-manifest](https://github.com/arduino/lmp-manifest) -> https://github.com/arduino/lmp-manifest.git
* Foundries derived factory repository `https://source.foundries.io/factories/<yourFactory>/lmp-manifest` -> `https://source.foundries.io/factories/<yourFactory>/lmp-manifest.git`

Then initialize the repository
```
repo init -u <repository> -m arduino.xml -b next
```


And download the files with `repo sync`

### Build the image

Set up the environment

You can set the `DISTRO` to `base`, `lmp` or `lmp-xwayland`
```
DISTRO=lmp-xwayland MACHINE=portenta-x8 . setup-environment
```

It will switch automatically to a new folder, now accept the EULA
```
echo "ACCEPT_FSL_EULA = \"1\"" >> conf/local.conf
```

Build the image
```
bitbake lmp-vendor-arduino-image
```

In case you want to use your computer at the same time, you should lower the used threads, to do so open conf/local.conf of your build image and lower this values
- `BB_NUMBER_PARSE_THREADS = "4"`
- `BB_NUMBER_THREADS = "4"`  
and add:
- `PARALLEL_MAKE = "-j 4"`

### Build the flashing tools

In order to flash your board you need to compile the needed tools, go back with `cd ~/builds/portenta-x8` and type the following commands:
```linux
DISTRO=lmp-mfgtool MACHINE=portenta-x8 . setup-environment
echo "ACCEPT_FSL_EULA = \"1\"" >> conf/local.conf
echo "MFGTOOL_FLASH_IMAGE = \"lmp-vendor-arduino-image\"" >> conf/local.conf
bitbake mfgtool-files
```

## Conclusion

Now you have all the required files to flash the image that you just built.

Please follow the [Flashing tutorial](image-flashing) in order to flash your device with your custom image, keep in mind you will need to use the files provided from this build, not the ones mentioned on the tutorial.

## Troubleshooting

- If you are having `do_fetch` issues try to check your system DNS and change it