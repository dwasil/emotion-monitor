from src.source.base import Base as BaseSource
from src.source.screen_area import ScreenArea

from src.processor.processor import Processor

from src.out.base import Base as BaseOut
from src.out.application_window import ApplicationWindow as ApplicationWindowOut
from src.out.application_twindow import ApplicationTWindow as ApplicationTWindowOut
from src.gui.window_gtk import WindowGTK

import threading

from src.gui.area_selector import AreaSelector

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class Application:

    def __init__(self, source: BaseSource, processor: Processor, out: BaseOut):
        self._source = source
        self._processor = processor
        self._out = out

    def run(self):
        print('run')
        frame = self._source.get_current_frame()

        if frame is None:
            return

        result_data = self._processor.process(frame)
        self._out.show_result(result_data)

    def destroy(self):
        self._source.destroy()
        self._out.destroy()

def run_application(x, y, width, height):

    window = WindowGTK(x, y, width, height)

    app = Application(
        ScreenArea(window),
        Processor(),
        ApplicationTWindowOut(window)
    )

    GObject.timeout_add(300, app.run)
    loop = GObject.MainLoop()
    loop.run()
    Gtk.main()
    return 0

if __name__ == "__main__":

    selector = AreaSelector(
        run_application
    )

    selector.show()
    Gtk.main()