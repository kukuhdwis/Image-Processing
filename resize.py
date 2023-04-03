import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Resize the image to 30x30, 90x90, and 120x120
resized_30 = cv2.resize(image, (30, 30))
resized_90 = cv2.resize(image, (90, 90))
resized_120 = cv2.resize(image, (120, 120))

# Display the original and resized images
plt.subplot(221), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(222), plt.imshow(cv2.cvtColor(resized_30, cv2.COLOR_BGR2RGB)), plt.title('Resized to 30x30')
plt.subplot(223), plt.imshow(cv2.cvtColor(resized_90, cv2.COLOR_BGR2RGB)), plt.title('Resized to 90x90')
plt.subplot(224), plt.imshow(cv2.cvtColor(resized_120, cv2.COLOR_BGR2RGB)), plt.title('Resized to 120x120')
plt.show()
