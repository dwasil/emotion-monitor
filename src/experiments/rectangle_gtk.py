import gi
import cairo
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

def draw_rectangle(w, context):
    print('draw_rectangle')

    context.set_line_width(3)
    context.set_source_rgba(0, 0, 0, 1)
    context.rectangle(100, 100, 500, 500)
    context.stroke()

window = Gtk.Window()
window.set_default_size(500, 500)
window.move(100, 100)
window.connect("destroy", Gtk.main_quit)


da=Gtk.DrawingArea()
da.connect("draw", draw_rectangle)
window.add(da)
window.show_all()

Gtk.main()