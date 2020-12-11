import numpy as np
import os
import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import pandas as pd

batch_size = 64
img_height = 200
img_width = 200


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
  layers.experimental.preprocessing.Resizing(28,28),
  layers.experimental.preprocessing.RandomZoom(.3, .3),
  layers.experimental.preprocessing.RandomRotation(.1),
  layers.Conv2D(32, 3, padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 3,padding='same',  activation='relu'),
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
  train,
  labels,
  validation_split=0.25,
  epochs=5
)
model.save("thirdSignLangNNModel")

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()




