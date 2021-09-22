from tkinter import *
from funcs import Create, Read, ReadSearch, Update, Delete
from interact_db import create_db
"""
This is the base frame for the GUI
"""
toplevels = {'Create': Create, 'Display All': Read,'Search': ReadSearch, 'Update': Update, 'Delete': Delete}

class Homepage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        Label(self, text='Job Application Tracker').grid(row=0)
        self.create_buttons()
        self.quit_button(self)

    def create_buttons(self):
        for title, func in toplevels.items():
            Button(self, text=title, command=func).grid(sticky='we', ipady=10, ipadx=40)

    # quit program
    def quit_button(self,frame):
        Button(frame, text='Quit', command=frame.quit).grid(row=60, sticky=SE)


if __name__ == "__main__":
    create_db()
    root = Tk()
    app = Homepage(master=root)
    app.mainloop()