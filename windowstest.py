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

# image1 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/A/A1.jpg')
image2 = cv2.imread('TestImages/b1.jpg')
#image3 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/A/A3.jpg')
#image4 = cv2.imread('/home/jetsonnano/tensorTests/TestImages/b1.jpg')
#image5 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/B/B2.jpg')
#image6 = cv2.imread('/home/jetsonnano/tensorTests/TestImages/c.jpg')
#image7 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/C/C2.jpg')
#image8 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/C/C3.jpg')

# image1 = cv2.resize(image1,(200,200))
image2 = cv2.resize(image2,(200,200))
#image3 = cv2.resize(image3,(200,200))
#image4 = cv2.resize(image4,(200,200))
#image5 = cv2.resize(image5,(200,200))
#image6 = cv2.resize(image6,(200,200))
#image7 = cv2.resize(image7,(200,200))
#image8 = cv2.resize(image8,(200,200))

save_path = "secondSignLangNNModel"

saved_model = keras.models.load_model(save_path)

# prediction1 = saved_model.predict(tf.reshape(image1,[1,200,200,3]))
# print(prediction1)
prediction2 = saved_model.predict(tf.reshape(image2,[1,200,200,3]))
print(prediction2)
# prediction3 = saved_model.predict(tf.reshape(image3,[1,200,200,3]))
# print(prediction3)
# prediction4 = saved_model.predict(tf.reshape(image4,[1,200,200,3]))
# print(prediction4)
# prediction5 = saved_model.predict(tf.reshape(image5,[1,200,200,3]))
# print(prediction5)
# prediction6 = saved_model.predict(tf.reshape(image6,[1,200,200,3]))
# print(prediction6)
# prediction7 = saved_model.predict(tf.reshape(image7,[1,200,200,3]))
# print(prediction7)
# prediction8 = saved_model.predict(tf.reshape(image8,[1,200,200,3]))
# print(prediction8)
