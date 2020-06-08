import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk

# full screenshot
window = Gdk.get_default_root_window()
pb = Gdk.pixbuf_get_from_window(window, *window.get_geometry())
pb.savev("sshot.png", "png", (), ())

'''
# screenshots for all windows
window = Gdk.get_default_root_window()
screen = window.get_screen()
typ = window.get_type_hint()
for i, w in enumerate(screen.get_window_stack()):
    pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
    pb.savev("{}.png".format(i), "png", (), ())

# screenshot active window
screen = Gdk.get_default_root_window().get_screen()
w = screen.get_active_window()
pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
pb.savev("active.png", "png", (), ())
'''