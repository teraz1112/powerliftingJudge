import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def estimate_pose(video_path):
    # 動画の読み込み
    cap = cv2.VideoCapture(video_path)

    # Pose推定のためのモデルを読み込む
    with mp_pose.Pose(
        min_detection_confidence=0.1,
        min_tracking_confidence=0.7) as pose:
        while cap.isOpened():
            # 動画から1フレームを読み込む
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                break
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # 1フレームごとにPose推定を実行
            results = pose.process(image)

            # 検出されたポーズの骨格をカメラ画像に重ねて描画
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()

# 動画のパスを指定してPose推定を実行
video_path = "../src/movie/frontSquat2.MP4"
estimate_pose(video_path)
