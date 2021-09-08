from tkinter import *
from interact_db import *

""" Functions for button callbacks """

# save entries into SQLite db

# homepage CRUD button funcs
# need to pass in homepage frame

entrybox_labels = ['Company','Contact Details', 'Position', 'Hiring Platform', 'Date Applied']
entry_variables = []

class Create:
    def __init__(self):
        self.create()

    def create(self):
        frame = Toplevel()
        Label(frame, text='Enter Job Application').grid()
        self.create_entries(frame)
        self.save_entries(frame)
                
    def create_entries(self, frame):
        for title in entrybox_labels:
            if title != 'Date Applied':
                Label(frame, text=title).grid()
                entry_variable = StringVar()
                # add logic/formatting for date applied
                Entry(frame, textvariable=entry_variable).grid(ipadx=10)
                entry_variables.append(entry_variable)
            Label(frame, text=(entrybox_labels[-1])).grid()
            

    def save_entries(self, frame):
        Button(frame, text='Save', command=lambda: populate_db(entry_variables)).grid(row=11, sticky=SE)
        
# figure out how to do rowspans so info is side by side
class Read:
    def __init__(self):
        self.read()

    def read(self):
        frame = Toplevel()
        table = read_data_from_db()
        
class Update:
    def __init__(self):
        self.update()

    def update():
        frame = Toplevel()

class Delete:
    def __init__(self):
        self.delete()

    def delete():
        frame = Toplevel()

toplevels = {'Create': Create, 'Read': Read, 'Update': Update, 'Delete': Delete}

