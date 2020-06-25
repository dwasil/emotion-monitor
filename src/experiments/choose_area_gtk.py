import gi
import cairo
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

root_window = Gdk.get_default_root_window()
geometry = root_window.get_geometry()

x1, y1, x2, y2 = 0, 0, 0, 0
isButtonPressed = False
isFrameCreated = False


def button_click(w, e):
    global x1, y1, isButtonPressed
    x1, y1 = e.x, e.y
    isButtonPressed = True


def button_release(w, e):

    global isFrameCreated

    if isFrameCreated:
        return

    global x1, y1, x2, y2, isButtonPressed
    isButtonPressed = False
    x2, y2 = e.x, e.y
    w2 = Gtk.Window()
    w2.set_title('emotion monitor')
    w2.move(x1, y1)
    w2.set_size_request(x2 - x1, y2 - y1)
    w2.show()
    w2.set_opacity(0.3)
    w2.connect("destroy", Gtk.main_quit)
    w2.connect("key-press-event", Gtk.main_quit)
    w.hide()
    isFrameCreated = True


def on_motion_notify(w, e):
    global x2, y2, isButtonPressed
    x2, y2 = e.x, e.y

    w.queue_draw()


def draw_rectangle(w, context):
    global x1, y1, x2, y2, isButtonPressed

    if isButtonPressed:
        context.set_source_rgba(1, 0, 0, 0.5)
        context.set_line_width(3)
        context.set_line_join(cairo.LINE_JOIN_BEVEL)
        context.rectangle(x1, y1, x2 - x1, y2 - y1)
        context.stroke()

window = Gtk.Window()
window.set_size_request(geometry.width, geometry.height)
window.move(0, 0)
window.set_decorated(False)
window.show()
window.set_opacity(0.5)
window.connect("destroy", Gtk.main_quit)
window.connect("button-press-event", button_click)
window.connect("button_release_event", button_release)
window.connect("key-press-event", Gtk.main_quit)
window.connect("motion_notify_event", on_motion_notify)

da=Gtk.DrawingArea()
da.connect("draw", draw_rectangle)
window.add(da)
window.show_all()

Gtk.main()