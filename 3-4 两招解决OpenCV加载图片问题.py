# 语法检测有问题
# windows下访问图片的路径与Mac\linux上不同

import cv2
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('perspective.jpeg')  # 可以导入新图片，并且显示出来
cv2.imshow('img', img)
key = cv2.waitKey(0)
print(key)  # 113
print('q')  # q
print(ord('q')) # 113
if (key & 0xFF ) == ord('q'):
    print('111')
    exit()
cv2.destroyAllWindows()













