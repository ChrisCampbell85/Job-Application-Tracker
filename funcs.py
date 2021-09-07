from tkinter import *
from interact_db import *

""" Functions for button callbacks """

# save entries into SQLite db

# homepage CRUD button funcs
# need to pass in homepage frame

entrybox_labels = ['Company','Contact Details', 'Position', 'Date Applied', 'Hiring Platform']
entry_variables = []

class Create:
    def __init__(self):
        self.create()

    def create(self):
        frame = Toplevel()
        Label(frame, text='Enter Job Application').pack()
        self.create_entries(frame)
        self.save_entries(frame)
                
    def create_entries(self, frame):
        for title in entrybox_labels:
            Label(frame, text=title).pack(anchor=NW)
            entry_variable = StringVar()
            # add logic/formatting for date applied
            Entry(frame, textvariable=entry_variable).pack(side=TOP)
            entry_variables.append(entry_variable)

    def save_entries(self, frame):
        Button(frame, text='Save', command=lambda: populate_db(entry_variables)).pack(anchor=SE)
        

def read():
    frame = Toplevel()

def update():
    frame = Toplevel()

def delete():
    frame = Toplevel()


# crud_classes =[CreateApplication, ReadApplication, UpdateApplication, DeleteApplication]
toplevels = {'Create': Create, 'Read': read, 'Update': update, 'Delete': delete}

