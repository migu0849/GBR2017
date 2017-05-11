from nanpy import ArduinoApi
from nanpy import SerialManager
import serial
import struct
import time
from time import sleep
import datetime
from nanpy.sockconnection import SocketManager
from nanpy import DHT
from firebase import firebase



connection = SerialManager()
a = ArduinoApi(connection=connection)

dhts = [DHT(6, DHT.DHT11)]

a.pinMode(0, a.INPUT)
a.pinMode(1, a.INPUT)
a.pinMode(2, a.INPUT)

def BoardStatus():
        print ("Status Broadcast")
        time.sleep(1)
        for i in range(3):
                        DHTSensor()
                        SoilMoistureSensor()
                        time.sleep(0.5)
        

def DHTSensor():
        for i in range(1):
                for i, dht in enumerate(dhts):
                        print ("DHT %d" % i)
                        print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
                        print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
                        print ("Humidity is %.2f %%" % dht.readHumidity())
        time.sleep(2)


def SoilMoistureSensor():
        READING = a.analogRead(0)
        READING2 = a.analogRead(1)
        READING3 = a.analogRead(2)
        print  (READING)
        print  (READING2)
        print  (READING3)

def commandInteraction():
    choice = int(input("What is your command:"))
    if (choice == 1):
        DHTSensor()
    elif (choice == 2):
        SoilMoistureSensor()
    elif (choice == 0):
        for i in range(3):
          BoardStatus()
          time.sleep(2)
        else:
          pass
        sleep(5)


valid = True

while True:
    try:
        BoardStatus()     
    except KeyboardInterrupt:
        commandInteraction()
        time.sleep(5)
        
        




#valid = True
#while(valid):
#        try:
#             BoardStatus()
#        
#        except KeyboardInterrupt:
#                commandInteraction()
#                time.sleep(5)
#                continue
        
