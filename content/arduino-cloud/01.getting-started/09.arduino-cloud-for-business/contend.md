---
beta: true
title: 'Getting started with Arduino Cloud for Business'
description: 'Get a general overview of Arduino Cloud for Business and its features'
difficulty: intermediate
tags:
  - IoT Cloud
  - Fleet Management
  - RBAC
author: 'Marta Barbero'
software:
  - iot-cloud
---


## Overview

The [Arduino Cloud for Business](https://www.arduino.cc/pro/software-arduino-iot-cloud/) is an Arduino IoT Cloud plan dedicated to companies and industrial clients wanting enhanced features in terms of device management, Role-Based-Access-Control, fleet management and safe remote access.

In this article, you will get a general overview of the major features of the Arduino Cloud for Business. However, if you are not familiar with Arduino IoT Cloud, we strongly recommend you to take a look at the following documentation: 
* To find all tutorials & articles, visit the [Arduino IoT Cloud Documentation page](https://docs.arduino.cc/cloud/iot-cloud).
* For a technical overview, list of features, and API guide, visit the [Arduino IoT Cloud Cheat Sheet](https://docs.arduino.cc/cloud/iot-cloud/tutorials/technical-reference).
* For API & SDK Documentation, visit the developer reference at[ Arduino IoT Cloud API](https://www.arduino.cc/reference/en/iot/api/).

## Goals
* Get in-depth information about how the Arduino Cloud for Business works
* Learn about the multiple dedicated features Arduino Cloud for Business provides
* Learn how to get started with Arduino Cloud for Business

## Required Software
* [Arduino Cloud for Business](https://cloud.arduino.cc/plans#business)


## Get Started With Arduino Cloud For Business

In order to get started with Arduino Cloud for Business, you need to [subscribe a plan](https://cloud.arduino.cc/plans#business). 

The Arduino Cloud for Business plan consists of two main subscriptions: 
* **Enterprise Base Plan.** It includes all the Arduino Cloud for Business features, like data plan, fleet management, Role-based-acess-control, Web Editor with Over-the-air updates, IoT Cloud with dashboards etc. Multiple of 50 devices can be connected under the Enterprise Base Plan – and you can always [contact our team](https://www.arduino.cc/pro/contact-us) for a tailored plan to accelerate your IoT solutions.
* **Optional Add-ons.** To address additional needs, Arduino Cloud for Business can be customized with optional add-ons. Check the [dedicated section](#Optional-Add-Ons) of this tutorial to learn more. 

If you do not need any tailored plan, go to [Arduino Cloud for Business page](https://cloud.arduino.cc/plans#business) and select **Purchase**. You will be then asked to login with your Arduino credentials. If you do not have an account yet, feel free to create a new one. 

![Arduino Cloud login](assets/arduino-account-login.png "Arduino Cloud login")

It is now time to customize your plan. Select the billing frequency you prefer and the number of Things (and so devices) that you would like to connect with your Arduino Cloud for Business workspace and click on **Continue**. 

![Customize your plan](assets/plan-customization.png "Customize your plan")

Go on by flagging the optional add-ons that you may need in your projects and click on **Add billing information**. Do you want to learn more on these add-ons? Check the [dedicated section](#optional-add-ons) of this getting started.

![Add-ons selection](assets/add-on-selection.png "Add-ons selection")

In the next steps, add all your billing and payment information and purchase your plan. 

Now you are ready to get started with your brand new Arduino Cloud for Business plan. Check the next sections to understand how to set-up your account and which features are included in your plan.  

### Join A Space

Once your plan has been successfully purchased, you will be asked to define the company / space name for your workspace. You are free to modify it in a second time by navigating to `Arduino Cloud > General Settings > Space information > Edit info > Name`. 

![Create new shared space](assets/create-new-space.png "Create new shared space")

Your Arduino Cloud for Business plan comes with two spaces by default: 
* **My Cloud**. My Cloud is a private space that is automatically created once a Arduino Cloud for Business plan is purchased. You can use this space for personal projects you do not want to share with all your team. This space is free and includes two Things, unlimited dashboards and 100MB of Sketch storage by default, but it can be further extended and customized by purchasing any [Individual plan on Arduino Cloud](https://cloud.arduino.cc/plans). Have a look at the [Arduino IT Cloud Getting Started](https://docs.arduino.cc/arduino-cloud/getting-started/iot-cloud-getting-started) if you want to start using your private space.
* **Shared space**. A shared space is the company space that you can use with all your team. As a matter of fact, a shared space can have any number of members, who can all access the resources inside of it. The level of access and specific permissions can be customized by the Space Admin (see [Invite members into your space section](#invite-members-into-your-space) to learn more). 

In the next sections, you will learn more on Shared Space features and functionalities. 

#### Change Shared Space Settings

To change the current settings of your Shared Space, navigate to **General Settings** tab using the sidebar. 

![Shared Space settings](assets/shared-space-settings.png "Shared space settings")

There you will find multiple options to customize your Shared Space, including: 
* Editing the Space name
* Assigning your own logo

#### Switch Between Spaces

If you are the owner of more than one Shared Space, or you have been invited into a Shared Space by another user, you can switch to other Shared Spaces at any time using the corresponding menu.

Move your mouse over the Space-Selector, which you can find at the top right hand corner and click on it. All the Spaces you hav access to will be listed there.

![Switch between Spaces](assets/switch-spaces.png "Switch between Spaces")

The Space-Selector shows you at any time which Space you are currently working on, in this case *Arduino PRO*. To switch to another Space, simply click with the mouse on the Space you would like to work on.

#### Create Additional Spaces

The Arduino Cloud for Business platform allows you to create and manage an unlimited number of Spaces. 

Take into consideration that, except for the automatically created Private Space, all the other Spaces need a dedicated subscription to Arduino Cloud. Check the available plans [here](https://cloud.arduino.cc/plans).

In order to create a new Shared Space, click on **New Shared Space** in the Space-Selector. 

![Switch between Spaces](assets/switch-spaces.png "Switch between Spaces")

Then you will be asked which type of Shared Space you want to create (i.e. For Business or For Education). Click on the type of your interest and proceed with purchasing a new plan as shown in [this section](#get-started-with-arduino-cloud-for-business). 

![Shared Space type selection](assets/shared-space-type-selection.png "Shared Space Type Selection")

#### Invite Members Into Your Space

To add additional users into your Shared Space, use the sidebar to navigate to the **Members** item under **Your space** group. 

![List of Shared Space Members](assets/members-home.png "List of Shared Space Members")

There you will find the complete list of all members who have access to your Shared Space, as well as the current role of each member. 

##### Members Types

There are multiple role types in Arduino Cloud for Business to allow the admin to have full control of the rights/permissions each user has in the Shared Space. In this way, the admin can set-up Role-Based Access Control (RBAC) by assigning profiles and sharing with any number of users.

The table below reports the list of supported roles and corresponding permissions. 

|                                           | Admin | Manager              | Editor | Viewer | Service Account |
|-------------------------------------------|-------|----------------------|--------|--------|-----------------|
| **Create/edit/delete Things**             | X     | X                    | X      |        |                 |
| **View Things**                           | X     | X                    | X      | X      |                 |
| **Add/edit/delete Devices**               | X     | X                    | X      |        |                 |
| **View Devices**                          | X     | X                    | X      | X      |                 |
| **Create/edit/delete Dashboards/Widgets** | X     | X                    | X      |        |                 |
| **View Dashboards**                       | X     | X                    | X      | X      |                 |
| **Widget Interaction**                    | X     | X                    | X      | X      |                 |
| **Download Historical Data**              | X     | X                    | X      | X      |                 |
| **Add/remove Members**                    | X     | X (only lower roles) |        |        |                 |
| **Manage billing**                        | X     |                      |        |        |                 |
| **Create/edit/delete API keys**           |       |                      |        |        | X               |

Thus, the only role with full permissions is the Admin, which basically corresponds to the owner of the Arduino Cloud for Business plan. 

In addition, we add a Service Account, which should be the one dedicated to the creation and maintenance of API Keys Tokens. We recommend to have at least one Service Account for each Shared Space and link it to a non-personal email account. In this way, API Keys do not risk to get lost by a specific user. 

##### Add A New Member

In order to add a new member, click on **ADD MEMBER** in the top right hand corner. 

![Add a new member](assets/members-home.png "Add a new member")

The following page will appear to allow you to send an email invitation to all the members you would like to join your Space. 

![New member invitation](assets/new-member-invitation.png "New member invitation")

Type the email addresses of all your team and define which role they will cover into your Space based on the available options. Click on **Invite**.  

The users you added will get the invitation by email with a link to join your Shared Space. You are now ready to start working all together into your Arduino Cloud projects.

### Device Managament

### Fleet Management

### Dashboards 

## Arduino Cloud API

## Arduino Cloud CLI 

## Optional Add-Ons

## Additional Tutorials

## Support
