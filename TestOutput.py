#import modules
import time
import RPi.GPIO as GPIO

#pin definitions
ledR = 2
ledG = 3
ledB = 5

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledG, GPIO.OUT)
GPIO.setup(ledB, GPIO.OUT)

#set initial LED states
GPIO.output(ledR, 1)
GPIO.output(ledG, 1)
GPIO.output(ledB, 1)

#main loop
try:
    while 1:
        tempStore = open("/sys/bus/w1/devices/28-0315902106ff/w1_slave")	#sample DEVICE ID, change to current using 
        data = tempStore.read()
        tempStore.close()
        tempData = data.split("\n")[1].split(" ")[9]
        temperature = float(tempData[2:])
        temperature = temperature/1000
        print temperature

        if temperature < 20:	#Threshold of too cold temp
            GPIO.output(ledR, 1)
            GPIO.output(ledG, 1)
            GPIO.output(ledB, 0)

        if temperature > 20 and temperature < 24:	#Threshold of comfortable temp
            GPIO.output(ledR, 1)
            GPIO.output(ledG, 0)
            GPIO.output(ledB, 1)

        if temperature > 24:	#Threshold of too hot temp
            GPIO.output(ledR, 0)
            GPIO.output(ledG, 1)
            GPIO.output(ledB, 1)

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print ("Program Exited Cleanly"