import cv2
import numpy as np
img=cv2.imread("C:\\Users\mksol\\Pictures\\Saved Pictures\\fix_img-u1BM.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)
d=cv2.CV_64F
sobely = cv2.Sobel(blur, d, 0, 1, 5)
cv2.imshow("Sobel Y",sobely)
cv2.waitkey(0)
cv2.destroyAllWindows()
