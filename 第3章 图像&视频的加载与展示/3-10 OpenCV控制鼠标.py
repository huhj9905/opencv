import cv2
import cv2 as cv

'''
setMouseCallback(winname,callback,userdata)
winname:窗口名称
callback:回调函数
userdata:传递的参数


callback(event,x,y,flags,userdata)
event:鼠标事件
x,y  坐标
flags:组合键
userdata:传递的值
'''

import cv2 as cv
import numpy as np

# 设置鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


cv.namedWindow('mouse', cv.WINDOW_NORMAL)
cv2.resizeWindow('mouse', 640, 360)

# 设置鼠标回调
cv.setMouseCallback('mouse', mouse_callback, '123')

img = np.zeros((360, 640, 3), np.uint8)

while True:
    cv.imshow('mouse', img)
    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()


