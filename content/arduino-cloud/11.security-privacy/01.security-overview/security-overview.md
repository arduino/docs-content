---
title: Security Overview
description: How Arduino secures Arduino Cloud — the shared responsibility model, data protection at rest and in transit, and secure development practices.
tags: [Arduino Cloud, Security]
author: Arduino Security Team
---

Arduino Cloud operates under a **shared security responsibility model**:
Arduino secures the cloud infrastructure, services, and the confidentiality of
sensitive data, while customers secure their account, credentials, and the
information they choose to store. Arduino's overall approach aligns with
cybersecurity standards such as ISO 27001.

<Alert type="info">

For any questions regarding security, contact the
[Arduino Security Team](mailto:security@arduino.cc).

</Alert>

## Shared Responsibility

| Arduino is responsible for | Customers are responsible for |
|---|---|
| Security of the cloud infrastructure and services | Their account and personal access credentials |
| Confidentiality of sensitive data | Information they choose to store in the Cloud |
| Regular security training, penetration tests, and least-privilege access | Enabling strong authentication and avoiding accidental disclosure |

On the customer side, Arduino recommends **two-step verification** for an extra
login factor, **social login** to avoid managing extra passwords, and care not
to disclose personal information inside shared projects or sketches.

## Data Protection

Arduino identifies sensitive data — personally identifiable information (PII)
and data sent from boards — and protects it at every stage:

- **At rest** — PII databases are encrypted with AES-256; user credentials are
  hashed with modern hashing algorithms.
- **In transit** — browser and API communication uses HTTPS secured with TLS;
  IoT devices send data over MQTT secured with TLS.

On boards with a secure element, device onboarding and operation use a
mutual-TLS authenticated connection, so both the device and the Cloud verify
each other's identity:

![Device setup and operation phases.](assets/device-phases.png)

The authentication layer adds protection against common web threats (XSS,
clickjacking, CSRF) and brute-force attempts, and a Content Delivery Network
provides DDoS protection and web-application firewalling.

## Secure Development Practices

Arduino follows a **Secure by Design** principle throughout the software
development lifecycle, applying defense in depth, least privilege, failing
securely, and assuming compromise. Dedicated pillars cover secure data
management, secure repositories, environment segregation, and continuous
security testing — design reviews, code reviews, penetration tests, and
vulnerability assessments — with findings remediated through an internal
vulnerability management program.

## Access Control and Monitoring

Internal access is governed by **least privilege**: staff generally have no
direct access to user PII, with limited, logged, multi-factor-protected
exceptions for support and specific technical roles. Systems are continuously
monitored for unauthorized activity, with automated anomaly detection for
threats like brute-force attacks. Suspected vulnerabilities can be reported via
Arduino's [Coordinated Vulnerability Disclosure policy](https://www.arduino.cc/en/security_cvd).

## Next Steps

- [ISO 27001](/arduino-cloud/security-privacy/iso-27001)
- [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets)
