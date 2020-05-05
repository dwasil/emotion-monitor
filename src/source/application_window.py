from .base import Base
from ..gui.target_choose_dialog import TargetChooseDialog
from Xlib import X
from PIL import Image


class ApplicationWindow(Base):

    def __init__(self, choose_dialog: TargetChooseDialog):
        self._choose_dialog = choose_dialog
        self._choose_dialog.show(self._on_window_choosed)
        self._window = None

    def _on_window_choosed(self, window):
        print('_on_window_choosed')
        print(window)
        self._window = window

    def get_current_frame(self):
        print('get_current_frame')
        print(self._window)
        result = None

        if self._window is not None:
            print('get_current_frame 2')
            raw = self._window.get_image(0, 0, 100, 100, X.ZPixmap, 0xffffffff)
            print(raw)
            result = Image.fromstring('RGB', (100, 100), raw.data, 'raw', 'BGRX')
            print(result)

        return result
