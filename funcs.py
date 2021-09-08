from tkinter import *
from tkinter.scrolledtext import ScrolledText
from interact_db import populate_db, read_data_from_db
from tkcalendar import DateEntry

""" Functions for HomePage button callbacks """

entrybox_labels = ['Company','Contact Details', 'Position', 'Hiring Platform', 'Misc Details', 'Date Applied']
scrolledtext_variables = []
entry_variables = []
date_variables = []

class Create:
    """Creates Toplevel for application entry"""
    def __init__(self):
        self.create()

    def create(self):
        """Creates Toplevel for entries and Date Appiled and Save buttons"""
        frame = Toplevel()
        Label(frame, text='Enter Job Application').grid()
        self.create_entries(frame)
        self.save_entries(frame)
                
    def create_entries(self, frame):
        """Populates Toplevel frame of Create class"""
        for title in entrybox_labels:
            if title != entrybox_labels[-1]:
                Label(frame, text=title).grid()
                entry_variable = StringVar()
                if title == entrybox_labels[-2]:
                    scroll_text = ScrolledText(frame, width=30, height=10)
                    scroll_text.grid()
                    scrolledtext_variables.append(scroll_text)
                else:
                    Entry(frame, textvariable=entry_variable).grid(sticky='we')
                    entry_variables.append(entry_variable)
            else:
                Label(frame, text=entrybox_labels[-1]).grid()
                date_entry = DateEntry(frame)
                date_entry.grid()
                date_variables.append(date_entry)
                

    def save_entries(self, frame):
        """Button that saves entry objects to database"""
        button = Button(frame, text='Save', command=lambda: populate_db(self.convert()))
        button.grid(row=60, sticky=SE)


    def convert(self):
        """Converts all the entry objects to string for populate_db.py"""
        converted = []
        for item in entry_variables:
            converted.append(item.get())
        for item in scrolledtext_variables:
            converted.append(item.get('1.0', 'end-1c'))
        # date output converted to str, year/month/day
        for item in date_variables:
            converted.append(str(item.get_date()))

        return converted

        
# figure out how to do rowspans so info is side by side
class Read:
    def __init__(self):
        self.read()

    def read(self):
        frame = Toplevel()
        table = read_data_from_db()
        print(table)
        
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

