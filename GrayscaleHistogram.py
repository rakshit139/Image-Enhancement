#For histogram math
#https://www.youtube.com/watch?v=PD5d7EKYLcA

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Lena.png')
#To change colour space 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#To get the histogram
#everything should be passed in tuple form
#cv2.calcHist(image, channels, mask, histSize i.e no. of bins, ranges )
#histSize is 256 because there are values from 0 to 255 the histogram intensities values
hist = cv2.calcHist([image], [0], None, [256], [0,255])
plt.plot(hist)
cv2.imshow('winname', image)

#To equalise
image_hist = cv2.equalizeHist(image)
hist = cv2.calcHist([image_hist], [0], None, [256], [0,255])
plt.plot(hist)
plt.show()
cv2.imshow('histogram', image_hist)

cv2.waitKey()