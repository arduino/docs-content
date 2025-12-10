---
title: 'Weather Audio Notifier'
description: 'Create an auditory weather notification project.'
tags: 
  - Weather
  - Piezo
  - Notification 
libraries:
  - name: ArduinoJson Library
    url: https://github.com/bblanchon/ArduinoJson
hardware:
  - hardware/02.hero/boards/zero
software:
  - ide-v1
  - ide-v2
  - web-editor
author: "Arduino"
---
## Introduction
This tutorial demonstrates how to use the Arduino Zero and the WiFi Shield 101 to act as a web client and parse Json formatted text. Json is well-known data-interchange format which is often used for communication between a server and client, and is particularly useful owing to its easy-to-read format and simplicity to parse and generate. In this example, weather information from [openweathermap.org](http://www.openweathermap.org) is used to display the current weather information. This is then periodically compared with weather information from the following hours.

## Goals

- About Json.
- Use weather data to create an audio notification when the weather changes.

## Hardware & Software Needed

- [Arduino Zero](https://store.arduino.cc/arduino-zero) Board
- [Arduino WiFi Shield 101](https://store.arduino.cc/arduino-wifi-101-shield)
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [ArduinoJson Library](https://github.com/bblanchon/ArduinoJson)
- Piezo
- Jumper wires

## The Circuit

The red wire of the piezo is connected to digital pin 8, and the black wire to ground. Optionally, the audio can be improved by using preloaded .wav files instead of the `tone()` function, in which case the circuit from [this audio player example](https://arduino.cc/en/Tutorial/SimpleAudioPlayerZero) can be substituted (with the addition of the WiFi Shield 101).

![The circuit for this tutorial.](assets/ArduinoWiFi101Piezo.png)



In the image above, the Arduino Zero board would be stacked below the WiFi Shield 101.

## Installing Libraries

The ArduinoJson library can installed from Arduino IDE's library manager. To do this, open the Arduino IDE, go to **Tools-> Manage Libraries..** There you can search **ArduinoJson** and install the library shown. The 'more info' link will take you to the GitHub page which includes all the documentation for the library. For a more detailed explanation on installing and importing libraries see [this tutorial](https://www.arduino.cc/en/Guide/Libraries#toc3).

## Parsing a Json

In this tutorial we use [openweathermap.org](http://www.openweathermap.org) to provide the Json information. An example of the raw information used can be found [here](http://api.openweathermap.org/data/2.5/forecast?q=Turin,it&amp;mode=json&amp;cnt=2), this is the API from openweathermap and the city can be changed in the URL.

Using the Json below as an example, we can see that it contains a lot of information, including the city, coordinates, rain, temperature, wind speeds, etc.
```json
{"city":{"id":3165524,"name":"Torino","coord":{"lon":7.68682,"lat":45.070492},"country":"IT","population":0,"sys":{"population":0}},"cod":"200","message":0.0066,"cnt":2,"list":[{"dt":1442404800,"main":{"temp":22.11,"temp_min":18.61,"temp_max":22.11,"pressure":989.45,"sea_level":1023.92,"grnd_level":989.45,"humidity":89,"temp_kf":3.5},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":80},"wind":{"speed":1.89,"deg":17.5001},"rain":{"3h":0.095},"sys":{"pod":"d"},"dt_txt":"2015-09-16 12:00:00"},{"dt":1442415600,"main":{"temp":22.93,"temp_min":19.62,"temp_max":22.93,"pressure":988.09,"sea_level":1022.61,"grnd_level":988.09,"humidity":79,"temp_kf":3.3},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":92},"wind":{"speed":2.01,"deg":29.502},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-16 15:00:00"}]}
```


It is useful to view this information as a tree using an online Json formatter so that we can easily see which of the nested objects/arrays contains the information in which we are interested. The following image shows the tree view of the previous Json. It is easy to see that inside the root object 'JSON', there is an object called 'city' and an array called 'list' which contains two objects; '0' and '1'. the '0' array contains current weather information and '1' contains later weather information.

If we then open further the 'main' and 'weather' fields, we can see that main contains various information and that 'weather' contains a further object called [0]. The information accessed in this example is 'temp' and 'humidity' which are inside 'main', and 'description' which is inside '0' inside 'weather', all of which are found in both [0] and [1] from the 'list' array.

![Json Tree View](assets/json_tutorial_treeview.png)

The part of the code that deals with parsing the information from the Json is seen in the following block. From the tree view, we can see that there is a root object which represents the entire Json and corresponds to the the 'root' `JsonObject` in the code. From there, we can access the list array with `'root["list"]'`. It can be seen that inside the list there are two objects; `[0]` and `[1]`, which correspond to 'now' and 'later' JsonObjects. Inside each of the objects `now` and `later`, there is an object called `main` and and an array called weather , inside which there is an object called `[0]` which contains the description. We are interested in the information inside `'main'` and `'weather -> [0]'` for both now and later, specifically, temperature, humidity and description. Therefore we can use the following code to access this information and store it either as a String or as a float. We can also access the city name directly from the root:

Note: Arduino Json library provides a syntax which allows you to navigate the tree starting from a JsonObject and searching the values by their labels.

```arduino
JsonArray& list = root["list"];

JsonObject& now = list[0];

JsonObject& later = list[1];

String city = root["city"]["name"];
float tempNow = now["main"]["temp"];
float humidityNow = now["main"]["humidity"];

String weatherNow = now["weather"][0]["description"];

float tempLater = later["main"]["temp"];
float humidityLater = later["main"]["humidity"];

String weatherLater = later["weather"][0]["description"];
```

## Code

The basic concept of this program is that it parses six fields from the Json; humidity, temperature and description for both now and later and compares them at an interval of 10 minutes (can be changed to a shorter period for testing). At the beginning of the sketch, you must manually enter the network name of your Wireless network, the password for this network and the city name and country code without spaces, for example: "NewYork,US".

```arduino
char ssid[] = "ssid";             //  your network SSID (name)
char pass[] = "password";         // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                 // your network key Index number (needed only for WEP)

String nameOfCity = "Turin,IT";   // your city of interest here in format "city,countrycode"
```

The melodies which will be played (for either a positive or negative weather change) are instantiated in the following block where the notes and note durations are defined for later:

```arduino
int posMelody[] = {330,415,494,659};     //E3,G#3,B3,E4
int negMelody[] = {392,370,349,330};     //G3,F#3,F3,E3
int noteDurations[] = {4, 4, 4, 8};      //Will correspond to note lengths 8th,8th,8th,4th
```

A statement to check if 10 minutes have passed is executed inside the loop, and if so a http request is made.

```arduino
if (millis() - lastConnectionTime > postingInterval) {

    // note the time that the connection was made:

    lastConnectionTime = millis();

    httpRequest();

  }
```

After that, there is a check to see whether there are incoming bytes available, which will only happen once every 10 minutes after the http request. Since it is known that a Json message is a nest of curly brackets and that for each open bracket there must be a close bracket, we can deduce that the message starts at the first curly bracket in the stream and ends when the number of open brackets - close brackets = 0. Therefore, the following code waits for the first curly bracket and then sets a variable `startJson` to `1`, indicating that the message has started, and increments a variable endResponse which decrements each time the incoming byte is a close bracket. Then, if `startJson` is true, i.e the message has started, the incoming byte is appended to the string text. If `endResponse = 0` indicating that there were an equal number of close and open brackets, then the message is over, providing that it started (startJson = 1). When both these conditions are met, then the Json is ready to be parsed and the string is sent to the `parseJson()` function.

```arduino
if (client.available()) {

    c = client.read();

    // json contains equal number of open and close curly brackets, therefore by counting

    // the open and close occurrences, we can determine when a json is completely received

    // endResponse == 0 means equal number of open and close curly brackets reached

    if (endResponse == 0 && startJson == true) {

      parseJson(text.c_str());  // parse c string text in parseJson function

      text = "";                // clear text string for the next time

      startJson = false;        // set startJson to false to indicate that a new message has not yet started

    }

    if (c == '{') {

      startJson = true;         // set startJson true to indicate json message has started

      endResponse++;

    }

    if (c == '}') {

      endResponse--;

    }

    if (startJson == true) {

      text += c;

    }

  }
```

The function `printDiffFloat()` compares the two values of the now and later floats and if there is a difference and if so, the difference is printed on the serial monitor. If there is no change, the return; exits the function and nothing is printed nor played.

```arduino
void printDiffFloat(float now, float later, String parameter, String unit) {

  String change;

  if (now > later) {        //if parameter is higher now than later

    change = "drop from ";

  }

  else if (now < later) {   //else if parameter is higher later than now

    change = "rise from ";

  }

  else {                    //else there is no difference

    return;                 //exit function printDiffFloat

  }

  Serial.print("UPDATE: The " + parameter + "will " + change); //print change

  Serial.print(now);

  Serial.print(unit + " to ");

  Serial.print(later);

  Serial.println(unit + "!");
}
```

The function `printDiffString()` checks for keywords inside the now and later strings. If the index of a word such as "rain" is not found because it does not exist inside the string, then the value of the int is set to `-1`. We can then check to see if the word was not in the string of current data but does exist in the string for the future data `(int != -1)`, and if so we can send a notification, either the positive or negative short melody depending on the change and the information of the change is printed in the serial monitor. Note that the search for clear is in a different statement than for words rain, snow and hail so that a positive notification is sounded instead of negative.

```arduino
void printDiffString(String now, String later, String weatherType) {

  int indexNow = now.indexOf(weatherType);

  int indexLater = later.indexOf(weatherType);

  //for all types of weather except for clear skies, if the current weather does not contain the weather type and the later message does, send notification

  if (weatherType != "clear") {

    if (indexNow == -1 && indexLater != -1) {

      Serial.println("Oh no! It is going to " + weatherType + " later! Predicted " + later);

      for (int thisNote = 0; thisNote < 4; thisNote++) {

        int noteDuration = 1000 / noteDurations[thisNote];

        tone(8, negMelody[thisNote], noteDuration);      //play negative melody through piezo

      }

    }

  }

  //for clear skies, if the current weather does not contain the word clear and the later message does, send notification that it will be sunny later

  else {

    if (indexNow == -1 && indexLater != -1) {

      Serial.println("It is going to be sunny later! Predicted " + later);

      for (int thisNote = 0; thisNote < 4; thisNote++) {

        int noteDuration = 1000 / noteDurations[thisNote];

        tone(8, posMelody[thisNote], noteDuration);      //play positive melody through piezo

      }

    }

  }
}
```

The full sketch can be seen below:

```arduino
/*

Weather Audio Notifier

Hardware Required:

* Arduino Zero Board

* Arduino WIFI Shield 101


* Piezo

Software Required:

* ArduinoJson Library

 created Sept 2015

 by Helena Bisby <support@arduino.cc>

This example code is in the public domain

http://arduino.cc/en/Tutorial/WeatherAudioNotifier



*/

#include <SPI.h>
#include <WiFi101.h>
#include <ArduinoJson.h>

#define JSON_BUFF_DIMENSION 2500
#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

String nameOfCity = "Turin,IT";   // your city of interest here in format "city,countrycode"

String text;
int endResponse = 0;
boolean startJson = false;
int posMelody[] = {330, 415, 494, 659};  //E3,G#3,B3,E4
int negMelody[] = {392, 370, 349, 330};  //G3,F#3,F3,E3
int noteDurations[] = {4, 4, 4, 8};      //Will correspond to note lengths 8th,8th,8th,4th
int status = WL_IDLE_STATUS;

const char server[] = "api.openweathermap.org";    // name address for openweathermap (using DNS)

WiFiClient client;
unsigned long lastConnectionTime = 10 * 60 * 1000;     // last time you connected to the server, in milliseconds

const unsigned long postingInterval = 10 * 60 * 1000;  // posting interval of 10 minutes  (10L * 1000L; 10 seconds delay for testing)

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  text.reserve(JSON_BUFF_DIMENSION);

  // check for the presence of the shield:

  if (WiFi.status() == WL_NO_SHIELD) {

    Serial.println("WiFi shield not present");

    // don't continue:

    while (true);

  }

  // attempt to connect to Wifi network:

  while ( status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  // you're connected now, so print out the status:

  printWifiStatus();
}

void loop() {

  // if ten minutes have passed since your last connection,

  // then connect again and send data:

  if (millis() - lastConnectionTime > postingInterval) {

    // note the time that the connection was made:

    lastConnectionTime = millis();

    httpRequest();

  }

  char c = 0;

  if (client.available()) {

    c = client.read();

    // json contains equal number of open and close curly brackets, therefore by counting

    // the open and close occurrences, we can determine when a json is completely received



    // endResponse == 0 means equal number of open and close curly brackets reached

    if (endResponse == 0 && startJson == true) {

      parseJson(text.c_str());  // parse c string text in parseJson function

      text = "";                // clear text string for the next time

      startJson = false;        // set startJson to false to indicate that a new message has not yet started

    }

    if (c == '{') {

      startJson = true;         // set startJson true to indicate json message has started

      endResponse++;

    }

    if (c == '}') {

      endResponse--;

    }

    if (startJson == true) {

      text += c;

    }

  }
}
void parseJson(const char * jsonString) {

  StaticJsonBuffer<4000> jsonBuffer;

  // FIND FIELDS IN JSON TREE

  JsonObject& root = jsonBuffer.parseObject(jsonString);

  if (!root.success()) {

    Serial.println("parseObject() failed");

    return;

  }

  JsonArray& list = root["list"];

  JsonObject& now = list[0];

  JsonObject& later = list[1];

  String city = root["city"]["name"];

  float tempNow = now["main"]["temp"];

  float humidityNow = now["main"]["humidity"];

  String weatherNow = now["weather"][0]["description"];

  float tempLater = later["main"]["temp"];

  float humidityLater = later["main"]["humidity"];

  String weatherLater = later["weather"][0]["description"];

  printDiffFloat(tempNow, tempLater, "temperature", "*C");

  printDiffString(weatherNow, weatherLater, "rain");

  printDiffString(weatherNow, weatherLater, "snow");

  printDiffString(weatherNow, weatherLater, "hail");

  printDiffString(weatherNow, weatherLater, "clear");

  printDiffFloat(humidityNow, humidityLater, "humidity", "%");

  Serial.println();

}

// this method makes a HTTP connection to the server:
void httpRequest() {

  // close any connection before send a new request.

  // This will free the socket on the WiFi shield

  client.stop();

  // if there's a successful connection:

  if (client.connect(server, 80)) {

    // Serial.println("connecting...");

    // send the HTTP PUT request:

    client.println("GET /data/2.5/forecast?q=" + nameOfCity + "&mode=json&units=metric&cnt=2 HTTP/1.1");

    client.println("Host: api.openweathermap.org");

    client.println("User-Agent: ArduinoWiFi/1.1");

    client.println("Connection: close");

    client.println();

  }

  else {

    // if you couldn't make a connection:

    Serial.println("connection failed");

  }
}

void printDiffString(String now, String later, String weatherType) {

  int indexNow = now.indexOf(weatherType);

  int indexLater = later.indexOf(weatherType);

  // for all types of weather except for clear skies, if the current weather does not contain the weather type and the later message does, send notification

  if (weatherType != "clear") {

    if (indexNow == -1 && indexLater != -1) {

      Serial.println("Oh no! It is going to " + weatherType + " later! Predicted " + later);

      for (int thisNote = 0; thisNote < 4; thisNote++) {

        int noteDuration = 1000 / noteDurations[thisNote];

        tone(8, negMelody[thisNote], noteDuration);      // play negative melody through piezo

      }

    }

  }

  // for clear skies, if the current weather does not contain the word clear and the later message does, send notification that it will be sunny later

  else {

    if (indexNow == -1 && indexLater != -1) {

      Serial.println("It is going to be sunny later! Predicted " + later);

      for (int thisNote = 0; thisNote < 4; thisNote++) {

        int noteDuration = 1000 / noteDurations[thisNote];

        tone(8, posMelody[thisNote], noteDuration);      // play positive melody through piezo

      }

    }

  }
}

void printDiffFloat(float now, float later, String parameter, String unit) {

  String change;

  if (now > later) {

    change = "drop from ";

  }

  else if (now < later) {

    change = "rise from ";

  }

  else {

    return;

  }

  Serial.print("UPDATE: The " + parameter + " will " + change);

  Serial.print(now);

  Serial.print(unit + " to ");

  Serial.print(later);

  Serial.println(unit + "!");
}

void printWifiStatus() {

  // print the SSID of the network you're attached to:

  Serial.print("SSID: ");

  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:

  IPAddress ip = WiFi.localIP();

  Serial.print("IP Address: ");

  Serial.println(ip);

  // print the received signal strength:

  long rssi = WiFi.RSSI();

  Serial.print("signal strength (RSSI):");

  Serial.print(rssi);

  Serial.println(" dBm");
}
```



## Testing It Out

After you have uploaded the code, if there is a change in weather conditions of the selected city of interest defined in `String nameOfCity = "cityname,countrycode"`; an update of the changes is written to the serial monitor and the piezo will generate an audio notification depending on the result of the weather change.



### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- You have not installed the ArduinoJson library.
- You have entered the incorrect `ssid` or `pass` of your network.

## Conclusion

In this example, we have learned how to create a weather notification project that notifies you when weather conditions change! All of this is possible because of Json and the ArduinoJson library. Now that you have finished this tutorial, you can start to use Json for other cool applications and projects.