import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Split the color channels of the image
b, g, r = cv2.split(image)

# Display the original and the split channels of the image
plt.subplot(221), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(222), plt.imshow(b, cmap='gray'), plt.title('Blue Channel')
plt.subplot(223), plt.imshow(g, cmap='gray'), plt.title('Green Channel')
plt.subplot(224), plt.imshow(r, cmap='gray'), plt.title('Red Channel')
plt.show()
