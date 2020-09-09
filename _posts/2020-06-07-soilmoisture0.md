---
layout: post
title: "Soil moisture monitoring in a flower garden - A first look"
categories: [blog]
mathjax: false
image: /assets/2020-06-07-soilmoisture0/yard.jpg
---    
How much is enough, and how do you know?

<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub>

It's been a while since I posted anything to the blog.  I've been busy out in the real world, doing yard work and other things since the weather has been so nice here lately.

The real world has now brought me back to the virtual world.  Yesterday and today were rainy, so I finally got a chance to sit down at the computer and take a look at some data gleaned from the yard work I've been doing.

My wife and I had some major work done on our yard last fall.  We had a 2500 liter (650 gallon) rain water cistern buried in the back yard and connected to the rain gutters.  We also had all the bushes and stuff taken out of the front yard, and the top 50 cm (20 inches) dug out and replaced with better dirt.  After all of that, we planted a bunch of roses and some lavender and some shrubs.

All the flowers have blossomed and look really nice.

|Flower garden|
|----------------|
|![Flower garden](/assets/2020-06-07-soilmoisture0/yard.jpg)|


I am the world's worst gardener.  If plants had nightmares, I'd be their Freddy Krueger.

To keep our newly planted flower garden from drying up and dying, my son and I installed a set of soaker lines in the front yard, then buried the whole mess under 10 centimeters (4 inches) of bark.  The cistern has a pump that is connected to the soaker lines, and I have a flow meter to measure how much water I've given the yard.  Watering is no problem.

The real question, though, is "How much water is enough?"

If you try to look it up, you get vague recommendations for different kinds of plants, but no concrete recommendations.

Even if you know how much water is enough, how do you measure it?

Measuring is easy - if you believe all the posts you can find on the internet about building various kinds of soil moisture sensors.  Then you check deeper, and find that most such projects are uncalibrated and basically uncalibratable. Commercially available sensors for hobbyists are out there, but mostly as relative measurements that tell you the soil moisture went up or down but that don't actually tell you how much moisture the soil contains.  To top it off, the sensors themselves aren't waterproof.  All the electronics bare, just waiting for rain or the watering can to ruin.

The low end of professional equipment is also not really all there.  Wire connections, and cobbled together housings that aren't waterproof.  I found one that recommended purchasing a separate housing for the battery because the battery would corrode in the moist conditions inside the data collection controller box.  Insane. 

I finally found that there are bluetooth connected, waterproof sensors available.  Xiaomi makes them, and there are several suppliers that sell compatible equipment under different names.  What's more, the software has a catalog of recommended soil moisture and fertilizer measurements for thousands of plants.  Not only can you measure with (semi) calibrated sensors, you have concrete recommendations to follow.

That's a big step in the right direction, so that's the way I went.

I have a couple of those sensors in my yard now, and I'm learning a bit about soil moisture.

I've kept an eye on the soil moisture for over a month, and I've noticed a few things:

1. The soil under the bark never really dries out.
2. The soil moisture varies depending on the recorded temperature.
3. The recommendations in the software are a starting point, but not complete.

I haven't had to water the front yard since I got the sensors.  I've found that the bark covering helps the soil retain enough moisture at all times to meet the software's recommendations.  The plants pretty much agree with that.  They are (almost) all green and healthy and blossoming like crazy.  Even the one (twenty year old) rose bush we kept is blooming much better than ever before.

"Almost" is important here.  Most things are green and healthy, but there's a spot or two where the plants are sort of yellowish like they aren't getting enough water.  Well, are they getting enough water or not? The recommendations from the software say, for example, that the soil moisture needs to be between 18% and 50% for roses. Does that mean average soil moisture over the whole day, or does it mean that the minimum should stay over 18%?  I don't know, and I suspect the manufacturer doesn't either.  The sensors are intended for use indoors with potted plants.  The variable soil moisture readings I get outdoors just don't exist in potted plants.  Sure, the soil moisture in indoor flower pots changes but it doesn't change in response to the air temperature.

To try to understand things better, I pulled all the data for the sensors out of the Android software that comes with the sensors, and used Libre Office to generate some graphs to get a better look at what's going on.

This is a sample of some of the charts I made:

|Complicated mess|
|----------------|
|![Soil moisture charts](/assets/2020-06-07-soilmoisture0/soilmoisture_vs_temperature_timeofday.png)|

That looks horrible, but it's fairly simple to understand:

- The color of the line is the day.
- There's a soil moisture and a temperature plot for each day.
- Each day has 24 measurements.

What I see there is that the hotter the day is, the more the soil moisture sinks during the day.  I also see that the soil moisture drops more as the month goes on.  There's apparently a lot of water trapped in the dirt under the bark.  The water evaporates during the day when it is warm, then replenishes from deeper down when the temperature drops again.  That "deeper down" water is slowly getting used up, but it is at all times enough to keep the soil moisture above the minimum recommended level.

What I also see is that there is a time coming when the soil moisture will drop below the minimum recommended level during the day.  That time may have already been reached at various spots in the garden, but with just two sensors I can't really tell.

What I'd like is to have more sensors and some software that summarizes the data into a sort of "heat map" showing the moisture distribution around the yard.

That won't happen with the standard software for the sensors.  That software is **sad:**

1. It stores your data in the cloud.  Somewhere.  It will not work without WiFi.
2. The software is setup to monitor individual plants with individual sensors - you can't get an overview of multiple sensors out of it.
3. The software can't even display a reasonable summary for a single sensor.  For example, it has no "last 30 days" charts.  It has a "month" chart.  You can't follow trends that way.  Even the "week" chart is the same way.  Not "last 7 days" but "this calender week."

The other thing is that the bluetooth signal doesn't do very well with the sensors down on the ground.  If I stand right in front of one, I often don't get a signal from it.  If I get further back, but higher up, then I usually get a good signal.  Getting all of the data from multiple sensors (without using a ladder) would consist of running around the yard and reading the data from each sensor indvidually.  Madness.

I've looked around, and found that there are open source projects that can read the sensor data and dump it to an MQTT server.  I plan to setup a small network of ESP32s around the house to read sensor data from a bunch of the bluetooth soil moisture sensors.  I'm going to put together a Django system to read the data from MQTT, store it in a database, then provide summary charts and graphs from there.

That's going to take a while.  I'll be posting more on this subject as it goes along, and I'll link them all together in a separate table of contents like I've done for some of my other projects.

For now, I still don't know how much soil moisture my plants really need.  It looks like they've (mostly) got enough, but I'm going to find out for sure - some day.

<sub>[All about my experiments in soil moisture monitoring - Table of Contents](soilmoisture-toc)</sub>
