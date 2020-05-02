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

    def draw_face(self, frame, face_data, emotion):
        x, y, w, h = face_data
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.putText(
            frame,
           str(emotion),
            (x,y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        return frame

    def predict_emotion(self, face_frame):
        emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        roi_gray = cv2.resize(face_frame, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        emotion_model = Emotion.loadModel()
        emotion_predictions = emotion_model.predict(roi)[0, :]
        return emotion_labels[int(np.argmax(emotion_predictions))]

    def process(self, frame):

        start_time = datetime.now() ###
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces_data = self.detect_faces(gray_frame)

        for (x, y, w, h) in faces_data:
            emotion = self.predict_emotion(gray_frame[y:y + h, x:x + w])
            frame = self.draw_face(frame, (x, y, w, h), emotion)

        print("Time: " + str(datetime.now() - start_time) + "\n")  ###
        return frame
