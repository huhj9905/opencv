import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)

# 获取视频设备/读取视频文件。
cap = cv2.VideoCapture(r'20220518_145442.mp4')
# cv2.resizeWindow('video', 640, 480)
# 设置视频播放间隔
interval = int(1000 / 24)
while True:
    # 从摄像头读取视频帧
    ret, frame = cap.read()  # 状态值，视频帧
    # 将视频帧在窗口显示
    cv2.imshow('video', frame)
    # 等待键盘事件
    key = cv2.waitKey(interval)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()  # 释放资源
