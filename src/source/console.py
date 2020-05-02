import cv2
from .base import Base


class Console(Base):

    def __init__(self, file_path):
        self._file_path = file_path

    def get_current_frame(self):
        return cv2.imread(self._file_path, cv2.IMREAD_COLOR)
