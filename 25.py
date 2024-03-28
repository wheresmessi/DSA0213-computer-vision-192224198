import cv2
import numpy as np

def sharpen_image(image_path, kernel_size=5, threshold=0.2, sharpening_factor=2):
  """
  Sharpens an image using gradient masking.

  Args:
      image_path (str): Path to the image file.
      kernel_size (int, optional): Kernel size for Gaussian blurring. Defaults to 5.
      threshold (float, optional): Threshold for the gradient mask. Defaults to 0.2.
      sharpening_factor (float, optional): Sharpening factor. Defaults to 2.

  Returns:
      numpy.ndarray: The sharpened image.
  """
  image = cv2.imread(image_path)

  blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

  sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
  sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

  magnitude, _ = cv2.cartToPolar(sobel_x, sobel_y, angleInDegrees=True)
  mask = np.where(magnitude > threshold, 1, 0)

  sharpened_image = image + sharpening_factor * mask * (image - blurred_image)

  return sharpened_image

# Example usage
image = sharpen_image('C:\\Users\\mksol\\Pictures\\Saved Pictures\\fix_img-qaoJ.jpg')

# Display or save the sharpened image
cv2.imshow('Sharpened Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Alternatively, save the sharpened image
cv2.imwrite('sharpened_image.jpg', image)
