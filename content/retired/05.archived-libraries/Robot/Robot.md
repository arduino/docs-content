---
title: 'Robot Library'
description: 'The library allows you to interface with the various sensors and peripherals on the control board.'
author: Arduino
---

***This library is archived and is no longer being maintained. It can be still be downloaded and used, but is read-only and cannot be contributed to. Furthermore, the Robot Library now exists as three separate libraries: [Robot_Control](https://github.com/arduino-libraries/Robot_Control), [Robot_Motor](https://github.com/arduino-libraries/Robot_Motor) and [RobotIRremote](https://github.com/arduino-libraries/RobotIRremote).***


The Robot library is included with Arduino IDE 1.0.5 and later.

The Robot has a number of built in sensors and actuators. The library is designed to easily access the robot's functionality.

The robot has two boards, a motor board and control board. Each board has a separate programmable processor.

The library allows you to interface with the various sensors and peripherals on the control board :

- potentiometer
- 5 momentary switches
- 160x120 pixel color screen
- 512Kbit EEPROM
- speaker
- compass
- 3 I2C connectors
- 8 TinkerKit input connectors

The library also enables you to do a number of things with the motor board :

- control motor speed and direction
- sense the current used by each motor
- read the state of the 5 floor sensors (also known as line detection sensors)
- access I/O pins on the board
- control an I2C port
- read the state of 4 TinkerKit inputs

For more information about the Robot, visit the getting started guide and the hardware page.

## Library structure

This library enables easy access to the functionality of the Arduino Robot. It relies on a number of 3rd party libraries including Fat16, [EasyTransfer](https://github.com/madsci1016/Arduino-EasyTransfer), [Squawk](https://github.com/stg/Squawk), and [IRRemote](https://github.com/Arduino-IRremote/Arduino-IRremote). It also relies on a number of Arduino libraries like [TFT](https://www.arduino.cc/en/Reference/TFTLibrary), [SPI](https://www.arduino.cc/en/Reference/SPI), and [Wire](https://www.arduino.cc/en/reference/wire). Their functionality has been replicated inside the robot's library to optimize the code's size.

It is possible to program both the Control and the Motor boards. However, it is recommended that novice programmers begin with programming the control board, leaving the motor board for later. The library exposes the sensors on both boards through a single object.

There are two main classes that command the robot:

- RobotControl: commands the Control Board as well as the I/Os and motors on the Motor Board, when running the default firmware.
- RobotMotor: commands the Motor Board. Use it to make your own custom version of the Motor Board firmware


## Examples

You can find examples for this library in the [Examples from Libraries](https://docs.arduino.cc/retired/#library-example) page. 

## RobotControl Class

---

### `RobotControl`

#### Description

The constructor is empty. As the methods can be accessed through the Robot object directly, you don't need to call the constructor.


#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>
void setup(){
  //methods can be accessed directly through Robot
  Robot.begin();
  Robot.motorsWrite(255,255);
}
void loop(){
}
```

---

### `begin()`

#### Description

Initializes the robot. Must be called in setup() to use Robot-specific features.

Robot.begin() does not initialize features like sound, the LCD module, or the SD card. Refer to the links in the "See also" section for reference on initializing these other modules.

#### Syntax

```
Robot.begin()

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>
void setup(){
  Robot.begin();
  //do stuff here
}
void loop(){
  //do stuff here
}
```

---

### `setMode()`

#### Description

Change the robot's mode. Depending on the mode it is currently in, the commands may change.

#### Syntax

```
Robot.setMode(modeName)

```

#### Parameters
- modeName: Name of the mode you want to set the robot into.
- MODE_SIMPLE : the robot will accept all commands.
- MODE_LINE_FOLLOW : the robot will start line-following, and stop responding to motor commands

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>
void setup(){
  Robot.begin();
  Robot.setMode(MODE_LINE_FOLLOW);
}
void loop(){

}
```

---

### `pauseMode()`

#### Description

Pause or resume the mode-specific action for the bottom board.

For line-following mode, the robot will stop following the line, but still receiving commands.

#### Syntax

```
Robot.pauseMode(onOff)

```

#### Parameters
onOff: boolean. true pauses the mode, false resumes it.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>
long timer;

void setup(){
  Robot.begin();
  Robot.beginLCD();
  delay(3000);

  Robot.setMode(MODE_LINE_FOLLOW);
  timer=millis();
  while(!Robot.isActionDone()){
    //pauses line-following for 3 seconds every 5 seconds
    if(millis()-timer>=5000){
      Robot.pauseMode(true);
      delay(3000);
      Robot.pauseMode(false);
      timer=millis();
    }
    Robot.debugPrint(millis());
  }
  Robot.text("Done!",0,10,true);
  while(true);

}
void loop(){
}
```

---

### `isActionDone()`

#### Description

Checks if the current motor board mode action is finished.

Line-following mode will report an action completed signal when it reaches a finishing line (a perpendicular line).

#### Syntax

```
Robot.isActionDone()

```

#### Parameters
none

#### Returns
boolean

#### Examples

```
#include <ArduinoRobot.h>
long timer;

void setup(){
  Robot.begin();
  Robot.beginLCD();
  delay(3000);

  Robot.setMode(MODE_LINE_FOLLOW);
  timer=millis();
  while(!Robot.isActionDone()){
    //pauses line-following for 3 seconds every 5 seconds
    if(millis()-timer>=5000){
      Robot.pauseMode(true);
      delay(3000);
      Robot.pauseMode(false);
      timer=millis();
    }
    Robot.debugPrint(millis());
  }
  Robot.text("Done!",0,10,true);
  while(true);

}
void loop(){
}
```

---

### `lineFollowConfig()`

#### Description

Change the parameters for line following.

Use this function if line-following is not working as expected, or you want to change the robot's speed while line-following.

This function changes the "PD algorithms" that enable to robot to think about what may happen next while line reading. The robot attempts to predict any possible errors on the next reading of the IR sensors, and corrects its movement accordingly by changing the speed of each wheel separately.

See the note below for a deeper explanation.

#### Syntax

```
Robot.lineFollowConfig(KP,KD,robotSpeed,intergrationTime)

```

#### Parameters
- KP : int, proportional gain
- KD : int, derivative gain
- integrationTime: int, delay time between each time we run the algorithm in ms
- robotSpeed: int, between 0 and 100, indicating the percentage speed of motors.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>
long timer;

void setup(){
  Robot.begin();
  Robot.beginLCD();
  delay(3000);

  Robot.lineFollowConfig(11,5,50,10);//set PID
  Robot.setMode(MODE_LINE_FOLLOW);
  timer=millis();
  while(!Robot.isActionDone()){
    //pauses line-following for 3 seconds every 5 seconds
    if(millis()-timer>=5000){
      Robot.pauseMode(true);
      delay(3000);
      Robot.pauseMode(false);
      timer=millis();
    }
    Robot.debugPrint(millis());
  }
  Robot.text("Done!",0,10,true);
  while(true);

}
void loop(){
}
```

---

### `digitalRead()`

#### Description

Reads the digital value one the defined port. These are exposed as TinkerKit connectors on the robot. See the diagrams below for pin locations

#### Syntax

```
Robot.digitalRead(portName)

```

#### Parameters
port: Valid names are TK0 to TK7 (found on the Control board), TKD0 to TKD5 (on the Control board), and B_TK1 to B_TK4 (on the Motor Board).

#### Returns
HIGH or LOW

#### Examples

```
#include <ArduinoRobot.h>
void setup(){
  Robot.begin();
  Serial.begin(9600);

}
void loop(){
  Serial.println(Robot.digitalRead(TK0)); //Print the value read on port TK0
  delay(100);
}
```

---

### `digitalWrite()`

#### Description

Write a HIGH or a LOW value to the defined port on the robot. the ports are exposed on the robot as TinkerKit connectors.

#### Syntax

```
Robot.digitalWrite(port, value)

```

#### Parameters
port: TKD0 to TKD5 (on the Control board), B_TK1 to B_TK4(on the Motor Board), or LED1 (located on the control board)

value: HIGH or LOW

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>
void setup(){
  Robot.begin();
}

void loop(){
  Robot.digitalWrite(TDK0, HIGH); // Turn on a Tinkerkit LED connected to TDK0
  delay(1000);
  Robot.digitalWrite(TK0, LOW); // Turn the LED off
  delay(1000);
}
```

#### Note
You cannot call Robot.digitalWrite() on TK0 to TK7

---

### `analogRead()`

#### Description

Reads the value from the specified port on the robot. The ports are exposed on the robot as TinkerKit connectors.

The board has a 10-bit analog to digital converter. This means that it will map input voltages between 0 and 5 volts into integer values between 0 and 1023.

#### Syntax

```
Robot.analogRead(port)
```

#### Parameters
port: TK0 to TK7 (found on the Control Board), TKD0 to TKD5 (found on the Control Board), or B_TK1 to B_TK4 (found on the motor Board)

#### Returns
int : 0 to 1023

#### Note
If the input port is not connected to anything, the value returned by Robot.analogRead() will fluctuate based on a number of factors (e.g. the values of the other analog inputs, how close your hand is to the board, etc.).

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Serial.begin(9600);
}

void loop(){
  Serial.println(Robot.analogRead(TK0)); //Print the value on port TK0
  delay(100);
}
```

---

### `analogWrite()`

#### Description

Writes an analog value as PWM to the specified port on the robot. The board has a 8-bit PWM, allowing for 256 discrete levels.

Robot.analogWrite() only works on TKD4, located on the Control Board. It cannot be used at the same time as TK0 through TK7.

#### Syntax

```
Robot.analogWrite(port, value)

```

#### Parameters
port: TKD4

value : 0 to 255

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Serial.begin(9600);
}

void loop(){
  for(int x=0;x<256;x++){
  Robot.analogWrite(TKD4, x); //increase brightness of an LED on TK0
  delay(20);
  }
}
```

---

### `updateIR()`

#### Description

Reads the values of the 5 IR line-reading sensors on the underside of the robot and stores the values in an array. This array can be accessed through Robot.IRarray[]. This function needs to be called from the Control Board.

To obtain the reading from a specific IR sensor, use IRRead() on the Motor Board.


#### Parameters
none

#### Returns
Robot.IRarray[] : contains the values of the 5 sensors

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Serial.begin(9600);
}

void loop(){
  Robot.updateIR(); // update the IR array
  for(int i=0;i<=4;i++){
    Serial.print(Robot.IRarray[i]); // print the values to the serial port
    Serial.print(",");
  }
  Serial.println("");
  delay(100);
}
```

---

### `knobRead()`

#### Description

Gets the analog value as a 10-bit value from the on-board potentiometer. This means that it will map input voltages between 0 and 5 volts into integer values between 0 and 1023.

#### Syntax

```
Robot.knobRead()

```

#### Parameters
none

#### Returns
int: 0 to 1023

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Serial.begin(9600);

}
void loop(){
  Serial.println(Robot.knobRead());
  delay(100);
}
```

---

### `compassRead()`

#### Description

Get the current direction from on-board compass. The values are degrees of rotation from north (in a clockwise direction), so that east is 90, south is 180, and west is 270.

#### Syntax

```
Robot.compassRead()

```

#### Parameters
none

#### Returns
int: 0 to 359, representing the number of degrees of rotation from north.

#### Note
The compass module may be disrupted by magnetic fields in surrounding areas.

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Serial.begin(9600);

}
void loop(){
  Serial.println(Robot.compassRead());
  delay(100);
}
```

---

### `keyboardRead()`

#### Description

Detects if one of the 5 momentary buttons on the control board is pressed.

#### Syntax

```
Robot.keyboardRead()

```

#### Parameters
none

#### Returns
- BUTTON_NONE if no key is pressed
- BUTTON_LEFT if left key is pressed
- BUTTON_DOWN if down key is pressed
- BUTTON_UP if up key is pressed
- BUTTON_RIGHT if right key is pressed
- BUTTON_MIDDLE if middle key is pressed

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Serial.begin(9600);
}

