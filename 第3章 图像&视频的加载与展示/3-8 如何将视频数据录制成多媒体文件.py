import cv2

'''
视频录制

VideoWriter
参数一：输出文件
参数二：多媒体文件格式(VideoWriter_fourcc)
参数三：帧率
参数四：分辨率大小


write


release

'''
# 获取视频设备/读取视频文件。
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 创建VideoWriter为写作多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('./out.mp4', fourcc, 25, (int(cap.get(3)), int(cap.get(4))))



while cap.isOpened():
    # 从摄像头读取视频帧
    ret, frame = cap.read()  # 状态值，视频帧
    if ret:
        # 写数据到多媒体文件
        out.write(frame.astype('uint8'))
        # 创建窗口
        cv2.namedWindow('video', cv2.WINDOW_NORMAL)
        # 将视频帧在窗口显示
        cv2.imshow('video', frame)
        # 等待键盘事件
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
