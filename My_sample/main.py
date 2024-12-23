from tkinter import *
from label_entry_class import LabelAndEntryMaker
from table import Table
from lesson import Lesson
import tkinter.messagebox as msg

win = Tk()
win.title("Lesson")
win.geometry("950x400")

name_label = LabelAndEntryMaker(win, "Name", 20, 20, data_type="str")
code_label = LabelAndEntryMaker(win, "Code", 20, 50, data_type="int")
day_label = LabelAndEntryMaker(win, "Day", 20, 80, data_type="str")
start_time_label = LabelAndEntryMaker(win, "Start time", 20, 110, data_type="str")
duration_label = LabelAndEntryMaker(win, "Duration", 20, 140, data_type="int")
teacher_label = LabelAndEntryMaker(win, "Teacher", 20, 170, data_type="str")


def reset_form():
    name_label.variable.set("")
    code_label.variable.set(0)
    day_label.variable.set("")
    start_time_label.variable.set("")
    duration_label.variable.set(0)
    teacher_label.variable.set("")


my_table = Table(win, (1, 2, 3, 4, 5, 6), 300, 20, 100)


def save_click():
    try:
        lesson = Lesson(name_label.variable.get(), code_label.variable.get(), day_label.variable.get(),
                        start_time_label.variable.get(),
                        duration_label.variable.get(), teacher_label.variable.get())
        msg.showinfo("Save successful", "Lesson Saved")
        reset_form()
        my_table.table.insert("", END, values=lesson.to_tuple())
    except Exception as e:
        msg.showerror("Save Error", f"Error : {e}")


Button(text="Save", command=save_click, width=10).place(x=50, y=220)

win.mainloop()
