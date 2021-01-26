import cv2
import numpy as np

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cap.read()
        # print(frame.shape)
        print(ret)
 
        # edges = cv2.Canny(frame, 100, 200)        
        
        cv2.imshow("Camera USB 2.0", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("{}.png".format(count), frame)
            count += 1
