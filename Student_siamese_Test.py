import cv2
#import tensorflow as tf
import os
import numpy as np
from keras.models import model_from_json


path_face = "/home/hewitt/Desktop/Project/Faces"
path_anchor = "/home/hewitt/Desktop/Project/Rooms/101/Anchors"
students = "/home/hewitt/Desktop/Project/Student_Pictures"

def prepare(filepath, image):

    os.chdir(filepath)
    image_size = 100
    img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (image_size,image_size))
    return new_array.reshape(-1, image_size, image_size,1)
    #return new_array

os.chdir("/home/hewitt/Desktop/Project/Rooms/101")
#load json and create model
json_file = open("Siamese.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("Student_siamese_model.h5")

CATEGORIES = sorted(os.listdir(students))


for img in sorted(os.listdir(path_face)):
    total_predict = []
    for anchor in sorted(os.listdir(path_anchor)):  
        test_image = prepare(path_face,img) / 255
        anchor_image = prepare(path_anchor,anchor) / 255
        prediction = loaded_model.predict([test_image,anchor_image])
        total_predict.append(prediction)

    
 #   person = CATEGORIES[np.argmin(total_predict)]
 #   print(person)
    print(np.amin(total_predict))


































