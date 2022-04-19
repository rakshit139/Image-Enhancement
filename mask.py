import cv2

# Reading the original image
image_spot = cv2.imread('dog.jpg')
cv2.imshow('Original',image_spot)

# Converting it to HSV color space
hsv_image_spot = cv2.cvtColor(image_spot, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv_image_spot)

# Setting the black pixel mask and perform bitwise_and to get only the black pixels
mask = cv2.inRange(hsv_image_spot, (0, 0, 0), (180, 255, 40))
masked = cv2.bitwise_and(hsv_image_spot, hsv_image_spot, mask=mask)
cv2.imshow('Mask',masked)
cv2.waitKey(0)