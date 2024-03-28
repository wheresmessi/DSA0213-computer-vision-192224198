import cv2
import numpy as np
img=cv2.imread("C:\\Users\mksol\\Pictures\\Saved Pictures\\fix_img-u1BM.jpg")
cv2.imshow('original', img)
cv2.waitkey(0)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)
d=cv2.CV_64F
sobelx = sc2.Sobel(nlur,)
cv2.imshow("Sobel X",sobelx)
