import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Images/opencv-logo.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 55, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Total no of contours : " + str(len(contours)))

cv2.drawContours(img, contours, -1, (255, 255, 0), 3)
cv2.imshow("image", img)
cv2.imshow("image_gray", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
