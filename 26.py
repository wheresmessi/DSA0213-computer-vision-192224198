import cv2

def add_text_watermark(image, text, font_scale=0.5, color=(255, 255, 255), thickness=1):
  # Get image dimensions
  height, width, _ = image.shape

  # Create font
  font = cv2.FONT_HERSHEY_SIMPLEX

  # Get text size
  text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

  # Calculate text position (center of bottom area)
  text_x = int((width - text_size[0]) / 2)
  text_y = height - int(text_size[1] / 2)

  # Add text watermark
  cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness)

  return image

# Load image
image = cv2.imread('C:\\Users\\mksol\\Pictures\\Saved Pictures\\fix_img-qaoJ.jpg')

# Add watermark text
watermarked_image = add_text_watermark(image.copy(), 'Nandy randi')

# Display or save watermarked image
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
