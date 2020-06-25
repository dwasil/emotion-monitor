#!/usr/bin/env python

import cairo
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WindowGTK(Gtk.Window):
    def __init__(self, x, y, width, height):
        Gtk.Window.__init__(self, title = "Empathy Assistant")
        self.move(x, y)
        self.resize(width, height)
        self.screen = self.get_screen()
        self.visual = self.screen.get_rgba_visual()
        self.rectangles = []
        self.base = [x, y]

        if self.visual is not None and self.screen.is_composited():
            self.set_visual(self.visual)

        self.set_app_paintable(True)
        self.connect("draw", self.area_draw)
        self.connect("destroy", lambda x: exit())
        self.show_all()


    def show(self):
        self.show_all()
        self.set_opacity(0.5)

    def get_geometry(self):
        position = self.get_position()
        size = self.get_size()
        return position[0], position[1], size[0], size[1]

    def area_draw(self, widget, cr):
        cr.set_source_rgba(.1, .1, .1, 0.3)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

        if len(self.rectangles) > 0:
            for rec in self.rectangles:
                self.draw_rectangle(rec[0] , rec[1], rec[2], rec[3], rec[4], rec[5], cr)

    def draw_rectangle(self, x, y, width, height, text, color, cr):
        r, g, b, tr = color
        cr.set_source_rgba(r, g, b, tr)
        cr.set_line_width(3)
        cr.rectangle(x, y, width, height)
        cr.set_line_join(cairo.LINE_JOIN_BEVEL)
        cr.stroke()

        cr.select_font_face("cairo :monospace", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(20)
        cr.move_to(x, y - 10)
        cr.show_text(text)


if __name__ == "__main__":

    win = WindowGTK(300, 300, 600, 600)
    win.rectangles = [
        [30, 30, 100, 100, 'text1', [1, 1, 1, 1]],
        [120, 120, 200, 200, 'text2', [0, 0, 0, 1]]
    ]

    win.queue_draw()
    Gtk.main()


