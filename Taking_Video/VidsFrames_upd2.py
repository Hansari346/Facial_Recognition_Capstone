import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN
import time

#video to frames function
def FrameCapture(path): 
    videoObj = cv2.VideoCapture(path) #select desired video 
    global frame_count 
    success = 1
    detector = MTCNN() #load MTCNN network 

    while success:
        success, frame = videoObj.read()
        cv2.imwrite("frame%d.jpg" % frame_count, frame) #save frame in "Frames" folder
        BoundingBox(frame_count,detector) #call bounding box function to look for faces, then crop	
        frame_count += 1

#Crop faces from frames
def BoundingBox(frame_count,detector):
    
    global face_count
    if os.path.getsize("/home/hewitt/Desktop/Project/Frames/frame%d.jpg" %frame_count) != 0:
        image = cv2.imread("frame%d.jpg" % frame_count)
        result = detector.detect_faces(image) #feedforward image to MTCNN network
        if result != []:			#if no face detected, result = []
            for person in result:		#could be multiple faces in one image
                bounding_box = person['box']    
                x = bounding_box[0]		#x coordinate of top-left pixel for bounding box
                y = bounding_box[1]		#y coordinate of top-left pixel for bounding box
                width = bounding_box[2]		#width of bounding box
                height = bounding_box[3]        #height of bounding box
                os.chdir("/home/hewitt/Desktop/Project/Faces") #store detected faces in "Faces" folder
                cv2.imwrite("face%d.jpg" %face_count, image[y:y+height, x:x+width]) #crop bounding box          
                face_count += 1
    os.chdir("/home/hewitt/Desktop/Project/Frames") #go back to "Frames" folder

#move video files to "Videos" folder
os.chdir('Videos')

#USB web cam
cap = cv2.VideoCapture(1)

#resolution
cap.set(3, 1280)
cap.set(4,720)
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

#define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_name,fourcc, frame_rate, (frame_width,frame_height))

#turn webcam on while interrupt is not triggered
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

#release everything if job is finished
cap.release()
out.release()
cv2.destroyWindow('frame')

#change directory to "Frames" folder. Here the frames will be saved
os.chdir("/home/hewitt/Desktop/Project/Frames")

FrameCapture("/home/hewitt/Desktop/Project/Videos/" + video_name)







