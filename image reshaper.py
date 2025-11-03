import cv2
image = cv2.imread("cartoon image.jpg")
sizes = {
    "small": (200, 200),
    "medium": (800, 800),
    "large": (500, 500),
}
for size_name, dimensions in sizes.items():
    resized = cv2.resize(image, dimensions)
    cv2.imwrite(f"{size_name}.jpg", resized)
    cv2.imshow(size_name, resized)
    cv2.waitKey(1000)
cv2.destroyAllWindows()