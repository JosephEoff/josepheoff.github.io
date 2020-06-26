---
layout: post
title: "Soil moisture monitoring in a flower garden - an infrastucture for testing my ideas"
categories: [blog]
mathjax: false
image: /assets/2020-06-26-soilmoisture1/firstsetup.jpg
---    
A garden from the inside out - first the servers, then the yard work.


As I mentioned before, I plan to use some ESP32s, an MQTT server, and some custom software based on Django to collect soil moisture data from my flower garden.

Since I'll have to write the Django software, and I expect to have to modify some available ESP32 software, the most reasonable place to start is with the MQTT server.  There are several MQTT servers out there, and client software for simple monitoring.  It's just a question picking a set and installing them in a server somewhere.

I have a Xen host here at home that runs a small server - DNS, DHCP, mail, web.  I had planned to install a second virtual machine on the Xen host and use that as my MQTT playground.  It turned out that the host machine itself is too small - not enough RAM.  I wasted many hours trying to make it go.  No luck.

I've just gone ahead and installed the [Eclipse Mosquitto MQTT server](https://mosquitto.org/) on the computer I use for all my hobby development stuff.  While I was at it, I installed the [Eclipse Paho](http://www.eclipse.org/paho/) MQTT client for Python.

A quick peek at some tutorials, and I verified that my MQTT server is running and passing messages.

Now for the ESP32.

I decided I'd try to use the [OpenMQTT Gateway](https://github.com/1technophile/OpenMQTTGateway) on the ESP32 to connect to my soil moisture monitors.  I cloned the current version from the github repository, and followed the [instructions](https://docs.openmqttgateway.com/upload/arduino-ide.html) for the Arduino IDE.  Those instructions also include links to instructions on installing the needed support for the ESP32 in the Arduino IDE.

Unfortunately, my Arduino IDE was too old.  I had version 1.6.13, and the support for partition schemes didn't show up until version 1.8 something.

There wasn't a newer version available for OpenSuse 15.0, so I upgraded to OpenSuse 15.1.  That was slightly painful - I ended up upgrading to 15.1, downgrading to 15.0, then upgrading to 15.1 again.

There was an unofficial Arduino 1.8 something available for OpenSuse 15.1, so I installed that and thought I could get on with things.

Nope.

There followed many days of trying to debug errors in compiling, and much pulling of hair and gnashing of teeth.

In the end, I found an obscure note somewhere that explained the behaviour I was seeing.  It came down to something wrong in the tool chain for the ESP32.  The unofficial OpenSuse Arduino package was broken.

OK, enough is enough.  I downloaded the Arduino Linux installer from the [Arduino site.](https://www.arduino.cc/en/Main/Donate) and installed that.  I try to avoid unpackaged software, but I'd really had enough monkeying around.

The Arduino Linux installer put a complete IDE and toolchain in my home folder - and it works.  

Two weeks after I started this, I could finally compile an ESP32 program and flash it into a module.

Whee!

Along the way, I changed from using OpenMQTT Gateway to the much simpler [flora](https://github.com/sidddy/flora) software.  It doesn't have all the bells and whistles of the OpenMQTT Gateway, but on the other hand I have some bells and whistles of my own to implement and that'll be easier when starting from a simpler base.

At any rate, I now have a small test setup running.

It's made of the following components:

1. A NodeMCU ESP32S running the flora firmware.
2. A simple MQTT client in python that just prints out all received messages.
3. A Mosquitto MQTT server installed on my computer rather than on a separate server machine.
4. An OEM relabeled (cheaper) Xiaomi MiFlora sensor.

It all looks like this:

|Not my garden|
|-------------|
|![Not my garden](/assets/2020-06-26-soilmoisture1/firstsetup.jpg)|

On screen to the left is the output of the Mosquitto server process.

On screen to the right is the MQTT listener output.

Hanging by the screen on the left is the ESP32.

Standing in front of the monitor is a white thingy - that's the sensor itself.

All together, they don't do much.  They do functionally represent all the components I'm going to need before this is over, though.

That's all for today.  It took far too long to reach this point, so I'm going to give it a rest.

