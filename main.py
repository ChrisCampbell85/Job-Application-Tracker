from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from buttons import Create, Display, Positions, Search, Update, Delete
from interact_db import create_db
from configs import style_tbutton
"""
This is the base frame for the GUI
"""
toplevels = {'Create Application': Create, 'Display All': Display, 'Position Overview': Positions, 'Search Positions': Search, 'Update': Update, 'Delete': Delete}
app_title = 'Job Application Tracker'

class Homepage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both')
        # img = ImageTk.PhotoImage(Image.open("coal_harbour.jpg"))
        # Label(self, text=app_title, font='30').grid(row=0)
        self.create_buttons()
        self.quit_button(self)


    def create_buttons(self):
        style_tbutton()
        for title, cls in toplevels.items():
            ttk.Button(self, text=title, command=cls).pack(fill='both', padx=10, pady=1)
            

    def quit_button(self,frame):
        ttk.Button(frame, text='Quit', command=frame.quit).pack()


if __name__ == "__main__":
    create_db()
    root = Tk()
    root.title('Application Tracker')
    root.geometry('300x310')
    app = Homepage(master=root)
    app.mainloop()