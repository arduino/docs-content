---
title: 'Upgrading an Arduino NG to Auto-Reset'
description: 'This page will show you how to upgrade your Arduino NG to auto-reset when powered or uploaded to.'
tags: 
  - Arduino NG
---
If you have an Arduino NG and you're envious of all the seconds saved by those Diecimila owners who don't have to press the reset button anymore, this page is for you. You can upgrade an Arduino NG to take advantage of the auto-reset functionality in Arduino 0009 and beyond with just a 0.1uF (100 nano-farad) capacitor and a soldering iron.

First, unplug your board from power and heat up your soldering iron.

Near the ATmega168 chip on the NG, there are four unused solder pads, as shown below. Solder a 0.1 uF capacitor across the bottom (top???) two pads:


Here's the board shown with the capacitor installed:


That's it. Now plug the board back into your computer and upload a new program, but don't hit the reset button. It should upload with no problems.

NOTE: Tymm Twillman notes that OSX triggers the RTS on serial port opening while Windows doesn't. So Windows machines may not respond to this fix. If you find this doesn't work for you, try soldering the cap to the upper two pads instead.

You may want to burn the Diecimila bootloader onto your chip as well, to eliminate the delay that happens between the end of upload and the beginning of your program.