import cv2
import os
import numpy as np
import time
from keras.models import model_from_json
from keras import backend as K
import tensorflow as tf


#note: will need to adapt image_size
def Prepare(filepath, image):

    os.chdir(filepath)
    Width = 100
    Height = 120
    img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (Width, Height))
    return new_array.reshape(-1, Width, Height,1) / 255


config = tf.ConfigProto(
    device_count={'GPU': 1},
    intra_op_parallelism_threads=1,
    allow_soft_placement=True)

config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.6
session = tf.Session(config=config)
K.set_session(session)

RoomPath = "/home/hewitt/Desktop/Project/Rooms/101"
#load json and create model
json_file = open(RoomPath + "/Siamese.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights(RoomPath + "/Student_siamese_model.h5")


def StudentPredict(FacesPath,RoomPath,StudentsPath):
    print('beginning StudentPredict function')
    start = time.time()

    AnchorsPath = RoomPath + "/Anchors"
    StudentsList = sorted(os.listdir(StudentsPath))
    students = []
    studentMins = []

    for img in sorted(os.listdir(FacesPath)):
        total_predict = []
        if os.path.getsize(FacesPath + "/" + img) != 0:
            for anchor in sorted(os.listdir(AnchorsPath)):  
                test_image = Prepare(FacesPath,img) / 255
                anchor_image = Prepare(AnchorsPath,anchor) / 255
                with session.as_default():
                    with session.graph.as_default():

                        prediction = loaded_model.predict([test_image,anchor_image])
                total_predict.append(prediction)

            person = StudentsList[np.argmin(total_predict)]
            students.append(person)
            studentMins.append(np.amin(total_predict))

            print(person)
            print(np.amin(total_predict))

    print('Time to compute StudentPredict: {} seconds'.format(time.time() - start))
    return students, studentMins


def StudentValidity(students,studentMins,StudentsPath):

    print('beginning StudentValidity function')
    StudentsList = sorted(os.listdir(StudentsPath))

    counter = [[0 for i in range(len(StudentsList))] for j in range(2)]  #2D list of zeros with length of CATEGORIES (students)
    for count in range(len(counter[0])):
        for x in range(len(students)):
            if students[x] == StudentsList[count]: #"and studentsMin[x] <= threshold
                counter[0][count] += 1
                counter[1][count] += studentMins[x]

    if max(counter[0]) >= 3:
        return True
    else:
        return False


def StudentPredict2(FacesPath,RoomPath,StudentsPath):
    print('beginning StudentPredict2 function')

    AnchorsPath = RoomPath + "/Anchors"
    StudentsList = sorted(os.listdir(StudentsPath))
    total_predict = []
    imgCount = 0
    for img in sorted(os.listdir(FacesPath)):

        total_predict.append([])

        if os.path.getsize(FacesPath + "/" + img) != 0:
            for anchor in sorted(os.listdir(AnchorsPath)):  
                test_image = Prepare(FacesPath,img)
                anchor_image = Prepare(AnchorsPath,anchor)
                with session.as_default():
                    with session.graph.as_default():
                        prediction = loaded_model.predict([test_image,anchor_image])
                        total_predict[imgCount].append(prediction)
            imgCount += 1

    return total_predict


def StudentValidity2(total_predict, StudentsPath)
    #note the following algorithm works for 100% accuracy only!
    StudentsList = sorted(os.listdir(StudentsPath))
    Students = []

    for i in range(len(total_predict)):
        person = Students.append(StudentsList[np.argmin(total_predict[i])])

    Students = set(Students)

    return Students










