from Xlib import display, X

disp = display.Display()

class TargetChooseDialog:

    def __init__(self, on_choose_cb):
        self._on_choose_cb = on_choose_cb

    def _init_windows_list(self, window):
        res = None
        attrs = window.get_attributes()

        if attrs.map_state == X.IsViewable:
            return window

        for child in window.query_tree().children:
            res = self._init_windows_list(child)
            if res:
                break

        return res

    def _print_win_list(self, win, indent):

        print(indent + str(win.get_wm_name()))
        print(indent + str(win.get_wm_class()))
        print(indent + str(win.get_geometry()))
        print(indent + str(win.get_attributes()))
        print("\n")

        for child in win.query_tree().children:
            self._print_win_list(child, indent + '-')

    def show(self):
        disp = display.Display()
        root = disp.screen().root
        root.grab_pointer(True, X.ButtonPressMask, X.GrabModeAsync, X.GrabModeAsync, 0, 0, X.CurrentTime)

        while True:
            event = root.display.next_event()

            if event:
                disp.ungrab_pointer(X.CurrentTime)
                res = root.query_pointer()
                self._print_win_list(res.child, '')
                window = self._init_windows_list(res.child)
                self._on_choose_cb(window)
                break

