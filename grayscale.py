import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and the Grayscale image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(gray_image, cmap='gray'), plt.title('Grayscale Image')
plt.show()