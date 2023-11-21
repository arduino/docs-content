---
title: abs()
categories: "Functions"
subCategories: "Math"
---





= abs(x)


// OVERVIEW SECTION STARTS
[#overview]
--

[float]
=== Description
Calculates the absolute value of a number.
[%hardbreaks]


[float]
=== Syntax
`abs(x)`


[float]
=== Parameters
`x`: the number


[float]
=== Returns
`x`: if x is greater than or equal to 0. +
`-x`: if x is less than 0.

--
// OVERVIEW SECTION ENDS




// HOW TO USE SECTION STARTS
[#howtouse]
--
[float]
=== Example Code
// Describe what the example code is all about and add relevant code   ►►►►► THIS SECTION IS MANDATORY ◄◄◄◄◄
Prints the absolute value of variable `x` to the Serial Monitor.

[source,arduino]
----
void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;  // wait for serial port to connect. Needed for native USB port only
  }
  int x = 42;
  Serial.print("The absolute value of ");
  Serial.print(x);
  Serial.print(" is ");
  Serial.println(abs(x));
  x = -42;
  Serial.print("The absolute value of ");
  Serial.print(x);
  Serial.print(" is ");
  Serial.println(abs(x));
}

void loop() {
}
----
[%hardbreaks]

[float]
=== Notes and Warnings
Because of the way the abs() function is implemented, avoid using other functions inside the brackets, it may lead to incorrect results.
[source,arduino]
----
abs(a++); // avoid this - yields incorrect results

// use this instead:
abs(a);
a++;  // keep other math outside the function
----
[%hardbreaks]


--
// HOW TO USE SECTION ENDS


// SEE ALSO SECTION
[#see_also]
--

[float]
=== See also

[role="language"]
* #LANGUAGE# link:../constrain[constrain()]
* #LANGUAGE# link:../map[map()]
* #LANGUAGE# link:../max[max()]
* #LANGUAGE# link:../min[min()]
* #LANGUAGE# link:../pow[pow()]
* #LANGUAGE# link:../sq[sq()]
* #LANGUAGE# link:../sqrt[sqrt()]

--
// SEE ALSO SECTION ENDS