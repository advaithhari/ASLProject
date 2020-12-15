import numpy as np
import os
import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import pandas as pd

batch_size = 16
img_height = 28
img_width = 28


#data_dir = pathlib.Path("/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/")
#print(data_dir)

#image_count = len(list(data_dir.glob('*/*.jpg')))
#print(image_count)

#data_augmentation = tf.keras.Sequential([
 # layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
#  layers.experimental.preprocessing.RandomRotation(0.2),
#])

#train_ds = tf.keras.preprocessing.image_dataset_from_directory(
 # data_dir,
 # labels="inferred",
 # label_mode='int',
 # validation_split=0.2,
 # subset="training",
 # seed=123,
 # image_size=(img_height, img_width),
 # batch_size=batch_size)

#class_names = ['A','B','C']

#val_ds = tf.keras.preprocessing.image_dataset_from_directory(
#  data_dir,
#  labels='inferred',
#  label_mode='int',
#  validation_split=0.2,
#  subset="validation",
#  seed=123,
 # image_size=(img_height, img_width),
 # batch_size=batch_size)


num_classes = 25 # no J and Z bc requires motion 

data = pd.read_csv('sign_mnist_train.csv')

train=data.values[0:,1:] # all columns 0->n, all rows 1->k
labels = data.values[0:,0] #all columns 0->n, 0th row

train = train/255 #normalize 

train = train.reshape(27455,28,28,1) # originally should be 27455, 784 for single pixel, we reshape into images

model = tf.keras.Sequential([
  layers.experimental.preprocessing.RandomZoom(.3, .3),
  layers.experimental.preprocessing.RandomRotation(.1),
  layers.Conv2D(32, 3, padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 3,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(256, activation='relu'),
  layers.Dense(64, activation='relu'),
  layers.Dense(num_classes,activation='softmax')
])


model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

model.fit(
  train,
  labels,
  validation_split=0.25,
  epochs=12,
  batch_size=batch_size
)
model.save("thirdSignLangNNModel")

