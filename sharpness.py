import cv2
import numpy as np

img = cv2.imread('girl3.jpeg')

gausian_blur = cv2.GaussianBlur(img, (7,7), 2)

#sharpening using add weighted
sharpened = cv2.addWeighted(img, 2.5, gausian_blur, -1.0, 0)

# cv2.imwrite('girl2.jpeg', sharpened)
# output_gauss = cv2.GaussianBlur(sharpened,(5,5), 1)
cv2.imshow('output_gauss', sharpened)
cv2.waitKey(0)