import cv2
import matplotlib.pyplot as plt


img = cv2.imread("./Images/lena.jpg")
cv2.imshow("lena", img)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
