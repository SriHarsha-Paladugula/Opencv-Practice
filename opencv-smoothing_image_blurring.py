import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Images/lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
hom_img = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
guassian_blur = cv2.GaussianBlur(img, (5, 5), 0)
median_blur = cv2.medianBlur(img, 7)
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)

images = [img, hom_img, blur, guassian_blur, median_blur, bilateral_filter]
titles = ['image', 'hom_img', 'blur', 'guassian_blur', 'median_blur', 'bilateral_filter']

for i in range(len(images)):
    plt.subplot(3, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
