import cv2
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from src.gui.window_gtk import WindowGTK
from src.source.base import Base
import numpy as np


class ScreenArea(Base):

    def __init__(self, window):
        self._window = window

    def array_from_pixbuf(self, p):
        " convert from GdkPixbuf to numpy array"
        w, h, c, r = (p.get_width(), p.get_height(), p.get_n_channels(), p.get_rowstride())
        assert p.get_colorspace() == GdkPixbuf.Colorspace.RGB
        assert p.get_bits_per_sample() == 8

        if p.get_has_alpha():
            assert c == 4
        else:
            assert c == 3

        assert r >= w * c
        a = np.frombuffer(p.get_pixels(), dtype=np.uint8)

        if a.shape[0] == w * c * h:
            return a.reshape((h, w, c))
        else:
            b = np.zeros((h, w * c), 'uint8')
            for j in range(h):
                b[j, :] = a[r * j:r * j + w * c]
            return b.reshape((h, w, c))


    def get_current_frame(self):
        window = Gdk.get_default_root_window()
        geometry = self._window.get_geometry()
        result = Gdk.pixbuf_get_from_window(window, geometry[0], geometry[1], geometry[2], geometry[3])
        return self.array_from_pixbuf(result)

if __name__ == "__main__":
    area = ScreenArea(
        WindowGTK(100, 100, 400, 400)
    )

    frame = area.get_current_frame()

    cv2.imshow('image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    Gtk.main()
