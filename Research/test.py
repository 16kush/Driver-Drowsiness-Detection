import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

img = cv2.imread('Assets/left-eye.jpg')

cv2.imshow('Video', img)

if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()