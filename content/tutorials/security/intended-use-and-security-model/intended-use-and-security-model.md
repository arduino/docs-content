---
title: 'Arduino Hardware Products: Intended Use and Security Model'
description: 'This document describes the intended use and security model for Arduino Hardware Products.'
tags: 
  - security
  - hardware
author: 'Arduino Security Team'
---

Version 1.2 — 03/07/2026

## Intended Use

Arduino Hardware Products (in the following also referred to as “boards”) might contain physical hardware boards, kits based on boards, and installation-ready programmable appliances.

Arduino boards are designed primarily as development and prototyping environments and can also serve as a basis for production solutions.

A “solution” designed by a customer might consist of one or more Arduino Boards, customized with additional external hardware (such as sensors, peripherals, actuators, motors, etc.) and additional software. 
When building a solution, and when moving it to production, security measures must be designed and implemented to match the intended deployment environment, and security controls should be verified early in the development lifecycle.

Security is a shared responsibility between Arduino and the builder of a solution for end users. The final security posture of a solution should be planned alongside functional requirements so that the implementation is appropriate to the intended deployment.

Depending on the solution and the required security level, the developer must verify which security features are provided by the specific hardware products adopted (both Arduino products and other products), and complement them with controls appropriate to the deployment.

The following sections highlight some of the considerations that a solution should consider depending on the final target deployment scenario.

## Physical Access and Hardware Integrity

Arduino Boards are designed to provide direct access to hardware features to support prototyping. By default, the Boards do not impose hardware limitations or physical access restrictions.

By default, interfaces, expansion ports, and programming mechanisms remain accessible, and hardening measures such as locked boot or restricted debug interfaces are not applied. Where a Board provides optional protections such as a Secure Element<sup>1</sup> or secure boot, enabling them is the developer’s responsibility.

<Alert type="note">

<sup>1</sup>A Secure Element (SE) is a dedicated, tamper-resistant microchip isolated from a device's main processor. It acts as a digital vault, designed exclusively to securely store sensitive data (like cryptographic keys) and safely perform critical operations without ever exposing your secrets to the outside system

</Alert>

When the Board is providing Bluetooth or Bluetooth Low Energy (BLE) capabilities, these can be operated in a development/prototyping environment, or in a production environment wherein physical proximity with the Board is controlled with external measures. Physical proximity with the Bluetooth Board is considered a safe connection method. The user might decide to add additional protection to the Bluetooth connection by implementing authentication methods.

Within this model, the following applies:

- **Default openness:** because the platform is open by default, the integrity of the system in uncontrolled deployment environments depends largely on the configuration implemented by the developer.
- **Physical access:** by default, a device in the hands of third parties should be considered fully accessible. The Boards do not feature physical or software locks that prevent data access or reprogramming, unless optional protections are enabled by the developer.
- **Developer responsibility:** for devices installed in public or unsupervised environments, the developer is responsible for implementing the physical or procedural protection measures required to prevent unauthorized access.

The default configuration of Arduino Boards prioritizes an unrestricted development workflow. Evaluating the installation context and adding appropriate protections is the developer’s responsibility.

### Optional Hardware-Backed Security

Some Arduino Boards provide optional hardware-backed protections that can strengthen integrity beyond the default open configuration. These are not present on every Arduino Board and are not enabled by default; their availability must be checked against the specific Board's technical specifications:

- **Secure Element:** A dedicated Secure Element for storage of security keys and credentials is available on a subset of Boards. Where present, it is abstracted by the libraries and can be used for trusted boot, mutual authentication, or secure storage.
- **Secure boot and signed updates:** on selected platforms, a secure boot capability and signed/encrypted update packages (for example via MCUboot) can be enabled so that only authenticated firmware is executed. This is an opt-in feature, not active unless explicitly configured, and is not available on all Boards.

Because these protections are optional and not present on every Board, the integrity of a solution deployed in an uncontrolled environment depends largely on the configuration implemented by the developer.

# Software Supply Chain

Arduino Boards support a broad ecosystem of software components, libraries, and AI models. The developer is responsible for the integrity and trustworthiness of every component used, and third-party libraries and models should be vetted as part of the development workflow.

