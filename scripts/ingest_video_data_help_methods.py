import numpy as np
import cv2

def darkSetting(filepath: str):
    cap = cv2.VideoCapture(filepath)
    nbr_frames=0
    class_sum = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        meanpercent = np.mean(im_gray) * 100 / 255
        frame_classification = 1 if meanpercent > 50 else 0
        class_sum = class_sum + frame_classification
        nbr_frames += 1

    video_dark_setting = "dark" if class_sum/nbr_frames < 0.5 else "light"
    return video_dark_setting