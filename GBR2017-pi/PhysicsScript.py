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
a.pinMode(6, a.OUTPUT)
a.pinMode(7, a.OUTPUT)
a.pinMode(8, a.OUTPUT)
a.pinMode(9, a.OUTPUT)
a.digitalWrite(2, 1)
a.digitalWrite(3, 1)
a.digitalWrite(4, 1)
a.digitalWrite(5, 1)
a.digitalWrite(6, 1)
a.digitalWrite(7, 1)
a.digitalWrite(8, 1)
a.digitalWrite(9, 1)


def RelayBoardStatus():
	print ("----------------------------------------")
	print ("Relay Status Broadcast")
	time.sleep(1)
	for i in range(500):
			print ("--------------------------------------")
			Relay1()
			Relay2()
			Relay3()
			Relay4()
			Relay5()
			Relay6()
			Relay7()
			Relay8()
			print ("-------------------------------------")
			time.sleep(3)
	
	
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
       
def Relay5():
	if (a.digitalRead(6) == 0):
		print ("Relay 5 is ON!")
		pass
	else:
		print ("Relay 5 is OFF!")
		pass


def Relay6():
	if (a.digitalRead(7) == 0):
		print ("Relay 6 is ON!")
		pass
	else:
		print ("Relay 6 is OFF!")
		pass


def Relay7():
	if (a.digitalRead(8) == 0):
		print ("Relay 7 is ON!")
		pass
	else:
		print ("Relay 7 is OFF!")
		pass


def Relay8():
	if (a.digitalRead(9) == 0):
		print ("Relay 8 is ON!")
		pass
	else:
		print ("Relay 8 is OFF!")
		pass  


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
        	print ("Relay 4 is OFF")
        	sleep(0.2)
	elif (choice == 5):
       	    	a.digitalWrite(6, 0)
       	    	print ("Relay 1 is ON")
       	    	sleep(0.2)
   	elif (choice == 55):
   	    	a.digitalWrite(6, 1)
      	    	print ("Relay 1 is OFF")
            	sleep(0.2)
        elif (choice == 6):
            	a.digitalWrite(7, 0)
            	print ("Relay 2 is ON")
            	sleep(0.2)
   	elif (choice == 66):
            	a.digitalWrite(7, 1)
            	print ("Relay 2 is OFF")
            	sleep(0.2)
       	elif (choice == 7):
        	a.digitalWrite(8, 0)
        	print ("Relay 3 is ON")
        	sleep(0.2)
        elif (choice == 77):
     	        a.digitalWrite(8, 1)
        	print ("Relay 3 is OFF")
        	sleep(0.2)
    	elif (choice == 8):
        	a.digitalWrite(9, 0)
        	print ("Relay 4 is ON")
        	sleep(0.2)
        elif (choice == 88):
        	a.digitalWrite(9, 1)
        	print ("Relay 4 is OFF")
        	sleep(0.2)				
        elif (choice == 123):
		a.digitalWrite(2, 0)
		a.digitalWrite(3, 0)
		a.digitalWrite(4, 0)
		a.digitalWrite(5, 0)
		a.digitalWrite(6, 0)
		a.digitalWrite(7, 0)
		a.digitalWrite(8, 0)
		a.digitalWrite(9, 0)
		print ("All Relays are ON")
	elif (choice == 321):
		a.digitalWrite(2, 1)
		a.digitalWrite(3, 1)
		a.digitalWrite(4, 1)
		a.digitalWrite(5, 1)
		a.digitalWrite(6, 1)
		a.digitalWrite(7, 1)
		a.digitalWrite(8, 1)
		a.digitalWrite(9, 1)
		print ("All Relays are OFF")
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
		RelayBoardStatus()
	
	except KeyboardInterrupt:
		commandInteraction()
		time.sleep(5)
		continue
	
