import RPi.GPIO as GPIO
import time
import cv2
import threading
from webcam_test import Camera
from yolov5 import run

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

def setLed(n):
    if n == 0:
        GPIO.output(17,True)
        time.sleep(5)
        GPIO.output(17,False)
    elif n == 1:
        GPIO.output(27,True)
        time.sleep(5)
        GPIO.output(27,False)
    elif n == 2:
        GPIO.output(22,True)
        time.sleep(5)
        GPIO.output(22,False)

if __name__ == '__main__':
    c = Camera()
    frame = c.getImage()
    ans = run(weights= "best.pt", source=frame, conf=0.80)
    setLed(ans)
    c.cam.release()
