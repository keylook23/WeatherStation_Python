import sys
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import mysql.connector

sensor = BMP085.BMP085()
humidity, temperature = Adafruit_DHT.read_retry(11, 17)

print('Temp1 = {0:0.2f}*C'.format(temperature, humidity))
print('Humidity = {1:0.2f}%'.format(temperature, humidity))
print('Temp2 = {0:0.2f}*C'.format(sensor.read_temperature()))
print('Pressure = {0:0.2f}hPa'.format(sensor.read_pressure()/100))

mydb = mysql.connector.connect(
	host = "localhost",
	user = "pi",
	passwd = "zaq12wsx",
	database = "weatherstation",
	)
	
mycursor = mydb.cursor()

insert_bmp = "INSERT INTO results (sensor, temperature, pressure) VALUES (%s, %s, %s)"
insert_dht = "INSERT INTO results (sensor, temperature, humidity) VALUES (%s, %s, %s)"

read_bmp = ('bmp', sensor.read_temperature(), sensor.read_pressure()/100)
read_dht = ('dht', temperature, humidity)

mycursor.execute(insert_bmp, read_bmp)
mycursor.execute(insert_dht, read_dht)

mydb.commit()
