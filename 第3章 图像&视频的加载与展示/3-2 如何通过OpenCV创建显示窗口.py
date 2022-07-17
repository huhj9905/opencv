import cv2


# 创建和显示窗口
cv2.namedWindow('new', cv2.WINDOW_NORMAL)  # 创建窗口
cv2.imshow('new', 0)  # 展示窗口
key = cv2.waitKey(0)  # 窗口显示时间，单位 毫秒 ,返回key。
if key == 'q':
    exit()
cv2.destroyAllWindows()