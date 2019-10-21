import cv2
import os
import numpy as np

mainPath = "/home/hewitt/Desktop/Project/Student_Pictures"
desiredPath = "/home/hewitt/Desktop/Project/Student_Pictures_100x120"

#this is the entire list of students we have so far
STUDENTS = sorted(os.listdir(mainPath))
#this is a list of strings: Anchor, Extras, Test, Train
SUBCATEGORY = sorted(os.listdir(mainPath+"/"+STUDENTS[0]))
#width of resized images
width = 100
#height of resized images
height = 120


#make a directory: os.mkdir(path)
'''
os.mkdir(desiredPath)

for student in STUDENTS:
    os.mkdir(desiredPath+"/"+student)
    for category in SUBCATEGORY:
        os.mkdir(desiredPath+"/"+student+"/"+category)
'''

#for each student in the list
for student in STUDENTS:
    #for each subdirectory in each student's directory
    for category in SUBCATEGORY:
        #create the total current path
        currentPath = mainPath + "/" + student + "/" + category
        #create the total desired path
        gotoPath = desiredPath + "/" + student + "/" + category
        #for each image in each subdirectory in each student's directory
        for img in os.listdir(currentPath):
            #read in the image
            image = cv2.imread(currentPath+ "/" + img)
            #resize the image
            resized_image = cv2.resize(image,(width,height))
            #save the image to the desired path
            cv2.imwrite(gotoPath + "/" + img, resized_image)


