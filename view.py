from tkinter import *
from funcs import toplevels
from interact_db import *
"""
This is the base frame for the GUI
"""

class Homepage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        Label(self, text='Job Application Tracker').pack()
        self.create_buttons()

    def create_buttons(self):
        for title, func in toplevels.items():
            Button(self, text=title, command=func).pack(side=TOP)


if __name__ == "__main__":
    create_db()
    root = Tk()
    app = Homepage(master=root)
    app.mainloop()