import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

Reshaped_Size = 100 #will resize to this number by this number

DIR = "/home/hewitt/Desktop/Project/Student_Pictures"	#take images from Faces. Note: will change this to another file based on training 

CATEGORIES = ['Benjamin Hewitt', "Eli Chodock", "Yaser El-Outa", "Hasan Ansari", "Zack Thomas", "John Hewitt", "Aaron Hewitt", "Kyle Sylvester", "Jackie Mueller", "Jason Kemppainen"] #categories of each class


training_data = []
testing_data = []

def create_data():
    for category in CATEGORIES:
        path = os.path.join(DIR, category + "/Train")
        class_num = CATEGORIES.index(category) #this will be the number for each class in order of CATEGORIES
        for img in os.listdir(path): #iterate through each file in the directory path
            img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_UNCHANGED) #eliminate the cv2.IMREAD_GRAYSCALE to get BGR data
            new_array = cv2.resize(img_array, (Reshaped_Size, Reshaped_Size))	#resize to 100x100       
            training_data.append([new_array, class_num])
    for category in CATEGORIES:
        path = os.path.join(DIR, category + "/Test")
        class_num = CATEGORIES.index(category) #this will be the number for each class in order of CATEGORIES
        for img in os.listdir(path): #iterate through each file in the directory path
            img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_UNCHANGED) #eliminate the cv2.IMREAD_GRAYSCALE to get BGR data
            new_array = cv2.resize(img_array, (Reshaped_Size, Reshaped_Size))	#resize to 100x100       
            testing_data.append([new_array, class_num])


create_data()

random.shuffle(training_data)	#shuffle data

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
x_train = np.array(x_train).reshape(-1,Reshaped_Size, Reshaped_Size) #-1 because gray scale (1D)
y_train = np.array(y_train)
x_test = np.array(x_test).reshape(-1,Reshaped_Size, Reshaped_Size) #-1 because gray scale (1D)
y_test = np.array(y_test)

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




