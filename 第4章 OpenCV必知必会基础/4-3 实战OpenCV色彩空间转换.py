import cv2
import cv2 as cv


def callback():
    pass


# 创建窗口
cv.namedWindow('color', cv2.WINDOW_NORMAL)
# 读取图片
img = cv.imread('OET.png')

# 定义颜色空间
colorspaces = [cv.COLOR_BGR2RGBA, cv.COLOR_BGR2BGRA,
               cv.COLOR_BGR2GRAY, cv.COLOR_BGR2HSV_FULL,
               cv.COLOR_BGR2YUV]
cv.createTrackbar('curcolor', 'color', 0, 4, callback)

while True:
    index = cv.getTrackbarPos('curcolor', 'color')

    # 颜色空间转换
    cvt_img = cv.cvtColor(img, colorspaces[index])

    # 图片展示
    cv.imshow('color', cvt_img)

    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()