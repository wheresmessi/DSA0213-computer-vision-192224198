import cv2

def find_image_boundary(image):
  # Convert to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply thresholding (adjust threshold value as needed)
  _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

  # Find contours (boundaries)
  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Assuming largest contour is the image boundary
  if len(contours) > 0:
    largest_contour = max(contours, key=cv2.contourArea)
    return largest_contour
  else:
    return None

# Load image
image = cv2.imread("C:\\Users\\mksol\\Pictures\\Saved Pictures\\fix_img-qaoJ.jpg")

# Find image boundary
boundary = find_image_boundary(image.copy())

# Draw boundary on a copy of the image (optional)
if boundary is not None:
  image_copy = image.copy()
  cv2.drawContours(image_copy, [boundary], -1, (0, 255, 0), 2)
  cv2.imshow('Image with Boundary', image_copy)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("No significant boundary found")
