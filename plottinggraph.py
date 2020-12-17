import tensorflow as tf
import numpy as np
import cv2
import os
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow import keras
import pandas as pd

# data = pd.read_csv('sign_mnist_train.csv')

# train=data.values[0:,1:] # all columns 0->n, all rows 1->k
# labels = data.values[0:,0] #all columns 0->n, 0th row


# train = train.reshape(27455,28,28,1) # originally should be 27455, 784 for single pixel, we reshape into images



cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
   
    nummm = 130

    plt.imshow(train[nummm].reshape((28,28)))
    plt.show()
    #plt.imshow(train[1].reshape((28,28)))
    save_path = "thirdSignLangNNModel"

    saved_model = keras.models.load_model(save_path)

  #  res=saved_model.predict(train.reshape(27455,28,28,1))

    rz= saved_model.predict(tf.cast(tf.reshape(frame,[1,28,28,1]),dtype='float32'))

    rz = list(rz[nummm])

   # res =list(res[nummm])
   # mx=max(res)

    mz =max(rz)

    print(rz.index(mz))
 #   print(res.index(mx))
  #  print(labels[nummm])



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


