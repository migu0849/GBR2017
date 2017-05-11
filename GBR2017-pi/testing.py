from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager()
a = ArduinoApi(connection=connection)

a.pinMode(8, a.OUTPUT)
a.pinMode(7, a.OUTPUT)
a.pinMode(13, a.OUTPUT)

def OFFstatus():
    a.digitalWrite(8,0)
    a.digitalWrite(7,0)
    a.digitalWrite(13,0)

valid = True

for i in range (1000):
    OFFstatus()
    choice = int(input("Select color:"))
    if (choice == 1):
        a.digitalWrite(8,1)
        a.digitalWrite(7,1)
        a.digitalWrite(13,1)
        print ("Relays On")
    elif (choice == 2):
        a.digitalWrite(8,0)
        a.digitalWrite(7,0)
        a.digitalWrite(13,0)
        print ("Relays Off")
