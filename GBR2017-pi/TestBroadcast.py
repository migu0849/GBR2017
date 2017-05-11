from nanpy import DHT


dhts = [
	DHT(6, DHT.DHT11),
	DHT(7, DHT.DHT11),
	DHT(8, DHT.DHT11)
]

for i, dht, in enumerate(dhts):
	print ("DHT %d" %i)
	print ("Temperature is %.2f degree Celcius" % dht.readTemperature(False))
	print ("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
	print ("Humidity is %.2f %%" % dht.readHumidity())
