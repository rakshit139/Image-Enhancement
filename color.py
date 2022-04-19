import cv2

image = cv2.imread('dog.jpg')

#HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

#LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

#YCrCb
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

cv2.imshow('YCrCb',ycrcb_image)
cv2.imshow('LAB',lab_image)
cv2.imshow('HSV', hsv_image)
cv2.waitKey(0)  

