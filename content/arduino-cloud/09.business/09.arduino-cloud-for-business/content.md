---
beta: true
title: 'Getting started with Arduino Cloud for Business'
description: 'Get a general overview of Arduino Cloud for Business and its features'
difficulty: intermediate
tags:
  - Arduino Cloud
  - Fleet Management
  - RBAC
author: 'Marta Barbero'
software:
  - iot-cloud
---


## Overview

The [Arduino Cloud for Business](https://www.arduino.cc/pro/software-arduino-iot-cloud/) is an Arduino Cloud plan dedicated to companies and industrial clients wanting enhanced features in terms of device management, Role-Based Access Control (RBAC), fleet management, and safe remote access.

In this article, you will get a general overview of the major features of the Arduino Cloud for Business.

If you are not familiar with Arduino Cloud, we strongly recommend you to take a look at the following documentation:

* To find all tutorials & articles, visit the [Arduino Cloud Documentation page](https://docs.arduino.cc/cloud/iot-cloud).
* For API & SDK Documentation, visit the developer reference at [Arduino Cloud API](https://www.arduino.cc/reference/en/iot/api/).

## Goals

* Get in-depth information about how the Arduino Cloud for Business works
* Learn about the multiple dedicated features Arduino Cloud for Business provides
* Learn how to get started with Arduino Cloud for Business

## Required Software

* [Arduino Cloud for Business](https://cloud.arduino.cc/plans#business)

## Purchase An Arduino Cloud For Business Plan

In order to get started with Arduino Cloud for Business, you need to [subscribe to a plan](https://cloud.arduino.cc/plans#business).

The Arduino Cloud for Business plan consists of two main subscriptions:

* **Enterprise Base Plan.** It includes all the Arduino Cloud for Business features, like data plane, fleet management, Role-Based-Access-Control, Cloud Editor with Over-the-air updates, IoT Cloud with dashboards, etc. Multiples of 50 devices can be connected under the Enterprise Base Plan – and you can always [contact our team](https://www.arduino.cc/pro/contact-us) for a tailored plan to accelerate your IoT solutions.

* **Optional Add-Ons.** To address additional needs, Arduino Cloud for Business can be customized with optional add-ons. Check the [dedicated section](#optional-add-ons) of this tutorial to learn more.

If you do not need any tailored plan, go to [Arduino Cloud for Business page](https://cloud.arduino.cc/plans#business) and select **Purchase**. You will be then asked to log in with your Arduino credentials. If you do not have an account yet, feel free to create a new one.

![Arduino Cloud login](assets/arduino-account-login.png "Arduino Cloud login")

It is now time to customize your plan. Select the billing frequency you prefer and the number of Things (and so devices) that you would like to connect with your Arduino Cloud for Business workspace. Click on **Continue**.

![Customize your plan](assets/plan-customization.png "Customize your plan")

Proceed by marking the optional add-ons you may need in your projects and click on **Add billing information**. To learn more about these add-ons, check the [dedicated section](#optional-add-ons) of the present getting started guide.

![Add-ons section](assets/add-on-selection.png "Add-ons section")

In the next steps, add all your billing and payment information and then purchase your plan.

Now you are ready to get started with your brand new Arduino Cloud for Business plan.

Check the next sections to understand how to set up your account and which features are included in your plan.

## Manage Your Spaces

Once your plan has been successfully activated, you will be asked to define the company/space name for your workspace. You are free to modify it later by navigating to `Arduino Cloud > Space Settings > General` and clicking on `Edit Info` within the three dots located at the top right side.

![Create new shared space](assets/create-new-space.png "Create new shared space")

Your Arduino Cloud for Business plan comes with two spaces by default:

* **My Cloud**. My Cloud is an automatically created private space once the Arduino Cloud for Business plan is purchased. You can use this space for personal projects you do not want to share with all your team. This space is free and includes two Things, unlimited dashboards, and 100MB of Sketch storage by default, but it can be further extended and customized within *My plans* settings. Have a look at the [Arduino IT Cloud Getting Started](https://docs.arduino.cc/arduino-cloud/guides/overview) if you would like to start using your private space.

* **Shared Space**. A *Shared Space* is a company space you can use with all your team. It can have any number of members, who can all access the resources within its space. The access level and specific permissions can be customized by the *Space Admin* (see [Invite members into your space section](#invite-members-into-your-space) to learn more).

In the next sections, you will learn more about Shared Space features and functionalities.

### Switch Between Spaces

If you are the owner of more than one Shared Space or have been invited into a Shared Space by another user, you can switch to other Shared Spaces at any time using the corresponding menu.

Move your mouse over the account button, which you can find at the top left-hand corner, and click on it. All the Spaces you have access to will be listed there.

![Switch between Spaces](assets/switch-spaces.png "Switch between Spaces")

If you have four shared spaces or more, it will show you a button named **Switch space**.

![Switch Space Selector](assets/switch-spaces-multiple-option.png "Switch Space Selector")

Clicking on the **Switch space** option will display all your spaces within the account.

![Multiple Spaces](assets/switch-spaces-multiple.png "Multiple Spaces")

The Space-Selector shows you which space you are currently working on at any time, in this case, *Test*. To switch to another Space, select the space you would like to work on.

### Change Shared Space Settings

To change the current settings of your Shared Space, navigate to the **Space Settings** tab using the sidebar.

![Shared Space settings](assets/shared-space-settings.png "Shared space settings")

There, you will find multiple options to customize your Shared Space:

* **General** tab to view shared space information and to edit space name
* [**Custom Branding**](#custom-branding) to assign custom logo
* [**Manage Members**](#invite-members-into-your-space) for space member management
* [**Roles & Permissions**](#members-types) for Role-Based-Access-Control management
* **Plan Usage** to view features usage

### Create Additional Spaces

The Arduino Cloud for Business plan allows you to create and manage one Shared Space and one Private Space. If you need additional Spaces, you have to purchase a new Arduino Cloud plan. Check the available plans [here](https://cloud.arduino.cc/plans).

### Custom Branding

The Arduino Cloud for Business provides the option to configure custom branding for your spaces, allowing you to personalize the appearance of your cloud environment with white labeling. This feature lets you customize branding elements to reflect your company's identity, including logos, URLs, and authentication methods.

To access the **Custom Branding** option, navigate to the **Space Settings** on the left sidebar of the Cloud space.

![Custom Branding - Space Settings](assets/custom-branding-1.png "Space Settings")

Select the **Custom Branding** page from the left sidebar inside the **Space Settings**. This page offers **Basic** and **Advanced** options for configuring custom branding and white labeling.

Under the **Basic** option, you can customize your logo and toggle the visibility of the Arduino logo on the sidebar.

![Custom Branding - Basic Options](assets/custom-branding-2.png)

Two configuration blocks will be present to set custom branding:

  - **Your Logo:** You can upload your custom logo in `JPEG` or `PNG` format, with a maximum size of 500 kb. The custom logo will be displayed on the Arduino Cloud sidebar and home page. The **Icon Logo** is used on the platform's sidebar, while the **Horizontal Logo** is used on your space's Home Page. It is recommended to use a ratio of *1:1* for the **Icon Logo** and a ratio of *3:1* for the **Horizontal Logo**.

  - **Arduino Logo:** You can toggle the visibility of the Arduino logo on the sidebar.

If you have applied a custom branding logo and toggled the Arduino logo, your **Basic** configuration page will resemble the following image:

![Custom Branding - Complete Basic Options](assets/custom-branding-2-1.png)

Once the configuration is set, your **Home** page will reflect your custom branding:

![Custom Branding - Home Page with Custom Logo](assets/custom-branding-2-2.png)

For customizations related to *white labeling*, navigate to the **Advanced** tab within the **Custom Branding** page.

![Custom Branding - Advanced Options](assets/custom-branding-3.png "Advanced Options")

In this section, you will find features that allow *white labeling*:

  - **Custom URL:** You can set a custom URL and a name for your site, usually the name of your company, which will be shown as the page title. Avoid using special characters or spaces for the custom subdomain. Once submitted, the custom subdomain will be validated, and a quick preview will be generated.

![Custom Branding - Custom URL (White Labeling)](assets/custom-branding-3-1.png)

  - **Social Sign-in:** By enabling *Social Sign-In*, you can offer faster authentication to your app. The available options for *Social Sign-In* are Google, GitHub, and Apple. **To enable this option, You must first complete the _Custom URL_ information. Otherwise, this feature will not be available.**

![Custom Branding - Social Sign-in (White Labeling)](assets/custom-branding-3-2.png)

  ***The __Social Sign-in__ options can be disabled later by toggling off this option. Be cautious, as it will remove the user's associated account and data corresponding to the authentication method.***

![Custom Branding - Disabling Social Sign-in (White Labeling)](assets/custom-branding-3-4.png)

With these configurations, you will have a complete custom branding setup with white labeling for your Cloud space. Remember to click **Save** to finish the setup.

### Invite Members Into Your Space

To add more members to your Shared Space, use the sidebar to navigate to the **Manage Members** item under **Space Settings**.

![List of Shared Space Members](assets/members-home.png "List of Shared Space Members")

There you will find the complete list of all members who have access to your Shared Space, as well as the role of each member.

#### Members Types

There are multiple role types in Arduino Cloud for Business to allow the admin to have full control of the rights/permissions each user has in the Shared Space. In this way, the admin can set up Role-Based-Access-Control (RBAC) by assigning profiles and sharing with any number of users.

By default the member who has activated the plan and created the workspace is set as Admin. The Role-Based-Access-Control can support multiple Admins with same permissions.

The table below reports the list of supported roles and corresponding permissions.

| **Things**                        | **Admin** | **Editor** | **Service Account** |
|-----------------------------------|-----------|------------|---------------------|
| Create/edit/delete things         | X         | X          |                     |
| Create/edit/delete variables      | X         | X          |                     |
| Create/edit/delete webhooks (API) |           |            | X                   |
| View Things                       | X         | X          |                     |
| Edit sketches                     | X         | X \[1\]    |                     |
| Change associated devices         | X         | X          |                     |
| Change network                    | X         | X \[2\]    |                     |

| **Dashboards**                | **Admin** | **Editor** | **Service Account** |
|-------------------------------|-----------|------------|---------------------|
| Create/edit/delete dashboards | X         | X          |                     |
| Create/edit/delete widgets    | X         | X          |                     |
| View dashboards               | X         | X          |                     |
| Widgets interaction           | X         | X          |                     |
| Download historic data        | X         | X          |                     |

| **Devices**             | **Admin** | **Editor** | **Service Account** |
|-------------------------|-----------|------------|---------------------|
| Add/edit/delete devices | X         | X          |                     |
| View devices            | X         | X          |                     |

| **Members Management**      | **Admin** | **Editor** | **Service Account** |
|-----------------------------|-----------|------------|---------------------|
| Add members to organization | X         |            |                     |
| Assign members’ roles       | X         |            |                     |

| **Plan Management** | **Admin** | **Editor** | **Service Account** |
|---------------------|-----------|------------|---------------------|
| Payment             | X         |            |                     |

\[1\] It can add/remove only Sketch owner.
\[2\] It can add/remove only Thing owner.

In addition to editor role, we added a Service Account, which should be one dedicated to the creation and maintenance of API Keys Tokens. We recommend having at least one Service Account for each Shared Space and linking it to a non-personal email account. In this way, API Keys do not risk getting lost with the cancellation of a personal email address.

#### Add A New Member

To add a new member, click on **ADD MEMBERS** in the top right-hand corner.

![Add a new member](assets/members-home.png "Add a new member")

The following page will appear to allow you to send an email invitation to all the members you would like to join your Space.

![New member invitation](assets/new-member-invitation.png "New member invitation")

Type the email addresses of all your team and define which role they will cover in your Space based on the available options. Click on **INVITE**.

The users you added will get the invitation by email with a link to join your Shared Space. You are now ready to start working all together on your Arduino Cloud projects.

## Device Management

The Arduino Cloud for Business allows for device management with Over-The-Air updates, secure provisioning to connect boards leveraging their secure element, and easy verification of their status (connected, not connected) and maintenance.

### Compatible Hardware

The Arduino Cloud for Business is compatible with multiple Arduino boards or devices based on the ESP32 / ESP8266 microcontrollers. The Arduino Cloud currently supports devices connected via Wi-Fi®, Ethernet, LoRa®-based networks (via The Things Network), and cellular connectivity.

To check the full list of compatible Hardware, have a look at [this tutorial](https://docs.arduino.cc/arduino-cloud/guides/overview).

### Device Provisioning

Arduino Cloud allows you to securely provision your devices through two different tools:

* **Arduino Cloud.** Arduino Cloud is an App integrated into your Arduino Cloud Space, guaranteeing straightforward provisioning of Arduino or other Cloud-compatible devices. It is provided with a dedicated User Interface which will guide you step-by-step during the onboarding process. This is a great choice in case you need to provision a few devices or you are not an advanced user.

* **Arduino Cloud CLI.** As explained in [this section](#arduino-cloud-cli), Arduino has developed a command line tool enabling the access of all Arduino Cloud features from a terminal window. Arduino Cloud CLI is the right choice when you need to provision multiple devices at the same time and you are an advanced user.

#### Device Provisioning With Arduino Cloud

If your device is compatible with Arduino Cloud, you can start provisioning it into your Shared Space by connecting it to your computer through a USB cable.

In addition, Arduino Cloud requires your computer to have the [Arduino Create Agent installed](https://create.arduino.cc/getting-started/plugin/welcome).

Let's begin by relocating to your Shared Space when you are all set up correctly.

![Arduino Cloud button](assets/iot-cloud-button.png "Arduino Cloud button")

Go to the **Devices** item within the sidebar, where it will list all the added devices. Since no devices have been added yet, it will show the option to add a device as the main option on the page.

![Devices page](assets/devices-list-page.png "Devices page")

click on **ADD DEVICE** and decide which type of device you would like to onboard. In this case, a Portenta H7 board will be used.

![Device selection](assets/device-onboarding.png "Device selection")

The agent will start looking for your board. When your board has been found, the following screen will appear. Click on **CONFIGURE**.

![Device configuration during provisioning](assets/portenta-found.png "Device configuration during provisioning")

Select a board name to be able to correctly identify your device and click on **NEXT**.  

![Device name configuration](assets/device-name-configuration.png "Device name configuration")

Define the connection type you want to use with your board and click on **NEXT**. The agent will start securely provisioning your device by leveraging the secure element embedded in your board. This way, your security keys will be stored in the secure element and full data encryption will be guaranteed during data exchanges between Arduino devices and the Cloud.

***If you want to learn more about security in Arduino Cloud, please check the [dedicated documentation](https://docs.arduino.cc/arduino-cloud/features/security-considerations).***

If the onboarding proceeds as expected, the following page will appear confirming that your device has been successfully provisioned in Arduino Cloud.

![Successful provisioning](assets/provisioning-success.png "Successful provisioning")

You can now check its status under the Devices section. This section displays the name, status, and linked Things for each of the configured devices. Clicking on the device allows for renaming it, as well as accessing more information about the device, such as its ID number, type, FQBN, firmware version, associated Thing, latest activity, and the date when the device was added.

The device status indicates whether it is connected to the Arduino Cloud (online), or not connected (offline).

![List of devices in your Arduino Cloud](assets/devices-list.png "List of devices in your Arduino Cloud")

If you click on the added device, it is possible to look into its details. The details can be its device properties, device status history, and device Over-The-Air updates.

![Device detail](assets/device-detail-information.png "Device detail")

### Assign A Thing To Your Device

As already said, once a device is successfully configured, it appears in the "Devices" list and can be used to create a Thing, or can be linked to an existing Thing.

To use your devices in IoT Cloud, you need to associate a Thing with each of them. A Thing is the digital twin of your device, holding the configuration of some variables and other settings, as well as the history of the data collected for those variables.

To create a Thing, click on **CREATE THING** found within **Things** page accessed via the Shared Space sidebar.

![Create a new Thing](assets/create-thing.png "Create a new Thing")

***If you want to understand how to work with your Things, check the dedicated documentation available [here](https://docs.arduino.cc/arduino-cloud/guides/overview#3-creating-a-thing).***

***Do you want to learn more about the different types of Variables and their features? Have a look at [this tutorial](https://docs.arduino.cc/arduino-cloud/getting-started/cloud-variables).***

### Device Programming

It is now time to start uploading sketches on your devices.

The Arduino Cloud has a feature capable of creating some pre-built sections of the sketch related to a Thing, including some libraries necessary to interact with the cloud variables, as well as directly populating and updating the sketch once the new cloud variables are created and defined.

The sketch related to the thing is visible from the tab "Sketch" next to the "Setup" view, where the Thing's list of cloud variables is shown.

![Cloud Editor - Full Editor](assets/sketch-full-editor.png "Get started with the Cloud Editor")

From this sketch view, by clicking the **Open full editor**, it is fast and smooth to access the Arduino Cloud integrated [Cloud Editor](https://docs.arduino.cc/learn/starting-guide/the-arduino-web-editor), which allows you to program your boards from any browser and use the latest Arduino IDE features and libraries without having to install any software locally.

Otherwise, to open the Cloud Editor to retrieve your sketches directly, go to Arduino Cloud Home and click on the [New Sketch File](https://create.arduino.cc/editor) button.

![Get started with the Cloud Editor](assets/web-editor-button.png "Get started with the Cloud Editor")

It can also be accessed directly by navigating to **Sketches** within the Shared Space sidebar. It will list all the available developed sketches. Clicking on one of the sketches will directly take you to the [Cloud Editor](https://docs.arduino.cc/learn/starting-guide/the-arduino-web-editor).

***To get started with the Cloud Editor, check the dedicated tutorial at [this link](https://docs.arduino.cc/arduino-cloud/getting-started/getting-started-web-editor). However, if you have already developed your sketch and you would like to import it into the Cloud Editor, see the corresponding documentation [here](https://docs.arduino.cc/arduino-cloud/tutorials/import-your-sketchbook-and-libraries-to-the-web-editor)***

All the created sketches are individual and owned by the user that created them. Other members of the Shared Space can access your sketch in their Cloud Editor only if you share it with them. If you would like to do so, have a look at [this tutorial](https://docs.arduino.cc/arduino-cloud/tutorials/share-your-sketches) on how to do it.

Keep in mind that your sketch may contain some sensitive data that you do not want to share with other members, like Wi-Fi® credentials or API keys. If this is the case, check [this tutorial](https://docs.arduino.cc/arduino-cloud/tutorials/store-your-sensitive-data-safely-when-sharing) to learn how to share sketches without sharing sensitive data.

### OTA Updates

Arduino Cloud for Business integrates an amazing feature: Over-The-Air updates. This feature allows you to upload sketches wirelessly to your Arduino boards. This way, as soon as you have a compatible board connected to a Wi-Fi®/Ethernet network and configured to work with OTA, you will not need to physically connect the board to your computer to upload new sketches to it; instead, everything will work Over-The-Air, even from remote.

***Are you interested in learning how to perform an OTA update? Check [this tutorial](https://docs.arduino.cc/arduino-cloud/features/ota-getting-started#how-does-it-work). If you prefer to use the Arduino Cloud CLI instead, go to [this link](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#ota-over-the-air).***

## Collaborative Coding

**Collaborative Coding** is a powerful feature available with the plan that enables multiple users within the same shared space to work together on the same code. This feature allows team members to share and edit code seamlessly, providing better collaboration overall.

In a collaborative coding environment, everyone can create and modify code simultaneously. Changes are updated and visible to all participants after the last user has finished editing. The code editor highlights the area being edited by others with an orange frame, helping team members stay synchronized and aware of each other's contributions.

The following short clip shows an idea of how the collaborative coding works from two different user perspectives:

![Collaborative Coding](assets/collab-code-demo.gif)

While a user is working on the code, the area they are editing is highlighted with the orange frame, and a warning block appears. This indicates that the user should wait to avoid any loss of change. Please wait for them to finish before editing the code to prevent conflicts and ensure all changes are correctly synchronized.

![Collaborative Coding - Code editor orange frame highlight](assets/collab-code-orange-frame.png)

This functionality ensures that all users remain aligned and can contribute effectively. Collaborative coding improves the overall development experience by making projects more interactive and engaging.

## Fleet Management

Now it is time for you to start managing your fleet of devices/Things. The Arduino Cloud for Business fleet management features allow you to filter your devices/Things by status, add tags to more efficiently identify your projects, search between boards, and list and order them.

Get started with this awesome feature by going to **Things** or **Devices** tab in [Arduino Cloud](https://app.arduino.cc/devices) and start searching and filtering among your Things/devices.

![Search and filter among devices](assets/search-things.png "Search and filter among devices")

If you want to create your tag, which you can use as a filtering option, go to **Things** tab, click on the Thing you would like to tag and go to the Metadata tab as shown in the figure below.

![Thing metadata](assets/thing-metadata.png "Thing metadata")

Click on **ADD**. You will be asked to customize your tag through two fields:

* **Key**. The Key is the filter name which you will see among the list of available filtering options. E.g. Location.
* **Value**. The Value corresponds to the specific value your tag has for that specific Thing. E.g. Rome.

![Customize your tag](assets/add-tag.png "Customize your tag")

You can add an unlimited number of tags to each Thing.

At this point, you can go back to the Things tab and start filtering your Things according to the new tag you have just created.

![New tag filtering](assets/new-tag-filtering.png "New tag filtering")

## Dashboards

With Arduino Cloud for Business, you can create an unlimited number of dashboards. Push button, Switch, Scheduler, Map, Chart… These are just a few of the many widgets you can customize to visualize all your data or to remotely control your devices.

To start creating your dashboard, go to the **Dashboards** tab in [Arduino Cloud](https://app.arduino.cc/dashboards) and select the Thing you want to create a dashboard for.

![Dashboard example](assets/dashboard-example.png "Dashboard example")

***If you want to learn more on how to customize your dashboard and leverage the wide widget portfolio, check the dedicated documentation available at [this link](https://docs.arduino.cc/arduino-cloud/getting-started/dashboard-widgets).***

### Sharing Dashboards

Whether it is your teammate, your customer, or your system integrator; you can freely share your dashboards with all the people you like. Just keep in mind that the interested stakeholders need to have an Arduino Account to access the dashboards.

![Share your dashboard](assets/dashboard-sharing.png "Share your dashboard")

***Ready to share your dashboard? Have a look at [this tutorial](https://docs.arduino.cc/arduino-cloud/features/sharing-dashboards).***

### Data Export

Arduino Cloud for Business allows any user to download historical data from Arduino Cloud Things and Variables. The data are downloaded in **.csv** format to be ready for further evaluation or manipulation.

The Arduino Cloud for Business plan includes 1-year of data retention by default; this means that your data will be available and downloadable from your Arduino Cloud account for 1 year.

To start exporting your data locally, navigate into one of your dashboards on the [Arduino Cloud](https://app.arduino.cc/dashboards). While inside a dashboard, press the Download icon in the upper right corner. This will open a new window that will allow you to select which historical data you would like to download.

![Download icon](assets/download-button.png "Download icon")

From here you can select all the variables you want to download by checking the boxes as well as the time frame you are interested in.

When you have selected the data, click on the **SELECT DATA SOURCE** button.

![Export your data](assets/download-data.png "Exporte your data")

At this point, click on **GET DATA** to receive your data by email.

![Get your data](assets/get-data.png "Get your data")

You will get an email like the one below with a link allowing you to download all your data.

![Link to download your data](assets/email-data.png "Link to download your data")

You are now ready to monitor and manipulate all your Cloud data.

## Arduino Cloud API

Use Arduino Cloud back-end to control Things and devices via Arduino rest APIs in [Javascript](https://www.npmjs.com/package/@arduino/arduino-iot-client), [Python](https://pypi.org/project/arduino-iot-client/), or [Go](https://github.com/arduino/iot-client-go). With Arduino rest APIs, you will be able to manage up to 10 requests per second, guaranteeing stable data sharing.

Leveraging the APIs, you can interact with any element of the Cloud: data, devices, dashboards, and web properties. At the same time, APIs allow you to add power to the script, create complex scenarios or send and receive data from your custom service, 3rd party solution, or mobile application.

To use the APIs, you need to create an API Key Token in the API Keys section of your Space.

***We strongly recommend you add a Service Account role to your Shared Space to create/manage/maintain API Keys Tokens. The Service Account should not be linked to a personal email account so that the API Keys which will be created do not risk getting lost if that email account gets canceled.***

***If you want to start creating your own API Keys Token, take a look at [this tutorial](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-iot-api) and [this documentation](https://www.arduino.cc/reference/en/iot/api/).***

## IoT Remote App

Monitor your dashboards anywhere, anytime, and use your dashboards on the go with the free IoT Remote App.

To start exploring it, you will need to download it from either [Google Play Store](https://play.google.com/store/apps/details?id=cc.arduino.cloudiot&hl=en&gl=US) or the [Apple App Store](https://apps.apple.com/us/app/arduino-iot-cloud-remote/id1514358431) depending on your device.

***Do you want to get started with IoT Remote App? Read [this tutorial](https://docs.arduino.cc/arduino-cloud/tutorials/iot-remote-phone-sensors#phone-setup).***

## Arduino Cloud CLI

As mentioned, Arduino Cloud for Business fully supports the [Arduino Cloud CLI](https://github.com/arduino/arduino-cloud-cli). This tool allows you to access all Arduino Cloud features from your terminal.

The Arduino Cloud CLI is a great option if you are familiar with command-line interfaces and want to manage multiple devices and *Things* simultaneously with just a few lines of code.

Here are the main features of the Arduino Cloud CLI:

* [Mass provisioning](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#device), i.e., the ability to provision multiple devices simultaneously.
* [Mass OTA updates](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#ota-over-the-air), i.e., performing Over-The-Air updates for multiple devices at the same time.
* Advanced fleet management, including multiple devices [tagging](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#list-devices).
* Things monitoring and management, such as Things [tagging](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#tag-a-thing), [listing](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#list-things), [cloning](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#clone-things) and [template creation](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#extract-thing-template).
* Dashboard [creation](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#create-dashboard)/[cancellation](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#delete-dashboards), maintenance and dashboard [template extraction](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-cloud-cli#extract-dashboard-template).

***To learn more about the Arduino Cloud CLI and get started, you can check the official documentation [here](https://docs.arduino.cc/arduino-cloud/arduino-cloud-cli/getting-started/).***

## Optional Add-Ons

Arduino Cloud for Business can be customized with optional add-ons:

* **Portenta X8 Board Manager**
* **Machine Learning Tools Enterprise**

These add-ons are located under **Integrations** page, found within the Shared Space sidebar.

![Arduino Cloud Homepage with Add-ons](assets/cloud-add-on.png "Arduino Cloud Homepage with Add-ons")

To get started with them, it is sufficient to click on the corresponding tab.

### Portenta X8 Board Manager

Securely maintain Portenta X8 Linux distribution with this dedicated add-on, powered by [Foundries.io](https://foundries.io/). Deploy and update all your applications packaged into containers and perform secure Over-The-Air differential updates to target Portenta X8 devices/fleets.

***Check [Portenta X8 documentation](https://docs.arduino.cc/hardware/portenta-x8) to find out more and start working with Portenta X8 Manager.***

### Machine Learning Tools Enterprise

Build and train professional-grade predictive models with just a few lines of code through this dedicated add-on, powered by [Edge Impulse®](https://www.edgeimpulse.com/). Deploy premade models out of the box to quickly develop your machine learning projects, starting from object detection, and machine vision to audio segmentation.

***If you are interested in learning more about this add-on, have a look at [this documentation](https://cloud.arduino.cc/machine-learning-tools). Otherwise, we have plenty of tutorials already using Machine Learning Tools. Check if your device is compatible with it in the board documentation available [here](https://docs.arduino.cc/).***

## Additional Tutorials

You can find more tutorials on the [Arduino Cloud documentation page](https://docs.arduino.cc/arduino-cloud/).

## Congratulations

You are just a few easy steps from deploying your very own IoT project. Having a project connected to the Arduino Cloud for Business opens up many possibilities, such as tracking data in real-time, triggering remote devices and building wireless systems.

What will you create?

[Start your Cloud journey now](https://cloud.arduino.cc/plans#business).

## Trademark Acknowledgments

- **LoRa®** is a registered trademark of Semtech Corporation.