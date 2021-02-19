import cv2
import matplotlib.pyplot as plt
img = cv2.imread("./Images/gradient.png")

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

images = [img, th1, th2, th3, th4, th5]
titles = ['Original', 'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV']

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

'''
cv2.imshow('image', img)
cv2.imshow('THRESH_BINARY', th1)
cv2.imshow('THRESH_BINARY_INV', th2)
cv2.imshow('THRESH_TRUNC', th3)
cv2.imshow('THRESH_TOZERO', th4)
cv2.imshow('THRESH_TOZERO_INV', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''