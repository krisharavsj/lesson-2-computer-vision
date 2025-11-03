import cv2
import matplotlib.pyplot as plt

image=cv2.imread('large.jpg')

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("rgb image")
plt.show()

image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray,cmap='gray')
plt.title("gray scale image")
plt.show()

cropped_image=image[100:300,200:400]
cropped_rgb=cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped image")
plt.show()