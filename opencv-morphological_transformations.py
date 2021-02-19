import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("./Images/smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3, 3), np.uint8)
dilated_img = cv2.dilate(mask, kernel, iterations=2)
eroded_img = cv2.erode(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # erode followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # dilation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)  # difference between dilated and eroded
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)  # difference between image and opening of image

images = [img, mask, dilated_img, eroded_img, opening, closing, mg, th]
titles = ["original_image", "mask", "dilated_img", "eroded_img", "opening", "closing", "gradient", "tophat"]

for i in range(len(images)):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
