from .base import Base
from .emotion_map import EmotionMap

class ApplicationTWindow(Base):

    def __init__(self, window):
        self._window = window

    def show_result(self, data):

        if self._window is not None:

            self._window.rectangles = []

            for item_data in data:
                x, y, w, h, emotion_id = item_data

                self._window.rectangles.append([x, y, w, h, EmotionMap.map2[emotion_id][0], EmotionMap.map2[emotion_id][1]])

            self._window.queue_draw()