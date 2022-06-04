---
layout: post
title: "Soil moisture monitoring in a flower garden - An update after a very long pause"
categories: [blog]
description: "Inverstigating causes of soil moisture variation in a flower garden."
mathjax: false
image: /assets/2022-06-04-soilmoisture-5/1.jpg
---    
Mysteriouser and mysteriouser.

<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub> 

The flower garden is back in bloom, and I've got my sensors out there again this season keeping track of the moisture.  I might have let it slide, but my wife talked me into putting the sensors back out in the yard - it seems to give her a bit of security about the garden when she knows I'm tracking it.

|Garden|
|------|
|![Garden](/assets/2022-06-04-soilmoisture-5/1.jpg)|

The big rose bush is blooming like crazy, the lavender is trying to take over the world, the little teacup roses are starting to bloom, and the peony has gone crazy (it has never had so many blossoms on it.)  The dahlias are sprouting, but not yet ready to bloom - they tend to show up later in the summer.

I've stuck to my usual "water and fertilize once in the spring" plan.  I mix a liter of liquid fertilizer with 100 liters of water in a rain barrel and pump it in under the bark using the watering lines my son and I laid before putting the bark on the flower garden.

As far as the plants are concerned, the verdict is in:  They grow and thrive, so they seem to have enough water.

I'm still not any closer to understanding the soil moisture in my garden, despite winning the "Data Wizard" prize in the [Hackaday "Data Loggin' Contest"](https://hackaday.io/contest/176306-data-loggin-contest) in April of 2021  for the [soil moisture monitoring project](https://hackaday.io/project/178004-soil-moisture-monitoring-in-a-flower-garden) that I put up on Hackaday.io.

The moisture fluctuates over the day, somewhat following the temperature.

Is it any surprise when the soil moisture is low under the hot mid-day sun?

|Hot day, low soil moisture|
|--------------------------|
|![Hot day, low soil moisture](/assets/2022-06-04-soilmoisture-5/2.png)|

That's at one o'clock in the afternoon on a warm day - the sensors are reporting 40 degrees C in some places.  I don't find it surprising that the dirt under the bark dries out a good bit.

I **do** find it surprising that the soil moisture went up drastically on the same day, just a few hours later - and without it actually raining.  The moisture changes in ways I don't understand.

|Same hot day, higher soil moisture in the mid-afternoon|
|-------------------------------------------------------|
|![Same hot day, higher soil moisture in the mid-afternoon](/assets/2022-06-04-soilmoisture-5/3.png)|

To make the confusion complete, the moisture takes a nose dive at around seven o'clock in the evening of the same day, only to recover completely an hour later.

|Same day, dry then moist in the evening|
|---------------------------------------|
|![Same day, dry then moist in the evening, 7 PM](/assets/2022-06-04-soilmoisture-5/4.png)|
|![Same day, dry then moist in the evening, 8 PM](/assets/2022-06-04-soilmoisture-5/5.png)|

I'm beginning to think that the soil itself plays a part in this - as well as the plants.

- Moisture takes time to "wick" up through the soil to replace evaporated water.
- The plants "drink" from the available moisture, making the soil dry.

I've been trying to think of ways to separate the effects of the soil, the evaporation due to heat, and the plants taking water out of the soil.

I may have to do something like set up some planters with monitors to take control data.

1. A planter without plants to observe the "wicking" effect and the evaporation.
2. A planter with plants (and a water reserve) to observe the effect of the plants "drinking."
3. Some other setup to capture just evaporation.

It looks like this is going to be a fairly long running project.

------

Besides taking a look at the data, I spent some time trying to figure out why the control nodes sometimes hang up and stop reporting data.

I think the problem lies in the WiFi management.

The control nodes are programmed to automatically "take a nap" and retry if any part of the monitoring cycle takes too long.  I've been watching what happens, and I think that the node sometimes has trouble connecting to the WiFi and hits the timeout.  When the "nap" ends, the WiFi can't doesn't connect at all.

Searching the internet lead me to a site (somewhere) this last week with the hint that you really need to call WiFi.disconnect() everytime your program is done with the WiFi adapter.  Given the way the timeout works, it isn't practical to call WiFi.disconnect() before doing the "take a nap" bit - you could get into an endless loop of timeouts and trying to disconnect.

What I did was change the WiFi connection routine in the control node software to call WiFi.disconnect() **before** starting the WiFi connection.  This clear away any leftover bits of whatever the WiFi was doing before starting it up again.

The problem only occurs sporadically, and only when the control nodes are out in the yard - there's no way to debug it on the workbench.

The nodes now have the modified software.  I'll be keeping an eye on things to see if it gets any better.

------


The tag-line for this post is a quote from a novel - an intentional mis-quote from Lewis Carroll's *Alice in Wonderland.* If you track down the quote, I recommend reading the book  - it's very good.


<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub> 
