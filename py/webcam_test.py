import cv2
import time
import threading

class Camera:
    def __init__(self):
        self.thread = None
        self.frame = None
        
    def getImage(self):
        if self.thread is None:
            self.thread = threading.Thread(target=self.streaming)
            self.thread.start()
            
            while self.frame is None:
                time.sleep(0)
            return self.frame
    
    def streaming(self):
        self.cam = cv2.VideoCapture(0)
        status, self.frame = self.cam.read()
        
        if not status:
            raise Exception("Read error!!")

        self.cam.release()
        time.sleep(0.5)
    
