from tkinter import *
# from tkinter.ttk import *
from PIL import ImageTk, Image
from funcs import Create, Read, Search, Update, Delete
from interact_db import create_db
"""
This is the base frame for the GUI
"""
toplevels = {'Create': Create, 'Display All': Read, 'Search': Search, 'Update': Update, 'Delete': Delete}
app_title = 'Job Application Tracker'

class Homepage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # img = ImageTk.PhotoImage(Image.open("coal_harbour.jpg"))
        Label(self, text=app_title, font='30').grid(row=0)
        self.create_buttons()
        self.quit_button(self)

    def create_buttons(self):
        for title, func in toplevels.items():
            Button(self, text=title, font='10', padx=100, command=func).grid(sticky='we', ipady=30, ipadx=40)

    def quit_button(self,frame):
        Button(frame, text='Quit', command=frame.quit).grid(row=60, sticky=SE)


if __name__ == "__main__":
    create_db()
    root = Tk()
    app = Homepage(master=root)
    app.mainloop()