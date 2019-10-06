import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN
import time


def TakeVideo():
    
    #move video files to "Videos" folder
    os.chdir(VideosPath)
    
    #update video name based on time
    video_name = format(int(round(time.time() * 100000))) + '.avi'
    out = cv2.VideoWriter(video_name,fourcc, frame_rate, (frame_width,frame_height))

    #turn webcam on while interrupt is not triggered
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): #set interrupt here - set to "q" for now
                break
        else:
            break

    #release everything if job is finished
    cap.release()
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

        #save each frame
        while success:
            success, frame = videoObj.read()
            cv2.imwrite(format(int(round(time.time() * 100000))) + '.jpg', frame) #save frame in "Frames" folder


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
                for person in result:		   #could be multiple detected faces in one image
                    bounding_box = person['box']    
                    x = bounding_box[0]		   #x coordinate of top-left pixel for bounding box
                    y = bounding_box[1]		   #y coordinate of top-left pixel for bounding box
                    width = bounding_box[2]	   #width of bounding box
                    height = bounding_box[3]       #height of bounding box       
                    cv2.imwrite(format(int(round(time.time() * 100000))) + '.jpg', image[y:y+height, x:x+width]) #crop the bounding box


#load MTCNN network once to save time
detector = MTCNN()

#Paths used in Project
VideosPath = "/home/hewitt/Desktop/Project/Videos" #folder for videos
FramesPath = "/home/hewitt/Desktop/Project/Frames" #folder for frames
FacesPath = "/home/hewitt/Desktop/Project/Faces" #folder for faces

#USB web cam
cap = cv2.VideoCapture(1)

#resolution
cap.set(3, 1280)
cap.set(4,720)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#frame rate
frame_rate = 30

cap.set(5,frame_rate)

#define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')


#Take Video
TakeVideo()

#Turn videos into frames
FrameCapture(VideosPath)

#Run MTCNN network to crop faces from frames
BoundingBox(FramesPath, detector)









