import tkinter as tk
from tkinter import ttk
from ..sys.windows_enumerator import WindowsEnumerator


class TargetChooseDialog:

    def __init__(self, windows_enumerator: WindowsEnumerator):
        self._windows_enumerator = windows_enumerator
        self._dialog = tk.Tk()
        self._dialog.geometry('300x100')
        self._dialog.title("Empathy Assistant")
        labelTop = tk.Label(self._dialog, text="Choose target window")
        labelTop.grid(column=0, row=0)
        self._windows_list_combo = ttk.Combobox(self._dialog, values=[])
        self._windows_list_combo.grid(column=0, row=1)
        tk.Button(self._dialog, text="Choose", command=self._choose_command).grid(column=0, row=2)
        self._on_window_changer_cb = None

    def _choose_command(self):
        print('_choose_command')
        window = self._windows_enumerator.get_window_by_index(self._windows_list_combo.current())
        print(window)
        print(self._on_window_changer_cb)

        if self._on_window_changer_cb is not None:
            self._on_window_changer_cb(window)

       # self._dialog.destroy()

    def _get_windows_list(self):
        result = []
        for window in self._windows_enumerator.get_windows_list():
            print(window.id)
            inst, cl = window.get_wm_class()
            result.append(inst)
        return result

    def show(self, on_window_changed_cb):
        self._on_window_changer_cb = on_window_changed_cb
        self._windows_list_combo['values'] = self._get_windows_list()
        self._dialog.mainloop()