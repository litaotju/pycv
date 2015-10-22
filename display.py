# -*-coding:utf-8 -*- #

import os
import cv2
import numpy as np

def displayImg(filename):
    img = cv2.imread(filename)
    name = os.path.splitext(filename)
    cv2.namedWindow(name[0])
    cv2.imshow(name[0], img)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyWindow(name[0])
    return None

def displayVideo(filename):
    cap = cv2.VideoCapture(filename)
    while(cap.isOpened()):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow(filename, rgb)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return None