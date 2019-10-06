import numpy as np
import cv2

#USB web cam
cap = cv2.VideoCapture(1)

#resolution
cap.set(3, 1920)
cap.set(4,1080)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#frame rate
frame_rate = 10

#video count
video_count = 0

#name of video
video_name = 'output' + str(video_count) + '.avi'

#detected face count
face_count = 0

#total frame count
frame_count = 0


#HASAN - THIS IS THE CODE BLOCK TO OPEN VIDEO

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_name,fourcc, frame_rate, (frame_width,frame_height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #set interrupt here - set to "q" for now
            video_count += 1
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyWindow('frame')
