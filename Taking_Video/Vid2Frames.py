
#Program to read video and extract frames

import cv2
import os

os.chdir('Frames')

def FrameCapture(path):
    videoObj = cv2.VideoCapture(path)
    count = 0
    success = 1

    while success:
        success, image = videoObj.read()
        cv2.imwrite("frame%d.jpg" % count, image)
        count += 1

if __name__ == '__main__':

    FrameCapture("/home/hewitt/Desktop/Project/Videos/output0.avi")
