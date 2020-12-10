import numpy as np
import os
import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers

batch_size = 10
img_height = 200
img_width = 200


data_dir = pathlib.Path("/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/")
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
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = ['A','B','C']

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  labels='inferred',
  label_mode='int',
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)


num_classes = 3

model = tf.keras.Sequential([
  layers.experimental.preprocessing.Rescaling(1./255),
  layers.Conv2D(32, 5, padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 5,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 5,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(256, 5,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(512, 5,padding='same',  activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(1024, 5, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes,activation='softmax')
])


model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=1
)
model.save("secondSignLangNNModel")

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




