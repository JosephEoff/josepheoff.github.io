import serial
import time
import math


comport = "/dev/ttyUSB0"
portspeed=1000000
maximumCount = 1023
R_base = float(3300.0)
R_collector = float(1000.0)
V_ref = float(5.0)
Oversampling = int(256)
BaseCurrentSamplingCount = int(256) 


serialport=serial.Serial(comport,portspeed) 
serialport.timeout = 5
time.sleep(2)

def readFromSerialPort():
    valuestring = serialport.readline()
    return valuestring

def getBaseCurrent(DACount):
    IBase = 0.0
    for count in range (0, BaseCurrentSamplingCount):
        serialport.write((str(DACount)+"B"+chr(13)).encode())
        valuestring = readFromSerialPort()
        stringvalues = valuestring.split(('\t').encode())
        VBias = (float(stringvalues[0])/maximumCount) * V_ref / Oversampling
        VBase = (float(stringvalues[1])/maximumCount) * V_ref / Oversampling
        IBase = IBase + math.fabs((VBias-VBase)/R_base) 
        
    return IBase/BaseCurrentSamplingCount

while True:
    daString = input("Base current count: ")
    try:
        DACount = int(daString)
        if DACount<0 or DACount>1023:
            print ("Bad value. Must be between 0 and 1023")
        else:
            basecurrent = getBaseCurrent(DACount)
            basecurrent = basecurrent*1000000 #microamperes
            print("Base current = " + str(basecurrent))
    except Exception as ex:
        print("Exception: " + str(ex))
        