void loop(){
  Serial.println(Robot.keyboardRead());
  delay(100);
}
```

---

### `waitContinue()`

#### Description

Pauses the current program and waits for a key press from one of the 5 momentary buttons. Once you press the key, the program continues.

#### Syntax

```
Robot.waitContinue()
Robot.waitContinue(key)
```

#### Parameters
key: the momentary switch to listen for. The default value is BUTTON_MIDDLE. Valid choices are

- BUTTON_LEFT
- BUTTON_RIGHT
- BUTTON_MIDDLE
- BUTTON_UP
- BUTTON_DOWN

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.waitContinue();//stop the robot, and wait for the middle button to be pressed
}

void loop(){
  Robot.motorsWrite(255,255);
  delay(2000);
  Robot.motorsWrite(0,0);
  delay(2000);
}
```

---

### `motorsWrite()`

#### Description

Controls the speed and direction of the two motors connected to the robot's wheels. motorsWrite() needs values between -255 and 255. If the value is greater than 0, the wheel turns forward. If less than 0, the motor turns backwards.

#### Syntax

```
Robot.motorsWrite(speedLeft, speedRight)

```

#### Parameters
- speedLeft: the speed of left wheel
- speedRight: the speed of right wheel

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
}
void loop(){
  Robot.motorsWrite(255,255); //Make the robot go forward, full speed
  delay(1000);
  Robot.motorsWrite(0,0); //Make the robot stop
  delay(1000);
  Robot.motorsWrite(255,-255);//Make the robot rotate right, full speed
  delay(1000);
  Robot.motorsWrite(0,0); //Make the robot stop
  delay(1000);
}
```

---

### `motorsStop()`

#### Description

Stop both motors of the robot.

#### Syntax

```
Robot.motorsStop()

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
}
void loop(){
  Robot.motorsWrite(255,255); //Make the robot go forward, full speed
  delay(1000);
  Robot.motorsStop(); //Fast stop the robot
  delay(1000);
  Robot.motorsWrite(255,-255);//Make the robot rotate right, full speed
  delay(1000);
  Robot.motorsWrite(0,0); //Slow stop the robot
  delay(1000);
}
```

#### Note
You can as well stop the motors by calling Robot.motorsWrite(0,0). Difference is, after the later is called, the motors may still move a little due to momentum(so called slow stop). Robot.motorsStop() will stop the motors and make them stiff, so stop instantly.

---

### `turn()`

#### Description

Make the robot turn a certain number of degrees from its current orientation. The current position is derived from the onboard compass.

#### Syntax

```
Robot.turn(degrees)

