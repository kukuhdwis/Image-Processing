import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Define the source and destination points for the perspective transform
src_points = np.float32([[141, 131], [480, 159], [493, 630], [64, 601]])
dst_points = np.float32([[0, 0], [image.shape[1], 0], [image.shape[1], image.shape[0]], [0, image.shape[0]]])

# Calculate the perspective transform matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Perform the perspective transformation on the image
transformed_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))

# Display the original and the transformed image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)), plt.title('Transformed Image')
plt.show()
