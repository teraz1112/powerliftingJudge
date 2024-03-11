import cv2

def show_camera_input():
    # カメラのキャプチャを作成
    cap = cv2.VideoCapture(0)

    while True:
        # フレームをキャプチャ
        ret, frame = cap.read()

        # フレームが正常にキャプチャされた場合
        if ret:
            # フレームを表示
            cv2.imshow('Camera Input', frame)

        # 'q'キーが押された場合はループを終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # キャプチャを解放してウィンドウを閉じる
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
# カメラの入力画像を表示する関数を呼び出す
    show_camera_input()
