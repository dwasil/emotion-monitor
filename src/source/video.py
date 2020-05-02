import cv2
from .base import Base


class Video(Base):

    def __init__(self, file_path):
        self._capture = cv2.VideoCapture(file_path)

    def get_current_frame(self):
        ret, frame = self._capture.read()
        return frame

    def destroy(self):
      self._capture.release()