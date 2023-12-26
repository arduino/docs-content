---
title: 'Security of Arduino IDE'
description: 'Learn about the secure development process behind the Arduino IDE.'

tags:
 - Security
author: 'Arduino Security Team'
---

Arduino IDE 2.x is the latest version of the Arduino Programming tool and it is built on Eclipse Theia, an open-source framework for building IDEs.

Arduino is committed to regularly monitor and update security measures applied to the Arduino IDE to ensure proper protection from any threats or vulnerabilities detected.

Arduino's defined principles and requirements to be followed within the secure development lifecycle of Hardware, System and Software and the development of the open-source Arduino software makes no exception. In particular, Arduino follows the **Secure by Design** principle in every stage of the software development and the **Security Principles** listed below are followed during the secure development lifecycle:


- **Apply Defense in Depth**: Layered security mechanisms are in place to increase security as a whole.
- **Use a Positive Security Model**: A ‘positive’ security model defines what is allowed and rejects everything else.
- **Fail Securely**: It is important that failures are handled so that exceptions do not enable unwanted behavior.
- **Run with Least Privileges**: The principle of least privilege is required to perform every business process.
- **Avoid Security through Obscurity**: Security through obscurity alone is a weak security mechanism, however when combined with all principles it can be used as an additional layer of security.
- **Keep Security Simple**: Keeping the application’s security simple is a better option than having complex designs.
- **Assuming compromise**: The assuming compromise principle is useful to improve the detection and response capabilities in order to predict and remediate the security events before they evolve into security incidents.
- **Keep people away from data**: Usage of mechanisms, patterns and tools to reduce or eliminate the need for direct data access or manual processing data with the aim of reducing the risk of mishandling or modification and human error when handling sensitive data.

Moreover, the members of Arduino take in considerations the following pillars as part of the Arduino Secure Software Development Lifecycle:

- **Education and Guidance**: developers have specific know-how and receive training on secure architectural and coding standards.
- **Secure Data Management**: sensitive data (such as PII) are properly managed in accordance with legislation and recommended security standards are properly implemented.
- **Secure Repository Management**: software repositories are protected with the Least of privilege and Separation of duties principles.
- **Secure Environment**: services and data are segregated between different environments: Development, Staging and Production.
- **Secure Development**: security requirements and best practices are taken into consideration in all the steps of the development lifecycle.
- **Security Testing**: activities performed by the security team to identify residual vulnerabilities as a result of the artifacts being developed.

As part of the security testing activities, Arduino periodically performs the following tasks on the Arduino IDE:

- **Secure Code Review (SCR)**: the code is reviewed in order to ensure the safety against main security vulnerabilities and threats.
- **Secure Component Analysis (SCA)**: security engineers evaluate components related to Theia npm packages and Electron.
- **Secrets scanning analysis**: activities performed to ensure that secrets are not inadvertently leaked within the repository.

Finally, should an Arduino user or customer suspect a vulnerability or security issue, they are invited to report it as described in our Coordinated Vulnerability Disclosure policy available at: [https://www.arduino.cc/en/security_cvd](https://www.arduino.cc/en/security_cvd).

## Third Party Components

In the process of conducting Secure Component Analysis, Arduino puts particular attention on the aforementioned  external dependencies (Eclipse Theia and OpenJS Electron) and reports any found vulnerability to the respective project maintainer:

- Eclipse Theia manages vulnerabilities using the process described in [https://www.eclipse.org/security](https://www.eclipse.org/security).
- OpenJS Electron vulnerabilities are managed using the process described in [https://www.electronjs.org/docs/latest/tutorial/security](https://www.electronjs.org/docs/latest/tutorial/security).

When vulnerabilities in third party components are fixed by the respective maintainer, Arduino will update the component involved as required, in a commercially reasonable time, based on the severity of the identified vulnerability.

## Version Management

When it comes to managing multiple versions of the Arduino IDE, the following policy will be applied:

- all security principles that are applicable to the process (design, development, testing, release) will apply to any version currently in development
- considerations related  to finding and fixing vulnerability, and providing security fixes for the same, are applicable to the latest stable release of Arduino IDE; in addition:
    - no security fixes are provided on nightly builds;
    - no security fixes  are provided on versions marked as “Legacy versions” of Arduino IDE as identified on arduino.cc/en/software 

In general, Arduino will prefer releasing a new version of Arduino IDE containing required security fixes rather than applying a security fix on an existing version. Users are recommended to stay current with the latest stable release of Arduino IDE, also leveraging the auto-update feature provided by the software itself, to ensure the latest and greatest features and security updates.

