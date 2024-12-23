import tkinter.ttk as ttk

headings = ["Name", "Code", "Day", "Start time", "Duration", "Teacher"]


class Table:
    def __init__(self, window, column, x, y, widths, headings_counter = 0):

        self.table = ttk.Treeview(window, columns=column, show="headings")
        self.table.place(x=x, y=y)

        for heading_text in headings :
            headings_counter += 1
            self.table.heading(headings_counter, text=heading_text)
            self.table.column(headings_counter, width=widths)