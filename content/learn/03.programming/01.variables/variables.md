---
title: 'Using Variables in Sketches'
description: 'What are variables, and how can we use them in a sketch.'
tags: [Basics, Variables]
---


A variable is a place to store a piece of data.  It has a name, a value, and a type.  For example, this statement (called a *declaration*):

`int pin = 13;`

creates a variable whose name is `pin`, whose value is `13`, and whose type is `int`.  Later on in the program, you can refer to this variable by its name, at which point its value will be looked up and used.  For example, in this statement:

`pinMode(pin, OUTPUT);`

it is the value of pin (13) that will be passed to the pinMode() function.  In this case, you don't actually need to use a variable, this statement would work just as well:

`pinMode(13, OUTPUT);`

The advantage of a variable in this case is that you only need to specify the actual number of the pin once, but you can use it lots of times.  So if you later decide to change from pin 13 to pin 12, you only need to change one spot in the code.  Also, you can use a descriptive name to make the significance of the variable clear (e.g. a program controlling an RGB LED might have variables called redPin, greenPin, and bluePin).

A variable has other advantages over a value like a number.  Most importantly, you can change the value of a variable using an *assignment* (indicated by an equals sign).  For example:

`pin = 12;`

will change the value of the variable to 12.  Notice that we don't specify the type of the variable: it's not changed by the assignment.  That is, the name of the variable is permanently associated with a type; only its value changes. [1]   Note that you have to declare a variable before you can assign a value to it.  If you include the preceding statement in a program without the first statement above, you'll get a message like: "error: pin was not declared in this scope".

When you assign one variable to another, you're making a copy of its value and storing that copy in the location in memory associated with the other variable.  Changing one has no effect on the other.  For example, after:

```arduino
int pin = 13;
int pin2 = pin;
pin = 12;
```

only pin has the value 12; pin2 is still 13.

Now what, you might be wondering, did the word "scope" in that error message above mean?  It refers to the part of your program in which the variable can be used.  This is determined by where you declare it.  For example, if you want to be able to use a variable anywhere in your program, you can declare at the top of your code.  This is called a *global* variable; here's an example:

```arduino
int pin = 13;
void setup()
{
pinMode(pin, OUTPUT);
}
void loop()
{
digitalWrite(pin, HIGH);
}
```

As you can see, `pin` is used in both the setup() and loop() functions.  Both functions are referring to the same variable, so that changing it one will affect the value it has in the other, as in:

```arduino
int pin = 13;
void setup()
{
pin = 12;
pinMode(pin, OUTPUT);
}
void loop()
{
digitalWrite(pin, HIGH);
}
```

Here, the digitalWrite() function called from loop() will be passed a value of 12, since that's the value that was assigned to the variable in the setup() function.

If you only need to use a variable in a single function, you can declare it there, in which case its scope will be limited to that function.  For example:

```arduino
void setup()
{
int pin = 13;
pinMode(pin, OUTPUT);
digitalWrite(pin, HIGH);
}
```

In this case, the variable pin can only be used inside the setup() function.  If you try to do something like this:

```arduino
void loop()
{
digitalWrite(pin, LOW); // wrong: pin is not in scope here.
}
```

you'll get the same message as before: "error: 'pin' was not declared in this scope".  That is, even though you've declared pin somewhere in your program, you're trying to use it somewhere outside its scope.

Why, you might be wondering, wouldn't you make all your variables global?  After all, if I don't know where I might need a variable, why should I limit its scope to just one function?  The answer is that it can make it easier to figure out what happens to it.  If a variable is global, its value could be changed anywhere in the code, meaning that you need to understand the whole program to know what will happen to the variable.  For example, if your variable has a value you didn't expect, it can be much easier to figure out where the value came from if the variable has a limited scope.

[block scope]
[size of variables]

[1] In some languages, like Python®, types are associated with values, not variable names, and you can assign values of any type to a variable.  This is referred to as *dynamic typing*.