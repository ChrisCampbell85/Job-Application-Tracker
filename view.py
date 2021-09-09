from tkinter import *
from funcs import toplevels
from interact_db import create_db
"""
This is the base frame for the GUI
"""

class Homepage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        Label(self, text='Job Application Tracker').grid(row=0)
        self.create_buttons()

    def create_buttons(self):
        for title, func in toplevels.items():
            Button(self, text=title, command=func).grid(sticky='we', ipady=10, ipadx=40)
            
        

if __name__ == "__main__":
    create_db(create=True)
    root = Tk()
    app = Homepage(master=root)
    app.mainloop()