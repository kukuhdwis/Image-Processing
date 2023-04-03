import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the original and the RGB image
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(rgb_image), plt.title('RGB Image')
plt.show()