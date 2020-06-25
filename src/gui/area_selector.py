import gi
import cairo
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class AreaSelector:

    def __init__(self, on_area_selected_cb):
        self._on_area_selected_cb = on_area_selected_cb
        root_window = Gdk.get_default_root_window()
        geometry = root_window.get_geometry()
        self._start_x = 0
        self._start_y = 0
        self._current_x = 0
        self._current_y = 0
        self._is_button_pressed = False
        self._window = Gtk.Window()
        da = Gtk.DrawingArea()
        da.connect("draw", self._draw_rectangle)
        self._window.add(da)
        self._window.set_size_request(geometry.width, geometry.height)
        self._window.move(0, 0)
        self._window.set_decorated(False)
        self._window.connect("destroy", Gtk.main_quit)
        self._window.connect("button-press-event", self._button_click)
        self._window.connect("button_release_event", self._button_release)
        self._window.connect("key-press-event", Gtk.main_quit)
        self._window.connect("motion_notify_event", self._on_motion_notify)


    def show(self):
        self._window.show_all()
        self._window.set_opacity(0.5)

    def _button_click(self, w, e):
        self._is_button_pressed = True
        self._start_x, self._start_y = e.x, e.y

    def _draw_rectangle(self, w, cr):

        if self._is_button_pressed:
            cr.set_source_rgba(0, 0, 0, 1)
            cr.set_line_width(3)
            cr.set_line_join(cairo.LINE_JOIN_BEVEL)
            cr.rectangle(self._start_x, self._start_y, self._current_x - self._start_x, self._current_y - self._start_y)
            cr.stroke()

    def _button_release(self, w, e):

        if not self._is_button_pressed:
            return

        self._is_button_pressed = False
        self._window.hide()
        self._on_area_selected_cb(
            int(self._start_x),
            int(self._start_y),
            int(e.x - self._start_x),
            int(e.y - self._start_y)
        )

    def _on_motion_notify(self, w, e):
        if self._is_button_pressed:
            self._current_x, self._current_y = e.x, e.y
            w.queue_draw()


if __name__ == "__main__":
    selector = AreaSelector(
        lambda x1, y1, x2, y2: print(x1, y1, x2, y2)
    )
    selector.show()
    Gtk.main()