```

#### Parameters
degrees:-180 to 180. Positive number for turning right, negative number for turning left.

#### Returns
none

#### Note
Magnetic objects in the surrounding may disrupt the compass module. Keep magnets, such as strong speakers, away from the robot.

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
}
void loop(){
  Robot.turn(90); //Make the robot turn 90 degrees right
  delay(1000);
}
```

---

### `pointTo()`

#### Description

Make the robot point in a particular direction. pointTo() makes the robot face an absolute direction based on the compass.

#### Syntax

```
Robot.pointTo(degrees)

```

#### Parameters
degrees:0 to 359.

#### Returns
none

#### Note
Magnetic objects in the surrounding may disrupt the compass module. Keep magnets, such as strong speakers, away from the robot.

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.pointTo(90); //The robot will turn to 90, by the value of compass
}
void loop(){
}
```

---

### `beginSpeaker()`

#### Description

Initializes the speaker and sound libraries. Must be included in setup().

#### Syntax

```
Robot.beginSpeaker()

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginSpeaker();//Initialize the sound module
}

void loop(){
  char aTinyMelody[] = "8eF-FFga4b.a.g.F.8beee-d2e.1-";// This is what we will play
  Robot.playMelody(aTinyMelody);// Play the melody

}
```

---

### `playMelody()`

#### Description

Plays a melody according to a string of music notes. The input string also contains information about note duration, as well as silences. Must be preceded by Robot.beginSpeaker() in setup().

NB : when a melody is playing, all other processes stop

#### Syntax

```
Robot.playMelody(melody)

