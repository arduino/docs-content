---
title: 'GSM Library'
description: 'A library made for the Arduino GSM Shield, allowing you to send/receive text messages, make/receive phone calls and  connect to the Internet.'
author: Arduino
---

***This library is archived and is no longer being maintained. It can be still be downloaded and used, but is read-only and cannot be contributed to. For more information, you can view this repository on [GitHub](https://github.com/arduino-libraries/GSM).***

The GSM Library is included with [Arduino IDE 1.0.4 and later](https://www.arduino.cc/en/Main/Software).

With the [Arduino GSM Shield](/retired/shields/arduino-gsm-shield), this library enables an Arduino board to do most of the operations you can do with a GSM phone: place and receive voice calls, send and receive SMS, and connect to the internet over a GPRS network.

The GSM shield has a modem that transfers data from a serial port to the GSM network. The modem executes operations via a series of AT commands. The library abstracts low level communications between the modem and SIM card. It relies on the [Software Serial library](https://www.arduino.cc/en/Reference/SoftwareSerial) for communication between the modem and Arduino.

Typically, each individual command is part of a larger series necessary to execute a particular function. The library can also receive information and return it to you when necessary.

To use this library
```
#include <GSM.h>
```
## Library structure
As the library enables multiple types of functionality, there are a number of different classes.

- The GSM class takes care of commands to the radio modem. This handles the connectivity aspects of the shield and registers your system in the GSM infrastructure. All of your GSM/GPRS programs will need to include an object of this class to handle the necessary low level communication.
- Voice call handling, managed by the GSMVoiceCall class.
- Send/receive SMS messages, managed by the GSM_SMS class.
- The GPRSClass is for connecting to the internet.
- GSMClient includes implementations for a client, similar to the Ethernet and WiFi libraries.
- GSMServer includes implementations for a server, similar to the Ethernet and WiFi libraries. NB : A number of network operators do not allow for incoming connections from the public internet, but will allow them from inside their own. Check with your operator to see what restrictions there are on data use.
- A number of utility classes such as GSMScanner and GSMModem
## Ethernet library compatibility
The library tries to be as compatible as possible with the current Ethernet library. Porting a program from an Arduino Ethernet or WiFi library to an Arduino with the GSM Shield should be fairly easy. While it is not possible to simply run Ethernet-compatible code on the GSM shield as-is, some minor, library specific, modifications will be necessary, like including the GSM and GPRS specific libraries and getting network configuration settings from your cellular network provider.

## Examples
There are two groups of examples for the GSM shield. There are examples to illustrate the possibilities of the shield, like how to send SMS messages and connect to the internet. There is also set of example tools that you can use to debug the functionality of the library and the hardware at lower level.

- [Gsm Web Client](https://www.arduino.cc/en/Tutorial/GSMExamplesWebClient): Download the content of a website to your Arduino board through GPRS.
- [Gsm Web Server](https://www.arduino.cc/en/Tutorial/GSMExamplesWebServer): Create a wireless web server through GPRS.
- [Make Voice Call](https://www.arduino.cc/en/Tutorial/GSMExamplesMakeVoiceCall): Get your shield to make phone calls from the Serial Monitor.
-  [Send SMS](https://www.arduino.cc/en/Tutorial/GSMExamplesSendSMS): Use the Serial Monitor to type in SMS messages to different phone numbers.
- [Receive Voice Call](https://www.arduino.cc/en/Tutorial/GSMExamplesReceiveVoiceCall): Check the status of the modem while getting voice calls.
- [Receive SMS](https://www.arduino.cc/en/Tutorial/GSMExamplesReceiveSMS): Read SMS messages and prompt them to the Serial Monitor.
### Tools
- [Band Management](https://www.arduino.cc/en/Tutorial/GSMToolsBandManagement): Manage the band the GSM shield connects to.
- [GSM Scan Networks](https://www.arduino.cc/en/Tutorial/GSMToolsGsmScanNetworks): Check for the available networks.
- [Pin Management](https://www.arduino.cc/en/Tutorial/GSMToolsPinManagement): Manage the PIN number of your SIM card.
- [Test GPRS](https://www.arduino.cc/en/Tutorial/GSMToolsTestGPRS): Test the proper functionality of the GPRS network using your SIM card.
- [Test Modem](https://www.arduino.cc/en/Tutorial/GSMToolsTestModem): Read the IMEI of your modem.
- [Test Web Server](https://www.arduino.cc/en/Tutorial/GSMToolsTestWebServer): Create a webserver with your GSM shield.

## GSM class 
---

### `GSM constructor`
#### Description
GSM is the base class for all GSM based functions.

#### Syntax
```
GSM GSMAccess
GSM GSMAccess(debug)
```
#### Parameters
debug: boolean (default FALSE) flag for turing on the debug mode. This will print out the AT commands from the modem.

#### Example
```
// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess;     // include a 'true' parameter for debug enabled

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY){
      notConnected = false;
      Serial.println("Connected to network");
    }
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }
}

void loop()
{
  // Nothing here
}
 
```

---

### `begin()`
#### Description
Connects to the GSM network identified on the SIM card.

#### Syntax
```
gsm.begin()
gsm.begin(pin)
gsm.begin(pin, restart)
gsm.begin(pin, restart, sync)
```
#### Parameters
- pin : character array with the PIN to access a SIM card (default = 0)
- restart : boolean, determines whether to restart modem or not (default= true)
- sync : boolean, synchronous (true, default) or asynchronous (false) mode
#### Returns
0 if asynchronous. If synchronous, returns status : ERROR, IDLE, CONNECTING, GSM_READY, GPRS_READY, TRANSPARENT_CONNECTED

#### Example
```#include <GSM.h>

#define PINNUMBER ""

GSM gsm; // include a 'true' parameter for debug enabled

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsm.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
}

void loop()
{
// once connected do something interesting
}
```

---

### `shutdown()`
#### Description
Disconnects from the GSM network identified on the SIM card by powering the modem off.

#### Syntax
```
gsm.shutdown()
```
#### Parameters
none

#### Returns
boolean : 0 while executing, 1 when successful

#### Example
```#include <GSM.h>

#define PINNUMBER ""

GSM gsm; // include a 'true' parameter for debug enabled

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsm.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");

  gsm.shutdown();
  Serial.println("GSM terminated");

}

void loop()
{
}
```

## GSMVoiceCall class

---

### `GSMVoiceCall constructor`
#### Description
GSMVoiceCall is the base class for all GSM functions relating to receiving and making voice calls.

---

### `getVoiceCallStatus()`
#### Description
Returns status of the voice call.

#### Syntax
```
voice.getVoiceCallStatus()
```
#### Parameters
none

#### Returns
char : IDLE_CALL, CALLING, RECEIVINGCALL, TALKING

#### Example
```

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSMVoiceCall vcs;


char numtel[20];           // buffer for the incoming call

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Receive Voice Call");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  // This makes sure the modem notifies correctly incoming events
  vcs.hangCall();

  Serial.println("Waiting Call");
}

void loop()
{
  // Check the status of the voice call
  switch (vcs.getvoiceCallStatus())
  {
    case IDLE_CALL: // Nothing is happening

      break;

    case CALLING: // This should never happen, as we are not placing a call

      Serial.println("CALLING");
      break;

    case RECEIVINGCALL: // Yes! Someone is calling us

      Serial.println("RECEIVING CALL");

      // Retrieve the calling number
      vcs.retrieveCallingNumber(numtel, 20);

      // Print the calling number
      Serial.print("Number:");
      Serial.println(numtel);

      // Answer the call, establish the call
      vcs.answerCall();        
      break;

    case TALKING:  // In this case the call would be established

      Serial.println("TALKING. Enter line to interrupt.");
      while(Serial.read()!='\n')
        delay(100);
      vcs.hangCall();
      Serial.println("HANG. Waiting Call.");      
      break;
  }
  delay(1000);
}
 
```

---

### `ready()`
#### Description
Reports if the previous voice command has executed successfully

#### Syntax
```
voice.ready()
```
#### Parameters
none

#### Returns
int
In asynchronous mode, ready() returns 0 if the last command is still executing, 1 if there is success, and >1 in case of an error. In synchronous mode, it returns 1 if it executed successfully, 0 if not.

---

### `voiceCall()`
#### Description
Places a voice call to a specified number. The methods returns different information depending on the GSM connection mode (synchronous or asynchronous). See below for details.

#### Syntax
```
voice.voiceCall(number)
```
#### Parameters
number : char array. The number to call.
#### Returns
int
In asynchronous mode, voiceCall() returns 0 if last command is still executing, 1 if successful, and >1 in case of an error. In synchronous mode, it returns 1 if the call is placed, 0 if not.

#### Example
```#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSMVoiceCall vcs;

String remoteNumber = "";  // the number you will call
char charbuffer[20];

void setup()
{

  // initialize serial communications
  Serial.begin(9600);

  Serial.println("Make Voice Call");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized.");
  Serial.println("Enter phone number to call.");

}

void loop()
{

  // add any incoming characters to the String:
  while (Serial.available() > 0)
  {
    char inChar = Serial.read();
    // if it's a newline, that means you should make the call:
    if (inChar == '\n')
    {
      // make sure the phone number is not too long:
      if (remoteNumber.length() < 20)
      {
        // let the user know you're calling:
        Serial.print("Calling to : ");
        Serial.println(remoteNumber);
        Serial.println();

        // Call the remote number
        remoteNumber.toCharArray(charbuffer, 20);


        // Check if the receiving end has picked up the call
        if(vcs.voiceCall(charbuffer))
        {
          Serial.println("Call Established. Enter line to end");
          // Wait for some input from the line
          while(Serial.read() !='\n' && (vcs.getvoiceCallStatus()==TALKING));          
          // And hang up
          vcs.hangCall();
        }
        Serial.println("Call Finished");
        remoteNumber="";
        Serial.println("Enter phone number to call.");
      }
      else
      {
        Serial.println("That's too long for a phone number. I'm forgetting it");
        remoteNumber = "";
      }
    }
    else
    {
      // add the latest character to the message to send:
      if(inChar!='\r')
        remoteNumber += inChar;
    }
  }
}
 
```

---

### `answerCall()`
#### Description
Accepts an incoming voice call. The method returns are different depending on the modem mode (asynchronous or synchronous), see below for details.

#### Syntax
```
voice.answerCall()
```
#### Parameters
none

#### Returns
int
In asynchronous mode, answerCall() returns 0 if last command is still executing, 1 if successful, and >1 in case of an error. In synchronous mode, it returns 1 if the call is answered, 0 if not.

#### Example
```#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSMVoiceCall vcs;

char numtel[20];           // buffer for the incoming call

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Receive Voice Call");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  // This makes sure the modem notifies correctly incoming events
  vcs.hangCall();

  Serial.println("Waiting Call");
}

void loop()
{
  // Check the status of the voice call
  switch (vcs.getvoiceCallStatus())
  {
    case IDLE_CALL: // Nothing is happening

      break;

    case CALLING: // This should never happen, as we are not placing a call

      Serial.println("CALLING");
      break;

    case RECEIVINGCALL: // Yes! Someone is calling us

      Serial.println("RECEIVING CALL");

      // Retrieve the calling number
      vcs.retrieveCallingNumber(numtel, 20);

      // Print the calling number
      Serial.print("Number:");
      Serial.println(numtel);

      // Answer the call, establish the call
      vcs.answerCall();        
      break;

    case TALKING:  // In this case the call would be established

      Serial.println("TALKING. Enter line to interrupt.");
      while(Serial.read()!='\n')
        delay(100);
      vcs.hangCall();
      Serial.println("HANG. Waiting Call.");      
      break;
  }
  delay(1000);
}

 
```

---

### `hangCall()`
#### Description
Hang up an established call or during incoming rings. Depending on the modems mode (synchronous or asynchronous) the method will return differently, see below for more detail.

#### Syntax
```
voice.hangCall()
```
#### Parameters
none

#### Returns
int
In asynchronous mode, hangCall() returns 0 if the last command is still executing, 1 if there is success, and >1 in case of an error. In synchronous mode, it returns 1 if the call is hung, 0 if not.

#### Example
```
// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSMVoiceCall vcs;


char numtel[20];           // buffer for the incoming call

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Receive Voice Call");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  // This makes sure the modem notifies correctly incoming events
  vcs.hangCall();

  Serial.println("Waiting Call");
}

void loop()
{
  // Check the status of the voice call
  switch (vcs.getvoiceCallStatus())
  {
    case IDLE_CALL: // Nothing is happening

      break;

    case CALLING: // This should never happen, as we are not placing a call

      Serial.println("CALLING");
      break;

    case RECEIVINGCALL: // Yes! Someone is calling us

      Serial.println("RECEIVING CALL");

      // Retrieve the calling number
      vcs.retrieveCallingNumber(numtel, 20);

      // Print the calling number
      Serial.print("Number:");
      Serial.println(numtel);

      // Answer the call, establish the call
      vcs.answerCall();        
      break;

    case TALKING:  // In this case the call would be established

      Serial.println("TALKING. Enter line to interrupt.");
      while(Serial.read()!='\n')
        delay(100);
      vcs.hangCall();
      Serial.println("HANG. Waiting Call.");      
      break;
  }
  delay(1000);
}

 
```

---

### `retrieveCallingNumber()`
#### Description
Retrieves the calling number, and stores it.

#### Syntax
```
voice.retrieveCallingNumber(number, size)
```
#### Parameters
- number : char array to hold the number
- size : the size of the array
#### Returns
int
In asynchronous mode, retrieveCallingNumber() returns 0 if the last command is still executing, 1 if success, and >1 if there is an error. In synchronous mode, it returns 1 if the number is obtained 0 if not.

#### Example
```#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSMVoiceCall vcs;

char numtel[20];           // buffer for the incoming call

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Receive Voice Call");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  // This makes sure the modem notifies correctly incoming events
  vcs.hangCall();

  Serial.println("Waiting Call");
}

void loop()
{
  // Check the status of the voice call
  switch (vcs.getvoiceCallStatus())
  {
    case IDLE_CALL: // Nothing is happening

      break;

    case CALLING: // This should never happen, as we are not placing a call

      Serial.println("CALLING");
      break;

    case RECEIVINGCALL: // Yes! Someone is calling us

      Serial.println("RECEIVING CALL");

      // Retrieve the calling number
      vcs.retrieveCallingNumber(numtel, 20);

      // Print the calling number
      Serial.print("Number:");
      Serial.println(numtel);

      // Answer the call, establish the call
      vcs.answerCall();        
      break;

    case TALKING:  // In this case the call would be established

      Serial.println("TALKING. Enter line to interrupt.");
      while(Serial.read()!='\n')
        delay(100);
      vcs.hangCall();
      Serial.println("HANG. Waiting Call.");      
      break;
  }
  delay(1000);
}

 
```

## GSM_SMS class
---

### `GSM_SMS constructor`
#### Description
GSM_SMS is the base class for all GSM functions relating to receiving and sending SMS messages.

---

### `beginSMS()`
#### Description
Identifies the telephone number to send an SMS message to.

#### Syntax
```
SMS.beginSMS(number)
```
#### Parameters
number : char array, the phone number to send the SMS to

#### Returns
int
In asynchronous mode, beginSMS() returns 0 if the last command is still executing, 1 if success, and >1 if there is an error. In synchronous mode, it returns 1 if it successfully executes, and 0 if it does not.

#### Example
```#include <GSM.h>

#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Sender");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
}

void loop()
{

  Serial.print("Enter a mobile number: ");
  char remoteNumber[20];  // telephone number to send sms
  readSerial(remoteNumber);
  Serial.println(remoteNumber);

  // sms text
  Serial.print("Now, enter SMS content: ");
  char txtMsg[200];
  readSerial(txtMsg);
  Serial.println("SENDING");
  Serial.println();
  Serial.println("Message:");
  Serial.println(txtMsg);

  // send the message
  sms.beginSMS(remoteNumber);
  sms.print(txtMsg);
  sms.endSMS();
  Serial.println("\nCOMPLETE!\n");
}

/*
  Read input serial
 */
int readSerial(char result[])
{
  int i = 0;
  while(1)
  {
    while (Serial.available() > 0)
    {
      char inChar = Serial.read();
      if (inChar == '\n')
      {
        result[i] = '\0';
        Serial.flush();
        return 0;
      }
      if(inChar!='\r')
      {
        result[i] = inChar;
        i++;
      }
    }
  }
}
```

---

### `ready()`
#### Description
Gets the status if the last GSMSMS command.

#### Syntax
```
SMS.ready()
```
#### Parameters
none

#### Returns
int
In asynchronous mode, ready() returns 0 if the last command is still executing, 1 if it was successful, and >1 if there is an error. In synchronous mode, it returns 1 if the previous successfully executed, and 0 if it has not.

---

### `endSMS()`
#### Description
Tells the modem that the SMS message is complete and sends it.

#### Syntax
```
SMS.endSMS()
```
#### Parameters
none

#### Returns
int
In asynchronous mode, endSMS() returns 0 if it is still executing, 1 if successful, and >1 if there is an error. In synchronous mode, it returns 1 if the previous successfully executed, and 0 if it has not.

#### Example
```#include <GSM.h>

#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Sender");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
}

void loop()
{

  Serial.print("Enter a mobile number: ");
  char remoteNumber[20];  // telephone number to send sms
  readSerial(remoteNumber);
  Serial.println(remoteNumber);

  // sms text
  Serial.print("Now, enter SMS content: ");
  char txtMsg[200];
  readSerial(txtMsg);
  Serial.println("SENDING");
  Serial.println();
  Serial.println("Message:");
  Serial.println(txtMsg);

  // send the message
  sms.beginSMS(remoteNumber);
  sms.print(txtMsg);
  sms.endSMS();
  Serial.println("\nCOMPLETE!\n");
}

/*
  Read input serial
 */
int readSerial(char result[])
{
  int i = 0;
  while(1)
  {
    while (Serial.available() > 0)
    {
      char inChar = Serial.read();
      if (inChar == '\n')
      {
        result[i] = '\0';
        Serial.flush();
        return 0;
      }
      if(inChar!='\r')
      {
        result[i] = inChar;
        i++;
      }
    }
  }
}
```

---

### `available()`
#### Description
Checks to see if there is a SMS messages on the SIM card to be read, and reports back the number of characters in the message.

#### Syntax
```
SMS.available()
```
#### Parameters
none

#### Returns
int : the number of characters in the message

#### Example
```#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

char remoteNumber[20];  // Holds the emitting number

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Receiver");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
  Serial.println("Waiting for messages");
}

void loop()
{
  char c;

  // If there are any SMSs available()  
  if (sms.available())
  {
    Serial.println("Message received from:");

    // Get remote number
    sms.remoteNumber(remoteNumber, 20);
    Serial.println(remoteNumber);

    // This is just an example of message disposal    
    // Messages starting with # should be discarded
    if(sms.peek()=='#')
    {
      Serial.println("Discarded SMS");
      sms.flush();
    }

    // Read message bytes and print them
    while(c=sms.read())
      Serial.print(c);

    Serial.println("\nEND OF MESSAGE");

    // delete message from modem memory
    sms.flush();
    Serial.println("MESSAGE DELETED");
  }

  delay(1000);

}

 
```

---

### `remoteNumber()`
#### Description
Retrieves the phone number an from an incoming SMS message and stores it in a named array.

#### Syntax
```
SMS.remoteNumber(number, size)
```
#### Parameters
- number : char array, a named array that will hold the sender's number
- size : int, the size of the array
#### Returns
int
In asynchronous mode, remoteNumber() returns 0 if the last command is still executing, 1 if success, and >1 if there is an error. In synchronous mode, it returns 1 if it successfully executes, and 0 if it does not.

#### Example
```#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

char remoteNumber[20];  // Holds the emitting number

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Receiver");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
  Serial.println("Waiting for messages");
}

void loop()
{
  char c;

  // If there are any SMSs available()  
  if (sms.available())
  {
    Serial.println("Message received from:");

    // Get remote number
    sms.remoteNumber(remoteNumber, 20);
    Serial.println(remoteNumber);

    // This is just an example of message disposal    
    // Messages starting with # should be discarded
    if(sms.peek()=='#')
    {
      Serial.println("Discarded SMS");
      sms.flush();
    }

    // Read message bytes and print them
    while(c=sms.read())
      Serial.print(c);

    Serial.println("\nEND OF MESSAGE");

    // delete message from modem memory
    sms.flush();
    Serial.println("MESSAGE DELETED");
  }

  delay(1000);

}
```

---

### `read()`
#### Description
Reads a byte from an SMS message. read() inherits from the Stream utility class.

#### Syntax
```
SMS.read()
```
#### Parameters
none

#### Returns
int - the first byte of incoming serial data available (or -1 if no data is available)

#### Example
```#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

char remoteNumber[20];  // Holds the emitting number

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Receiver");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
  Serial.println("Waiting for messages");
}

void loop()
{
  char c;

  // If there are any SMSs available()  
  if (sms.available())
  {
    Serial.println("Message received from:");

    // Get remote number
    sms.remoteNumber(remoteNumber, 20);
    Serial.println(remoteNumber);

    // This is just an example of message disposal    
    // Messages starting with # should be discarded
    if(sms.peek()=='#')
    {
      Serial.println("Discarded SMS");
      sms.flush();
    }

    // Read message bytes and print them
    while(c=sms.read())
      Serial.print(c);

    Serial.println("\nEND OF MESSAGE");

    // delete message from modem memory
    sms.flush();
    Serial.println("MESSAGE DELETED");
  }

  delay(1000);

}
 
```

---

### `write()`
#### Description
Writes a character to a SMS message.

#### Syntax
```
SMS.write(val)
```
#### Parameters
val: a character to send in the message

#### Returns
byte - write() will return the number of bytes written, though reading that number is optional

#### Example
```#include <GSM.h>

#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Sender");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
}

void loop()
{

  Serial.print("Enter a mobile number: ");
  char remoteNumber[20];  // telephone number to send sms
  readSerial(remoteNumber);
  Serial.println(remoteNumber);

  // sms text
  Serial.print("Now, enter SMS content: ");
  char txtMsg[200];
  readSerial(txtMsg);
  Serial.println("SENDING");
  Serial.println();
  Serial.println("Message:");
  Serial.println(txtMsg);

  // send the message
  sms.beginSMS(remoteNumber);
  sms.print(txtMsg);
  sms.endSMS();
  Serial.println("\nCOMPLETE!\n");
}

/*
  Read input serial
 */
int readSerial(char result[])
{
  int i = 0;
  while(1)
  {
    while (Serial.available() > 0)
    {
      char inChar = Serial.read();
      if (inChar == '\n')
      {
        result[i] = '\0';
        Serial.flush();
        return 0;
      }
      if(inChar!='\r')
      {
        result[i] = inChar;
        i++;
      }
    }
  }
}
```

---

### `print()`
#### Description
Writes a char array as a SMS message.

#### Syntax
```
SMS.print(message)
```
#### Parameters
message - char array, the message to send

#### Returns
int : the number of bytes printed

#### Example
```#include <GSM.h>

#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Sender");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
}

void loop()
{

  Serial.print("Enter a mobile number: ");
  char remoteNumber[20];  // telephone number to send sms
  readSerial(remoteNumber);
  Serial.println(remoteNumber);

  // sms text
  Serial.print("Now, enter SMS content: ");
  char txtMsg[200];
  readSerial(txtMsg);
  Serial.println("SENDING");
  Serial.println();
  Serial.println("Message:");
  Serial.println(txtMsg);

  // send the message
  sms.beginSMS(remoteNumber);
  sms.print(txtMsg);
  sms.endSMS();
  Serial.println("\nCOMPLETE!\n");
}

/*
  Read input serial
 */
int readSerial(char result[])
{
  int i = 0;
  while(1)
  {
    while (Serial.available() > 0)
    {
      char inChar = Serial.read();
      if (inChar == '\n')
      {
        result[i] = '\0';
        Serial.flush();
        return 0;
      }
      if(inChar!='\r')
      {
        result[i] = inChar;
        i++;
      }
    }
  }
}
```

---

### `peek()`
#### Description
Returns the next byte (character) of an incoming SMS without removing it from the message. That is, successive calls to peek() will return the same character, as will the next call to read(). peek() inherits from the Stream utility class.

#### Syntax
```
SMS.peek()
```
#### Parameters
none

#### Returns
int - the first byte available of a SMS message (or -1 if no data is available)

#### Example
```/*
SMS receiver

 This sketch, for the Arduino GSM shield, waits for SMS messages
 and displays them through the Serial port.

 Circuit:
 * GSM shield

 created 25 Feb 2012
 by Javier Zorzano / TD

 This example is in the public domain.
*/

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

char remoteNumber[20];  // Holds the emitting number

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Receiver");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
  Serial.println("Waiting for messages");
}

void loop()
{
  char c;

  // If there are any SMSs available()  
  if (sms.available())
  {
    Serial.println("Message received from:");

    // Get remote number
    sms.remoteNumber(remoteNumber, 20);
    Serial.println(remoteNumber);

    // This is just an example of message disposal    
    // Messages starting with # should be discarded
    if(sms.peek()=='#')
    {
      Serial.println("Discarded SMS");
      sms.flush();
    }

    // Read message bytes and print them
    while(c=sms.read())
      Serial.print(c);

    Serial.println("\nEND OF MESSAGE");

    // delete message from modem memory
    sms.flush();
    Serial.println("MESSAGE DELETED");
  }

  delay(1000);

}

 
```

---

### `flush()`
#### Description
flush() clears the modem memory of any sent messages once all outgoing characters have been sent. flush() inherits from the Stream utility class.

#### Syntax
```
SMS.flush()
```
#### Parameters
none

#### Returns
none

#### Example
```/*
SMS receiver

 This sketch, for the Arduino GSM shield, waits for SMS messages
 and displays them through the Serial port.

 Circuit:
 * GSM shield

 created 25 Feb 2012
 by Javier Zorzano / TD

 This example is in the public domain.
*/

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance
GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

char remoteNumber[20];  // Holds the emitting number

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  Serial.println("SMS Messages Receiver");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized");
  Serial.println("Waiting for messages");
}

void loop()
{
  char c;

  // If there are any SMSs available()  
  if (sms.available())
  {
    Serial.println("Message received from:");

    // Get remote number
    sms.remoteNumber(remoteNumber, 20);
    Serial.println(remoteNumber);

    // This is just an example of message disposal    
    // Messages starting with # should be discarded
    if(sms.peek()=='#')
    {
      Serial.println("Discarded SMS");
      sms.flush();
    }

    // Read message bytes and print them
    while(c=sms.read())
      Serial.print(c);

    Serial.println("\nEND OF MESSAGE");

    // delete message from modem memory
    sms.flush();
    Serial.println("MESSAGE DELETED");
  }

  delay(1000);

}

 
```

## GPRS class
---

### `GPRS constructor`
#### Description
GPRS is the base class for all GPRS functions, such as internet client and server behaviors.

---

### `attachGPRS()`
#### Description
Connects to the specified Access Point Name (APN) to initiate GPRS communication.

Every cellular provider has an Access Point Name (APN) that serves as a bridge between the cellular network and the internet. Sometimes, there is a username and password associated with the connection point. For example, the Bluevia APN is bluevia.movistar.es, but it has no password or login name.

This page lists a number of carrier's information, but it may not be up to date. You may need to get this information from your service provider.

#### Syntax
```
grps.attachGPRS(APN, user, password)
```
#### Parameters
- APN : char array, the Access Point Name (APN) provided by the mobile operator
- user : char array, the username for the APN
- password : char array, the password to access the APN
#### Returns
ERROR, IDLE, CONNECTING, GSM_READY, GPRS_READY, TRANSPARENT_CONNECTED

#### Example
```#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// APN data
#define GPRS_APN       "GPRS_APN" // replace your GPRS APN
#define GPRS_LOGIN     "login"    // replace with your GPRS login
#define GPRS_PASSWORD  "password" // replace with your GPRS password


// initialize the library instance
GPRS gprs;
GSM gsmAccess;     // include a 'true' parameter for debug enabled
GSMServer server(80); // port 80 (http default)

// timeout
const unsigned long __TIMEOUT__ = 10*1000;

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while(notConnected)
  {
    if((gsmAccess.begin(PINNUMBER)==GSM_READY) &
        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD)==GPRS_READY))
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("Connected to GPRS network");

  // start server
  server.begin();

  //Get IP.
  IPAddress LocalIP = gprs.getIPAddress();
  Serial.println("Server IP address=");
  Serial.println(LocalIP);
}

void loop() {


  // listen for incoming clients
  GSM3MobileClientService client = server.available();



  if (client)
  {  
    while (client.connected())
    {
      if (client.available())
      {
        Serial.println("Receiving request!");
        bool sendResponse = false;
        while(char c=client.read()) {
          if (c == '\n') sendResponse = true;
        }

     // if you've gotten to the end of the line (received a newline
     // character)
       if (sendResponse)
       {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println();
          client.println("<html>");
          // output the value of each analog input pin
          for (int analogChannel = 0; analogChannel < 6; analogChannel++) {
            client.print("analog input ");
            client.print(analogChannel);
            client.print(" is ");
            client.print(analogRead(analogChannel));
            client.println("<br />");      
          }
          client.println("</html>");
          //necessary delay
          delay(1000);
          client.stop();
        }
      }
    }
  }
}

 
```

## GSMClient class
---

### `Client`
#### Description
Client is the base class for all GPRS client based calls. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `ready()`
#### Description
Gets the status of the last command

#### Syntax
```
client.ready()
```
#### Parameters
none

#### Returns
In asynchronous mode, ready() returns 0 if the last command is still executing, 1 if it was successful, and >1 if there is an error. In synchronous mode, it returns 1 if the previous successfully executed, and 0 if it has not.

---

### `connect()`
#### Description
Connects to a specified IP address and port. The return value indicates success or failure.

#### Syntax
```
client.connect(ip, port)
```
#### Parameters
- ip: the IP address that the client will connect to (array of 4 bytes)
- port: the port that the client will connect to (int)
#### Returns
boolean : Returns true if the connection succeeds, false if not.

#### Example
```/*
  Web client

 This sketch connects to a website through a GSM shield. Specifically,
 this example downloads the URL "http://arduino.cc/" and prints it
 to the Serial monitor.

 Circuit:
 * GSM shield attached to an Arduino
 * SIM card with a data plan

 created 8 Mar 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/GSMExamplesWebClient

 */

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// APN data
#define GPRS_APN       "GPRS_APN" // replace your GPRS APN
#define GPRS_LOGIN     "login"    // replace with your GPRS login
#define GPRS_PASSWORD  "password" // replace with your GPRS password

// initialize the library instance
GSMClient client;
GPRS gprs;
GSM gsmAccess;

// URL, path & port (for example: arduino.cc)
char server[] = "arduino.cc";
char path[] = "/";
int port = 80; // port 80 is the default for HTTP

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Starting Arduino web client.");
  // connection state
  boolean notConnected = true;

  // After starting the modem with GSM.begin()
  // attach the shield to the GPRS network with the APN, login and password
  while(notConnected)
  {
    if((gsmAccess.begin(PINNUMBER)==GSM_READY) &
        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD)==GPRS_READY))
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("connecting...");

  // if you get a connection, report back via serial:
  if (client.connect(server, port))
  {
    Serial.println("connected");
    // Make a HTTP request:
    client.print("GET ");
    client.print(path);
    client.println(" HTTP/1.0");
    client.println();
  }
  else
  {
    // if you didn't get a connection to the server:
    Serial.println("connection failed");
  }
}

void loop()
{
  // if there are incoming bytes available
  // from the server, read them and print them:
  if (client.available())
  {
    char c = client.read();
    Serial.print(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.available() && !client.connected())
  {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();

    // do nothing forevermore:
    for(;;)
      ;
  }
}
```

---

### `beginWrite()`
#### Description
Tells the client to start writing to the server it is connected to.

#### Syntax
```
client.beginWrite()
```
#### Parameters
none

#### Returns
none

---

### `write()`
#### Description
Write data to the server the client is connected to.

#### Syntax
```
client.write(data)
client.write(buffer)
client.write(buffer, size)
```
#### Parameters
- data: the value to write (byte or char)
- buffer : an array of data (byte or char) to write
- size : size of the buffer to write (byte)
#### Returns
byte - write() returns the number of bytes written. It is not necessary to read this.

---

### `endWrite()`
#### Description
Stops writing data to a server

#### Syntax
```
client.endWrite()
```
#### Parameters
none

#### Returns
none

---

### `connected()`
#### Description
Returns whether or not the client is connected. A client is considered connected if the connection has been closed but there is still unread data.

#### Syntax
```
client.connected()
```
#### Parameters
none

#### Returns
boolean - Returns true if the client is connected, false if not.

#### Example
```/*
  Web client

 This sketch connects to a website through a GSM shield. Specifically,
 this example downloads the URL "http://arduino.cc/" and prints it
 to the Serial monitor.

 Circuit:
 * GSM shield attached to an Arduino
 * SIM card with a data plan

 created 8 Mar 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/GSMExamplesWebClient

 */

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// APN data
#define GPRS_APN       "GPRS_APN" // replace your GPRS APN
#define GPRS_LOGIN     "login"    // replace with your GPRS login
#define GPRS_PASSWORD  "password" // replace with your GPRS password

// initialize the library instance
GSMClient client;
GPRS gprs;
GSM gsmAccess;

// URL, path & port (for example: arduino.cc)
char server[] = "arduino.cc";
char path[] = "/";
int port = 80; // port 80 is the default for HTTP

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Starting Arduino web client.");
  // connection state
  boolean notConnected = true;

  // After starting the modem with GSM.begin()
  // attach the shield to the GPRS network with the APN, login and password
  while(notConnected)
  {
    if((gsmAccess.begin(PINNUMBER)==GSM_READY) &
        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD)==GPRS_READY))
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("connecting...");

  // if you get a connection, report back via serial:
  if (client.connect(server, port))
  {
    Serial.println("connected");
    // Make a HTTP request:
    client.print("GET ");
    client.print(path);
    client.println(" HTTP/1.0");
    client.println();
  }
  else
  {
    // if you didn't get a connection to the server:
    Serial.println("connection failed");
  }
}

void loop()
{
  // if there are incoming bytes available
  // from the server, read them and print them:
  if (client.available())
  {
    char c = client.read();
    Serial.print(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.available() && !client.connected())
  {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();

    // do nothing forevermore:
    for(;;)
      ;
  }
}
```

---

### `read()`
#### Description
Read the next byte received from the server the client is connected to (after the last call to read()).

read() inherits from the Stream utility class.

#### Syntax
```
client.read()
```
#### Parameters
none

#### Returns
int - The next byte (or character), or -1 if none is available.

#### Example
```/*
  Web client

 This sketch connects to a website through a GSM shield. Specifically,
 this example downloads the URL "http://arduino.cc/" and prints it
 to the Serial monitor.

 Circuit:
 * GSM shield attached to an Arduino
 * SIM card with a data plan

 created 8 Mar 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/GSMExamplesWebClient

 */

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// APN data
#define GPRS_APN       "GPRS_APN" // replace your GPRS APN
#define GPRS_LOGIN     "login"    // replace with your GPRS login
#define GPRS_PASSWORD  "password" // replace with your GPRS password

// initialize the library instance
GSMClient client;
GPRS gprs;
GSM gsmAccess;

// URL, path & port (for example: arduino.cc)
char server[] = "arduino.cc";
char path[] = "/";
int port = 80; // port 80 is the default for HTTP

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Starting Arduino web client.");
  // connection state
  boolean notConnected = true;

  // After starting the modem with GSM.begin()
  // attach the shield to the GPRS network with the APN, login and password
  while(notConnected)
  {
    if((gsmAccess.begin(PINNUMBER)==GSM_READY) &
        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD)==GPRS_READY))
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("connecting...");

  // if you get a connection, report back via serial:
  if (client.connect(server, port))
  {
    Serial.println("connected");
    // Make a HTTP request:
    client.print("GET ");
    client.print(path);
    client.println(" HTTP/1.0");
    client.println();
  }
  else
  {
    // if you didn't get a connection to the server:
    Serial.println("connection failed");
  }
}

void loop()
{
  // if there are incoming bytes available
  // from the server, read them and print them:
  if (client.available())
  {
    char c = client.read();
    Serial.print(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.available() && !client.connected())
  {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();

    // do nothing forevermore:
    for(;;)
      ;
  }
}
```

---

### `available()`
#### Description
Returns the number of bytes available for reading (that is, the amount of data that has been written to the client by the server it is connected to).

available() inherits from the Stream utility class.

#### Syntax
```
client.available()
```
#### Parameters
none

#### Returns
The number of bytes available.

#### Example
```/*
  Web client

 This sketch connects to a website through a GSM shield. Specifically,
 this example downloads the URL "http://arduino.cc/" and prints it
 to the Serial monitor.

 Circuit:
 * GSM shield attached to an Arduino
 * SIM card with a data plan

 created 8 Mar 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/GSMExamplesWebClient

 */

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// APN data
#define GPRS_APN       "GPRS_APN" // replace your GPRS APN
#define GPRS_LOGIN     "login"    // replace with your GPRS login
#define GPRS_PASSWORD  "password" // replace with your GPRS password

// initialize the library instance
GSMClient client;
GPRS gprs;
GSM gsmAccess;

// URL, path & port (for example: arduino.cc)
char server[] = "arduino.cc";
char path[] = "/";
int port = 80; // port 80 is the default for HTTP

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Starting Arduino web client.");
  // connection state
  boolean notConnected = true;

  // After starting the modem with GSM.begin()
  // attach the shield to the GPRS network with the APN, login and password
  while(notConnected)
  {
    if((gsmAccess.begin(PINNUMBER)==GSM_READY) &
        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD)==GPRS_READY))
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("connecting...");

  // if you get a connection, report back via serial:
  if (client.connect(server, port))
  {
    Serial.println("connected");
    // Make a HTTP request:
    client.print("GET ");
    client.print(path);
    client.println(" HTTP/1.0");
    client.println();
  }
  else
  {
    // if you didn't get a connection to the server:
    Serial.println("connection failed");
  }
}

void loop()
{
  // if there are incoming bytes available
  // from the server, read them and print them:
  if (client.available())
  {
    char c = client.read();
    Serial.print(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.available() && !client.connected())
  {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();

    // do nothing forevermore:
    for(;;)
      ;
  }
}
```

---

### `peek()`
#### Description
Returns the next byte (character) of an incoming message removing it from the message. That is, successive calls to peek() will return the same character, as will the next call to read(). peek() inherits from the Stream utility class.

#### Syntax
```
client.peek()
```
#### Parameters
none

#### Returns
int - the next byte in an incoming message.

---

### `flush()`
#### Description
Discards any bytes that have been written to the client but not yet read.

flush() inherits from the Stream utility class.

#### Syntax
```
client.flush()
```
#### Parameters
none

#### Returns
none

---

### `stop()`
#### Description
Disconnects from the server

#### Syntax
```
client.stop()
```
#### Parameters
none

#### Returns
none

#### Example
```/*
  Web client

 This sketch connects to a website through a GSM shield. Specifically,
 this example downloads the URL "http://arduino.cc/" and prints it
 to the Serial monitor.

 Circuit:
 * GSM shield attached to an Arduino
 * SIM card with a data plan

 created 8 Mar 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/GSMExamplesWebClient

 */

// libraries
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// APN data
#define GPRS_APN       "GPRS_APN" // replace your GPRS APN
#define GPRS_LOGIN     "login"    // replace with your GPRS login
#define GPRS_PASSWORD  "password" // replace with your GPRS password

// initialize the library instance
GSMClient client;
GPRS gprs;
GSM gsmAccess;

// URL, path & port (for example: arduino.cc)
char server[] = "arduino.cc";
char path[] = "/";
int port = 80; // port 80 is the default for HTTP

void setup()
{
  // initialize serial communications
  Serial.begin(9600);
  Serial.println("Starting Arduino web client.");
  // connection state
  boolean notConnected = true;

  // After starting the modem with GSM.begin()
  // attach the shield to the GPRS network with the APN, login and password
  while(notConnected)
  {
    if((gsmAccess.begin(PINNUMBER)==GSM_READY) &
        (gprs.attachGPRS(GPRS_APN, GPRS_LOGIN, GPRS_PASSWORD)==GPRS_READY))
      notConnected = false;
    else
    {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("connecting...");

  // if you get a connection, report back via serial:
  if (client.connect(server, port))
  {
    Serial.println("connected");
    // Make a HTTP request:
    client.print("GET ");
    client.print(path);
    client.println(" HTTP/1.0");
    client.println();
  }
  else
  {
    // if you didn't get a connection to the server:
    Serial.println("connection failed");
  }
}

void loop()
{
  // if there are incoming bytes available
  // from the server, read them and print them:
  if (client.available())
  {
    char c = client.read();
    Serial.print(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.available() && !client.connected())
  {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();

    // do nothing forevermore:
    for(;;)
      ;
  }
}
```

## GSMServer class

---

### `Server`
#### Description
Server is the base class for all GPRS server based calls. It is not called directly, but invoked whenever you use a function that relies on it.

#### Syntax
```
GSMServer server(port);
```
#### Parameters
port: int, the port the server will accept connections on. The default web port is 80.

---

### `ready()`
#### Description
Get last command status to the server

#### Syntax
```
server.ready()
```
#### Parameters
none

#### Returns
int - 0 if last command is still executing, 1 if success, >1 if an error.

---

### `beginWrite()`
#### Description
Begins writing to connected clients.

#### Syntax
```
server.beginWrite()
```
#### Parameters
none

#### Returns
none

---

### `write()`
#### Description
Write data to all the clients connected to a server.

#### Syntax
```
server.write(data)
server.write(buffer)
server.write(buffer, size)
```
#### Parameters
- data: the value to write (byte or char)
- buffer : an array of data (byte or char) to write
- size : size of the buffer to write (byte)
#### Returns
byte - write() returns the number of bytes written. It is not necessary to read this.

---

### `endWrite()`
#### Description
Tells the server to stop writing to connected clients.

#### Syntax
```
server.endWrite()
```
#### Parameters
none

#### Returns
none

---

### `read()`
#### Description
Read the next byte received from an attached client (after the last call to read()).

read() inherits from the Stream utility class.

#### Syntax
```
server.read()
```
#### Parameters
none

#### Returns
int - The next byte (or character), or -1 if none is available.

---

### `available()`
#### Description
Listens for incoming clients

#### Syntax
```
server.available()
```
#### Parameters
none

#### Returns
int : the number of connected clients

---

### `stop()`
#### Description
Tells the server to stop listening for incoming connections.

#### Syntax
```
server.stop()
```
#### Parameters
none

#### Returns
none

## GSMModem class
---

### `GSMModem Constructor`
#### Description
GSMModem is the base class for calls that have specific diagnostic functionality with the modem. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `begin()`
#### Description
Checks the modem status, and restarts it. Call this before GSMModem.getIMEI().

#### Syntax
```
modem.begin()
```
#### Parameters
none

#### Returns
int : returns 1 if modem is OK, otherwise returns an error.

---

### `getIMEI()`
#### Description
Retrieves the modem's IMEI number. Call this after GSMModem.begin().

#### Syntax
```
modem.getIMEI()
```
#### Parameters
none

#### Returns
String : the modem's IMEI number

#### Example
```// libraries
#include <GSM.h>

// modem verification object
GSMModem modem;

// IMEI variable
String IMEI = "";

void setup()
{
  // initialize serial communications
  Serial.begin(9600);

  // start modem test (reset and check response)
  Serial.print("Starting modem test...");
  if(modem.begin())
    Serial.println("modem.begin() succeeded");
  else
    Serial.println("ERROR, no modem answer.");
}

void loop()
{
  // get modem IMEI
  Serial.print("Checking IMEI...");
  IMEI = modem.getIMEI();

  // check IMEI response
  if(IMEI != NULL)
  {
    // show IMEI in serial monitor
    Serial.println("Modem's IMEI: " + IMEI);
    // reset modem to check booting:
    Serial.print("Resetting modem...");
    modem.begin();
    // get and check IMEI one more time
    if(modem.getIMEI() != NULL)
    {
      Serial.println("Modem is functioning properly");
    }
    else
    {
      Serial.println("Error: getIMEI() failed after modem.begin()");
    }
  }
  else
  {
    Serial.println("Error: Could not get IMEI");
  }
  // do nothing:
  while(true);
}
```

## GSMScanner class
---

### `GSMScanner Constructor`
#### Description
GSMScanner is the base class for calls that have specific diagnostic functionality relating to scanning for available networks. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `begin()`
#### Description
Resets modem hardware.

#### Syntax
```
scanner.begin()
```
#### Parameters
none

#### Returns
int : returns 1 if modem is OK, otherwise returns an error.

---

### `getCurrentCarrier()`
#### Description
Gets and returns the name of the current network carrier.

#### Syntax
```
scanner.getCurrentCarrier()
```
#### Parameters
none

#### Returns
String : name of the current network carrier

---

### `getSignalStrength()`
#### Description
Gets and returns the strength of the signal of the network the modem is attached to.

#### Syntax
```
scanner.getSignalStrength()
```
#### Parameters
none

#### Returns
String : signal strength in 0-31 scale. 31 means power > 51dBm. 99=not detectable

---

### `readNetworks()`
#### Description
Searches for available carriers, and returns a list of them.

#### Syntax
```
scanner.readNetworks()
```
#### Parameters
none

#### Returns
String : A string with list of networks available

## GSMPIN class
---

### `GSMPIN constructor`
#### Description
GSMPIN is the base class for all GSM based functions that deal with interacting with the PIN on the SIM card.

---

### `begin()`
#### Description
Checks the modem status, and restarts it.

#### Syntax
```
GSMPIN.begin()
```
#### Parameters
none

#### Returns
int : returns 1 if modem is OK, otherwise returns an error.

---

### `isPIN()`
#### Description
Checks the SIM card to see if it is locked with a PIN.

#### Syntax
```
pin.isPIN()
```
#### Parameters
none

#### Returns
int : 0 if PIN lock is off, 1 if PIN lock is on, -1 if PUK lock is on, -2 if error exists.

---

### `checkPIN()`
#### Description
Queries the SIM card with a PIN number to see if it is valid.

#### Syntax
```
pin.checkPIN(PIN)
```
#### Parameters
PIN : String with the PIN number to check

#### Returns
int : Returns 0 if the PIN is valid, returns -1 if it is not.

---

### `checkPUK()`
#### Description
Check the SIM if PUK code is correct and establish new PIN code.

#### Syntax
```
pin.checkPUK(puk, pin)
```
#### Parameters
- puk : String with the PUK number to check
-pin : String with the PIN number to check
#### Returns
int : Returns 0 if successful, -1 if it is not.

---

### `changePIN()`
#### Description
Changes the PIN number of a SIM, after verifying the existing one.

#### Syntax
```
pin.changePIN(oldPIN, newPIN)
```
#### Parameters
- oldPIN : String with the existing PIN number 
- newPIN : String with the desired PIN number

#### Returns
none

---

### `switchPIN()`
#### Description
Change PIN lock status.

#### Syntax
```
pin.switchPIN(pin)
```
#### Parameters
pin : String with the existing PIN number

#### Returns
none

---

### `checkReg()`
#### Description
Check if modem was registered in GSM/GPRS network

#### Syntax
```
pin.checkReg()
```
#### Parameters
none 
#### Returns
int : 0 if modem was registered, 1 if modem was registered in roaming, -1 if error exists

---

### `getPinUsed()`
#### Description
Check if PIN lock is used.

#### Syntax
```
pin.getPinUsed()
```
#### Parameters
none 
#### Returns
boolean : TRUE id locked, FALSE if not

---

### `setPinUsed()`
#### Description
Set PIN lock status.

#### Syntax
```
pin.setPinUsed(used)
```
#### Parameters
used : boolean, TRUE to lock the PIN, FALSE to unlock.

#### Returns
none

## GSMBand class
---

### `GSMBand Constructor`
#### Description
GSMBand is the base class for calls that have specific diagnostic functionality relating to the bands the modem can connect to. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `begin()`
#### Description
Checks the modem status, and restarts it.

#### Syntax
```
band.begin()
```
#### Parameters
none

#### Returns
int : returns 1 if modem is OK, otherwise returns an error.

---

### `getBand()`
#### Description
Gets and returns the frequency band the modem is currently connected to. Check http://www.worldtimezone.com/gsm.html for general GSM band information. Typical regional configurations are :

- Europe, Africa, Middle East: E-GSM(900)+DCS(1800)
- USA, Canada, South America: GSM(850)+PCS(1900)
- Mexico: PCS(1900)
- Brazil: GSM(850)+E-GSM(900)+DCS(1800)+PCS(1900)
#### Syntax
```
band.getBand()
```
#### Parameters
none

#### Returns
String : name of the frequency band the modem connects to

- GSM_MODE_UNDEFINED
- GSM_MODE_EGSM
- GSM_MODE_DCS
- GSM_MODE_PCS
- GSM_MODE_EGSM_DCS
- GSM_MODE_GSM850_PCS
- GSM_MODE_GSM850_EGSM_DCS_PCS

---

### `setBand()`
#### Description
Sets the frequency band the modem connects to. Check http://www.worldtimezone.com/gsm.html for general GSM band information. Typical regional configurations are :

- Europe, Africa, Middle East: E-GSM(900)+DCS(1800)
- USA, Canada, South America: GSM(850)+PCS(1900)
- Mexico: PCS(1900)
- Brazil: GSM(850)+E-GSM(900)+DCS(1800)+PCS(1900)
#### Syntax
```
band.setBand(type)
```
#### Parameters
type : String identifying what frequency band the modem should connect to :

- GSM_MODE_UNDEFINED
- GSM_MODE_EGSM
- GSM_MODE_DCS
- GSM_MODE_PCS
- GSM_MODE_EGSM_DCS
- GSM_MODE_GSM850_PCS
- GSM_MODE_GSM850_EGSM_DCS_PCS
#### Returns
boolean : returns true if the process is successful, false if it is not