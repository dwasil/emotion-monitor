import tkinter as tk
from tkinter import ttk


def choose_command(*args):
    print("choose_command")
    print(comboExample.current())

app = tk.Tk()
app.geometry('300x100')
app.title("Empathy Assistant")


labelTop = tk.Label(app,
                    text="Choose target window")

labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app,
                            values=[
                                "January",
                                "February",
                                "March",
                                "April"])

comboExample.grid(column=0, row=1)

tk.Button(app, text="Calculate", command=choose_command).grid(column=0, row=3)

app.mainloop()