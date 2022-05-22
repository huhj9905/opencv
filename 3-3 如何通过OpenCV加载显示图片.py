import cv2
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('perspective.jpeg')  # 可以导入新图片，并且显示出来
cv2.imshow('img', img)
key = cv2.waitKey(0)
if key == 'q':
    exit()
cv2.destroyAllWindows()




