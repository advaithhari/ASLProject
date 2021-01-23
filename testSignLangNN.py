import tensorflow as tf
import numpy as np
import cv2
import os
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow import keras


img_width = 100
img_height = 72
num_channels = 3 

image1 = cv2.imread('numbersDataset/unknown/unknown_8.jpg')
image2 = cv2.imread('numbersDataset/7/seven_3.jpg')
image3 = cv2.imread('testnums/7.jpg')
print("image 1 shape below")
print(image1.shape)

# image4 = cv2.imread('/home/jetsonnano/tensorTests/TestImages/b1.jpg')
# image5 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/B/B2.jpg')
# image6 = cv2.imread('/home/jetsonnano/tensorTests/TestImages/c.jpg')
# image7 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/C/C2.jpg')
# image8 = cv2.imread('/home/jetsonnano/tensorTests/sign-language-alphabet-recognizer/dataset/C/C3.jpg')
def resize(image,desired_final_size_width,desired_final_size_height): 
    old_size = image.shape[:2] # old_size is in (height, width) format
    desired_size = max(old_size)
   # print("old size")
    print(old_size)
    ratio = float(desired_final_size_width)/max(old_size)
    
    print("ratio "+ str(ratio))

    new_size = tuple([int(x*ratio) for x in old_size])
    print("new size 0"  + str(new_size[0]) + " new size 1 " + str(new_size[1]))
    print(new_size)
    # new_size should be in (width, height) format
    
    image = cv2.resize(image, (new_size[1], new_size[0]))

    delta_w = desired_final_size_width - new_size[1]
    delta_h = desired_final_size_height - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    print("top " + str(top)  + " bottom " + str(bottom) + " left " + str(left) + " right " + str(right))
    color = [128, 128, 128]
    new_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)
    resized_size = new_image.shape[:2] # old_size is in (height, width) format
    print(resized_size)
    #print("resized")
    #print(resized_size)
   # new_image = cv2.resize(new_image,(desired_final_size_width, desired_final_size_height))
   # final_resized_size = new_image.shape[:2] # old_size is in (height, width) format
    #print("final resize")
    #print(final_resized_size)
    return new_image

# image7 = cv2.cvtColor(cv2.resize(image7,(200,200)), cv2.COLOR_BGR2GRAY)
# image8 = cv2.cvtColor(cv2.resize(image8,(200,200)), cv2.COLOR_BGR2GRAY)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)

image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2, cv2.COLOR_GRAY2BGR)

image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
image3 = cv2.cvtColor(image3, cv2.COLOR_GRAY2BGR)

image1 = resize(image1,img_height, img_width)
image2 = resize(image2,img_height, img_width)
image3 = resize(image3,img_height, img_width)



save_path = "numbersSignLangNNModel2"

saved_model = keras.models.load_model(save_path)

prediction1 = saved_model.predict(tf.cast(tf.reshape(image1,[1,img_width,img_height,num_channels]),dtype='float32'))
print("DS 8 ")
print(prediction1)
prediction2 = saved_model.predict(tf.cast(tf.reshape(image2,[1,img_width,img_height,num_channels]),dtype='float32'))
print("DS 1 ")
print(prediction2)
prediction3 = saved_model.predict(tf.cast(tf.reshape(image3,[1,img_width,img_height,num_channels]),dtype='float32'))
print("FS 1 ")
print(prediction3)
