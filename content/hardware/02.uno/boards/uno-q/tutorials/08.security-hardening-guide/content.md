---
title: 'UNO Q Security Hardening Guide'
difficulty: advanced
compatible-products: [uno-q]
description: 'Security best practices and hardening procedures for the UNO Q.'
author: 'Alessandro Braccio'
tags:
  - Security
  - Cybersecurity
  - Linux
  - Debian
hardware:
  - hardware/02.hero/boards/uno-q
software:
  - app-lab
  - app-cli
---

### Overview 

Arduino UNO Q is a hardware development board that comes with a pre-installed distribution of Arduino Debian for UNO Q. This operating system is based on the open-source Debian project ([https://www.debian.org/](https://www.debian.org/)). 

In addition, the board has a set of software packages developed by Arduino, as follows:

On Linux:
* [Arduino App Lab](https://docs.arduino.cc/software/app-lab/)  
* [Arduino App CLI](https://docs.arduino.cc/software/app-lab/tutorials/cli/)  

On the Microcontroller:
* [Arduino core for UNO Q based on Zephyr RTOS](https://github.com/arduino/ArduinoCore-zephyr)

Using these software tools, users can create their own Applications running on Linux and MicroController. Depending on the user application, a different set of security measures may be required to harden the solution properly. UNO Q provides all the necessary tools to implement a strong security posture.

***Before continuing, if you're not familiar with the UNO Q or want to get more familiar before proceeding with this security guide, please refer to the following tutorials: [__ADB Access__](https://docs.arduino.cc/tutorials/uno-q/adb/), [__SSH Connectivity__](https://docs.arduino.cc/tutorials/uno-q/ssh/), [__Single-Board Computer Mode__](https://docs.arduino.cc/tutorials/uno-q/single-board-computer/), and [__Debian System Guide__](https://docs.arduino.cc/tutorials/uno-q/debian-guide/).***

The following guide provides information on how to adapt the security posture of UNO Q to the specific type of user application developed.

Some of the limitations to take into consideration are as follows: 

* Arduino does not recommend the usage of UNO Q as part of systems involving credit card payments or other forms of payment or transactions; this is not an intended usage and hence not part of the cybersecurity recommendations.   
* If the product is used to build toys or solutions for kids, it's the user's responsibility to provide proper parental control features

### Authentication / Access Control / Password Protection

The UNO Q system comes with a pre-configured OS user named `arduino`. This user is essential for a proper experience, as it has all the necessary tools for the Arduino App Labs pre-installed and set up.

Furthermore, the `arduino` user is the main user for the system's file segregation. Its user data is stored on a separate partition from the system data. This is crucial because it protects your personal files from being deleted if you ever need to reformat the system. Therefore, it is highly recommended to use the `arduino` user when using the UNO Q system.

The first time UNO Q is accessed (either in Single-Board Computer mode or via USB connected to a PC through App Lab), the user must set a mandatory password for the OS user `arduino`. The user does not have a password, and it is mandatory to set one on first access (the system prompts the user to do so and can't continue logging in until it's set).

It is recommended to set a strong password that consists of at least 12 characters, including one or more characters from each of the following sets:

- Lower and Upper case alphabetics  
- Digits 0 through 9  
- Punctuation marks

Some details of interest are as follows: 

- Don't use easily guessed words for your password. It includes usernames, machine names, account names, family member or pet names, dictionary words, or simple character sequences like `12345` or `qwerty`.   
- Avoid reusing passwords. Please don't use the same one for different accounts or systems.

### Auditing login operations 

The **last** command in Linux provides a **history of user logins and logouts** by reading from a binary log file located at `/var/log/wtmp`. This file isn't plain text; instead, system processes write a record to it every time a user **successfully logs in**, **logs out**, or the **system is rebooted**. 

When you run the last command, it reads this `wtmp` file from the end to the beginning, translating the binary records into a human-readable list. Each line of output typically shows:

* the username,   
* the terminal they used (e.g., `pts/0` for a remote SSH session),   
* the source IP address or hostname they connected from,   
* the login and logout times,  
* the total duration of the session.

Because it also records system reboots, it serves as a quick and effective tool for auditing who has accessed the system and tracking its uptime.

### Operating System Update

Regularly updating your UNO Q operating system is an important security practice. Here's why it's so important for your hardware board:

* *Vulnerability Fixes:* Software, including the Linux kernel and various third-party and Arduino applications, can have security vulnerabilities discovered after their release. These vulnerabilities could allow an attacker to gain unauthorised access, execute malicious code, or disrupt your system's operation.

* *Access to the Latest Security Advisories:* The Debian project has a dedicated security team that monitors for vulnerabilities in all packages. When a vulnerability is found, they quickly release an updated package with a fix and issue a security advisory.

* *Stability and Reliability:* The Debian package management system is designed to provide stable and reliable updates. The updates are tested to ensure they don't break existing functionality. This helps your hardware board remain operational and secure.

OS updates are distributed via Debian Packages and installed with the `apt-get` command; in particular, packages come from official Debian repositories and from a dedicated Arduino repository containing Debian packages for Arduino software. This mechanism leverages the strong security features provided by the Debian registry (PGP signatures, TLS transport, etc). 

To ensure your system is as secure as possible, run the command `arduino-app-cli system update` to update the list of Debian packages and apply any available updates (download new packages for both the OS and the Arduino software components). 

### Physical access

By default, UNO Q comes preconfigured with the ADB (Android Debug Bridge) daemon listening on the USB port. Hence, when connected to a PC or laptop via USB, it's possible to issue adb commands (e.g., `adb shell`) and access the Linux Operating System as the `arduino` user. The `arduino` user can also become an admin via the “sudo” command.   
App Lab uses this feature to allow programming UNO Q via USB in `PC connected` mode.

If the ability to program the board via USB cable is not desirable (for example, when the development process is complete and the board is ready for its final application), ADB can be stopped as described below. 
 
Note that this implies that the only way to access the board to program it will be to connect a monitor, keyboard, and mouse directly in **Single-Board Computer** mode.

To stop the `adbd` daemon, you can run the following command:

```bash
sudo systemctl stop adbd
```

To restart the `adbd` service, use the following command:

```bash
sudo systemctl start adbd
```

It is possible to disable the auto-execution feature of the service `adbd` using the following command:

```bash
sudo systemctl disable adbd
```

The service can be restarted in auto-start mode by using the following command:

```bash
sudo systemctl enable adbd
```

### Network access

The pre-installed Debian distribution on UNO Q does not expose any open TCP port on the network by default.   

The user might want to enable network services such as SSH, depending on the intended use (for example, during development). In general, it is recommended to switch off SSH or other network access protocols when the device is used in production. 

The recommended method for securely exposing a service is **SSH tunnelling**. An example of its implementation is provided below.

#### How to protect a local service through SSH Tunnelling (Local Port Forwarding) 

SSH tunnelling is useful because it creates a secure, encrypted channel between your local machine and a remote server. Instead of exposing a service's native port, for example, a service listening on port `8900` to the internet, you can keep it firewalled and inaccessible.

You then use your SSH connection to `tunnel` traffic from a local port on your computer to that secure, internal port on the remote server. The traffic flowing through this tunnel is encrypted, protecting sensitive data from interception or unauthorized access, and is accessible only through the authentication mechanisms provided by SSH itself.

The following example shows commands to protect a service listening on TCP port `8900` on the UNO Q system. The firewall rules allow only SSH tunnelling to this service.

##### Prerequisites

- The SSH service must be configured and running in the UNO Q system and must be accessible to proceed further and configure the SSH tunnelling

##### Step 1: Allow all incoming connections from localhost to the service 

The first step is to apply an incoming firewall rule that allows all connections from the UNO Q's localhost interface to itself. This rule is necessary because all incoming requests to the exposed service will be denied unless they originate from localhost (or from the SSH tunnel).

```bash
sudo iptables -A INPUT -i lo -j ACCEPT
```

##### Step 2: Protect the running service from external access 

The second step is to implement firewall deny rules to block all incoming traffic to the exposed service listening on port `8900`.

By applying this rule, no one will be able to connect to the service, except for connections coming from localhost or through the SSH tunnel described in the previous step.

```bash
sudo iptables -A INPUT -p tcp --dport 8900 -j DROP
```

##### Step 3: Establish the SSH Tunnel

Any external user can connect to the protected service running on port `8900` via an SSH tunnel, as shown below.

```bash
ssh -L 9999:<UNOQ_Ip_Address>:8900 arduino@UNOQ_Ip_Address
```

The user is using an SSH tunnel that connects their local port `9999` to port `8900`, which is listening on the UNO Q service. Since the redirection happens within the UNO Q system through the SSH service, the connection is permitted because it originates from the local interface of UNO Q rather than an external one.

### Communicating with web services

When implementing applications on your UNO Q, it's important to make sure that secure communication protocols are used, for example:

* SSL/TLS  
* HTTPS    
* MQTT-S

If the user application is using the Arduino App Lab environment, it can instantiate the WebUI Brick to host a network-reachable web server. The user can configure this component to require HTTPS communication.

For this reason, certificates can be provided by the user in a known directory so that the web server will use them for HTTPS connections.

If no certificates are provided but HTTPS is required by user configuration, self-signed certificates will be automatically generated and placed in the same known directory.

#### Configuring WebUI brick with HTTPS and Custom Certification Authority

To provide a secure connection between the WebUI brick and the browser, you can use the **mkcert** tool. 

The scope is:

* **Create a Certification Authority** to provide secure keys and certificates  
* **Create a private key and a signed certificate** to use with the WebUI brick and expose an HTTPS service  
* **Export the root CA** provided by mkcert  
* **Trust the root CA** in the client host to verify the connection

##### Install mkcert 

Install the latest version of mkcert, which at the time of writing is `v1.4.4`, from the following link: [https://github.com/FiloSottile/mkcert/](https://github.com/FiloSottile/mkcert/), using the commands shown below:

```bash
# Download the mkcert binary for Linux ARM64
cd /tmp
wget https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-linux-arm64
```

```bash
# Make it executable
chmod +x mkcert-v1.4.4-linux-arm64
```

```bash
# Move it to a location in PATH
sudo mv mkcert-v1.4.4-linux-arm64 /usr/local/bin/mkcert
```

```bash
# Verify installation
mkcert -version
```

##### Configure certificates

Log in to the Arduino UNO Q device and:

1. Enter the WebUI Application directory;  
2. Create a **certs** directory inside the Application where you have to add the private key and certificate;  
3. Enter the **certs** directory.

```bash
cd ~/ArduinoApps/APPLICATION_NAME
```
```bash
mkdir certs
```
```bash
cd certs
```

Then you have to:

1. Install the root CA provided by mkcert in the system trust store (optional);  
2. Create a certificate and a private key for your application;  
3. Rename the file with the path expected by WebUI brick:   
   - `cert.pem` for certificate  
   - `key.pem` for private key  
4. Upload the files to the application path

**Step 1: Install mkcert CA (optional)**

```bash
mkcert -install
```

Expected output:

```
Created a new local CA 💥
The local CA is now installed in the system trust store! ⚡️
```

**Step 2: Create certificate and private key**

```bash
mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1
```

Expected output:

```
Created a new certificate valid for the following names 📜
 - "example.com"
 - "*.example.com"
 - "example.test"
 - "localhost"
 - "127.0.0.1"
 - "::1"

Reminder: X.509 wildcards only go one level deep, so this won't match a.b.example.com ℹ️

The certificate is at "./example.com+5.pem" and the key at "./example.com+5-key.pem" ✅
It will expire on 30 April 2028 🗓
```

**Step 3: Rename files to WebUI expected names**

```bash
mv ./example.com+5.pem cert.pem
```

```bash
mv ./example.com+5-key.pem key.pem
```

Now, to use HTTPS, you have to pass the following parameters to the WebUI constructor:

```python
ui = WebUI(use_ssl=True)
```

The next step is to trust the root CA to the client host. The root CA certificate is located in the path:

```bash
/home/arduino/.local/share/mkcert/rootCA.pem
```

Where **`arduino`** is the username. You can extract the root CA certificate to your host with the command:

```bash
adb pull /home/arduino/.local/share/mkcert/rootCA.pem
```

In the final configuration step, you need to add the `rootCA.pem` file as a trusted certificate in your browser.

#### Configuring WebUI brick with HTTPS and Public Certification Authority 

To provide a secure connection between the WebUI brick and the browser with a certificate provided by a public Certification Authority.

The scope is:

* **Create a private key and a signed certificate** to use with the WebUI brick and expose an HTTPS service  
* **Install the private key and the signed certificate** in the WebUI brick application

Log in to the Arduino UNO Q device and:

1. Enter the WebUI Application directory.  
2. Create a **certs** directory inside the Application where you have to add the private key and certificate.
3. Enter the **certs** directory.

```bash
cd ~/ArduinoApps/APPLICATION_NAME
```

```bash
mkdir certs
```

```bash
cd certs
```

Then you have to:

1. Create the CSR and private key for your application.
2. Sign the CSR with the Public Certification Authority  
3. Rename the files with the name expected by WebUI brick:   
- `cert.pem` for certificate  
- `key.pem` for private key  
4. Upload the files to the application path

```bash
adb push cert.pem /home/arduino/ArduinoApps/APPLICATION_NAME/certs
```

```bash
adb push key.pem /home/arduino/ArduinoApps/APPLICATION_NAME/certs
```

Now, to use HTTPS, you have to pass the following parameters to the WebUI constructor:

```python
ui = WebUI(use_ssl=True)
```

### Data Protection 

If you are using UNO Q to store private information, it is recommended that you implement encryption at rest to protect it. Various approaches are available; some of them are proposed below:

#### Add an encrypted private directory to the user's home directory 

The following procedure outlines how to create a subdirectory within the user's home directory that is managed by the operating system, allowing data to be stored and guaranteeing protection at rest.

The protected data will be stored in the `\~/.Private\` directory, which will be automatically mounted to the `\~/Private\` directory after each successful login.

Once mounted, all interactions with files in the `\~/Private\` directory will be encrypted at rest.

It is important to note that all files outside the `\~/Private\` directory, even if they are in the user's home directory, will not be protected by encryption at rest.

To configure a specific system user to use an encrypted home directory, please follow these steps.

##### Step 1: Install the encryptfs-utils components

The following command must be performed as root:

```bash
sudo apt update
```

```bash
sudo apt install ecryptfs-utils
```

##### Step 2: Create the Private encrypted directory in the user's home

The following command must be run by the user who wants to create a private directory within their home directory.

The user's password is required, and there is an option to provide a custom mount passphrase that serves as the encryption key for all files in the private directory.

```bash
ecryptfs-setup-private
```

##### Step 3: Save the encryption passphrase in a safe location 

To make sure the safe recovery of your data in the future, it is important to store the chosen encryption passphrase in a secure online/offline location, such as a Password Manager. 

The following command retrieves the unwrapped passphrase set during setup.

```bash
ecryptfs-unwrap-passphrase ~/.ecryptfs/wrapped-passphrase
```

##### Step 4: Mount the encrypted Private directory 

The private directory located at `~/Private` is automatically mounted using the passphrase provided during setup after a successful login.

Therefore, any successful SSH access will automatically and transparently mount the private directory without requiring any additional information from the user.

However, there is an exception for ADB access, such as when using the `adb shell` command. Since `adb shell\` does not perform a login, the operating system cannot complete the internal steps required to mount the private directory automatically.

For this reason, the user must perform the following command immediately after being prompted by the `adb shell\`.

```bash
sudo su -l arduino
```

Once the command above is performed successfully, the private directory will be mounted at `~/Private` as expected.

### Monitoring device

If your UNO Q is part of a critical application, it's a best practice to set up monitoring for failures and resource usage.

#### Configure the log service and sending messages to remote server 

**rsyslog** is the standard system logger on modern Debian systems and is usually installed by default. This guide will cover verifying the installation, configuring it to send specific logs to a new file, and setting up log rotation.

##### Check Installation & Status

First, let's make sure `rsyslog` is installed and running.

1. **Check if the package is installed:** Open your terminal and run:

```bash
dpkg -l | grep rsyslog
```

2. If it's installed, you'll see it listed. If not, you can install it with:

```bash
sudo apt update && sudo apt install rsyslog
```

3. **Check if the service is running:** Use `systemctl` to check the status of the `rsyslog` daemon.

```bash
sudo systemctl status rsyslog
```

You should see an output indicating it's **active (running)**. If not, enable and start it:

```bash
sudo systemctl enable rsyslog
```

```bash
sudo systemctl start rsyslog
```

##### Understand the Configuration Structure 

Before making changes, it's good to know where `rsyslog` stores its files.

* **/etc/rsyslog.conf**: This is the main configuration file. It includes a line to load all files from the directory below.  
* **/etc/rsyslog.d/**: This is the **recommended directory** for your custom configuration files. By creating your own file here (e.g., `50-custom.conf`), you avoid conflicts when the main `rsyslog` package is updated.

The basic syntax for a logging rule is: `facility.priority action`.

* **Facility**: The type of program generating the log (e.g., `auth`, `cron`, `kern`, `mail`, `syslog`).  
* **Priority**: The severity of the message (e.g., `info`, `notice`, `warning`, `err`, `crit`).  
* **Action**: What to do with the message (e.g., write it to a file like `/var/log/auth.log`).

##### Sending logs to a Centralized Logs Server

1. Create a Forwarding Rule

Create a new configuration file to define the forwarding rule. It allows your custom settings to be protected from package updates.

```bash
sudo nano /etc/rsyslog.d/90-forward.conf
```

2. Add the Forwarding Configuration  

Paste the following configuration into the file. This rule forwards **all** logs (`*.*`) to your remote server using TCP.

```
# Configuration to forward all logs to a remote server
# Replace <REMOTE_SERVER_IP> with your log server's actual IP address

action(
    type="omfwd"
    target="<REMOTE_SERVER_IP>"
    port="514"
    protocol="tcp"

    # Use a disk queue for reliability. If the remote server is down,
    # logs will be buffered to disk and sent when it's back online.
    queue.type="linkedList"
    queue.filename="fwd_queue" # A unique name for the queue file
    queue.saveOnShutdown="on" # Save in-mem data if rsyslog shuts down
    action.resumeRetryCount="-1" # Retry indefinitely if the server is down
)
```

**Important:** Replace `<REMOTE_SERVER_IP>` with the actual IP address of your log server. The `queue` parameters are highly recommended as they prevent log loss if the remote server is temporarily unreachable.

3. Restart rsyslog  

Apply the new configuration to the client.

```bash
sudo systemctl restart rsyslog
```

#### Send notification from the board

**Monit** is a lightweight, open-source utility that automatically monitors and manages server processes, files, directories, and devices. If a service fails, *Monit* can automatically restart it and send you an alert.

##### Installation

1. First, update your package list and install the *Monit* package.

```bash
sudo apt update && sudo apt install monit
```

2. Once installed, the *Monit* service will start automatically. You can verify its status with:

```bash
sudo systemctl status monit
```

##### Core Configuration

The main configuration file is located at **`/etc/monit/monitrc`**. Let's edit this file to set up email alerts and enable the web interface.

```bash
sudo nano /etc/monit/monitrc
```

Scroll through the file and make the following changes:

###### Set Up Mail Server

Find the mail server section. Uncomment the lines and fill in the details for your SMTP server. This example uses *Gmail*, which requires an **App Password** if you have 2-Factor Authentication enabled.

```
# Set your mail server for sending alerts
set mailserver smtp.gmail.com port 587
    username "your-email@example.com" password "your-16-digit-app-password"
    using tlsv12

# Customize the email format (optional)
set mail-format { 
  from:    monit@your-server-hostname.com
  subject: Monit Alert -- $EVENT on $SERVICE
  message: $EVENT Service $SERVICE
                Date:        $DATE
                Action:      $ACTION
                Host:        $HOST
                Description: $DESCRIPTION
}

# Set the recipient for alerts
set alert your-recipient-email@example.com
```

Replace the placeholder values with your actual email, App Password, and the recipient's email address.

###### Enable the Web Interface

The web interface provides a convenient dashboard to view the status of all monitored services. Find the `set httpd port 2812` section and uncomment it.

```
# Enable the web interface
set httpd port 2812 and
    # Restrict access to localhost only for security
    use address localhost 
    # Or allow access from a specific IP
    # use address 192.168.1.100  
    
    # Set a username and password
    allow admin:monit
```

For security, it's best to keep `use address localhost` and access it via an SSH tunnel. If you need direct access, replace `localhost` with your server's IP address and make sure your firewall is configured.

The `allow admin:monit` line sets the username to `admin` and the password to `monit`.

##### Example: Monitor for Hardware Failure

*Hardware failure* can mean many things. A common and easy-to-monitor proxy for a failing hard drive is rapidly increasing **disk space usage** or running out of **inodes**. **Monit** can monitor this for you.

It's best practice to add new checks in separate files inside the `/etc/monit/conf.d/` directory.

1. **Create a new configuration file for your check:**

```bash
sudo nano /etc/monit/conf.d/disk-check
```

2. **Add the monitoring rules:** Paste the following configuration into the file. This rule checks the root filesystem (`/`) and sends an `alert` if disk or inode usage exceeds *85%*.

```
# Check the root filesystem for space and inode usage
check filesystem rootfs with path /
  if space usage > 85% then alert
  if inode usage > 85% then alert
```

3. The `alert` action tells Monit to send an email to the recipient you configured in `monitrc`.

##### Apply and Test 

1. **Test the Monit configuration for syntax errors:**

```bash
sudo monit -t
```

If it says "Control file syntax OK," you are ready to proceed.

2. **Reload Monit to apply the changes:**

```bash
sudo systemctl reload monit
```

3. **Verify the configuration:**  

* **Via Web Browser:** If you enabled the web interface, navigate to `http://<your-server-ip>:2812`. You'll be prompted for the username (`admin`) and password (`monit`) you set. You should see the `rootfs` filesystem check listed.  

* **Via Command Line:** Run the following command to see a summary of all monitored services.  

```bash
sudo monit status
```

To test the email alert, you could temporarily lower the threshold in your `disk-check` file to a value you know is exceeded (e.g., `if space usage > 10% then alert`), reload Monit, wait for the email, and then change it back to a sensible value.

