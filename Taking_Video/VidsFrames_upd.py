import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN

#Video to Frames
def FrameCapture(path): 
    videoObj = cv2.VideoCapture(path)
    frame_count = 0
    face_count = 0
    success = 1

    detector = MTCNN()   

    while success:
        success, frame = videoObj.read()
        cv2.imwrite("frame%d.jpg" % frame_count, frame)
        
        if os.path.getsize("/home/hewitt/Desktop/Project/Frames/frame%d.jpg" %frame_count) != 0:
            image = cv2.imread("frame%d.jpg" % frame_count)
            result = detector.detect_faces(image)
            if result != []:
                for person in result:
                    bounding_box = person['box']
                    x = bounding_box[0]
                    y = bounding_box[1]
                    width = bounding_box[2]
                    height = bounding_box[3]
                    cv2.imwrite("face%d.jpg" %face_count, image[y:y+height, x:x+width])             
                    face_count += 1


        frame_count += 1

def BoundingBox():

    frame_count = 0
    image = cv2.imread("frame%d.jpg" % frame_count) #could be an issue with name of frame
    result = detector.detect_faces(image)

    if result != []:
        for person in result:
            bounding_box = person['box']
            x = bounding_box[0]
            y = bounding_box[1]
            width = bounding_box[2]
            height = bounding_box[3]
            cv2.imwrite("face%d.jpg",face_count, frame[y:y+height, x:x+width])             
            face_count += 1


#move video files to "Videos" folder
os.chdir('Videos')

#USB web cam
cap = cv2.VideoCapture(1)

#set resolution
cap.set(3, 1280)
cap.set(4,720)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#set frame rate
frame_rate = 10

#set video count
video_count = 0

#set name of video
video_name = 'output' + str(video_count) + '.avi'

#number of faces counted
#face_count = 0

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
#cv2.destroyAllWindows()
cv2.destroyWindow('frame')

os.chdir("/home/hewitt/Desktop/Project/Frames")


FrameCapture("/home/hewitt/Desktop/Project/Videos/" + video_name)







