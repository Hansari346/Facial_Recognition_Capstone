#updated time stamp from video to frames. 

import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN
import time
import datetime 


def get_timestamp(stamp,delay):
    stamp = stamp[0:-4]
    delay = int(float('%.6f'%(delay)) * 1000000)
    datetime_object = datetime.datetime.strptime(stamp, '%Y-%m-%d %H:%M:%S.%f')
    updated_time = datetime_object+datetime.timedelta(0,0,delay)
    return str(updated_time)


def TakeVideo():
    
    #move video files to "Videos" folder
    os.chdir(VideosPath)
    
    #update video name based on current time in seconds
    video_name = str(datetime.datetime.now()) + '.avi'
    out = cv2.VideoWriter(video_name,fourcc, frame_rate, (frame_width,frame_height))
    
    #turn webcam on while interrupt is not triggered
    while(True):
        ret, frame = cap.read()        
        if ret==True:
            out.write(frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'): #set interrupt here - set to "q" for now
                break
        else:
            break
    #release out and 
    out.release()
    cv2.destroyWindow('frame')


#video to frames function
def FrameCapture(path): 

    #change directory to "Frames" folder. Here the frames will be saved
    os.chdir(FramesPath)

    #run through each video
    for vid in os.listdir(path):
        videoObj = cv2.VideoCapture(path+ "/" + vid) #select desired video 
        success = 1 
        
        delay = 0
        #save each frame
        while success:
            success, frame = videoObj.read()            
            cv2.imwrite(get_timestamp(vid,delay) + '.jpg', frame) #save frame in "Frames" folder
            delay += frame_delay

#Crop faces from frames
def BoundingBox(path, detector):

    #store detected faces in "Faces" folder 
    os.chdir(FacesPath)            

    #for each photo in "Frames" folder
    for img in os.listdir(path):    

        if os.path.getsize(path + "/" + img) != 0:
            image = cv2.imread(path + "/" + img)
            result = detector.detect_faces(image)  #feedforward image to MTCNN network
            if result != []:			   #if no face detected, result = []
                face_count = 0
                for person in result:		   #could be multiple detected faces in one image                    
                    bounding_box = person['box']    
                    x = bounding_box[0]		   #x coordinate of top-left pixel for bounding box
                    y = bounding_box[1]		   #y coordinate of top-left pixel for bounding box
                    width = bounding_box[2]	   #width of bounding box
                    height = bounding_box[3]       #height of bounding box
                    #image_name = float(img[0:-4]) + image_count       
                    cv2.imwrite(img[0:20] + str(int(img[20:26]) + face_count) + '.jpg', image[y:y+height, x:x+width]) #crop the bounding box
                    face_count += 1

#load MTCNN network once to save time
detector = MTCNN()

#Paths used in Project
VideosPath = "/home/hewitt/Desktop/Project/Videos" #folder for videos
FramesPath = "/home/hewitt/Desktop/Project/Frames" #folder for frames
FacesPath = "/home/hewitt/Desktop/Project/Faces" #folder for faces

#USB web cam
cap = cv2.VideoCapture(1)

#set resolution
cap.set(3, 1280)
cap.set(4,720)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#setframe rate
frame_rate = 10
#frame delay for timestamping images
frame_delay = (1 / frame_rate)

cap.set(5,frame_rate)

ret, frame = cap.read()
#cv2.imshow('frame',frame)

#define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Take Video
TakeVideo()

#Turn videos into frames
FrameCapture(VideosPath)

#Run MTCNN network to crop faces from frames
BoundingBox(FramesPath, detector)


#remove cap at end of day
cap.release()




