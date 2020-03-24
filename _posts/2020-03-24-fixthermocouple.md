---
layout: post
title: "Fixing a K-type thermocouple"
categories: [blog]
mathjax: false
---
When cheap crap breaks and ordering a replacement will take too long.

I recently bought a new soldering iron, and have been familiarizing myself with it and learning what temperature it takes to do what.  With my old iron, I just cranked up the heat any time I felt like it wasn't hot enough.  It didn't have a display, and I'm not sure it even had a temperature sensor.

In any case, I've been comparing the temperature at the tip of my new iron to the measured temperature on the display.  I found that the display was fairly accurate with the original tip, but lost about 30 degrees celsius when using the fine tip I prefer.

I've also found that it takes a higher temperature to solder with a fine tip than with a blunt tip.  I can solder wires with the fine tip just fine at 260 degrees celsius, but it takes about 300 degrees to do SMD parts.

I've been using the K-type thermocouple with my multimeter to measure the temperatures.  It agrees to within a couple of degrees of the measured temperature on the soldering station when using the original tip so I figure the meter and the soldering station are at least somewhat accurately calibrated.  That may not be a safe assumption, but I haven't got anything else to go on.

While checking the tip temperature of the fine tip while soldering an SOIC-8 part, the meter just up and quit measuring temperatures.

Here's the guilty party:

|Meter and thermocouple|
|---------|
|![Meter and thermocouple](/assets/2020-03-24-fixthermocouple/meter.jpg)|

The jack for the thermcouple on the meter was always a little flaky, so I thought it might be broken or just have bad contact.  I took the meter apart, disassembled the jack, tightened the pressure on the spring contacts, and reassembled the whole thing.  The plug fit better and held tighter, but still no temperature.

I fiddled with it for a while, then figured it was time to order a new thermocouple.  A quick look at Amazon and other places showed I'd be waiting a couple of weeks for one to be delivered, so I decided to take a closer look at the thermocouple.

I checked the internet, and found that a properly working K-type thermocouple will have pretty much no resistance when measured with an ohmmeter.  Mine showed pretty much zero ohms from pin to pin, so at least it wasn't an open circuit.

A functioning thermocouple should also show a few millivolts DC when hot.  I checked that, and found zip - no voltage at all from the thermocouple.

On a random impulse, I measure the resistance between the two wires at the thermocouple end.  That was odd.  There's about three ohms of resistance across the thermocouple at that end.

The only way for that to be possible was for there to be a short in the wiring in the plug.

Fortunately, the plug can be disassembled.

Once I got all the fuzz from the cloth covered wires out of the way, I could see that the bare wires inside had been twisted around and shorted out.  The plug end was indeed shorted.  The plug has a strain relief for the cable, but there's nothing to prevent the wire from spinning inside the strain relief.  Just using the probe had twisted the wires around inside the strain relief and shorted them.

I disconnected the wires from the plug pins, cleaned more fuzz out of the way, and untwisted the wires.  With it all reassembled, the meter was again showing the correct temperature.

While putting it back together, I put a small piece of heat shrink tubing over one of the wires inside the plug.  Maybe it'll help, maybe it won't.

If you have a K-type thermocouple that came with your multimeter or if you bought one of the many cheap K-type thermocouples from Amazon or wherever, it may some day quit on you.  It might be broken, but there's a better than fair chance that it is just shorted out.

This is what a cheap K-type thermocouple looks like:

|K-type thermocouple|
|---------|
|![K-type thermocouple](/assets/2020-03-24-fixthermocouple/thermocouple.jpg)|

Note that the wires to the thermocouple (the little metal ball at the end of the cable there in the upper left corner of the picture) are bare - they can easily be shorted by bending or twisting the wires.  You might also get a splatter or crumb of solder or other metal between them.

The wires inside the plug are bare as well:

|Bare wires inside the plug|
|---------|
|![Bare wires inside the plug](/assets/2020-03-24-fixthermocouple/plug-barewires.jpg)|

This is what the inside of the plug looked like when I got done:

|Fixed plug|
|---------|
|![Fixed plug](/assets/2020-03-24-fixthermocouple/plug-fixed.jpg)|

Here's how to check and fix your thermocouple:

1. Measure the resistance from pin to pin on the plug.  It should be low, but definitely not a dead short.  Mine showed about 0.1 ohms when it wasn't working.  Now that is working again, it shows about 15 ohms.
2. If the resistance measurement shows an open circuit, look closely at the thermocouple itself.  The actual thermocouple on mine is just a bare metal ball.  It may have gotten crushed or one of the wires may have broken off.  If it is mashed or one of the wires is broken off right at the thermocouple then you're going to have get a new one - that kind of thing can't be fixed.
3. There may be a broken wire in the plug if you find an open circuit from pin to pin.  Open the plug and see if one of the wires has been twisted off. If so, strip back some of the insulation, cut both bare wires to the same length, and reattach the wires.
4. If the resistance measurement shows a dead short from pin to pin, check the thermocouple itself first.  The cheap ones have the thermocouple sticking out of the end of a cloth covered cable.  The bare wires can get shorted just by bending them.  They can also get twisted and short out.  If you've been measuring the temperature of soldering iron tips like I was, you should also check and see if a splatter of solder is shorting the thermocouple.
5. If you find a dead short from pin to pin, check the inside of the plug and see if the wires are twisted.  If so, unscrew them from the pins and untwist the wires.  It might help to put a piece of heat shrink tubing over one of the wires before reassembling it. 

If you have to disconnect the wires from the plug pins then you'll have to take care to get them back on the proper pins when you reassemble the plug.  You'll know you did it wrong if you measure the temperature of some hot thing and the displayed temperature drops instead of rising.  Just swap the two wires and it'll be OK.

A little poking around saved me a few bucks and a couple of weeks worth of waiting for a new thermocouple.

If you found your way here and managed to fix your thermcouple, leave a comment and let me know how yours was broken and how you fixed it.

