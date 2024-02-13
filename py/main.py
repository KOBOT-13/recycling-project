import time
import cv2
import threading
from webcam_test import Camera
from yolov5 import detect


def run():
    ans = detect.run(weights= "py/best.pt", source=0, conf_thres=0.5)
    

if __name__ == '__main__':
    ans = detect.run(weights= "py/best.pt", source=0, conf_thres=0.5)
    
