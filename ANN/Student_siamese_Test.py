import cv2
import tensorflow as tf
import os
from keras.models import model_from_json


def prepare(filepath):
    
    image_size = 100
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (image_size,image_size))
    return new_array.reshape(-1, image_size, image_size)

#load json and create model
json_file = open("Siamese.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("Student_siamese_model.h5")


CATEGORIES = ['Benjamin Hewitt', "Eli Chodock", "Yaser El-Outa", "Hasan Ansari"]

num_classes = 4


#total number of face.jpg images in "Faces" folder
face_count = 84

os.chdir("/home/hewitt/Desktop/Project/Faces")

for x in range(face_count+1):
    
    if cv2.imread("face%d.jpg" %x).shape[1] > 100 and cv2.imread("face%d.jpg" %x).shape[2] > 100:
        prediction = loaded_model.evaluate([prepare("face%d.jpg" %x)],prepare["face%d.jpg" %x])
        print(prediction)























