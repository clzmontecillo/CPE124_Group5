import Adafruit_DHT
import sqlite3
import time

from gpiozero import LED



# Create your views here.

con = sqlite3.connect("db.sqlite3")
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class DataInsert:
    led = LED(17)
    
    def selectQuery(self):
        query = "select * from app_thresh where id = 1"
        cursor = con.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        
        for x in result:
            return str(x[1]), str(x[2])
        return None
    
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
                
                
                a, b = self.selectQuery()
                print(a, b, "is the humid and temp")
                try:
                    
                    if round(humidity,2) > int(b) and round(temperature,2) > int(a):
                        self.led.on()
                    else:
                        self.led.off()
                except:
                    cursor = con.cursor()
                    query = "update app_sensor set temperature = ?, humidity = ?"
                    val = (round(temperature,2), round(humidity,2))
                    count = cursor.execute(35,90)
                    con.commit()                    
                    
           
              
                return None
            else:
                print("Failed to retrieve data from humidity sensor")
                return None


