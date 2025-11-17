import cv2
import numpy as np

img = cv2.imread("cat.jpeg")
h, w = img.shape[:2]

rot_mat = cv2.getRotationMatrix2D((w//2, h//2), 45, 1)
rotated = cv2.warpAffine(img, rot_mat, (w, h))

crop = img[50:250, 50:250]

brightness = cv2.convertScaleAbs(img, alpha=1, beta=60)

cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)
cv2.imshow("Cropped", crop)
cv2.imshow("Brightened", brightness)

cv2.waitKey(0)
cv2.destroyAllWindows()
