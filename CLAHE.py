import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('girl.jpeg')
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#declaration of limit for clahe
clahe = cv2.createCLAHE(clipLimit = 5)
final_img = clahe.apply(image_bw)

cv2.imshow('winname',final_img)
cv2.waitKey(0)