- **User code and containers:** applications and container images run with the privileges granted by the developer. The principle of least privilege should be applied and software dependencies kept up to date.
- **Third-party components:** libraries and modules obtained from external repositories should be vetted for source and integrity before deployment, preferring official and maintained versions. A Secure Component Analysis<sup>2</sup> on external dependencies is recommended.
- **Machine learning models:** third-party AI models may exhibit unexpected behavior. Model provenance should be validated and safety boundaries tested, particularly where models influence physical actuation or critical decision-making.
- **Inter-processor communication:** in multi-processor designs, communication channels should be secured and all incoming commands validated.
- **Secure code review:** custom firmware should be reviewed from a security standpoint before running, to limit the introduction of security risks.


<Alert type="note">

<sup>2</sup>Secure Component Analysis, also referred to as Software Composition Analysis (SCA), is a cybersecurity process that identifies and manages third-party and open-source components within an application. It aims to detect vulnerabilities in software components and libraries used by an application

</Alert>

## Network and Connectivity

The network environment should be designed with a security-by-design approach, with isolation and encryption treated as native components of the deployment. Key requirements include:

- **TLS encryption:** where connectivity is available, TLS should be used to provide confidentiality of information transmitted over the network.
- **Credential management:** on Boards without a Secure Element, authentication with user/secret credentials provided in the application firmware or stored on local storage such as flash memory. Hardcoding credentials should be avoided wherever possible.
- **Network segregation and Wi-Fi security:** proper network segmentation, robust encryption protocols, and traffic monitoring to reduce the attack surface and prevent unauthorized access from remote attackers. Moreover, the developer is responsible for mechanisms to prevent and detect Man-in-the-Middle (MitM) attacks, particularly on public or untrusted networks.
- **Bluetooth Low Energy (BLE) security:** BLE connectivity falls within both the physical and network security perimeter. Appropriate pairing, bonding, and encryption controls must be implemented to protect the device from unauthorized proximity-based or remote access.

## Shared Responsibility

Arduino operates under a shared security responsibility model that distinguishes the responsibilities of Arduino from those of the customer.

### Arduino is responsible for

- The security of the Arduino Core RTOS firmware for Microcontroller Boards, and the security of the base Linux OS build provided for Microprocessor Boards
- The security of the libraries and components officially distributed with the Boards, including periodic Secure Code Review<sup>3</sup> and Secure Component Analysis on cores and libraries explicitly marked as maintained by Arduino
- Selecting state-of-the-art hardware to protect against tampering of security-related components, where such components are present on the Board
- Managing the security protocols for connecting devices to the Arduino Cloud, designed to help ensure safe data transmission, authentication, device provisioning and claiming, and Over-The-Air firmware updates

<Alert type="note">

<sup>3</sup>A secure code review is the systematic examination of software source code to identify security vulnerabilities, logical flaws, and insecure design patterns before the application is deployed.

</Alert>

### The customer is responsible for

- The security of the final solution built with Arduino Boards
- The security of any third-party component included in the solution, such as hardware, software components, or libraries. In particular, even if libraries or other third-party components are installed using the Arduino IDE or with Arduino tools, but the library is not maintained by Arduino, its security remains responsibility of the maintainer, to be evaluated by the customer
- Network security and adequate segregation of Boards to reduce the remote attack surface
- Physical protection: placing Boards where unauthorized parties cannot tamper with the hardware, and enabling any optional hardware protections appropriate to the deployment

## Arduino Security Resources

Further information on the security of the Arduino ecosystem is available at the following official resources:

- **Official Security Page:** [https://www.arduino.cc/en/security/](https://www.arduino.cc/en/security/)
- **Hardware Security Considerations:** [https://docs.arduino.cc/tutorials/security/security-consideration-hardware](https://docs.arduino.cc/tutorials/security/security-consideration-hardware)
- **Coordinated Vulnerability Disclosure (CVD):** [https://www.arduino.cc/en/security_cvd/](https://www.arduino.cc/en/security_cvd/)
- **Security Bulletins:** [https://support.arduino.cc/hc/en-us/sections/10926243830172-Arduino-Security-Bulletins](https://support.arduino.cc/hc/en-us/sections/10926243830172-Arduino-Security-Bulletins)
