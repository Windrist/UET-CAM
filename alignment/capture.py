from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

if __name__ == "__main__":
    # Camera Pi configuration
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 60
    # camera.rotation = 180
    rawCapture = PiRGBArray(camera, size=camera.resolution)
    
    time.sleep(0.1)
    count = 0
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Capture", image)
        key =  cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite('image/{}.png'.format(count), image)
            count += 1

