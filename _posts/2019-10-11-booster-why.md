---
layout: post
title: "One last word about the simple voltage booster"
categories: [blog]
mathjax: true
--- 
{% include lib/mathjax.html %}
Ulterior motives revealed.

The idea for the simple voltage booster came up during an discussion in the Electrical Engineering Stack Exchange chat room.  There was a person present who was **convinced** that inductors cannot store energy, and that they certainly couldn't store it in the magnetic field of the inductor.  This person would not accept that switching regulators do it all the time.  Nope.  The switching regulators **must** store the energy somewhere else because inductors **cannot** store energy.

Faced with that amount of pig headedness, I started trying to figure out how to build a simple and obvious voltage booster where it is bleeding obvious that energy is stored in an inductor.

The result was the [simple voltage booster.](voltagebooster) It's obvious as all get out that the only place energy can be stored is in the inductor because there's really **nothing** to it but an inductor.

That backstory is also the reason for having the LED in parallel with the coil.

Here's the circuit again:

|Simple voltage booster|
|----------------------|
|![booster circuit](/assets/voltagebooster/boostercircuit.png)|

That way of building it makes it so that the LED can only ever get current from the inductor.  The battery can **never** directly supply current to the LED.  The LED is reverse biased when looking at the battery - no current can flow.  Only when the battery is disconnected and the coil is the only current source available does the LED light up.

The alternative would have been to build it this way:

|Simple voltage booster alternative|
|----------------------|
|![booster circuit](/assets/voltagebooster/boostercircuit_alternative.png)|

That circuit works as well as the one I originally used in the simple voltage booster, but it could be argued that the battery in all cases directly powers the LED in the alternative circuit.  That's not the case - you and I know better.  But, I was arguing with a very thick headed person.

The alternative circuit seems to be a little brighter than the original because the coil voltage adds to the battery voltage - the booster doesn't have to provide all of the voltage so it lights a little longer on each pulse than in the original circuit.

I thought the clearer argument was worth the loss of  a little brightness.

In any case, said person in the chat room backed down the day **after** I wrote up the simple voltage booster but **before** anyone except I could have seen it.

So call it a victory for truth, even if I didn't win it.  It won itself while I was off playing "Art Attack."



