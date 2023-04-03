import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Get the height and width of the image
height, width = image.shape[:2]

# Define the rotation matrix with angle 45 degrees and scale 1.0
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1.0)

# Perform the rotation on the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and the rotated image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)), plt.title('Rotated Image')
plt.show()