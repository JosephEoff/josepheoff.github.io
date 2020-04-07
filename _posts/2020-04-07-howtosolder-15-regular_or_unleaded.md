---
layout: post
title: "HowTo: Solder by hand - Regular or unleaded"
categories: [blog]
mathjax: false
---  
What kind of solder is best?

<sub>[HowTo: Solder by hand - Table of Contents](howtosolder-toc)</sub> 

For those in a hurry:

**Good lead free solder is just as easy to use as tin/lead 60/40.** 

There's a summary of the required soldering iron tip temperatures at the end of this post.

------------------

|Regular vs. Unleaded|
|--------|
|![Regular vs. Unleaded](/assets/2020-04-07-howtosolder-15-regular_or_unleaded/solder.jpg)|

From the very first word I wrote in this series, I had planned on comparing 60/40 tin/lead solder with lead free solder.  Every time the subject of lead free solder comes up on the ["Electrical Engineering" stackexchange,](https://electronics.stackexchange.com/) you hear cries about how difficult lead free is to use, and that you need lots of flux, and just general complaining about how horrible it is.  I wanted to see for myself just how bad lead free is in comparison to the old standby tin/lead 60/40.

I've used tin/lead for a very long time - I learned to solder with it as a kid, and I'm over 50 now.  I've spent the better part of four decades using solder with lead in it.  I know how to work with it, and have no trouble using it at all.

Up until recently, I had never used any lead free solder.  I left the last job where I used a soldering iron every day just as lead free solder was becoming a thing, and never had a need to switch.  I've got a 100 gram roll of 60/40 that I've been using for years for hobby stuff.

Solder with lead isn't completely forbidden, even in Europe.  The [RoHS restriction of lead in solder](https://en.wikipedia.org/wiki/Solder#Lead-free_solder) applies to lead in **consumer** devices.  That's anything commercially mass produced and sold to typical users.  It doesn't apply to hobby use, and 60/40 tin lead solder is still commonly available.

At first I had intended to do a separate comparison of lead free and tin/lead solder, but the roll of lead free solder I ordered came before I had made even the first photo for this series.  With the lead free solder in hand, I figured I'd do better to give it a really good try by doing all of the photos using lead free solder.

I mostly stuck to that, and it worked well.  I learned a bit about lead free solder, and got more experience with it than I would have in doing just a short set of test joints for a comparison.

I say mostly because when I started doing the photos for the post "[Soldering SMD ICs](howtosolder-13soldersmdic)," my old soldering iron kind of wimped out on me.  It did the first couple of joints just fine, then the temperature dropped.  It will no longer get any hotter than about 270 degrees celsius, which is far too low for lead free solder.

I finished the last two posts ("Soldering SMD ICs" and "Removing SMD ICs") using 60/40 tin/lead and my old iron.

I've bought [a new soldering iron](howtosolder-16-new-soldering-iron) and gone back to confirm that SMD ICs really can be soldered and removed using lead free solder just as I did it with the 60/40 solder.

Now, I must admit that I haven't tried out all kinds of lead free solder.  I don't have that much time, nor the inclination to shell out 20Euros a roll for several rolls of solder that I'll never use up.

What I did was to read up on what types of lead free solder there are.  What I found was that the lead free solders known as ["SN100C"](http://nihonsuperior.co.jp/english/product/leadfree/core/) (despite having small amounts of other metals in the alloy) were the best and easiest to use.  I also found that the company that makes the solder I've used for the last 30 years or so also makes a [SN100C type alloy.](https://www.stannol.de/en/news/news/sn100c/)

What I ended up with was not quite SN100C.  I bought a roll of [SN99.3Cu0.7 HS10 solder from Stannol.](https://www.conrad.com/p/stannol-hs10-fair-solder-reel-sn993cu07-100-g-05-mm-1414237) It has a core of 2.5% rosin flux.

I don't know if SN100C (or some other alloy) is better.

I do know that I had no trouble with my roll of SN99.3Cu0.7.  It does require a higher temperature than tin/lead 60/40.  Once you work that out, it is just as easy to use as the 60/40 ever was.

If somebody's griping about how hard lead free solder is to use, then either they've got some crappy solder or don't have the temperature high enough - or they just plain don't know what they're doing.

A bottle of liquid flux or a flux pen isn't needed, either.  There's an appropriate amount of flux in the solder - if it isn't adequate you are doing something wrong.

Summary:

**Good lead free solder is just as easy to use as tin/lead 60/40.**

Since it does take a much higher temperature to use lead free than the typical old tin/lead 60/40, I thought I'd post a table of temperatures for different tasks.

These are the temperatures I found useful with the two types of solder I have, and using the small (1.2mm) chisel tip that I prefer.

|Task| Stannol Sn60Pb39Cu1 0.5mm (535236)|Stannol Sn99.3Cu0.7 0.5mm (599102)|
|----|-----------------------------------|---------------------------------|
|Solder through hole parts|270°C/520°F|330°C/630°F   |
|Remove through hole parts|310°C/590°F|330°C/630°F   |
|Solder SMD passive parts|270°C/520°F|360°C/680°F    |
|Remove SMD passive parts|270°C/520°F|360°C/680°F    |
|Solder SMD IC|270°C/520°F|360°C/680°F|
|Remove SMD IC|270°C/520°F|400°C/750°F    |
|Clean SMD pads with solder wick|270°C/520°F|360°C/680°F|

Those temperatures are measured at the tip with a K-Type thermocouple.  While making the measurements, I noticed something that bears mentioning.

All through this series, I've been reminding you to get a spot of solder on the tip of the iron every time you go to do something.

I've also mentioned that it is because the solder helps to conduct the heat from the tip to the parts and the PCB.

Clean solder conducts heat better than a bare tip.

The measurements of the tip temperature were always far too low if I wiped all the solder off the tip.

You **must** have a layer or drop of solder on the tip to quickly heat the joints.

Another thing I noticed is that oxidized solder conducts heat worse than fresh solder.

Always poke that bit of solder onto the tip immediately before using it.  Don't let it hang around for a long time.

And now, finally, lead free solder oxidizes much faster than the tin/lead 60/40.  Probably because of the higher temperature, but it does oxidize **much** faster.

A wait of just a few seconds can easily make a 20°C (70°F) difference in the temperature that you can measure at the tip.  That's loss of heat conductivity.

Don't fiddle around when working with lead free.  Poke some fresh solder on the tip, and move right on to whatever task you are working on.

It's a good idea to work that way regardless of the type of solder.  For lead free, it is an absolute **must** to work quickly and smoothly to minimize the oxidation of the solder on the tip of the iron.

A final note:

The temperatures for soldering and removing SMD parts really are that high.

Lower temperatures when soldering SMD parts with lead free solder leave you with dull gray joints - cold soldered joints are unreliable.  The higher temperature is needed to get a really shiny joint.

You need the higher temperature when removing the parts because you must switch back and forth between the rows of pins.  One row has to stay hot enough to remain liquid while you are heating the other row.  Lead free solidifies faster than tin/lead solder does.  Whether it cools faster or has a different transition from liquid to solid I don't know.  I just know that it took that 400°C to be able to consistently remove an eight pin SOIC easily.

---------------

That's my experience with lead free in comparison to tin/lead solder.

I don't think there's a clear winner on how well you can work with them.  I had no trouble with the lead free at all.

The old tin/lead solder does have the advantage of a lower working temperature.  If you have to work around other (plastic) components on your boards then that might mean the difference between a melted connector and one with just a skid marring the surface after you bumped it with the iron.

Other than that, I'm happy with either one.

What do you think?  What kind of lead free solder have you used?  Did you like it?  Let me know in the comments below.

<sub>[HowTo: Solder by hand - Table of Contents](howtosolder-toc)</sub> 
