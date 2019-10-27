#updated time stamp from video to frames. 
import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN
import time
import datetime 
from i2c_trigger_Final import *
import shutil


#USB web cam
cap = cv2.VideoCapture(1)

#set resolution
cap.set(3, 1280)
cap.set(4,720)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#setframe rate
frame_rate = 15
cap.set(5,frame_rate)

#frame delay for timestamping images
frame_delay = (1 / frame_rate)



#initialize read and imshow for time save
ret, frame = cap.read()
cv2.imshow('frame',frame)
time.sleep(0.1)
cv2.destroyWindow('frame')


#define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')


def get_timestamp(stamp,delay):
    stamp = stamp[0:-4]
    delay = int(float('%.6f'%(delay)) * 1000000)
    datetime_object = datetime.datetime.strptime(stamp, '%Y-%m-%d %H:%M:%S.%f')
    updated_time = datetime_object+datetime.timedelta(0,0,delay)
    return str(updated_time)


def TakeVideo(VideosPath):
    print('start TakeVideo')
    count = 15

    #update video name based on current time in seconds
    video_name = str(datetime.datetime.now()) + '.avi'
    out = cv2.VideoWriter(VideosPath + "/" + video_name,fourcc, frame_rate, (frame_width,frame_height))
    
    #turn webcam on while interrupt is not triggered
    while(cap.isOpened()):          
        ret, frame = cap.read()        
        if ret==True:
            out.write(frame) 
            cv2.imshow('frame',frame)
            if Thermal_Values() == False:
                count -= 1
            else:
                count = 15
            cv2.waitKey(1)
#            if cv2.waitKey(1) & 0xFF == ord('q'):
            if count <= 0:
                break
        else:
            break
    #release out and frame
    out.release()
    cv2.destroyWindow('frame')
#    cap.release()    


def TakeFrames(LateFramesPath): 
    print('Start FrameCapture')
    start = time.time() 

    count = 5

    while (count >= 0):
        ret, frame = cap.read() #takes approximately 80 milliseconds
        if ret==True:

            cv2.imwrite(LateFramesPath + "/" + str(datetime.datetime.now()) + '.jpg', frame)
            count -= 1
            if count <= 0: #set interrupt here - set to "q" for now
                break
        else:
            break

    print('Time to compute TakeFrames: {} seconds'.format(time.time() - start))
#    cap.release()
#    cap.destroyWindow('frame')



def Vids2Frames(VideosPath,FramesPath): 
    print('Start Vids2Frames')

    #run through each video
    for vid in os.listdir(VideosPath):
        videoObj = cv2.VideoCapture(VideosPath+ "/" + vid) #select desired video 
        success = 1         
        delay = 0

        #save each frame in each video
        while success:
            success, frame = videoObj.read()            
            cv2.imwrite(FramesPath + "/" + get_timestamp(vid,delay) + '.jpg', frame) #save frame in "Frames" folder
            delay += frame_delay


#Crop faces from frames
def BoundingBox(FramesPath, FacesPath, detector):
    print('Start BoundingBox')      
    start = time.time()    

    #for each photo in "Frames" folder
    for img in os.listdir(FramesPath):    

        if os.path.getsize(FramesPath + "/" + img) != 0:
            image = cv2.imread(FramesPath + "/" + img)
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
                    cv2.imwrite(FacesPath + "/" + image_name, image[y:y+height, x:x+width]) #crop the bounding box

                    face_count += 1

    print('Time to compute BoundingBox: {} seconds'.format(time.time() - start))

def MoveData(currentPath,desiredPath):
    print('Start MoveData')

    for data in os.listdir(currentPath):
        shutil.move(currentPath+"/"+data,desiredPath+"/"+data)







