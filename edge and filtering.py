import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(title,image):
    plt.figure(figsize=(8,8))
    if len(image.shape)==2:
        plt.imshow(image,cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
        plt.title('title')
        plt.axis('off')
        plt.show()

def interactive_edge_detection(image_path):
    image=cv2.imread(image_path)
    if image is None:
        print("ERROR,IMAGE NOT FOUND!")
        return
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    display_image('gray scale image', gray_image)
    print("select an option")
    print("1. Sobel edge detection")
    print("2. Canny edge detection")
    print("3. Laplacian edge detection")
    print("4. Gaussian smoothing")
    print("5. Median filtering")
    print("6. Exit")

    while True:
        choice=input("enter your choice: ")
        if choice=="1":
            sobelx=cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=3)
            sobely=cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=3)
            combine_sobel=cv2.bitwise_or(sobelx.astype(np.uint8),sobely.astype(np.uint8))
            display_image("sobel image",combine_sobel)
        else:
            print("invalid choice")
interactive_edge_detection('cartoon image.jpg')
