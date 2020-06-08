
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk


win = Gtk.Window()


def button_press_event(w, event):
    print(w.get_pointer())
    rootwin = w.get_screen().get_root_window()
    print(rootwin.get_pointer())
    print(event)



win.set_title('test')
win.connect('delete-event', Gtk.main_quit)
win.connect("button_press_event", button_press_event)

win.show_all()

Gtk.main()