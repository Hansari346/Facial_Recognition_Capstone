import cv2
import os
import numpy as np
from keras.models import model_from_json
from keras import backend as K


path_face = "/home/hewitt/Desktop/Project/Faces"
path_anchor = "/home/hewitt/Desktop/Project/Rooms/101/Anchors"
students = "/home/hewitt/Desktop/Project/Student_Pictures"

CATEGORIES = sorted(os.listdir(students))

def Prepare(filepath, image):

    os.chdir(filepath)
    image_size = 100
    img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (image_size,image_size))
    return new_array.reshape(-1, image_size, image_size,1)
    #return new_array

'''
os.chdir("/home/hewitt/Desktop/Project/Rooms/101")
#load json and create model
json_file = open("Siamese.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("Student_siamese_model.h5")
'''

def StudentPredict(face_path):

    os.chdir("/home/hewitt/Desktop/Project/Rooms/101")
    #load json and create model
    json_file = open("Siamese.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    #load weights into new model
    loaded_model.load_weights("Student_siamese_model.h5")

    students = []
    studentMins = []

    for img in sorted(os.listdir(face_path)):
        total_predict = []
        for anchor in sorted(os.listdir(path_anchor)):  
            test_image = Prepare(face_path,img) / 255
            anchor_image = Prepare(path_anchor,anchor) / 255
            prediction = loaded_model.predict([test_image,anchor_image])
            total_predict.append(prediction)

        person = CATEGORIES[np.argmin(total_predict)]
        students.append(person)
        studentMins.append(np.amin(total_predict))

        print(person)
        print(np.amin(total_predict))

    #will need an algorithm for first determining if each image belongs to the class based on the threshold, then take the sum of the five photos and 


def StudentValidity(students,studentMins):

    counter = [[0 for i in range(len(CATEGORIES))] for j in range(2)]  #2D list of zeros with length of CATEGORIES (students)
    for count in range(len(counter[0])):
        for x in range(len(students)):
            if students[x] == CATEGORIES[count]: #"and studentsMin[x] <= threshold
                counter[0][count] += 1
                counter[1][count] += studentMins[x]

#    index = counter.index(max(counter[0]))




























