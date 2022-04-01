---
layout: post
title: "A sewing machine motor speed control - A pulse width modulation driver with PID as a motor speed control"
categories: [blog]
mathjax: false
description: "Some notes on how not to build a motor speed control.  A pulse width modulation driver with back EMF feedback and a PID controller as a motor speed control."
image: /assets/2022-03-07-motorcontrol4/1.jpg
---
Getting closer.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub> 

The last time around, I described a motor controller using feedback from the back EMF of the motor.  The control algorithm was rather naive, so it didn't react well to changes in the load.

I spent a few minutes on a Sunday afternoon a couple of weeks ago putting the [AutoPID](https://www.arduino.cc/reference/en/libraries/autopid/) library in my simple Arduino program.

Getting the PID controller in was trivial.  Tuning it took a couple of hours of twiddling - and I'm still not happy with it.

The end result is much better than with my original, simple controller:

<iframe src="https://player.vimeo.com/video/690091538?h=3c21020795&amp;title=0&amp;byline=0&amp;portrait=0&amp;speed=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="720" height="540" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Motor control with PWM and PID"></iframe>

The controller reacts almost instantly to load changes, and most importantly to **removing** the load.  The controller does its best (within the limits of the power supply) to keep the motor speed constant at what ever speed I set with the potentiometer.

It handles load changes about as well as the [MOSFET source follower](motorcontrol2) I tried out a few weeks ago - with one big improvement.

The MOSFET doesn't get hot when used with the PID/PWM controller like it did in the source follower controller.

That's a large step in the direction I want things to go.

If you look closely at the video, you may notice that I'm using the same circuit as in the [last post.](motorcontrol2)  That's because the only difference this time around was the software.

Here's the current program:

```C++
#include <TimerOne.h>
#include <AutoPID.h>

#define PWM_PIN 9
#define period 50 //20kHz

#define OUTPUT_MIN 0
#define OUTPUT_MAX 1023
#define KP 2
#define KI 10
#define KD 3



double potentiometerValue;
double PWMValue = 0;
double BEMFValue = 0;
int difference = 0;
int highSide = 0;
int lowSide = 0;

AutoPID MotorPID(&BEMFValue, &potentiometerValue, &PWMValue, OUTPUT_MIN, OUTPUT_MAX, KP, KI, KD);

void setup() {
  Serial.begin(1000000);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  pinMode(PWM_PIN, OUTPUT);
  Timer1.initialize(period);
  Timer1.pwm(PWM_PIN,5);
  MotorPID.setBangBang(75);
  MotorPID.setTimeStep(10);
}

void loop() {
  Timer1.pwm(PWM_PIN, 0); //Stop PWM to read the BEMF
  delayMicroseconds(50);
  potentiometerValue = analogRead(A0); 

  highSide = analogRead(A1);

  lowSide = analogRead(A2);
  
  BEMFValue = (BEMFValue + (highSide - lowSide))/2;
  

  MotorPID.run();

  Timer1.pwm(PWM_PIN, (int)PWMValue);
  delayMicroseconds(10000);
}
```
The biggest thing is that I've thrown out my naive algorithm and put a PID controller in its place.  That necessitated some changes to the timing but for the most part it simplified the code drastically.

I don't think the gain values for the proportional, integral and derivative parts are really all that optimal.  They work to some extent, but somebody who knows how to do it would probably have a fit.

I'm still using two ADCs to measure the back EMF from the motor.  That's not going to be manageable in the final circuit.  The final circuit will have to measure anything from 0VDC to over 300VDC.  There are isolated voltage sensors available that could do the job, but I'd need two of them -and I'd still need to periodically stop the PWM signal to measure the back EMF.

What I want is to measure the back EMF using the motor current so that I only need one isolated sensor and don't have to stop the PWM to measure the back EMF.

The next step will be to measure current through the motor to determine the back EMF.  I'll be using a current shunt to do that, so it will still be using two ADCs to measure voltage- but I won't have to stop the PWM to do so.

Not tonight, though.  It's already way to late in the day to be starting something new.

------

I'm going to have to find a better way to tune the PID controller.  All the descriptions I could find were "take a guess, try it out, change it, keep trying until it behaves like you want it."  I really dislike that kind of approach.  Somewhere there has to be a more methodical way to do it.  I'm going to have to find it before I built the real controller for the sewing machine motor.  "Try crap at random for a couple of hours" doesn't sound like a good idea when trying things out means wasting material (cloth, leather, and thread) to do it.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub> 
