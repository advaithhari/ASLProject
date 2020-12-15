import tensorflow as tf
import numpy as np
import cv2
import os
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow import keras
import pandas as pd

data = pd.read_csv('sign_mnist_train.csv')

train=data.values[0:,1:] # all columns 0->n, all rows 1->k
labels = data.values[0:,0] #all columns 0->n, 0th row

train = train/255 #normalize 

train = train.reshape(27455,28,28,1) # originally should be 27455, 784 for single pixel, we reshape into images

plt.imshow(train[5].reshape((28,28)),cmap="Greys")
plt.show()
#plt.imshow(train[1].reshape((28,28)))
save_path = "thirdSignLangNNModel"

saved_model = keras.models.load_model(save_path)

res=saved_model.predict(train.reshape(27455,28,28,1))
res =list(res[5])
mx=max(res)
print(res.index(mx))
print(labels[5])
