#!/usr/bin/python

# Python 2/3 compatibility.
from __future__ import print_function

import sys
import os

# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib import display, X, threaded
import time
import _thread

def redraw(win, gc):
    # win.clear_area()
    win.rectangle(gc, 20, 20, 60, 60, onerror=None)

def blink(display, win, gc, cols):
    while 1:
        time.sleep(2)
        print('Changing color', cols[0])
        gc.change(foreground = cols[0])
        cols = (cols[1], cols[0])
        redraw(win, gc)
        display.flush()

def main():

    d = display.Display()
    root = d.screen().root
    print(d.screen().root.list_installed_colormaps())
    exit(1)

    colormap = d.screen().default_colormap

    red = colormap.alloc_named_color("red").pixel
    blue = colormap.alloc_named_color("green").pixel
    background = colormap.alloc_named_color("white").pixel

    window = root.create_window(300, 300, 100, 100, 1,
        X.CopyFromParent, X.InputOutput,
        X.CopyFromParent,
        background_pixel = 0,
        event_mask = X.StructureNotifyMask | X.ExposureMask)

    window.map()

    gc = window.create_gc(
        foreground = red,
        line_width=4
    )

    _thread.start_new_thread(blink, (d, window, gc, (blue, red)))

    while 1:
        event = d.next_event()
        if event.type == X.Expose:
            if event.count == 0:
                redraw(window, gc)
        elif event.type == X.DestroyNotify:
            sys.exit(0)

if __name__ == "__main__":
    main()
