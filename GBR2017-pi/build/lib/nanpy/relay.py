from nanpy import (ArduinoApi, SerialManager)
from nanpy import DHT

connection = SerialManager(device='/dev/ttyACM0')
a = ArduinoApi(connection=connection)

dhts = [
    DHT(10, DHT.DHT11)
]

for i, dht in enumerate(dhts):
    print("DHT %d" % i)
    print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
    print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
    print("Humidity is %.2f %%" % dht.readHumidity())
