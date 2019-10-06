from __future__ import absolute_import
from __future__ import print_function
import numpy as np
import random
from keras.models import Model, model_from_json
from keras.regularizers import l2
from keras.layers import Flatten, Dense, Dropout, Lambda, Conv2D, MaxPooling2D, Dropout, Input
from keras.optimizers import RMSprop, Adam, SGD
from keras import backend as K
import numpy.random as rng
from keras.callbacks import ModelCheckpoint, TensorBoard
import pickle
import time
import os


#NAME = "Classroom_SIAMESE-CNN-{}".format(int(time.time()))
#tensorboard = TensorBoard(log_dir = 'logs/{}'.format(NAME))

num_classes = 10 #total number of students in this particular class
epochs = 40

Reshaped_Size = 100 #try to get this from the Training_Data_Setup.py file

def euclidean_distance(vects):
    x, y = vects
    sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
    return K.sqrt(K.maximum(sum_square, K.epsilon()))


def eucl_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)

#loss function
def contrastive_loss(y_true, y_pred):
    '''Contrastive loss from Hadsell-et-al.'06
    http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
    '''
    margin = 1
    sqaure_pred = K.square(y_pred)
    margin_square = K.square(K.maximum(margin - y_pred, 0))
    return K.mean(y_true * sqaure_pred + (1 - y_true) * margin_square)


def create_pairs(x, digit_indices):
    '''Positive and negative pair creation.
    Alternates between positive and negative pairs.
    '''
    pairs = []
    labels = []
    n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    for d in range(num_classes):
        for i in range(n):
            z1, z2 = digit_indices[d][i], digit_indices[d][i + 1]
            pairs += [[x[z1], x[z2]]]
            inc = random.randrange(1, num_classes)
            dn = (d + inc) % num_classes
            z1, z2 = digit_indices[d][i], digit_indices[dn][i]
            pairs += [[x[z1], x[z2]]]
            labels += [1, 0]
    return np.array(pairs), np.array(labels)

#neural network architecture - CNN
def create_base_network(input_shapes):
    '''base network model - CNN
    '''
    #update based on real time execution and optimization
    input = Input(shape=input_shapes)
    conv1 = Conv2D(64,kernel_size=3,activation='relu',input_shape=input_shape, kernel_regularizer = l2(2e-4))(input)
    pool1 = MaxPooling2D(pool_size=(2,2))(conv1)
    conv2 = Conv2D(64,kernel_size=3,activation='relu')(pool1)
    pool2 = MaxPooling2D(pool_size=(2,2))(conv2)
    conv3 = Conv2D(128,kernel_size=3,activation='relu')(pool2)

    pool3 = MaxPooling2D(pool_size=(2,2))(conv3)
    conv4 = Conv2D(128,kernel_size=3,activation='relu')(pool3)
    pool4 = MaxPooling2D(pool_size=(2,2))(conv4)
    conv5 = Conv2D(256,kernel_size=3,activation='relu')(pool4)
    pool5 = MaxPooling2D(pool_size=(2,2))(conv5)
    flat = Flatten()(pool5)
    Dense1 = Dense(4096,activation="sigmoid",kernel_regularizer=l2(1e-3))(flat)
    
    return Model(input, Dense1)


def compute_accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    pred = y_pred.ravel() < 0.5
    return np.mean(pred == y_true)


def accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    return K.mean(K.equal(y_true, K.cast(y_pred < 0.5, y_true.dtype)))


# import the datasets
# os.chdir("/home/hewitt/Desktop/Project/Rooms/101")
x_train = pickle.load(open("x_train.pickle", "rb"))
y_train = pickle.load(open("y_train.pickle", "rb"))
x_test = pickle.load(open("x_test.pickle", "rb"))
y_test = pickle.load(open("y_test.pickle", "rb"))

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0],1,Reshaped_Size,Reshaped_Size) #note: adapt the 100s to Reshaped_Size in other .py
    x_test = x_test.reshape(x_test.shape[0],1,Reshaped_Size,Reshaped_Size)
    input_shape = (1,Reshaped_Size,Reshaped_Size)
else:
    x_train = x_train.reshape(x_train.shape[0],Reshaped_Size,Reshaped_Size,1)
    x_test = x_test.reshape(x_test.shape[0],Reshaped_Size,Reshaped_Size,1)
    input_shape = (Reshaped_Size,Reshaped_Size,1)    

#normalize dataset to values between 0 and 1
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

                            
# create training+test positive and negative pairs
digit_indices = [np.where(y_train == i)[0] for i in range(num_classes)]
tr_pairs, tr_y = create_pairs(x_train, digit_indices)

digit_indices = [np.where(y_test == i)[0] for i in range(num_classes)]
te_pairs, te_y = create_pairs(x_test, digit_indices)

# network definition
base_network = create_base_network(input_shape)

input_a = Input(shape=input_shape)
input_b = Input(shape=input_shape)

# because we re-use the same instance `base_network`,
# the weights of the network
# will be shared across the two branches
processed_a = base_network(input_a)
processed_b = base_network(input_b)

distance = Lambda(euclidean_distance,
                  output_shape=eucl_dist_output_shape)([processed_a, processed_b])

model = Model([input_a, input_b], distance)

# train with optimizer and contrastive loss function
opt = RMSprop()
model.compile(loss=contrastive_loss, optimizer=opt, metrics=[accuracy])
history = model.fit([tr_pairs[:, 0], tr_pairs[:, 1]], tr_y,
          batch_size=62,
          epochs=epochs,
          validation_data=([te_pairs[:, 0], te_pairs[:, 1]], te_y)) 
          #callbacks=[tensorboard])

'''
#serialize model to JSON
model_json = model.to_json()
with open("Siamese.json", "w") as json_file:
        json_file.write(model_json)
#serialize weights to HDF5
model.save_weights("Student_siamese_model.h5")
'''














