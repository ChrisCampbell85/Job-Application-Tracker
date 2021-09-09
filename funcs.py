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
        converted_variables = []
        for item in entry_variables:
            converted_variables.append(item.get())
        for item in scrolledtext_variables:
            converted_variables.append(item.get('1.0', 'end-1c'))
        # date output converted to str, year/month/day
        for item in date_variables:
            converted_variables.append(str(item.get_date()))

        return converted_variables

        
# figure out how to do rowspans so info is side by side
class Read:
    def __init__(self):
        self.read()

    def read(self):
        """Displays current entries in database"""
        # add scroll functionality!
        frame = Toplevel()
        table = read_data_from_db()
        sorted_table = self.sort_db_table(table)
        for application in sorted_table:
            for label, entry in application.items():
                text_label = f'{label}: {entry}'
                Label(frame, text=text_label).grid(sticky=W)
        
    def sort_db_table(self, table):
        """Matches each entry label with entry data"""
        zipped_list = []
        for item in table:
            entry = dict((zip(entrybox_labels, item)))
            zipped_list.append(entry)

        return zipped_list

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

