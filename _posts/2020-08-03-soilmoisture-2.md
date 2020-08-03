---
layout: post
title: "Soil moisture monitoring in a flower garden - a little bit of planning"
categories: [blog]
mathjax: false
image: /assets/2020-08-03-soilmoisture2/yard.png
---    
What am I doing here, anyhow?

<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub> 

Though I haven't been writing much lately, I have been keeping an eye on the flower garden and thinking about how to handle the monitoring the way I think it needs to be done.

I finally sat back down at the computer this last weekend and sketched out my yard and the flower garden.

It looks like this:

|House and yard|
|--------------|
|![House and yard](/assets/2020-08-03-soilmoisture2/yard.png)|

The flower garden is in front of the house - that's the bottom of the sketch.  The tan color indicates the area covered in bark.  Nominally 10 centimeters deep, though I have my doubts about how evenly it's covered.  We have bunch of lavender plants and a bunch of small bush roses planted in elliptically curved rows.  There are other types of flowers and shrubs scattered around the free area. The brown strip in front of the strip indicating the bush roses is a row of sandstone blocks and old sandstone watering troughs.  We use the troughs as flower pots, and have other flowers planted in and around the rocks.  The rocks are from an old quarry that belongs to my wife's family.  The green strip in front of that is a row of tulip like things - I have no idea what they are called. 

The house is in the middle.  That's the light blue colored area.  It isn't really all that big, it's just that the yard is very small.  The house has two floors and an attic, and it is made of concrete and cinderblocks with a lot of stucco - it does a dandy job blocking radio waves.

The back yard is along the top of the sketch.  The light green color indicates the grass growing there.  The apple tree was kind of forced on us - the city requires a tree of some kind in every yard, but not too big.  We get maybe two or three apples a year from it.  There's a corner behind the apple tree and the flower pots where we have wildflowers for the bees and the butterflies.

Along the left side of the yard and curving around to the back is a row of big flower pots.  These are 40 centimeter kidney shaped pots stacked two or three high.  My yard and the neighbor's yard aren't even - his is anywhere between 30 centimeters (at the front of the house) to 1 meter higher than mine.  The flower pots are set in concrete and act as a retaining wall so that the neighbor's yards stays in his yard.  We have various flowers and other things planted in the pots, including a bunch of roses (the red dots inside the brown flower pots.)

There are five blue dots scattered around the yard.  Those are the soil moisture sensors I currently have.  I've got them placed in the spots I think are most critical right now.

The tulip things need more water, there's a holly looking kind of thing that seemed to be a little yellow like it wasn't getting enough water.  I particularly wanted to keep an eye on those.

There's one sensor in the front yard by a big rose bush.  That's the only one we kept when we had the yard landscaped last fall.  That rose bush has alway done well, and since I put that sensor in there I know why.  Besides now always having enough water, it turns out that that one spot in the yard has the absolute best nutrient values of the whole yard.  For what ever reason, the dirt there is just really good.

I have one sensor in the flower pots in the back yard to tell me when the pots need water.  It turns out that they need water almost every day.  They don't hold moisture well.

There's one sensor in with the wild flowers because that spot is different from everything else.  It's just the plain old dirt (with lots of clay) that was originally in the yard.  No bark or anything else.  It turns out that corner holds moisture better than the flower pots do.

What I intend to do is to change the front yard from "monitor critical spots" to "monitor the whole thing in a grid."  I want to study how the soil moisture behaves over time and across the whole flower garden.

Besides that, I want to extend the montoring in the back yard from just the two (supposedly) representative spots to at least six spots because the flower pots don't all get the same amount of sunlight - some of them may dry out faster than others.

With that picture of the yard to look at, you can see that it is unlikely that a single monitoring station would have a Bluetooth connection to all of the sensors.  I'm going to need at least two and maybe three ESP32s to cover the whole area.

## Planning

The layout of the yard dictates a lot of things, and has an lot of influence on how much hardware I need and what the software will have to do.

### Hardware

- I'm going to need at least 15 soil moisture sensors.
- I'm going to need three monitors.
- Each monitor will be made of an ESP32 and a solar charging power bank.
- The monitors will read the soil moisture data from the sensors using Bluetooth, and send them to a central server in the house using MQTT over WiFi.

I kept trying to figure out how to hook up each ESP32 to a solar charged battery, and keep the whole thing water proof.  I kept coming up with "3D print a housing an custom design a BMS and solar charging circuit" then thinking "nope, too much stuff."  I finally figured out how to do it simply:  I've ordered some cheap battery banks with built in solar cells, and I'm going to attach them to fence posts.  The ESP32s go on the fence post as well, with a plain old (short) USB cable connecting the power bank and its ESP32.  Then I'm going to cut the necks off of some 3 liter platic bottles and plop them down over the ESP32 and the power bank.  Rain protection for the electronics, and transparent for the solar panels.  Cheap, simple, stupid, easy.

### Software

There's several pieces of software I'm going to have to write.  I have particular ideas about the montoring that don't square with the way most projects work, so I'll have to write my own ESP32 software. I have peculiar ideas about how to assign sensors to monitors, which means that there has to be a server part that works as a go between for the ESP32s and the Django server that will be collecting the data and providing simple summaries.  Finally, there will be an analysis program that can make 3D graphs of the soil moisture data.

# ESP32

The plan here is to make the firmware as stupid as possible.  "Brains" will be in the server.

Since the Bluetooth range of the monitors will overlap, the sensors have to be assigned to monitors.  The Django software will handle the assignment (GUI for the user) and the server will enforce that on the ESP32 monitors.

# Server

Will run as a demon on a Linux system.  It will consist of some MQTT stuff (to talk to the monitors) and some Django libraries (to dump the 
sensor data into the Django database.)  It will read the sensor assignment from the Django database and make sure each monitor reads the correct sensors.

# Django application

This will be installed in a web server and will handle management of the system and provide some simple views of the collected data.

# Analysis software

This will use the Django libraries to access the collected data.  What I want to do is to look at soil moisture over time and location, and in relation to temperature and sunlight intensity.  The sensors provide four different values (soil moisture, temperature, nutrients, and sunlight intensity) over time.  I want to visualize how they all relate.

The software might be some scripts to pull the required data out of the Django database for use in some standard data analysis program, or it might be something written just for this task.  It depends on what I can find, and whether any existing program can do what I want.

---------

That's the plan in a nutshell.  I'll write more about each part as I go to implement it.

<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub> 
