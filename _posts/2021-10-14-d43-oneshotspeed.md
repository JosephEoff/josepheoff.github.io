---
layout: post
title: "D43 oscilloscope software - Oneshot capture and the D43 time base"
categories: [blog]
mathjax: false
image: /assets/2021-10-14-d43-oneshotspeed/10microsecondpercm.png
---
I feel the need — the need for speed!

<sub>[My Telequipment D43 projects - Table of Contents](d43toc)</sub> 

I found some folks discussing the D43 software recently on a forum somewhere.  One of the folks involved suggested that the oneshot function might not be terribly useful, as the camera wouldn't be able to capture anything really fast.

Well, you know, it **is** just a webcam.

So how fast can it go?

The only way to find out is to try it and see.

To try it, you have to have a source of one shot signals of very short duration.

Since fastest sweep time on the D43 is 0.5 microseconds per division, a pulse a couple of microseconds long should do just fine.

My home lab is rather short on high speed anything, but rather long on typical hobbyist stuff - like the ubiquitous Arduino.

I found [this](https://wp.josh.com/2015/03/05/the-perfect-pulse-some-tricks-for-generating-precise-one-shots-on-avr8/) blog post on generating short, single shot events with an Arduino.

I modified a copy of the [program code](https://github.com/bigjosh/TimerShot) to send a single pulse everytime it gets a character over the serial port, and sent some pulses at my D43.

After dinking around with it a bit to get the triggering on the D43 adjusted correctly, I found that the software/webcam combination will work at sweep speeds up to 5 microseconds per division.

With a little tweaking of the webcam settings through OpenCV, I found I could get it up to 2 microseconds per division.

The 1 microsecond and 0.5 microsecond per division sweeps are too dim for the camera to capture.

The captures look like this:

|5 microseconds per division|
|---------------------------|
|![5 microseconds per division](/assets/2021-10-14-d43-oneshotspeed/5microsecondpercm.png)|

That's the limit with the standard settings for the webcam.

|2 microseconds per division|
|---------------------------|
|![2 microseconds per division](/assets/2021-10-14-d43-oneshotspeed/2microsecondpercm.png)|

That's the absolute limit if I tweak the webcam settings through OpenCV.

Even the 5 microsecond per division sweep is a little anemic.  You have to look **really** close to see the trace.

The 10 microsecond per division sweep is much better, but then the short signal looks **really** short:

|10 microseconds per division|
|---------------------------|
|![10 microseconds per division](/assets/2021-10-14-d43-oneshotspeed/10microsecondpercm.png)|

It looks like I'm not going to get all the speed there is.

At least now I know how much I **can** get.

<sub>[My Telequipment D43 projects - Table of Contents](d43toc)</sub> 
