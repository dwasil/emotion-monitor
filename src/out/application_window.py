from .base import Base
import Xlib.display, Xlib.X
from .emotion_map import EmotionMap


class ApplicationWindow(Base):

    def __init__(self, window):
        self._window = window
        self._display = Xlib.display.Display()
        self._gc = None

    def _draw_rectangle(self, item_data):
        x, y, w, h, emotion_id = item_data

        if self._gc:
            self._gc.free()

        self._gc = self._window.create_gc(
            line_width=4,
            foreground= EmotionMap.map[emotion_id][1] # green 62740
        )
        self._window.clear_area()
        self._window.draw_text(self._gc, x, y, EmotionMap.map[emotion_id][0])
        self._window.rectangle(self._gc, x, y, w, h, onerror=None)

        self._display.flush()

    def show_result(self, data):
        if self._window is not None:
            for item_data in data:
                self._draw_rectangle(item_data)