```

#### Parameters
melody: A string of notes to be played and their duration.

The string may contain following chars:
Notes

- `c` : play "C"
- `C` : play "#C"
- `d` : play "D"
- `D` : play "#D"
- `e` : play "E"
- `f` : play "F"
- `F` : play "#F"
- `g` : play "G"
- `G` : play "#G"
- `a` : play "A"
- `A` : play "#A"
- `b` : play "B"
- `-` : silence

#### Duration

- `1` : Set the following as full notes
- `2` : Set the following as half notes
- `4` : Set the following as quarter notes
- `8` : Set the following as eight notes
- `.` : Set the note duration as its duration plus an half of its duration (Example 1/4 + 1/8)

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginSpeaker();//Initialize the sound module
}

void loop(){
  char aTinyMelody[] = "8eF-FFga4b.a.g.F.8beee-d2e.1-";// This is what we will play
  Robot.playMelody(aTinyMelody);// Play the melody

}
```

---

### `beep()`

#### Description

Make a short beeping sound. Must be preceded by Robot.beginSpeaker() in setup().

NB : when a beep is playing, all other processes stop

#### Syntax

```
Robot.beep(beep_length)

```

#### Parameters
beep_length: Any of the const below indicating type of beep sound.

- BEEP_SIMPLE: a short beep
- BEEP_DOUBLE: double beep
- BEEP_LONG: a longer beep

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginSpeaker();//Initialize the sound module
}

