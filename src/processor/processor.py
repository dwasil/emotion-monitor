import cv2


class Processor:

    def process(self, frame):

        face_cascade = cv2.CascadeClassifier('/home/user/PycharmProjects/empathy_assistant/resources/haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return frame
