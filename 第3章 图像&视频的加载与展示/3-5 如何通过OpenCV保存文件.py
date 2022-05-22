import cv2

'''
保持图片
'''

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('perspective.jpeg')  # 可以导入新图片，并且显示出来
while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(0)
    if (key & 0xFF) == ord('q'):
        print('exit')
        cv2.destroyAllWindows()
        break
    elif (key & 0xFF) == ord('s'):
        print('save')
        savename = 'perspective-副本.png'
        cv2.imwrite(savename, img)
