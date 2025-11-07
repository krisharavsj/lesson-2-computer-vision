import cv2

img = cv2.imread("medium.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 50 and h > 50:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.arrowedLine(img, (x, y - 20), (x + w, y - 20), (255, 0, 0), 2)
        cv2.arrowedLine(img, (x + w, y - 20), (x, y - 20), (255, 0, 0), 2)
        cv2.putText(img, f"Width: {w}px", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

cv2.imshow("Annotated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
