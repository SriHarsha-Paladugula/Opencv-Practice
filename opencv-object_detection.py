import numpy as np
import cv2


def nothing(x):
    pass


cv2.namedWindow('Tracking')


cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)


while True:
    img = cv2.imread('/home/sriharsha.p/Personal/Opencv-Practice/Images/smarties.png')
    cv2.imshow('image', img)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(img_hsv, l_b, u_b)
    cv2.imshow('mask', mask)

    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('masked_image', res)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()