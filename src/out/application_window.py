from .base import Base
import Xlib.display
import cv2


class ApplicationWindow(Base):

    def __init__(self, window):
        self._window = window

    def show_result(self, result_data):
        if self._window is not None:
            display = Xlib.display.Display()
            gc = self._window.create_gc()
            self._window.draw_text(gc, 100, 100, b"Hello, world!")  # changed the coords more towards the center
            display.flush()  # To actually send the request to the server
