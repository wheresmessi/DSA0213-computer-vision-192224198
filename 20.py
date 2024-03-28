import cv2
import numpy as np
img=cv2.imread("C:\\Users\mksol\\Pictures\\Saved Pictures\\fix_img-u1BM.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]])
sharpened = cv2.filter2D(gray,-1,kernel)
cv2.imshow('original',gray)
cv2.imshow("Sharpened",sharpened)
cv2.waitkey()
cv2.destroyAllWindows()
