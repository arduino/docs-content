---
title: 'Running a webserver container on the Portenta X8'
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

Using the Arduino Portenta X8 we can host a webserver and run wordpress using containers. This is a relatively simple way to configure and run your own webserver and wordpress page. 

## Goals

- Create the required container
- Run the container

### Required Hardware and Software

- [Arduino Portenta X8](https://store.arduino.cc/products/portenta-x8)
- USB-C cable (either USB-C to USB-A or USB-C to USB-C)

## Instructions

### Creating the container

To make be able to host our wordpress site we need to also run a webserver container. We will be using mariadb as our webserver container. This can run on the Portenta X8's architecture. We just need to write a ``docker-compose.yml`` file. Below you will find the entire file that will work with the X8.

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

Now we can create a directory on our X8 and put this docker-compose.yml file in there. 

### Install The Container

Navigate into the directory where the docker-compose.yml file is located. This can be done with a simple ``cd`` command. When you are in the correct directory we now need to run ``docker compose -d``. This will start installing the wordpress and mariadb containers. You can follow the progress in the terminal, it can take a while.

Once it is done you can check so that everything is running fine with ``docker ps -a``. This will show all your running containers and what port they are running on.

## Conclusion



### Next Steps



## Troubleshooting