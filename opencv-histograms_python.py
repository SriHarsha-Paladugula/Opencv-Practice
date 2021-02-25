import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Images/lena.jpg")
b, g, r = cv2.split(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)

# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
# plt.show()

hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
