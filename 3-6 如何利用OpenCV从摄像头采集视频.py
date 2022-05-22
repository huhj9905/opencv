import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)

# 获取视频设备
cap = cv2.VideoCapture(0)
cv2.resizeWindow('video', 640, 480)
while True:
    # 从摄像头读取视频帧
    cap, frame = cap.read()  # 状态值，视频帧
    # 将视频帧在窗口显示
    cv2.imshow('video', frame)
    # 等待键盘事件
    key = cv2.waitKey(5)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows() # 释放资源









