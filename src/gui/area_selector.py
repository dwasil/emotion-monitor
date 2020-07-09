import cairo
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class AreaSelector:

    def __init__(self, on_area_selected_cb):
        self.on_area_selected_cb = on_area_selected_cb
        root_window = Gdk.get_default_root_window()
        geometry = root_window.get_geometry()
        self.start_x = 0
        self.start_y = 0
        self.current_x = 0
        self.current_y = 0
        self.is_button_pressed = False
        self.window = Gtk.Window()
        da = Gtk.DrawingArea()
        da.connect("draw", self.draw_rectangle)
        self.window.add(da)
        self.window.set_size_request(geometry.width, geometry.height)
        self.window.move(0, 0)
        self.window.set_decorated(False)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.connect("button-press-event", self.button_click)
        self.window.connect("button_release_event", self.button_release)
        self.window.connect("key-press-event", Gtk.main_quit)
        self.window.connect("motion_notify_event", self.on_motion_notify)

    def show(self):
        self.window.show_all()
        self.window.set_opacity(0.5)

    def button_click(self, w, e):
        self.is_button_pressed = True
        self.start_x, self.start_y = e.x, e.y

    def draw_rectangle(self, w, cr):

        if self.is_button_pressed:
            cr.set_source_rgba(0, 0, 0, 1)
            cr.set_line_width(3)
            cr.set_line_join(cairo.LINE_JOIN_BEVEL)
            cr.rectangle(self.start_x, self.start_y, self.current_x - self.start_x, self.current_y - self.start_y)
            cr.stroke()

        cr.select_font_face("cairo :monospace", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_source_rgba(0, 0, 1, 1)
        cr.set_font_size(30)
        cr.move_to(100, 40)
        cr.show_text('Select The Area With The Faces')

    def button_release(self, w, e):

        if not self.is_button_pressed:
            return

        self.is_button_pressed = False
        self.window.hide()
        self.on_area_selected_cb(
            int(self.start_x),
            int(self.start_y),
            int(e.x - self.start_x),
            int(e.y - self.start_y)
        )

    def on_motion_notify(self, w, e):
        if self.is_button_pressed:
            self.current_x, self.current_y = e.x, e.y
            w.queue_draw()


if __name__ == "__main__":
    selector = AreaSelector(
        lambda x1, y1, x2, y2: print(x1, y1, x2, y2)
    )
    selector.show()
    Gtk.main()
