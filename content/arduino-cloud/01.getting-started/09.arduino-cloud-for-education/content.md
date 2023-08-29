---
beta: true
title: 'Getting started with Arduino Cloud for Education'
description: 'Get a general overview of Arduino Cloud for Education and its features'
difficulty: intermediate
tags:
  - IoT Cloud
  - Education
  - RBAC
author: 'Gaia Castronovo'
software:
  - iot-cloud
---


## Introduction

The [Arduino Cloud for Schools](https://cloud.arduino.cc/schools/) is a tool that provides an online space for teachers and students. 

In this article, you will get a general overview of the major features of the Arduino Cloud for Education and the features *Free* and *School* plan can offer.

## Required Software

* [Arduino Cloud ](https://cloud.arduino.cc/plans#school)

## How to create an account

In order to get started with Arduino Cloud, you need to [have an Arduino account](https://auth.arduino.cc/login.). An **Arduino account gives** you **full access to all Arduino websites, apps**, and **services**.

If you do not have an account yet, feel free to create a new one. You can follow [this tutorial](https://support.arduino.cc/hc/en-us/articles/360016724040-Create-an-Arduino-account) for a step by step explanation on how to do it.

![Arduino Cloud login](assets/arduino-account-login.png "Arduino Cloud login")

After the registration is completed, you should verify your email address by clicking CONFIRM NOW in the email that was automatically sent to your inbox.

Now let's explore https://cloud.arduino.cc/home/:

![Arduino Cloud home](assets/cloud-home.png "Arduino Cloud Homepage View")

The Arduino Cloud for Education consists of **two main subscriptions**:

* **Free Plan**  
* **School Plan** 

By default, any new user who created an Arduino account has access to Arduino Cloud with a *Free Plan*.

## Free Plan

### Access to free online courses content

Once you've logged in, you are free to check out our free content in `Arduino Cloud > home > Courses` or click [here](https://cloud.arduino.cc/home/courses). 

![free courses in the cloud](assets/free-courses.PNG "Free Content Courses in the Cloud")

In this section you get access to several free online courses, for different age groups and topics. This library of courses get widen and extended regularly with new releases.

***With a School Plan you unlock access to extra online courses.***

## Manage Your Spaces

In your Arduino Cloud free plan comes with two **spaces** by default:

![free courses in the cloud](assets/join-space.PNG "My Cloud - default Space")

* **My Cloud**. My Cloud is an *automatically* created private space once joined Arduino Cloud. You can use this space for personal projects you do not want to share with all your class. This space is free and includes *two Things*, unlimited dashboards, 100MB of Sketch storage, 1 day data retention by default.
* **New shared space**. A *Shared Space* is a space you can use with all your students. There is no limit in the number of members, who can all access the resources within its space.
* **Join Space** - copy paste here the space code that another admin or teacher shared with you to join their space. Like in the image below.

![join space](assets/joinspace.PNG "Join Space - Insert Code")

### Create a shared space

Open the top-right space selection menu and click on *New shared space*.

![New shared space creation](assets/join-space-highlight.png "New shared space creation")

Then you will be asked which type of Shared Space you want to create (i.e. For Business or For Education). Click on **For Education** and proceed with creating a online space to share with your students or other colleagues.  

![Shared Space type selection](assets/shared-space-type-selection.png "Shared Space Type Selection")

Fill in additional information.

![Fill in school information for the new Space](assets/fillinschoolinfo.PNG "Fill in School Information")

Congratulations! Now you own a Shared Space linked to your Arduino account.

### Switch Between Spaces

You can switch to other Shared Spaces at any time using the corresponding menu, which you can find at the top right-hand corner, and click on it.

***With a Free Plan or School Plan there is no limitations in the number of Shared Space you can have.***

![shared space vs private](assets/my-school.PNG)

### Change Shared Space Settings

To change the current settings of your Shared Space, navigate to the **General Settings** tab using the sidebar.

![Shared Space settings](assets/shared-space-settings.png "Shared space settings")

Here you can edit for example your displayed name or change the logo of your Space.

### Invite Members Into Your Space

To add more members to your Shared Space, use the sidebar to navigate to the **Members** item under **Your space** group.

![List of Shared Space Members](assets/members-home.png)

There you will find the complete list of all members who have access to your Shared Space, as well as the current role of each member. 

You can add members in **three possible ways**:

1. Type the **email addresses** of each user and define which role they will cover in your Space based on the available options. Click on **Invite**. The users you added will get the invitation by email with a link to join your Shared Space. 

2. You can invite your students to the Space through **Code** invitation (check *Join Space* explained above).

3. **Copy pasting the link** and share it with the whole class.

![Invite members through email](assets/add-member.PNG)

### Role types

There are [three role types](https://cloud.arduino.cc/home/roles-permissions) in Arduino Cloud for Schools: 

* Admin
* Teacher
* Students

By default the member who has activated the plan and created the workspace is set as *Admin*. It is possible to have multiple Admins with same permissions. The admin has full control of the rights/permissions each user has in the Shared Space:

The list of supported roles and corresponding permissions can be found here:

https://cloud.arduino.cc/home/roles-permissions

Important to remember are **Student role limitations:**

* They are not allowed to add new members to your School organization
* They are not allowed to assign members roles
* They are not allowed to view the Plan Management and Payment information

![school user roles differences](assets/users-roles.PNG)

***There is no limitation on the numbers of members you can add into a Shared Space.***

## CLOUD APPS

On the left menu bar in https://cloud.arduino.cc/home/ are listed the Cloud apps:

* Web Editor
* IoT Cloud
* Triggers

![Cloud APPS](assets/leftsidebare.PNG)

With a *Free* *Plan* you have access both to Arduino Web Editor and Arduino IoT Cloud, with **different limitations**. We'll discuss more in details below what those limitations are.

With a *Free Plan* you won't have access to Cloud Triggers, so you'll see something similar to this:

![Triggers with a free plan](assets/triggers-free-plan.PNG)

If you want to unlock this function, you'll need to upgrade to a [School Plan](https://digital-store.arduino.cc/education/purchase).

### What is Arduino Web Editor?

[Arduino Web Editor](http://create.arduino.cc/editor) allows you to **write code** and **upload sketches** to any Arduino board after installing a **[simple plug-in](https://create.arduino.cc/getting-started/plugin/welcome) for your browser**. Your Sketchbook will be stored in the Cloud and accessible from any device. If you have a *Free Plan* you can store to a maximum of 100 MB of sketches. You can import your Sketchbook via a .zip file. Arduino Web Editor is part of Arduino Cloud, that simplifies a project by bringing all the different tools you need together in one place. This is a complementary solutions for schools or institutions that don't want to install [Arduino IDE](https://www.arduino.cc/en/software) to program their devices.

If you want to know more about Arduino Web Editor [visit this link](https://docs.arduino.cc/arduino-cloud/getting-started/getting-started-web-editor).

A **lite version of the Web Editor** is included in the Arduino IoT Cloud, under `Things > Sketch`, which is actually a preview of a sketch saved on the Web Editor. 

![Arduino IoT Cloud lite Editor](assets/gs-thing-editor.png)

***The Arduino Cloud Free Plan allows a maximum online space to store your sketches and libraries of 100 MB and a maximum of 25 code compilations per day by default.                                                                                                                                                                                    The Arduino Cloud School Plan allows unlimited online storage space and unlimited code compilations for your sketches.***

You can check how many times you've left to verify and upload your program from the [Cloud home](https://cloud.arduino.cc/home/), on the `Feature Usage` menu on the left bottom corner.

![feature usage menu](assets/features-usage.png) 

***

### What is Arduino IoT Cloud?

Arduino IoT Cloud is an easy-to-use Internet of Things application platform. Arduino IoT Cloud makes the creation of connected objects quick, simple, and secure. You can connect multiple devices and allow them to exchange real-time data. You can also monitor them from anywhere using a simple user interface. It is integrated into your Arduino Cloud Space. 



## IoT Projects Management

In your IoT projects with Arduino you'll need **three elements**:

1. [The **Arduino IoT Cloud**](https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started)
2. [The **Arduino Create Agent**:](https://create.arduino.cc/getting-started/plugin/welcome) the middle man between Arduino’s Web Editor, Arduino IoT Cloud and your computer. It allows you to use the browser to edit and deploy sketches to your Arduino board, and is required to be installed when using this kit.
3. **A device** of your choice.

### Setup a Device in Arduino IoT Cloud

The Arduino IoT Cloud is compatible with multiple Arduino boards or devices based on the ESP32 / ESP8266 microcontrollers. The Arduino IoT Cloud currently supports devices connected via Wi-Fi®, Ethernet, LoRaWAN® (via The Things Network), and cellular connectivity. You can check the [full list of compatible hardware here](https://support.arduino.cc/hc/en-us/articles/360016077320-What-devices-can-be-used-with-Arduino-IoT-Cloud-).

If your device is compatible with Arduino IoT Cloud, you can start to *Setup your Device* in your Shared Space by connecting it to your computer through a USB cable.

![Device selection](assets/device-onboarding.png "Device selection")

The agent will start looking for your board. When your board has been found, the following screen will appear. Click on **Configure**.

![set up board in the cloud](assets/setup-cloud-board.png)

Select a board name to be able to correctly identify your device and click on **Next**.  

![Give a name to the device](assets/name-device.png)

Define the connection type you want to use with your board and click on **Next.** 

If the onboarding proceeds as expected, the following page will appear confirming that your device has been successfully set up.

![successfully set up device](assets/congratulations-setup.png)

The `Devices` tab displays the name, status, and linked `Things` for each of the configured devices. Clicking on the device allows for renaming it, as well as accessing more information about the device, such as its ID number, type, FQBN, serial number, firmware version, linked Thing, latest activity, and the date when the device was added.

The device status indicates whether it is connected to the Arduino IoT Cloud (online), or not connected (offline).

![List of devices in your Arduino IoT Cloud](assets/devices-list.png "List of devices in your Arduino IoT Cloud")

### Link A Thing To Your Device

To use a device in IoT Cloud, you need to [create a Thing](https://create.arduino.cc/iot/things), or associate it to an existing Thing. A Thing is the digital twin of your device, like a reference to the actual hardware used to implement them. Each Thing is represented by a collection of properties, the configuration of some variables and other settings, as well as the history of the data collected for those variables.

To create a Thing, click on **Create Thing** next to the device of your interest, and your Thing will be automatically created for you. 

![create a thing from device tab](assets/create-a-thing.png)

If you want to explore more on how Things work, check [here](https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started#3-creating-a-thing).

***With a Free Plan you can only connect two Things with the IoT Cloud at the a time.                                    With a School Plan each member you've included in your plan can connect up tp five Things to a Device.***

The image  below highlights the important elements that we will use frequently. Each number is explained below the image.

![things overview](assets/edu-tutorial-thing-overview.png)

1. **Name of thing:** By clicking on "Untitled", we can rename our thing to anything we like. 
2. **Navigation menu:** This helps to navigate between things, dashboards and devices. 
3. **Thing tab:** There are two different tabs: **Setup**, **Sketch** and **Metadata**. The setup is the current view, while the sketch works as the Arduino IDE where the Serial Monitor is detachable.
4. **Variables:** By clicking the **Add variable** button, we can create variables that will be incorporated in a sketch later on. These variables can then be linked to a dashboard.
5. **Device configuration:** To associate our Thing with a device, detach or change it.
6. **Network configuration:** Here, we will enter the name and password of our Wi-Fi network, which will be necessary to communicate with the IoT Cloud.

### Filter your Things or Devices

You can search and filter among your Things/Devices by going to **Things** or **Devices** tab in [Arduino IoT Cloud](https://create.arduino.cc/iot/devices)

![Search and filter among devices](assets/search-things.png "Search and filter among devices")

If you want to **create your tag**, which you can use as a filtering option, go to Things tab, click on the Thing you would like to tag and go to the **Metadata** tab as shown in the figure below. Click on **Add**. You can add an unlimited number of tags to each Thing.

![Thing metadata](assets/thing-metadata.png "Thing metadata").



You can go back to the Things tab and start filtering your Things according to the new tag you have just created.

![New tag filtering](assets/new-tag-filtering.png "New tag filtering")

### Variables

In order to retrieve and store information we need to create Variables in the Arduino IoT Cloud are very similar to the variables we create in a regular sketch. 

![variables in the Arduino IoT Cloud](assets/variables.PNG)

When we create variables here, they are automatically generated in a sketch, and when we upload the code to the board, the variables used in the sketch synchronize with the variables in the cloud.

To learn more on the different types of Variables and their features go to [this tutorial](https://docs.arduino.cc/arduino-cloud/getting-started/cloud-variables).

***The Arduino Cloud Free Plan allows a maximum number of 5 variables per each Thing by default.                                                                                                                                                                                    The Arduino Cloud School Plan allows unlimited number of variables per each Thing.***

### Dashboards

Dashboards are used to visualize real-time data and to enable direct interaction with the board through the IoT Cloud. Go to `Dashboard` and click the green button `Create`. We'll link `Variables` we've created before to a **Widget**.

With a *Free Plan* is not possible to share your Dashboard with other users.

![Dashboard example](assets/dashboard-example.png "Dashboard example")

Widgets are the ‘building blocks’ of a dashboard, and are directly linked to our properties. They allow us to visualize the data we get from sensors. There are several different widgets: gauges, sliders, switches, color palettes, messenger and more.

![widgets selection](assets/widgets.PNG)

If you want to learn more on how to customize your dashboard and widgets, check [this link](https://docs.arduino.cc/arduino-cloud/getting-started/dashboard-widgets).

***If want to use to Advanced Chart Widget for your IoT projects, that allows you to visualize multiple variables in one chart, you'll need access to the School Plan***

![advance widget](assets/advanced-chart.gif)

You can read more about Advance Chart Widget [here](https://docs.arduino.cc/arduino-cloud/features/advanced-chart).

### Data Export

Arduino Cloud, both with free or School plan, allows any user to download historical data from Arduino IoT Cloud Things and Variables. The data are downloaded in **.csv** format to be ready for further evaluation or manipulation.

***The Arduino Cloud Free Plan allows only 1 day of data retention by default.                                     
The Arduino Cloud for School Plan includes 6 months of data retention by default; this means that your data will be available and downloadable from your Arduino Cloud account for 6 months.***

To start exporting your data locally, navigate into one of your dashboards on the [Arduino IoT Cloud](https://create.arduino.cc/iot/dashboards). While inside a dashboard, press the **Download** icon in the upper right corner. This will open a new window that will allow you to select which historical data you would like to download.

![Download icon](assets/download-button.png "Download icon")

From here you can select all the variables you want to download by checking the boxes as well as the time frame you are interested in.

When you have selected the data, click on the **Select Data Source** button.

![Export your data](assets/download-data.png "Exporte your data")

At this point, click on **Get data** to receive your data by email.

![Get your data](assets/get-data.png "Get your data")

You will get an email like the one below with a link allowing you to download all your data.

![Link to download your data](assets/email-data.png "Link to download your data")

You are now ready to monitor and manipulate all your Cloud data.

## School Plan

As an Educator you might need:

* To create and store in the Cloud more sketches
* To collaborate in your IoT projects sharing real-time data dashboards and programs
* To integrate your IoT Project with an LMS tool
* To customize your projects with additional functionalities provided by APIS

### Buy a School Plan



### Sharing Dashboards

With a School Plan is possible to share any Dashboard with anyone. Go to the [Dashboard](https://create.arduino.cc/iot/dashboards) tab in Arduino IoT Cloud, click on the three dots on the Dashboard you would like to share.

As shown in the image below you can either send it directly to the user's *email* or *username*, or *share the link* with your class.

![Share your dashboard](assets/dashboard-sharing.png "Share your dashboard")

You can check [this tutorial](https://docs.arduino.cc/arduino-cloud/features/sharing-dashboards) to learn more about sharing a dashboard.

### Cloud Triggers

![cloud triggers with school plan](assets/available_triggers.png)

Triggers are used in many IoT projects to monitor specific variables within your Things and receive notifications.  This is super useful when you monitor data and you need to know about any change as soon as it happens. This could be anything from different values in environmental monitoring or something security related such as movement detection. 

***With a School Plan you have 10 notifications per day for 10 members of your Shared Space. There is no limitations on how many triggers you can create for your projects and you can combine them together.***

To learn how to use triggers that allow you to send notifications based on set conditions, [read this tutorial](https://docs.arduino.cc/arduino-cloud/features/triggers).

### Google Classroom Integration

With a School plan any educator that is part of a Shared Space can create assignments and share a sketch directly from the Arduino Web Editor, that is part of the Arduino Cloud apps.

![share sketch with google classroom](assets/google-integration-arduino-cloud02.png)

It is also possible to share the content of a course or give it as an assignment.

![share content with google classroom](assets/google-classroom-content-share.png)

### Arduino Cloud API

For more customized IoT projects and classes the *School Plan* offers full access to Arduino IoT Cloud back-end offering to control Things and Devices via Arduino rest APIs in [Javascript](https://www.npmjs.com/package/@arduino/arduino-iot-client), [Python](https://pypi.org/project/arduino-iot-client/), or [Go](https://github.com/arduino/iot-client-go). With Arduino rest APIs, you will be able to manage up to **10 requests per second**, guaranteeing stable data sharing.

With APIs, you can interact with any element of the Cloud: data, devices, dashboards, and web properties. and receive data from an external service. 

To use the APIs, you need to create an API Key Token in the API Keys section of your Space.

![cloud api keys](assets/api-keys.png)

If you want to start creating your own API Keys Token, take a look at [this tutorial](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-iot-api) and [this documentation](https://www.arduino.cc/reference/en/iot/api/).

### Over the Air Uploads

This feature, included in the Arduino Cloud *School Plan*, allows you to upload programs wirelessly to your Arduino boards. If you have a compatible board connected to a Wi-Fi®/Ethernet network and configured to work with OTA, you won’t need to physically connect the board to the computer in order to upload new sketches to it. 

 Check [this tutorial](https://docs.arduino.cc/arduino-cloud/features/ota-getting-started#how-does-it-work) to learn how to upload your program remotely to your board.

### Billing

School plan is specifically designed for institutions that aim to cover a larger amount of users. The billing account can be managed by a single Arduino account that then will grant access to different users and assign a role.

### Junior Account

The content courses included in the School Plan are only partially available for minor users. They will get access only to COPPA compliant courses. If your students are **under the age of 14**, they need parental consent to sign up for an Arduino account. We recommend to read [this tutorial](https://support.arduino.cc/hc/en-us/articles/360022234360) to learn how to manage a Junior account. Arduino Education provides [several solutions for middle school](https://www.arduino.cc/education/middle-school/) students.



## Arduino IoT Cloud Remote

It allows you to monitor your dashboards anywhere, anytime, from a **mobile device** i.e smartphone or tablet and use your dashboards on the go with the *free* Arduino IoT Cloud Remote App. Download it from either [Google Play Store](https://play.google.com/store/apps/details?id=cc.arduino.cloudiot&hl=en&gl=US) or the [Apple App Store](https://apps.apple.com/us/app/arduino-iot-cloud-remote/id1514358431) depending on your device.

***Do you want to get started with IoT Remote App? Read [this tutorial](https://docs.arduino.cc/arduino-cloud/tutorials/iot-remote-phone-sensors#phone-setup).***

## Arduino Cloud Tutorials

You can find more tutorials on the [Arduino IoT Cloud documentation page](https://docs.arduino.cc/arduino-cloud/).

