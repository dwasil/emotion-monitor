import cv2
from datetime import datetime
import numpy as np
from deepface.extendedmodels import Emotion
from tensorflow.keras.preprocessing.image import img_to_array


class Processor:

    def __init__(self):
        self._face_cascade = cv2.CascadeClassifier('/home/user/PycharmProjects/empathy_assistant/resources/haarcascade_frontalface_default.xml')

    def detect_faces(self, gray_frame):
        return self._face_cascade.detectMultiScale(gray_frame, 1.2, 4)

    def predict_emotion(self, face_frame):
        roi_gray = cv2.resize(face_frame, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        emotion_model = Emotion.loadModel()
        emotion_predictions = emotion_model.predict(roi)[0, :]
        return int(np.argmax(emotion_predictions))

    def process(self, frame):

        result = []
        start_time = datetime.now() ###
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_data = self.detect_faces(gray_frame)

        for (x, y, w, h) in faces_data:
            emotion_id = self.predict_emotion(gray_frame[y:y + h, x:x + w])
            result.append((x, y, w, h, emotion_id))

        # print("Process time: " + str(datetime.now() - start_time) + "\n")  ###
        return result