void loop(){
  Robot.beep(BEEP_SIMPLE);//Make a single beep sound
  delay(1000);
}
```

---

### `playFile()`

#### Description

Play a .sqm music file stored on a SD card. Robot.beginSpeaker() and Robot.beginSD() are both required in setup().

Unlike Robot.playMelody() and Robot.playBeep(), playFile() does not halt other processes while playing. However, you cannot load new images on the LCD screen when playFile() is in use.

Valid files for playback are generated/converted by the sound library Squawk. See the library README for details on how to create your own music.

#### Syntax

```
Robot.playFile(filename)

```

#### Parameters
filename: file name of the music to be played

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginSpeaker();//Initialize the sound module
  Robot.beginSD();//Initialize the sd card
  Robot.playFile("melody.sqm");//Play the original music come with the robot.
}

void loop(){
  //do other stuff here
}
```

---

### `tuneWrite()`

#### Description

When playing a music file through playFile(), this will change the pitch of the sound. The larger the value, the higher the pitch.

#### Syntax

```
Robot.tuneWrite(pitch)

```

#### Parameters
pitch: float, indicating the pitch of the sound currently playing. 1.0 is the baseline value.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginSpeaker();//Initialize the sound module
  Robot.beginSD();//Initialize the sd card
  Robot.playFile("melody.sqm");//Play the original music come with the robot.
  Robot.tuneWrite(1.4);//40% higher than default
}

void loop(){

}
```

---

### `tempoWrite()`

#### Description

When playing a music file with playFile(), this will change the tempo, or speed of the playback. The larger the value, the quicker the sound will play back. Smaller values will slow the playback.

#### Syntax

```
Robot.tempoWrite(speed)

```

#### Parameters
speed: int, the tempo. Default is 50.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginSpeaker();//Initialize the sound module
  Robot.beginSD();//Initialize the sd card
  Robot.playFile("melody.sqm");//Play the original music come with the robot.
  Robot.tempoWrite(70);//20 higher than default
}

void loop(){

}
```

---

### `beginTFT()`

#### Description

Initialize the TFT module. All general TFT functions are dependent on this.

#### Syntax

```
Robot.beginTFT()
Robot.beginTFT(foreGround, backGround)
```

#### Parameters
foreGround: set a universal foreground color. Default is black.
backGround: set a universal background color. Default is white.
#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginTFT();//Initialize the TFT module
}

void loop(){
  Robot.fill(255,255,255);
  Robot.text("Hello World",0,0);
  delay(2000);

  Robot.fill(0,0,0);
  Robot.text("Hello World",0,0,false);//It's necessary to erase the old text, before showing new text

  Robot.fill(255,255,255);
  Robot.text("I am a robot",0,0);
  delay(3000);

  Robot.fill(0,0,0);
  Robot.text("I am a robot",0,0);
}
```

---

### `text()`

#### Description

Write some text to an attached TFT.

When updating the screen, remember to erase the text before writing new text on the same place, or the new/old text will be overlapping each other.

The screen is only 128 pixels tall and 160 pixels wide. It's recommended to use small values for x and y, or text may be cropped/invisible in unpredictable ways.

#### Syntax

```
Robot.text(toWrite, x, y, writeOrErase)

```

#### Parameters
toWrite: text/value to be written on the LCD. Can be a string, an int or a long.

x: x axis of starting position on the screen.

y: y axis of starting position on the screen.

writeOrErase: specify whether to write the text or erase the text. Use true to write and false to erase.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginTFT();//Initialize the TFT module
}

void loop(){
  Robot.text("Hello World",0,0,true);
  delay(2000);

  Robot.text("Hello World",0,0,false);//It's necessary to erase the old text, for showing new text
  Robot.text("I am a robot",0,0,true);
  delay(3000);

  Robot.text("I am a robot",0,0,false);
}
```

---

### `beginBMPFromEEPROM()`

#### Description
After beginBMPFromEEPROM() is called, drawBMP() will look for images from the EEPROM, until endBMPFromEEPROM() is called.

Images stored in EEPROM are accessed more slowly than from an SD card.

If drawBMP() cannot find images from EEPROM with the given file name, no image will be rendered on screen, even if a bmp with the same file name is stored on a SD card.

