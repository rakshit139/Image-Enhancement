import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Lena.png')
b,g,r = cv2.split(image)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(image_hsv)
v = cv2. equalizeHist(v)
merged_hsv = cv2.merge((h,s,v))
bgr_enhanced = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2BGR)
#split is used to break the image into 3 color components that is b g r 
#split returns an image 

cv2.imshow('winname', image)
cv2.imshow('winname', bgr_enhanced)
hist = cv2.calcHist([b], [0], None, [256], [0,255])
plt.plot(hist)
hist = cv2.calcHist([g], [0], None, [256], [0,255])
plt.plot(hist)
hist = cv2.calcHist([r], [0], None, [256], [0,255])
plt.plot(hist)
plt.show()

cv2.waitKey(0000)
