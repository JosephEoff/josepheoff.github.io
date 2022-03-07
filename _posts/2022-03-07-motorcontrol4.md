---
layout: post
title: "A sewing machine motor speed control - A pulse width modulation driver with feedback as a motor speed control"
categories: [blog]
mathjax: false
description: "Some notes on how not to build a motor speed control.  A pulse width modulation driver with back EMF feedback as a motor speed control."
image: /assets/2022-03-07-motorcontrol4/1.jpg
---
Moving forwards again.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub> 

The pulse width modulation (PWM) scheme I introduced in my last post is an improvement over the previous variable resistor type controllers, but is is still far from good enough.  The PWM setup has no feedback - it regulates power to the motor, not motor speed.

Since I'm using an Arduino Nano with eight analog inputs, feedback is just a matter of a couple of wires and some more code.

First the hardware:

|Expanded PWM circuit|
|--------------------|
|![Expanded PWM circuit](/assets/2022-03-07-motorcontrol4/1.jpg)|

The most obvious difference is that I've added connections to two analog inputs.  One of them measures the DC voltage to the motor, while the other measures the DC voltage after the motor.

Motors have this thing called [back electromotive force (back EMF.)](https://en.wikipedia.org/wiki/Counter-electromotive_force)

It is common knowledge that motors act like generators when driven mechanically.  What most people don't realize is that a motor is **simultaneously** a generator.  When you drive a motor to make it turn, its own rotation generates a current in its coils that opposes the rotation.  That's back EMF.

Back EMF is zero when the motor isn't moving.  When the motor reaches full speed, the back EMF is as high as the driving voltage.

My software is driving the motor with pulse width modulation (PWM.)  The pulsing voltage applied to the motor means I can't measure the back EMF directly - if I just measured it, I'd get a pulsing mess.

To accurately measure the back EMF, the program stops the PWM for a very short time (about the length of one PWM pulse) and measures the voltage across the motor - it measures the voltage at both ends of the motor and takes the difference.  The voltage across the motor in the brief pause is the back EMF.

Since back EMF is directly proportional to the motor speed, I can use it to see if the motor is speeding up or slowing down.  When the back EMF drops, the motor is slowing down.  When the back EMF goes up, the motor is speeding up.

The program in the Nano watches the back EMF and compares it to the voltage set with the potentiometer.  It tries to maintain the back EMF at the same voltage as the potentiometer input by driving the PWM width up and down.  If the motor is too slow, the pulses get wider.  If the motor is too fast, the pulses get narrower.

It works pretty well.  It is very difficult to grab the shaft and make the motor stop.

Here's the code:

```C++
#include <TimerOne.h>

#define PWM_PIN 9
#define period 50 //20kHz
#define maximumStepSize 3


int potentiometerValue;
int PWMValue = 0;
int BEMFValue =0;
int difference = 0;
int stepSize = 3;
int highSide = 0;
int lowSide = 0;


void setup() {
  pinMode(PWM_PIN, OUTPUT);
  Timer1.initialize(period);
  Timer1.pwm(PWM_PIN,5);
}

void loop() {
  Timer1.pwm(PWM_PIN, 0); //Stop PWM to read the BEMF
  delayMicroseconds(60);
  potentiometerValue = analogRead(A0); 

  highSide = analogRead(A1);

  lowSide = analogRead(A2);
  
  BEMFValue = highSide - lowSide;

  difference = potentiometerValue - BEMFValue;
  stepSize = 0;
  if (difference >0){
    stepSize = maximumStepSize;
  }
  if (difference<0){
    stepSize = -maximumStepSize;
  }
  
  PWMValue = PWMValue + stepSize ;

  if (PWMValue >1023){
    PWMValue = 1023;
  }
  if (PWMValue<0){
    PWMValue = 0;
  }
  Timer1.pwm(PWM_PIN, PWMValue);
  delayMicroseconds(3000);
}
```

Not much to it.

While it is much better than any of the options up to now, it **still** isn't good enough.

The algorithm that tries to match the real speed to the set speed is rather naive.  It works, but it could be **lots** better.

One of the most obvious things about this naive controller is that it takes a while to get things under control again when there's a sudden change in the load.  This is most noticeable when releasing a heavy load.

<iframe src="https://player.vimeo.com/video/685612141?h=97ac9ece20&amp;title=0&amp;byline=0&amp;portrait=0&amp;speed=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="480" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Pulse width modulation with back EMF feedback"></iframe>

You can hear the motor trying to maintain its speed as I press on the shaft.  The little power suppy can't deliver enough current for the motor to maintain its speed against the load, but it does its best.

When I let go of the motor shaft, the motor speeds up drastically before dropping back down to its set speed.

That overshoot is caused by the naive method I'm using to adjust the PWM width.  It can't react quickly to sudden changes.

To make that work properly, I need to implement a [proportional, integral, derivative (PID) controller.](https://en.wikipedia.org/wiki/PID_controller)

PID controllers can adapt quickly to sudden changes while also maintaining precise control when the changes are smaller.  I'm not so much interested in precise control as in the ability to handle sudden changes.

I could try to implement a PID controller in software myself, but since this project is all about the hardware, I'll use something like the [Arduino AutoPID](https://github.com/r-downing/AutoPID) library.

The next post will be about a PWM controller with back EMF feedback and a PID controller.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub> 
