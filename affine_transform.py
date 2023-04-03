import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Define the transformation matrix
matrix = np.float32([[1, 0.5, 50], [0.2, 1.2, 100]])

# Perform the affine transformation on the image
transformed_image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

# Display the original and the transformed image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)), plt.title('Transformed Image')
plt.show()