---
layout: post
title: "Voltage multipliers - Part 2 The Greinacher voltage doubler"
categories: [blog]
--- 

Getting better.

<sub>[Voltage multiplier experiments - Table of Contents](2-voltagemultiplier-toc)</sub>

The output of the Villard circuit is higher than the output of a simple rectifier, but it doesn't much resemble DC.

The [Greinacher doubler](https://en.wikipedia.org/wiki/Voltage_doubler#Greinacher_circuit) improves greatly on the Villard.  It follows the Villard doubler with another diode and a capacitor.  This forms a peak detector, and smooths the extreme fluctuations of the Villard into something more resembling the output of a simple rectifier - but, the voltage is **still** much higher.

This is what a Greinacher doubler looks like:

|Greinacher voltage doubler|
|--------------------------|
|![Greinacher voltage doubler.](/assets/voltage_multiplier/greinacherdoubler.png)|

If you refer back to the schematic diagrams in [part 1 of this series, ](diode-capacitors-volts-pt1) you can see how a Villard doubler is combined with a simple rectifier to produce the Greinacher design.  Really, the Greinacher is just a Villard followed by a simple rectifier.

Here are the waveforms and voltages for a Greinacher doubler:

|AC voltage|DC voltage|
|----------|----------|
|![Rectifier voltage AC](/assets/voltage_multiplier/greinacher_AC.png)|![Rectifier voltage DC](/assets/voltage_multiplier/greinacher_DC.png)|

That is **much** better than the Villard:

![Rectifier voltage DC](/assets/voltage_multiplier/villard_DC.png)

The peak voltage isn't as high, but it is a much cleaner approximation of DC.

The Villard adds a DC component of 1/2 the peak voltage to the AC.  Adding that second diode and capacitor (mostly) removes the AC and adds another 2/3 (strictly, 2/Pi) of the peak AC voltage to the DC from the Villard.

The AC is 33V peak to peak.  Half of that is 16.5.  2/Pi of 33V is 21V.  16.5V + 21V is 27.5V.  The measured voltage is 24.3V.  Add in 2V for the voltage drop on the diodes to get 26.3.  That's pretty close to the approximation.

That's pretty good.  We've gotten 24.3VDC out of 33VAC.  That's a bit more than double the DC that a simple rectifier can make out of AC.

Now, what do you do if you need even **more** voltage?

You turn to a [Cockcroft-Walton](https://en.wikipedia.org/wiki/Cockcroft%E2%80%93Walton_generator) multiplier.

I'll describe that the next time around.

[**Next**](diode-capacitors-volts-pt3)

<sub>[Voltage multiplier experiments - Table of Contents](2-voltagemultiplier-toc)</sub>
