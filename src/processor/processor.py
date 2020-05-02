import cv2
from datetime import datetime

class Processor:

    def __init__(self):
        self._face_cascade = cv2.CascadeClassifier('/home/user/PycharmProjects/empathy_assistant/resources/haarcascade_frontalface_default.xml')
        self._eye_cascade = cv2.CascadeClassifier('/home/user/PycharmProjects/empathy_assistant/resources/haarcascade_eye_tree_eyeglasses.xml')

    def detect_faces(self, gray_frame):
        return self._face_cascade.detectMultiScale(gray_frame, 1.2, 4)

    def detect_eyes(self, gray_frame):
        return self._eye_cascade.detectMultiScale(gray_frame, 1.2, 4)

    def draw_faces(self, frame, faces_data):

        for (x, y, w, h) in faces_data:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return frame

    def draw_eyes(self, frame, eyes_data, x_bias, y_bias):

        for (x, y, w, h) in eyes_data:
            cv2.rectangle(frame, (x + x_bias, y + y_bias), (x + x_bias + w, y + y_bias + h), (255, 0, 0), 2)

        return frame

    def process(self, frame):

        start_time = datetime.now() ###
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_data = self.detect_faces(gray_frame)

        for (x, y, w, h) in faces_data:
            face_gray_frame = gray_frame[y:y + h, x:x + w]
            eyes_data = self.detect_eyes(face_gray_frame)
            frame = self.draw_eyes(frame, eyes_data, x, y)

        frame = self.draw_faces(frame, faces_data)

        print("Time: " + str(datetime.now() - start_time) + "\n")  ###
        return frame
