from gi.repository import Gtk, Gdk

w1 = Gtk.Window()
w2 = Gtk.Window()

def w2_hide(widget, event):
    w2.set_opacity(0.25)

def w2_show(widget, event):
    w2.set_opacity(0.75)

def w2_click(widget, event):
    w2.hide()

w1.set_size_request(600, 400)
w2.set_transient_for(w1)
w2.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)

w1.show()
w2.show()
w2_show(w2, None)

w1.connect("destroy", Gtk.main_quit)
w2.connect("leave-notify-event", w2_hide)
w2.connect("enter-notify-event", w2_show)
w2.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
w2.connect("button-press-event", w2_click)

Gtk.main()