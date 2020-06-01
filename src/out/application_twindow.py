from .base import Base
import Xlib.display, Xlib.X, Xlib.Xutil, Xlib.X as X
from .emotion_map import EmotionMap
from ..gui.window_gtk import WindowGTK

class ApplicationTWindow(Base):

    def __init__(self, window):
        self._window = window
        self._display = Xlib.display.Display()
        self._screen = self._display.screen()
        geometry = self._window.get_geometry()
        self._gtk_window = WindowGTK(geometry.x, geometry.y, geometry.width, geometry.height)
        self._gtk_window.show()

    def show_result(self, data):

        if self._window is not None:

            self._gtk_window.rectangles = []

            for item_data in data:
                x, y, w, h, emotion_id = item_data

                self._gtk_window.rectangles.append([x, y, w, h, EmotionMap.map2[emotion_id][0], EmotionMap.map2[emotion_id][1]])

            self._gtk_window.queue_draw()