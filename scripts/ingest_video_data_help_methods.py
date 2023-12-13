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


def nbrPeopleInVideo(filepath: str):
    face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(filepath)
    nbr_frames=0
    people_sum = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        nbr_people = len(face_classifier.detectMultiScale(im_gray, minNeighbors = 4, minSize = (30, 30), scaleFactor = 1.3))
        people_sum += nbr_people        
        nbr_frames += 1

    avarage_nbr_people = round(people_sum/nbr_frames)
    return avarage_nbr_people

