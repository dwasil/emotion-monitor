from Xlib import display, X
import pyautogui


def show_window_thumbnail(x, y, width, height, window_name):
    im = pyautogui.screenshot(region=(x, y, width, height))
    im = im.resize((149, 149))
    im.show(window_name)

def print_win_list(win, indent):

    attrs = win.get_attributes()
    geometry = win.get_geometry()
    name = win.get_wm_name()
    win_class = win.get_wm_class()

    print(win_class)

    if win_class is not None:

        inst, cl = win_class

        if inst != 'desktop_window':

            print(inst)
            print(cl)

            if attrs.map_state == X.IsViewable \
                    and geometry.x >= 0 \
                    and geometry.y >= 0 \
                    and geometry.width >= 150 \
                    and geometry.height >= 150:

                print(indent + str(name))
                print(win.get_attributes())
                print(geometry)

                print("\n\n")

                show_window_thumbnail(geometry.x, geometry.y, geometry.width, geometry.height, 'win_class[0]')

    for child in win.query_tree().children:
        print_win_list(child, indent + '-')


disp = display.Display()

print_win_list(disp.screen().root, '-')

