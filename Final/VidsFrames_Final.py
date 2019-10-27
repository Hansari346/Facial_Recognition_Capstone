#updated time stamp from video to frames. 

import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN
import time
import datetime 
from i2c_trigger_Final import *
import shutil


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
frame_rate = 15
#frame delay for timestamping images
frame_delay = (1 / frame_rate)

cap.set(5,frame_rate)

#ret, frame = cap.read()
#cv2.imshow('frame',frame)

#define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')


def get_timestamp(stamp,delay):
    stamp = stamp[0:-4]
    delay = int(float('%.6f'%(delay)) * 1000000)
    datetime_object = datetime.datetime.strptime(stamp, '%Y-%m-%d %H:%M:%S.%f')
    updated_time = datetime_object+datetime.timedelta(0,0,delay)
    return str(updated_time)


def TakeVideo():
    count = 20
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
            cv2.imshow('frame',frame)
            if Thermal_Values() == False:
                count -= 1
            else:
                count = 20
            if cv2.waitKey(1) and count <= 0:
                break
        else:
            break
    #release out and 
    out.release()
    cv2.destroyWindow('frame')

#video to frames function
def FrameCapture(desired_path): 

    count = 5
    #save to "Frames" folder 
    os.chdir(desired_path)
    #turn webcam on while interrupt is not triggered

#    while(cap.isOpened()):
    while (count >= 0):
        ret, frame = cap.read() #takes approximately 80 milliseconds
        if ret==True:

 #           cv2.imshow('frame',frame)
            cv2.imwrite(str(datetime.datetime.now()) + '.jpg', frame)
            count -= 1
            if count <= 0: #set interrupt here - set to "q" for now
                break
        else:
            break
#    cap.release()
#    cap.destroyWindow('frame')

#video to frames function
def Vids2Frames(path): 

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
def BoundingBox(picture_path, desired_path, detector):

    #store detected faces in "Faces" folder 
    os.chdir(desired_path)            

    #for each photo in "Frames" folder
    for img in os.listdir(picture_path):    

        if os.path.getsize(picture_path + "/" + img) != 0:
            image = cv2.imread(picture_path + "/" + img)
            result = detector.detect_faces(image)  #feedforward image to MTCNN network
            if result != []:			   #if no face detected, result = []
                face_count = 0
                for person in result:		   #could be multiple detected faces in one image                    
                    bounding_box = person['box']    
                    x = bounding_box[0]		   #x coordinate of top-left pixel for bounding box
                    y = bounding_box[1]		   #y coordinate of top-left pixel for bounding box
                    width = bounding_box[2]	   #width of bounding box
                    height = bounding_box[3]       #height of bounding box
                    image_name = img[0:20] + str(int(img[20:26])+face_count) + '.jpg'
                    cv2.imwrite(image_name, image[y:y+height, x:x+width]) #crop the bounding box
                    #cv2.imwrite(img, image[y:y+height, x:x+width])
                    face_count += 1


def MoveImages(currentPath1,desiredPath1,currentPath2,desiredPath2):
    
    for img in os.listdir(currentPath1):
        shutil.move(currentPath1+"/"+img,desiredPath1+"/"+img)
    for img in os.listdir(currentPath2):
        shutil.move(currentPath2+"/"+img,desiredPath2+"/"+img)







