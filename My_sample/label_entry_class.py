from tkinter import *


class LabelAndEntryMaker:
    def __init__(self, window, text, x, y, distance=80, data_type="str", state=None):
        Label(window, text=text).place(x=x, y=y)

        if data_type == "str":
            self.variable = StringVar()
        elif data_type == "int":
            self.variable = IntVar()
        elif data_type == "float":
            self.variable = DoubleVar()
        elif data_type == "bool":
            self.variable = BooleanVar()
        else:
            self.variable = StringVar()

        Entry(window, textvariable=self.variable, state=state).place(x=x + distance, y=y)
