---
title: Arduino/Processing/Python Language Comparison
description: Comparison between three programming languages
---

## Arduino/Processing Language Comparison

The Arduino language (based on Wiring) is implemented in C/C++, and therefore has some differences from the Processing language, which is based on Java.

## Arrays

|Arduino|Processing|Python|
|-|-|-|
|int bar[8];<br/>bar[0] = 1;|int[] bar = new int[8];<br/>bar[0] = 1;||
|int foo[] = \{ 0, 1, 2 };|	int foo[] = \{ 0, 1, 2 }; <br/> or <br/>int[] foo = \{ 0, 1, 2 };||

## Loops

|Arduino|Processing|Python|
|-|-|-|
|int i;<br/>for (i = 0; i < 5; i++) \{ ... }|	for (int i = 0; i < 5; i++) \{ ... }||

## Printing

|Arduino|Processing|Python|
|-|-|-|
|Serial.println("hello world");	| println("hello world");||
|int i = 5; <br/> Serial.println(i); | int i = 5; <br/> println(i); ||
|int i = 5; <br/> Serial.print("i = "); <br/> Serial.print(i); <br/> Serial.println();|int i = 5; <br/> println("i = " + i);||
