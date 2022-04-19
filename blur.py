import cv2
import numpy as np

img = cv2.imread('Lena.png')
rows, cols = img.shape[:2]

#kernel blurring
kernel_25 = np.ones((25,25), np.float32)/625.0
output_kernel = cv2.filter2D(img, -1, kernel_25)

# #Blur function
output_blur = cv2.blur(img,(25,25))

# #BoxFilter
output_box= cv2.boxFilter(img, -1, (5,5), normalize=False) #does not normalize

# #Gaussian blurring
output_gauss = cv2.GaussianBlur(img,(5,5), 1)

# #median blur
output_med = cv2.medianBlur(img, 5)

# #bilateral blur
output_bi = cv2.bilateralFilter(img, 10, 6,6)

cv2.imshow('kernel_blur', output_kernel)
cv2.imshow('blur function', output_blur)
cv2.imshow('Box filter', output_box)
cv2.imshow('Gaussian blur', output_gauss)
cv2.imshow('Median blur', output_med)
cv2.imshow('Bilateral filter', output_bi)
cv2.waitKey(0)                                                                                                                                                              
