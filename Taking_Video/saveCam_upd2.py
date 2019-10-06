import numpy as np
import cv2
import os
from datetime import datetime

#move video files to "Videos" folder
os.chdir('Videos')

#USB web cam
cap = cv2.VideoCapture(1)

#set resolution
cap.set(3, 1920)
cap.set(4,1080)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#set frame rate
frame_rate = 60

#set video count
video_count = 0

#set name of video
video_name = 'output' + str(video_count) + '.avi'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#creates file
#out = cv2.VideoWriter(video_name,fourcc, frame_rate, (frame_width,frame_height))

DT = datetime.now()
time_in_seconds = DT.second + DT.minute * 60 + DT.hour * 3600

#while(True):

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
	
	
 #          out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #place timing statement here
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()










