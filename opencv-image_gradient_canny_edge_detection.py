import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Images/messi5.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(lap))

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel_y = np.uint8(np.absolute(sobel_y))

sobelCombined = cv2.bitwise_or(sobel_y, sobel_x)


def nothing(x):
    pass


images = [img, laplacian, sobel_x, sobel_y, sobelCombined]
titles = ["image", "laplacian", "sobel_x", "sobel_y", "sobelCombined", "canny"]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.namedWindow("Tracking")
cv2.createTrackbar("th1", "Tracking", 0, 255, nothing)
cv2.createTrackbar("th2", "Tracking", 0, 255, nothing)

while True:
    th1 = cv2.getTrackbarPos("th1", "Tracking")
    th2 = cv2.getTrackbarPos("th2", "Tracking")

    canny = cv2.Canny(img, th1, th2)

    cv2.imshow("canny", canny)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
