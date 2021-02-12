import tensorflow as tf
import numpy as np
import cv2
import os
import pathlib
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow import keras

# data = pd.read_csv('sign_mnist_train.csv')

# train=data.values[0:,1:] # all columns 0->n, all rows 1->k
# # labels = data.values[0:,0] #all columns 0->n, 0th row


# train = train.reshape(27455,28,28,1) # originally should be 27455, 784 for single pixel, we reshape into images

img_width = 58
img_height = 100
num_channels = 3 


cap = cv2.VideoCapture(0)


# def resize(image,desired_final_size_width,desired_final_size_height): #resize method we made
#     old_size = image.shape[:2] # old_size is in (height, width) format
#     desired_size = max(old_size)
#     print("old size")
#     print(old_size)
#     print("old size hello")
#     print("test test")
#     meanBorder = calcMeanOfBorder(image, old_size[0], old_size[1])
#     print("mean of border " + str(meanBorder))
#     color = [int(meanBorder),int(meanBorder),int(meanBorder)]
    
#     ratio = float(desired_final_size_width)/max(old_size)
    
#     print("ratio "+ str(ratio))

#     new_size = tuple([int(x*ratio) for x in old_size])
#     print("new size 0"  + str(new_size[0]) + " new size 1 " + str(new_size[1]))
#     print(new_size)
#     # new_size should be in (width, height) format
    
#     image = cv2.resize(image, (new_size[1], new_size[0])) 

#     delta_w = desired_final_size_width - new_size[1]
#     delta_h = desired_final_size_height - new_size[0]
#     top, bottom = delta_h//2, delta_h-(delta_h//2)
#     left, right = delta_w//2, delta_w-(delta_w//2)
#     print("top " + str(top)  + " bottom " + str(bottom) + " left " + str(left) + " right " + str(right))

#     #color = [128,128,128]

#     new_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT,
#         value=color)
#     resized_size = new_image.shape[:2] # old_size is in (height, width) format
#     print("final size")
#     print(resized_size)
#     #print("resized")
#     #print(resized_size)
#    # new_image = cv2.resize(new_image,(desired_final_size_width, desired_final_size_height))
#    # final_resized_size = new_image.shape[:2] # old_size is in (height, width) format
#     #print("final resize")
#     #print(final_resized_size)
#     return new_image
# def calcMeanOfBorder(image1,width,height):
#     sumOfBorderPixels = (0,0,0); 
#     counter = 0
#     for i in range(int(width/8)) :
#         for j in range(int(height/8)) :
#             sumOfBorderPixels+=image1[i,j]
#             #print("image 1 i, j value " + str(image1[i,j]))
#             #print(str(sumOfBorderPixels))
#             tempJ = width-j-1
#             tempI = height-i-1
#             sumOfBorderPixels+=image1[tempI,tempJ]
#             counter+=2
#           #  print("image 1 tempI, tempJ val " + str(image1[tempI,tempJ]))
#           #  print("sum of border pixels two val " + str(sumOfBorderPixels))
#     return sumOfBorderPixels[0]/counter
while(cap.isOpened()):
    ret, frame = cap.read()
      

    cv2.rectangle(frame,(230,0),(468,400),(255,0,0),2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        original = frame
        
        
        print(frame.shape[:2])
        
        frame = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        frame = frame[0:400,232:232*2]
        
        cv2.imshow('original',frame)        
        print("hi")
      
        
        frame = cv2.resize(frame,(img_width,img_height))

        print("final shape : " + str(frame.shape[:2])) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()

        save_path = "numbersSignLangNNModel4"

        saved_model = keras.models.load_model(save_path)

        
        prediction1 = saved_model.predict(tf.cast(tf.reshape(frame,[1,img_height,img_width,num_channels]),dtype='float32'))
        prediction1
        print(prediction1)
        #print(prediction1)
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()