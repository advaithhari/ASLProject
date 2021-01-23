import numpy as np
import os
import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers, preprocessing
import pandas as pd
from tensorflow.keras.layers import experimental
from tensorflow.python.keras.layers.preprocessing.image_preprocessing import Rescaling, Resizing

batch_size = 16

img_height  = 100
img_width = 72


data_dir = pathlib.Path("numbersDataset/")
print(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

data_augmentation = tf.keras.Sequential([
 layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
 layers.experimental.preprocessing.RandomRotation(0.2),
])

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
 data_dir,
 labels="inferred",
 label_mode='int',
 validation_split=0.25,
 subset="training",
 seed=469169,
 image_size=(img_height, img_width),
 batch_size=batch_size)

#class_names = ['A','B','C']

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
 data_dir,
 labels='inferred',
 label_mode='int',
 validation_split=0.25,
 subset="validation",
 seed=469169,
 image_size=(img_width, img_height),
 batch_size=batch_size)


num_classes = 11 # 0->9 and then a category for unknown. 

# data = pd.read_csv('sign_mnist_train.csv')

# train=data.values[0:,1:] # all columns 0->n, all rows 1->k
# labels = data.values[0:,0] #all columns 0->n, 0th row

# train = train/255 #normalize 

# train = train.reshape(27455,28,28,1) # originally should be 27455, 784 for single pixel, we reshape into images

model = tf.keras.Sequential([
  layers.experimental.preprocessing.Rescaling(1./255),# do this to normalize it 255 is the full color 
  layers.Conv2D(32, 3, padding='same',  activation='relu'),#convolutional and pooling layers to shrink image
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 3,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(256, 3,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(512, activation='relu'),
  layers.Dense(num_classes,activation='softmax')
])


model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=6,
  batch_size=batch_size
)
model.save("numbersSignLangNNModel3")

