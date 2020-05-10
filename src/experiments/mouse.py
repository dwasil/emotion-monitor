import Xlib
import Xlib.display
from Xlib import X

def main():
    display = Xlib.display.Display()
    root = display.screen().root
    root.grab_pointer(True, X.ButtonPressMask, X.GrabModeAsync, X.GrabModeAsync, 0, 0, X.CurrentTime)

    while True:
        event = root.display.next_event()
        print(event)
        break

if __name__ == "__main__":
    main(  )