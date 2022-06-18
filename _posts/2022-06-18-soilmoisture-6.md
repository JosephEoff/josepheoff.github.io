---
layout: post
title: "Soil moisture monitoring in a flower garden - Catastrophe - or not"
categories: [blog]
description: "Inverstigating causes of soil moisture variation in a flower garden."
mathjax: false
image: /assets/2022-06-18-soilmoisture-6/1.jpg
---
When planning pays off.

<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub>

I was out in the garden yesterday, talking to a neighbor, and noticed one of my soil moisture sensors laying on the bark chips.  Oops.  Somebody stepped on it and killed it.

|Dead sensor|
|-----------|
|![Dead sensor 1](/assets/2022-06-18-soilmoisture-6/1.jpg)|
|![Dead sensor 2](/assets/2022-06-18-soilmoisture-6/2.jpg)|

It's times like these when you are glad you stopped to think about project requirements before writing software.

Back when I wrote the [Mud-Py software,](https://github.com/JosephEoff/Mud-Py) I thought a good bit about not only the things that it had to do to be functional,  I also thought about things that would happen to the system that it would have to be able to deal with.

Among the non-software things I figured the software would have to deal with was damaged or destroyed sensors.  The sensors aren't that large, and they are stuck in the dirt through 4 inches (10 centimeters) of bark chips.  They are hard to see when you are doing yard work. It isn't a question of if somebody (like me) will step on one, it is a question of when it will happen.

It happened on 14 June, 2022 at around 6PM.

|Smoking gun|
|-----------|
|![Smoking gun](/assets/2022-06-18-soilmoisture-6/3.png)|

At 5:30PM, the soil moisture reads over 35 percent.  At 6:30PM, the moisture reading has dropped to zero.

I usually do my gardening after work - quitting time is around six o'clock in the evening.  Looks like I killed the sensor myself.

Interestingly, the sensor kept running until about 3:00 AM the next day.  It kept running, though the soil moisture  and the conductivity detectors were gone.  The damage seems to have caused the sensor to expend a lot of energy.  Maybe there was a short circuit somewhere.  What's certain is that the battery charge level dropped from over 50 percent at the time it was damaged to 0 percent at 1:30AM the next day.  At 2:30AM, the sensor lost contact with the control nodes.

|Dying battery|
|-------------|
|![Dying battery](/assets/2022-06-18-soilmoisture-6/4.png)|

So what's all this got to do with software design?

Everything.

Resiliency was a concern from the start.  Mud-Py was written with the assumption in mind that every piece of hardware out in the yard could be damaged (or swiped) at any moment.  Because of that assumption, it is structured so that replacing a piece of hardware is easy.  The structure also allows me to track which piece of hardware was doing what, when.

Mud-Py data consists of three sections:
1. Zones
2. Control nodes
3. Sensors

- Sensors collect the soil moisture data.
- Control nodes collect the sensor data and send it to the database.
- Sensors are assigned to zones to generate the charts.

None of the assignments are hard coded.  Any sensor can be assigned to any zone and to any control node.

The analysis software ([Mud-Py Analyser](https://github.com/JosephEoff/Mud-Py-Analyser)) collects the sensor data for all sensors in a zone to make its plots.  Since the sensor data are stored with the zone and GPS coordinates for the sensor at the time each measurement was made, the analyser can make its charts no matter how I've moved the sensors around or replaced them.

To replace sensor 12, all I had to do was to stick sensor 6 (a spare) in the ground where sensor 12 was, then take sensor 12 out of the "Front Yard" zone and out of the control node assignment. Sensor 6 was then assigned to "Front Yard" and to the closest control node and given the coordinates from sensor 12.  It took me less time to do it than to write about it - in fact, the software part went faster than digging sensor 6 out of storage and sticking it in the ground.

This same flexibility is also the reason putting the sensors out in the yard this spring was no problem.  Rather than trying to put each sensor back where it was last year, I stuck them all in place, noted where they were in a sketch, then assigned them to their new positions sitting comfortably at my computer.

I was going to post some updates, but the plots are still wonky.  I haven't gotten around to rewriting the interpolation routines in the heatmap display.  I'll try to take another look at that soon.  The data is being saved properly - it is all correct.  It's just the display that seems totally bizarre.

Another day.




<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub>