Call endBMPFromEEPROM() after drawBMP() if you want to get images from a SD card afterwards.

#### Syntax

```
Robot.beginBMPFromEEPROM()
```

#### Parameters
none

#### Returns
none

#### Example

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
  Robot.readyLCD();

  //The image is pulled from EEPROM
  Robot.beginBMPFromEEPROM();
  Robot.drawBMP("inicio.bmp",0,0);
  Robot.endBMPFromEEPROM();

}
void loop(){
}
```

---

### `endBMPFromEEPROM()`

#### Description
Stops drawBMP() from pulling images in EEPROM. Used in conjunction with beginBMPFromEEPROM().

#### Syntax
```
Robot.endBMPFromEEPROM()
```

#### Parameters
none

#### Returns
none

#### Example

```
#include <ArduinoRobot.h>
void setup(){
  Serial.begin(9600);
  Robot.begin();
  Robot.readyLCD();

  //The image is pulled from EEPROM
  Robot.beginBMPFromEEPROM();
  Robot.drawBMP("inicio.bmp",0,0);
  Robot.endBMPFromEEPROM();

}

void loop(){
}
```

---

### `drawDire(direction)`

#### Description
A helper function for drawing a compass on the LCD screen

#### Parameters
direction: an int between 0 and 359, indicating where the compass should be pointing at. Typically it's one get from Robot.compassRead().

#### Returns
none

#### Example

```
#include <ArduinoRobot.h>
void setup(){
  Robot.begin();
  Robot.readyLCD();//Initialize the LCD module
}
void loop(){
  int dire=Robot.compassRead();
  Robot.drawDire(dire);
}
```

---

### `drawBMP()`

#### Description

Display a bmp file on the LCD screen. The bmp file should be stored in sd card. BMP format should be 24-bit color, and no bigger than 128*160. If an image dimensions exceed the size of the screen, it will be cropped.

To use this method, you must initialize the SD card by calling Robot.beginSD() in setup().

#### Syntax

```
Robot.drawBMP(filename, x, y)

```

#### Parameters
filename: name of the bmp file to be displayed.
x: x-axis of starting position on the screen.
y: y-axis of starting position on the screen.
#### Returns
none

#### Examples

```
// Draws an image named "intro.bmp" from the SD card

#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.readyTFT();
  Robot.beginSD();

  //The image is pulled from sd card
  Robot.drawBMP("intro.bmp",0,0);
}

void loop(){
  // nothing happening here
}
```

---

### `debugPrint()`

#### Description

Print and refresh a value to the LCD screen. You need to first initialize the LCD screen in setup() by calling Robot.readyLCD(). If no starting point is defined, text defaults to starting at 0,0, the top left of the screen.

#### Syntax

```
Robot.debugPrint(toPrint)
Robot.debugPrint(toPrint, x, y)
```

#### Parameters
toPrint: value to be printed. Must be int or long.
x: x axis of starting position on the screen.
y: y axis of starting position on the screen.
#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.readyTFT();//Initialize the TFT module
}

void loop(){
  int val=Robot.analogRead(TK0); //Get analog value from port TK0 on top board.
  Robot.debugPrint(val); //No need to erase the old value
  delay(100);
}
```

---

### `clearScreen()`

#### Description

Fill the entire screen with the background color. Default is black.

#### Syntax

```
Robot.clearScreen();

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginTFT();//Initialize the TFT module
}

void loop(){
  Robot.text("Hello World",0,0,true);
  delay(2000);

  Robot.clearScreen();//empty the screen
  delay(2000);
}
```

---

### `displayLogos()`

#### Description

A helper function for displaying an opening sequence in some of the examples.

displayLogos() draws "lg0.bmp" and "lg1.bmp" from an attached SD card to the screen, with 2 seconds of delay between the first and second image. There is a 2 second delay after "lg1.bmp", for a total of 4 seconds.

You need to initialize both the LCD and SD card, and have "lg0.bmp" and "lg1.bmp" on the card (they are installed by default).

#### Syntax

```
Robot.displayLogos();

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.beginTFT();//Initialize the TFT module
  Robot.displayLogos();//Show the opening sequence
}

void loop(){
  Robot.text("Hello World",0,0,true);
  delay(2000);

  Robot.text("Hello World",0,0,false);//It's necessary to erase the old text, for showing new text
  Robot.text("I am a robot",0,0,true);
  delay(3000);

  Robot.text("I am a robot",0,0,false);
}
```

