import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle


def concatenate_training_data(student_pic_path):
    training_data = []
    for category in CATEGORIES:
        path = os.path.join(student_pic_path, category + "/Train")
        class_num = CATEGORIES.index(category) #teacher vector value for each class
        for img in os.listdir(path): #iterate through each file in the directory path
            img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) #Grayscale image
            new_array = cv2.resize(img_array, (Reshaped_Size, Reshaped_Size))	#resize to 100x100       
            training_data.append([new_array, class_num])
    return training_data

def concatenate_testing_data(student_pic_path):
    testing_data = []
    for category in CATEGORIES:
        path = os.path.join(student_pic_path, category + "/Test")
        class_num = CATEGORIES.index(category) #teacher vector value for each class
        for img in os.listdir(path): #iterate through each file in the directory path
            img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) #Grayscale image
            new_array = cv2.resize(img_array, (Reshaped_Size, Reshaped_Size))	#resize to 100x100       
            testing_data.append([new_array, class_num])
    return testing_data


#will resize to this number by this number
Reshaped_Size = 100 
#take images from Faces. Note: will change this to another file based on training 
student_picture_path = "/home/hewitt/Desktop/Project/Student_Pictures"
#categories of people in this particular class
CATEGORIES = sorted(os.listdir(student_picture_path))

#concatenate training and testing data
training_data = concatenate_training_data(student_picture_path)
testing_data = concatenate_testing_data(student_picture_path)

#shuffle data
random.shuffle(training_data)	
random.shuffle(testing_data)


#separate data by each desired vector (training and testing)
x_train = []
y_train = []
x_test = []
y_test = []


#separate image data from teacher vector data
for features, label in training_data:
    x_train.append(features)
    y_train.append(label)

for features, label in testing_data:
    x_test.append(features)
    y_test.append(label)

#turn the arrays into np arrays
x_train = np.array(x_train).reshape(-1,Reshaped_Size, Reshaped_Size) #-1 because gray scale
y_train = np.array(y_train)
x_test = np.array(x_test).reshape(-1,Reshaped_Size, Reshaped_Size) #-1 because gray scale
y_test = np.array(y_test)

#move to specific room folder
os.chdir("/home/hewitt/Desktop/Project/Rooms/101")

#export data to both x_train and y_train
pickle_out = open("x_train.pickle", "wb")
pickle.dump(x_train,pickle_out)
pickle_out.close()

pickle_out = open("y_train.pickle", "wb")
pickle.dump(y_train,pickle_out)
pickle_out.close()

#export data to both x_test and y_test
pickle_out = open("x_test.pickle", "wb")
pickle.dump(x_test,pickle_out)
pickle_out.close()

pickle_out = open("y_test.pickle", "wb")
pickle.dump(y_test,pickle_out)
pickle_out.close()




