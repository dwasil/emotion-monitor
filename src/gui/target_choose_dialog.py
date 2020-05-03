import tkinter as tk
from tkinter import ttk


class TargetChooseDialog:
    def __init__(self):
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

    def show(self, windows_list):
        self._windows_list_combo['values'] = windows_list
        self._dialog.mainloop()