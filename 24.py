import numpy as np
import cv2
def high_boost_filter(image, kernel_size, strength):
    laplacian_kernel = np.array([[0, -1, 0],
                                  [-1, 4, -1],
                                  [0, -1, 0]])
    
    laplacian = cv2.filter2D(image, -1, laplacian_kernel)
    
    scaled_laplacian = strength * laplacian
    
    scaled_laplacian = scaled_laplacian.astype(np.uint8)
    
    sharpened = cv2.add(image, scaled_laplacian)
    
    return sharpened

image = cv2.imread("C:\\Users\\mksol\\Pictures\\Saved Pictures\\fix_img-qaoJ.jpg")
sharpened_image = high_boost_filter(image, kernel_size=3, strength=1.5)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
