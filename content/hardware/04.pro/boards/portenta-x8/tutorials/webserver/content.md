---
title: 'Running Wordpress on the Portenta X8'
description: 'Learn how to run a database and wordpress container on the Portenta X8'
difficulty: easy
tags:
  - containers
  - Docker
author: 'Benjamin Dannegård'
software:
  - Terminal
  - Docker
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

Using the Arduino Portenta X8 we can host a webserver and run wordpress using containers. This is a relatively simple way to configure and run your own webserver and wordpress page. We will then access the wordpress site on the X8 and begin setting it up.

## Goals

- Create the file to install docker containers
- Install and run the containers
- Connect to the Wordpress container running on the X8

### Required Hardware and Software

- [Arduino Portenta X8](https://store.arduino.cc/products/portenta-x8)
- USB-C cable (either USB-C to USB-A or USB-C to USB-C)

## Instructions

### Creating the docker-compose.yml File

The Wordpress container we will be using also requires a webserver container. We will be using **mariadb** as our webserver container. This container can run on the Portenta X8's architecture. All we need to being installing these containers is to write a `docker-compose.yml` file. This file will contain information about what image we want to install and some important configuration information. Such as the username for the database, password, timezone and database name. The same goes for the Wordpress container, it will contain the password and username, we will also enter the database host name and which container it will use as the database. If you would like to change any password to a more secure one, feel free to replace the generic ones that are stated in the file below.


### The Complete docker-compose.yml File

In this section you can find the complete **docker-compose.yml** file that we will be using for this tutorial.

```linux
version: "3.9"
    
services:
  db:
    image: lscr.io/linuxserver/mariadb:latest
    container_name: mariadb
    environment:
      - PUID=1000
      - PGID=1000
      - MYSQL_ROOT_PASSWORD=wordpress
      - TZ=Europe/London
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped
    
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    volumes:
      - wordpress_data:/var/www/html
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
volumes:
  wordpress_data: {}
  db_data: {}
```

Now lets create a directory on our X8 and put this **docker-compose.yml** file on our device.

### Installing The Containers

First we create a directory where we want put our **docker-compose.yml** file. Using the `mkdir` command we will create a directory named wordpress-test. Navigate into this directory with a simple `cd` command. Either copy the docker-compose.yml file into this directory or create it directly here.

[cd into dir]()

When you are in the correct directory we now need to run `docker compose up`. This will start installing the **Wordpress** and **mariadb** containers. You can follow the progress in the terminal, it can take a while. Once it is done we can connect to the device and site.

[progress of install]()

### Connecting to the Wordpress Site

To connect to the Wordpress setup site we simply need to access it with our Portenta X8s unique id and port. So for example `http://<uuid>.local:<port>`, where you would substitute the `<uuid>` with your Portenta X8s unique id and the port chosen for the wordpress container with `<port>`. The `<uuid>` can be found on the setup page that is showed in the (Getting started tutorial)[], you can also see it in the terminal when running `adb`. Or you can go to `http://192.168.7.1:8000` if you use Windows and Linux, on MacOS use `http://192.168.8.1:8000`.

[Highlight url]()

When you connect you should se more text being printed in the terminal. Like shown in the image below.

[Terminal with connection]()

Now you should see a webpage like on the next image.

[Wordpress site]()

You are now free to go through the wordpress set up process and configure it.

## Conclusion

In this tutorial we went through how to install and run a wordpress and database container on the Portenta X8. We then accessed the Wordpress site on our X8 through our web browser.


### Next Steps



## Troubleshooting

- If the containers aren't installing or running correctly check if there are any other containers currently running on the same ports as the ones used by the wordpress container. You can check this with ``docker ps -a``.
- If there is any issue running docker commands, make sure you are using ``sudo`` before the commands.
- If you can't connect to the site when everything is running you can double check the X8s ip address. Run the command `ip s a` in the adb shell. ????