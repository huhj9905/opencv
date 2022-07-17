import cv2 as cv
import numpy as np


def callback():
    pass


# 创建窗口
cv.namedWindow('trackbar', cv.WINDOW_NORMAL)

# 创建trackbar
cv.createTrackbar('R', 'trackbar', 0, 255, callback)
cv.createTrackbar('G', 'trackbar', 0, 255, callback)
cv.createTrackbar('B', 'trackbar', 0, 255, callback)

img = np.zeros((480, 460, 3), np.uint8)

while True:
    # 获取rgb的值
    r = cv.getTrackbarPos('R', 'trackbar')
    g = cv.getTrackbarPos('G', 'trackbar')
    b = cv.getTrackbarPos('B', 'trackbar')
    # 将获取到的值赋值到img图像中
    img[:] = [b, g, r]
    # 将获取到的值显示出来
    cv.imshow('trackbar', img)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cv.destroyAllWindows()