---

### `drawCompass()`

#### Description

A helper function for displaying the compass on the TFT. Relies on Robot.beginTFT(). drawCompass() uses debugPrint(), which can't be used in the same sketch.

Mind where you draw text and other graphic elements when using drawCompass() so that you don;t overlap elements.

#### Syntax

```
Robot.drawCompass(degrees);

```

#### Parameters
degrees: int between 0 and 359. Typically it's determined by Robot.compassRead().

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

int compassValue;

void setup(){
  Robot.begin();
  Robot.beginTFT();//Initialize the TFT module
}

void loop(){
  compassValue=Robot.compassRead();
  Robot.drawCompass(compassValue);//draw the compass
}
```

---

### `beginSD()`

#### Description

Initialize the SD card for use. Functions that read data from a SD card like drawBMP() and playFile() are dependent on this.

NB : This function uses a lot of memory, and may leads to undefined results if used in a complex sketch. It's recommended to not use this unless you are using the SD card.

#### Syntax

```
Robot.beginSD()

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Robot.readyTFT();
  Robot.beginSD();//Initialize the sd card

  Robot.drawBMP("inicio.bmp",0,0);//draw an image from the sd card

}

void loop(){
}
```

---

### `userNameRead()`

#### Description

Read the name stored in EEPROM. The name is set by userNameWrite(). EEPROM is not erased when the robot is turned off and can be read anytime after being set.

#### Syntax

```
Robot.userNameRead(container)

```

#### Parameters
container: a char array with 8 elements.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
}

void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  char container[8];
  Robot.userNameRead(container)
  Serial.println(container);

  Robot.robotNameRead(container)
  Serial.println(container);

  Robot.cityNameRead(container)
  Serial.println(container);

  Robot.countryNameRead(container)
  Serial.println(container);
}
```

---

### `userNameWrite()`

#### Description

Store your name into EEPROM. EEPROM is always saved, even when the power is switched off.

#### Syntax

```
Robot.userNameWrite(name)

```

#### Parameters
name: string to be stored

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
}

void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  Serial.println(Robot.userNameRead());
  Serial.println(Robot.robotNameRead());
  Serial.println(Robot.cityNameRead());
  Serial.println(Robot.countryNameRead());
}
```

---

### `RobotNameRead()`

#### Description

Read the robot name stored in EEPROM. This can be set by robotNameWrite().

#### Syntax

```
Robot.RobotNameRead(container)

```

#### Parameters
container: a char array with 8 elements.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
}

void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  char container[8];
  Robot.userNameRead(container)
  Serial.println(container);

  Robot.robotNameRead(container)
  Serial.println(container);

  Robot.cityNameRead(container)
  Serial.println(container);

  Robot.countryNameRead(container)
  Serial.println(container);
}
```

---

### `robotNameWrite()`

#### Description

Store the robot's name into EEPROM.

#### Syntax

```
Robot.robotNameWrite(name)

```

#### Parameters
name: string to be stored

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
}

void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  Serial.println(Robot.userNameRead());
  Serial.println(Robot.robotNameRead());
  Serial.println(Robot.cityNameRead());
  Serial.println(Robot.countryNameRead());
}
```

---

### `cityNameRead()`

#### Description

Read your city's name stored in EEPROM. This can be set by cityNameWrite().

#### Syntax

```
Robot.cityNameRead(container)

```

#### Parameters
container: a char array with 8 elements.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
}

void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  char container[8];
  Robot.userNameRead(container)
  Serial.println(container);

  Robot.robotNameRead(container)
  Serial.println(container);

  Robot.cityNameRead(container)
  Serial.println(container);

  Robot.countryNameRead(container)
  Serial.println(container);
}
```

---

### `cityNameWrite()`

#### Description

Store your city's name into EEPROM.

#### Syntax

```
Robot.cityNameWrite(name)

```

#### Parameters
name: string to be stored

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
}

void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  Serial.println(Robot.userNameRead());
  Serial.println(Robot.robotNameRead());
  Serial.println(Robot.cityNameRead());
  Serial.println(Robot.countryNameRead());
}
```

---

### `countryNameRead()`

#### Description

Read your country's name stored in EEPROM. This is set by userNameWrite().

#### Syntax

```
Robot.countryNameRead(container)

