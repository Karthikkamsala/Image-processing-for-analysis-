# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XVpFeQ93S7hhKQg9lUC4y7tsaTAayzhF

libraries importing
"""

import matplotlib.image as mp
import matplotlib.pyplot as plt

"""image loading

"""

img=mp.imread('/content/puppy.webp')

type(img)

print(img.shape)   # gives the dimensions width ,height, RGBor B&W

print(img) # image is stored in matrix form

"""we can also convert numpy array into image (reverse)"""

img_plt=plt.imshow(img) #used from matplotlib
plt.show()

from PIL import Image # importing Image module from PILLOW library

#resizing the image 
from PIL import Image # importing Image module from PILLOW library
img=Image.open('/content/puppy.webp')
img_resized=img.resize((200,200))

print(img_resized)

#need to save the resized image to know the properties
img_resized.save('resized.jpg')

rimg=mp.imread('/content/resized.jpg') #loading the resized image and checking matrix
print(rimg)

rimg=plt.imshow(rimg)
plt.show()



"""converting RGB to Grayscale

"""

#load the image into cv2
import cv2
img=cv2.imread('/dog-puppy-on-garden-royalty-free-image-1586966191.webp')

gs_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

print(gs_image)

type(gs_image)
gs_image.shape

from google.colab.patches import cv2_imshow
cv2_imshow(gs_image)

print(gs_image.shape)

#to save using cv2 
cv2.imwrite('B&W.jpeg',gs_image)

