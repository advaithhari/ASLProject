import tensorflow as tf
import numpy as np
import cv2
import os
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow import keras


batch_size = 5
img_height = 200
img_width = 200

image1 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/A/A1.jpg')
image2 = cv2.imread('/home/jetsonnano/tensorTests/TestImages/A.jpg')
image3 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/A/A3.jpg')
image4 = cv2.imread('/home/jetsonnano/tensorTests/TestImages/b1.jpg')
image5 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/B/B2.jpg')
image6 = cv2.imread('/home/jetsonnano/tensorTests/TestImages/c.jpg')
image7 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/C/C2.jpg')
image8 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/C/C3.jpg')

image1 = cv2.cvtColor(cv2.resize(image1,(28,28)), cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(cv2.resize(image2,(28,28)), cv2.COLOR_BGR2GRAY)
image3 = cv2.cvtColor(cv2.resize(image3,(28,28)), cv2.COLOR_BGR2GRAY)
image4 = cv2.cvtColor(cv2.resize(image4,(28,28)), cv2.COLOR_BGR2GRAY)
image5 = cv2.cvtColor(cv2.resize(image5,(28,28)), cv2.COLOR_BGR2GRAY)
image6 = cv2.cvtColor(cv2.resize(image6,(28,28)), cv2.COLOR_BGR2GRAY)
image7 = cv2.cvtColor(cv2.resize(image7,(28,28)), cv2.COLOR_BGR2GRAY)
image8 = cv2.cvtColor(cv2.resize(image8,(28,28)), cv2.COLOR_BGR2GRAY)

save_path = "/home/jetsonnano/tensorTests/thirdSignLangNNModel"

saved_model = keras.models.load_model(save_path)

prediction1 = saved_model.predict(tf.cast(tf.reshape(image1,[1,28,28,1]),dtype='float32'))
print("DS A ")
print(prediction1)
prediction2 = saved_model.predict(tf.cast(tf.reshape(image2,[1,28,28,1]),dtype='float32'))
print("DS A ")
print(prediction2)
prediction3 = saved_model.predict(tf.cast(tf.reshape(image3,[1,28,28,1]),dtype='float32'))
print("DS A ")
print(prediction3)
prediction4 = saved_model.predict(tf.cast(tf.reshape(image4,[1,28,28,1]),dtype='float32'))
print("DS B ")
print(prediction4)
prediction5 = saved_model.predict(tf.cast(tf.reshape(image5,[1,28,28,1]),dtype='float32'))
print("DS B ")
print(prediction5)
prediction6 = saved_model.predict(tf.cast(tf.reshape(image6,[1,28,28,1]),dtype='float32'))
print("DS C ")
print(prediction6)
prediction7 = saved_model.predict(tf.cast(tf.reshape(image7,[1,28,28,1]),dtype='float32'))
print("DS C ")
print(prediction7)
prediction8 = saved_model.predict(tf.cast(tf.reshape(image8,[1,28,28,1]),dtype='float32'))
print("DS C ")
print(prediction8)

