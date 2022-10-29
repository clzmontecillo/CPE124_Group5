import Adafruit_DHT
import sqlite3

# Create your views here.

con = sqlite3.connect("db.sqlite3")
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class DataInsert:
    
    def insert(self):
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

            
            if humidity is not None and temperature is not None:
                
                cursor = con.cursor()
                query = "update app_sensor set temperature = ?, humidity = ?"
                val = (round(temperature,2), round(humidity,2))
                count = cursor.execute(query,val)
                con.commit()

                print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
                return None
            else:
                print("Failed to retrieve data from humidity sensor")
                return None


