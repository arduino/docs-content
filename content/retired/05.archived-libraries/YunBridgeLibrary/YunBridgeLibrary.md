---
title: 'Bridge Library for Yún devices'
description: 'The Bridge library simplifies communication between the ATmega32U4 - or the board attached if you use the shield - and the AR9331.'
author: Arduino
---

***This library is archived and is no longer being maintained. It can be still be downloaded and used, but is read-only and cannot be contributed to. For more information, you can view this repository on [GitHub](https://github.com/arduino-libraries/Bridge).***

## Overview

The [Yún](https://www.arduino.cc/en/Products/ArduinoYUN) has two processors on board. One is an ATmega32U4 like on the [Leonardo](https://www.arduino.cc/en/Main/ArduinoBoardLeonardo). The other is an Atheros 9331, running Linux and the OpenWRT wireless stack, which enables the board to connect to WiFi and Ethernet networks. It is possible to call programs or custom scripts on the Linux system through the Arduino to connect with various internet services. The [Yún Shield](https://www.arduino.cc/en/Main/ArduinoYunShield) shares the same architecture and features, but it is a shield and needs to be attached to a board, where the microcontroller is interfaced with the Atheros processor through hardware Serial port.

The Bridge library simplifies communication between the ATmega32U4 - or the board attached if you use the shield - and the AR9331. Bridge commands from the board microcontroller are interpreted by Python® on the AR9331. Its role is to execute programs on the GNU/Linux side when asked by Arduino, provide a shared storage space for sharing data like sensor readings between the Arduino and the Internet, and receiving commands from the Internet and passing them directly to the Arduino.

Bridge allows communication in both directions, acting as an interface to the the Linux command line. For a brief explanations of the terminal and executing commands on Linux [see here](https://www.arduino.cc/en/Tutorial/LinuxCLI).

To become familiar with the Yún family boards please see the [Yún getting started page](https://www.arduino.cc/en/Guide/ArduinoYun) and the or the [Yún Shield getting started page](https://www.arduino.cc/en/Guide/ArduinoYunShield).

### Process

Process is used to launch processes on the Linux processor, and other things like shell scripts.

### Console

Console can be used to communicate with the network monitor in the Arduino IDE, through a shell. Functionally, it is very similar to Serial.

### FileIO

An interface to the Linux file system. Can be used to read/write files on the SD card, or on the USB memory if you are using the Yún Shield.

### HttpClient

Creates a HTTP client on Linux. Acts as a wrapper for common CURL commands, by extending Process.

### Mailbox

An asynchronous, session-less interface for communicating between Linux and Arduino.

### BridgeClient

An Arduino based HTTP client, modeled after the EthernetClient class.

### BridgeServer

An Arduino based HTTP server, modeled after the EthernetServer class.

### Temboo

An interface to Temboo making it easy to connect to a large variety of online tools. See the [Tembo documentation](https://temboo.com/arduino) for more.

### Examples

- [Bridge](https://www.arduino.cc/en/Tutorial/Bridge): Access the pins of the board with a web browser.
- [Console ASCII Table](https://www.arduino.cc/en/Tutorial/ConsoleAsciiTable): Demonstrates printing various formats to the Console.
- [Console Pixel](https://www.arduino.cc/en/Tutorial/ConsolePixel): Control an LED through the Console.
- [Console Read](https://www.arduino.cc/en/Tutorial/ConsoleRead): Parse information from the Console and repeat it back.
- [Datalogger](https://www.arduino.cc/en/Tutorial/YunDatalogger): Store sensor information on a SD card.
- [File Write Script](https://www.arduino.cc/en/Tutorial/FileWriteScript): Demonstrates how to write and execute a shell script with Process.
- [HTTP Client](https://www.arduino.cc/en/Tutorial/HttpClient): Create a simple client that downloads a webpage and prints it to the serial monitor.
- [HTTP Client Console](https://www.arduino.cc/en/Tutorial/HttpClientConsole): Create a simple client that downloads a webpage and prints it to the serial monitor via WiFi using Console.
- [Mailbox Read Messages](https://www.arduino.cc/en/Tutorial/MailboxReadMessage): Send text messages to the Arduino processor using REST API through a browser.
- [Process](https://www.arduino.cc/en/Tutorial/Process): Demonstrates how to use Process to run Linux commands.
- [Remote Due Blink](https://www.arduino.cc/en/Tutorial/RemoteDueBlink): Demonstrates how to upload remotely a sketch on DUE boards.
- [Shell Commands](https://www.arduino.cc/en/Tutorial/ShellCommands): Use Process to run shell commands.
- [SpacebrewYun](http://docs.spacebrew.cc/): See the Spacebrew documentation pages for more infos on the Examples listed in the Arduino Software.
- [Temboo](https://temboo.com/arduino): See the Temboo documentation section for more infos on the Examples listed in the Arduino Software.
- [Temperature Web Panel](https://www.arduino.cc/en/Tutorial/TemperatureWebPanel): Post sensor data on a webpage when requested by a browser.
- [Time Check](https://www.arduino.cc/en/Tutorial/TimeCheck): Get the time from a network time server and print it to the serial monitor.
- [WiFi Status](https://www.arduino.cc/en/Tutorial/WiFiStatus): Runs a pre-configured script that reports back the strength of the current WiFi network.
- [Yun First Config](https://www.arduino.cc/en/Tutorial/YunFirstConfig): Connect your Yun product to the WiFi networks in a breeze using the Serial Monitor and answering a few simple questions within it.
- [Yun Serial Terminal](https://www.arduino.cc/en/Tutorial/YunSerialTerminal): Access the Linux Terminal through the serial monitor.

## Bridge class
Bridge is the base class for all Bridge based calls. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `begin()`

#### Description
Starts Bridge, facilitating communication between the AVR and Linux processor. This should be called once in setup()

begin() is a blocking function. Once you call Bridge.begin(), nothing else will happen in your sketch until it has completed. This process takes approximately three seconds.

#### Syntax
```
Bridge.begin()
```
#### Parameters
none

#### Returns
none

---

### `put()`
#### Description
The put() function allows you to store data on the Linux processor using a Key/Value structure. The Key field is like a label and you can associate a value to it. The key name must be unique in order to identify the correct value. On the Linux side there is a data store where all the keys and the values are saved.

The datastore is saved in the RAM of the AR9331, you will lose the datastore when you restart the bridge software on the Linux side (through power cycling, resetting the Linux processor, or uploading a sketch through WiFi or Ethernet). You will not lose the datastore if you reset the ATMega32u4 processor.

#### Syntax
```
bridge.put(key, value)
```
#### Parameters
key: char or string, the key name you want to assign to identify the value.

value: char or string, the value you want to store.

#### Returns
None

---

### `get()`
#### Description
get() allows you to read a key/value item previously saved on the Linux processor. You can request for a value stored in the datastore by passing get() the Key you want to search for, the support buffer, and its size. The Key is similar to a label, used to identify an associated value. The key name must be unique in order to identify the correct value.

The datastore is saved in RAM, you will lose the datastore when you restart the bridge software on the Linux side (through power cycling, resetting the Linux processor, or uploading a sketch through WiFi or Ethernet). You will not lose the datastore if you reset the ATMega32u4 processor.

#### Syntax
```
bridge.get(key, buffer, buffer_length)
```
#### Parameters
key: The name of the key associated with the value you are requesting.

buffer: The support buffer used to save the value returned from the searched Key. A string terminator is added after the last byte that compose the value filed has been read.

buffer_length: the length of the buffer passed to the function.

#### Returns
The function returns the length of the read byte of the requested value.

---

### `transfer()`
#### Description
transfer() is used by other functions that communicate between the ATMega32u4 microcontroller and the Linux processor.

Method to transfer a frame. This methods implement a protocol that feature error correction and response from the Linux processor

The two sides of Bridge make use of a serial protocol to transfer a message to each other. A call to a Bridge.transfer(), sends a message to the Linux side and waits for an answer. transfer() also checks for the integrity of the packet and rejects packet that contain errors.

The function implements a re-transmission mechanism if an acknowledgment is not sent from Linux within 100 ms, or if the packet is corrupt. The re-transmission is repeated until an answer is received from Linux.

transfer() function returns the length of the buffer that contains the answer from Linux.

#### Syntax
```
transfer(buff1, len1, buff2, len2, buff3, len3, rxbuff, rxlen);

derived functions:
transfer(buff1, len1);
transfer(buff1, len1, rxBuff, rxLen);
transfer(buff1, len1, buff2, len2, rxBuff, rxLen);

```
#### Parameters
buff_N: is the buffer N array with the content of the message you want to send. The transfer function support up to 3 buffers to be concatenated.

len_N: is the number of element contained in the buffer_N.

rxbuff: is the support buffer that you pass as a parameter where the answer from the linux side will be stored.

rxLen: is the length of the rxBuffer.

#### Returns
The length of the buffer that contains the answer from Linux. In case the rxlen is shorter than the length of the answer, the function will return rxlen to indicate that the rx buffer is full.'

## Process class
Process is the base class for all Bridge based calls for communicating with the Yun's shell. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `begin()`
#### Description
Starts a Linux named process. Only the command should be called here. followed by run() or runAsynchronously(), and optionally addParameter(). The named process does not start executing until run() is called.

#### Syntax
```
Process.begin(cmd)
```
#### Parameters
cmd (string) : the Linux command you wish to run.
#### Returns
none

---

### `addParameter()`
#### Description
addParameter() adds a parameter to a Linux command initiated with begin(). It's not necessary to add spaces, addParameter() inserts them for you.

#### Syntax
```
Process.addParameter(param)
```
#### Parameters
param (string) : The parameter you wish to add to a command
#### Returns
none

---

### `run()`
#### Description
Starts a Linux process identified in Process.begin().

run() is a blocking function. That is, once you call Process.run(), nothing else will happen in your sketch until it has completed. The time depends on the nature of the command you are executing. For a non-blocking alternative, see runAsynchronously().

#### Syntax
```
Process.run()
```
#### Parameters
none
#### Returns
int

---

### `runAsynchronously()`
#### Description
Starts a Linux process identified in Process.begin().

Unlike run(), runAsynchronously() is not-blocking. Your sketch will continue to run while the Linux process runs in the background.

Please note that since Process.begin(). calls close the running process is terminated. This is the reason why you can not run 2 processes the same time with the same Process instance.

#### Syntax
```
Process.runAsynchronously()
```
#### Parameters
none

#### Returns
none

---

### `running()`
#### Description
Checks a process started by runAsynchronously() to see if it is still running.

#### Syntax
```
Process.running()
```
#### Parameters
none

#### Returns
boolean

---

### `exitValue()`
#### Description
Returns the exit value (aka return code) of a process that was running. Used by run() and runShellCommand() to return the status of the process that the user has launched.

exitValue() #### Returns a 0 if the process is has completed correctly.

If an error occurred during the process the exit value will different than 0. There isn't a standard definition for the return code, it depends on the process. Refer to the documentation of the process to know what the code means.

#### Syntax
```
Process.exitValue()
```
#### Parameters
none

#### Returns
unsigned int. 0 if the process completed correctly. Any value other than 0 means an error occurred during the process. There isn't a standard for the return code, depends on the process you have run.


---

### `close()`
#### Description
Closes a process started by runAsynchronously().

#### Syntax
```
Process.close()
```
#### Parameters
none

#### Returns
none

---

### `runShellCommand()`
#### Description
Starts a shell command in Linux.

runShellCommand() is a blocking function. That is, once you call Process.runShellCommand(), nothing else will happen in your sketch until it has completed. The time depends on the nature of the command you are executing. For a non-blocking alternative, see runShellCommandAsynchronously().

#### Syntax
```
Process.runShellCommand(cmd)
```
#### Parameters
cmd : String containing the command
#### Returns
int

---

### `runShellCommandAsynchronously()`
#### Description
Starts a Linux shell command

Unlike runShellCommand(), runShellCommandAsynchronously() is not-blocking. Your sketch will continue to run while the Linux process runs in the background.

Please note that since Process.begin(). calls close the running process is terminated. This is the reason why you can not run 2 processes the same time with the same Process instance.

#### Syntax
```
Process.runShellCommandAsynchronously(cmd)
```
#### Parameters
cmd : String containing the command to execute
#### Returns
none

---

### `available()`
#### Description
Get the number of bytes (characters) available for reading from the Linux connection. This is data that's already arrived and stored in the receive buffer. available() inherits from the Stream utility class.

#### Syntax
```
Process.available()
```
#### Parameters
none

#### Returns
the number of bytes available to read

---

### `read()`
#### Description
Reads incoming data from a Linux process. read() inherits from the Stream utility class.

#### Syntax
```
Process.read()
```
#### Parameters
none

#### Returns
int : the first byte of incoming data available (or -1 if no data is available)

---

### `write()`
#### Description
Writes data to a Linux process. This data is sent as a byte or series of bytes. write() inherits from the Stream utility class.

#### Syntax
```
Process.write(val)
Process.write(str)
Process.write(buf, len)
```
#### Parameters
val: a value to send as a single byte
str: a string to send as a series of bytes
buf: an array to send as a series of bytes
len: the length of the buffer
#### Returns
byte : the number of bytes written. Reading the number is optional.

---

### `peek()`
#### Description
Returns the next byte (character) of incoming data from a Linux process without removing it from the internal buffer. Successive calls to peek() will return the same character, as will the next call to read(). peek() inherits from the Stream utility class.

#### Syntax
```
Process.peek()
```
#### Parameters
none

#### Returns
int : the first byte of incoming data available (or -1 if no data is available)

---

### `flush()`
#### Description
Clears the Process buffer of any bytes. Waits for the transmission of outgoing data to complete.

#### Syntax
```
Process.flush()
```
#### Parameters
none

#### Returns
none

## Console class
Console is the base class for all Bridge based calls for communicating with the Yun through the serial monitor as if it were a termnal. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `begin()`
#### Description
Starts a terminal session accessible through the serial monitor.

#### Syntax
```
Console.begin()
```
#### Parameters
none

#### Returns
none

---

### `end()`
#### Description
Ends a terminal session accessible through the serial monitor.

#### Syntax
```
Console.end()
```
#### Parameters
none

#### Returns
none

---

### `buffer()`
#### Description
Sets the size of the buffer for the console.

#### Syntax
```
Console.buffer(size)
```
#### Parameters
size (int) : the size of the buffer
#### Returns
none

---

### `noBuffer()`
#### Description
Removes any buffer for the console.

#### Syntax
```
Console.noBuffer()
```
#### Parameters
none

#### Returns
none

---

### `connected()`
#### Description
Reports back the connection status of the console.

#### Syntax
```
Console.connected()
```
#### Parameters
none

#### Returns
boolean

---

### `available()`
#### Description
Get the number of bytes (characters) available for reading from the Console. This is data that's already arrived and stored in the receive buffer. available() inherits from the Stream utility class.

#### Syntax
```
Console.available()
```
#### Parameters
none

#### Returns
the number of bytes available to read

---

### `read()`
#### Description
Reads incoming data from the console connection. read() inherits from the Stream utility class.

#### Syntax
```
Console.read()
```
#### Parameters
none

#### Returns
int : the first byte of incoming data available (or -1 if no data is available)

---

### `write()`
#### Description
Writes data to the console. This data is sent as a byte or series of bytes. write() inherits from the Stream utility class.

#### Syntax
```
Console.write(val)
Console.write(str)
Console.write(buf, len)
```
#### Parameters
val: a value to send as a single byte
str: a string to send as a series of bytes
buf: an array to send as a series of bytes
len: the length of the buffer
#### Returns
byte : the number of bytes written. Reading the number is optional.

---

### `peek()`
#### Description
Returns the next byte (character) of incoming data from the console without removing it from the internal buffer. Successive calls to peek() will return the same character, as will the next call to read(). peek() inherits from the Stream utility class.

#### Syntax
```
Console.peek()
```
#### Parameters
none

#### Returns
int : the first byte of incoming data available (or -1 if no data is available)

---

### `flush()`
#### Description
Clears the Console buffer of any bytes. Waits for the transmission of outgoing data to complete.

#### Syntax
```
Console.flush()
```
#### Parameters
none

#### Returns
none

## FileIO class
FileIO is the base class for writing and reading to a SD card mounted on the Yún. It is part of Bridge. It is not called directly, but invoked whenever you use a function that relies on it.

To prepare your SD card for writing and reading, create an empty folder in the SD root named "arduino". This will ensure that the Yún will create a link to the SD to the "/mnt/sd" path.

---

### `FileSystem.begin()`
#### Description
Initializes the SD card and FileIO class. This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
FileSystem.begin()
```
#### Parameters
none

#### Returns
boolean : true on success; false on failure

---

### `FileSystem.open()`
#### Description
Opens a file on the SD card. If the file is opened for writing, it will be created if it doesn't already exist (but the directory containing it must already exist).

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

Note: only one file can be open at a time.

#### Syntax
```
FileSystem.open(filename)
FileSystem.open(filename, mode)
```
#### Parameters
filename: the name the file to open, which can:include directories (delimited by forward slashes, /) - char
mode (optional): the mode in which to open the file, defaults to FILE_READ. Can be either "
FILE_READ: open the file for reading, starting at the beginning of the file.
FILE_WRITE: open the file for reading and writing, starting at the end of the file.
#### Returns
a File object referring to the opened file; if the file couldn't be opened, this object will evaluate to false in a boolean context, i.e. you can test the return value with "if (f)".

---

### `FileSystem.exists()`
#### Description
Tests whether a file or directory exists on the SD card.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and hardware connections are different.

#### Syntax
```
FileSystem.exists(filename)
```
#### Parameters
filename: the name of the file to test for existence, which can include directories (delimited by forward-slashes, /)

#### Returns
boolean : true if the file or directory exists, false if not

---

### `FileSystem.mkdir()`
#### Description
A wrapper for the mkdir command with the -p flag, FileSystem.mkdir() creates a named directory on an SD card.

This communicates with the Linux distribution through Bridge.

#### Syntax
```
FileSystem.mkdir(directory)
```
#### Parameters
directory: the name of the name of the directory to create. Nested directories can be created with a /.

#### Returns
boolean : true if the file or directory exists, false if not

---

### `FileSystem.rmdir()`
#### Description
A wrapper for the rmdir command, FileSystem.rmdir() removes an empty directory from an SD card. Before removing a directory with a file in it, you must call FileSystem.remove().

This communicates with the Linux distribution through Bridge.

#### Syntax
```
FileSystem.rmdir(directory)
```
#### Parameters
directory: the name of the directory to remove.

#### Returns
boolean : true if successful, false if not

---

### `FileSystem.remove()`
#### Description
A wrapper for the rm command, FileSystem.remove() removes a file or directory from an SD card.

This communicates with the Linux distribution through Bridge.

#### Syntax
```
FileSystem.remove(file)
```
#### Parameters
file: the name of the directory to remove.

#### Returns
boolean : true if successful, false if not

---

### `File`
#### Description
A named file to manipulate through FileIO.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
File filename
```
#### Parameters
'filename'' : the named instance of the file.

#### Returns
none

---

### `close()`
#### Description
Close an open file, and ensure that any data written to it is physically saved to the SD card.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
'file'.close(file)
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())

#### Returns
none

---

### `rewindDirectory()`
#### Description
rewindDirectory() will bring you back to the first file in the directory on an SD card. Used in conjunction with openNextFile().

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.rewindDirectory()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())

#### Returns
none

---

### `openNextFile()`
#### Description
Reports the next file or folder in a directory.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.openNextFile()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())

#### Returns
char : the next file or folder in the path

---

### `seek()`
#### Description
Seek to a new position in the file, which must be between 0 and the size of the file (inclusive).

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.seek(pos)
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
pos: the position to which to seek (unsigned long)
#### Returns
boolean : true for success, false for failure

---

### `position()`
#### Description
Get the current position within the file (i.e. the location to which the next byte will be read from or written to).

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.position()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
#### Returns
unsigned long :the position within the file

---

### `size()`
#### Description
Get the size of the current file.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.size()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
#### Returns
unsigned long : the size of the file in bytes

---

### `available()`
#### Description
Check if there are any bytes available for reading from the file.

available() inherits from the Stream utility class.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.available()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
#### Returns
int : the number of bytes available

---

### `read()`
#### Description
Read a byte from the file.

read() inherits from the Stream utility class.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.read()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
#### Returns
The next byte (or character), or -1 if none is available.

---

### `write()`
#### Description
Write data to the file.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.write(data)
file.write(buf, len)
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
data: the byte, char, or string (char *) to write
buf: an array of characters or bytes
len: the number of elements in buf
#### Returns
byte : write() will return the number of bytes written, though reading that number is optional

---

### `peek()`
#### Description
Read a byte from the file without advancing to the next one. Successive calls to peek() will return the same value, as will the next call to read().

peek() inherits from the Stream utility class.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.peek()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
#### Returns
The next byte (or character), or -1 if none is available.

---

### `flush()`
#### Description
flush() clears the buffer once all outgoing characters have been sent.

flush() inherits from the Stream utility class.

This communicates with the Linux distribution through Bridge. While functionally similar to the SD library, the underlying code and connections are different.

#### Syntax
```
file.flush()
```
#### Parameters
file: an instance of the File class (returned by FileIO.open())
#### Returns
none

## Mailbox class
Mailbox is the base class for all Bridge based calls that use the mailbox interface for communicating between the two processors on the Yun.

---

### `begin()`
#### Description
Starts the mailbox on the Linux and Arduino processors.

#### Syntax
```
Mailbox.begin()
```
#### Parameters
none

#### Returns
none

---

### `end()`
#### Description
Closes all existing mailboxes on the Linux and Arduino processors.

#### Syntax
```
Mailbox.end()
```
#### Parameters
none

#### Returns
none

---

### `readMessage()`
#### Description
Receive a message and store it inside a String

#### Syntax
```
Mailbox.readMessage(buffer, size)
```
#### Parameters
buffer : String : the named buffer to store the message in
size : unsigned int, max length 128 : number of bytes in the message
#### Returns
message from Bridge.transfer()

---

### `writeMessage()`
#### Description
Sends a message from the 32U4 to the AR9331

#### Syntax
```
Mailbox.writeMessage(buffer, size)
Mailbox.writeMessage(content)
```
#### Parameters
buffer : int : the buffer to send the message to
size : unsigned int, max length 128 : number of bytes in the message
content : String : message to send information to.
#### Returns
none

---

### `writeJSON()`
#### Description
Sends a JSON message from the 32U4 to the AR9331

#### Syntax
```
Mailbox.JSON(message)
```
#### Parameters
message : String : message to send information to.
#### Returns
none

---

### `messageAvailable()`
#### Description
Checks and Returns the size of the next available message.

#### Syntax
```
Mailbox.messageAvailable()
```
#### Parameters
none

#### Returns
int : The size of the next available message. Returns 0 if there is no messages in the queue.

See also
Bridge.transfer()

## HttpClient class
HttpClient extends Process and acts as a wrapper for common cURL commands by creating a HTTP client in the Linux side.

---

### `get()`
#### Description
A wrapper for the cURL command get.

The method gets the specified URL from a server.

#### Syntax
```
client.get(url)
```
#### Parameters
client : an instance of the HttpClient class
url : a string containing the url to retrieve
#### Returns
none

---

### `getAsynchronously()`
#### Description
A wrapper for the cURL command get. This command runs asynchronously and is non-blocking

The method gets the specified URL from a server.

#### Syntax
```
client.getAsynchronously(url)
```
#### Parameters
client : an instance of the HttpClient class
url : a string containing the url to retrieve
#### Returns
none

---

### `ready()`
#### Description
Checks if an HTTP request initiated with getAsynchronously() is still in progress.

#### Syntax
```
client.ready()
```
#### Parameters
client : an instance of the HttpClient class
#### Returns
boolean false if the request is still in progress, true if the request is completed

---

### `getResult()`
#### Description
Checks a process started by runAsynchronously() to see if it is still running.

#### Syntax
```
client.getResult()
```
#### Parameters
client : an instance of the HttpClient class
#### Returns
// see also exitValue()

## BridgeClient class
---

### `BridgeClient`
#### Description
BridgeClient is the base class for all client based calls on the Yún. It is not called directly, but invoked whenever you use a function that relies on it.

#### Syntax
```
BridgeClient client
```
#### Parameters
client : the named client to refer to

#### Returns
None

---

### `BridgeSSLClient`
#### Description
BridgeSSLClient is the base class for all client based calls to SSL services on the Yún. It is not called directly, but invoked whenever you use a function that relies on it.

#### Syntax
```
BridgeSSLClient client
```
#### Parameters
client : the named client to refer to

#### Returns
None

---

### `stop()`
#### Description
Disconnect from the server.

#### Syntax
```
client.stop()
```
#### Parameters
client : the named instance of YunClient

#### Returns
None

---

### `connect()`
#### Description
Connects to a specified IP address and port. The return value indicates success or failure. Also supports DNS lookups when using a domain name.

#### Syntax
```
client.connect()
client.connect(ip, port)
client.connect(URL, port)
```
#### Parameters
client : the named instance of YunClient
ip: the IP address that the client will connect to (array of 4 bytes)
URL: the domain name the client will connect to (string, ex.:"arduino.cc")
port: the port that the client will connect to (int)
#### Returns
Returns true if the connection succeeds, false if not.

---

### `connected()`
#### Description
Whether or not the client is connected. Note that a client is considered connected if the connection has been closed but there is still unread data.

#### Syntax
```
client.connected()
```
#### Parameters
client : the named instance of YunClient
#### Returns
Returns true if the client is connected, false if not.

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
client : the named instance of YunClient
#### Returns
The number of bytes available.

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
client : the named instance of YunClient
#### Returns
The next byte (or character), or -1 if none is available.

---

### `write()`
#### Description
Write data to the server the client is connected to.

#### Syntax
```
client.write(data)
```
#### Parameters
client : the named instance of YunClient
data: the byte or char to write
#### Returns
byte: the number of characters written. it is not necessary to read this value.

---

### `peek()`
#### Description
Read a byte from the file without advancing to the next one. That is, successive calls to peek() will return the same value, as will the next call to read().

#### Syntax
```
client.peek()
```
#### Parameters
client : the named instance of YunClient
#### Returns
int : the first byte of incoming data available (or -1 if no data is available)

---

### `flush()`
#### Description
Discard any bytes that have been written to the client but not yet read.

#### Syntax
```
client.flush()
```
#### Parameters
client : the named instance of YunClient
#### Returns
none

## BridgeServer class
BridgeServer is the base class for all server server based calls on the Yun. It is not called directly, but invoked whenever you use a function that relies on it.

---

### `begin()`
#### Description
Tells the server to begin listening for incoming connections. The Bridge server communicates on port 5555 at localhost.

#### Syntax
```
server.begin()
```
#### Parameters
server : the named instance of YunServer

#### Returns
None

---

### `listenOnLocalhost()`
#### Description
Tells the server to begin listening for incoming connections. The Bridge server communicates on port 5555 at localhost.

#### Syntax
```
server.listenOnLocalhost()
```
#### Parameters
server : the named instance of YunServer

#### Returns
None

---

### `noListenOnLocalhost()`
#### Description
Tells the server to begin listening for incoming connections. The Bridge server communicates on port 5555 at a specified address.

#### Syntax
```
server.noListenOnLocalhost()
```
#### Parameters
server : the named instance of YunServer

#### Returns
None

---

### `write()`
#### Description
Write data to all the clients connected to a server.

#### Syntax
```
server.write(data)
```
#### Parameters
server : the named instance of YunServer
data : the value to write (byte or char)
#### Returns
byte
write() Returns the number of bytes written. It is not necessary to read this.

## Deprecated classes

---

### `YunClient`
NOTE: The use of YunClient is deprecated. Use BridgeClient or the BridgeSSLClient instead.

#### Description
YunClient is the base class for all client based calls on the Yun. It is not called directly, but invoked whenever you use a function that relies on it.

#### Syntax
```
YunClient client
```
#### Parameters
client : the named client to refer to

#### Returns
None

---

### `YunServer Constructor`
NOTE: The use of YunServer is deprecated. Use BridgeServer instead.

#### Description
YunServer is the base class for all server server based calls on the Yun. It is not called directly, but invoked whenever you use a function that relies on it.

#### Syntax
```
YunServer server
```
#### Parameters
server : the named instance of YunServer