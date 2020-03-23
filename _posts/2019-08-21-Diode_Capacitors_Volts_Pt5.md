---
layout: post
title: "Voltage multipliers - Part 5 Tying it all together"
categories: [blog]
---  

Haven't we met before?

<sub>[Voltage multiplier experiments - Table of contents](2-voltagemultiplier-toc)</sub>

After going through a couple of simple voltage doublers and then the more complicated full wave Cockcroft-Walton multiplier, I'm going to back down to the simpler half wave Cockcroft-Walton multiplier.  From there, I'll go into how they are all related.

I introduced the Cockcroft-Walton multiplier because it makes the most sense to me.  It is based on an easily recognized circuit, and it is fairly obvious what it does.  Now I'm going to go to the simpler (but for me less obvious) half wave Cockcroft-Walton multiplier.

I'll just modify the drawing I've been using.

Here are the circuits:

|Full wave Cockcroft-Walton multiplier|Half wave Cockcroft-Walton multiplier|
|-------------------------------------|-------------------------------------|
|![Full wave Cockcroft-Walton multiplier](/assets/voltage_multiplier/cockcroftwalton3.png)|![Half wave Cockcroft-Walton multiplier](/assets/voltage_multiplier/cockcroftwalton_halfwave.png)|

The half wave version is almost literally half of the full wave version.  Just strip off the lower row of diodes, and you're pretty much done.

Now, let's have a look at the voltages:

|Half wave Cockcroft-Walton multiplier DC stage 1|
|-----------------------------------------|
|![Half wave Cockcroft-Walton multiplier](/assets/voltage_multiplier/cockcroftwalton_halfwave1_DC.png)|


The half wave Cockcroft-Walton multiplier works about like the full wave version does.  

No.  Wait.

That's a single stage of the halfwave Cockcroft-Walton, and it's already **doubled** the voltage.

There's 26V DC, or 24VRMS, already there at the first stage.  The full wave Cockcroft-Walton multiplier required **two** stages to do that.

That's because the full wave Cockcroft-Walton stage is a full wave rectifier.  The diodes can't play with the capacitors to make a clamp.

Back to the circuits.

If you look at that half wave Cockcroft-Walton circuit closely, it might seem familiar - at least in parts.

Having gone through the Villard and the Greinacher voltage doublers, I find each stage of the Cockcroft-Walton half wave multiplier **very** familiar.

Let's have a look:

|Single half wave Cockcroft-Walton stage|Greinacher voltage doubler|
|-------------------------------------|-------------------------------------|
|![Single half wave Cockcroft-Walton stage](/assets/voltage_multiplier/cockcroftwalton_halfwave_stage.png)|![Greinacher voltage doubler](/assets/voltage_multiplier/greinacherdoubler.png)|

Squint a little and maybe cock your head, and I'm sure you'll see it.

A half wave Cockcroft-Walton voltage multiplier is nothing but a bunch of Greinacher doublers strung together.

That whole realization is the reason I've been drawing the full wave version in the diamond form.  That's the thing that made clear to me how they are all related.

If I draw the Cockcroft-Walton the way you have to do it in KiCad (and other schematic capture programs that don't allow 45 degree angles) then that relationship is obscured.

With the point made, I'm going to switch back to drawing schematics in KiCad.

Here's a half wave Cockcroft-Walton multiplier drawn in KiCAD:

|Half wave Cockcroft-Walton multiplier|
|-------------------------------------|
|![Full wave Cockcroft-Walton multiplier](/assets/voltage_multiplier/cockcroftwalton3_kicad.png)|

Having gone through the development of the various multipliers and doublers, I can now see the Greinacher and the Villard in there.  

Next time around, I'm going to have a look at why the voltage drops so horribly on the higher stages.

[**Next**](diode-capacitors-volts-pt6)

<sub>[Voltage multiplier experiments - Table of contents](2-voltagemultiplier-toc)</sub>
