---
layout: post
title: "A sewing machine motor speed control - Functional"
categories: [blog]
mathjax: false
description: "A test run of my DIY sewing machine controller with the final software."
image: /assets/2023-11-10-motorcontrol13/1.jpg
---
A look at a functional DIY sewing machine motor speed control.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub>   

After only (snork) 18 months of development,  I present to you the finished "Bigfoot" sewing machine motor speed control.

|Bigfoot|
|-------|
|![Bigfoot](/assets/2023-11-10-motorcontrol13/1.jpg)|

It looks just like it did the [last time I worked on it](motorcontrol12) - software is invisible.

The difference is now that it makes use of the tachometer to regulate the speed.  The pedal is no longer a "gas pedal" to regulate the power to the motor.  The pedal is now the input to a "cruise control" that maintains the same stitching speed, no matter what comes.  It will go from stitching through eight layers of [Naugahyde](https://en.wikipedia.org/wiki/Naugahyde) (fake leather) down to two layers and back up to four layers while maintaining the same speed:

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/883578648?badge=0&amp;autopause=0&amp;quality_selector=1&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Bigfoot"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

Here's a close-up of the strip of fake leather:

|Layers of fake leather|
|----------------------|
|![Layers of fake leather](/assets/2023-11-10-motorcontrol13/5.jpg)|

I cut a strip an inch or so wide, then folded it in two the long way.  I then folded it once (4 layers) and twice (8 layers) the short way.

As you can see, the machine maintains the set speed no matter how many layers of fake leather it is punching through.

I did that with fake leather, but it will do the same with the real stuff.  Real leather is thicker so I can only get six layers under the presser foot.

To give Bigfoot a good test,  I made a carrying case for the music stand that my wife uses when she goes to choir practice. 

|Carrying case|
|-------------|
|![Carrying case 1](/assets/2023-11-10-motorcontrol13/2.jpg)|
|![Carrying case 2](/assets/2023-11-10-motorcontrol13/3.jpg)|
|![Carrying case 3](/assets/2023-11-10-motorcontrol13/4.jpg)|

Most of the seams are through three layers of leather.  The carrying strap is sewn through one layer of nylon webbing and two layers of leather because I put backing patches behind the leather to make sure they straps don't tear off.

I made a practice case out of fake leather first, then made the red and black one from pieces of leather that I bought on Amazon.  I've found that it is hard to purchase large pieces of leather.  All I've been able to find are scraps (at stupidly high prices) and large pieces at outrageously high prices.  Maybe I just haven't found the right source yet.

I've put the plans and the software for Bigfoot in a [GitHub repository by the name of Bigfoot.](https://github.com/JosephEoff/Bigfoot)  It is currently a disorganized mess of all the things I collected and made and designed and wrote to get Bigfoot working.  I need to organize it, get everything up to date, and corrected.  That will take a while yet.

Have a look.  If you're interested but can't make sense of the mess that is currently the Bigfoot repository, drop me a message in the comments below or open an issue on GitHub.  You may also visit the [Hackaday.io Bigfoot project page.](https://hackaday.io/project/193592-bigfoot-sewing-machine-motor-speed-control)

------

A word of warning:
There are a couple of things I need to change in the schematic.  I forgot them when I designed the board and tacked them on when I assembled it.  Wait for the updated version before you build a copy.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub> 
