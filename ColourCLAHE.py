import cv2
from matplotlib import pyplot as plt
import numpy as np
#Read bgr image
bgr = cv2.imread('girl3.jpeg')
#convert it to lab
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
#Split
lab_planes = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.0)

lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

cv2.imwrite('winname.jpeg',bgr)
cv2.waitKey(0)