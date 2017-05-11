from nanpy import ArduinoApi
from nanpy import SerialManager
import serial
import struct
import time
from time import sleep
import datetime
from nanpy.sockconnection import SocketManager
from nanpy import DHT



connection = SerialManager()
a = ArduinoApi(connection=connection)


a.pinMode(2, a.OUTPUT)
a.pinMode(3, a.OUTPUT)
a.pinMode(4, a.OUTPUT)
a.pinMode(5, a.OUTPUT)
a.digitalWrite(2, 1)
a.digitalWrite(3, 1)
a.digitalWrite(4, 1)
a.digitalWrite(5, 1)

dhts = [DHT(6, DHT.DHT11)]

a.pinMode(0, a.INPUT)
a.pinMode(1, a.INPUT)
a.pinMode(2, a.INPUT)

def BoardStatus():
	print ("Status Broadcast")
	time.sleep(1)
	for i in range(500):
			Relay1()
			Relay2()
			Relay3()
			Relay4()
			DHTSensor()
			SoilMoistureSensor()
			time.sleep(0.5)
	
def Relay1():
	if (a.digitalRead(2) == 0):
		print ("Relay 1 is ON!")
		pass
	else:
		print ("Relay 1 is OFF!")
		pass


def Relay2():
	if (a.digitalRead(3) == 0):
		print ("Relay 2 is ON!")
		pass
	else:
		print ("Relay 2 is OFF!")
		pass


def Relay3():
	if (a.digitalRead(4) == 0):
		print ("Relay 3 is ON!")
		pass
	else:
		print ("Relay 3 is OFF!")
		pass


def Relay4():
	if (a.digitalRead(5) == 0):
		print ("Relay 4 is ON!")
		pass
	else:
		print ("Relay 4 is OFF!")
		pass  
       

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
	DATA = READING 
	DATA2 = READING2 
	DATA3 = READING3 
	print  DATA
	print  DATA2
	print  DATA3

	
		



def commandInteraction():    
    	choice = int(input("What is your command:"))
    	if (choice == 1):
       	    	a.digitalWrite(2, 0)
       	    	print ("Relay 1 is ON")
       	    	sleep(0.2)
   	elif (choice == 11):
   	    	a.digitalWrite(2, 1)
      	    	print ("Relay 1 is OFF")
            	sleep(0.2)
        elif (choice == 2):
            	a.digitalWrite(3, 0)
            	print ("Relay 2 is ON")
            	sleep(0.2)
   	elif (choice == 22):
            	a.digitalWrite(3, 1)
            	print ("Relay 2 is OFF")
            	sleep(0.2)
       	elif (choice == 3):
        	a.digitalWrite(4, 0)
        	print ("Relay 3 is ON")
        	sleep(0.2)
        elif (choice == 33):
     	        a.digitalWrite(4, 1)
        	print ("Relay 3 is OFF")
        	sleep(0.2)
    	elif (choice == 4):
        	a.digitalWrite(5, 0)
        	print ("Relay 4 is ON")
        	sleep(0.2)
        elif (choice == 44):
        	a.digitalWrite(5, 1)
        	print ("Relay 4 is ON")
        	sleep(0.2)
        elif (choice == 5):
		DHTSensor()
	elif (choice == 6):
		SoilMoistureSensor()
        elif (choice == 0):
		for i in range(3):
	     	  BoardStatus()
	          time.sleep(2)
    	else:
		return
		sleep(5)


valid = True


while(1):
	try:
		BoardStatus()
	
	except KeyboardInterrupt:
		commandInteraction()
		time.sleep(5)
		continue
	
