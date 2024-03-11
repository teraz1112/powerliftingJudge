import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

def estimate_pose(image_path):
    # 画像を設定した高さと幅で読み込む
    image = cv2.imread(image_path)
    image = cv2.resize(image, (640, 480))

    # MediapipeのPose推定モデルを初期化する
    mp_pose = mp.solutions.pose.Pose()

    # 画像をRGBに変換する
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 画像をPose推定モデルに入力し、ポーズを推定する
    results = mp_pose.process(image_rgb)

    # 推定結果を表示する
    print(results.pose_landmarks)

    # 画像を表示する
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp.solutions.pose.POSE_CONNECTIONS)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 画像のパスを指定してポーズ推定を行う
image_path = "./img/IMG_2463.jpg"
estimate_pose(image_path)

