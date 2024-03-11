import movieJudge as s1
import imageJudge as ip
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def main():
    # 動画のパスを指定してPose推定を実行
    s1.estimate_pose("../../src/movie/frontSquat.MP4")
    ip.estimate_pose("./l_min_img.jpg")

if __name__ == "__main__":
    main()