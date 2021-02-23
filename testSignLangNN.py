import tensorflow as tf
import numpy as np
import cv2
import os
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow import keras
import sys;
img_width = 58
img_height = 100
num_channels = 3
# image1 = sys.argv[1]
# #print("image 1 shape below")


# def resize(image, desired_final_size_width, desired_final_size_height):  # resize method we made
#     old_size = image.shape[:2]  # old_size is in (height, width) format
#     desired_size = max(old_size)
#   #  print("old size")
#   #  print(old_size)
#     #print("old size hello")
#   #  print("test test")
#     meanBorder = calcMeanOfBorder(image, old_size[0], old_size[1])
#   #  print("mean of border " + str(meanBorder))
#     color = [int(meanBorder), int(meanBorder), int(meanBorder)]

#     ratio = float(desired_final_size_width)/max(old_size)

#    # print("ratio "+ str(ratio))

#     new_size = tuple([int(x*ratio) for x in old_size])
#   #  print("new size 0"  + str(new_size[0]) + " new size 1 " + str(new_size[1]))
#  #   print(new_size)
#     # new_size should be in (width, height) format

#     image = cv2.resize(image, (new_size[1], new_size[0]))

#     delta_w = desired_final_size_width - new_size[1]
#     delta_h = desired_final_size_height - new_size[0]
#     top, bottom = delta_h//2, delta_h-(delta_h//2)
#     left, right = delta_w//2, delta_w-(delta_w//2)
#   #  print("top " + str(top)  + " bottom " + str(bottom) + " left " + str(left) + " right " + str(right))

#     #color = [128,128,128]

#     new_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT,
#                                    value=color)
#     resized_size = new_image.shape[:2]  # old_size is in (height, width) format

#     return new_image


# def calcMeanOfBorder(image1, height, width):
#     sumOfBorderPixels = (0, 0, 0)
#     counter = 0
#     for i in range(int(width/10)):
#         for j in range(int(height/10)):
#             sumOfBorderPixels += image1[i, j]
#             #print("image 1 i, j value " + str(image1[i,j]))
#             # print(str(sumOfBorderPixels))
#             tempJ = width-j-1
#             tempI = height-i-1
#             sumOfBorderPixels += image1[tempI, tempJ]
#             counter += 2
#           #  print("image 1 tempI, tempJ val " + str(image1[tempI,tempJ]))
#           #  print("sum of border pixels two val " + str(sumOfBorderPixels))
#     return sumOfBorderPixels[0]


# #     print("mean of border " + str(sumOfBorderPixels/counter))
# # image7 = cv2.cvtColor(cv2.resize(image7,(200,200)), cv2.COLOR_BGR2GRAY)
# # image8 = cv2.cvtColor(cv2.resize(image8,(200,200)), cv2.COLOR_BGR2GRAY)
# image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # change the color to gray
# image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)  # change it back to normal

# # image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# # image2 = cv2.cvtColor(image2, cv2.COLOR_GRAY2BGR)

# # image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
# # image3 = cv2.cvtColor(image3, cv2.COLOR_GRAY2BGR)

# # using our resize function and inputing a height and width
# image1 = resize(image1, img_width, img_height)
# # image2 = resize(image2, img_width, img_height)
# # image3 = resize(image3, img_width, img_height)

# #cv2.imshow("imgage 1",image1)
# #cv2.imshow("imgage 2",image2)
# #cv2.imshow("imgage 3",image3)


# #save_path = "numbersSignLangNNModel4"
# save_path = "/numbersSignLangNNModel4"

# saved_model = keras.models.load_model(
#     "numbersSignLangNNModel4")  # loading our model in

# prediction1 = saved_model.predict(tf.cast(tf.reshape(image1, [1, img_height, img_width, num_channels]), dtype='float32'))  # getting the accuracy values as an array
# #print("DS 8 ")
# # print(prediction1)
# # prediction2 = saved_model.predict(tf.cast(tf.reshape(image2, [1, img_height, img_width, num_channels]), dtype='float32'))
# # #print("DS 1 ")
# # # print(prediction2)
# # prediction3 = saved_model.predict(tf.cast(tf.reshape(image3, [1, img_height, img_width, num_channels]), dtype='float32'))
# # #print("FS 1 ")
# # # print(prediction3)

#print(prediction1)

print("test response stuff")
