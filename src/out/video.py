import cv2
from .base import Base


class Video(Base):

    def __int__(self):
        self._window_name = 'test'

    def show_result(self, result_data):
        cv2.imshow('test', result_data)

    def destroy(self):
       cv2.destroyAllWindows()
