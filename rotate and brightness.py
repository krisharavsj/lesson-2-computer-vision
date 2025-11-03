import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread('large.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

(h,w)=image.shape[:2]
centre=(w//2,h//2)
M=cv2.getRotationMatrix2D(centre,45,1.0)
rotated=cv2.warpAffine(image,M,(h,w))

rotated_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("rotated image")
plt.show()

brighter_matrix=np.ones(image.shape,dtype="uint8")*50
brighter=cv2.add(image,brighter_matrix)

brighter_rgb=cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("brightness image")
plt.show()