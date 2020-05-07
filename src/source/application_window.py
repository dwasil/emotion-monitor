from .base import Base
from Xlib import X
import numpy as np
from PIL import Image

class ApplicationWindow(Base):

    def __init__(self, window):
        self._window = window

    def get_current_frame(self):

        result = None

        if self._window is not None:
            geometry = self._window.get_geometry()
            raw = self._window.get_image(0, 0, geometry.width, geometry.height, X.ZPixmap, 0xffffffff)
            pil_image = Image.frombytes('RGB', (geometry.width, geometry.height), raw.data, 'raw', 'BGRX')
            result = np.array(pil_image)
            result = result[:, :, ::-1].copy()

        return result