```

#### Parameters
container: a char array of 8 elements.

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>

void setup(){
  Serial.begin(9600);
  Robot.begin();
}

void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  char container[8];
  Robot.userNameRead(container)
  Serial.println(container);

  Robot.robotNameRead(container)
  Serial.println(container);

  Robot.cityNameRead(container)
  Serial.println(container);

  Robot.countryNameRead(container)
  Serial.println(container);
}
```

---

### `countryNameWrite()`

#### Description

Store the user's country name into EEPROM.

#### Syntax

```
Robot.countryNameWrite(name)

```

#### Parameters
name: string to be stored

#### Returns
none

#### Examples

```
#include <ArduinoRobot.h>
void setup(){
  Serial.begin(9600);
  Robot.begin();
}
void loop(){
  Robot.userNameWrite("Aaa");
  Robot.robotNameWrite("The Robot");
  Robot.cityNameWrite("Malmo");
  Robot.countryNameWrite("Sweden");

  Serial.println(Robot.userNameRead());
  Serial.println(Robot.robotNameRead());
  Serial.println(Robot.cityNameRead());
  Serial.println(Robot.countryNameRead());
}
```

## RobotMotor Class

---

### `RobotMotorBoard()`

#### Description

The constructor is empty, as the methods can be accessed through Robot object directly, you don't need to call the constructor.

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobotMotorBoard.h>
void setup(){
  //methods can be accessed directly through RobotMotor
  RobotMotor.begin();
  RobotMotor.motorsWrite(255,255);
}
void loop(){
}
```

---

### `begin()`

#### Description

Initializes the robot motor board. Must be called in setup() to use Robot-specific features. This can only be called on the Motor Board processor.

#### Syntax

```
RobotMotor.begin()

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobotMotorBoard.h>

void setup(){
  RobotMotor.begin();
}

void loop(){
  //The robot motor board core routine
  RobotMotor.parseCommand();
  RobotMotor.process();
}
```

---

### `process()`

#### Description

Carry out different actions according to the mode Robot is in. It's part of Robot motor board's core routine. If you want to extend it, see this document.

This can only be called from the Motor Board processor.

#### Syntax

```
RobotMotor.process()

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobotMotorBoard.h>
void setup(){
  RobotMotor.begin();
}
void loop(){
  //The robot motor board core routine
  RobotMotor.parseCommand();
  RobotMotor.process();
}
```

---

### `parseCommand()`

#### Description

Receive commands from Robot Control Board, and carry them out accordingly. It's part of Robot motor board's core routine. If you want to extend it, see this document.

This can only be called from the Motor Board processor.

#### Syntax

```
RobotMotor.parseCommand()

```

#### Parameters
none

#### Returns
none

#### Examples

```
#include <ArduinoRobotMotorBoard.h>
void setup(){
  RobotMotor.begin();
}
void loop(){
  //The robot motor board core routine
  RobotMotor.parseCommand();
  RobotMotor.process();
}
```

---

### `motorsWrite()`

#### Description

Control the robot's wheels speed and direction from the Motor Board processor. It's different from motorsWrite() of the control board. This one drives the motors directly, while the former sends signals to the motor board. So don't mix them in usage.

#### Syntax

```
RobotMotor.motorsWrite(speedL, speedR)

```

#### Parameters
speedLeft: controls the speed of left wheel.

speedRight: controls the speed of right wheel.

Both values can be from -255 to 255. If the value is bigger than 0, the wheel turns forward. Smaller than 0, the motor turns backwards.

#### Returns
none

#### Examples

```
#include <ArduinoRobotMotorBoard.h>

void setup(){
  RobotMotor.begin();
}

void loop(){
  RobotMotor.motorsWrite(255,255);
  delay(1000);
  RobotMotor.motorsWrite(0,0);
  delay(1000);
}
```

---

### `IRread()`

#### Description

Get the reading from a specific IR sensor. This can only be called from the Motor Board processor. To read the IR sensors from the Control Board, use updateIR().

#### Syntax

```
RobotMotor.IRread(num)

```

#### Parameters
num: 1 to 5, corresponding to sensors 1 to 5.

#### Returns
int : 0 to 1023

#### Examples

```
#include <ArduinoRobotMotorBoard.h>
void setup(){
  Serial.begin(9600);
  RobotMotor.begin();
}
void loop(){
  Serial.println(RobotMotor.IRread(1));
  delay(10);
}
```
