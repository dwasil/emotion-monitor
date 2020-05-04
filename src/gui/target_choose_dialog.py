import tkinter as tk
from tkinter import ttk
from ..sys.windows_enumerator import WindowsEnumerator
from Xlib import Xatom


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

    def _choose_command(self):
        print("choose_command")
        print(self._windows_list_combo.current())
        window = self._windows_enumerator.get_window_by_index(self._windows_list_combo.current())
        print(window)

    def _get_windows_list(self):
        result = []
        for window in self._windows_enumerator.get_windows_list():
            print(window.id)
            inst, cl = window.get_wm_class()
            result.append(inst)
        return result

    def show(self):
        self._windows_list_combo['values'] = self._get_windows_list()
        self._dialog.mainloop()