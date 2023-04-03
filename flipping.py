import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Perform the horizontal flip on the image
flipped_image = cv2.flip(image, 1)

# Display the original and the flipped image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)), plt.title('Flipped Image')
plt.show()