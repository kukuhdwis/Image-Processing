import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Get the height and width of the image
height, width = image.shape[:2]

# Define the translation matrix
translation_matrix = np.float32([[1, 0, 50], [0, 1, 100]])

# Perform the translation on the image
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Display the original and the translated image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB)), plt.title('Translated Image')
plt.show()
