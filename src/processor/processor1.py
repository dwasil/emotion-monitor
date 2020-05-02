import cv2
from tensorflow.keras.models import load_model
from datetime import datetime
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

class Processor:

    def __init__(self):
        self._face_cascade = cv2.CascadeClassifier('/home/user/PycharmProjects/empathy_assistant/resources/haarcascade_frontalface_default.xml')
        # @see https://towardsdatascience.com/face-detection-recognition-and-emotion-detection-in-8-lines-of-code-b2ce32d4d5de
        self._emotion_detector_model = load_model("/home/user/PycharmProjects/empathy_assistant/resources/model_v6_23.hdf5")

    def detect_faces(self, gray_frame):
        return self._face_cascade.detectMultiScale(gray_frame, 1.2, 4)

    def draw_face(self, frame, face_data, emotion):
        class_labels = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}
        x, y, w, h = face_data
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.putText(
            frame,
            str(class_labels[emotion]),
            (x,y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        return frame

    def predict_emotion(self, face_frame):
        roi_gray = cv2.resize(face_frame, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        return np.argmax(self._emotion_detector_model.predict(roi)[0])

    def process(self, frame):

        start_time = datetime.now() ###
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces_data = self.detect_faces(gray_frame)

        for (x, y, w, h) in faces_data:
            emotion = self.predict_emotion(gray_frame[y:y + h, x:x + w])
            frame = self.draw_face(frame, (x, y, w, h), emotion)
            print(str(emotion))

        print("Time: " + str(datetime.now() - start_time) + "\n")  ###
        return frame
