import cv2

img = cv2.imread("./Images/sudoku.png", 0)

mean_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
guassian_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow("image", img)
cv2.imshow("mean_threshold", mean_threshold)
cv2.imshow("guassian_threshold", guassian_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()