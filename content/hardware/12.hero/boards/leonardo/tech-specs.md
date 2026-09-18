Here you will find the technical specifications for the Arduino Leonardo.

**Please note:** 

If the Mouse or Keyboard library is constantly running, it will be difficult to program your board. Functions such as Mouse.move() and Keyboard.print() will move your cursor or send keystrokes to a connected computer and should only be called when you are ready to handle them. 

It is recommended to use a control system to turn this functionality on, like a physical switch or only responding to specific input you can control. When using the Mouse or Keyboard library, it may be best to test your output first using Serial.print(). This way, you can be sure you know what values are being reported. Refer to the Mouse and Keyboard examples for some ways to handle this.
