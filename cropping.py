import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Crop the image
crop_image = image[100:300, 200:400]

# Display the original and the cropped image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(crop_image, cv2.COLOR_BGR2RGB)), plt.title('Cropped Image')
plt.show()