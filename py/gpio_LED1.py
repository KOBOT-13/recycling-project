import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

while True:
    LEDnum = int(input())
    if LEDnum == 0:
        GPIO.setup(17,GPIO.OUT)
        GPIO.output(17,True)
        time.sleep(5)
        GPIO.output(17,False)
    elif LEDnum == 1:
        GPIO.setup(27,GPIO.OUT)
        GPIO.output(27,True)
        time.sleep(5)
        GPIO.output(27,False)
    elif LEDnum == 2:
        GPIO.setup(22,GPIO.OUT)
        GPIO.output(22,True)
        time.sleep(5)
        GPIO.output(22,False)
    elif LEDnum == 999:
        break
    else:
        print("Please enter one of the three numbers: 0,1,2 (+ 999 is break)")

    
