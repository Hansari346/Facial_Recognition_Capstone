import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

#NAME = "Students-cnn-64x2-{}".format(int(time.time()))

#tensorboard = TensorBoard(log_dir='logs/{}'.format(Name)


x = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("Y.pickle", "rb"))

x = x/255

model = Sequential()
model.add(Conv2D(64, (3,3), input_shape = x.shape[1:])) #note, shape is for gray scaled photo
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(64, (3,3))) #note, shape is for gray scaled photo
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation("sigmoid))


model.compile(loss = "sparse_categorical_crossentropy", optimizer = "adam", metrics = ['accuracy'])

model.fit(x,y, batch_size = 128, epochs = 20, validation_split = 0.3) #, callbacks = [tensorboard])


