import cv2

if __name__ == '__main__':
    # 初始化摄像头
    cap = cv2.VideoCapture(0)

    while True:
        # 从摄像头读取帧
        ret, frame = cap.read()

        # 显示帧
        cv2.imshow('Video Stream', frame)

        # 按下 'Q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头和销毁所有 OpenCV 窗口
    cap.release()
    cv2.destroyAllWindows()
