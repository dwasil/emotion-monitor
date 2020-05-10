from Xlib import display, X

disp = display.Display()

class TargetChooseDialog:

    def __init__(self, on_choose_cb):
        self._on_choose_cb = on_choose_cb

    def _init_windows_list(self, window):
        res = None
        attrs = window.get_attributes()

        print('_init_windows_list')
        print(window.id)
        print(attrs)

        gc = window.create_gc(
            line_width=4,
            foreground=62740  # green 62740
        )
        window.draw_text(gc, 100, 100, str.encode(str(window.id)))

        if attrs.map_is_installed == 0 and attrs.map_state == X.IsViewable:
            res = window

        for child in window.query_tree().children:
            tmp_res = self._init_windows_list(child)

            if tmp_res:
                res = tmp_res

        return res

    def show(self):
        disp = display.Display()
        root = disp.screen().root
        root.grab_pointer(True, X.ButtonPressMask, X.GrabModeAsync, X.GrabModeAsync, 0, 0, X.CurrentTime)

        while True:
            event = root.display.next_event()

            if event:
                disp.ungrab_pointer(X.CurrentTime)
                res = root.query_pointer()

                window = self._init_windows_list(res.child)
                print('def show(self):')
                print(window.id)
                #exit(1)
                self._on_choose_cb(window)
                break

