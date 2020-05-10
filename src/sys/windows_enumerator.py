from Xlib import display, X
import time

class WindowsEnumerator:

    def __init__(self):
        self._windows_list = []
        disp = display.Display()

        time.sleep(5)
        
        res = disp.screen().root.query_pointer()
        window = res.child
        print(window.id)
        d = display.Display()
        gc = window.create_gc()
        window.draw_text(gc, 200, 200, str.encode(str(window.id)))  # changed the coords more towards the center
        window.rectangle(gc, 100, 100, 100, 100, onerror=None)
        d.flush()

        self._init_windows_list(disp.screen().root)


    def get_windows_list(self):
        return self._windows_list

    def get_window_by_index(self, index):
        return self._windows_list[index]

    def _init_windows_list(self, window):

        if self._is_window_compatible(window):
            self._windows_list.append(window)

        for child in window.query_tree().children:
            self._init_windows_list(child)

    def _is_window_compatible(self, window) -> bool:

        d = display.Display()
        gc = window.create_gc()

        if gc:
            if window.id == 85983364:
                a = 1

            window.draw_text(gc, 220, 220, str.encode(str(window.id)))  # changed the coords more towards the center
            window.rectangle(gc, 100, 100, 100, 100, onerror=None)
            d.flush()  # To actually send the request to the server

        attrs = window.get_attributes()
        if attrs.map_state != X.IsViewable:
            return False

        geometry = window.get_geometry()
        if geometry.x < 0 or geometry.y < 0 or geometry.width < 150 or geometry.height < 150:
            return False

        win_class = window.get_wm_class()
        if win_class is None:
            return False

        inst, cl = win_class
        if inst == 'desktop_window':
            return False

        return True

