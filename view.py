from tkinter import *
from typing import List

"""
This is the base frame for the GUI
"""

# Company
# Contact Details (Optional)
# Position
# Date Applied
# Platform Applied on (LinkedIn etc)

entrybox_labels = ['Company','Contact Details', 'Position', 'Date Applied', 'Hiring Platform']

class Tracker(Frame):
    def __init__(self, master=None, entrybox_labels = []):
        super().__init__(master)
        self.master = master
        self.entrybox_labels = entrybox_labels
        self.entry_variables = []
        self.pack()

    def create_entries(self):
        for title in self.entrybox_labels:
            Label(self, text=title).pack(anchor=NW)
            entry_variable = StringVar()
            Entry(self, textvariable=entry_variable).pack(side=TOP)
            self.entry_variables.append(entry_variable)

root = Tk()
app = Tracker(root, entrybox_labels)
app.create_entries()
print(app.entry_variables)
app.mainloop()