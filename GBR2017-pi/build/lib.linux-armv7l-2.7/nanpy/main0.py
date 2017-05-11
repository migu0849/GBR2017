from nanpy import (ArduinoApi, SerialManager)
import serial
import struct
import time
import datetime

PIN = A0

connection = SerialManager(device='/dev/ttyACM0')
Board1 = ArduinoApi(connection=connection)

Board1.pinMode(PIN, Board1.INPUT)

print "Connecting to Arduino...."
time.sleep(1)
print "Handshake:Good"

def outputResponse (command):
    value = Board1.analogRead(A0)
    return value()


def inputCommand ():
    return raw_input('what is your command-->')

while 1:
    command = inputCommand()
    result = outputResponse(command)
    if result == 0:
        Board1.digitalWrite(A0, Board1.HIGH)
        print "Relay 1 is On"
    else :
        print "Relay 1 is already On"
