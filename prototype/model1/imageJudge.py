import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

def estimate_pose(image_path):
    # 画像を設定した高さと幅で読み込む
    image = cv2.imread(image_path)
    # 画像をリサイズする.高さのみを指定し、幅はアスペクト比を保持して自動的に計算される
    # 元の画像の幅と高さを取得
    original_height, original_width = image.shape[:2]

    # 新しい高さを指定
    new_height = 900

    # アスペクト比を保持するための新しい幅を計算
    new_width = int(new_height * original_width / original_height)

    # 新しい幅と高さで画像をリサイズ
    image = cv2.resize(image, (new_width, new_height))

    with mp.solutions.pose.Pose(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as pose:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp.solutions.pose.POSE_CONNECTIONS)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
